---
name: pangu-spacing
description: 在中英文之间自动加空格（pangu 排版规范）。当用户说"加空格"、"pangu"、"中英文空格"、"排版修正"、"/pangu-spacing"时，立即激活此技能。只要用户提交了一个 .md 文件路径并希望自动修正中英文之间的空格，就应该使用此技能。
---

# Pangu Spacing

在 Markdown 文件的中英文之间自动添加空格，符合 pangu 排版规范。

---

## 背景

中文与英文、数字混排时，中英文之间缺少空格会影响可读性。
本技能调用 `.claude/skills/pangu-spacing/pangu_spacing.py` 脚本，自动在中文字符与半角字母/数字之间插入空格，并保护 URL 不被误加空格。

---

## 工作流程

### Step 1：确定目标文件

- 用户指定文件路径时直接使用
- 未指定时，默认处理当前文章目录的 `draft.md`

### Step 2：运行脚本（in-place）

用 Bash tool 调用脚本，输出到同一文件（先写临时文件再覆盖）：

```bash
python3 .claude/skills/pangu-spacing/pangu_spacing.py <input> /tmp/pangu_tmp.md && mv /tmp/pangu_tmp.md <input>
```

### Step 3：报告结果

- 告知用户哪个文件已处理完毕
- 如需要，可追加 git commit（询问用户是否需要）
