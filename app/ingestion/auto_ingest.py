"""Auto-ingestão do corpus de content/ na inicialização.

Se o banco estiver vazio (nenhum documento), ingere automaticamente:
- Markdown das aulas (content/markdown/aulas/*.md)
- PDFs (content/documents/*.pdf)
- Áudios (content/audio/*.mp3 — com transcrições em content/audio/transcriptions/)

Se já houver documentos, não faz nada (idempotente).
"""

from __future__ import annotations

import logging
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal, engine
from app.ingestion.pipeline import IngestionError, ingest_file

logger = logging.getLogger(__name__)

CONTENT_DIR = Path("content")
MARKDOWN_DIR = CONTENT_DIR / "markdown" / "aulas"
AUDIO_DIR = CONTENT_DIR / "audio"
PDF_DIR = CONTENT_DIR / "documents"


def is_database_empty() -> bool:
    """Verifica se não há documentos no banco."""
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM documents")).scalar()
    return count == 0


def collect_corpus() -> list[Path]:
    """Coleta todos os arquivos do corpus em ordem (markdown, pdf, áudio)."""
    files: list[Path] = []
    files.extend(sorted(MARKDOWN_DIR.glob("*.md")))
    files.extend(sorted(PDF_DIR.glob("*.pdf")))
    files.extend(sorted(AUDIO_DIR.glob("*.mp3")))
    return files


def auto_ingest() -> int:
    """Ingere todo o corpus se o banco estiver vazio.

    Returns:
        Número de arquivos ingeridos.
    """
    if not is_database_empty():
        logger.info("Banco já possui documentos — pulando auto-ingestão.")
        return 0

    files = collect_corpus()
    if not files:
        logger.warning("Nenhum arquivo encontrado em content/ para ingerir.")
        return 0

    logger.info("Auto-ingestão: %d arquivos encontrados.", len(files))

    db: Session = SessionLocal()
    success = 0
    try:
        for idx, file_path in enumerate(files, start=1):
            logger.info("[%d/%d] Ingerindo %s...", idx, len(files), file_path.name)
            try:
                result = ingest_file(db, file_path)
                logger.info(
                    "  OK: %s -> %d chunks (document_id=%s)",
                    result["filename"],
                    result["chunks"],
                    result["document_id"][:8],
                )
                success += 1
            except IngestionError as exc:
                logger.warning("  Pulando %s: %s", file_path.name, exc)
            except Exception as exc:
                logger.error("  Erro em %s: %s", file_path.name, exc)
    finally:
        db.close()

    logger.info("Auto-ingestão concluída: %d/%d arquivos.", success, len(files))
    return success
