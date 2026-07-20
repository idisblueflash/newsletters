---
name: blockframe
description: Geometry-first cover-image workflow — lock composition, camera, object counts, positions and orientations in a free Blender greybox FIRST, then apply the inkframe ink-storyboard style in a single Nano Banana pass LAST. Use this whenever making a newsletter cover whose scene has real spatial structure (a room, multiple placed objects, a specific camera angle, a window/desk/bed layout, "match this reference composition"), or whenever a cover has been costing many regenerations to fix geometry (an object in the wrong place, a wrong angle, wrong count, an open/closed state). Also trigger on "blockout", "blueprint", "3D blockout", "Blender cover", "camera angle for the cover", "the bed/window/tree is in the wrong place". For a purely style-driven single-subject image with no fussy geometry, plain inkframe is fine; reach for blockframe the moment placement/angle/count matters.
---

# blockframe — geometry-first cover images

A cover splits into two very different kinds of work:

- **Geometry** — where things are, how big, which way they face, how many, the camera angle. The image model sadly **samples** these (window pane-count, bed angle, an object's position), and each wrong guess costs a **1–2 min paid regeneration** to fight with drift-prone text edits. Both of the Blender-via-Claude tutorials in `ref/` independently report the same thing: the model's **perspective/3D vision is weak**, so asking it to "move X" or "use this angle" in prose is the slow path.
- **Style** — the ink woodcut look, contrast, brushwork. The model does this **reliably** from a short style block, and it's also the *cheapest* thing to fix afterward.

So the whole method is: **do all geometry off the paid model, in a free Blender greybox; spend exactly one paid call on style; finish deterministically.** This inverts `inkframe` (which leads with style). Use `inkframe`'s style DNA only at the render step — see `.claude/skills/inkframe/SKILL.md`.

## Why this ordering (facts established by testing, don't re-litigate)

- A single Nano Banana call is **fixed latency** — `--size preview` and `--size medium` are the *same* 1K request (0.5K unsupported), and it's already the fast `gemini-3.1-flash-image` model. You cannot make one call faster; you can only make **fewer** calls and run them **in parallel**.
- The Gemini API has **no mask/inpaint**. "Keep everything else identical" is *best-effort semantic* preservation — it is the source of drift, not a fix. Real area-edits must be done **off-model** (crop → edit → composite).
- A **saturated color-coded greybox leaks its palette** through image-to-image and overrides "No color". Fix with the **off-model desaturate** finish (below) — it doubles as the "almost zero gray midtones" enforcer.
- The model's **3D vision is weak** → place geometry by **scripted coordinates**, and let the **human pick the camera**. When driving Blender live over MCP, prefer cheap **viewport screenshots** over full renders, and enable the MCP add-on's **auto-start** so the socket doesn't drop.

## The pipeline

Run render/generate steps from the `newsletters` repo root. Blender runs headless; no GUI needed except when the human is adjusting the camera.

### 0. (Recommended) Blueprint → dimensions
If you're matching a reference image or a concrete scene, first turn it into a **plan + elevation blueprint** to get metric dimensions and object layout — a top-down plan sidesteps the model's weak perspective vision. Prompt template: `references/blueprint-prompt.md`.

```bash
.claude/skills/inkframe/scripts/generate-cover.py "$(cat blueprint_prompt.txt)" \
  --input path/to/reference.jpg --size medium --output output/blueprint
```
Read the plan for room size, wall height, ceiling-slope angle, sill height, and object placement. **The printed numbers are approximate/decorative** — trust the proportions and layout, not the exact digits.

### 1. Blockout (all geometry work happens here — free, ~1 s each)
Copy `scripts/blockout_template.py` and edit it for the scene: a parametric **metric** room shell plus **color-coded primitive masses** (one flat color per object, BoxCtrl-style, so the render doubles as a labeled guide). Render the flat greybox headless:

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background --python scripts/blockout_template.py
```
Iterate here as much as you like — position, size, count, orientation, the sloped ceiling, the camera. It's instant and free, so **never** spend a paid generation to discover geometry. Read the `-` PNG back to check composition (`output/blockout/…png`).

### 2. Camera (hand it to the human — their eyes beat the model's)
The template saves an editable `.blend` with **Lock-Camera-to-View** enabled. Open it for the user:
```bash
open -a Blender output/blockout/<scene>-blockout.blend
```
They orbit/pan/zoom (camera follows), then **⌘S**. Re-render from their camera with `scripts/rerender.py`:
```bash
/Applications/Blender.app/Contents/MacOS/Blender -b output/blockout/<scene>-blockout.blend \
  --python scripts/rerender.py    # prints the new CAM_LOC / CAM_ROT_DEG so it round-trips
```
(If Lock-Camera-to-View isn't taking effect, the human can also just select `Cam` and G/R it, or run `scripts/enable_lock.py` on the `.blend`.)

### 3. Style pass (the ONE paid call)
Feed the greybox as an image-to-image structure guide with a **style + color→object mapping** prompt — geometry is delegated to the image, so the prompt carries *only* style and what each color means. Template: `references/style-mapping-prompt.md`.

```bash
.claude/skills/inkframe/scripts/generate-cover.py "$(cat style_prompt.txt)" \
  --input output/blockout/<scene>-blockout.png --size medium
```
For a hard-to-hit look, fire **2–4 candidates in parallel** (background the calls) and pick — same cost, one wait instead of several. Transient `ChunkedEncodingError`/`IncompleteRead` are API flakes: just retry.

### 4. Finish (off-model, free, instant)
The saturated greybox usually leaks color into the render. Convert to B&W ink and enforce the woodcut contrast deterministically — this also erases any single stray leaked-color smudge:
```bash
python3 -c "from PIL import Image,ImageEnhance,ImageOps; \
im=ImageOps.autocontrast(Image.open('IN.png').convert('L'),cutoff=1); \
ImageEnhance.Contrast(im).enhance(1.4).convert('RGB').save('OUT-bw.png')"
```
Then save the accepted image into the article's `cover/` per the inkframe save rule.

## Edit routing — match the fix to the cheapest tool

| The change is… | Do this | Not this |
|---|---|---|
| structural: move / rotate / recount / re-angle / re-frame | edit the **blockout** + regenerate | ❌ text-editing the ink render |
| a self-contained local element (add a band, swap a prop) | **crop → edit that crop → composite back** (rest stays byte-identical) | ❌ full-frame "keep everything else identical" |
| tone / contrast / desaturate / grain / crop | **deterministic PIL/ImageMagick** pass | ❌ a paid regeneration |
| the ink look itself (brushwork, hatching) | one Nano Banana pass, or parallel candidates | ❌ a long serial edit chain |

The tell you're doing it wrong: your edit prompts grow longer each round to fence off the *last* mistake ("there is exactly ONE window, do not add a second…"). That's specification work that belonged in the blockout.

## Common pitfalls

- ❌ Discovering geometry with paid generations — that's what the free greybox is for.
- ❌ Serial text edits of position/angle — the model can't do "left" or "45°" reliably; move it in Blender.
- ❌ Trusting the blueprint's exact numbers — proportions yes, digits no.
- ❌ Leaving the greybox colors in the final — always run the desaturate finish (or use a muted greybox).
- ❌ Bundling edits that fight over the same region; but **do** batch edits that touch disjoint regions.

## Files
- `scripts/blockout_template.py` — parametric metric room + color-coded masses + camera + flat 21:9 render + `.blend` save. The per-scene starting point.
- `scripts/rerender.py` — re-render a `.blend` after the human moves the camera; prints the camera transform.
- `scripts/enable_lock.py` — force Lock-Camera-to-View on a `.blend`.
- `references/blueprint-prompt.md` — image → plan+elevation blueprint prompt.
- `references/style-mapping-prompt.md` — color→object ink-style render prompt.
- Style DNA + `generate-cover.py` are reused from `.claude/skills/inkframe/`.
