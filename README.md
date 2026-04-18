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
| [seedance-prompt](./seedance-prompt/) | Generate professional Seedance 2.0 video prompts via CLI | ❌ |

## Installation

### Via Claude Code (recommended)

Just tell Claude:

> *"Install the whisper skill from https://github.com/danbart2022/bartel-media-claude-skills"*

Claude reads the `INSTALL.md` inside each skill folder and handles everything automatically — downloading, copying, installing dependencies, and confirming when done.

### Manually

Clone the repo and copy the skill folder:

```bash
git clone --depth=1 https://github.com/danbart2022/bartel-media-claude-skills.git
cp -r bartel-media-claude-skills/whisper ~/.claude/skills/
```

Claude Code automatically detects skills placed in `~/.claude/skills/`.

## License

MIT
