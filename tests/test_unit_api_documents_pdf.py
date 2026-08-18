"""Testes do endpoint GET /api/documents/pdf/{filename}."""

from __future__ import annotations

from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _pdf_bytes() -> bytes:
    return b"%PDF-1.4 teste"


def test_get_pdf_returns_file(tmp_path):
    pdf = tmp_path / "apostila.pdf"
    pdf.write_bytes(_pdf_bytes())
    with patch("app.api.routes.documents.PDF_DIR", tmp_path):
        response = client.get("/api/documents/pdf/apostila.pdf")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content == _pdf_bytes()


def test_get_pdf_404_when_missing(tmp_path):
    with patch("app.api.routes.documents.PDF_DIR", tmp_path):
        response = client.get("/api/documents/pdf/nao-existe.pdf")

    assert response.status_code == 404


def test_get_pdf_404_on_path_traversal(tmp_path):
    with patch("app.api.routes.documents.PDF_DIR", tmp_path):
        response = client.get("/api/documents/pdf/../../.env")

    assert response.status_code == 404


def test_get_pdf_404_on_non_pdf(tmp_path):
    md = tmp_path / "nota.md"
    md.write_text("# teste")
    with patch("app.api.routes.documents.PDF_DIR", tmp_path):
        response = client.get("/api/documents/pdf/nota.md")

    assert response.status_code == 404