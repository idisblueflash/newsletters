# 本地生图是不是越大越好？

横向对比三个模型看效果

**Takeaway**: bigger isn't better. 768×768 is roughly the cost/quality inflection point for every model tested here — pushing past it tends to buy new artifacts, not better images. What actually determines image quality is the model's own understanding of action and composition — and that's not something resolution can fix.

**要点**：不是越大越好。768x768 是合适的尺寸。从时间花费和品质上看，这个尺寸更好，而且三个不同的模型都这样。继续提高尺寸会带来奇怪的效果。如果模型自身对动作和构图的理解力不足，再大的尺寸也没用。

---

I ran the same experiment on my Mac mini (M4, 16GB) across three models — Z-Image-Turbo, Flux Schnell, and Flux.2 Klein: fixed prompt and seed, only the output resolution changes (512, 768, 1024, 1280 square). Here's what the timing and quality curves actually look like.

A few results are counter-intuitive.

我在自己的 Mac mini（M4，16GB）上测试了三个生图模型（Z-Image-Turbo，Flux Schnel 和 Flux 2 Klein）。我把其他生图参数都锁上了，只变了生成尺寸（512，768，1024，1280）。下面会根据时间和品质的维度具体分析。

有些结果挺反直觉的。

## 1. Time doesn't scale linearly with resolution — but the marginal cost keeps climbing

Going from 512×512 to 1280×1280 multiplies pixel count by 6.25×, but generation time only grows 3.7–4.4× across the three models — cheaper than the naive "quadratic in resolution" intuition suggests. But the *marginal* cost of each step climbs: 512→768 costs far less than proportional to pixel count, while 1024→1280 is almost exactly proportional to it. All runs here are warm (model already resident, no cold load), so the gap isn't model-loading — it's the other fixed, per-job costs that don't scale with resolution: text encoding, ComfyUI's graph dispatch, and per-step kernel-launch overhead (a fixed number of sampling steps regardless of size). At 512×512 that fixed overhead is a large share of a short run; by 1280×1280 it's diluted into a much longer one, and the sampler's own per-pixel compute takes over.

## 一、尺寸越大耗时越长

单靠直觉我们也能想通这一点。下面的图表也验证了我们的想法。

其实真实设计试验的时候，还是会考虑更多。比如，我不能把每次切换模型的时间算进去，而是要记录纯粹的生图时间。另外， ComfyUI 的生图流程中每个节点也是会耗时的。这种细节从简单的图表很难看出来。

| Model                | 512        | 768         | 1024        | 1280        | Time multiple (512→1280) |
| -------------------- | ---------- | ----------- | ----------- | ----------- | ------------------------ |
| Z-Image-Turbo GGUF   | 74.82s / 8 | 123.81s / 9 | 205.52s / 9 | 330.36s / 8 | 4.42×                    |
| Flux Schnell GGUF    | 54.83s / 6 | 81.78s / 7  | 134.78s / 7 | 212.05s / 6 | 3.87×                    |
| Flux.2 Klein 4B GGUF | 24.65s / 8 | 37.54s / 9  | 59.82s / 8  | 91.85s / 7  | 3.73×                    |

![Generation time growth from 512 to 1280 resolution for Z-Image-Turbo, Flux Schnell, and Flux.2 Klein, showing Z-Image-Turbo scaling fastest at 4.42× and Flux.2 Klein staying flattest at 3.73×](time-scaling-trend.png)

## 2. 768×768 is the sweet spot for all three models

Z-Image and Flux Schnell both plateau at 768 — matching their 1024 scores (9 and 7 respectively), so pushing past 768 buys nothing. Klein makes the case even more strongly: 768 is its single best score (9) in the entire sweep, and both 1024 and 1280 score lower. For Klein, 768 isn't just "good enough" — it's the actual optimum, and going higher is a net loss.

Cost efficiency (seconds spent per megapixel rendered) tells the same story from the other side: it keeps improving slightly past 768, but quality doesn't follow it there — so any extra efficiency you buy past 768 comes with no upside, only the same duplicated-object risk from insight #3.

## 二、768 x 768 是最佳尺寸

让我们换个思路，用回报率的角度来看。比如，我们把变大的部分用像素的面积表示，除以增加的数就能得到「秒/百万像素」这个指标。再把三个模型的平均值都算出来，再加上生图品质打分，放在图表上一起看：

![Average cost-per-megapixel and average quality score across all three models at each resolution, showing the two curves diverge after 768: quality drops from 8.33 to 7.0 while cost efficiency barely moves](return-on-time-spent.png)

从 768 之后的回报率就不高了。

往后再增加尺寸不会提升图片品质，还会引入新问题。

## 3. Higher resolution never fixes a problem — it only ever exposes a new one

Across this sweep, more resolution never repaired a compositional or anatomical flaw — it either left things unchanged or revealed something new. All three models' 1280×1280 outputs show the same class of artifact: a duplicated foreground still-life object. Z-Image gets a second inkwell, Flux Schnell a second carved bust, Klein an unexplained extra trinket.

## 三、提高尺寸不能修复原有问题

有时候提高尺寸可以让图片变得更好，但这也是看情况的。生图模型训练的时候会用固定的尺寸，这个尺寸生图才保险。低于或者高于这个尺寸都会有问题。比如模型是按照 512x512 训练的，256 生出来的图就不够好，提高到 512 效果一下子就好很多，可是提高到 1024 我们会看到人物变成了两个头叠加在一起的情况。

![Z-Image-Turbo, Flux Schnell, and Flux.2 Klein each showing a duplicated foreground object at 1280×1280](1280-artifact-grid.png)

## 4. Flux.2 Klein is the fastest of the three — and quality doesn't suffer for it

At every size, Klein runs 2–3× faster than Z-Image and 1.9–2.3× faster than Flux Schnell, while landing in the upper-middle of the quality range (matching Z-Image's score at 768, beating Flux Schnell at 512/1024/1280). That makes Klein the best speed/quality tradeoff in this sweep — with the caveat that this run's "warm-up" wasn't a genuine cold start, so Klein's real cold-load time is still unmeasured.

## 四、Flux 2 Klein 又快又好

如果我们的场景是那种简单的（机器人），Flux 2 Klein 是首选。但是如果我们的场景有复杂的人物动作和构图，就需要换 Z-Image-Turbo 了。

![Z-Image-Turbo, Flux Schnell, and Flux.2 Klein compared at 1024×1024, with generation time and quality score per model — Klein finishes in a third of Z-Image's time and still scores within one point](speed-quality-grid.png)

## 5. "Whip trailing to the ground" is a persistent miss for the Flux family, and a persistent win for Z-Image

The prompt calls for a specific action detail: the whip should trail taut across the ground. At every single size, Z-Image nails it. At every single size, Flux Schnell and Flux.2 Klein don't — the whip ends up held aloft, looped in-hand, or rigidly floating. This gap holds regardless of resolution, which points to a shared Flux-family (Schnell and its architecturally related sibling Klein) prompt-adherence limitation rather than anything resolution-related.

## 五、皮鞭的特例

在我的提示词里说到了皮鞭，只有 Z-Image-Turbo 还原了，其他模型没办法做到。不光是皮鞭的姿势奇怪，就连皮鞭本身也看上去像跟绳子。这种问题和尺寸关系不大，因为同样的 Flux 系列模型都有这种问题。

![Z-Image-Turbo, Flux Schnell, and Flux.2 Klein compared on whip-to-ground contact at 768×768](whip-ground-grid.png)

以上。
