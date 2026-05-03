# 写作风格

- 避免使用破折号（——），用其他标点或改写句子结构代替

# Subagent 调用规范

- **Stone Reverge**：Agent tool 的 `subagent_type` 必须设为 `general-purpose`，不能用 `stone-reverge`。原因：Agent tool 只识别内置 agent 类型，自定义名称会报错。
- **Percy**：Percy 是 subagent，review 和 PR 操作由她独立完成，主 agent 不介入。用户说"Percy 看看"时，直接把任务完整交给 Percy，不要自己动手改文件或开 PR。Percy 对应 `perception-analysis` 技能（感知传递），不是 `show-dont-tell-review`。

# 逐段审查行为

- 无问题的段落直接跳过，不要输出"可以跳过"等提示
- 有多处需改进时，一次只提一段建议，等用户确认后再进入下一段
