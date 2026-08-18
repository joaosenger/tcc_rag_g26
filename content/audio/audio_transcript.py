"""Módulo de transcrição local de aulas em MP3 com Whisper para o pipeline RAG.

Exporta funções reutilizáveis para transcrever um único arquivo ou ser chamado
em lote por `transcribe_all.py`.

Engines suportadas:
    - faster-whisper (padrão): usa batch na GPU, muito mais rápido.
    - openai-whisper: fallback original.
"""

from __future__ import annotations

import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Iterable

import torch


def format_timestamp(seconds: float) -> str:
    """Formata segundos no formato [HH:MM:SS]."""
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def extract_lesson_name(audio_path: Path) -> str:
    """Deriva o nome base da aula a partir do nome do arquivo (ex.: aula-00)."""
    stem = audio_path.stem
    stem = re.sub(r"[^\w\-]", "_", stem)
    return stem


def convert_to_wav(audio_path: Path, output_wav: Path) -> None:
    """Converte o áudio para WAV 16kHz mono via FFmpeg (evita gargalo de decode)."""
    if output_wav.exists():
        output_wav.unlink()

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(audio_path),
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        str(output_wav),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def save_markdown(
    segments: list[dict[str, Any]],
    output_path: Path,
    audio_path: Path,
    model_name: str,
    language: str,
    engine: str,
) -> None:
    """Salva a transcrição em Markdown com timestamps, no formato do pipeline RAG."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcrição da Aula: {audio_path.name}\n\n")
        f.write(f"<!-- engine: {engine} | modelo: {model_name} | idioma: {language} -->\n\n")

        for segment in segments:
            start = segment.get("start", 0.0)
            text = segment.get("text", "").strip()
            if not text:
                continue
            timestamp = format_timestamp(start)
            f.write(f"**[{timestamp}]** {text}\n\n")


def save_json(
    result: dict[str, Any],
    output_path: Path,
    audio_path: Path,
    model_name: str,
    language: str,
    engine: str,
) -> None:
    """Salva o artefato completo da transcrição em JSON, com metadados de origem."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    artifact = {
        "source": str(audio_path),
        "filename": audio_path.name,
        "engine": engine,
        "model": model_name,
        "language": language,
        "text": result.get("text", ""),
        "segments": result.get("segments", []),
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(artifact, f, ensure_ascii=False, indent=2)


def _segments_to_dicts(segments: Iterable[Any]) -> list[dict[str, Any]]:
    """Normaliza os segmentos do faster-whisper para dicionários."""
    out = []
    for seg in segments:
        out.append(
            {
                "id": getattr(seg, "id", None),
                "seek": getattr(seg, "seek", None),
                "start": getattr(seg, "start", 0.0),
                "end": getattr(seg, "end", 0.0),
                "text": getattr(seg, "text", "").strip(),
                "tokens": getattr(seg, "tokens", []),
                "temperature": getattr(seg, "temperature", None),
                "avg_logprob": getattr(seg, "avg_logprob", None),
                "compression_ratio": getattr(seg, "compression_ratio", None),
                "no_speech_prob": getattr(seg, "no_speech_prob", None),
                "words": [
                    {
                        "start": getattr(w, "start", None),
                        "end": getattr(w, "end", None),
                        "word": getattr(w, "word", ""),
                        "probability": getattr(w, "probability", None),
                    }
                    for w in getattr(seg, "words", []) or []
                ],
            }
        )
    return out


def load_faster_model(
    model_name: str,
    device: str,
    compute_type: str,
):
    """Carrega e retorna o modelo faster-whisper ( WhisperModel + BatchedInferencePipeline )."""
    from faster_whisper import BatchedInferencePipeline, WhisperModel

    model = WhisperModel(
        model_name,
        device=device,
        compute_type=compute_type,
        cpu_threads=0 if device == "cpu" else 4,
    )
    batched_model = BatchedInferencePipeline(model=model)
    return batched_model


