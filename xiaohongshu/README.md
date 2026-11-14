# 小红书短笔记 — idea lab

Daily short posts on 小红书 are the top of the funnel: each note tests **one** idea in public.
The notes that get saved and commented on become the next full-length articles. Nothing here
goes through the article branch/PR flow — notes live directly on `main`.

**You write every published word.** The assistant asks the next question, transcribes your own
words, and counts characters. It does not draft the claim, the title, or the body.

## The loop

1. **Capture** — `inbox.md`, one line per idea, dated. Don't expand it.
2. **State the claim** — `/short-post` starts a guided session. You say the one judgment the
   note will test, in your own words. The assistant asks; it doesn't propose one.
3. **Build the support** — you answer who would disagree, what specific evidence supports it,
   and what the first line is. The assistant asks one question at a time and transcribes.
4. **Write the note** — you write the body. The assistant can count characters and point at a
   sentence that doesn't support the claim; it cannot rewrite that sentence.
5. **Publish** — copy the title, body and tags into 小红书 by hand. Then fill in the URL in
   `note.md`, set `status: published`, and add a row to `ledger.md`.
6. **Read the signal** — after 48h, and again after a week, copy 浏览 / 点赞 / 收藏 / 评论 into
   `ledger.md`. Record **which part** people responded to and what the top comments say.
7. **Promote** — `/short-review` ranks the ledger, picks the strongest note, and turns the
   resonant part into a long article under `articles/` (the normal `WORKFLOW.md` stages then
   apply). The article keeps a `source_note:` line pointing back here.

## The four questions

The whole note comes from these, answered in your words:

1. **判断** — 你想让读者接受的那一句话是什么？
2. **反面** — 谁会不同意？什么观察会让它不成立？
3. **证据** — 哪个具体场景、数字、前后对比或一句原话撑住它？
4. **第一行** — 怎么写才能让陌生人想知道这个判断？

If you cannot answer 1 in one sentence, it is an inbox idea, not a note. If you cannot answer 3
with something concrete, the note is an assertion — wait until you have the example.

## Rules

- **Experience, not instruction.** The claim is something you lived, not a law. Write what
  happened to you and what you now do; don't tell the reader what they should do. No "you
  should", no "the rule is", no lesson handed down from above. The reader takes the lesson
  themselves.
- **Interesting and useful, to the reader.** A note earns its place only if a stranger gets
  something from it — an idea worth knowing, or a move worth copying. Interesting alone is
  entertainment; the note is a probe.
- **Useful beats interesting.** When the two pull apart, cut the interesting-but-useless part.
  Saves are the signal this whole loop ranks on, and people save what they can use.
- **You write every published word.** The assistant asks, transcribes, counts. It does not
  compose, rewrite, or suggest phrasing unless you explicitly ask for it.
- **One idea per note.** If a note carries three ideas you cannot tell which one landed.
- **The claim is yours.** The assistant does not issue a PASS/FIX verdict; it only points out
  an empty answer or a sentence that does not support your claim.
- **The first line is the hook.** 小红书 truncates the body; a stranger must know why to keep
  reading before the "…more" fold.
- **Concrete before abstract.** One scene, one number, one before/after. No thesis statement
  without an example.
- **End with a question**, not a summary. Comments are the signal you are collecting.
- **≤ 20 characters for the title, ≤ 1000 characters for the body** (punctuation counts).
  Tags go at the end of the body.
- **The cover is optional.** If used: 3:4 (1080×1440), JPEG, one clear subject. Text-only notes
  are fine — don't let a cover block the daily cadence.
- **Never delete an idea.** Mark it `dropped` in the ledger with a one-line reason. The inbox is
  an asset, not a queue.
- **No branch, no PR.** Commit notes on `main` if you feel like it (`[note] ...`), or leave them
  uncommitted. They are probes, not shipped artifacts.

## What counts as "popular"

Rank by **saves** first, then **comments**. Likes are the weakest signal.

| Signal | What it means | What to do |
|---|---|---|
| 收藏 | "I'll need this later" — the utility landed | candidate for a how-to article |
| 评论 asking the same question | a missing step or an undefined term | answer it in the long post |
| 评论 quoting one line | that line is the hook | build the article around that line |
| 点赞 only | agreement, no pull | not enough on its own |
| 私信 / 涨粉 | the topic has an audience | prioritize |

**Promotion rule:** promote a note when it has either (a) saves ≥ 3× your median, (b) at least
3 comments circling the same point, or (c) you want to write the topic anyway (strategic
override). Expand the **part that resonated** — don't summarize the whole note.

## Layout

```
xiaohongshu/
├── README.md            # this file
├── inbox.md             # raw one-line ideas, append-only
├── ledger.md            # every published note + its numbers
├── _template/
│   └── note.md          # per-note template
├── _archive/            # superseded / AI-generated material, never published
└── 2026-11-13-<slug>/
    └── note.md          # one folder per note, date-prefixed like articles/
```

## Commands

- `/short-post` — guided session: 判断 → 反面 → 证据 → 第一行 → your body.
- `/short-review` — weekly ranking, pick the next long article.
- `claim-guide` — run the four questions directly on any note.

If a note is promoted, the article's `draft.md` gets `source_note: xiaohongshu/<folder>` in its
frontmatter and `stage-log.md` records the promotion.
