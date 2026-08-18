"""Testes unitários do retrieval (Sprint 8).

Valida que a consulta SQL usa o operador de similaridade cosseno (<=>) do
pgvector e que K vem exclusivamente da configuração central.
"""

from __future__ import annotations

import inspect
from unittest.mock import MagicMock, patch

import pytest

from app.config.chunking import TOP_K
from app.retrieval.vector_search import retrieve_top_k


def test_retrieve_top_k_uses_top_k_from_config():
    """K não é parâmetro de retrieve_top_k; vem da configuração central."""
    sig = inspect.signature(retrieve_top_k)
    assert "k" not in sig.parameters, "retrieve_top_k não deve aceitar parâmetro k"
    assert "question" in sig.parameters
    assert "db" in sig.parameters


def test_retrieve_top_k_passes_top_k_to_similarity_search():
    """retrieve_top_k repassa TOP_K fixo para similarity_search."""
    db = MagicMock()
    with (
        patch("app.retrieval.vector_search.embed_text", return_value=[0.1] * 1024) as mock_embed,
        patch("app.retrieval.vector_search.similarity_search", return_value=[]) as mock_search,
    ):
        retrieve_top_k(db, "o que é FastAPI?")

    mock_embed.assert_called_once_with("o que é FastAPI?")
    mock_search.assert_called_once()
    _, kwargs = mock_search.call_args
    assert kwargs.get("k") == TOP_K


def test_similarity_search_query_uses_cosine_operator():
    """A consulta SQL deve usar o operador <=> (distância cosseno do pgvector)."""
    from app.database.crud import similarity_search

    src = inspect.getsource(similarity_search)
    assert "<=>" in src, "consulta deve usar operador <=> do pgvector"
    assert "ORDER BY" in src
    assert "LIMIT" in src
    assert "embedding IS NOT NULL" in src


def test_similarity_search_returns_content_and_metadata():
    """O retorno deve incluir content, metadata e score."""
    from app.database.crud import similarity_search

    src = inspect.getsource(similarity_search)
    assert "content" in src
    assert "metadata" in src
    assert "score" in src
    assert "document_filename" in src


def test_top_k_is_frozen_constant():
    """TOP_K deve ser um valor inteiro positivo e estável."""
    assert isinstance(TOP_K, int)
    assert TOP_K > 0
    # Garante que é um valor congelado típico para RAG.
    assert TOP_K in (1, 2, 3, 5, 10)
