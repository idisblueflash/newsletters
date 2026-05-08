# Beehiiv Code Blocks

_来源：articles/dev-log-ch01-dairy-or-log/draft.md_

在 Beehiiv 编辑器中输入 `/html` 插入 HTML Block，粘贴对应块的 HTML 内容。

---

## Block 1（系统日志示例，第 8–17 行）

```html
<pre style="background:#000;padding:16px;border-radius:6px;font-family:'Noto Sans Mono',monospace;font-size:14px;line-height:1.6;color:#fff;overflow-x:auto;white-space:pre;"><code style="font-family:inherit;background:none;padding:0;">  [2026-05-07 14:32]  INFO   App started on http://localhost:3000
  [2026-05-07 14:33]  INFO   User clicked &quot;Add Task&quot; — input: &quot;Buy groceries&quot;
  [2026-05-07 14:33]  INFO   Task saved to list. Total tasks: 1
  [2026-05-07 14:35]  INFO   User clicked &quot;Add Task&quot; — input: &quot;&quot; (empty)
  [2026-05-07 14:35]  WARN   Empty task rejected. Nothing saved.
  [2026-05-07 14:36]  INFO   User marked task #1 as done
  [2026-05-07 14:38]  ERROR  Failed to delete task #1 — task ID not found
  [2026-05-07 14:38]  INFO   App closed</code></pre>
```

---

## Block 2（Vibe Coding 日志模板示例，第 19–36 行）

```html
<pre style="background:#000;padding:16px;border-radius:6px;font-family:'Noto Sans Mono',monospace;font-size:14px;line-height:1.6;color:#fff;overflow-x:auto;white-space:pre;"><code style="font-family:inherit;background:none;padding:0;"># 开发日志 — 2026-05-07

## 今天做了什么
用 Claude 做了一个番茄钟网页。描述了需求，AI 生成了初版，有开始和重置按钮，计时器正常运行。

## 出了什么问题
倒计时结束没有任何提示。加了弹窗之后，弹窗又挡住了重置按钮，体验很差。

## 怎么修的
让 Claude 把弹窗换成页面顶部的提示条，3 秒后自动消失。提示词："把弹窗换成页面顶部的提示条，3 秒后自动消失。"

## 学到了什么
提示词越具体，AI 给的结果越准。"加个提示"太模糊，"顶部提示条 + 3 秒消失"一次到位。

## 明天做什么
  - 加一个会话计数，记录今天完成了几个番茄
  - 试试让 Claude 帮我把样式改成深色模式</code></pre>
```

---

## Block 3（社群日记模板，第 38–45 行）

```html
<pre style="background:#000;padding:16px;border-radius:6px;font-family:'Noto Sans Mono',monospace;font-size:14px;line-height:1.6;color:#fff;overflow-x:auto;white-space:pre;"><code style="font-family:inherit;background:none;padding:0;">**日期: 2025-09-06**

- 今天做了什么（可附 commit/链接）
- 卡在哪里 &amp; 你尝试了什么
- 解决/下一步计划（最小可验证动作）
- 参考/素材链接</code></pre>
```
