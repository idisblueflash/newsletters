# Cover prompt — The last stretch before the station

Scene: a small one-car local train coming round a bend through thick mountain greenery in rural Kochi (Shikoku), almost at the station. In the foreground, out-of-focus ferns and leaves fill most of the frame; the train shows only on the right third, half hidden behind fern fronds, the way the panda peeks in at the edge of the reference. It is the moment the draft ends on: 「火车进站前那段熟悉的风景」, the scenery you only notice when you are nearly home.

Visual reference: `/Users/husongtao/Projects/smooth motion coding/The Spectacular Wildlife of China ｜ 4KUHD ｜ BBC Earth [e72XTfO0t8o].mp4-00_00_22-2026-11-10-12h13m30s384.jpg` (BBC Earth frame: dense green ferns blurred in the foreground and left edge, a giant panda half hidden on the right third, shallow depth of field, soft diffuse forest light). Borrow the composition only: foliage-dominated frame, subject small and partly hidden on the right, eye level, telephoto compression. No panda, no logo.

Fact check: JR Shikoku runs one-car diesel railcars (e.g. KiHa 1000 / 1500 series) on the Dosan Line between Awa-Ikeda and Kochi, through the Yoshino river gorge and steep, densely forested mountains. Small rural stations there are a single concrete platform with a simple shelter. Mid-summer foliage is deep green with ferns along the cuttings.

Mood (my call from the draft's ending: 「最让人安心的」): calm, quiet relief, not drama. So eye level, soft overcast light, the train small and unhurried.

## Version A — train peeking through ferns, right third (recommended)

```
An eye-level telephoto documentary photograph taken from inside dense mountain undergrowth in rural Kochi, Japan. Large green fern fronds and broad leaves fill the foreground and the left two thirds of the frame, soft and out of focus. On the right third, partly hidden behind fern fronds, a single-car Japanese local diesel train with a white and light-blue body rolls slowly along a single track, its front window and headlight visible, about to arrive at a small rural station. Behind it, steep forested hillside in deep summer green. Soft diffuse overcast daylight, gentle green tones, humid air. Natural color grading, fine film grain. Long lens, f/2.8, shallow depth of field, focus on the train's front, foreground foliage blurred. Exactly one train, no people in view, no text, no watermark, no logo.
```

## Version B — the platform edge

```
An eye-level telephoto documentary photograph looking through dense green ferns at the end of a small single-platform rural station in the mountains of Shikoku, Japan. Out-of-focus fern fronds fill the left and bottom of the frame. On the right third, half hidden by leaves, a single-car local diesel train with a white body and blue stripe pulls in beside a plain concrete platform with a small shelter. Steep forested slope behind, soft overcast light. Natural color grading, fine film grain. Long lens, f/2.8, focus on the train, foreground blurred. Exactly one train, no readable signs, no text, no watermark.
```

## Version C — wider gorge

```
An eye-level photograph from a fern-covered bank above a river gorge in Kochi, Japan. Blurred ferns frame the left edge and bottom of the picture. Across the gorge on the right third, a single-car local diesel train, small in the frame and partly hidden by trees, runs along a track cut into the steep green mountainside. Lush summer forest, soft mist, diffuse light. Natural color grading, fine film grain. Telephoto lens, f/4, focus on the train. Exactly one train, no people, no text, no watermark.
```

## Rendered with _jenny (2026-11-10)

Version A, three steps on local ComfyUI. Output: `cover.png` (1440×720, not yet converted). Composition reference was the BBC Earth frame `The Spectacular Wildlife of China ｜ 4KUHD ｜ BBC Earth [e72XTfO0t8o].mp4-00_00_22-2026-11-10-12h13m30s384.jpg` (ferns blurred in the foreground and on the left, subject half hidden on the right third). Step 1 took two rounds: every round 1 image showed a multi-car train, so round 2 rewrote the train clause (one short solo railcar, a cab at each end, exactly one carriage). Steps 2 and 3 came from their first round.

Step 1: Z-Image Turbo txt2img, short prompt (round 2):

```
An eye-level telephoto photograph from inside dense fern undergrowth in rural Kochi, Japan. Large blurred green fern fronds fill the foreground and the left side. Just right of centre, small in the frame and half hidden behind fern fronds, one short solo railcar: a single white and light-blue carriage with a driver's cab at each end, both ends visible, seen in three-quarter view with its front angled to the left, on a single track below a steep green forested hillside. Soft overcast light, shallow depth of field. Exactly one carriage, no other cars coupled, no people, no text, no watermark.
```

Step 2: Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt), `--place right --subject-x 0.65` (train on the right third, ferns continued across the left).

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt:

```
A wide 2:1 eye-level ink drawing looking out from inside dense fern undergrowth in the mountains of rural Kochi, Japan. Large fern fronds fill the foreground and the whole left side, drawn loose and bold. On the right third, small in the frame and partly hidden behind fern fronds, one short single-car local diesel train in three-quarter view rolls along a single track below a steep forested hillside. The train body left as bright white paper with a mid-gray stripe, the forest behind in flat grays, heavy solid black brush shadows under the ferns and the train. Exactly one single-car train, no people, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `573155459301288`, step 2 `1006609988345275`, step 3 `586389287095245` (re-run with an explicit single-track clause after seed `1094489675853023` drew a doubled track; old render kept as `cover-old.png`).

Colour version: `cover-color.png`, CMYK old-comic colorize of `cover.png` (Flux 2 Klein, default fade `--saturation 0.55 --paper 0.18`), palette `deep green ferns and forest, white train body with a light blue stripe, warm gray gravel and rails, pale overcast sky`, seed `741630171073725`.
