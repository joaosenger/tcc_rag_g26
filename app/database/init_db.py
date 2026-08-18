"""Cria as tabelas do banco de dados (incluindo extensão pgvector)."""

from __future__ import annotations

from sqlalchemy import text

from app.database.connection import Base, engine
from app.database import models  # noqa: F401 — registra os modelos no Base.metadata


def init_db() -> None:
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        conn.commit()
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")


if __name__ == "__main__":
    init_db()
