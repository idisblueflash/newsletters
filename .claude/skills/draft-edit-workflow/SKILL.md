---
name: draft-edit-workflow
description: 文章协作修改 + PR 追踪工作流。把"开 PR → 逐条修改确认 → commit（带修改理由）→ push → merge"整套流程固化。当用户说"创建 PR 方便我们修改"、"把修改提交到 PR"、"合并 PR"、或配合任何 review skill 需要 PR 追踪时激活。
---

# 文章协作修改 PR 工作流

此 skill 负责文章修改过程中所有的 Git / GitHub 操作。**修改内容由调用方的 review skill 决定**，此 skill 只负责"怎么用 PR 追踪修改"，不负责"改什么"。

---

## 阶段一：开 PR

在开始任何修改讨论之前执行。

### 1. 同步 main

```bash
git fetch origin
git checkout main
git merge --ff-only origin/main
```

### 2. 创建新分支

分支名格式：`{文章目录slug}-{review类型}`，例如 `ch02-perception-review`。

```bash
git checkout -b {branch-name}
```

### 3. Bootstrap commit + push

```bash
git commit --allow-empty -m "chore: open branch for {描述}"
git push -u origin {branch-name}
```

### 4. 创建 PR

```bash
gh pr create --title "{PR标题}" --body "$(cat <<'EOF'
## Summary

{本次 review 的目标和范围，1-3 条}

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

记录 PR URL，告知用户。

---

## 阶段二：逐条修改 + commit

每次用户确认一处修改后：

### 1. 修改文件

用 Edit 工具修改对应段落。

### 2. commit（带修改理由）

commit message 格式：
- **标题**：`review: {一句话描述改了什么}`
- **正文**：解释为什么这样改——原句的问题是什么，新句子解决了什么，具体到词或句子层面
- **署名**：`Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`

```bash
git add {文件路径}
git commit -m "$(cat <<'EOF'
review: {标题}

{修改理由，2-4行，具体说明原句问题和新句子的改进}

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

**不要在每次 commit 后立即 push**，等全文处理完再统一 push。

---

## 阶段三：push 到 PR

全文所有修改都确认完毕后，统一 push：

```bash
git push
```

告知用户：所有修改已推送到 PR。

---

## 阶段四：合并 PR

**仅在用户明确要求时执行。** 合并前先确认：

> 确认把 PR merge 进 main？分支一并删除吗？

用户确认后执行：

```bash
gh pr merge {pr_number} --merge --delete-branch
```

---

## 约束条件

- 不要在每次 commit 后立即 push，统一等全文处理完
- 合并前必须得到用户明确确认
- commit message 的修改理由必须具体到词或句子层面，不能只写"改善感知"这类空话
- 分支命名要能反映文章和 review 类型，方便日后回溯
