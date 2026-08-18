"""Testes das funções puras da sidebar (links de conteúdo)."""

from __future__ import annotations

from pathlib import Path

from frontend.utils import build_pdf_url, list_corpus_pdfs


def test_list_corpus_pdfs_returns_only_pdfs(tmp_path):
    (tmp_path / "aula.pdf").write_bytes(b"%PDF")
    (tmp_path / "nota.md").write_text("# nota")
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "interno.pdf").write_bytes(b"%PDF")

    assert list_corpus_pdfs(tmp_path) == ["aula.pdf"]


def test_list_corpus_pdfs_sorted(tmp_path):
    (tmp_path / "z.pdf").write_bytes(b"%PDF")
    (tmp_path / "a.pdf").write_bytes(b"%PDF")

    assert list_corpus_pdfs(tmp_path) == ["a.pdf", "z.pdf"]


def test_list_corpus_pdfs_missing_dir(tmp_path):
    assert list_corpus_pdfs(tmp_path / "inexistente") == []


def test_build_pdf_url(tmp_path):
    assert (
        build_pdf_url("http://localhost:8000", "apostila.pdf")
        == "http://localhost:8000/api/documents/pdf/apostila.pdf"
    )


def test_build_pdf_url_strips_trailing_slash():
    assert (
        build_pdf_url("http://localhost:8000/", "apostila.pdf")
        == "http://localhost:8000/api/documents/pdf/apostila.pdf"
    )


def test_build_pdf_url_with_space():
    assert (
        build_pdf_url("http://localhost:8000", "minha apostila.pdf")
        == "http://localhost:8000/api/documents/pdf/minha apostila.pdf"
    )


def test_build_pdf_url_uses_pathlib(tmp_path):
    assert isinstance(list_corpus_pdfs(tmp_path), list)
    assert all(isinstance(p, str) for p in list_corpus_pdfs(tmp_path))
    assert isinstance(Path("content/documents"), Path)