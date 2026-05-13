---
name: commit-edit
description: 提交文章修改的轻量 git commit 工具。在主 agent 完成文件编辑后调用，负责 git add + commit，commit message 须清楚说明修改原因。适用场景：每次完成一处文章修改后立即提交。
---

# commit-edit — 文章修改提交工具

## 执行步骤

1. 用 Bash 运行：
   ```
   git -C <repo_root> add <file_path>
   git -C <repo_root> commit -m "<commit_message>"
   ```
2. 输出一行确认：`✓ committed: <commit_message>`

## Commit message 写法规则

- 格式：`[标签] 修改类型: 说明改了什么以及为什么`
- 标签沿用当前文件的 commit 历史风格（参考 `git log --oneline <file_path>` 最近几条）
- **必须写清楚修改原因**，不能只写「修改表达」「优化文字」这种泛泛的说法
  - ✅ `[Vivian] Show Don't Tell: 删除「那么证明这个规范起作用了」结论宣告句`
  - ✅ `[Percy] 感知传递: 三个症状从标签改为具体画面（结构/开头/语气）`
  - ❌ `优化表达`
  - ❌ `修改文章`
- 不要用破折号（——），改用其他标点或空格

## 规则

- 只做 add + commit，不分析内容，不创建分支，不开 PR
- repo root 通常是 `/Users/husongtao/Projects/newsletters`
