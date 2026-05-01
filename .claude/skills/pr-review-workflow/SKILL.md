---
name: pr-review-workflow
description: 【内部工具，供 Stone Reverge / Percy Vivian 等 agent 调用，请勿手动触发】GitHub PR review 工作流。负责读取 PR 信息、管理 comment threads、发布 inline comment、处理人工回复、提交修改。review 标准由调用方的 agent 提供。
---

# PR Review 工作流

此 skill 负责所有与 GitHub PR 的交互逻辑。**review 标准由调用此 skill 的 agent 自行提供**，此 skill 只负责"怎么和 PR 交互"，不负责"review 什么"。

---

## 第一步：获取 PR 信息

```bash
gh pr view --json number,headRefName,baseRefName,url
gh repo view --json nameWithOwner
```

记录：`owner`、`repo`、`pr_number`、`branch`。

---

## 第二步：读取 draft.md，确保文件在 PR diff 中

```bash
gh pr view --json files --jq '.files[].path' | grep draft.md
```

读取文件**完整内容**，通读全文，理解整体结构和论述逻辑。**不得逐段孤立分析。**

**⚠️ 检查 draft.md 是否在 PR diff 中**：

```bash
gh api repos/{owner}/{repo}/pulls/{pr_number}/files --jq '.[].filename' | grep draft.md
```

如果 draft.md **不在** PR diff 中（即分支与 base 相比没有任何改动），必须先执行以下步骤，否则 inline comment 无法被回复：

1. 读取文件末尾，确认是否已有换行，然后做一个最小化的空白修正（如确保文件末尾有且只有一个换行符）
2. 提交这个 bootstrap commit：
   ```bash
   git add {draft.md路径}
   git commit -m "chore: bootstrap diff for inline comments"
   git push origin HEAD
   ```

这样 draft.md 就会出现在 PR diff 中，后续所有 inline comment 都可以正常回复。

---

## 第三步：获取 comment threads（排除已 resolved）

```bash
gh api graphql -f query='
{
  repository(owner: "OWNER", name: "REPO") {
    pullRequest(number: PR_NUMBER) {
      reviewThreads(first: 100) {
        nodes {
          isResolved
          comments(first: 20) {
            nodes {
              databaseId
              body
              path
              line
              author { login }
            }
          }
        }
      }
    }
  }
}'
```

- 只处理 `isResolved: false` 的 threads
- 已 resolved 的直接跳过，计入"跳过数"
- 本 agent 的 comment 结尾带有专属标记（由调用方 agent 定义），用于区分自己与 human 的发言

---

## 阶段 A：处理有人工回复的 threads

找出**最后一条回复来自 human**（不含本 agent 专属标记）的未 resolved thread，分析意图：

**意图判断**：
- **同意 / 接受**（如"好的"、"改吧"、"对"、"👍"、"可以"）→ 执行修改
- **疑问 / 反对 / 补充**（如"但是"、"为什么"、"不对"、"我觉得"）→ 继续讨论

**执行修改时**：
1. 读取 thread 完整讨论，理解修改共识
2. 定位 draft.md 对应段落，按共识修改
3. 提交并推送，记录 commit hash：
   ```bash
   git add {draft.md路径}
   git commit -m "review: 按讨论修改 [简短描述]"
   git push origin HEAD
   HASH=$(git rev-parse HEAD)
   ```
4. 回复 thread，附上可点击的 commit 链接（使用调用方 agent 定义的署名格式 + 专属标记）：
   `{署名} 已按讨论修改：{owner}/{repo}@{HASH}{专属标记}`

**继续讨论时**：
- 针对 human 疑问给出进一步解释或替代方案
- 回复（使用调用方 agent 定义的署名格式 + 专属标记）：
  `{署名} {回复内容}{专属标记}`

```bash
gh api repos/{owner}/{repo}/pulls/comments/{comment_id}/replies \
  -f body="..."
```

---

## 阶段 B：发起新 comment

**仅在阶段 A 没有待处理的人工回复 thread 时执行。**

1. 调用方 agent 对全文进行 review，产出若干条**原子建议**
2. 每条建议作为独立的 GitHub inline comment，定位到最相关的行：

```bash
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments \
  -f body="..." \
  -f commit_id="$(git rev-parse HEAD)" \
  -f path="{draft.md路径}" \
  -f line={行号} \
  -f side="RIGHT"
```

**原子建议原则**：每条 comment 只包含一个建议。如果一条建议包含多个独立改动点，必须拆开单独发。最终取最重要的 **3 条**。

---

## 结束汇报格式

```
{agent署名} 完成本轮工作：
- 跳过了 X 个 resolved thread
- 处理了 X 个 thread（Y 个修改 / Z 个继续讨论）
- 发了 X 个新 comment
```
