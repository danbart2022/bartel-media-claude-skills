# Seedance Prompt — Seedance 2.0 Prompt Generator

Generates professional, copy-ready [Seedance 2.0](https://seedance.ai) timeline prompts.
A bundled Python script collects and validates parameters — Claude writes the creative prompt.

## How it works

```
User input
    │
    ▼
seedance_prompt.py ──── collects & validates params ──► brief file (/tmp/seedance_*.txt)
                                                              │
                                                              ▼
                                                        Claude reads brief
                                                              │
                                                              ▼
                                                   Complete Seedance 2.0 prompt
```

## Two modes

### Express — all params upfront, instant result

```bash
python3 scripts/seedance_prompt.py "skater at sunset" \
  --style cinematic \
  --light golden-hour \
  --mood energetic \
  --aspect 16:9 \
  --scenes 5
```

### Minimal — Claude fills in the gaps

```bash
python3 scripts/seedance_prompt.py "rainy city street at night"
```

Claude will ask for missing parameters, then re-run with your answers.

## Installation as a Claude Code Skill

```bash
cp -r seedance-prompt ~/.claude/skills/
```

Claude Code picks up the skill automatically via `SKILL.md`.

## All parameters

| Flag | Options | Default |
|------|---------|---------|
| `--style` | `cinematic` `anime` `commercial` `ugc` `atmospheric` `retro` `vfx` `portrait` | auto |
| `--light` | `golden-hour` `blue-hour` `neon` `window` `studio` `rim` `backlight` `noir` `candle` `overcast` `rembrandt` | auto |
| `--color` | `warm` `cool` `vibrant` `muted` `bw` `neon` `pastel` | auto |
| `--texture` | `film-grain` `soft-blur` `sharp` `bokeh` `lo-fi` | auto |
| `--mood` | `epic` `chill` `energetic` `romantic` `mystic` `melancholic` `luxury` `humorous` | auto |
| `--camera-size` | `extreme-wide` `wide` `medium` `close-up` `extreme-close` `mix` | auto |
| `--camera-angle` | `eye-level` `low` `high` `pov` `dutch` `birds-eye` `mix` | auto |
| `--camera-move` | `static` `dolly-in` `dolly-out` `tracking` `pan` `tilt` `aerial` `handheld` `orbit` `zoom` `slow-mo` `mix` | auto |
| `--structure` | `single` `short-film` `action` `story` `loop` | auto |
| `--aspect` | `16:9` `9:16` `1:1` | `16:9` |
| `--scenes` | `1`–`6` | `5` |
| `--assets` | e.g. `@Image1 as first frame` | — |
| `--out` | custom output path | `/tmp/seedance_<hash>.txt` |

See `references/parameters.md` for full descriptions of every option.

## Requirements

No dependencies beyond Python 3.6+. No API key needed.

## Example output

Given:
```bash
python3 scripts/seedance_prompt.py "woman reading in a rainy cafe" \
  --style atmospheric --light window --mood chill --aspect 9:16 --scenes 4
```

Claude generates:

**Woman in the Rain Cafe** — Atmospheric | Chill | 9:16 | 4 Scenes

```
[Scene context: Cozy cafe interior on a rainy afternoon, soft natural window light filtering through fogged glass, warm interior tones contrasting cool grey outside. Ethereal and dreamlike atmosphere, soft light bloom, dark moody atmospheric quality, 4K.]

[Scene 1: 0:00-0:05] Wide shot, static locked-off, rain streaking down the cafe window, blurred figures inside visible through glass, reflections of warm light on wet street outside.
[Scene 2: 0:05-0:10] Medium shot, slow dolly push-in, woman seated at window table, open book resting in her hands, soft window light falling across the pages, steam rising from her cup.
[Scene 3: 0:10-0:15] Close-up, static locked-off, her eyes moving slowly across the page, raindrops casting shifting shadows across her face through the window.
[Scene 4: 0:15-0:20] Extreme wide shot, slow dolly pull-back, cafe receding into the rainy street scene, warm glow of the interior shrinking against the grey afternoon. Avoid jitter, avoid temporal flicker.
```

📊 Atmospheric | Chill | 9:16 | 4 Scenes
