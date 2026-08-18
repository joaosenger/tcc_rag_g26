"""Cliente do AWS Bedrock para geração de respostas com DeepSeek.

Inclui retry com backoff exponencial para lidar com throttling.
"""

from __future__ import annotations

import logging
import time

import boto3
from botocore.config import Config

from app.config import settings

logger = logging.getLogger(__name__)

_MAX_RETRIES = 5
_BASE_DELAY = 2.0


def get_client():
    return boto3.client(
        "bedrock-runtime",
        region_name=settings.aws_region,
        config=Config(retries={"max_attempts": 3, "mode": "adaptive"}),
    )


def generate(prompt: str) -> str:
    """Invoca o LLM via Converse API com retry manual para throttling.

    Args:
        prompt: prompt completo (system + contexto + pergunta).

    Returns:
        Texto da resposta do LLM.
    """
    client = get_client()
    messages = [{"role": "user", "content": [{"text": prompt}]}]

    last_exc: Exception | None = None
    for attempt in range(1, _MAX_RETRIES + 1):
        try:
            response = client.converse(
                modelId=settings.bedrock_llm_model,
                messages=messages,
            )
            return response["output"]["message"]["content"][0]["text"]
        except Exception as exc:
            last_exc = exc
            if "Throttling" in type(exc).__name__ or "Throttling" in str(exc):
                delay = _BASE_DELAY * (2 ** (attempt - 1))
                logger.warning(
                    "Bedrock throttling (tentativa %d/%d), aguardando %.1fs...",
                    attempt,
                    _MAX_RETRIES,
                    delay,
                )
                time.sleep(delay)
                continue
            raise

    raise RuntimeError(f"Bedrock falhou após {_MAX_RETRIES} tentativas") from last_exc


if __name__ == "__main__":
    answer = generate("Responda em uma frase: o que é RAG?")
    print(f"model={settings.bedrock_llm_model} answer={answer}")
