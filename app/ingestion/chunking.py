"""Chunking semântico/hierárquico para PDF, Markdown e transcrições de áudio.

Todos os splitters usam as constantes centralizadas em app.config.chunking
para garantir reprodutibilidade experimental.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from app.config.chunking import (
    AUDIO_CHUNK_TARGET_SIZE,
    AUDIO_JOIN_MAX_GAP_SECONDS,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    SEPARATORS,
)

logger = logging.getLogger(__name__)


def _base_splitter() -> RecursiveCharacterTextSplitter:
    """Cria um RecursiveCharacterTextSplitter padronizado."""
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=SEPARATORS,
        length_function=len,
        is_separator_regex=False,
    )


def chunk_text(text: str, metadata: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """Fragmenta um texto genérico em chunks preservando metadados.

    Args:
        text: texto a ser fragmentado.
        metadata: metadados de origem a replicar em cada chunk.

    Returns:
        Lista de dicionários {"content": str, "metadata": dict}.
    """
    if not text or not text.strip():
        return []

    splitter = _base_splitter()
    docs = splitter.create_documents([text], metadatas=[metadata or {}])
    return [{"content": doc.page_content, "metadata": doc.metadata} for doc in docs]


def chunk_pdf_blocks(
    blocks: list[dict[str, Any]],
    source: str | Path,
) -> list[dict[str, Any]]:
    """Fragmenta blocos extraídos de PDF garantindo metadados de página e seção.

    Args:
        blocks: saída de app.ingestion.pdf.extract_pdf.
        source: caminho/nome do arquivo de origem.

    Returns:
        Lista de chunks com metadados unificados.
    """
    splitter = _base_splitter()
    chunks: list[dict[str, Any]] = []

    for block in blocks:
        content = block.get("content", "")
        meta = block.get("metadata", {})
        if not content or not content.strip():
            continue

        base_meta = {
            "type": "pdf",
            "source": str(source),
            "filename": Path(source).name,
            "page": meta.get("page"),
            "section": meta.get("heading"),
        }

        docs = splitter.create_documents([content], metadatas=[base_meta])
        chunks.extend(
            {"content": doc.page_content, "metadata": doc.metadata} for doc in docs
        )

    return chunks


def chunk_markdown_blocks(
    blocks: list[dict[str, Any]],
    source: str | Path,
) -> list[dict[str, Any]]:
    """Fragmenta blocos extraídos de Markdown preservando hierarquia de seções.

    Args:
        blocks: saída de app.ingestion.markdown.extract_markdown.
        source: caminho/nome do arquivo de origem.

    Returns:
        Lista de chunks com metadados unificados.
    """
    splitter = _base_splitter()
    chunks: list[dict[str, Any]] = []

    for block in blocks:
        content = block.get("content", "")
        meta = block.get("metadata", {})
        if not content or not content.strip():
            continue

        base_meta = {
            "type": "markdown",
            "source": str(source),
            "filename": Path(source).name,
            "section": meta.get("section"),
            "title": meta.get("title"),
        }

        docs = splitter.create_documents([content], metadatas=[base_meta])
        chunks.extend(
            {"content": doc.page_content, "metadata": doc.metadata} for doc in docs
        )

    return chunks


def chunk_markdown_text(
    text: str,
    source: str | Path,
    title: str | None = None,
) -> list[dict[str, Any]]:
    """Fragmenta texto Markdown puro usando split hierárquico por headers.

    Útil quando o arquivo Markdown ainda não passou por extract_markdown.
    """
    if not text or not text.strip():
        return []

    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "header_1"), ("##", "header_2"), ("##", "header_3")]
    )
    header_docs = header_splitter.split_text(text)

    splitter = _base_splitter()
    chunks: list[dict[str, Any]] = []

    for doc in header_docs:
        section_path = " > ".join(
            str(v) for k, v in sorted(doc.metadata.items()) if k.startswith("header_")
        )
        base_meta = {
            "type": "markdown",
            "source": str(source),
            "filename": Path(source).name,
            "section": section_path or "raiz",
            "title": title,
        }

        sub_docs = splitter.create_documents([doc.page_content], metadatas=[base_meta])
        chunks.extend(
            {"content": d.page_content, "metadata": d.metadata} for d in sub_docs
        )

    return chunks


def chunk_audio_segments(
    segments: list[dict[str, Any]],
    source: str | Path,
) -> list[dict[str, Any]]:
    """Fragmenta segmentos Whisper agrupando segmentos consecutivos.

    Args:
        segments: lista de segmentos do JSON de transcrição (campo 'segments').
        source: caminho/nome do arquivo de origem.

    Returns:
        Lista de chunks com metadados de timestamp início/fim.
    """
    chunks: list[dict[str, Any]] = []
    buffer_texts: list[str] = []
    start_time: float | None = None
    end_time: float | None = None
    last_end: float | None = None

    def _flush() -> None:
        nonlocal buffer_texts, start_time, end_time
        if not buffer_texts:
            return
        content = " ".join(buffer_texts).strip()
        if content:
            chunks.append(
                {
                    "content": content,
                    "metadata": {
                        "type": "audio",
                        "source": str(source),
                        "filename": Path(source).name,
                        "start": _format_timestamp(start_time or 0.0),
                        "end": _format_timestamp(end_time or 0.0),
                    },
                }
            )
        buffer_texts = []
        start_time = None
        end_time = None

    for segment in segments:
        text = segment.get("text", "").strip()
        if not text:
            continue

        seg_start = segment.get("start", 0.0)
        seg_end = segment.get("end", seg_start)

        # Decide se inicia um novo chunk: se buffer atingiu o tamanho alvo
        # ou se há uma pausa grande demais entre segmentos.
        current_len = sum(len(t) for t in buffer_texts)
        gap = (
            (seg_start - last_end)
            if last_end is not None and seg_start >= last_end
            else 0.0
        )

        if buffer_texts and (
            current_len + len(text) > AUDIO_CHUNK_TARGET_SIZE
            or gap > AUDIO_JOIN_MAX_GAP_SECONDS
        ):
            _flush()

        if start_time is None:
            start_time = seg_start
        end_time = seg_end
        buffer_texts.append(text)
        last_end = seg_end

    _flush()
    return chunks


def _format_timestamp(seconds: float) -> str:
    """Formata segundos no formato HH:MM:SS."""
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
