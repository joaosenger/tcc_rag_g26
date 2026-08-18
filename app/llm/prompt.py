"""Construção do prompt e formatação de fontes para o LLM (Sprint 9).

Funções puras e testáveis que implementam as regras da seção 13 do PRD:
1. Responder EXCLUSIVAMENTE com base no contexto recuperado.
2. Citar as fontes (documento/página/seção/tempo) ao final da resposta.
3. Sinalizar evidência insuficiente quando o contexto não contiver a resposta.
4. Responder em português do Brasil, em linguagem clara para estudantes.
"""

from __future__ import annotations

from typing import Any

SYSTEM_PROMPT = """Você é um assistente de um curso de tecnologia. Responda EXCLUSIVAMENTE com base no contexto fornecido.
Cite as fontes (documento, página/seção/tempo) ao final da resposta.
Se o contexto não contiver a resposta, declare explicitamente que a evidência disponível é insuficiente — nunca complemente com conhecimento externo.
Nunca use conhecimento externo ou paramétrico. Responda em português do Brasil, em linguagem clara para estudantes."""


def format_source_label(idx: int, chunk: dict[str, Any]) -> str:
    """Formata o rótulo de fonte de um chunk (página/seção/tempo).

    Args:
        idx: índice da fonte (1-based).
        chunk: dicionário com document_filename e metadata.

    Returns:
        String formatada, ex.: "[1] apostila.pdf (p. 5) | seção: Introdução"
    """
    meta = chunk.get("metadata", {})
    label = f"[{idx}] {chunk.get('document_filename', 'desconhecido')}"

    if meta.get("page") is not None:
        label += f" (p. {meta['page']})"
    if meta.get("section"):
        label += f" | seção: {meta['section']}"
    if meta.get("start") and meta.get("end"):
        label += f" | tempo: {meta['start']} - {meta['end']}"

    return label


def format_sources(chunks: list[dict[str, Any]]) -> list[str]:
    """Formata a lista de fontes legíveis a partir dos chunks recuperados.

    Args:
        chunks: lista de chunks com document_filename e metadata.

    Returns:
        Lista de strings formatadas.
    """
    return [format_source_label(idx, chunk) for idx, chunk in enumerate(chunks, start=1)]


def build_prompt(question: str, chunks: list[dict[str, Any]]) -> str:
    """Monta o prompt completo para o LLM com contexto + pergunta.

    Args:
        question: pergunta do usuário.
        chunks: chunks recuperados pelo retrieval.

    Returns:
        Prompt formatado conforme as regras da seção 13 do PRD.
    """
    context_parts = []
    for idx, chunk in enumerate(chunks, start=1):
        label = format_source_label(idx, chunk)
        context_parts.append(f"{label}\n{chunk.get('content', '')}")

    context = "\n\n".join(context_parts)
    sources_block = "\n".join(format_sources(chunks))

    return f"""{SYSTEM_PROMPT}

Contexto recuperado:
{context}

Fontes:
{sources_block}

Pergunta: {question}

Resposta:"""
