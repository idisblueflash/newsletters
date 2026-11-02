# The author's recurring issues

Mined from the `stage-log.md` of every post since 2026-10-03: each pattern below was raised as **blocking** by `_cold_reader` in at least two posts. Add a pattern here when a new one recurs; add an example when an old one comes back.

Each entry: what it looks like, past cases, and the fix direction that worked.

---

## P1 · Unintroduced name or term

**Looks like**: a tool, project, person, or coined word appears as if the reader already knows it — Jev, Sumomo, Clash, worktree, backlog, 辅助句, "taste", a rule like the coin/jar shelf.

**Past cases**: Jev unexplained (10-23, 10-28, 10-20); Sumomo vs Jev roles unclear (10-28); Clash/线路 unexplained (10-23); developer jargon and a second plugin unintroduced (10-21); "taste" undefined (10-21); app purpose undefined, "30 small day cells" undefined (10-09); Blow/McMillen unexplained (10-12).

**Fix that worked**: at first mention, one plain clause saying what it *does for the story* (not what it is in general). Or cut the name if the story doesn't need it (Jev was cut from 10-20).

## P2 · One thing, several names (or several things, one name)

**Looks like**: the same entity called by different names, or a pronoun/name that could mean two of them — Claude / Claude Code / Sonnet / Jev; "seven files" vs "three places"; "150 个熟词" vs "解释句".

**Past cases**: which Claude did the second fix (10-28, still taste in read #4); Claude/Clash mixed (10-23); "seven files" vs "three places" (10-21, three rounds); 150 words vs sentences (11-02, two rounds).

**Fix that worked**: pick one name per entity and hold it through the whole piece; when two actors share a brand, give each a role label the first time ("Claude Code 在终端里…, 手机上的 Claude…").

## P3 · Dangling reference

**Looks like**: "这个比喻", "this loop", "the trail", "my second reason", "the table" — pointing back to something the reader can't find, or that is too far back.

**Past cases**: "my second reason", "the trail" (10-21); "这个比喻" with no referent, "这个循环" far from its setup (10-12); "the table" (10-03).

**Fix that worked**: name the thing again instead of pointing at it, or move the setup next to the callback.

## P4 · Missing step or missing why

**Looks like**: the narrative jumps from problem to result, or states a choice without the reason. The author knows the reason; the reader isn't told.

**Past cases**: first failure's cause missing, second failure's cause vague (10-28); why not add a retry first (10-23); worktree argument missing the why (10-21); why the AI must pick instead of users (10-20); where exchanged coins go, what happens when the shelf is full (10-09); nib width → line spacing bridge, AI-template step (11-02).

**Fix that worked**: one sentence of cause between the two beats ("因为…，所以我…").

## P5 · The text contradicts itself

**Looks like**: two sentences, often far apart, that can't both be true — usually because one was edited and the other wasn't.

**Past cases**: "piling up" vs 6-jar cap (10-09); 小提示 vs 一个字的说明都没有 (10-12); 最近开始 vs 一直在做 (10-20); ending contradicts the story (10-23); "right every time" vs the tenth moment (10-21); 「是跟市场走不一样的」 misstating reason two (10-12).

**Fix that worked**: after any edit, search the draft for other sentences making the same claim and align them.

## P6 · Claim bigger than the evidence

**Looks like**: "the numbers show", "neither path is safe", a heading that states more than the section proves.

**Past cases**: "the numbers show" overclaim, "toss-up" sliding back to the stronger claim, "isn't safe" heading (10-09); history facts stated from memory and later corrected against the source (11-02).

**Fix that worked**: shrink the claim to what the example actually shows; check facts against the source before the cold read.

## P7 · Story stops for an explainer

**Looks like**: in a scene-driven piece, a paragraph switches to encyclopedia voice — no "I", no senses, definitions and categories first, the concrete example last, often followed by a code block or a block of numbers. Readers skip the whole block. A real reader did exactly this on one issue; `_cold_reader` had not flagged it.

**Past cases**: abstract problem cases before the example (10-04); app tour number-heavy, delays the hook (10-09); crowded L31 paragraph (10-28); concurrency explanation too long (10-23).

**Not a hit**: an explanation told as the author's own action, example first — 「AI 把这个单词的发音和意思编进一个生动的句子里，我管它叫辅助句」 (#14) keeps the "I" and names the term after showing it.

**Fix that worked**: explain only what the story needs right now, as a thing that happened to the author — one moment of the tool or idea doing something for them — then the catch that matters to the story. Concrete example first, term after (or never). Shrink code/data to one line, or move it to the end.

## P8 · Sentence too tangled to parse

**Looks like**: a thesis or pivot sentence packing two or three ideas, broken grammar left over from edits, or a sentence chopped by commas.

**Past cases**: thesis sentence tangled (10-21); backlog intro broken grammar (10-21); "这么干的人其他人" garbled pivot, comma-chopped sentence (10-12); L11 grammar (10-04).

**Fix that worked**: split into one idea per sentence; read the pivot aloud.
