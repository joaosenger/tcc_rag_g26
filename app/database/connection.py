"""Conexão com PostgreSQL + pgvector via SQLAlchemy.

A URL de conexão pode ser informada diretamente pela variável de ambiente
DATABASE_URL ou montada a partir das variáveis POSTGRES_*.
"""

from __future__ import annotations

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


def _build_database_url() -> str:
    """Monta DATABASE_URL a partir das variáveis de ambiente."""
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    user = os.getenv("POSTGRES_USER", "rag")
    password = os.getenv("POSTGRES_PASSWORD", "rag")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "rag")

    return f"postgresql+psycopg2://{quote_plus(user)}:{quote_plus(password)}@{host}:{port}/{quote_plus(db)}"


DATABASE_URL = _build_database_url()

engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Gerenciador de contexto para sessões do banco."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
