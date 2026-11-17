# Cover prompt — 一根竹子，自己挑的

Scene: a giant panda sitting upright in a bamboo forest, both forepaws wrapped around one stalk it has picked, biting open the peeled end, the rest of the grove lost in soft green behind it. Chosen from the reference sheet below as scene **a** (sitting in bamboo, holding one stalk) — the only one of the four where 「只挑自己喜欢的」 comes from the action itself rather than from the caption, and the only one that leaves clean green space on one side for the 2:1 crop.

Visual reference: `/Users/husongtao/Projects/sumomo/youtube/the-spectacular-wildlife-of-china-4kuhd-bbc-earth/cover-the-spectacular-wildlife-of-china-4kuhd-/picks/0202-panda-holding-bamboo.jpg` (BBC Earth frame: clear frontal panda with a split bamboo stalk across its mouth, lush green habitat behind, shallow depth of field, soft diffuse forest light), plus `picks/0214-panda-eating-bamboo-leaves.jpg` for the seated full-body posture and the leaf bundle in the paws. Borrow the animal, the light and the green; the 2:1 composition and the right-third placement are ours.

Fact check (Gould, *The Panda's Thumb*; Wang et al., *Scientific Reports* 2022; Chengdu Panda Foundation): giant pandas feed sitting upright, hooking a culm in with the curved forepaw, then holding it against the five digits and the enlarged radial sesamoid — the false thumb — to strip and chew it. They manipulate the stalk with the forepaws, shedding leaves and eating the shoots; they cannot wrap the false thumb around the stalk the way a human palm would. So both forepaws close on one stalk, the grip stays open-ended, and one end of the culm is bitten and peeled, not snapped in half.

Mood: quiet absorption, no drama. Eye level, soft overcast light filtered through the canopy, the animal fully occupied with the one thing in its paws.

## Version A — sitting in bamboo, holding one stalk, right third (recommended)

```
An eye-level telephoto documentary photograph of an adult giant panda sitting upright on the mossy floor of a dense bamboo forest, its whole body placed in the right third of the frame. Both forepaws are wrapped around one pale-green bamboo culm held diagonally across its chest, the near end bitten open, a thin strip of the green outer skin curling away from the white inner wood, a few narrow leaves still attached further up the stalk. The black eye patches and cream-white fur carry fine wet detail, individual guard hairs catching light on the shoulders. Tall culms and leaf litter behind it fall into soft deep-green blur, leaving the left side of the frame an even, uncluttered green. Overcast diffused forest light from high above and slightly behind, bloomed through the canopy. Quiet and absorbed. Natural colour grading, fine film grain. 400mm telephoto, f/4, focus locked on the eyes, shallow depth of field. Exactly one panda, both eyes visible, simple uncluttered left side, no text, no watermark, no logo, no other animals.
```

## Version B — the face behind the leaves it is eating

```
An eye-level close-up documentary photograph of an adult giant panda's head and shoulders, the muzzle half behind a bunch of narrow bamboo leaves it is feeding on. The leaves cross the lower third of the frame in front of its chin, few enough that both black eye patches and the nose stay fully visible; the stalk they hang from is held up out of frame by one dark forepaw. Cream-white fur and coarse black fur in fine wet detail, faint green light caught in the white. Behind it, deep green bamboo forest melted into an even blur. Soft diffuse overcast daylight from above. Absorbed, unhurried. Natural colour grading, fine film grain. 200mm lens, f/2.8, focus on the eyes, foreground leaves softly blurred. Exactly one panda, face unobstructed at the eyes, no text, no watermark, no logo.
```

## Version C — the grove is huge, it picked one stalk

```
A high-angle wide documentary photograph looking down into a dense bamboo grove in the mountains of Sichuan, China. Tall green culms and a floor of dry leaf litter fill the frame. In the lower right, small in the picture, one adult giant panda sits upright on the litter with a single bamboo stalk held between its forepaws, chewing the peeled end, its white back bright against the dark green. Deep shade below the canopy, broken by narrow shafts of overcast daylight coming through the leaves. Still and calm. Natural colour grading, fine film grain. 35mm lens, f/5.6, focus on the panda, the grove in crisp detail around it. Exactly one panda, no people, no text, no watermark, no logo.
```

## Render notes for _jenny

- Target 1440×720 (2:1). Subject on the **right** third for A and C; Version B has no usable negative space, so it would need centring or a soft left extension.
- Step 3 style-transfer target is `.claude/agents/_jenny.assets/cover-style.jpg` (gray ink house style), same as #16/#17 covers.
- Keep exactly one panda through every round: Z-Image tends to add a second bear in the background of grove scenes.

## Rendered with _jenny (2026-11-16)

Version A, three steps on local ComfyUI. Output: `cover.png` (1440×720, not yet converted). Step 1 took three rounds: round 1 (4) filled the left edge with culms; round 2 (3) reduced them but kept stalks at the edge; round 3 (3) added a clause making the left half an empty green wash, which cleaned the negative space. Step 2 came from its first round (3). Step 3 took two rounds: round 1 (4) kept a faint green tint on the culm (p99 chroma 12, against 6 on earlier house covers), round 2 (3) named the culm as pale gray ink and came out achromatic (p99 chroma 4). Every variation in all rounds held exactly one panda with both eyes clear.

Step 1: Z-Image Turbo txt2img, short prompt (round 3):

```
An adult giant panda sits upright on mossy ground, turned about 45° in three-quarter view, face clear with both eyes visible, both forepaws wrapped around one pale-green bamboo culm held across its chest, the near end bitten open with a strip of green skin curling back. Behind it the dense grove melts into an even soft green haze, the left half of the frame a smooth empty green wash with no stalks. Overcast forest light. Exactly one panda, no other animals, no text, no watermark.
```

Step 2: Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt), `--place right --subject-x 0.58` (panda on the right third, misty grove continued across the left two-thirds).

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt (round 2):

