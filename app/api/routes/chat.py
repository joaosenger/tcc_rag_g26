"""Rota de chat RAG (Sprint 9)."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.llm.bedrock import generate
from app.llm.prompt import build_prompt
from app.retrieval.vector_search import retrieve_top_k

router = APIRouter(prefix="/api/chat", tags=["chat"])


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    document_filename: str
    document_type: str
    metadata: dict
    content: str
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)) -> Any:
    """Responde uma pergunta usando RAG: retrieval + LLM + fontes."""
    try:
        chunks = retrieve_top_k(db, request.question)
        if not chunks:
            return ChatResponse(
                answer=(
                    "A evidência disponível é insuficiente para responder "
                    "a esta pergunta. Não foram encontrados trechos relevantes "
                    "no material do curso."
                ),
                sources=[],
            )

        prompt = build_prompt(request.question, chunks)
        answer = generate(prompt)

        sources = [
            Source(
                document_filename=chunk["document_filename"],
                document_type=chunk["document_type"],
                metadata=chunk["metadata"],
                content=chunk["content"],
                score=chunk["score"],
            )
            for chunk in chunks
        ]

        return ChatResponse(answer=answer, sources=sources)

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"falha no chat: {exc}") from exc
