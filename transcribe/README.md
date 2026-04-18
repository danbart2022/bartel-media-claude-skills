# Transcribe — Audio Transcription with Speaker Diarization

Transcribes audio files via the **OpenAI API** (`gpt-4o-transcribe`).  
Supports optional **diarization** — identifies and labels different speakers.

## Requirements

- OpenAI API key set as an environment variable: `OPENAI_API_KEY`
- Python 3.9+

```bash
pip3 install openai
```

## Installation as a Claude Code Skill

```bash
cp -r transcribe ~/.claude/skills/
```

Claude Code picks up the skill automatically via `SKILL.md`.

## Usage

Just ask Claude:

> "Transcribe this interview: ~/recording.mp3"  
> "Transcribe with speaker detection: ~/meeting.m4a"

## Direct CLI usage

**Simple transcription:**
```bash
python3 scripts/transcribe_diarize.py audio.mp3
```

**With speaker diarization:**
```bash
python3 scripts/transcribe_diarize.py audio.mp3 \
  --model gpt-4o-transcribe-diarize \
  --response-format diarized_json
```

**Multiple files:**
```bash
python3 scripts/transcribe_diarize.py *.mp3 --out-dir ./output/
```

## Models

| Model | Use case |
|-------|----------|
| `gpt-4o-mini-transcribe` | **Default** — fast & cost-efficient |
| `gpt-4o-transcribe` | Higher quality |
| `gpt-4o-transcribe-diarize` | With speaker recognition |

## Supported formats

`.mp3` `.mp4` `.m4a` `.wav` `.webm` `.ogg` `.flac`
