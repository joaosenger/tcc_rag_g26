import logging
import subprocess
from pathlib import Path

from app.config import settings

logger = logging.getLogger(__name__)

MODEL_NAME = "small"
ALLOWED_EXTENSIONS = {".mp3", ".mp4", ".wav", ".m4a"}


class TranscriptionError(Exception):
    pass


def _check_ffmpeg():
    try:
        subprocess.run(
            ["ffmpeg", "-version"], capture_output=True, check=True
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise TranscriptionError(
            "ffmpeg nao encontrado no PATH; instale antes de transcrever"
        ) from exc


def parse_whisper_result(result: dict) -> list[dict]:
    """Converte a saída do Whisper em segmentos com timestamps."""
    segments = []
    for segment in result.get("segments", []):
        content = segment.get("text", "").strip()
        if not content:
            continue
        segments.append(
            {
                "content": content,
                "metadata": {
                    "start": round(float(segment["start"]), 2),
                    "end": round(float(segment["end"]), 2),
                },
            }
        )
    return segments


def transcribe_file(audio_path: str | Path, transcripts_dir: str | Path = "content/transcripts") -> Path:
    """Transcreve um arquivo de áudio com Whisper local.

    Salva o artefato em content/transcripts/<stem>.json no mesmo formato
    do restante do pipeline (content + metadata com start/end).
    Idempotente: se o artefato já existe, é reaproveitado.
    """
    source = Path(audio_path)
    if source.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise TranscriptionError(f"formato nao suportado: {source.suffix}")
    if not source.is_file():
        raise TranscriptionError(f"arquivo nao encontrado: {source}")

    output = Path(transcripts_dir) / f"{source.stem}.json"
    if output.is_file():
        logger.info("transcricao ja existe: %s", output)
        return output

    _check_ffmpeg()
    output.parent.mkdir(parents=True, exist_ok=True)

    import json

    import whisper

    logger.info("carregando modelo whisper %s", MODEL_NAME)
    model = whisper.load_model(MODEL_NAME)
    logger.info("transcrevendo %s", source)
    try:
        result = model.transcribe(str(source), language="pt", verbose=False)
    except Exception as exc:
        logger.exception("falha ao transcrever %s", source)
        raise TranscriptionError(f"falha ao transcrever {source.name}") from exc

    segments = parse_whisper_result(result)
    if not segments:
        raise TranscriptionError(f"transcricao vazia para {source.name}")

    payload = {
        "source": source.name,
        "model": MODEL_NAME,
        "language": "pt",
        "segments": segments,
    }
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    logger.info("transcricao salva: %s (%d segmentos)", output, len(segments))
    return output


if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Transcreve audios das aulas (Whisper local)")
    parser.add_argument("arquivos", nargs="+", help="caminhos dos mp3")
    parser.add_argument("-o", "--output", default="content/transcripts")
    args = parser.parse_args()
    for path in args.arquivos:
        print(transcribe_file(path, args.output))
