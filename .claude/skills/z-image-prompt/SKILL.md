---
name: z-image-prompt
version: 1.0.0
description: Generate a Z-Image Turbo (Alibaba Tongyi S3-DiT model) image prompt from article/text content, for local ComfyUI rendering. Activate when the user says "z-image prompt", "generate a Z-Image prompt", "write a ComfyUI prompt", "Turbo mode prompt", or "make me an image prompt (Z-Image)". Do not reuse the inkframe/blockframe layered formula here — Z-Image Turbo's prompt style is completely different from Nano Banana's.
---

# Z-Image Turbo Prompt Generator

Generates prompts for **Z-Image Turbo** (Alibaba Tongyi Lab's S3-DiT architecture, a 6B distilled model) running locally in ComfyUI. This model's prompting style differs from Nano Banana / SDXL-family models — porting those conventions over noticeably hurts output quality. Read the hard rules below first.

## Hard rules for Z-Image Turbo

| Rule | Why |
|------|-----|
| **Write one natural-language instruction, not a comma-separated tag list** | The model reads the prompt like a sentence, not like tag-matching in older SD models. Write it like a director's brief to a camera crew, not a list of adjectives |
| **There is no working negative prompt** | The distilled Turbo variant doesn't use CFG at inference, so ComfyUI's negative-prompt box mostly does nothing. Every "don't want" has to become a positive constraint clause appended to the end of the positive prompt |
| **Stick to 3-5 core concepts — don't stack adjectives** | Attention drifts past that, and the image gets muddier, not better. Contradictory styles ("photoreal anime cel-shaded oil painting") produce an uncanny four-way mashup |
| **Use concrete texture words, not vague quality words** | To avoid a plastic look, name pores, fabric weave, film grain, brushstrokes — not "high quality" or "detailed" |
| **Wrap any text you want rendered in the image in double quotes** | Accurate quoted-text rendering is one of Z-Image's real strengths; don't quote anything else |
| **Aim for ~80-250 words, token cap 512 (can push to 1024)** | Long and specific beats short and vague |

Source: [Z-Image-Turbo Prompting Guide](https://gist.github.com/illuminatianon/c42f8e57f1e3ebf037dd58043da9de32), [ComfyUI official tutorial](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo)

## Recommended ComfyUI sampler settings

Pass these along too — they're not part of the prompt text, but they directly affect output quality:

- **Steps**: 8 (sweet spot is 5-9; past 9 steps quality typically gets worse, not better)
- **CFG / guidance**: 1.0-2.0 (the official pipeline uses 0.0; pushing the ComfyUI CFG node to 4+ noticeably degrades results and just slows generation down for no gain)
- **Negative prompt box**: leave it empty — it's mostly inert
- **Resolution**: generate at 1024×1024 first for the most stable quality; for higher res, use an upscale node + a second KSampler pass (denoise ≈ 0.3) rather than generating straight to 2K, which tends to distort
- **Seed**: lock it while iterating on wording, so what you see is the effect of the wording, not random noise

## Prompt structure (fill in this order)

```
[shot & subject] + [age & appearance] + [clothing & color] + [environment/background]
+ [lighting] + [mood] + [style/medium] + [technical notes] + [positive constraint/cleanup clause]
```

Detail on each part:

1. **Shot & subject**: shot type (close-up / medium / full-body / wide), angle, who's doing what
2. **Age & appearance**: for any human, spell out an age bracket explicitly (e.g. "adult woman") to avoid the model defaulting to ambiguous or underage-looking figures
3. **Clothing & color**: 3-5 words naming the outfit and the dominant palette
4. **Environment**: keep the background as simple as possible — clutter competes with the subject
5. **Lighting**: Z-Image responds strongly to lighting keywords (e.g. "soft diffused daylight", "cinematic warm key light") — this one clause carries most of the mood
6. **Mood**: a word or two to set the tone, but let lighting/composition/action carry it rather than piling on emotional adjectives
7. **Style/medium**: photography, illustration, oil painting, flat vector, etc. — pick one, don't mix
8. **Technical notes**: lens focal length, resolution, focus behavior — camera-language, not vague quality words
9. **Positive constraint/cleanup clause**: goes at the very end of the paragraph, turning every "don't want" into a positive statement, e.g. `simple uncluttered background, no text, no watermark, no extra limbs, safe for work`

## Workflow

### Step 1: Confirm which image this is for

Read the user's target file (default to `draft.md` or `seo.md` in the current article folder if unspecified), or take the scene the user describes directly. If the article has several image-worthy motifs, confirm which one to use:

> I see a few motifs in this article that could work as an image: [list 2-3]. Which one do you want, or do you already have a scene in mind?

Don't pick the theme for the user — but if they've already given you a concrete scene, skip straight to Step 2.

### Step 2: Extract the visual elements from the content

For the confirmed theme, work out (no need to narrate each one to the user unless something's ambiguous):

- Who/what the subject is and what it's doing
- If a person is involved: age bracket + clothing + setting need to be explicit, so the model doesn't fill in defaults on its own (words like "CEO" or "model" carry stereotype baggage — better to swap in "role + concrete appearance description")
- Environment/background — the simpler the better
- Light direction and hardness
- Desired medium/style (realistic photo / illustration / flat vector / hand-drawn…) — one quick question to the user unless it's already obvious from context
- Whether any text needs to appear in the image (a title, a sign, etc.) — if so, note the exact string to wrap in double quotes

### Step 3: Write it as one natural-language prompt

Following the structure order above, write one continuous paragraph (not a list, not comma-separated tags), roughly 80-250 words. The positive constraint clause goes as the final sentence.

Deliver it in a code block so the user can paste it straight into ComfyUI's CLIP Text Encode node:

```
[full English prompt]
```

Follow with one line of sampler guidance, e.g.:

> Steps 8 / CFG 1.5-2.0 / resolution 1024×1024 / leave negative prompt empty

### Step 4: Iterate as needed

When the user asks for "more of X," edit only the relevant clause (e.g. the lighting sentence or the environment sentence) rather than rewriting the whole paragraph — and remind them to lock the seed before tweaking wording, so they're seeing the effect of the wording change, not random variance.

## Example

**Input scene**: a newsletter piece about information overload eroding focus, wanting a flat-illustration-style image.

**Output prompt**:

```
Flat vector illustration of an adult person sitting at a small desk in
the center of a plain pale-gray room, surrounded by dozens of floating
rectangular screens and notification bubbles that drift in from every
direction, screens rendered as simple glowing rectangles with tiny
abstract icons, no readable text on any screen. The person's shoulders
are slightly hunched, one hand raised halfway toward the nearest screen,
head tilted down. Soft even studio lighting with no strong shadows,
muted pastel palette of dusty blue, warm gray and soft yellow. Minimal
flat shading, clean thin outlines, generous negative space around the
desk to emphasize isolation. Modest casual clothing, long-sleeved shirt
and trousers, fully clothed. Simple uncluttered composition, no text, no
watermark, no logos, no extra limbs, safe for work.
```

> Steps 8 / CFG 1.5-2.0 / resolution 1024×1024 / leave negative prompt empty
