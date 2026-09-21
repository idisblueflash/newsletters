# Does a Bigger Output Resolution Actually Help? A Size Sweep Across Three Models

I ran the same experiment on my Mac mini (M4, 16GB) across three models — Z-Image-Turbo, Flux Schnell, and Flux.2 Klein: fixed prompt and seed, only the output resolution changes (512, 768, 1024, 1280 square). Here's what the timing and quality curves actually look like.

A few results are counter-intuitive.

## 1. Time doesn't scale linearly with resolution — but the marginal cost keeps climbing

Going from 512×512 to 1280×1280 multiplies pixel count by 6.25×, but generation time only grows 3.7–4.4× across the three models — cheaper than the naive "quadratic in resolution" intuition suggests. But the *marginal* cost of each step climbs: 512→768 costs far less than proportional to pixel count (a fixed, resolution-independent overhead — queueing, model dispatch — dominates at this end), while 1024→1280 is almost exactly proportional to pixel count, as that fixed overhead gets diluted and the sampler's own per-pixel cost takes over.

| Model | 512 | 768 | 1024 | 1280 | Time multiple (512→1280) |
|---|---|---|---|---|---|
| Z-Image-Turbo GGUF | 74.82s / 8 | 123.81s / 9 | 205.52s / 9 | 330.36s / 8 | 4.42× |
| Flux Schnell GGUF | 54.83s / 6 | 81.78s / 7 | 134.78s / 7 | 212.05s / 6 | 3.87× |
| Flux.2 Klein 4B GGUF | 24.65s / 8 | 37.54s / 9 | 59.82s / 8 | 91.85s / 7 | 3.73× |

![Generation time growth from 512 to 1280 resolution for Z-Image-Turbo, Flux Schnell, and Flux.2 Klein, showing Z-Image-Turbo scaling fastest at 4.42× and Flux.2 Klein staying flattest at 3.73×](time-scaling-trend.png)

## 2. 768×768 is the sweet spot for all three models

Z-Image and Flux Schnell both plateau at 768 — matching their 1024 scores (9 and 7 respectively), so pushing past 768 buys nothing. Klein makes the case even more strongly: 768 is its single best score (9) in the entire sweep, and both 1024 and 1280 score lower. For Klein, 768 isn't just "good enough" — it's the actual optimum, and going higher is a net loss.

## 3. Higher resolution never fixes a problem — it only ever exposes a new one

Across this sweep, more resolution never repaired a compositional or anatomical flaw — it either left things unchanged or revealed something new. All three models' 1280×1280 outputs show the same class of artifact: a duplicated foreground still-life object. Z-Image gets a second inkwell, Flux Schnell a second carved bust, Klein an unexplained extra trinket.

![Z-Image-Turbo, Flux Schnell, and Flux.2 Klein each showing a duplicated foreground object at 1280×1280](1280-artifact-grid.png)

## 4. Flux.2 Klein is the fastest of the three — and quality doesn't suffer for it

At every size, Klein runs 2–3× faster than Z-Image and 1.9–2.3× faster than Flux Schnell, while landing in the upper-middle of the quality range (matching Z-Image's score at 768, beating Flux Schnell at 512/1024/1280). That makes Klein the best speed/quality tradeoff in this sweep — with the caveat that this run's "warm-up" wasn't a genuine cold start, so Klein's real cold-load time is still unmeasured.

## 5. "Whip trailing to the ground" is a persistent miss for the Flux family, and a persistent win for Z-Image

The prompt calls for a specific action detail: the whip should trail taut across the ground. At every single size, Z-Image nails it. At every single size, Flux Schnell and Flux.2 Klein don't — the whip ends up held aloft, looped in-hand, or rigidly floating. This gap holds regardless of resolution, which points to a shared Flux-family (Schnell and its architecturally related sibling Klein) prompt-adherence limitation rather than anything resolution-related.

![Z-Image-Turbo, Flux Schnell, and Flux.2 Klein compared on whip-to-ground contact at 768×768](whip-ground-grid.png)

---

**Takeaway**: bigger isn't better. 768×768 is roughly the cost/quality inflection point for every model tested here — pushing past it tends to buy new artifacts, not better images. What actually determines image quality is the model's own understanding of action and composition — and that's not something resolution can fix.
