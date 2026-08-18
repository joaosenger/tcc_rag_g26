import json
from unittest.mock import MagicMock, patch

from app.embeddings import bedrock


def _mock_response(vector):
    response = MagicMock()
    response.__getitem__ = MagicMock(
        side_effect=lambda key: {"body": _FakeBody(vector)}[key]
    )
    return response


class _FakeBody:
    def __init__(self, payload):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode()


def test_embed_text_returns_vector_and_payload():
    fake_vector = [0.1] * 1024
    with patch.object(bedrock, "get_client") as mock_client:
        mock_client.return_value.invoke_model.return_value = _mock_response(
            {"embedding": fake_vector}
        )
        result = bedrock.embed_text("texto de teste")
    assert result == fake_vector
    args = mock_client.return_value.invoke_model.call_args.kwargs
    assert args["modelId"] == "amazon.titan-embed-text-v2:0"
    body = json.loads(args["body"])
    assert body["inputText"] == "texto de teste"
    assert body["dimensions"] == 1024
    assert body["normalize"] is True