```
A wide 2:1 ink drawing of an adult giant panda sitting upright on a mossy forest floor, turned about 45° in three-quarter view, face clear with both eyes visible, both forepaws wrapped around one bamboo culm held diagonally across its chest, the near end bitten open with a strip of skin curling back. The panda sits on the right third of the frame in bold solid black and white paper tones, its white fur left as bright paper; the whole left two-thirds melts into flat mid-gray forest haze with a few pale trunks. The culm drawn in pale gray ink, the entire picture strictly monochrome black, gray and white with no green tint anywhere. Exactly one panda, no other animals, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `1044128279068361`, step 2 `868978264480894`, step 3 `293797792957161`.

**Superseded** by the round below (2026-11-16): the panda filled about 55% of the frame height and the culm was a short, fat, node-less tube. That render is kept at `/tmp/jenny-panda-18/round1-cover.png`; `cover.prev.png` now holds the round-2 render.

## Rendered with _jenny (2026-11-16, round 2)

Version A again, two changes: panda at three-fifths of its old scale (body about a third of the frame height, a small animal in a big grove) and the culm thinner and longer (about a sixth of the head width, node rings, a small spray of leaves near the upper end, bitten and peeled at the near end). Everything else held: one panda, right third, both eyes clear, house ink style, 1440×720. Output: `cover.png`. Step 1 took eight rounds of 4. Near-profile faces hid the far eye (round 4); frontal faces grew the panda back to ~45% (rounds 5–6); a "wall of culms in the upper two thirds" clause produced a zoo wall (round 7); round 8 balanced a small figure against a clean left edge and a thin noded stalk. Step 2 came from its first round (3): the outpaint re-densified the grove across the left, so the left is a soft gray grove haze rather than the empty wash of round 1. Step 3 came from its first round (4), achromatic on the first try (p99 chroma 2–3, max 5). Every variation in every round held exactly one panda.

Step 1: Z-Image Turbo txt2img, short prompt (round 8):

```
A wide landscape of a dense bamboo grove: one small giant panda sits at the base of the tall culms on the mossy floor, a small figure about one third of the picture height, the grove rising high above it with no wall or fence behind, pure bamboo forest. Its head is turned only slightly to one side so both black eye patches and both eyes face the camera clearly. Both forepaws grip one long slender culm, thinner than a sixth of its head, that leans down from its paws toward the lower left, its tip leaving the frame at the bottom left corner, two node rings along it and a small spray of narrow leaves near the tip; the bitten peeled end at its mouth, green skin curling back. The left side of the frame is empty soft green haze. Exactly one panda, no other animals, no text, no watermark.
```

Step 2: Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt), `--place right --subject-x 0.70`.

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt:

```
A wide 2:1 ink drawing of a tall bamboo grove: one small giant panda sits at the base of the culms on the right third of the frame, a small figure about a third of the frame tall, dwarfed by the tall stalks. Its head is turned only slightly, both black eye patches and both eyes clear. Both forepaws grip one long slender culm, pencil-thin, running diagonally across the frame with two node rings and a small spray of narrow leaves near its upper end; the bitten peeled end at its mouth. The panda stays small and the culm stays thin, never enlarged. The left two-thirds of the frame melts into flat mid-gray haze, plain and uncluttered behind a few pale trunks. The whole picture strictly monochrome black, gray and white with no green tint anywhere. Exactly one panda, no other animals, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `984780467022513`, step 2 `482679251540117`, step 3 `589226531849668`. Working files: `/tmp/jenny-panda-18/` (`round2-step1r8/`, `round2-step2/`, `round2-step3/`).

