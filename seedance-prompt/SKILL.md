---
name: seedance-prompt
description: >
  Generates professional Seedance 2.0 video prompts. Use whenever the user wants
  to create a video, film, or animation with Seedance — even for vague inputs like
  "make me a clip", "I need a video", or when a scene or concept is described.
tools:
  - Bash
  - Read
---

# Seedance 2.0 Prompt Generator

Generates complete, copy-ready Seedance 2.0 timeline prompts.
Uses a bundled Python script to collect parameters — Claude writes the final prompt.

---

## Two modes

### Express mode — user provides details upfront

Run the script with known parameters. Claude fills in anything left as `auto`.

```bash
python3 ~/.claude/skills/seedance-prompt/scripts/seedance_prompt.py "SUBJECT" \
  --style cinematic \
  --light golden-hour \
  --mood energetic \
  --aspect 16:9 \
  --scenes 5
```

Read the brief file the script prints, then generate the prompt.

### Interview mode — subject only, Claude asks questions

If the user gives only a vague idea, run with subject only:

```bash
python3 ~/.claude/skills/seedance-prompt/scripts/seedance_prompt.py "SUBJECT"
```

Then ask the user for missing parameters using the question guide in
`references/parameters.md`. Re-run the script with collected answers, then generate.

---

## Generating the prompt

After reading the brief file, write a complete Seedance 2.0 timeline prompt.

**Rules (non-negotiable):**
- One camera movement per scene — never combine two
- No `fast`, `quickly`, `amazing`, `epic`, `stunning` — describe concretely
- Global context block first: 1–3 sentences covering atmosphere, style, light, quality
- Scene format: `[Scene N: MM:SS-MM:SS] [shot type], [camera move], [subject action], [visual detail].`
- Last scene always ends with: `Avoid jitter, avoid temporal flicker.`
- Output the prompt inside a single fenced code block — raw, copy-ready

**Output structure:**
1. Short title (outside code block)
2. One fenced code block with the complete prompt
3. Specs line: `📊 [Style] | [Mood] | [Aspect] | [N] Scenes`
4. Ask: "Want a variant with a different style or camera perspective?"

---

## All valid parameter values

See `references/parameters.md` for the full list of choices per parameter.

---

## Seedance 2.0 grammar reference

### Scene context block
```
[Scene context: Atmosphere, setting, style, lighting, quality — 1–3 sentences.]
```

### Scene line
```
[Scene N: MM:SS-MM:SS] [Shot type], [camera move], [subject action], [visual detail].
```

### Camera moves (one per scene)
`static locked-off` · `slow dolly push-in` · `slow dolly pull-back` · `tracking shot following the subject` · `gentle pan` · `slow tilt up` · `aerial drone shot pulling back` · `handheld slight camera shake` · `slow orbit around the subject` · `subtle zoom in` · `slow motion`

### Edit prompt (for modifying existing videos)
```
[Action] @Video1 (Extend by Xs / Re-plot / Replace A with B),
[New Details: I @Assets / II Content / III Camera],
while keeping the original [Style/Camera/Character].
```
