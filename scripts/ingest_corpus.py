"""Ingere todo o corpus de content/ automaticamente via API.

Uso:
    python scripts/ingest_corpus.py
    python scripts/ingest_corpus.py --api http://localhost:8000
    python scripts/ingest_corpus.py --only markdown
    python scripts/ingest_corpus.py --only audio
    python scripts/ingest_corpus.py --only pdf
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import requests

DEFAULT_API = "http://localhost:8000"
CONTENT_DIR = Path("content")
MARKDOWN_DIR = CONTENT_DIR / "markdown" / "aulas"
AUDIO_DIR = CONTENT_DIR / "audio"
PDF_DIR = CONTENT_DIR / "documents"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingere todo o corpus de content/.")
    parser.add_argument("--api", default=DEFAULT_API, help="URL da API")
    parser.add_argument(
        "--only",
        choices=["markdown", "audio", "pdf", "all"],
        default="all",
        help="Tipo de conteúdo a ingerir",
    )
    return parser.parse_args()


def ingest_file(api_url: str, file_path: Path) -> dict:
    """Envia um arquivo para a API e retorna o resultado."""
    with open(file_path, "rb") as f:
        files = {"file": (file_path.name, f, "application/octet-stream")}
        resp = requests.post(f"{api_url}/api/documents", files=files, timeout=600)
    if resp.status_code == 200:
        return resp.json()
    raise RuntimeError(f"Erro {resp.status_code} ao ingerir {file_path.name}: {resp.text}")


def collect_files(content_type: str) -> list[Path]:
    """Coleta os arquivos a ingerir por tipo."""
    files = []
    if content_type in ("markdown", "all"):
        files.extend(sorted(MARKDOWN_DIR.glob("*.md")))
    if content_type in ("audio", "all"):
        files.extend(sorted(AUDIO_DIR.glob("*.mp3")))
    if content_type in ("pdf", "all"):
        files.extend(sorted(PDF_DIR.glob("*.pdf")))
    return files


def main() -> int:
    args = parse_args()

    files = collect_files(args.only)
    if not files:
        print(f"Nenhum arquivo encontrado em content/ para o tipo '{args.only}'.")
        return 1

    print(f"API: {args.api}")
    print(f"Tipo: {args.only}")
    print(f"Arquivos a ingerir: {len(files)}")
    print("-" * 60)

    success = 0
    errors = 0
    start = time.monotonic()

    for idx, file_path in enumerate(files, start=1):
        print(f"[{idx}/{len(files)}] Ingerindo {file_path.name}...", end=" ", flush=True)
        try:
            result = ingest_file(args.api, file_path)
            print(
                f"OK -> {result['type']}, {result['chunks']} chunks "
                f"(document_id={result['document_id'][:8]}...)"
            )
            success += 1
        except Exception as exc:
            print(f"ERRO: {exc}")
            errors += 1

    elapsed = time.monotonic() - start
    print("-" * 60)
    print(f"Resumo: {success} sucesso(s), {errors} erro(s), {elapsed:.1f}s total")

    if errors > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
