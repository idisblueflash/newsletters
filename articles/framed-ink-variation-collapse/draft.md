# Insight: Framed Ink Style Collapses Output Variation

**Question: which style should I generate my scene in for variations —
photorealistic or Ink style?**

**Takeaway:** The "Framed Ink" style descriptor block causes a variation
collapse that's a property of the prompt text itself, not the checkpoint
or sampler. Under the identical scene prompt, seeds, and settings, the
"Original real photo" style produced genuinely different poses and
compositions across 9 samples (variation score 6/10), while adding the
Framed Ink block collapsed nearly all 18 outputs to one near-identical
composition — same 3/4-profile pose, same whip angle, same sparse paper
count — despite using fully independent seeds (variation score 2-3/10).
This reproduced almost identically on a second, architecturally unrelated
model (Flux.2 Klein 4B), ruling out sampler/checkpoint as the cause.
**Practical implication:** don't rely on seed variety alone for
compositional diversity when using Framed Ink — vary the prompt's
pose/action language directly, since the style block itself suppresses
the model's exploration of the latent space.

## Evidence

Source: [variation-comparison-trial-results.md](variation-comparison-trial-results.md)
(9 explicit seeds condition only; batch=9 tracked these results closely
and is omitted here for simplicity)

**Hedge:** variation/quality scores are subjective 1-10 ratings assigned
by Claude Sonnet 5 looking at the images, not by a human rater — treat
them as a rough signal (the direction and size of the gap is large and
visually obvious from the grids below), not a precise or validated metric.

| Model | Style | Variation score |
|---|---|---|
| Z-Image-Turbo GGUF | Original real photo | 6/10 |
| Z-Image-Turbo GGUF | Framed Ink | 2/10 |
| Flux.2 Klein 4B GGUF | Original real photo | 8/10 |
| Flux.2 Klein 4B GGUF | Framed Ink | 3/10 |

### Z-Image-Turbo GGUF — Original real photo (6/10)

![s1a-1](images/variation-comparison-trial-1/style1-A-seed1.png)
![s1a-2](images/variation-comparison-trial-1/style1-A-seed2.png)
![s1a-3](images/variation-comparison-trial-1/style1-A-seed3.png)
![s1a-4](images/variation-comparison-trial-1/style1-A-seed4.png)
![s1a-5](images/variation-comparison-trial-1/style1-A-seed5.png)
![s1a-6](images/variation-comparison-trial-1/style1-A-seed6.png)
![s1a-7](images/variation-comparison-trial-1/style1-A-seed7.png)
![s1a-8](images/variation-comparison-trial-1/style1-A-seed8.png)
![s1a-9](images/variation-comparison-trial-1/style1-A-seed9.png)

### Z-Image-Turbo GGUF — Framed Ink (2/10)

![s2a-1](images/variation-comparison-trial-1/style2-A-seed1.png)
![s2a-2](images/variation-comparison-trial-1/style2-A-seed2.png)
![s2a-3](images/variation-comparison-trial-1/style2-A-seed3.png)
![s2a-4](images/variation-comparison-trial-1/style2-A-seed4.png)
![s2a-5](images/variation-comparison-trial-1/style2-A-seed5.png)
![s2a-6](images/variation-comparison-trial-1/style2-A-seed6.png)
![s2a-7](images/variation-comparison-trial-1/style2-A-seed7.png)
![s2a-8](images/variation-comparison-trial-1/style2-A-seed8.png)
![s2a-9](images/variation-comparison-trial-1/style2-A-seed9.png)

### Flux.2 Klein 4B GGUF — Original real photo (8/10)

![klein-s1a-1](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed1.png)
![klein-s1a-2](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed2.png)
![klein-s1a-3](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed3.png)
![klein-s1a-4](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed4.png)
![klein-s1a-5](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed5.png)
![klein-s1a-6](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed6.png)
![klein-s1a-7](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed7.png)
![klein-s1a-8](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed8.png)
![klein-s1a-9](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style1-A-seed9.png)

### Flux.2 Klein 4B GGUF — Framed Ink (3/10)

![klein-s2a-1](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed1.png)
![klein-s2a-2](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed2.png)
![klein-s2a-3](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed3.png)
![klein-s2a-4](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed4.png)
![klein-s2a-5](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed5.png)
![klein-s2a-6](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed6.png)
![klein-s2a-7](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed7.png)
![klein-s2a-8](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed8.png)
![klein-s2a-9](../2026-09-19/images/variation-comparison-flux2-klein-trial-2/style2-A-seed9.png)

Cross-model reproduction (Z-Image-Turbo's `dpmpp_sde`/5-step vs. Klein's
guidance-distilled `euler`/4-step) rules out a single sampler/architecture
quirk — the collapse tracks the Framed Ink prompt block across both.

## Notable side effect

Framed Ink's low variation is largely why it scored a *higher* good-count
than the Original photo condition: since the composition barely changes,
there's little scene-fidelity risk on any given seed. The Original photo
condition's lower good-count came from real fidelity misses (e.g. whip
reading as held-in-air or cane-like) that a repeated composition wouldn't
expose. Framed Ink also under-realized "papers exploding into the air"
(3-6 sheets vs. Original's 5-15+) — a separate prompt-adherence gap, not
caused by variation or seeding method.
