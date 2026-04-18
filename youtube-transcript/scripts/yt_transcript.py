#!/usr/bin/env python3
"""
yt_transcript.py — Token-efficient YouTube transcription for Claude Code.

Strategy:
  1. youtube-transcript-api  (fast, no download, uses YouTube captions)
  2. yt-dlp + whisper         (fallback when no captions available)

Output is written to a file. Only the file path is printed to stdout,
so Claude reads the result on demand instead of flooding the context.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_video_id(url: str) -> str:
    patterns = [
        r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})",
        r"(?:embed/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    sys.exit(f"[ERROR] Could not extract video ID from: {url}")


def clean_text(segments) -> str:
    lines = []
    for entry in segments:
        text = getattr(entry, "text", str(entry))
        text = text.strip().replace("\n", " ")
        if text:
            lines.append(text)
    return " ".join(lines)


def write_output(text: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(str(out_path))  # only this line reaches Claude's context


# ---------------------------------------------------------------------------
# Strategy 1 — youtube-transcript-api
# ---------------------------------------------------------------------------

def try_api(video_id: str, languages: list[str]) -> str | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
    except ImportError:
        print("[INFO] youtube-transcript-api not installed, skipping.", file=sys.stderr)
        return None

    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(video_id, languages=languages)
        return clean_text(transcript)
    except (NoTranscriptFound, TranscriptsDisabled) as e:
        print(f"[INFO] No captions via API ({e}), falling back to yt-dlp + whisper.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[WARN] API error: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Strategy 2 — yt-dlp + whisper
# ---------------------------------------------------------------------------

def find_whisper() -> str | None:
    for candidate in ["whisper", "whisper-ctranslate2"]:
        result = subprocess.run(["which", candidate], capture_output=True, text=True)
        if result.returncode == 0:
            return candidate
    return None


def try_yt_dlp_whisper(url: str, language: str, model: str) -> str | None:
    whisper_bin = find_whisper()
    if not whisper_bin:
        sys.exit("[ERROR] Whisper not found. Install with: pip3 install openai-whisper")

    tmp_dir = Path(tempfile.mkdtemp(prefix="yt_transcript_"))
    audio_path = tmp_dir / "audio.%(ext)s"

    print("[INFO] Downloading audio with yt-dlp...", file=sys.stderr)
    dl = subprocess.run(
        [
            "yt-dlp", "-x",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", str(audio_path),
            url,
        ],
        capture_output=True, text=True,
    )
    if dl.returncode != 0:
        sys.exit(f"[ERROR] yt-dlp failed:\n{dl.stderr}")

    mp3_files = list(tmp_dir.glob("*.mp3"))
    if not mp3_files:
        sys.exit("[ERROR] yt-dlp produced no mp3 file.")
    mp3 = mp3_files[0]

    print(f"[INFO] Transcribing with whisper ({model})...", file=sys.stderr)
    whisper_out = tmp_dir / "whisper"
    w = subprocess.run(
        [
            whisper_bin, str(mp3),
            "--language", language,
            "--model", model,
            "--output_format", "txt",
            "--output_dir", str(whisper_out),
        ],
        capture_output=True, text=True,
    )
    if w.returncode != 0:
        sys.exit(f"[ERROR] Whisper failed:\n{w.stderr}")

    txt_files = list(whisper_out.glob("*.txt"))
    if not txt_files:
        sys.exit("[ERROR] Whisper produced no output file.")

    text = txt_files[0].read_text(encoding="utf-8").strip()

    # cleanup
    for f in tmp_dir.rglob("*"):
        if f.is_file():
            f.unlink()
    tmp_dir.rmdir() if not any(tmp_dir.iterdir()) else None

    return text


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe a YouTube video to a text file.")
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("--language", default="de", help="Language code (default: de)")
    parser.add_argument("--model", default="small", help="Whisper model for fallback (default: small)")
    parser.add_argument("--out", default=None, help="Output file path (default: /tmp/yt_<id>.txt)")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    out_path = Path(args.out) if args.out else Path(f"/tmp/yt_{video_id}.txt")

    # Strategy 1
    text = try_api(video_id, languages=[args.language, "en"])

    # Strategy 2
    if not text:
        text = try_yt_dlp_whisper(args.url, language=args.language, model=args.model)

    if not text:
        sys.exit("[ERROR] Transcription failed with all strategies.")

    write_output(text, out_path)


if __name__ == "__main__":
    main()
