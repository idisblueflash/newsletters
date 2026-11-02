# The author's recurring issues

Mined from the `stage-log.md` of every post since 2026-10-03: each pattern below was raised as **blocking** in at least two posts, and is the kind a single stranger read tends to miss — a block readers skip silently (P7), or a slip you only see by comparing lines far apart (P5, P2). Other recurring issues (unintroduced terms, dangling references, missing steps, overclaims, tangled sentences) are left to `_cold_reader`, which catches them reliably. The IDs keep their original numbers.

Add a pattern here only if it is one `_cold_reader` misses; add an example when an old one comes back.

Each entry: what it looks like, past cases, and the fix direction that worked.

---

## P7 · Story stops for an explainer

**Looks like**: in a scene-driven piece, a paragraph switches to encyclopedia voice — no "I", no senses, definitions and categories first, the concrete example last, often followed by a code block or a block of numbers. Readers skip the whole block. A real reader did exactly this on one issue; `_cold_reader` had not flagged it.

**Past cases**: abstract problem cases before the example (10-04); app tour number-heavy, delays the hook (10-09); crowded L31 paragraph (10-28); concurrency explanation too long (10-23).

**Not a hit**: an explanation told as the author's own action, example first — 「AI 把这个单词的发音和意思编进一个生动的句子里，我管它叫辅助句」 (#14) keeps the "I" and names the term after showing it.

**Fix that worked**: explain only what the story needs right now, as a thing that happened to the author — one moment of the tool or idea doing something for them — then the catch that matters to the story. Concrete example first, term after (or never). Shrink code/data to one line, or move it to the end.

---

## P5 · The text contradicts itself

**Looks like**: two sentences, often far apart, that can't both be true — usually because one was edited and the other wasn't.

**Past cases**: "piling up" vs 6-jar cap (10-09); 小提示 vs 一个字的说明都没有 (10-12); 最近开始 vs 一直在做 (10-20); ending contradicts the story (10-23); "right every time" vs the tenth moment (10-21); 「是跟市场走不一样的」 misstating reason two (10-12).

**Fix that worked**: after any edit, search the draft for other sentences making the same claim and align them.

---

## P2 · One thing, several names (or several things, one name)

**Looks like**: the same entity called by different names, or a pronoun/name that could mean two of them — Claude / Claude Code / Sonnet / Jev; "seven files" vs "three places"; "150 个熟词" vs "解释句".

**Past cases**: which Claude did the second fix (10-28, still taste in read #4); Claude/Clash mixed (10-23); "seven files" vs "three places" (10-21, three rounds); 150 words vs sentences (11-02, two rounds).

**Fix that worked**: pick one name per entity and hold it through the whole piece; when two actors share a brand, give each a role label the first time ("Claude Code 在终端里…, 手机上的 Claude…").
