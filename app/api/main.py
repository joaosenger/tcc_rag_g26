"""Aplicação FastAPI com endpoints da API RAG."""

from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes import chat, documents

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="RAG TCC G26", version="0.1.0")


@app.on_event("startup")
async def startup_event() -> None:
    """Auto-ingere o corpus se o banco estiver vazio."""
    from app.ingestion.auto_ingest import auto_ingest

    try:
        count = auto_ingest()
        if count > 0:
            logger.info("Corpus ingerido automaticamente: %d arquivos.", count)
    except Exception as exc:
        logger.error("Falha na auto-ingestão: %s", exc)


@app.get("/health", tags=["health"])
async def health_check() -> JSONResponse:
    """Healthcheck simples da API."""
    return JSONResponse({"status": "ok"})


app.include_router(documents.router)
app.include_router(chat.router)
