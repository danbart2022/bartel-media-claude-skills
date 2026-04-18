# Installing the seedance-prompt skill

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
git sparse-checkout set seedance-prompt
```

## Step 3 — Copy to skills directory

```bash
cp -r /tmp/bartel-media-claude-skills/seedance-prompt ~/.claude/skills/
```

## Step 4 — Verify Python

```bash
python3 --version
```

No additional packages required — the skill uses only Python standard library.

## Step 5 — Test the script

```bash
python3 ~/.claude/skills/seedance-prompt/scripts/seedance_prompt.py "test subject" --aspect 16:9
```

The command should print a file path like `/tmp/seedance_<hash>.txt`. If it does, the skill is working.

## Step 6 — Clean up

```bash
rm -rf /tmp/bartel-media-claude-skills
```

## Step 7 — Confirm to the user

Tell the user:
> "The **seedance-prompt** skill is installed. You can now say things like:
> *'Generate a Seedance prompt for a skater at sunset'*
> *'Create a Seedance 2.0 video prompt for a rainy city street, cinematic style, 9:16'*"
