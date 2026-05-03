---
name: draft-edit-workflow
description: 文章协作修改 + PR 追踪工作流（Workflow 3.1）。减少交互次数，保留原子化提交。当用户说"创建 PR 方便我们修改"、"把修改提交到 PR"、"合并 PR"、或配合任何 review skill 需要 PR 追踪时激活。
---

# 文章协作修改 PR 工作流

此 skill 负责文章修改过程中所有的 Git / GitHub 操作。**修改内容由调用方的 review skill 决定**，此 skill 只负责"怎么用 PR 追踪修改"，不负责"改什么"。

---

# Workflow 3.1：AI 辅助编辑流程

## 设计目标

- 减少用户交互次数
- 保留原子化提交（每个 commit 带改动理由，用于提取 Anki 卡片）
- 不遗漏任何修改项
- 符合 AI 辅助开发最佳实践（先生成全部变更，再按逻辑单元拆分提交）

---

## 完整流程

### 阶段 1：Subagent 全文分析（不 commit）

Subagent 读完整篇 draft.md，输出编号清单。

**清单格式（每条包含）：**

```
编号 | 原文（含段落行号锚点）| 改后 | 改的理由
```

**额外规则：**
- 超过 20 条时，按段落分组显示
- 讨论项须附原文完整上下文引用（锁定锚点，供阶段 4 定位）

---

### 阶段 2：用户一次性标注

**规则：**
- 只需标注接受的编号
- 未标注的，默认进入讨论队列
- 格式：`a 1 3 5`（a = accept，空格分隔编号）

**示例：**

```
Subagent 列出 1-8 条
用户输入：a 1 3 5
→ 1、3、5 进入 commit 队列
→ 2、4、6、7、8 自动进入讨论队列
```

---

### 阶段 3：Subagent 原子化提交接受项

**步骤 1：批量写入**
- Subagent 将所有接受项一次性修改到文件
- 文件此时包含全部变更，但不 stage

**步骤 2：git add -p 逐条暂存**
- Subagent 按接受编号顺序，逐个 hunk 暂存
- 每次只 stage 对应那一条修改

**步骤 3：逐条 commit**
- `git commit -m "[编号] [阶段 1 写的改动理由]"`
- 重复步骤 2-3，直到接受项全部提交完

---

### 阶段 4：处理讨论项

- 逐条讨论，每条讨论完后即 commit（同样原子化）
- 因阶段 1 已锁定行号锚点，上下文完整，不会断裂

---

### 阶段 5：收尾

**步骤 1：同步 main 并创建分支**

```bash
git fetch origin
git checkout main
git merge --ff-only origin/main
git checkout -b {文章目录slug}-{review类型}
```

**步骤 2：push**

```bash
git push -u origin {branch-name}
```

**步骤 3：创建 PR**

```bash
gh pr create --title "{PR标题}" --body "$(cat <<'EOF'
## Summary

{本次 review 的目标和范围，1-3 条}

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**步骤 4：merge（仅在用户明确要求时执行）**

合并前先确认：
> 确认把 PR merge 进 main？分支一并删除吗？

```bash
gh pr merge {pr_number} --merge --delete-branch
```

---

## 设计决策说明

| 决策 | 理由 |
|------|------|
| PR 移到最后创建 | 避免开始时出现空 PR，PR 一出现即是完整 diff |
| 默认未标注 = 讨论 | 不存在静默丢失，所有项必须被处理 |
| git add -p 拆分提交 | 写入与提交解耦，出错可随时重来，符合 AI 辅助开发最佳实践 |
| Subagent 理由直接复用为 commit message | 分析输出与 git 记录合一，无额外编辑成本 |
| 讨论项锚点在阶段 1 锁定 | 阶段 3 commit 完成后上下文不丢失 |
| 超 20 条分组显示 | 防止长清单认知过载 |

---

## 与前版本对比

| | Workflow 2 | Workflow 3.1 |
|---|---|---|
| 确认节奏 | 每处等一次确认 | 一次过完全部再标注 |
| PR 时机 | 开始时建空 PR | 全部 commit 后建 PR |
| commit message | 需要另外写 | Subagent 的理由直接复用 |
| 讨论项 | 阻塞主流程 | 单独队列，不阻塞 |
| 文件写入方式 | 确认一处改一处 | 先全部写入，再用 git add -p 拆分 |
| 讨论项上下文 | 无锚点，容易断裂 | 阶段 1 锁定行号锚点 |

---

*基于 Thomas 贝叶斯分析（2026-05-03）设计，参见 `outputs/2026-05-03-workflow3-bayesian-analysis.md`*
