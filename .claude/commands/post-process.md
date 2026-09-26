---
description: Post-processing for a finished article — write descriptive image alt text, convert PNG images to JPEG, archive the original PNGs and their grid/table source HTML into assets/image-raw/, then generate beehiiv.html and open it
argument-hint: [article directory or draft.md path]
---

# /post-process

Four wrap-up steps once an article's content is finalized. Run them in order, giving a brief report after each step before moving to the next.

## 0. Determine the target article directory

- If `$ARGUMENTS` is a directory path, use it directly.
- If `$ARGUMENTS` is a file path (e.g. `articles/xxx/draft.md`), use its containing directory.
- If `$ARGUMENTS` is empty, use the article directory currently being worked on in this conversation (the `draft.md` most recently read or edited in this session or recent turns); if it can't be determined, ask the user.

Below, `<dir>` refers to this directory.

## 1. Write descriptive image alt text

- Find every `![alt](path)` image reference in `<dir>/draft.md`.
- For each image, use the Read tool to actually look at the image content (read local paths directly, for every image that can be read), and rewrite the alt text into a sentence that concretely describes what's in the picture — not a placeholder (like the generic drafting-stage text such as "图：方形图片" or "图组：xxx 对比"), but something specific enough that someone who hasn't seen the image can tell what it shows from the alt text alone; for a comparison/grid image, call out what's being compared.
- Keep the repo's existing alt-text formatting convention (wrapped in 「」, a single image starting with "图：…", a group/grid image starting with "图组：…") — only replace the descriptive part in the middle, don't change the overall structure or the image path.
- Update `<dir>/draft.md` in place. No need to report each individual change — a short "alt text updated" after this step is enough.

## 2. Convert PNG to JPEG

- Find all `*.png` files at the top level of `<dir>` (do not recurse into `assets/`, `images/`, or similar subdirectories):
  ```
  find <dir> -maxdepth 1 -iname "*.png"
  ```
- For each file, call the web-image-optimize script, keeping the original pixel dimensions and no filename suffix:
  ```
  python3 .claude/skills/web-image-optimize/scripts/optimize.py <file> --suffix ""
  ```
- The script outputs `.jpg`; rename it to `.jpeg` to match the repo's existing naming convention (see `articles/z-image-vs-flux`):
  ```
  mv <stem>.jpg <stem>.jpeg
  ```
- Leave the converted `.jpeg` at the top level of `<dir>`; leave the original `.png` in place for now — it gets archived in step 3.
- For every file just converted, check whether `<dir>/draft.md` links to it by its old `.png` name (or `.png` inside any path, e.g. `./original.png`) and update that reference to the new `.jpeg` filename in place, keeping the rest of the image line (alt text, path prefix) untouched. Skip files that draft.md doesn't reference — plenty of top-level PNGs are just raw source material for `_gala`/`_tabitha` outputs living under `assets/images/`, not something draft.md points to directly.

## 3. Archive the original PNGs and their source HTML

- Create the directory: `mkdir -p <dir>/assets/image-raw`
- Move the original `*.png` files at the top level of `<dir>` (the conversion sources from step 2), along with their companion grid/table generation source files (`*.source.html`, or any other top-level HTML file that's clearly used by `_gala`/`_tabitha` to render that image), into `<dir>/assets/image-raw/`, keeping filenames unchanged.
- Use `git mv` rather than plain `mv` to preserve git history; if a file isn't tracked yet, plain `mv` is fine.
- Do not move images already under `<dir>/assets/images/` that have been synced — that directory is used by cova for syncing to R2 and is out of scope for this archiving step.

## 4. Generate HTML and open it

- Call the `beehiiv-draft2html` skill with the target file `<dir>/draft.md` to generate/update `<dir>/beehiiv.html`.
- Open it in the default browser with `open <dir>/beehiiv.html`.

## Wrap-up

Once all four steps are done, show the user the changes with `git status`. Do not auto-commit — committing happens only after the user confirms (unless the user has already said in this conversation to go ahead and commit).
