# Bartel Media Claude Skills

Eine Sammlung von Claude Code Skills für den täglichen Einsatz — entwickelt und kuratiert von [Bartel Media](https://bartel-media.de).

## Was sind Claude Code Skills?

Skills sind Erweiterungen für [Claude Code](https://claude.ai/code), die Claude beibringen, bestimmte Aufgaben eigenständig und konsistent auszuführen. Jeder Skill besteht aus einer `SKILL.md`, die Claude als Anweisung dient.

## Skills

| Skill | Beschreibung | API-Key nötig |
|-------|-------------|---------------|
| [whisper](./whisper/) | Lokale Audio-Transkription mit OpenAI Whisper | ❌ |
| [transcribe](./transcribe/) | Audio-Transkription + Sprecher-Erkennung via OpenAI API | ✅ OpenAI |

## Installation

Einzelnen Skill installieren:

```bash
cp -r whisper ~/.claude/skills/
```

Alle Skills auf einmal:

```bash
for skill in whisper transcribe; do
  cp -r "$skill" ~/.claude/skills/
done
```

Claude Code erkennt Skills automatisch im Verzeichnis `~/.claude/skills/`.

## Lizenz

MIT
