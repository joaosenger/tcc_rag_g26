"""Teste unitário do endpoint POST /api/chat com mocks (Sprint 9).

Valida que o endpoint responde com resposta + fontes quando o retrieval e o
LLM são mockados.
"""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _mock_chunks() -> list[dict]:
    return [
        {
            "chunk_id": "chunk-1",
            "document_id": "doc-1",
            "document_filename": "apostila.pdf",
            "document_type": "pdf",
            "content": "FastAPI é um framework moderno para APIs em Python.",
            "metadata": {"type": "pdf", "page": 5, "section": "Introdução"},
            "score": 0.92,
        }
    ]


def test_chat_returns_answer_and_sources():
    with (
        patch("app.api.routes.chat.retrieve_top_k", return_value=_mock_chunks()),
        patch("app.api.routes.chat.generate", return_value="FastAPI é um framework Python."),
    ):
        response = client.post("/api/chat", json={"question": "O que é FastAPI?"})

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert data["answer"] == "FastAPI é um framework Python."
    assert len(data["sources"]) == 1
    assert data["sources"][0]["document_filename"] == "apostila.pdf"
    assert data["sources"][0]["metadata"]["page"] == 5
    assert data["sources"][0]["score"] == 0.92


def test_chat_returns_insuficient_evidence_when_no_chunks():
    with patch("app.api.routes.chat.retrieve_top_k", return_value=[]):
        response = client.post("/api/chat", json={"question": "Pergunta sem contexto."})

    assert response.status_code == 200
    data = response.json()
    assert "insuficiente" in data["answer"].lower()
    assert data["sources"] == []


def test_chat_returns_500_on_error():
    with patch("app.api.routes.chat.retrieve_top_k", side_effect=RuntimeError("boom")):
        response = client.post("/api/chat", json={"question": "erro"})

    assert response.status_code == 500
    assert "falha" in response.json()["detail"].lower()
