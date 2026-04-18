# Installing the transcribe skill

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
git sparse-checkout set transcribe
```

## Step 3 — Copy to skills directory

```bash
cp -r /tmp/bartel-media-claude-skills/transcribe ~/.claude/skills/
```

## Step 4 — Install dependency

```bash
pip3 install openai
```

If `pip3` is not available, try `pip` or `python3 -m pip install openai`.

## Step 5 — Check for API key

Check if `OPENAI_API_KEY` is set:

```bash
echo ${OPENAI_API_KEY:0:4}
```

If the output is empty, inform the user:
> "You need an OpenAI API key for this skill. Set it in your shell:
> `export OPENAI_API_KEY=your-key-here`
> Get a key at https://platform.openai.com/api-keys"

## Step 6 — Clean up

```bash
rm -rf /tmp/bartel-media-claude-skills
```

## Step 7 — Confirm to the user

Tell the user:
> "The **transcribe** skill is installed. You can now say things like:
> *'Transcribe this interview: ~/recording.mp3'*
> *'Transcribe with speaker detection: ~/meeting.m4a'*"
