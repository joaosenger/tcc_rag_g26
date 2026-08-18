import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from app.ingestion.video import (
    TranscriptionError,
    parse_whisper_result,
    transcribe_file,
)


def test_parse_whisper_result_segments():
    result = {
        "segments": [
            {"text": " Primeira frase. ", "start": 0.0, "end": 3.24},
            {"text": "Segunda frase.", "start": 3.4, "end": 6.0},
            {"text": "   ", "start": 6.1, "end": 7.0},
        ]
    }
    segments = parse_whisper_result(result)
    assert len(segments) == 2
    assert segments[0]["content"] == "Primeira frase."
    assert segments[0]["metadata"] == {"start": 0.0, "end": 3.24}
    assert segments[1]["metadata"] == {"start": 3.4, "end": 6.0}


def test_parse_empty_result():
    assert parse_whisper_result({}) == []
    assert parse_whisper_result({"segments": []}) == []


def test_transcribe_file_reuses_existing_artifact(tmp_path):
    audio = tmp_path / "aula-99.mp3"
    audio.write_bytes(b"fake audio")
    artifact = tmp_path / "out" / "aula-99.json"
    artifact.parent.mkdir()
    artifact.write_text("{}")
    with patch("app.ingestion.video._check_ffmpeg") as mock_check:
        result = transcribe_file(audio, transcripts_dir=artifact.parent)
    assert result == artifact
    mock_check.assert_not_called()


def test_transcribe_file_rejects_unsupported_extension(tmp_path):
    audio = tmp_path / "aula.txt"
    audio.write_text("nada")
    with pytest.raises(TranscriptionError, match="formato nao suportado"):
        transcribe_file(audio, transcripts_dir=tmp_path)


def test_transcribe_file_missing_file(tmp_path):
    with pytest.raises(TranscriptionError, match="arquivo nao encontrado"):
        transcribe_file(tmp_path / "sumiu.mp3", transcripts_dir=tmp_path)


def test_transcribe_file_writes_artifact(tmp_path):
    audio = tmp_path / "aula-98.mp3"
    audio.write_bytes(b"fake audio")
    fake_model = MagicMock()
    fake_model.transcribe.return_value = {
        "segments": [{"text": "Conteudo da aula.", "start": 0.0, "end": 2.5}]
    }
    with (
        patch("app.ingestion.video._check_ffmpeg"),
        patch("whisper.load_model", return_value=fake_model) as mock_load,
    ):
        result = transcribe_file(audio, transcripts_dir=tmp_path / "out")
    mock_load.assert_called_once_with("small")
    fake_model.transcribe.assert_called_once_with(str(audio), language="pt", verbose=False)
    payload = json.loads(result.read_text(encoding="utf-8"))
    assert payload["source"] == "aula-98.mp3"
    assert payload["model"] == "small"
    assert payload["segments"] == [
        {"content": "Conteudo da aula.", "metadata": {"start": 0.0, "end": 2.5}}
    ]


def test_transcribe_file_empty_transcription_raises(tmp_path):
    audio = tmp_path / "aula-97.mp3"
    audio.write_bytes(b"fake audio")
    fake_model = MagicMock()
    fake_model.transcribe.return_value = {"segments": []}
    with (
        patch("app.ingestion.video._check_ffmpeg"),
        patch("whisper.load_model", return_value=fake_model),
    ):
        with pytest.raises(TranscriptionError, match="transcricao vazia"):
            transcribe_file(audio, transcripts_dir=tmp_path / "out")
