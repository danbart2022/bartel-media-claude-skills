---
name: youtube-transcript
description: >
  Transcribes YouTube videos to text. Use whenever the user provides a YouTube URL
  and asks to transcribe, summarize, or extract the content of a video.
  Tries YouTube's built-in captions first (fast, no download).
  Falls back to yt-dlp + local Whisper if no captions are available.
tools:
  - Bash
  - Read
---

# YouTube Transcript Skill

Token-efficient YouTube transcription via a bundled Python script.
The script writes output to a file — Claude reads it on demand, never floods the context.

## Workflow

### Step 1 — Run the script

```bash
python3 ~/.claude/skills/youtube-transcript/scripts/yt_transcript.py "YOUTUBE_URL"
```

The script prints **only the output file path** to stdout. Save it.

Optional flags:
- `--language de` — target language for captions / Whisper (default: `de`)
- `--model small` — Whisper model for fallback (default: `small`)
- `--out /path/to/output.txt` — custom output path

### Step 2 — Read the result

```bash
cat /tmp/yt_<video_id>.txt
```

Read the file only when you need the content. Do not pipe the transcript directly
into the conversation unless the user explicitly asks for the full text.

### Step 3 — Present to user

- Short video (< 10 min): offer full transcript + 5–10 bullet summary
- Long video (> 10 min): offer summary only, full transcript on request

---

## Transcription strategies (automatic, in order)

| # | Method | Requires | Speed |
|---|--------|----------|-------|
| 1 | `youtube-transcript-api` | pip package | Instant — no download |
| 2 | `yt-dlp` + local `whisper` | yt-dlp + openai-whisper | Slower — downloads audio |

Strategy 2 is cross-platform (Mac, Linux, Windows) but requires Whisper installed locally.

---

## Installation

```bash
pip3 install youtube-transcript-api yt-dlp openai-whisper
```

Whisper downloads its model on first use (~460 MB for `small`).

---

## Supported URL formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- Plain video ID: `VIDEO_ID`
