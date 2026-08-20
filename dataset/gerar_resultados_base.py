#!/usr/bin/env python
"""Gera dataset/resultados_avaliacao.md a partir de dataset/perguntas_avaliacao.json."""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CAMPO_CATEGORIA = "categories"
CAMPO_EXPECTATIVA = "expected"


def main() -> None:
    dataset = json.loads((BASE_DIR / "perguntas_avaliacao.json").read_text(encoding="utf-8"))
    perguntas = dataset["questions"]

    linhas = [
        "# Resultados da Avaliação da RAG — TCC G26",
        "",
        "Preencher os campos abaixo após testar cada pergunta no chat.",
        "Legenda das respostas:",
        "",
        "- **fonte_correta_recuperada**: `sim` | `nao` | `parcial`",
        "- **resposta_adequada**: `sim` | `nao` | `parcial`",
        "- **sinalizou_insuficiencia**: `sim` | `nao` | `n/a` (esperado `sim` nas perguntas fora de contexto)",
        "- **qualidade_geral**: nota de 1 a 5",
        "",
        "",
        f"Total de perguntas: **{len(perguntas)}**",
        "",
    ]

    for grupo, grupo_nome in _grupos_ordenados(perguntas):
        linhas.append(f"## Grupo {grupo} — {grupo_nome}")
        linhas.append("")
        for q in [p for p in perguntas if p["group"] == grupo]:
            linhas.append(f"### {q['id']} ({q['language']})")
            linhas.append("")
            linhas.append(f"**Pergunta:** {q['question']}")
            linhas.append(f"**Categorias:** {' | '.join(q[CAMPO_CATEGORIA])}")
            linhas.append(f"**Expectativa:** `{q[CAMPO_EXPECTATIVA]}`")
            linhas.append("")
            for campo in (
                "Resposta obtida",
                "Fontes obtidas",
                "Fonte correta recuperada",
                "Resposta adequada",
                "Sinalizou insuficiência",
                "Qualidade geral (1–5)",
                "Observações",
            ):
                linhas.append(f"- **{campo}:**")
            linhas.append("")

    (BASE_DIR / "resultados_avaliacao.md").write_text("\n".join(linhas), encoding="utf-8")
    print(f"Gerado: {BASE_DIR / 'resultados_avaliacao.md'}")


def _grupos_ordenados(perguntas: list[dict]) -> list[tuple[int, str]]:
    vistos: dict[int, str] = {}
    for p in perguntas:
        vistos.setdefault(p["group"], p["group_name"])
    return sorted(vistos.items())


if __name__ == "__main__":
    main()