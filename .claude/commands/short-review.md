---
description: Weekly 小红书 review — rank published notes by saves and comments, pick the part worth promoting, and scaffold the long article.
argument-hint: [optional: paste the numbers to update first]
---

# /short-review

Find the note whose **part** deserves a full-length article. Ranking is only a conversation
starter — the point is to read the comments and locate what resonated.

## 0. Load

Read `xiaohongshu/README.md`, `xiaohongshu/ledger.md`, and `xiaohongshu/inbox.md`.

## 1. Update stale numbers first

For every `published` row whose latest numbers are missing or older than 48 hours:

- If `$ARGUMENTS` contains the numbers, write them into the ledger.
- Otherwise list exactly which notes need numbers, ask the user to paste them in one message
  (浏览 / 点赞 / 收藏 / 评论 per note), and **stop**.

Do not guess or estimate any metric.

## 2. Rank

- Ignore rows with status `promoted` or `dropped`, and notes published less than 48 hours ago.
- Order by `saves × 3 + comments × 2 + likes`. Call this a *sort key, not a verdict*.
- Compute the median save count of the remaining rows.

## 3. Present the top 3

For each, show: title, age, the numbers, the recorded 最有共鸣的部分, and the gist of the top
comments. Then:

- Recommend one **primary** and one **backup** to promote.
- Say which promotion trigger fired (saves ≥ 3× median / ≥ 3 comments on one point /
  strategic override).
- Name the **part** to expand — a specific paragraph, line, or unanswered question. The long
  article deepens that part; it does not summarize the whole note.
- Carry over the note's `Claim` block: the article's job is to defend that claim with more
  evidence, not to retell the note at length.

Ask the user to pick one, or say "none this week". **Stop here.**

## 4. Scaffold the article (after the user picks)

Use the ad-hoc flow in `.claude/commands/new-post.md`:

- Branch: `git checkout main && git pull && git checkout -b <YYYY-MM-DD>-<slug>`.
- Folder: `articles/<YYYY-MM-DD>-<slug>/`, file `draft.md`.
- Seed `draft.md` with frontmatter containing `source_note: xiaohongshu/<folder>` and the
  note's working title. Add a `## 素材` section containing, **verbatim**: the author's claim,
  the line or paragraph that resonated, and the comments that circled it. Do not write body
  prose — the long article is the author's; the assistant has only assembled the material.
- Append to `stage-log.md`:
  `- <date> · Promoted from 小红书 note <path>; resonant part: <part>.`
- Set the ledger row to `promoted` and fill `article:` in the note's frontmatter.
- Do not push, do not open a PR, do not merge.

## 5. Report

Give the branch, the draft path, and the resonant part it will expand. Tell the user to say
"continue" when `draft.md` is complete — `WORKFLOW.md` takes over from there.