Known compromise: the model would not draw the stalk running down and out of the lower left; in every round it rises up-left from the paws, so the picked stalk carries its node rings and leaf spray at the upper end instead, with the cut end near the mouth. The stalk did end up thin (well under a sixth of the head width) and the panda reads at about a third of the frame height.

**Superseded** by round 3 (2026-11-17): two planes and almost no tonal movement. That render is kept at `/tmp/jenny-panda-18/round2-step3/step3-02-seed589226531849668.png`; `cover.prev.png` now holds the round-4 render's predecessor (round 3).

## Rendered with _jenny (2026-11-17, round 3)

Version A again, composition change only: the frame now carries four depth planes and a full tonal ladder, matching the range of `articles/2026-11-10-scenery-and-dialect/cover.jpeg`. Near foreground: big bamboo leaves and thin branch tips in solid black cropping the bottom left corner and bottom edge. Mid-ground: thick pale culms at the right rim, thinner darker culms receding between them, leaf sprays at different heights and angles, one leaning stalk, ferns and grass tufts, a fallen culm across the litter. Left side: receding culms staggered back through dark, mid and pale gray into mist, with one soft light patch near the top left, the whole left still lighter than the right. Tonal ladder held from solid black foreground to dark near culms, mid gray, light gray distance, and paper white on the held culm and the lit side of the head. Output: `cover.png` (1440×720). Step 1 took two rounds of 4: round 1 had the four planes and the correct ~30% panda but regressed to short stubby stalks; round 2 kept the planes and restored the long thin noded culm with its leaf spray. Step 2 came from its first round (3). Step 3 came from its first round (4) and was achromatic on the first try (p99 chroma 3, max 5). Exactly one panda in every variation of every round; no second animal, no wall.

Step 1: Z-Image Turbo txt2img, short prompt (round 2):

```
Four layers of depth in one bamboo grove. Large near-black bamboo leaves and drooping branch tips crop into the bottom left corner and along the bottom edge as the nearest, darkest shape. Behind them two thick pale culms stand close to the right rim, thinner darker culms recede between them, leaf sprays hang at different heights, one stalk leans, ferns and grass tufts cover the floor with one fallen culm lying across the litter. Further back the culms turn pale and fade into mist, brightest near the top left corner. One small giant panda sits at the right, about a third of the picture height, both black eye patches and both eyes clear. Both forepaws grip one long thin culm, thinner than a sixth of its head, with two node rings, the bitten peeled end at its mouth and a small spray of narrow leaves still on it. Exactly one panda, no other animals, no text, no watermark.
```

Step 2: Flux 2 Klein 4B + pixaoutpaint, outpaint to 1440×720 (default outpaint prompt), `--place right --subject-x 0.79`.

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt:

