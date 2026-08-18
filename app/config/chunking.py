"""Configurações centralizadas de chunking para o pipeline RAG.

TODOS os splitters do projeto devem importar essas constantes.
Os valores estão congelados para garantir reprodutibilidade experimental (RNF-06).
"""

from __future__ import annotations

# Tamanho do chunk e overlap (em caracteres).
# Um chunk de ~1024 caracteres em português equivale a aproximadamente
# 200-280 tokens, deixando folga confortável para o embedding do Titan V2.
CHUNK_SIZE = 1024
CHUNK_OVERLAP = 128  # ~12,5% de sobreposição

# Número de chunks recuperados por pergunta (congelado para os experimentos).
TOP_K = 5

# Separadores usados pelo RecursiveCharacterTextSplitter, do mais prioritário
# ao menos prioritário. Isso favorece quebras naturais de parágrafo/frase.
SEPARATORS = ["\n\n", "\n", ". ", " ", ""]

# Áudio: agrupamento de segmentos Whisper consecutivos.
# Segmentos com gap menor que esse valor (em segundos) são unidos no mesmo chunk.
AUDIO_JOIN_MAX_GAP_SECONDS = 2.0
AUDIO_CHUNK_TARGET_SIZE = CHUNK_SIZE

# Modelos fixos (RNF-06).
EMBEDDING_MODEL = "amazon.titan-embed-text-v2:0"
EMBEDDING_DIMENSION = 1024
LLM_MODEL = "us.deepseek.r1-v1:0"

# Headers para split hierárquico de Markdown.
MARKDOWN_HEADERS = [
    ("#", "header_1"),
    ("##", "header_2"),
    ("###", "header_3"),
]
