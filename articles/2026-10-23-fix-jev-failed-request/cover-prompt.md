# Cover prompt — Five on the line

Scene: five barn swallows on the top rail of a weathered wooden five-bar farm gate. Four are already perched, evenly spaced. The fifth hovers just above the one empty gap, about to land. It stands for the five requests sent at once, with the failed one coming back on a retry.

Visual reference: `sumomo/bilibili/swallow-migration-BV1UW31z9Etm/cover-trial/picks/1239-on-farm-gate.jpg` (green pasture, dry-stone wall, weathered gate, soft overcast light).

Fact check: swallows perched on fences space themselves at fairly regular intervals. They claim a spot by flying straight in and hovering briefly before they land. A perched swallow keeps its forked tail closed, so only the incoming bird should show spread wings and a forked tail.

## Version A — eye level, calm (recommended)

```
An eye-level documentary-style photograph of five barn swallows on the top rail of a weathered grey wooden five-bar farm gate. Four swallows sit perched in a neat row, evenly spaced a hand's width apart, glossy steel-blue backs, rusty-red throats, cream bellies, forked tails folded. The fifth swallow hovers just above the single empty gap at the right end of the row, wings spread wide, forked tail open, feet reaching down to land. Behind the gate, a mossy dry-stone wall and a soft green hillside pasture fall out of focus. Soft overcast daylight, even and shadowless, gentle film grain, natural color grading. Shot on a 300mm telephoto lens at f/4, sharp focus on the rail and the hovering bird, creamy background blur. Exactly five birds, anatomically correct swallows, simple uncluttered background, no text, no watermark.
```

## Version B — medium-close, the landing bird as hero

```
A medium-close documentary-style photograph at eye level of the top rail of an old weathered wooden farm gate, its grain cracked and silver-grey. Four barn swallows perch along the rail, steel-blue backs, rust-red faces, pale bellies, tails folded, all facing the same way. On the right, a fifth barn swallow hangs in the air a few centimetres above the empty spot, wings raised in a frozen wingbeat, long forked tail streamers spread, legs lowered toward the wood. The green pasture and a low stone wall behind are a soft wash of green. Diffused overcast light from above, fine feather texture visible, subtle film grain. 400mm telephoto, f/5.6, fast shutter freezing the wings, shallow depth of field. Exactly five birds, realistic swallow anatomy, clean background, no text, no watermark.
```

## Version C — wider, the gate in its landscape

```
A wide documentary-style landscape photograph at eye level of a weathered wooden five-bar farm gate set in a mossy dry-stone wall, a rolling green pasture and a large oak tree behind it. Along the top rail of the gate sit four small barn swallows in an evenly spaced row, and a fifth swallow swoops in from the right, wings spread, about to land in the last open space. The birds are small in the frame, occupying the left-center third, the gate and wall forming a strong horizontal line across the lower half. Soft overcast summer light, muted greens and greys, natural color grading, light film grain. 135mm lens, f/8, gate and birds in sharp focus, background gently softened. Exactly five birds, realistic proportions, uncluttered scene, no people, no text, no watermark.
```

## Rendered with _jenny (2026-10-23)

Version A, three steps on local ComfyUI. Output: `cover.png` (1440×720).

Step 1 — Z-Image Turbo txt2img, short prompt (round 2; round 1 said "five swallows" and gave five perched birds plus the flyer):

```
An eye-level documentary photograph of the top rail of a weathered grey wooden farm gate. Only four barn swallows sit on the rail, evenly spaced in the middle, steel-blue backs, rusty-red throats, tails folded, with one empty space at the right end of the row. A single fifth swallow hovers just above that empty space, wings spread, about to land. Behind, a mossy stone wall and soft green pasture fall out of focus at both sides. Soft overcast daylight. Four perched birds and one flying bird, five birds in total, no text, no watermark.
```

Step 2 — Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt).

Step 3 — Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg` (round 2), full style prompt:

```
A wide 2:1 eye-level ink drawing of the top rail of a weathered wooden farm gate standing in the middle of the frame, a stone gatepost at its left end. Exactly four barn swallows sit on the rail, evenly spaced, left of centre, tails folded, and the right half of the rail is bare. A single fifth swallow hovers just above the first bare spot, wings spread, about to land. Heavy solid black brush shadows under the rail, in the gatepost and in the grass, bright white paper sky. Four perched birds and one flying bird, five birds in total, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `74218089940280`, step 2 `63054401471450`, step 3 `511361655575377`.
