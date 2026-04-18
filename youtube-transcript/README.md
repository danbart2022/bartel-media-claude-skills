# YouTube Transcript — Token-Efficient YouTube Transcription

Transcribes YouTube videos to text with minimal Claude context usage.  
A bundled Python script handles all the logic and writes output to a file —  
Claude reads it on demand instead of pulling everything into the conversation.

## How it works

```
YouTube URL
    │
    ▼
youtube-transcript-api ──── captions available? ──► clean text file
    │                              no
    ▼
yt-dlp (download audio)
    │
    ▼
local Whisper (transcribe)
    │
    ▼
clean text file
```

**Strategy 1** (instant): fetches YouTube's built-in auto-captions — no download, no API key.  
**Strategy 2** (fallback): downloads audio via yt-dlp and transcribes locally with OpenAI Whisper.

Both strategies are cross-platform (Mac, Linux, Windows).

## Requirements

```bash
pip3 install youtube-transcript-api yt-dlp openai-whisper
```

Whisper downloads its model on first use (~460 MB for `small`).  
No API key needed for either strategy.

## Installation as a Claude Code Skill

```bash
cp -r youtube-transcript ~/.claude/skills/
```

Claude Code picks up the skill automatically via `SKILL.md`.

## Usage

Just ask Claude:

> "Transcribe this video: https://www.youtube.com/watch?v=..."  
> "Summarize what's said in this YouTube video: https://youtu.be/..."

## Direct CLI usage

```bash
# Default (German, small model)
python3 scripts/yt_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

# English video, higher quality fallback
python3 scripts/yt_transcript.py "https://youtu.be/VIDEO_ID" --language en --model medium

# Custom output path
python3 scripts/yt_transcript.py "URL" --out ~/Desktop/transcript.txt
```

The script prints only the output file path to stdout — keeping your terminal and Claude's context clean.

## Whisper models (fallback only)

| Model | Size | Use case |
|-------|------|----------|
| `base` | 140 MB | Short clips, fast |
| `small` | 460 MB | **Default** — good balance |
| `medium` | 1.5 GB | Poor audio or technical terms |
| `large` | 3 GB | Maximum accuracy |
