# 文章修改 SOP

当用户说「开始改文章」、「按流程改」、「走流程」，或类似表达时，按以下顺序逐步执行，每个 subagent 完成并合并 PR 后，再询问用户是否继续下一步。

**目标文件**：用户指定的文件，未指定时默认为当前文章目录的 `draft.md`。

| 步骤 | Subagent / 工具 | 任务 | 原因 |
|------|----------|------|------|
| 1 | Stone Reverge | 用七步框架检查大结构 | 结构改动影响最大，优先处理，避免细节白做 |
| 2 | Deva | 找出可以删除的冗余内容 | 删减在细节完善之前，否则改完再删是浪费 |
| 3 | Owen | 口语化审查，替换书面语 | 删减定稿后再做转写，改动范围确定 |
| 4 | Percy | 感知传递改写 | 表达层面的深度优化，在口语化之后进行 |
| 5 | de-ai-flavor skill | 扫描中文 AI 味（对仗、名词化、抽象金句、缺锚点等五类） | 最后打磨，挑出残留的 AI 表面特征 |

**执行规则**：
- 开始前先用 `git log <目标文件>` 查看 commit 历史，根据前缀判断哪些步骤已完成（`[Stone]`=步骤1，大量「删除」类 commit=步骤2，`[Owen]`=步骤3，`[Percy]`=步骤4，`[de-AI]`=步骤5），直接从第一个未完成的步骤开始
- 每步完成、PR 合并后，提示「步骤 N 完成，是否继续步骤 N+1？」
- 用户可随时说「跳过」进入下一步，或「停」暂停流程
- 所有 subagent 的调用规范见下方「Subagent 调用规范」

---

# 写作风格

- 避免使用破折号（——），用其他标点或改写句子结构代替

# 提交规范

- 每处修改独立 commit，不合并多处改动到一个 commit
- commit message 须写清楚「改了什么 + 为什么改」，不能写泛泛的「优化表达」

# Subagent 调用规范

- **Stone Reverge**：Agent tool 的 `subagent_type` 必须设为 `general-purpose`，不能用 `stone-reverge`。原因：Agent tool 只识别内置 agent 类型，自定义名称会报错。Stone 只负责分析和提建议，不写文件、不 commit、不开 PR。用户确认后，由主 agent 执行 Edit + 调用 `commit-edit` skill 提交。
- **Percy**：只负责分析，不写文件、不 commit、不开 PR。一次读完目标文件，在上下文里记住内容和行号，逐条提建议。用户确认后，由主 agent 执行 Edit + 调用 `commit-edit` skill 提交，Percy 立刻继续分析下一处。Percy 对应 `perception-analysis` 技能（感知传递），不是 `show-dont-tell-review`。
- **de-ai-flavor**：主 agent 直接调用 `de-ai-flavor` skill 扫描目标文件，挑出最重的 3 处 AI 味，用户标注后主 agent 执行 Edit + `commit-edit`。commit 前缀用 `[de-AI]`。
- **commit-edit**：轻量 Skill（`.claude/skills/commit-edit/`），负责 git add + commit。主 agent 完成 Edit 后用 Skill tool 调用，commit message 须写清楚修改原因。

# Percy 工作模式

**Normal mode（默认）**：Percy 逐条提建议，等用户确认后主 agent 执行 Edit + 调用 `commit-edit` skill 提交，Percy 继续下一条。

**Fast mode**：用户说「fast mode」或「快速模式」时启用。每条建议的执行顺序严格如下：

1. Percy 内部确定问题和改写，**不向用户输出任何内容**——用户通过 git diff / PR review 看结果，屏幕上显示是浪费
2. 主 agent 直接执行 Edit（fast mode 的核心：建议即执行，不需要二次确认）
3. 调用 `commit-edit` skill 提交
4. **主 agent 用 Read tool 重新读取刚改动的行及前后各 5 行**（必须，不可跳过；不需要读全文）
5. Percy 基于重读后的文件内容提下一条建议

每条独立 commit（方便事后 `git revert <hash>` 精确回滚）。全部完成后开 PR 供用户 review。

步骤 4 是 fast mode 与 normal mode 的等价保证：normal mode 下人工确认产生的消息边界让主 agent 自然获得最新文件状态；fast mode 下没有消息边界，必须显式 re-read 来替代这个上下文刷新。跳过 re-read 会导致 Percy 基于过时上下文累积建议，出现「先建后删同一段」的反复改动。

# 逐段审查行为

- 无问题的段落直接跳过，不要输出"可以跳过"等提示
- 有多处需改进时，一次只提一段建议，等用户确认后再进入下一段
