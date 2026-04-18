---
name: whisper
description: >
  Transcribes audio files locally using OpenAI Whisper — no API key, no tokens.
  Use this skill whenever the user asks to "transcribe", "write down what's said",
  or provides a path to an audio file (.m4a, .mp3, .wav, .mp4, .ogg, .flac, .webm, .aac, .opus).
  Local processing always takes priority over API-based transcription.
---

# Whisper — Local Audio Transcription

Transcribes audio files fully locally using the OpenAI Whisper CLI.
No API key, no cloud, no token costs.

## Standard procedure

### Step 1 — Resolve file path

- Absolute path provided → use directly
- Only filename provided → search in:
  1. `~/Downloads/`
  2. `~/Desktop/`
  3. Current project directory

```bash
find ~/Downloads ~/Desktop -name "filename.m4a" 2>/dev/null | head -1
```

### Step 2 — Language

- Default: **German** (`--language German`)
- English explicitly requested → `--language English`
- Unknown → omit `--language` flag (Whisper auto-detects)

### Step 3 — Choose model

| Model | Use case | Size |
|-------|----------|------|
| `base` | Short notes < 2 min, very fast | 140 MB |
| `small` | **Default** — good & fast | 460 MB |
| `medium` | Poor audio quality, technical terms, > 10 min | 1.5 GB |
| `large` | Maximum quality, rarely needed | 3 GB |

**Default: `small`**

### Step 4 — Run Whisper

```bash
whisper "/absolute/path/to/file.m4a" \
  --language German \
  --model small \
  --output_format txt \
  --output_dir /tmp/whisper_out
```

**Note on first run:** The model is downloaded once (~460 MB for `small`).
Inform the user: *"Downloading Whisper model 'small', one-time ~460 MB..."*
Cache lives in `~/.cache/whisper/` and is reused on subsequent runs.

### Step 5 — Output result

```bash
cat /tmp/whisper_out/[filename].txt
```

- Output the transcript **directly in chat**
- For > 500 words: show full text + offer a short summary
- Clean up afterwards: `rm -rf /tmp/whisper_out`

---

## Quality issues?

If the result is unreadable or incomplete → automatically retry with `medium`:

```bash
whisper "/path/file.m4a" --language German --model medium --output_format txt --output_dir /tmp/whisper_out
```

---

## Whisper not found?

```bash
pip3 install openai-whisper
```

---

## Supported formats

`.m4a` `.mp3` `.wav` `.mp4` `.ogg` `.flac` `.webm` `.aac` `.opus`
