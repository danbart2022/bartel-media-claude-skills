# Seedance 2.0 — Parameter Reference

All valid values for `seedance_prompt.py` flags and the interview question guide.

---

## Interview question block (for Claude)

When running in interview mode, present these as a single structured block.
Users can answer with numbers or short keywords.

---

**1. Visual Style** `--style`
| Key | Description |
|-----|-------------|
| `cinematic` | 35mm film grain, Kodak color palette, anamorphic lens flares |
| `anime` | Studio Ghibli aesthetic, hand-drawn warmth, cel-shaded |
| `commercial` | Contemporary commercial style, bright and clean, polished |
| `ugc` | Social media UGC style, authentic and raw, handheld naturalistic |
| `atmospheric` | Ethereal and dreamlike, soft light bloom, dark moody |
| `retro` | VHS tape aesthetic, Super 8 film, warm grain, light leaks |
| `vfx` | Experimental VFX, particles, energy waves, abstract motion |
| `portrait` | Portrait photography style, dreamcore and fantasy |

---

**2. Lighting** `--light`
| Key | Description |
|-----|-------------|
| `golden-hour` | Warm golden hour sunlight, long soft shadows |
| `blue-hour` | Blue twilight, cool desaturated tones |
| `neon` | Neon reflections on wet pavement, cyberpunk glow |
| `window` | Soft natural window light, no harsh shadows |
| `studio` | Clean studio lighting, soft box, neutral background |
| `rim` | Dramatic rim light, subject edge highlights |
| `backlight` | Strong backlight creating silhouette effect |
| `noir` | Hard chiaroscuro lighting, deep dramatic shadows |
| `candle` | Warm candlelight flickering, intimate low key |
| `overcast` | Soft diffused overcast light, even exposure |
| `rembrandt` | Rembrandt lighting, texture light, visible god rays |

---

**3. Color Tone** `--color`
| Key | Description |
|-----|-------------|
| `warm` | Warm amber tones, golden highlights |
| `cool` | Cool blue color temperature, desaturated |
| `vibrant` | Vibrant high saturation, punchy colors |
| `muted` | Muted desaturated tones, film fade |
| `bw` | Black and white high contrast |
| `neon` | Dark base with neon accent pops |
| `pastel` | Pastel soft tones, light and airy |

---

**4. Texture & Quality** `--texture`
| Key | Description |
|-----|-------------|
| `film-grain` | Cinematic 35mm film grain |
| `soft-blur` | Soft long-shutter blur, glowing highlights |
| `sharp` | Ultra sharp, crisp detail, no grain |
| `bokeh` | Rich layers, bokeh background, shallow depth of field |
| `lo-fi` | VHS texture, scanlines, color bleeding |

---

**5. Mood / Atmosphere** `--mood`
| Key | Description |
|-----|-------------|
| `epic` | Epic and dramatic |
| `chill` | Relaxed and calming, healing atmosphere |
| `energetic` | Energetic and dynamic |
| `romantic` | Romantic and intimate |
| `mystic` | Mystical and surreal |
| `melancholic` | Melancholic and nostalgic |
| `luxury` | Luxurious and premium |
| `humorous` | Light-hearted and playful |

---

**6. Camera — Shot Size** `--camera-size`
| Key | Description |
|-----|-------------|
| `extreme-wide` | Extreme wide establishing shot |
| `wide` | Wide shot — full subject, lots of environment |
| `medium` | Medium shot — subject from waist up |
| `close-up` | Close-up — face, hands, or detail |
| `extreme-close` | Extreme close-up — eye, mouth, texture |
| `mix` | Varied shot sizes across scenes |

---

**7. Camera — Angle** `--camera-angle`
| Key | Description |
|-----|-------------|
| `eye-level` | Neutral eye level |
| `low` | Low angle looking up — makes subject powerful |
| `high` | High angle looking down |
| `pov` | POV first-person perspective |
| `dutch` | Dutch angle tilt — tension |
| `birds-eye` | Bird's eye top-down view |
| `mix` | Varied angles across scenes |

---

**8. Camera — Movement** `--camera-move`

> Seedance requires exactly one camera movement per scene.

| Key | Prompt phrase |
|-----|---------------|
| `static` | `static locked-off shot` |
| `dolly-in` | `slow dolly push-in` |
| `dolly-out` | `slow dolly pull-back` |
| `tracking` | `tracking shot following the subject` |
| `pan` | `gentle pan` |
| `tilt` | `slow tilt up` |
| `aerial` | `aerial drone shot pulling back` |
| `handheld` | `handheld slight camera shake` |
| `orbit` | `slow orbit around the subject` |
| `zoom` | `subtle zoom in` |
| `slow-mo` | `slow motion with reduced movement` |
| `mix` | Claude varies movements across scenes |

---

**9. Structure / Timeline** `--structure`
| Key | Description |
|-----|-------------|
| `single` | One scene (4–6 seconds), focused and still |
| `short-film` | 4–6 scenes, narrative build (~20 seconds) |
| `action` | 5–6 scenes, dynamic cuts |
| `story` | Setup → peak → resolution |
| `loop` | Looping atmospheric, no action, pure mood |

---

**10. Aspect Ratio** `--aspect`
| Key | Use case |
|-----|----------|
| `16:9` | YouTube, desktop, widescreen |
| `9:16` | TikTok, Reels, Shorts |
| `1:1` | Instagram feed |

---

**11. Number of scenes** `--scenes`
`1` · `2` · `3` · `4` · `5` · `6`

---

**12. Asset references** `--assets` *(optional)*
- Image as first/last frame: `@Image1 as first frame`
- Video for camera reference: `@Video1 for camera movement`
- Audio as background music: `@Audio1 for background music`
