"""Modelos SQLAlchemy para documentos e chunks vetoriais."""

from __future__ import annotations

import uuid
from datetime import datetime

from pgvector.sqlalchemy import Vector
from sqlalchemy import JSON, Column, DateTime, Integer, String, Text

from app.config.chunking import EMBEDDING_DIMENSION
from app.database.connection import Base


class Document(Base):
    """Documento ingerido no sistema RAG."""

    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, nullable=False)
    type = Column(String, nullable=False)  # pdf | markdown | audio
    s3_key = Column(String, nullable=True)
    metadata_ = Column("metadata", JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Chunk(Base):
    """Chunk de conteúdo com embedding vetorial."""

    __tablename__ = "chunks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    document_id = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    metadata_ = Column("metadata", JSON, nullable=False, default=dict)
    embedding = Column(Vector(EMBEDDING_DIMENSION), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