```
A wide 2:1 ink drawing of a bamboo grove in four depth planes. In the bottom left corner and along the bottom edge, big bamboo leaves and thin drooping branch tips crop in as the nearest shape, drawn solid black. Behind them a dark cluster of near culms, then a mid-gray band of thinner culms receding, then a pale misty distance with one soft light patch near the top left; the left side stays lighter than the right. On the right rim two thick pale culms; between them thinner darker culms, leaf sprays at different heights and angles, one stalk leaning, ferns and grass tufts on the forest floor, one fallen culm lying across the litter. One small giant panda sits on the right third, about a third of the frame tall, both black eye patches and both eyes clear, both forepaws gripping one long thin culm with two node rings and a small leaf spray, the bitten peeled end at its mouth. Full tonal ladder: solid black foreground foliage, dark gray near culms, mid gray grove, light gray distance, paper white on the held culm and the lit side of the panda's head. Exactly one panda, no other animals, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seeds: step 1 `302199133157289`, step 2 `845956849424515`, step 3 `593419926104591`. Working files: `/tmp/jenny-panda-18/round3-step1/`, `round3-step1r2/`, `round3-step2/`, `round3-step3/`.

**Superseded** by round 4 (2026-11-17): foreground leaves had no stems. That render is kept as `cover.prev.png` (and at `/tmp/jenny-panda-18/round3-cover.png`).

## Rendered with _jenny (2026-11-17, round 4)

Foreground fix only: every black leaf cluster now grows off a visible tapering black stem that runs back through the dark mass or out of the frame, two or three branches carrying the clusters, and a branch crossing the pale gray stays continuous and legible. Position and coverage of the near-black bottom-left mass were held to the round-3 frame (dark-pixel share of the bottom-left block 43.4% vs 41.6%; of the bottom edge 56.2% vs 57.2%). Steps 1 and 2 are unchanged: the same step-2 pick (`845956849424515`) fed two fresh style rounds. Step 3 round 1 attached the clusters to stems but drew them as hairlines; round 2 restated them as heavy tapering black strokes the weight of the blades, which produced the delivered frame. The pick is achromatic (p99 chroma 3, max 5) and keeps the four planes, the tonal ladder, the mist and its light patch, the leaning stalks, the fallen culm, the rim culms, and the single panda at about 28% of frame height on the right third with both eyes clear. Output: `cover.png` (1440×720).

Step 1 seed unchanged (`302199133157289`) and step 2 seed unchanged (`845956849424515`); only the style prompt changed.

Step 3: Flux 2 Klein 4B two-image style transfer against `.claude/agents/_jenny.assets/cover-style.jpg`, full style prompt:

```
A wide 2:1 ink drawing of a bamboo grove in four depth planes. In the bottom left corner and along the bottom edge, big bamboo leaves crop in as the nearest, darkest mass, drawn solid black. The leaf clusters hang on heavy stems, not air: each cluster sits at the tip of one thick tapering branch drawn in solid black, as heavy as the blades themselves and tapering from a broad base to a fine tip, never a hairline wire; two or three such branches carry all the foreground clusters, running from the leaves back through the black mass and out of the frame, and where a branch crosses the pale gray background the black stem stays broad, continuous and clearly legible. Behind them a dark cluster of near culms, then a mid-gray band of thinner culms receding, then a pale misty distance with one soft light patch near the top left; the left side stays lighter than the right. On the right rim two thick pale culms; between them thinner darker culms, leaf sprays at different heights and angles, one stalk leaning, ferns and grass tufts on the forest floor, one fallen culm lying across the litter. One small giant panda sits on the right third, about a third of the frame tall, both black eye patches and both eyes clear, both forepaws gripping one long thin culm with two node rings and a small leaf spray, the bitten peeled end at its mouth. Full tonal ladder: solid black foreground foliage, dark gray near culms, mid gray grove, light gray distance, paper white on the held culm and the lit side of the panda's head. Exactly one panda, no other animals, no text, no watermark.

Line work: loose, confident black ink/brush linework with visible overshoot strokes at joints and edges (classic concept-art "energy line" gesture drawing)

Shading: flat mid-gray fills for the base tone plus a single darker gray for core shadows — a 3-value system (white/light gray paper, mid-gray flat, black ink accents), no gradients or rendered soft shading

Rendering approach: shapes blocked in with a marker/brush rather than fully rendered — reads as a fast, expressive design sketch rather than a finished illustration

