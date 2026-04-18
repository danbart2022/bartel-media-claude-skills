#!/usr/bin/env python3
"""
seedance_prompt.py — Seedance 2.0 prompt brief generator for Claude Code.

Collects and validates all parameters, then writes a structured brief to a file.
Claude reads the brief and generates the final prompt using Seedance 2.0 grammar.

Usage:
  # Express mode — all params via flags
  python3 seedance_prompt.py "skater at sunset" --style cinematic --light golden-hour --mood energetic --aspect 16:9

  # Minimal — Claude fills in missing params
  python3 seedance_prompt.py "rainy city street at night"

  # Full control
  python3 seedance_prompt.py "woman reading in a cafe" \\
    --style atmospheric --light window --color muted --texture film-grain \\
    --mood chill --camera-size close-up --camera-angle eye-level \\
    --camera-move dolly-in --structure single --aspect 9:16 --scenes 1
"""

import argparse
import hashlib
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Parameter lookup tables
# ---------------------------------------------------------------------------

STYLES = {
    "cinematic":   "cinematic 35mm film grain, Kodak color palette, anamorphic lens flares",
    "anime":       "Studio Ghibli aesthetic, hand-drawn warmth, cel-shaded anime style",
    "commercial":  "contemporary commercial style, bright and clean, sleek and polished",
    "ugc":         "social media UGC style, authentic and raw, handheld naturalistic",
    "atmospheric": "ethereal and dreamlike, soft light bloom, dark moody atmospheric",
    "retro":       "VHS tape aesthetic, scanlines, Super 8 film, warm grain, light leaks",
    "vfx":         "experimental VFX, particles, energy waves, abstract motion",
    "portrait":    "portrait photography style, mixed with dreamcore and fantasy",
}

LIGHTS = {
    "golden-hour": "warm golden hour sunlight, long soft shadows",
    "blue-hour":   "blue twilight, cool desaturated tones",
    "neon":        "neon reflections on wet pavement, cyberpunk glow",
    "window":      "soft natural window light, no harsh shadows",
    "studio":      "clean studio lighting, soft box, neutral background",
    "rim":         "dramatic rim light, subject edge highlights",
    "backlight":   "strong backlight creating silhouette effect",
    "noir":        "hard chiaroscuro lighting, deep dramatic shadows",
    "candle":      "warm candlelight flickering, intimate low key",
    "overcast":    "soft diffused overcast light, even exposure",
    "rembrandt":   "Rembrandt lighting, texture light, visible god rays",
}

COLORS = {
    "warm":    "warm amber tones, golden highlights",
    "cool":    "cool blue color temperature, desaturated",
    "vibrant": "vibrant high saturation, punchy colors",
    "muted":   "muted desaturated tones, film fade",
    "bw":      "black and white high contrast",
    "neon":    "dark base with neon accent pops",
    "pastel":  "pastel soft tones, light and airy",
}

TEXTURES = {
    "film-grain": "cinematic 35mm film grain",
    "soft-blur":  "soft long-shutter blur, glowing highlights",
    "sharp":      "ultra sharp, crisp detail, no grain",
    "bokeh":      "rich layers, bokeh background, shallow depth of field",
    "lo-fi":      "VHS texture, scanlines, color bleeding",
}

MOODS = {
    "epic":         "epic and dramatic",
    "chill":        "relaxed and calming, healing atmosphere",
    "energetic":    "energetic and dynamic",
    "romantic":     "romantic and intimate",
    "mystic":       "mystical and surreal",
    "melancholic":  "melancholic and nostalgic",
    "luxury":       "luxurious and premium",
    "humorous":     "light-hearted and playful",
}

CAMERA_SIZES = {
    "extreme-wide": "extreme wide establishing shot",
    "wide":         "wide shot",
    "medium":       "medium shot",
    "close-up":     "close-up shot",
    "extreme-close":"extreme close-up",
    "mix":          "varied shot sizes across scenes",
}

CAMERA_ANGLES = {
    "eye-level":  "eye level",
    "low":        "low angle looking up",
    "high":       "high angle looking down",
    "pov":        "POV first-person perspective",
    "dutch":      "dutch angle tilt",
    "birds-eye":  "bird's eye top-down view",
    "mix":        "varied angles across scenes",
}

CAMERA_MOVES = {
    "static":    "static locked-off shot",
    "dolly-in":  "slow dolly push-in",
    "dolly-out": "slow dolly pull-back",
    "tracking":  "tracking shot following the subject",
    "pan":       "gentle pan",
    "tilt":      "slow tilt up",
    "aerial":    "aerial drone shot pulling back",
    "handheld":  "handheld slight camera shake",
    "orbit":     "slow orbit around the subject",
    "zoom":      "subtle zoom in",
    "slow-mo":   "slow motion with reduced movement",
    "mix":       "varied camera movements across scenes",
}

