#!/usr/bin/env python
"""Consulta a API RAG com as 60 perguntas do dataset e preenche resultados_avaliacao.md.

Uso:
    python consultar_api.py run     # executa as consultas (15 s entre requisições)
    python consultar_api.py fill    # preenche resultados_avaliacao.md a partir de resultados_rag.json

As respostas são salvas incrementalmente em dataset/resultados_rag.json e a execução
é retomável: perguntas já respondidas são puladas ao reexecutar `run`.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent
PERGUNTAS_PATH = BASE_DIR / "perguntas_avaliacao.json"
RESULTADOS_PATH = BASE_DIR / "resultados_rag.json"
SAIDA_PATH = BASE_DIR / "resultados_avaliacao.md"
RESPOSTAS_SEM_RAG_PATH = BASE_DIR / "resultados_sem_rag.json"

API_URL = "http://98.86.159.78:8000/api/chat"
INTERVALO_SEGUNDOS = 15
TIMEOUT_SEGUNDOS = 180

# Regras de fonte esperada por pergunta, derivadas das notas do dataset.
# Cada regra é um par (tipo, valor): "filename" casa substring do
# document_filename; "content" casa substring do conteúdo do chunk (case-insensitive).
RULES = {
    "G01-Q01": [("filename", "01.md"), ("filename", "aula-01")],
    "G01-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G01-Q03": [("filename", "02.md"), ("filename", "aula-02")],
    "G01-Q04": [("content", "fastapi")],
    "G01-Q05": [("filename", "Introdução ao Python")],
    "G01-Q06": [("filename", "02.md"), ("filename", "aula-02")],
    "G02-Q01": [("filename", "02.md"), ("filename", "aula-02")],
    "G02-Q02": [("filename", "06.md"), ("filename", "aula-06")],
    "G02-Q03": [("filename", "01.md"), ("filename", "aula-01")],
    "G02-Q04": [("filename", "02.md"), ("filename", "aula-02")],
    "G02-Q05": [("filename", "11.md"), ("filename", "aula-11")],
    "G02-Q06": [("filename", "01.md"), ("filename", "aula-01")],
    "G05-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G05-Q03": [("filename", "01.md"), ("filename", "aula-01")],
    "G05-Q04": [("content", "instalar"), ("filename", "01.md"), ("filename", "02.md")],
    "G05-Q06": [("filename", "01.md"), ("filename", "aula-01")],
    "G06-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G06-Q03": [("filename", "02.md"), ("filename", "aula-02")],
    "G06-Q04": [("filename", "02.md"), ("filename", "aula-02")],
    "G06-Q05": [("filename", "06.md"), ("filename", "aula-06")],
    "G06-Q06": [("filename", "02.md"), ("filename", "aula-02")],
    "G07-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G07-Q03": [("filename", "06.md"), ("filename", "aula-06")],
    "G07-Q05": [("filename", "02.md"), ("filename", "aula-02")],
    "G07-Q06": [("content", "fastapi")],
    "G08-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G08-Q03": [("filename", "01.md"), ("filename", "aula-01")],
    "G08-Q04": [("filename", "06.md"), ("filename", "aula-06")],
    "G08-Q05": [("content", "swagger"), ("filename", "02.md")],
    "G08-Q06": [("filename", "11.md"), ("filename", "aula-11")],
    "G09-Q02": [("filename", "01.md"), ("filename", "aula-01")],
    "G09-Q03": [("filename", "02.md"), ("filename", "aula-02")],
    "G09-Q04": [("filename", "01.md"), ("filename", "aula-01")],
    "G09-Q05": [("content", "fastapi")],
    "G09-Q06": [("filename", "02.md"), ("filename", "aula-02")],
    "G10-Q03": [("filename", "06.md"), ("filename", "aula-06")],
    "G10-Q04": [("filename", "01.md"), ("filename", "aula-01"), ("content", "ambiente virtual")],
    "G10-Q05": [("filename", "01.md"), ("filename", "aula-01")],
}


def carregar_perguntas() -> list[dict]:
    dataset = json.loads(PERGUNTAS_PATH.read_text(encoding="utf-8"))
    return dataset["questions"]


def carregar_respostas() -> dict:
    if not RESULTADOS_PATH.exists():
        return {"responses": {}}
    dados = json.loads(RESULTADOS_PATH.read_text(encoding="utf-8"))
    return dados


def salvar_respostas(dados: dict) -> None:
    RESULTADOS_PATH.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def consultar(question: str) -> tuple[dict, None] | tuple[None, str]:
    try:
        resp = requests.post(
            API_URL,
            json={"question": question},
            timeout=TIMEOUT_SEGUNDOS,
        )
        if resp.status_code != 200:
            return None, f"HTTP {resp.status_code}: {resp.text[:300]}"
        payload = resp.json()
        return payload, None
    except Exception as exc:  # noqa: BLE001
        return None, f"erro: {exc}"


def run() -> None:
    perguntas = carregar_perguntas()
    dados = carregar_respostas()
    pendentes = [q for q in perguntas if q["id"] not in dados["responses"]]
    if not pendentes:
        print("Nenhuma pergunta pendente.")
        return

    print(f"{len(pendentes)} perguntas pendentes de {len(perguntas)}.")
    for i, q in enumerate(pendentes, start=1):
        if i > 1:
            print(f"aguardando {INTERVALO_SEGUNDOS}s...", flush=True)
            time.sleep(INTERVALO_SEGUNDOS)
        qid = q["id"]
        print(f"[{i}/{len(pendentes)}] {qid}: {q['question'][:60]!r}", flush=True)
        payload, erro = consultar(q["question"])
        dados["responses"][qid] = {
            "id": qid,
            "question": q["question"],
            "expected": q["expected"],
            "language": q["language"],
            "categories": q["categories"],
        }
        if erro:
            dados["responses"][qid]["status"] = "error"
            dados["responses"][qid]["error"] = erro
            print(f"    ERRO: {erro}", flush=True)
        else:
            dados["responses"][qid]["status"] = "ok"
            dados["responses"][qid]["answer"] = payload.get("answer", "")
            dados["responses"][qid]["sources"] = payload.get("sources", [])
        salvar_respostas(dados)

    resumos = datos_sumario(dados)
    print(resumos)


def datos_sumario(dados: dict) -> str:
    responses = dados["responses"]
    ok = sum(1 for r in responses.values() if r["status"] == "ok")
    erro = sum(1 for r in responses.values() if r["status"] == "error")
    return f"Concluído: {ok} ok, {erro} erro, {len(responses)} total."


def _formata_fonte(src: dict) -> str:
    parts = [f"`{src['document_filename']}` ({src['document_type']})"]
    meta = src.get("metadata") or {}
    if meta.get("page") is not None:
        parts.append(f"p. {meta['page']}")
    if meta.get("section"):
        parts.append(f"seção: {meta['section']}")
    if meta.get("start") is not None and meta.get("end") is not None:
        parts.append(f"tempo {meta['start']}-{meta['end']}s")
    parts.append(f"score: {src['score']:.4f}")
    return " — ".join(parts)


def _fonte_correta(q: dict, resp: dict) -> str:
    if q["expected"] == "out_of_context":
        return "n/a"
    sources = resp.get("sources") or []
    if not sources:
        return "nao"
    regras = RULES.get(q["id"])
    if not regras:
        return "n/a"

    def casa(src: dict) -> bool:
        content = (src.get("content") or "").lower()
        fname = src.get("document_filename") or ""
        for kind, valor in regras:
            if kind == "filename" and valor in fname:
                return True
            if kind == "content" and valor.lower() in content:
                return True
        return False

    casados = [casa(s) for s in sources]
    if casados[0]:
        return "sim"
    if any(casados):
        return "parcial"
    return "nao"


def _formata_campo(campo: str, valor: str) -> list[str]:
    """Formata um campo do markdown preservando a estrutura do texto.

    A primeira linha vai inline após o rótulo; as demais são recuadas em 2
    espaços para manter o item de lista válido e renderizar o markdown interno
    (títulos, listas, tabelas, blocos de código) corretamente.
    """
    if not valor:
        return [f"- **{campo}:**"]
    linhas = valor.rstrip().splitlines()
    out = [f"- **{campo}:** {linhas[0]}"]
    for linha in linhas[1:]:
        out.append(f"  {linha}" if linha.strip() else "")
    return out


def fill() -> None:
    perguntas = carregar_perguntas()
    dados = carregar_respostas()
    responses = dados["responses"]
    try:
        sem_rag = json.loads(RESPOSTAS_SEM_RAG_PATH.read_text(encoding="utf-8"))[
            "responses"
        ]
    except (OSError, KeyError, json.JSONDecodeError):
        sem_rag = {}

    linhas = [
        "# Resultados da Avaliação da RAG — TCC G26",
        "",
        "Campos preenchidos automaticamente via API (dataset/resultados_rag.json).",
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

    def _respondida(qid: str) -> bool:
        resp = responses.get(qid)
        return bool(resp and resp["status"] == "ok")

    for grupo in range(1, 11):
        do_grupo = [q for q in perguntas if q["group"] == grupo]
        nome_grupo = do_grupo[0]["group_name"]
        linhas.append(f"## Grupo {grupo} — {nome_grupo}")
        linhas.append("")
        for q in do_grupo:
            qid = q["id"]
            linhas.append(f"### {qid} ({q['language']})")
            linhas.append("")
            linhas.append(f"**Pergunta:** {q['question']}")
            linhas.append(f"**Categorias:** {' | '.join(q['categories'])}")
            linhas.append(f"**Expectativa:** `{q['expected']}`")
            linhas.append("")

            campos: dict[str, str] = {
                "Resposta obtida (RAG)": "",
                "Análises": "",
                "Resposta sem RAG": "",
                "Fontes obtidas": "",
                "Fonte correta recuperada": "",
                "Resposta adequada": "",
                "Sinalizou insuficiência": "",
                "Qualidade geral (1–5)": "",
                "Observações": "",
            }

            if _respondida(qid):
                resp = responses[qid]
                campos["Resposta obtida (RAG)"] = (resp["answer"] or "").strip()
                sem_rag_resp = sem_rag.get(qid)
                if sem_rag_resp and sem_rag_resp.get("status") == "ok":
                    campos["Resposta sem RAG"] = (
                        (sem_rag_resp.get("answer") or "").strip()
                    )
                else:
                    campos["Resposta sem RAG"] = "—"
                sources = resp.get("sources") or []
                if sources:
                    campos["Fontes obtidas"] = "\n".join(
                        f"- {_formata_fonte(s)}" for s in sources
                    )
                else:
                    campos["Fontes obtidas"] = "nenhuma"
                campos["Fonte correta recuperada"] = _fonte_correta(q, resp)
            else:
                resp = responses.get(qid, {})
                campos["Resposta obtida (RAG)"] = (
                    f"FALHA NA CONSULTA: {resp.get('error', 'não consultada')}"
                )
                campos["Resposta sem RAG"] = "—"
                campos["Fontes obtidas"] = "—"
                campos["Fonte correta recuperada"] = "—"

            for campo, valor in campos.items():
                linhas.extend(_formata_campo(campo, valor))
            linhas.append("")

    SAIDA_PATH.write_text("\n".join(linhas), encoding="utf-8")
    print(f"Gerado: {SAIDA_PATH}")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"run", "fill"}:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "run":
        run()
    else:
        fill()


if __name__ == "__main__":
    main()