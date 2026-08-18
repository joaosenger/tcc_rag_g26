"""Transcreve todas as aulas MP3 de uma só vez.

As transcrições são salvas em Markdown + JSON dentro de content/audio/transcriptions/.

Uso:
    python content/audio/transcribe_all.py
    python content/audio/transcribe_all.py --batch-size 32
    python content/audio/transcribe_all.py --no-skip-existing
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import timedelta
from pathlib import Path

import torch

from audio_transcript import load_faster_model, transcribe_single_file


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcreve todas as aulas MP3 do diretório content/audio/."
    )
    parser.add_argument(
        "--audio-dir",
        type=Path,
        default=Path("content/audio"),
        help="Diretório com os arquivos MP3 (padrão: content/audio).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("content/audio/transcriptions"),
        help="Diretório onde serão salvos os artefatos (padrão: content/audio/transcriptions).",
    )
    parser.add_argument(
        "--engine",
        type=str,
        default="faster",
        choices=["faster", "openai"],
        help="Engine de transcrição (padrão: faster).",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="small",
        help="Modelo Whisper (padrão: small).",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda" if torch.cuda.is_available() else "cpu",
        help="Dispositivo para inferência (padrão: cuda se disponível).",
    )
    parser.add_argument(
        "--language",
        type=str,
        default="pt",
        help="Código do idioma forçado (padrão: pt).",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
        help="Tamanho do batch para faster-whisper (padrão: 16).",
    )
    parser.add_argument(
        "--compute-type",
        type=str,
        default="float16",
        choices=["int8", "int8_float16", "int16", "float16", "float32"],
        help="Tipo de computação para faster-whisper (padrão: float16).",
    )
    parser.add_argument(
        "--skip-existing",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Pula aulas já transcritas (padrão: True).",
    )
    parser.add_argument(
        "--keep-wav",
        action="store_true",
        help="Mantém os arquivos WAV temporários (útil para debug).",
    )
    return parser.parse_args(argv)


def find_pending_mp3s(audio_dir: Path, output_dir: Path, skip_existing: bool) -> list[Path]:
    """Retorna a lista de MP3 que ainda precisam ser transcritos."""
    mp3_files = sorted(audio_dir.glob("*.mp3"))
    if not mp3_files:
        return []

    if not skip_existing:
        return mp3_files

    pending = []
    for mp3 in mp3_files:
        lesson_name = mp3.stem
        md_file = output_dir / f"{lesson_name}.md"
        json_file = output_dir / f"{lesson_name}.json"
        if md_file.exists() and json_file.exists():
            print(f"[PULAR] {mp3.name} já transcrito.")
        else:
            pending.append(mp3)

    return pending


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.device.startswith("cuda") and not torch.cuda.is_available():
        print("Aviso: CUDA solicitado mas não disponível. Usando CPU.", file=sys.stderr)
        args.device = "cpu"

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Diretório de áudio : {args.audio_dir}")
    print(f"Diretório de saída : {args.output_dir}")
    print(f"Engine             : {args.engine}")
    print(f"Modelo             : {args.model}")
    print(f"Dispositivo        : {args.device}")
    print(f"Batch size         : {args.batch_size}")
    print(f"Compute type       : {args.compute_type}")
    print(f"Pular existentes   : {args.skip_existing}")
    print("-" * 60)

    pending = find_pending_mp3s(args.audio_dir, args.output_dir, args.skip_existing)

    if not pending:
        print("Nenhum arquivo MP3 pendente de transcrição.")
        return 0

    print(f"\nAulas a transcrever: {len(pending)}")
    for mp3 in pending:
        print(f"  - {mp3.name}")

    # Carrega o modelo uma única vez para todo o lote.
    model = None
    if args.engine == "faster":
        print("\nCarregando modelo faster-whisper na GPU/CPU...")
        model = load_faster_model(args.model, args.device, args.compute_type)
        print("Modelo carregado.")

    start_total = time.monotonic()
    processed = 0
    errors: list[tuple[str, str]] = []

    try:
        for idx, mp3 in enumerate(pending, start=1):
            print(f"\n{'=' * 60}")
            print(f"[{idx}/{len(pending)}] Processando {mp3.name}...")
            print("=" * 60)

            start_file = time.monotonic()
            transcribe_single_file(
                audio_path=mp3,
                output_dir=args.output_dir,
                engine=args.engine,
                model_name=args.model,
                device=args.device,
                language=args.language,
                batch_size=args.batch_size,
                compute_type=args.compute_type,
                keep_wav=args.keep_wav,
                model=model,
            )
            elapsed_file = time.monotonic() - start_file
            print(f"Tempo da aula: {timedelta(seconds=int(elapsed_file))}")
            processed += 1

    except Exception as exc:
        errors.append((mp3.name, str(exc)))
        print(f"\n[ERRO] Falha ao processar {mp3.name}: {exc}", file=sys.stderr)
        raise  # Para tudo conforme solicitado.

    finally:
        elapsed_total = time.monotonic() - start_total
        print("\n" + "=" * 60)
        print("RESUMO")
        print("=" * 60)
        print(f"Total de aulas no lote : {len(pending)}")
        print(f"Processadas com sucesso: {processed}")
        print(f"Puladas (já existiam)  : {len(pending) - processed - len(errors)}")
        print(f"Falhas                 : {len(errors)}")
        if errors:
            print(f"Parado em              : {errors[0][0]}")
        print(f"Tempo total            : {timedelta(seconds=int(elapsed_total))}")
        print(f"Arquivos salvos em     : {args.output_dir}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
