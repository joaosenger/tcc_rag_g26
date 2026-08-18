from pathlib import Path

import pytest

from app.config.chunking import CHUNK_SIZE
from app.ingestion.chunking import (
    chunk_audio_segments,
    chunk_markdown_blocks,
    chunk_pdf_blocks,
    chunk_text,
)


def _generate_text(size: int, word: str = "palavra") -> str:
    return " ".join([word] * size)


def test_chunk_text_splits_large_text_and_preserves_metadata():
    text = _generate_text(CHUNK_SIZE * 2)
    metadata = {"type": "pdf", "source": "doc.pdf", "page": 1}
    chunks = chunk_text(text, metadata)

    assert len(chunks) > 1
    joined = " ".join(c["content"] for c in chunks)
    # O RecursiveCharacterTextSplitter insere overlap entre chunks, então a
    # contagem final pode ser maior; garantimos que nenhuma palavra foi perdida.
    assert joined.count("palavra") >= CHUNK_SIZE * 2
    for chunk in chunks:
        assert chunk["metadata"]["type"] == "pdf"
        assert chunk["metadata"]["source"] == "doc.pdf"
        assert chunk["metadata"]["page"] == 1


def test_chunk_text_returns_empty_for_blank_text():
    assert chunk_text("") == []
    assert chunk_text("   \n\n  ") == []


def test_small_text_generates_single_chunk():
    text = "Texto curto que cabe em um único chunk."
    chunks = chunk_text(text, {"source": "x.txt"})
    assert len(chunks) == 1
    assert chunks[0]["content"] == text


def test_chunk_pdf_blocks_preserves_page_and_heading():
    blocks = [
        {
            "content": "Introdução ao tema principal. " + _generate_text(CHUNK_SIZE),
            "metadata": {"page": 1, "heading": "Introdução"},
        },
        {
            "content": "Detalhes avançados. " + _generate_text(CHUNK_SIZE),
            "metadata": {"page": 2, "heading": "Avançado"},
        },
    ]
    chunks = chunk_pdf_blocks(blocks, "apostila.pdf")

    assert len(chunks) > 2
    pages = {c["metadata"]["page"] for c in chunks}
    assert pages == {1, 2}

    headings = {c["metadata"]["section"] for c in chunks}
    assert "Introdução" in headings
    assert "Avançado" in headings

    for chunk in chunks:
        assert chunk["metadata"]["type"] == "pdf"
        assert chunk["metadata"]["filename"] == "apostila.pdf"


def test_chunk_markdown_blocks_preserves_section_path():
    blocks = [
        {
            "content": "Conteúdo da introdução. " + _generate_text(CHUNK_SIZE),
            "metadata": {"section": "Aula 01 > Introdução", "title": "Aula 01"},
        }
    ]
    chunks = chunk_markdown_blocks(blocks, "aulas/01.md")

    assert len(chunks) >= 1
    for chunk in chunks:
        assert chunk["metadata"]["type"] == "markdown"
        assert chunk["metadata"]["section"] == "Aula 01 > Introdução"
        assert chunk["metadata"]["title"] == "Aula 01"
        assert chunk["metadata"]["filename"] == "01.md"


def test_chunk_audio_segments_groups_consecutive_segments():
    segments = [
        {"text": "Primeira frase.", "start": 0.0, "end": 2.0},
        {"text": "Segunda frase.", "start": 2.5, "end": 5.0},
        {"text": "Terceira frase.", "start": 5.5, "end": 8.0},
    ]
    chunks = chunk_audio_segments(segments, "aula-00.mp3")

    assert len(chunks) >= 1
    first = chunks[0]
    assert first["metadata"]["type"] == "audio"
    assert first["metadata"]["filename"] == "aula-00.mp3"
    assert first["metadata"]["start"] == "00:00:00"

    joined = " ".join(c["content"] for c in chunks)
    assert "Primeira frase." in joined
    assert "Segunda frase." in joined
    assert "Terceira frase." in joined


def test_chunk_audio_segments_splits_on_large_gap():
    segments = [
        {"text": "Antes da pausa.", "start": 0.0, "end": 2.0},
        {"text": "Depois da pausa.", "start": 10.0, "end": 12.0},
    ]
    chunks = chunk_audio_segments(segments, "aula-01.mp3")

    assert len(chunks) == 2
    assert chunks[0]["metadata"]["end"] == "00:00:02"
    assert chunks[1]["metadata"]["start"] == "00:00:10"


def test_chunk_audio_segments_respects_target_size():
    # Cria segmentos suficientemente grandes para forçar múltiplos chunks.
    segments = [
        {"text": _generate_text(CHUNK_SIZE // 2), "start": float(i), "end": float(i) + 1.0}
        for i in range(10)
    ]
    chunks = chunk_audio_segments(segments, "aula-02.mp3")

    assert len(chunks) > 1
    for chunk in chunks:
        assert chunk["metadata"]["type"] == "audio"
