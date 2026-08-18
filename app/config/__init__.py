"""Configurações centralizadas do projeto."""

from app.config.chunking import (
    AUDIO_CHUNK_TARGET_SIZE,
    AUDIO_JOIN_MAX_GAP_SECONDS,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_DIMENSION,
    EMBEDDING_MODEL,
    LLM_MODEL,
    MARKDOWN_HEADERS,
    SEPARATORS,
    TOP_K,
)
from app.config.settings import settings

__all__ = [
    "settings",
    "CHUNK_SIZE",
    "CHUNK_OVERLAP",
    "TOP_K",
    "SEPARATORS",
    "AUDIO_JOIN_MAX_GAP_SECONDS",
    "AUDIO_CHUNK_TARGET_SIZE",
    "EMBEDDING_MODEL",
    "EMBEDDING_DIMENSION",
    "LLM_MODEL",
    "MARKDOWN_HEADERS",
]
