# Installing the whisper skill

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
git sparse-checkout set whisper
```

## Step 3 — Copy to skills directory

```bash
cp -r /tmp/bartel-media-claude-skills/whisper ~/.claude/skills/
```

## Step 4 — Install dependency

```bash
pip3 install openai-whisper
```

If `pip3` is not available, try `pip` or `python3 -m pip install openai-whisper`.

> Note: On first use, Whisper downloads the `small` model (~460 MB). Inform the user.

## Step 5 — Clean up

```bash
rm -rf /tmp/bartel-media-claude-skills
```

## Step 6 — Confirm to the user

Tell the user:
> "The **whisper** skill is installed. You can now say things like:
> *'Transcribe this file: ~/Downloads/recording.m4a'*"
