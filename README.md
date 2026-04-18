# Bartel Media Claude Skills

A collection of Claude Code skills for everyday use — developed and curated by [Bartel Media](https://bartel-media.de).

## What are Claude Code Skills?

Skills are extensions for [Claude Code](https://claude.ai/code) that teach Claude to perform specific tasks autonomously and consistently. Each skill consists of a `SKILL.md` that Claude uses as its instruction set.

## Skills

| Skill | Description | API Key required |
|-------|-------------|-----------------|
| [whisper](./whisper/) | Local audio transcription via OpenAI Whisper CLI | ❌ |
| [transcribe](./transcribe/) | Cloud audio transcription + speaker diarization via OpenAI API | ✅ OpenAI |
| [youtube-transcript](./youtube-transcript/) | Transcribe YouTube videos — captions first, local Whisper fallback | ❌ |

## Installation

Install a single skill:

```bash
cp -r whisper ~/.claude/skills/
```

Install all skills at once:

```bash
for skill in whisper transcribe youtube-transcript; do
  cp -r "$skill" ~/.claude/skills/
done
```

Claude Code automatically detects skills placed in `~/.claude/skills/`.

## License

MIT
