---
description: Start a new article draft: create a new branch, scaffold a placeholder folder under articles/, and save it as draft.md
argument-hint: [draft text or file path]
---

# /new-post

The user wants to start a new article. Follow these steps:

## 0. Check the GitHub project board first

Per the S.O.P in `agents.md`, daily article topics come from the [GitHub project board](https://github.com/users/idisblueflash/projects/3/views/1?layout_template=board).

- Run `gh project item-list 3 --owner idisblueflash` to check the board for a card in `In Progress` status.
  - If it fails with missing `read:project` scope, tell the user to run `gh auth refresh -s read:project` to authorize — don't skip this and go straight to the ad-hoc flow.
- If an `In Progress` card is found:
  - Name the branch after the card's topic (not the placeholder `<date>-<slug>` format — use the topic directly, per agents.md).
  - The card's title is the topic; a title is all a new post ever starts with, so no draft body is expected yet.
  - After creating the draft (steps 3-4) and committing (step 5), **open a PR** and **link the card** in the PR description or a comment (`gh pr create` + reference the issue/card URL).
  - In that case, adjust the step 6 wrap-up to say "PR created and linked to the board card" instead of "don't push or open a PR automatically".
- If there's no `In Progress` card on the board, or the user explicitly says they want an ad-hoc draft outside the board, fall through to the ad-hoc flow below.

## 1. Get the topic / draft content

- If `$ARGUMENTS` is an existing file path, use Read to load its content as the draft.
- If `$ARGUMENTS` is a block of text longer than a short title, use it directly as the draft body.
- Otherwise (no board card, no `$ARGUMENTS`, or `$ARGUMENTS`/the card title is just a short title) there is no body yet — that's normal for a new post. Don't ask the user for content and don't fabricate any; just use the title for the folder-name slug (step 2) and seed `draft.md` with that title as a single `# <title>` heading (step 4).

## 2. Generate a placeholder folder name

This is a placeholder name, not the final article title — it can be changed later. Format is fixed as `<YYYY-MM-DD>-<slug>` (the date prefix keeps things sorted chronologically and easy to find):

- Prefer extracting 2-4 English words from the draft's first line / title as the slug, in kebab-case (match the naming style of existing directories under `articles/`, e.g. `picture-the-word`, `dog-and-breakfast`).
- If the draft has no clear title to extract from, use `new-post` as the slug.
- Use today's date (`YYYY-MM-DD`).
- Run `ls articles/` to confirm there's no existing directory with the same name; if there's a collision, append `-2`, `-3`, etc. to the slug.

## 3. Create the branch

First confirm the working tree is clean (`git status`); if there are uncommitted changes, warn the user first — don't overwrite them.

```
git checkout main
git pull
git checkout -b <placeholder-folder-name>
```

## 4. Write the draft

```
mkdir -p articles/<placeholder-folder-name>
```

Write the draft content to `articles/<placeholder-folder-name>/draft.md` — the full body if step 1 found one, otherwise just a `# <title>` heading.

## 5. Commit

```
git add articles/<placeholder-folder-name>/draft.md
git commit -m "[draft] <short description>"
```

Write the commit message in Chinese, summarizing what the article is about — not an empty phrase like "add new article" (matches this repo's existing commit convention).

## 6. Wrap up

Tell the user:
- The new branch name
- The draft file path
- A reminder that they can say "start editing the article" to kick off the S.O.P flow in `agents.md`
- Don't push or open a PR automatically, unless the user explicitly asks
