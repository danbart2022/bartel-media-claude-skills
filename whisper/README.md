# Whisper — Lokale Audio-Transkription

Transkribiert Audiodateien vollständig **lokal** mit OpenAI Whisper CLI.  
Kein API-Key, keine Cloud, keine Token-Kosten.

## Voraussetzungen

```bash
pip3 install openai-whisper
```

Beim ersten Aufruf lädt Whisper das gewählte Modell automatisch herunter (~460 MB für `small`).

## Installation als Claude Code Skill

```bash
cp -r whisper ~/.claude/skills/
```

Claude erkennt den Skill automatisch anhand der `SKILL.md`.

## Nutzung

Einfach Claude ansprechen:

> "Transkribiere diese Datei: ~/Downloads/aufnahme.m4a"  
> "Schreib mir diese Sprachnachricht ab: /pfad/zur/datei.opus"

## Direkte CLI-Nutzung

```bash
whisper "/pfad/zur/datei.m4a" \
  --language German \
  --model small \
  --output_format txt \
  --output_dir /tmp/whisper_out
```

## Modelle

| Modell | Einsatz | Größe |
|--------|---------|-------|
| `base` | Kurze Notizen < 2 Min | 140 MB |
| `small` | **Standard** — gut & schnell | 460 MB |
| `medium` | Schlechte Qualität oder Fachbegriffe | 1,5 GB |
| `large` | Maximale Qualität | 3 GB |

## Unterstützte Formate

`.m4a` `.mp3` `.wav` `.mp4` `.ogg` `.flac` `.webm` `.aac` `.opus`
