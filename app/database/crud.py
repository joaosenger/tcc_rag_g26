"""Operações de CRUD e busca vetorial para documents e chunks."""

from __future__ import annotations

import logging
from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config.chunking import EMBEDDING_DIMENSION, TOP_K
from app.database.models import Chunk, Document

logger = logging.getLogger(__name__)


def get_document_by_filename(db: Session, filename: str) -> Document | None:
    """Busca um documento pelo nome do arquivo."""
    return db.query(Document).filter(Document.filename == filename).first()


def create_document(
    db: Session,
    filename: str,
    doc_type: str,
    metadata: dict[str, Any] | None = None,
) -> Document:
    """Cria um novo documento."""
    document = Document(
        filename=filename,
        type=doc_type,
        metadata_=metadata or {},
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def delete_document_and_chunks(db: Session, document_id: str) -> None:
    """Remove um documento e todos os seus chunks (idempotência)."""
    db.query(Chunk).filter(Chunk.document_id == document_id).delete()
    db.query(Document).filter(Document.id == document_id).delete()
    db.commit()


def create_chunks(db: Session, document_id: str, chunks: list[dict[str, Any]]) -> int:
    """Insere chunks em lote vinculados a um documento.

    Args:
        db: sessão do SQLAlchemy.
        document_id: ID do documento pai.
        chunks: lista de {"content": str, "metadata": dict, "embedding": list[float]}.

    Returns:
        Número de chunks inseridos.
    """
    if not chunks:
        return 0

    db_chunks = [
        Chunk(
            document_id=document_id,
            content=chunk["content"],
            metadata_=chunk.get("metadata", {}),
            embedding=chunk.get("embedding"),
        )
        for chunk in chunks
    ]
    db.add_all(db_chunks)
    db.commit()
    return len(db_chunks)


def similarity_search(
    db: Session,
    embedding: list[float],
    k: int = TOP_K,
) -> list[dict[str, Any]]:
    """Busca os k chunks mais similares por similaridade cosseno.

    Args:
        db: sessão do SQLAlchemy.
        embedding: vetor de consulta.
        k: número de resultados.

    Returns:
        Lista de dicionários com content, metadata, document_id e score.
    """
    # Usa <=> (distance) do pgvector: menor distância = mais similar.
    # 1 - distance = similaridade cosseno.
    query = text(
        f"""
        SELECT
            c.id,
            c.document_id,
            d.filename AS document_filename,
            d.type AS document_type,
            c.content,
            c.metadata,
            1 - (c.embedding <=> :embedding) AS score
        FROM chunks c
        JOIN documents d ON d.id = c.document_id
        WHERE c.embedding IS NOT NULL
        ORDER BY c.embedding <=> :embedding
        LIMIT :k
        """
    )

    result = db.execute(
        query,
        {"embedding": str(embedding), "k": k},
    ).mappings()

    return [
        {
            "chunk_id": row["id"],
            "document_id": row["document_id"],
            "document_filename": row["document_filename"],
            "document_type": row["document_type"],
            "content": row["content"],
            "metadata": row["metadata"],
            "score": row["score"],
        }
        for row in result
    ]
