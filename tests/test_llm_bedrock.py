from unittest.mock import MagicMock, patch

from app.llm import bedrock


def test_generate_returns_text():
    fake = {
        "output": {"message": {"content": [{"text": "Resposta do modelo"}]}}
    }
    with patch.object(bedrock, "get_client") as mock_client:
        mock_client.return_value.converse.return_value = fake
        result = bedrock.generate("pergunta?")
    assert result == "Resposta do modelo"
    args = mock_client.return_value.converse.call_args.kwargs
    assert args["messages"] == [
        {"role": "user", "content": [{"text": "pergunta?"}]}
    ]
