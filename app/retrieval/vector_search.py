"""Busca vetorial Top-K no PostgreSQL + pgvector.

K é fixo e vem exclusivamente da configuração central (app.config.chunking.TOP_K),
garantindo reprodutibilidade experimental (RNF-06).
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.config.chunking import TOP_K
from app.database.crud import similarity_search
from app.embeddings.bedrock import embed_text


def retrieve_top_k(
    db: Session,
    question: str,
) -> list[dict]:
    """Gera embedding da pergunta e recupera os Top-K chunks mais similares.

    K é fixo (TOP_K da configuração central) e não pode ser alterado por chamada.

    Args:
        db: sessão do SQLAlchemy.
        question: pergunta em linguagem natural.

    Returns:
        Lista de chunks com score de similaridade e metadados de origem.
    """
    embedding = embed_text(question)
    return similarity_search(db, embedding, k=TOP_K)
