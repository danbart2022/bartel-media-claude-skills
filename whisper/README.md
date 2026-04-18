# Whisper — Local Audio Transcription

Transcribes audio files fully **locally** using the OpenAI Whisper CLI.  
No API key, no cloud, no token costs.

## Requirements

```bash
pip3 install openai-whisper
```

On first use, Whisper downloads the selected model automatically (~460 MB for `small`).

## Installation as a Claude Code Skill

```bash
cp -r whisper ~/.claude/skills/
```

Claude Code picks up the skill automatically via `SKILL.md`.

## Usage

Just ask Claude:

> "Transcribe this file: ~/Downloads/recording.m4a"  
> "Write down what's said in: /path/to/voicenote.opus"

## Direct CLI usage

```bash
whisper "/path/to/file.m4a" \
  --language German \
  --model small \
  --output_format txt \
  --output_dir /tmp/whisper_out
```

## Models

| Model | Use case | Size |
|-------|----------|------|
| `base` | Short notes < 2 min | 140 MB |
| `small` | **Default** — good & fast | 460 MB |
| `medium` | Poor audio quality or technical terms | 1.5 GB |
| `large` | Maximum quality | 3 GB |

## Supported formats

`.m4a` `.mp3` `.wav` `.mp4` `.ogg` `.flac` `.webm` `.aac` `.opus`
