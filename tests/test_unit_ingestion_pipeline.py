"""Testes unitários do pipeline de ingestão integrado."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from app.ingestion.pipeline import (
    IngestionError,
    UnsupportedFileError,
    detect_type,
    ingest_file,
)


def test_detect_type_pdf():
    assert detect_type(Path("aula.pdf")) == "pdf"


def test_detect_type_markdown():
    assert detect_type(Path("aula.md")) == "markdown"


def test_detect_type_mp3():
    assert detect_type(Path("aula-00.mp3")) == "audio"


def test_detect_type_mp4():
    assert detect_type(Path("aula-00.mp4")) == "audio"


def test_detect_type_unsupported_raises():
    with pytest.raises(UnsupportedFileError, match="suportada"):
        detect_type(Path("arquivo.txt"))


def test_detect_type_case_insensitive():
    assert detect_type(Path("Aula.PDF")) == "pdf"
    assert detect_type(Path("AULA.MD")) == "markdown"


def test_ingest_file_missing_file_raises(tmp_path):
    db = MagicMock()
    with pytest.raises(IngestionError, match="encontrado"):
        ingest_file(db, tmp_path / "inexistente.pdf")


def test_ingest_file_unsupported_extension_raises(tmp_path):
    db = MagicMock()
    arquivo = tmp_path / "dados.txt"
    arquivo.write_text("conteudo")
    with pytest.raises(UnsupportedFileError):
        ingest_file(db, arquivo)


def test_ingest_file_markdown_pipeline_calls_extract_chunk_embed(tmp_path):
    md = tmp_path / "aula.md"
    md.write_text("# Teste\n\nConteudo de teste.")

    db = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = None

    with (
        patch("app.ingestion.pipeline.extract_markdown", return_value=[{"content": "Conteudo", "metadata": {"section": "raiz"}}]) as mock_extract,
        patch("app.ingestion.pipeline.chunk_markdown_blocks", return_value=[{"content": "Conteudo", "metadata": {}}]) as mock_chunk,
        patch("app.ingestion.pipeline.embed_text", return_value=[0.1] * 1024) as mock_embed,
    ):
        result = ingest_file(db, md)

    mock_extract.assert_called_once()
    mock_chunk.assert_called_once()
    assert mock_embed.call_count == 1
    assert result["type"] == "markdown"
    assert result["chunks"] == 1
    db.add.assert_called()
    db.commit.assert_called()


def test_ingest_file_idempotent_replaces_existing(tmp_path):
    md = tmp_path / "aula.md"
    md.write_text("# Teste\n\nConteudo de teste.")

    existing_doc = MagicMock()
    existing_doc.id = "doc-velho"

    db = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = existing_doc

    with (
        patch("app.ingestion.pipeline.extract_markdown", return_value=[{"content": "X", "metadata": {}}]),
        patch("app.ingestion.pipeline.chunk_markdown_blocks", return_value=[{"content": "X", "metadata": {}}]),
        patch("app.ingestion.pipeline.embed_text", return_value=[0.0] * 1024),
        patch("app.ingestion.pipeline.delete_document_and_chunks") as mock_delete,
    ):
        ingest_file(db, md)

    mock_delete.assert_called_once_with(db, "doc-velho")


def test_ingest_file_audio_requires_transcript(tmp_path):
    mp3 = tmp_path / "aula-99.mp3"
    mp3.write_bytes(b"fake audio")
    db = MagicMock()
    with pytest.raises(IngestionError, match="transcri"):
        ingest_file(db, mp3)