Palette: strictly achromatic (black/gray/white), grayscale digital marker brushes or Copic-marker-on-paper study
```

Picked seed: step 3 `580490558888935` (round 2 of the style pass; round 1 pick was `35143007750771`). Candidates: `/tmp/jenny-panda-18/round4-restyle/` and `/tmp/jenny-panda-18/round4b-restyle/`.

Kept as `cover.prev.png`.

## Rendered with _jenny (2026-11-17, round 5)

**Why the base changed.** Round 4 handed the same style prompt to the same step-2 photograph twice and still came back with foreground leaves hanging on nothing. The author's diagnosis: the fault is in the photograph, not the ink pass — the step-2 frame never gave the leaves a branch to hold, so the style model had nothing to trace. To test that, step 3 stayed identical to round 4 and the photographic chain was rebuilt underneath it: a new step 1 that makes the near branch itself the subject of the prompt, a new step 2 from that pick, the same step 3 prompt. The result attaches every foreground cluster to a branch (the fix held), at the cost of a smaller, flatter panda and a slightly emptier bottom-left than round 4. The author chose it over round 4.

A patch of the round-4 plate was tried first and abandoned: `comfy_cover.py patch` pastes a redraw of a named box into the rest of the frame, so it can move a branch but cannot supply one that was never in the photograph, and the box's top edge cut the culm it crossed.

Step 1: Z-Image Turbo, 1024×1024, n=4, two rounds. Round 1 named the branch but over-corrected into bright green saplings and lost the near-black mass; round 2 reframed the branch as the nearest object to the camera, which fixed it. The round-2 prompt:

```
A bamboo grove in four depth planes, photographed from inside the thicket. The nearest thing to the camera is a single bamboo branch: it enters from the bottom left corner of the frame, thick, black and out of focus-close, with one node ring visible, and forks into three tapering twigs that fan up and to the right across the lower left quadrant, each twig carrying a spray of narrow leaves along its length, every leaf joined to a twig that is continuous and clearly thicker than a leaf midrib. Because this branch is closest to the camera it is the largest and darkest thing in the picture, its leaves solid near-black against the mist behind. Behind it the grove recedes: thin dark culms, then a band of mid gray culms, then pale culms fading into mist, brightest near the top left corner, ferns and grass tufts and one fallen culm on the litter. One small giant panda sits on the right third, about a third of the picture height, both black eye patches and both eyes clear, both forepaws gripping one long thin culm with two node rings, the bitten peeled end at its mouth. Exactly one panda, no other animals, no text, no watermark.
```

Step 2: `--place right --subject-x 0.83`, n=3. The far-left ~360 px of the wide frame is invented by the outpaint, not carried over from the square.

Step 3: same prompt as round 4 — the test only works if the ink pass is held constant.

Picked seeds: step 1 `242069681560459`, step 2 `974791914190321`, step 3 `996584995123920` (candidate 1 of 4; p99 chroma 8). Delivered as `cover.png`; round 4 kept as `cover.prev.png`, round 3 as `cover.round3.png`. Candidates: `/tmp/jenny-panda-18/round5-step1r2/`, `/tmp/jenny-panda-18/round5-step2/`, `/tmp/jenny-panda-18/round5-step3/`.

## Coloured with _jenny (2026-11-17, colorize)

The author asked for a colour cover after the round-5 gray one was approved. `colorize` runs on that gray cover, so every ink line stays and only the fills change — 1950s four-colour comic print, Ben-Day halftone, slightly off-register, faded toward newsprint (`--saturation 0.55 --paper 0.18`, the approved defaults).

```bash
python3 .claude/agents/_jenny.assets/comfy_cover.py colorize \
  --image newsletter/18-next-newsletter/cover.jpeg \
  --palette "pale jade-green bamboo culms, deep forest green leaf masses, black and cream-white panda, pale misty blue-gray distance, ochre-brown forest floor litter" \
  --n 3 --out /tmp/jenny-color-18
```

Picked seed `3511485090349`: the cleanest white on the panda, crisp halftone, jade culms against a blue-gray distance. Candidate 1 (`417437485618514`) is warmer and creamier with a stray magenta patch in the bottom-left corner; candidate 2 (`553755957021742`) puts a lavender cast across the panda's back.

Delivered as `cover.jpeg` (404 KB). The gray round-5 render is kept at `assets/image-raw/cover.png`, and the colour raw at `assets/image-raw/cover-color.png`. Candidates: `/tmp/jenny-color-18/`.
