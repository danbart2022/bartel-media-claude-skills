# Installing the youtube-transcript skill

Follow these steps exactly when the user asks to install this skill.

## Step 1 — Ensure the skills directory exists

```bash
mkdir -p ~/.claude/skills
```

## Step 2 — Download the skill

```bash
git clone --depth=1 --filter=blob:none --sparse \
  https://github.com/danbart2022/bartel-media-claude-skills.git \
  /tmp/bartel-media-claude-skills

cd /tmp/bartel-media-claude-skills
git sparse-checkout set youtube-transcript
```

## Step 3 — Copy to skills directory

```bash
cp -r /tmp/bartel-media-claude-skills/youtube-transcript ~/.claude/skills/
```

## Step 4 — Install dependencies

```bash
pip3 install youtube-transcript-api yt-dlp openai-whisper
```

If `pip3` is not available, try `pip` or `python3 -m pip install ...`.

> Note: `openai-whisper` is only used as a fallback when a video has no captions.
> On first fallback use, Whisper downloads the `small` model (~460 MB). Inform the user.

## Step 5 — Clean up

```bash
rm -rf /tmp/bartel-media-claude-skills
```

## Step 6 — Confirm to the user

Tell the user:
> "The **youtube-transcript** skill is installed. You can now say things like:
> *'Transcribe this video: https://www.youtube.com/watch?v=...'*
> *'Summarize what's said in this YouTube video: https://youtu.be/...'*"
