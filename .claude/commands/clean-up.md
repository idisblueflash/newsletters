---
description: Wrap up a finished article branch — commit the remaining work, push, open (or reuse) the PR linked to its board card, merge into main, then switch back to main and fast-forward it to origin
argument-hint: [optional commit message or PR title]
---

# /clean-up

The article is done and post-processed. This command takes the branch from "files sitting in the working tree" to "merged into main, local main clean and up to date."

Run the steps in order, giving a one-line report after each before moving on. Steps 4 and 5 are the two that leave the machine — **each needs the user's explicit go-ahead** (see below).

The user's natural phrasing for this is "commit, open a PR, push, merge, go back to main" — the actual git order is commit → push → PR → merge, and that's what this command does.

## 0. Preflight

```bash
git status
git branch --show-current
```

- **If the current branch is `main`, stop.** There is nothing to merge. Tell the user and ask which branch they meant.
- If the working tree is completely clean **and** the branch has no unpushed commits **and** there is no open PR, there is nothing to do — say so and stop.
- Note the article directory the changes live in (`articles/<slug>/`); steps 2 and 3 need it.

## 1. Review what is about to be committed

```bash
git status --short
git diff --stat
```

Show the user the file list and call out anything that looks like it should **not** be committed, before staging:

- Raw generation scratch directories (e.g. `outpaint-swift/`, `issue-outpaint/`, `left-only-outpaint/`) — these are usually working material, not article assets. Ask before including them.
- `.DS_Store` — never commit it.
- Anything outside `articles/<slug>/` and `.claude/` that the user didn't expect to touch.

If anything is questionable, ask **once**, as a single batched question. Don't ask file by file.

## 2. Commit

Stage what survived step 1 and commit. If the remaining changes cover clearly separate concerns (draft edits vs. image conversion vs. archiving vs. generated HTML), make **separate atomic commits** — this repo commits one reason at a time.

```bash
git add <paths>
git commit -m "$(cat <<'EOF'
<类型>: <中文说明，写清改动的原因>

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
EOF
)"
```

Commit message convention (match the existing log — run `git log --oneline -10` if unsure):

- **Written in Chinese**, with a prefix naming the area: `正文:`, `配图:`, `SEO:`, `工作流:`, `[draft]`.
- Say *why*, not just *what*. "配图: PNG 转 JPEG 并归档原图" beats "update images".
- If `$ARGUMENTS` is given, use it as the commit subject (still add the prefix and the `Co-Authored-By` line).

## 3. Push

```bash
git push -u origin <branch>
```

If the remote branch already exists and has diverged, **do not force-push**. Report the divergence and ask the user how they want to resolve it.

## 4. Open or reuse the PR

First check whether one already exists:

```bash
gh pr view --json number,url,state 2>/dev/null
```

- **If an open PR exists**, reuse it. The push in step 3 already updated it. Report its number and URL.
- **If there is no PR**, create one. Per the S.O.P in `agents.md`, the PR must **link the GitHub project board card** for the article:

  ```bash
  gh project item-list 3 --owner idisblueflash
  ```

  Find the card matching this article's topic and include its URL in the PR body. If `gh` fails with a missing `read:project` scope, tell the user to run `gh auth refresh -s read:project` — don't silently skip the link.

  ```bash
  gh pr create --title "<PR 标题>" --body "$(cat <<'EOF'
  ## Summary

  <1-3 条，说明这篇文章写了什么、这个分支做了哪些事>

  Card: <board card URL>

  🤖 Generated with [Claude Code](https://claude.com/claude-code)
  EOF
  )"
  ```

  Use `$ARGUMENTS` as the PR title if it was given and reads like a title.

**Opening a PR is outward-facing.** If the user's invocation didn't already say "open a PR" or "merge it," confirm before creating one.

## 5. Merge

**Always confirm before merging, even if the user said "merge" when invoking the command** — show them the PR URL and the commit list first, since merging into `main` is the one step here that is hard to undo:

> 确认把 PR #<n> merge 进 main？分支一并删除吗？

On a yes:

```bash
gh pr merge <pr_number> --merge --delete-branch
```

Use `--merge` (not squash or rebase) to match this repo's history. Drop `--delete-branch` if the user wants to keep the branch.

If the merge is blocked (conflicts, failing checks, review required), **report the actual reason from `gh`** and stop. Don't try to work around it.

## 6. Back to main, synced with remote

```bash
git checkout main
git fetch origin
git merge --ff-only origin/main
```

`--ff-only` is deliberate: local `main` should never carry commits of its own, so a non-fast-forward here means something is wrong and deserves a report rather than a merge commit.

Then confirm the end state:

```bash
git status
git log --oneline -5
```

## Wrap-up

Report, in one short block:

- The commits that were made
- The PR number and URL, and whether it was created or reused
- Whether it merged, and whether the branch was deleted
- That local `main` is now at `origin/main` (quote the top commit)

If any step was skipped or blocked, say which one and why — don't report a clean finish over a partial one.