def transcribe_faster(
    audio_path: Path,
    model,
    language: str,
    batch_size: int,
) -> dict[str, Any]:
    """Transcreve com faster-whisper usando um modelo já carregado."""
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        best_of=5,
        condition_on_previous_text=True,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        batch_size=batch_size,
    )

    segments_list = _segments_to_dicts(segments)
    full_text = " ".join(seg["text"] for seg in segments_list)

    return {
        "text": full_text,
        "language": info.language,
        "language_probability": info.language_probability,
        "segments": segments_list,
    }


def transcribe_openai(
    audio_path: Path,
    model_name: str,
    device: str,
    language: str,
) -> dict[str, Any]:
    """Transcreve com openai-whisper (fallback)."""
    import whisper

    model = whisper.load_model(model_name).to(device)
    result = model.transcribe(
        str(audio_path),
        fp16=(device != "cpu"),
        language=language,
        verbose=False,
    )
    return {
        "text": result.get("text", ""),
        "language": language,
        "language_probability": None,
        "segments": result.get("segments", []),
    }


def transcribe_single_file(
    audio_path: Path,
    output_dir: Path,
    engine: str = "faster",
    model_name: str = "small",
    device: str = "cuda" if torch.cuda.is_available() else "cpu",
    language: str = "pt",
    batch_size: int = 16,
    compute_type: str = "float16",
    keep_wav: bool = False,
    model=None,
) -> tuple[Path, Path]:
    """Transcreve um único arquivo de áudio e salva MD + JSON.

    Args:
        audio_path: caminho do MP3.
        output_dir: pasta onde serão salvos os artefatos.
        engine: "faster" ou "openai".
        model_name: modelo Whisper.
        device: "cuda" ou "cpu".
        language: idioma forçado.
        batch_size: batch para faster-whisper.
        compute_type: tipo de computação para faster-whisper.
        keep_wav: mantém o WAV temporário.
        model: modelo faster-whisper pré-carregado (opcional). Se None, carrega um novo.

    Returns:
        (caminho_md, caminho_json)
    """
    if not audio_path.exists():
        raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")

    if device.startswith("cuda") and not torch.cuda.is_available():
        print("Aviso: CUDA solicitado mas não disponível. Usando CPU.")
        device = "cpu"

    lesson_name = extract_lesson_name(audio_path)
    md_output = output_dir / f"{lesson_name}.md"
    json_output = output_dir / f"{lesson_name}.json"

    print(f"\nArquivo de entrada : {audio_path}")
    print(f"Engine             : {engine}")
    print(f"Modelo Whisper     : {model_name}")
    print(f"Dispositivo        : {device}")
    print(f"Idioma             : {language}")
    if engine == "faster":
        print(f"Batch size         : {batch_size}")
        print(f"Compute type       : {compute_type}")
    print(f"Saída Markdown     : {md_output}")
    print(f"Saída JSON         : {json_output}")

    wav_path: Path | None = None
    try:
        print("\nConvertendo áudio para WAV 16kHz mono ( FFmpeg )...")
        wav_path = Path(tempfile.gettempdir()) / f"{lesson_name}.wav"
        convert_to_wav(audio_path, wav_path)
        print(f"WAV temporário: {wav_path}")

        print("Carregando modelo e transcrevendo...")
        if engine == "faster":
            if model is None:
                model = load_faster_model(model_name, device, compute_type)
            result = transcribe_faster(wav_path, model, language, batch_size)
        else:
            result = transcribe_openai(wav_path, model_name, device, language)

        segments = result.get("segments", [])
        print(f"Transcrição concluída: {len(segments)} segmentos.")

        save_markdown(segments, md_output, audio_path, model_name, language, engine)
        save_json(result, json_output, audio_path, model_name, language, engine)

        print(f"Markdown salvo em: {md_output}")
        print(f"JSON salvo em: {json_output}")

        return md_output, json_output

    finally:
        if wav_path is not None and wav_path.exists() and not keep_wav:
            wav_path.unlink()
            print(f"WAV temporário removido: {wav_path}")
