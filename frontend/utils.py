"""Funções puras do frontend (testáveis sem Streamlit)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

INSUFFICIENT_KEYWORDS = (
    "insuficiente",
    "insuficiência",
    "insuficiencia",
    "não contém",
    "não contem",
    "não possui",
    "não possui",
    "não foi possível",
    "não foi possivel",
    "evidência disponível",
    "evidencia disponivel",
    "não encontrei",
    "não foram encontrados",
)


def list_corpus_pdfs(base_dir: Path) -> list[str]:
    """Lista os nomes dos PDFs disponíveis no corpus, em ordem alfabética.

    Args:
        base_dir: diretório onde ficam os PDFs (ex.: `content/documents`).

    Returns:
        Lista de nomes de arquivos `.pdf` existentes.
    """
    if not base_dir.is_dir():
        return []
    return sorted(p.name for p in base_dir.glob("*.pdf") if p.is_file())


PDF_EXTERNAL_URLS = {
    "Introdução ao Python.pdf": "https://files.cercomp.ufg.br/weby/up/688/o/M2_IP_24-09-24.pdf",
    "Python para Processamento de Dados.pdf": (
        "https://portaldelivros.ufg.br/index.php/cegrafufg/catalog/view/642/614/2539"
    ),
}


def resolve_pdf_url(api_url: str, filename: str) -> str:
    """Retorna a URL de um PDF: externa (UFG) se mapeada, senão o endpoint local da API.

    Args:
        api_url: URL base da API (ex.: `http://localhost:8000`).
        filename: nome do arquivo PDF.

    Returns:
        URL externa oficial ou a URL do endpoint local que serve o PDF.
    """
    return PDF_EXTERNAL_URLS.get(filename, build_pdf_url(api_url, filename))


def build_pdf_url(api_url: str, filename: str) -> str:
    """Monta a URL do endpoint que serve um PDF do corpus.

    Args:
        api_url: URL base da API (ex.: `http://localhost:8000`).
        filename: nome do arquivo PDF.

    Returns:
        URL completa para visualizar/baixar o PDF.
    """
    return f"{api_url.rstrip('/')}/api/documents/pdf/{filename}"


def format_source(source: dict[str, Any]) -> str:
    """Formata uma fonte individual em string legível.

    Args:
        source: dicionário com document_filename, document_type, metadata, content, score.

    Returns:
        String formatada, ex.: "**apostila.pdf** (pdf) — p. 5 | seção: Intro | score: 0.92"
    """
    filename = source.get("document_filename") or "desconhecido"
    doc_type = source.get("document_type") or ""
    meta = source.get("metadata", {})
    score = source.get("score", 0.0)

    parts = [f"**{filename}**"]
    if doc_type:
        parts.append(f"({doc_type})")

    if meta.get("page") is not None:
        parts.append(f"p. {meta['page']}")
    if meta.get("section"):
        parts.append(f"seção: {meta['section']}")
    if meta.get("start") and meta.get("end"):
        parts.append(f"tempo: {meta['start']} - {meta['end']}")

    parts.append(f"score: {score:.4f}")
    label = " — ".join(parts)

    content = source.get("content", "")
    snippet = content[:200] + "..." if len(content) > 200 else content
    return f"{label}\n\n> {snippet}"


def format_sources_display(sources: list[dict[str, Any]]) -> str:
    """Formata a lista de fontes para exibição no chat.

    Args:
        sources: lista de fontes recuperadas.

    Returns:
        String Markdown com todas as fontes, ou string vazia se nenhuma.
    """
    if not sources:
        return ""
    blocks = []
    for idx, source in enumerate(sources, start=1):
        blocks.append(f"**[{idx}]** {format_source(source)}")
    return "\n\n---\n\n".join(blocks)


def is_insufficient_evidence(answer: str) -> bool:
    """Detecta se a resposta sinaliza evidência insuficiente.

    Args:
        answer: texto da resposta do LLM.

    Returns:
        True se a resposta contiver palavras-chave de insuficiência.
    """
    if not answer:
        return False
    answer_lower = answer.lower()
    return any(kw in answer_lower for kw in INSUFFICIENT_KEYWORDS)
