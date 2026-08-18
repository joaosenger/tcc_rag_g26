import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    aws_region: str = os.getenv("AWS_REGION", "us-east-1")
    bedrock_embedding_model: str = os.getenv(
        "BEDROCK_EMBEDDING_MODEL", "amazon.titan-embed-text-v2:0"
    )
    bedrock_llm_model: str = os.getenv("BEDROCK_LLM_MODEL", "us.deepseek.r1-v1:0")


settings = Settings()
