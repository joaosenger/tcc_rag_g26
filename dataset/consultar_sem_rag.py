#!/usr/bin/env python
"""Consulta o DeepSeek (Bedrock) SEM RAG para as 60 perguntas do dataset.

Condição experimental sem recuperação: a pergunta é enviada diretamente ao
modelo generativo, sem o contexto do corpus. Usa o MESMO modelo do pipeline
com RAG (app.llm.bedrock.generate) para manter os parâmetros constantes.

Uso:
    python dataset/consultar_sem_rag.py run   # executa as consultas (3 s entre requisições)

Requisitos:
    Credenciais AWS com acesso ao Bedrock no ambiente (env, ~/.aws ou IAM role).
    O modelo (us.deepseek.r1-v1:0) e a região devem estar habilitados na conta.

Saídas:
    dataset/respostas_sem_rag.json   - respostas do modelo sem RAG (incremental/retomável)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJETO_ROOT = BASE_DIR.parent
sys.path.insert(0, str(PROJETO_ROOT))

from app.config import settings  # noqa: E402
from app.llm.bedrock import generate  # noqa: E402

PERGUNTAS_PATH = PROJETO_ROOT / "dataset" / "perguntas.json"
RESULTADOS_PATH = PROJETO_ROOT / "dataset" / "respostas_sem_rag.json"

INTERVALO_SEGUNDOS = 3


def carregar_perguntas() -> list[dict]:
    dados = json.loads(PERGUNTAS_PATH.read_text(encoding="utf-8"))
    return dados["questions"]


def carregar_respostas() -> dict:
    if not RESULTADOS_PATH.exists():
        return {"responses": {}}
    return json.loads(RESULTADOS_PATH.read_text(encoding="utf-8"))


def salvar_respostas(dados: dict) -> None:
    RESULTADOS_PATH.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def run() -> None:
    perguntas = carregar_perguntas()
    dados = carregar_respostas()
    pendentes = [q for q in perguntas if q["id"] not in dados["responses"]]

    if not pendentes:
        print("Nenhuma pergunta pendente.")
        return

    print(
        f"Modelo: {settings.bedrock_llm_model} | região: {settings.aws_region} | "
        f"{len(pendentes)}/{len(perguntas)} pendentes."
    )

    for i, q in enumerate(pendentes, start=1):
        if i > 1:
            print(f"aguardando {INTERVALO_SEGUNDOS}s...", flush=True)
            time.sleep(INTERVALO_SEGUNDOS)
        qid = q["id"]
        print(f"[{i}/{len(pendentes)}] {qid}: {q['question'][:60]!r}", flush=True)
        registro = {
            "id": qid,
            "question": q["question"],
            "answer": "",
        }
        try:
            resposta = generate(q["question"])
            registro["answer"] = resposta
            registro["status"] = "ok"
        except Exception as exc:  # noqa: BLE001
            registro["status"] = "error"
            registro["error"] = str(exc)
            print(f"    ERRO: {exc}", flush=True)
        dados["responses"][qid] = registro
        salvar_respostas(dados)

    ok = sum(1 for r in dados["responses"].values() if r["status"] == "ok")
    erro = sum(1 for r in dados["responses"].values() if r["status"] == "error")
    print(f"Concluído: {ok} ok, {erro} erro, {len(dados['responses'])} total.")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] != "run":
        print(__doc__)
        sys.exit(1)
    run()


if __name__ == "__main__":
    main()