STRUCTURES = {
    "single":     "single scene (4–6 seconds), focused and still",
    "short-film": "short film sequence, 4–6 scenes, narrative build (~20 seconds)",
    "action":     "action sequence, 5–6 scenes, dynamic cuts",
    "story":      "story arc — setup, peak, resolution",
    "loop":       "looping atmospheric, no action, pure mood",
}

ASPECTS = {
    "16:9": "16:9 widescreen",
    "9:16": "9:16 vertical, dynamic close framing",
    "1:1":  "1:1 square, centered composition",
}

# ---------------------------------------------------------------------------
# Brief builder
# ---------------------------------------------------------------------------

def resolve(table: dict, key: str | None, label: str) -> tuple[str, str]:
    """Returns (key, description). Falls back to 'claude-decides' if key is None."""
    if key is None:
        return ("auto", f"[Claude decides based on subject and mood]")
    key = key.lower()
    if key not in table:
        valid = ", ".join(table.keys())
        sys.exit(f"[ERROR] Invalid {label}: '{key}'. Valid options: {valid}")
    return (key, table[key])


def build_brief(args: argparse.Namespace) -> str:
    lines = ["# Seedance 2.0 Prompt Brief", ""]
    lines.append(f"Subject: {args.subject}")
    lines.append("")

    def row(label, table, val):
        key, desc = resolve(table, val, label)
        lines.append(f"{label}: {key} | {desc}")

    row("Style",         STYLES,        args.style)
    row("Light",         LIGHTS,        args.light)
    row("Color",         COLORS,        args.color)
    row("Texture",       TEXTURES,      args.texture)
    row("Mood",          MOODS,         args.mood)
    row("Camera size",   CAMERA_SIZES,  args.camera_size)
    row("Camera angle",  CAMERA_ANGLES, args.camera_angle)
    row("Camera move",   CAMERA_MOVES,  args.camera_move)
    row("Structure",     STRUCTURES,    args.structure)
    row("Aspect ratio",  ASPECTS,       args.aspect)

    lines.append(f"Scenes: {args.scenes}")

    if args.assets:
        lines.append(f"Assets: {args.assets}")

    lines.append("")
    lines.append("---")
    lines.append("Generate a complete Seedance 2.0 timeline prompt from this brief.")
    lines.append("Follow Seedance 2.0 grammar: one camera move per scene, no evaluative adjectives,")
    lines.append("Scene context block first, then numbered scenes with timestamps,")
    lines.append("last scene ends with: Avoid jitter, avoid temporal flicker.")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a Seedance 2.0 prompt brief for Claude Code.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("subject", help="What the video is about (concept, scene, or description)")

    # Optional parameters — all default to None (Claude decides)
    parser.add_argument("--style",        choices=list(STYLES),        default=None, metavar="STYLE")
    parser.add_argument("--light",        choices=list(LIGHTS),        default=None, metavar="LIGHT")
    parser.add_argument("--color",        choices=list(COLORS),        default=None, metavar="COLOR")
    parser.add_argument("--texture",      choices=list(TEXTURES),      default=None, metavar="TEXTURE")
    parser.add_argument("--mood",         choices=list(MOODS),         default=None, metavar="MOOD")
    parser.add_argument("--camera-size",  choices=list(CAMERA_SIZES),  default=None, metavar="SIZE")
    parser.add_argument("--camera-angle", choices=list(CAMERA_ANGLES), default=None, metavar="ANGLE")
    parser.add_argument("--camera-move",  choices=list(CAMERA_MOVES),  default=None, metavar="MOVE")
    parser.add_argument("--structure",    choices=list(STRUCTURES),    default=None, metavar="STRUCTURE")
    parser.add_argument("--aspect",       choices=list(ASPECTS),       default="16:9")
    parser.add_argument("--scenes",       type=int, default=5, choices=range(1, 7), metavar="N (1-6)")
    parser.add_argument("--assets",       default=None, help="Asset references, e.g. '@Image1 as first frame'")
    parser.add_argument("--out",          default=None, help="Output file path (default: /tmp/seedance_<hash>.txt)")

    args = parser.parse_args()

    brief = build_brief(args)

    slug = hashlib.md5(args.subject.encode()).hexdigest()[:8]
    out_path = Path(args.out) if args.out else Path(f"/tmp/seedance_{slug}.txt")
    out_path.write_text(brief, encoding="utf-8")
    print(str(out_path))


if __name__ == "__main__":
    main()
