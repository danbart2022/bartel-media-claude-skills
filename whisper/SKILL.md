---
name: whisper
description: >
  Transkribiert Audiodateien lokal mit OpenAI Whisper — keine API, keine Tokens.
  Nutze diesen Skill immer wenn der Nutzer sagt "transkribiere", "transkribier mal",
  "schreib das ab", "was steht in der Audiodatei" oder einen Dateipfad zu einer
  Audiodatei nennt (.m4a, .mp3, .wav, .mp4, .ogg, .flac, .webm, .aac).
  LOKALE Verarbeitung hat immer Vorrang vor API-basierter Transkription.
---

# Whisper — Lokale Audio-Transkription

Transkribiert Audiodateien vollständig lokal mit OpenAI Whisper CLI.
Kein API-Key, keine Cloud, keine Token-Kosten.

## Standardverfahren (immer so vorgehen)

### Schritt 1 — Dateipfad auflösen

- Absoluter Pfad angegeben → direkt nutzen
- Nur Dateiname angegeben → suchen in:
  1. `~/Downloads/`
  2. `~/Desktop/`
  3. Aktuelles Projektverzeichnis

```bash
find ~/Downloads ~/Desktop -name "dateiname.m4a" 2>/dev/null | head -1
```

### Schritt 2 — Sprache

- Standard: **Deutsch** (`--language German`)
- Englisch explizit gewünscht → `--language English`
- Unbekannt → kein `--language` Flag (Whisper erkennt automatisch)

### Schritt 3 — Modell wählen

| Modell | Einsatz | Größe |
|--------|---------|-------|
| `base` | Kurze Notizen < 2 Min, sehr schnell | 140 MB |
| `small` | **Standard** — gut & schnell | 460 MB |
| `medium` | Schlechte Qualität, Fachbegriffe, > 10 Min | 1,5 GB |
| `large` | Maximale Qualität, selten nötig | 3 GB |

**Default: `small`**

### Schritt 4 — Whisper ausführen

```bash
whisper "/absoluter/pfad/zur/datei.m4a" \
  --language German \
  --model small \
  --output_format txt \
  --output_dir /tmp/whisper_out
```

**Hinweis beim ersten Start:** Modell wird einmalig heruntergeladen (~460 MB für `small`).
Den Nutzer informieren: *"Lade Whisper-Modell 'small' herunter, einmalig ~460 MB..."*
Cache liegt in `~/.cache/whisper/` und wird wiederverwendet.

### Schritt 5 — Ergebnis ausgeben

```bash
cat /tmp/whisper_out/[dateiname].txt
```

- Transkript **direkt in den Chat** ausgeben (kein Link)
- Bei > 500 Wörtern: Volltext ausgeben + kurze Zusammenfassung anbieten
- Danach aufräumen: `rm -rf /tmp/whisper_out`

---

## Qualitätsproblem?

Falls das Ergebnis unleserlich oder lückenhaft → automatisch mit `medium` wiederholen:

```bash
whisper "/pfad/datei.m4a" --language German --model medium --output_format txt --output_dir /tmp/whisper_out
```

---

## Whisper nicht gefunden?

```bash
pip3 install openai-whisper
```

---

## Unterstützte Formate

`.m4a` `.mp3` `.wav` `.mp4` `.ogg` `.flac` `.webm` `.aac` `.opus`
