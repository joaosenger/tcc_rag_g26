"""Testes unitários do prompt e formatação de fontes (Sprint 9).

Valida que o prompt segue as regras da seção 13 do PRD:
1. Responder exclusivamente com base no contexto.
2. Citar fontes (documento/página/seção/tempo).
3. Sinalizar evidência insuficiente.
4. Proibir conhecimento externo.
5. Responder em português do Brasil.
"""

from __future__ import annotations

from app.llm.prompt import (
    SYSTEM_PROMPT,
    build_prompt,
    format_source_label,
    format_sources,
)


def _sample_chunks() -> list[dict]:
    return [
        {
            "document_filename": "apostila.pdf",
            "document_type": "pdf",
            "content": "FastAPI é um framework para APIs em Python.",
            "metadata": {"type": "pdf", "page": 5, "section": "Introdução"},
            "score": 0.92,
        },
        {
            "document_filename": "aula-01.md",
            "document_type": "markdown",
            "content": "O Uvicorn é o servidor de aplicação.",
            "metadata": {"type": "markdown", "section": "Servidores"},
            "score": 0.85,
        },
        {
            "document_filename": "aula-00.mp3",
            "document_type": "audio",
            "content": "Transcrição sobre rede e HTTP.",
            "metadata": {"type": "audio", "start": "00:01:23", "end": "00:01:58"},
            "score": 0.78,
        },
    ]


def test_build_prompt_contains_question():
    chunks = _sample_chunks()
    prompt = build_prompt("O que é FastAPI?", chunks)
    assert "Pergunta: O que é FastAPI?" in prompt


def test_build_prompt_contains_context_content():
    chunks = _sample_chunks()
    prompt = build_prompt("O que é FastAPI?", chunks)
    assert "FastAPI é um framework para APIs em Python." in prompt
    assert "O Uvicorn é o servidor de aplicação." in prompt


def test_build_prompt_contains_insuficiency_instruction():
    chunks = _sample_chunks()
    prompt = build_prompt("O que é FastAPI?", chunks)
    assert "insuficiente" in prompt.lower()
    assert "evidência" in prompt.lower() or "evidencia" in prompt.lower()


def test_build_prompt_contains_no_external_knowledge_instruction():
    chunks = _sample_chunks()
    prompt = build_prompt("O que é FastAPI?", chunks)
    assert "EXCLUSIVAMENTE" in prompt or "exclusivamente" in prompt.lower()
    assert "conhecimento externo" in prompt.lower() or "paramétrico" in prompt.lower()


def test_build_prompt_contains_portuguese_instruction():
    assert "português do Brasil" in SYSTEM_PROMPT


def test_build_prompt_contains_sources_block():
    chunks = _sample_chunks()
    prompt = build_prompt("O que é FastAPI?", chunks)
    assert "Fontes:" in prompt
    assert "[1]" in prompt
    assert "[2]" in prompt
    assert "[3]" in prompt


def test_format_source_label_with_page():
    chunk = {
        "document_filename": "apostila.pdf",
        "metadata": {"page": 12, "section": "Capítulo 2"},
    }
    label = format_source_label(1, chunk)
    assert "[1] apostila.pdf" in label
    assert "p. 12" in label
    assert "seção: Capítulo 2" in label


def test_format_source_label_with_section_only():
    chunk = {
        "document_filename": "aula-01.md",
        "metadata": {"section": "Introdução > Redes"},
    }
    label = format_source_label(2, chunk)
    assert "[2] aula-01.md" in label
    assert "seção: Introdução > Redes" in label
    assert "p." not in label


def test_format_source_label_with_timestamps():
    chunk = {
        "document_filename": "aula-00.mp3",
        "metadata": {"start": "00:05:30", "end": "00:06:15"},
    }
    label = format_source_label(3, chunk)
    assert "[3] aula-00.mp3" in label
    assert "tempo: 00:05:30 - 00:06:15" in label


def test_format_source_label_with_no_metadata():
    chunk = {
        "document_filename": "doc.txt",
        "metadata": {},
    }
    label = format_source_label(1, chunk)
    assert label == "[1] doc.txt"


def test_format_source_label_with_unknown_filename():
    chunk = {"metadata": {}}
    label = format_source_label(1, chunk)
    assert "desconhecido" in label


def test_format_sources_returns_list():
    chunks = _sample_chunks()
    sources = format_sources(chunks)
    assert isinstance(sources, list)
    assert len(sources) == 3
    assert all(isinstance(s, str) for s in sources)


def test_build_prompt_with_empty_chunks():
    prompt = build_prompt("Pergunta?", [])
    assert "Pergunta: Pergunta?" in prompt
    assert "Fontes:" in prompt


def test_build_prompt_contains_all_four_prd_rules():
    chunks = _sample_chunks()
    prompt = build_prompt("Teste?", chunks)
    # Regra 1: exclusivamente contexto
    assert "contexto" in prompt.lower()
    # Regra 2: citar fontes
    assert "fontes" in prompt.lower()
    # Regra 3: insuficiência
    assert "insuficiente" in prompt.lower()
    # Regra 4: português do Brasil
    assert "português" in prompt.lower()
