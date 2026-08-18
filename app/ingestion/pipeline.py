"""Pipeline integrado de ingestão: arquivo → chunks → embeddings → PostgreSQL."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

from app.database.crud import (
    create_chunks,
    create_document,
    delete_document_and_chunks,
    get_document_by_filename,
)
from app.embeddings.bedrock import embed_text
from app.ingestion.chunking import (
    chunk_audio_segments,
    chunk_markdown_blocks,
    chunk_pdf_blocks,
)
from app.ingestion.markdown import extract_markdown
from app.ingestion.pdf import extract_pdf

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {".pdf", ".md", ".mp3", ".mp4"}


class IngestionError(Exception):
    pass


class UnsupportedFileError(IngestionError):
    pass


def detect_type(path: Path) -> str:
    """Detecta o tipo de documento pela extensão."""
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "pdf"
    if ext == ".md":
        return "markdown"
    if ext in {".mp3", ".mp4"}:
        return "audio"
    raise UnsupportedFileError(f"extensão não suportada: {ext}")


def _extract_blocks(path: Path, doc_type: str) -> list[dict[str, Any]]:
    """Extrai blocos de conteúdo de acordo com o tipo."""
    if doc_type == "pdf":
        return extract_pdf(path, fast=True)
    if doc_type == "markdown":
        return extract_markdown(path)
    if doc_type == "audio":
        # Espera transcrição prévia em content/audio/transcriptions/<stem>.json
        transcript_path = (
            Path("content/audio/transcriptions") / f"{path.stem}.json"
        )
        if not transcript_path.exists():
            raise IngestionError(
                f"transcrição não encontrada para {path.name}: {transcript_path}"
            )
        with open(transcript_path, "r", encoding="utf-8") as f:
            transcript = json.load(f)
        return transcript.get("segments", [])
    raise IngestionError(f"tipo desconhecido: {doc_type}")


def _chunk_blocks(
    blocks: list[dict[str, Any]], doc_type: str, source: Path
) -> list[dict[str, Any]]:
    """Fragmenta os blocos extraídos em chunks."""
    if doc_type == "pdf":
        return chunk_pdf_blocks(blocks, source)
    if doc_type == "markdown":
        return chunk_markdown_blocks(blocks, source)
    if doc_type == "audio":
        return chunk_audio_segments(blocks, source)
    raise IngestionError(f"tipo desconhecido: {doc_type}")


def _embed_chunks(chunks: list[dict[str, Any]], batch_size: int = 8) -> list[dict[str, Any]]:
    """Gera embeddings para os chunks em lotes."""
    result = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        for chunk in batch:
            embedding = embed_text(chunk["content"])
            result.append({**chunk, "embedding": embedding})
    return result


def ingest_file(
    db: Session,
    file_path: str | Path,
    batch_size: int = 8,
) -> dict[str, Any]:
    """Ingere um arquivo no pipeline RAG.

    O processo é idempotente: se o arquivo já foi ingerido, o documento e seus
    chunks antigos são removidos antes de recriar.

    Args:
        db: sessão do SQLAlchemy.
        file_path: caminho do arquivo local.
        batch_size: tamanho do lote para geração de embeddings.

    Returns:
        Dicionário com document_id, type e quantidade de chunks.
    """
    source = Path(file_path)
    if not source.exists():
        raise IngestionError(f"arquivo não encontrado: {source}")

    doc_type = detect_type(source)

    # Idempotência: remove documento e chunks anteriores, se existirem.
    existing = get_document_by_filename(db, source.name)
    if existing:
        logger.info("Reingestão de %s (documento %s)", source.name, existing.id)
        delete_document_and_chunks(db, existing.id)

    logger.info("Extraindo blocos de %s", source.name)
    blocks = _extract_blocks(source, doc_type)
    if not blocks:
        raise IngestionError(f"nenhum conteúdo extraído de {source.name}")

    logger.info("Criando chunks de %s", source.name)
    chunks = _chunk_blocks(blocks, doc_type, source)
    if not chunks:
        raise IngestionError(f"nenhum chunk gerado para {source.name}")

    logger.info("Gerando embeddings para %d chunks de %s", len(chunks), source.name)
    chunks_with_embedding = _embed_chunks(chunks, batch_size=batch_size)

    document = create_document(
        db,
        filename=source.name,
        doc_type=doc_type,
        metadata={"source_path": str(source)},
    )
    create_chunks(db, document.id, chunks_with_embedding)

    logger.info(
        "Ingestão concluída: %s -> %d chunks (document_id=%s)",
        source.name,
        len(chunks_with_embedding),
        document.id,
    )

    return {
        "document_id": document.id,
        "filename": source.name,
        "type": doc_type,
        "chunks": len(chunks_with_embedding),
    }
