import json

import boto3

from app.config import settings


def get_client():
    return boto3.client("bedrock-runtime", region_name=settings.aws_region)


def embed_text(text: str) -> list[float]:
    response = get_client().invoke_model(
        modelId=settings.bedrock_embedding_model,
        accept="application/json",
        contentType="application/json",
        body=json.dumps(
            {
                "inputText": text,
                "dimensions": 1024,
                "normalize": True,
            }
        ),
    )
    payload = json.loads(response["body"].read())
    return payload["embedding"]


if __name__ == "__main__":
    vector = embed_text("Teste de embedding para o TCC de RAG.")
    print(f"model={settings.bedrock_embedding_model} dimension={len(vector)}")
