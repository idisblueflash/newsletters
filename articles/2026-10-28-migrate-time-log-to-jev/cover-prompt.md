# Cover prompt — Mending the dam

Scene: a beaver at dusk, half out of the water on the crest of its stick-and-mud dam, pressing a fresh peeled stick into the top. The dam already holds. The beaver is not building it from scratch, only patching the spot that leaked. It stands for a workflow you keep using and keep mending: 且用且完善.

Visual reference: `sumomo/youtube/beaver-documentaries/cover-trial/picks/3336-on-dam-with-stick.jpg` (dark blue water behind, wet dark-brown fur, a pale stick angled up out of the grassy dam crest in the foreground). Alternative: `picks/4218-swimming-with-branch.jpg` (the beaver hauling a leafy branch to the dam). Not 3424-climbing-dam: it was already the reference for 2026-10-03-calendar-time and 2026-10-09-the-safe-bet.

Fact check: beavers repair dams mostly at dusk and through the night, and patch leaks within hours of finding them. They carry sticks in their mouths and push mud and sticks into place with their small, dexterous forepaws. Sticks on a dam are often peeled pale, because beavers eat the bark first.

## Version A — eye level, close to the water (recommended)

```
An eye-level documentary-style photograph taken from just above the waterline of a North American beaver on the crest of its dam at dusk. The beaver is half out of the water, wet dark-brown fur slicked into spikes, small forepaws pressing a fresh pale peeled stick into a tangle of older grey sticks and dark mud along the top of the dam. Behind it, the dark blue-grey surface of the pond ripples softly, falling out of focus. Low warm dusk light from the side catches the wet fur and the pale wood, deep soft shadows elsewhere, gentle film grain, natural color grading. Shot on a 300mm telephoto lens at f/4, sharp focus on the beaver's head, paws and the new stick, shallow depth of field. A single beaver, realistic beaver anatomy with a flat scaly tail just visible in the water, simple uncluttered background, no people, no text, no watermark.
```

## Version B — medium-close, the stick as hero

```
A medium-close documentary-style photograph at eye level of a beaver's head and forepaws on top of a stick-and-mud dam. Gripped crosswise in its orange front teeth is a freshly peeled pale willow stick, which it is lowering into a gap among the weathered grey sticks of the dam crest. Water beads on the dense brown fur and whiskers. The pond behind is a dark, softly rippled blue-grey wash. Warm low evening light from the left, fine fur and wood-grain texture, subtle film grain. 400mm telephoto, f/5.6, shallow depth of field, focus on the eye and the stick. One beaver, anatomically correct, clean background, no text, no watermark.
```

## Version C — wider, the dam in its pond

```
A wide documentary-style landscape photograph at eye level of a long beaver dam of stacked sticks and mud running across the lower third of the frame, holding back a calm dark pond that reflects a pale dusk sky and a line of willows. Near the right third of the dam crest, one small beaver is half out of the water, pushing a fresh pale stick into the top of the dam. The dam forms a strong horizontal line, the beaver small in the frame. Soft warm dusk light, muted greens, browns and greys, natural color grading, light film grain. 135mm lens, f/8, dam and beaver in sharp focus, background gently softened. A single beaver, realistic proportions, uncluttered scene, no people, no text, no watermark.
```

## Rendered with _jenny (2026-10-28)

Version A, three steps on local ComfyUI. Output: `cover.png` (1440×720). Visual reference was `picks/3336-on-dam-with-stick.jpg` (not 3424-climbing-dam). All renders came from the first round; nothing was rerun.

Step 1: Z-Image Turbo txt2img, short prompt:

```
An eye-level documentary photograph from just above the waterline of a single North American beaver at dusk, half out of the water on the crest of its stick-and-mud dam in the centre of the frame. Its wet dark-brown fur is slicked into spikes, and its small forepaws press a fresh pale peeled stick into the grey sticks and mud of the dam top. Behind, a calm dark blue-grey pond fills both sides, softly out of focus. Low warm side light. Exactly one beaver, no text, no watermark.
```

Step 2: Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt).

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt:

```
A wide 2:1 eye-level ink drawing from just above the waterline of a single beaver at dusk, sitting in the centre of the frame on the crest of its stick-and-mud dam. Its wet spiky fur is massed in solid black ink, and its small forepaws press a fresh pale peeled stick into the dam top. The dam crest runs as a long horizontal band of stacked sticks and mud across the whole frame, a calm pond behind it on both sides and its reflection below. Heavy solid black brush shadows in the mud and under the sticks, bright white paper highlights on the pale stick and the water. Exactly one beaver, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `494208114580278`, step 2 `1091560843525602`, step 3 `698482217004515`.
