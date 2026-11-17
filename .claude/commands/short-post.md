---
description: Guide the author from one claim to its support, then scaffold the note. The author writes every word; this command only asks, transcribes, and counts. No branch, no PR.
argument-hint: [starting image, scene, or idea — optional]
---

# /short-post

This is a guided session, not a drafting session. **You do not write the claim, the title, or
the body.** The author writes; you ask the next question and transcribe their own words.

## 0. Load

Read `xiaohongshu/README.md` and `xiaohongshu/_template/note.md`, then follow the `claim-guide`
skill.

## 1. Start from the author's material

- If `$ARGUMENTS` is non-empty, treat it as the starting point — a scene, an image, a detail.
  It is **not** a claim yet.
- If empty, ask one question: 「今天想从哪件事、哪个画面开始？」
- Do not propose topics or claims.

## 2. The four questions, all in one message

Put all four in a single message, numbered, and let the author answer them together — as many as
they can. Quote each answer back verbatim, then follow up **only on the ones left blank**, one at
a time. Never answer a question yourself; never offer a "better" version.

1. 「这条 note 只验证一个判断。你想让读者接受的那一句话是什么？」
2. 「谁会不同意？什么观察会让这个判断不成立？」
3. 「你手里哪个具体场景、数字、前后对比或一句原话，能撑住这个判断？」
4. 「第一行怎么写，才能让陌生人想知道这个判断？」

If an answer is vague, ask one smaller question rather than supplying the missing content.

## 3. Create the folder and transcribe (only after all four are answered)

- Slug: 2–4 English words from the author's own claim, kebab-case.
- Folder: `xiaohongshu/<YYYY-MM-DD>-<slug>/` (append `-2`, `-3` on collision).
- Copy `_template/note.md` into it as `note.md`.
- Fill `date`, `status: drafted`, and `source_idea` with the author's opening idea verbatim.
- Fill `这一条只验证一个判断` with the four answers **verbatim**. Do not polish.

## 4. The author writes the body

Ask the author to write the body — in the chat or directly in `note.md`. If in the chat,
transcribe it verbatim, word for word.

Then count characters (replace the path):

```bash
python3 - <<'PY'
import re
from pathlib import Path
text = Path("xiaohongshu/<folder>/note.md").read_text(encoding="utf-8")

def section(name):
    m = re.search(rf"^## {name}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""

body = section("正文")
body = "\n".join(l[1:].strip() if l.startswith(">") else l.strip()
                 for l in body.splitlines())
body = re.sub(r"\n{2,}", "\n", body).strip()
print(f"body: {len(body)} / 1000 chars")
print("--- body ---")
print(body)
for line in section("标题候选").splitlines():
    line = re.sub(r"^\d+\.\s*", "", line).strip()
    if line:
        print(f"title: {len(line):>2} chars  {line}")
PY
```

Then report two mechanical facts only:

- If the body is over 1000: name the longest paragraph and ask the author what to cut. Do not
  cut it yourself.
- Name any sentence that does not support the claim, quote it, and ask whether to cut it.
  Do not rewrite it.

## 5. Report and stop

Tell the author:

- The folder path and the character counts.
- Publishing is manual: copy title/body/tags into 小红书, then paste back the URL and the 48-hour
  numbers (浏览 / 点赞 / 收藏 / 评论) so the ledger can be filled.
- The note stays on `main`; no PR, and no commit unless asked.
