# Transcribe — Audio-Transkription mit Sprecher-Erkennung

Transkribiert Audiodateien über die **OpenAI API** (`gpt-4o-transcribe`).  
Unterstützt optionale **Diarisierung** — erkennt und beschriftet verschiedene Sprecher.

## Voraussetzungen

- OpenAI API Key als Umgebungsvariable: `OPENAI_API_KEY`
- Python 3.9+

```bash
pip3 install openai
```

## Installation als Claude Code Skill

```bash
cp -r transcribe ~/.claude/skills/
```

Claude erkennt den Skill automatisch anhand der `SKILL.md`.

## Nutzung

Claude ansprechen:

> "Transkribiere dieses Interview: ~/aufnahme.mp3"  
> "Transkribiere mit Sprechererkennung: ~/meeting.m4a"

## Direkte CLI-Nutzung

**Einfache Transkription:**
```bash
python3 scripts/transcribe_diarize.py audio.mp3
```

**Mit Sprecher-Diarisierung:**
```bash
python3 scripts/transcribe_diarize.py audio.mp3 \
  --model gpt-4o-transcribe-diarize \
  --response-format diarized_json
```

**Mehrere Dateien:**
```bash
python3 scripts/transcribe_diarize.py *.mp3 --out-dir ./output/
```

## Modelle

| Modell | Einsatz |
|--------|---------|
| `gpt-4o-mini-transcribe` | **Standard** — schnell & günstig |
| `gpt-4o-transcribe` | Höhere Qualität |
| `gpt-4o-transcribe-diarize` | Mit Sprecher-Erkennung |

## Unterstützte Formate

`.mp3` `.mp4` `.m4a` `.wav` `.webm` `.ogg` `.flac`
