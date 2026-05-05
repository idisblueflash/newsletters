---
name: draft-edit-workflow
version: "4.0.0"
description: 文章协作修改 + PR 追踪工作流（Workflow 4.0）。减少交互次数，保留原子化提交。当用户说"创建 PR 方便我们修改"、"把修改提交到 PR"、"合并 PR"、或配合任何 review skill 需要 PR 追踪时激活。
---

# 文章协作修改 PR 工作流

此 skill 负责文章修改过程中所有的 Git / GitHub 操作。**修改内容由调用方的 review skill 决定**，此 skill 只负责"怎么用 PR 追踪修改"，不负责"改什么"。

---

# Workflow 4.0：AI 辅助编辑流程

## 设计目标

- 减少用户交互次数
- 保留原子化提交（每个 commit 带改动理由）
- 不遗漏任何修改项
- 流程简单，不依赖复杂脚本

---

## 完整流程

### 阶段 1：建分支

```bash
git fetch origin
git checkout main
git merge --ff-only origin/main
git checkout -b {文章目录slug}-{review类型}
```

### 阶段 2：全文分析（不 commit）

调用方的 review skill 通读目标文件，输出编号清单：

```
编号 | 原文（含行号锚点）| 改后 | 改的理由
```

超过 20 条时按段落分组显示。

---

### 阶段 3：用户一次性标注

- 只需标注接受的编号
- 未标注的默认进入讨论队列
- 格式：`a 1 3 5`（a = accept，空格分隔编号）

---

### 阶段 4：逐条修改 + commit

按接受编号顺序，每条依次执行：

1. Edit 文件，只改这一条
2. `git add {文件路径}`
3. `git commit -m "[编号] {阶段 2 写的改动理由}"`

重复直到接受项全部提交完。

---

### 阶段 5：处理讨论项

逐条讨论，每条确认后即按阶段 4 同样方式 edit + commit。

---

### 阶段 6：Push + 建 PR

```bash
git push -u origin {branch-name}
gh pr create --title "{PR标题}" --body "$(cat <<'EOF'
## Summary

{本次 review 的目标和范围，1-3 条}

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

### 阶段 7：合并（仅用户明确要求时执行）

合并前先确认：
> 确认把 PR merge 进 main？分支一并删除吗？

```bash
gh pr merge {pr_number} --merge --delete-branch
```

---

## 设计决策说明

| 决策 | 理由 |
|------|------|
| 分支在开始创建 | 所有 commit 直接落在分支上，不污染 main |
| 逐条 edit → commit | 天然原子化，不需要 git add -p |
| PR 在最后建 | PR 一出现即是完整 diff，不出现空 PR |
| 未标注 = 讨论 | 不存在静默丢失，所有项必须被处理 |
