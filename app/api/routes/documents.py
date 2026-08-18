"""Rotas de upload, listagem e acesso a documentos."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Document
from app.ingestion.pipeline import UnsupportedFileError, ingest_file

router = APIRouter(prefix="/api/documents", tags=["documents"])

PDF_DIR = Path("content/documents")

SUPPORTED_CONTENT_TYPES = {
    "application/pdf": ".pdf",
    "text/markdown": ".md",
    "audio/mpeg": ".mp3",
    "audio/mp3": ".mp3",
    "video/mp4": ".mp4",
}


class IngestionResponse(BaseModel):
    document_id: str
    filename: str
    type: str
    chunks: int


class DocumentSummary(BaseModel):
    id: str
    filename: str
    type: str
    created_at: str

    class Config:
        from_attributes = True


@router.post("", response_model=IngestionResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> Any:
    """Faz upload de um arquivo e dispara o pipeline de ingestão."""
    original_name = Path(file.filename or "upload").name
    suffix = SUPPORTED_CONTENT_TYPES.get(file.content_type or "")
    if not suffix:
        suffix = Path(original_name).suffix.lower()
        if suffix not in {".pdf", ".md", ".mp3", ".mp4"}:
            raise HTTPException(
                status_code=415,
                detail=f"tipo de arquivo não suportado: {file.content_type or suffix}",
            )

    tmp_dir = Path(tempfile.mkdtemp())
    tmp_path = tmp_dir / original_name
    try:
        content = await file.read()
        tmp_path.write_bytes(content)

        result = ingest_file(db, tmp_path)
        return result

    except UnsupportedFileError as exc:
        raise HTTPException(status_code=415, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"falha na ingestão: {exc}") from exc
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
        tmp_dir.rmdir()


@router.get("/pdf/{filename}")
async def get_pdf(filename: str) -> FileResponse:
    """Serve um PDF do corpus para visualização em nova aba ou download."""
    name = Path(filename).name
    if name != filename or not name.lower().endswith(".pdf"):
        raise HTTPException(status_code=404, detail="arquivo não encontrado")

    pdf_path = PDF_DIR / name
    if not pdf_path.is_file():
        raise HTTPException(status_code=404, detail="arquivo não encontrado")

    return FileResponse(pdf_path, media_type="application/pdf", filename=name)


@router.get("", response_model=list[DocumentSummary])
async def list_documents(db: Session = Depends(get_db)) -> Any:
    """Lista todos os documentos ingeridos."""
    docs = db.query(Document).order_by(Document.created_at.desc()).all()
    return [
        {
            "id": doc.id,
            "filename": doc.filename,
            "type": doc.type,
            "created_at": doc.created_at.isoformat(),
        }
        for doc in docs
    ]
