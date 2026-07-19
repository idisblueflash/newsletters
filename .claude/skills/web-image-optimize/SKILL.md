# Web Image Optimize

Convert a PNG (or other raster) cover image into a smaller web-friendly JPEG —
same pixel dimensions by default, just re-encoded with JPEG compression.
Use this whenever the user asks to "format/convert an image for web", make a
"web version" of a cover, or shrink a PNG's file size without resizing it.

## When to trigger

- "let's make a web version of this image"
- "convert this cover to jpeg for web"
- "reduce the size of this PNG"
- "/web-image-optimize"

## How to invoke

```bash
python3 .claude/skills/web-image-optimize/scripts/optimize.py <image1> [image2 ...]
```

Defaults: JPEG quality 85, same pixel dimensions as the source, output saved
next to the source file with a `-web` suffix (e.g. `cover.png` ->
`cover-web.jpg`).

### Options

| flag | default | purpose |
|------|---------|---------|
| `--quality N` | 85 | JPEG quality (1-95) |
| `--max-width N` | none (keep original width) | downscale if wider than N px |
| `--suffix STR` | `-web` | filename suffix inserted before `.jpg` |
| `--out DIR` | same dir as source | where to write output files |

### Examples

```bash
# Single file, default settings
python3 .claude/skills/web-image-optimize/scripts/optimize.py articles/foo/cover/cover.png

# Multiple files at once
python3 .claude/skills/web-image-optimize/scripts/optimize.py \
  articles/foo/cover/cover.png articles/foo/cover/cover-color.png

# Also downscale for a thumbnail
python3 .claude/skills/web-image-optimize/scripts/optimize.py \
  articles/foo/cover/cover.png --max-width 600 --suffix -thumb
```

## Defaults rule

**Do not resize unless asked.** The whole point of this skill (as clarified
by the user) is that most of the file-size win on illustrated cover art comes
from PNG -> JPEG re-encoding, not from downscaling. Only pass `--max-width`
if the user explicitly wants a smaller thumbnail, not just a smaller file.

## Prerequisites

`Pillow` on the Python path (`pip install Pillow`).
