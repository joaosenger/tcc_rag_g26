"""Testes unitários das funções puras do frontend (Sprint 10)."""

from __future__ import annotations

from frontend.utils import (
    INSUFFICIENT_KEYWORDS,
    format_source,
    format_sources_display,
    is_insufficient_evidence,
)


def _sample_source(doc_type: str = "pdf") -> dict:
    return {
        "document_filename": "apostila.pdf",
        "document_type": doc_type,
        "content": "FastAPI é um framework moderno para APIs em Python.",
        "metadata": {"type": "pdf", "page": 5, "section": "Introdução"},
        "score": 0.92,
    }


def test_format_source_pdf_with_page_and_section():
    source = _sample_source("pdf")
    result = format_source(source)
    assert "apostila.pdf" in result
    assert "(pdf)" in result
    assert "p. 5" in result
    assert "seção: Introdução" in result
    assert "score: 0.9200" in result
    assert "FastAPI" in result


def test_format_source_audio_with_timestamps():
    source = {
        "document_filename": "aula-00.mp3",
        "document_type": "audio",
        "content": "Transcrição sobre rede.",
        "metadata": {"type": "audio", "start": "00:01:23", "end": "00:01:58"},
        "score": 0.78,
    }
    result = format_source(source)
    assert "aula-00.mp3" in result
    assert "(audio)" in result
    assert "tempo: 00:01:23 - 00:01:58" in result
    assert "p." not in result


def test_format_source_markdown_with_section_only():
    source = {
        "document_filename": "aula-01.md",
        "document_type": "markdown",
        "content": "Conteúdo sobre servidores.",
        "metadata": {"type": "markdown", "section": "Servidores"},
        "score": 0.85,
    }
    result = format_source(source)
    assert "aula-01.md" in result
    assert "(markdown)" in result
    assert "seção: Servidores" in result
    assert "p." not in result
    assert "tempo:" not in result


def test_format_source_unknown_filename():
    source = {
        "document_filename": "",
        "document_type": "",
        "content": "Texto.",
        "metadata": {},
        "score": 0.0,
    }
    result = format_source(source)
    assert "desconhecido" in result


def test_format_source_truncates_long_content():
    source = {
        "document_filename": "doc.pdf",
        "document_type": "pdf",
        "content": "A" * 300,
        "metadata": {},
        "score": 0.5,
    }
    result = format_source(source)
    assert "..." in result
    assert len(result) < 400


def test_format_sources_display_empty_returns_empty():
    assert format_sources_display([]) == ""


def test_format_sources_display_multiple_sources():
    sources = [_sample_source(), _sample_source(), _sample_source()]
    result = format_sources_display(sources)
    assert "[1]" in result
    assert "[2]" in result
    assert "[3]" in result
    assert "---" in result


def test_is_insufficient_evidence_detects_keywords():
    assert is_insufficient_evidence("A evidência disponível é insuficiente.") is True
    assert is_insufficient_evidence("Não contém informação suficiente.") is True
    assert is_insufficient_evidence("Não encontrei informações relevantes.") is True


def test_is_insufficient_evidence_normal_answer_returns_false():
    assert is_insufficient_evidence("FastAPI é um framework Python.") is False
    assert is_insufficient_evidence("O PostgreSQL usa pgvector.") is False


def test_is_insufficient_evidence_empty_returns_false():
    assert is_insufficient_evidence("") is False
    assert is_insufficient_evidence(None) is False


def test_insufficient_keywords_not_empty():
    assert len(INSUFFICIENT_KEYWORDS) > 0
    assert all(isinstance(kw, str) for kw in INSUFFICIENT_KEYWORDS)
