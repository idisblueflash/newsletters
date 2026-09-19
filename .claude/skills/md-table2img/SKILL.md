---
name: md-table2img
description: 将 Markdown 表格渲染成 PNG 图片，保存到文章目录并替换原表格。用于 Beehiiv 等编辑器里 HTML 表格样式失效、或表格需要以图片形式呈现的场景。当用户说"表格转图片"、"table2img"、"md-table2img"、"生成表格图片"、"HTML 样式不管用，转图片"时激活。只处理表格渲染成图片，不处理 HTML table（那是 beehiiv-table2html 的职责）。
---

# md-table2img — Markdown 表格转图片

把 draft.md 里的 Markdown 表格渲染成带样式的 PNG 图片，替换原表格文本。

---

## 何时使用

- Beehiiv 或其他编辑器里表格的 HTML/内联样式方案不生效（例如 `beehiiv-table2html` 生成的样式被编辑器剥离）
- 用户明确要求把表格做成图片

如果只是需要 HTML table 代码块，用 `beehiiv-table2html`，不要用这个技能。

---

## 依赖

- 本机 Chrome：`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`（headless 截图）
- ImageMagick `magick`（裁边距、加白边）

用前用 `which magick` 和 `ls "/Applications/Google Chrome.app"` 确认都在，缺哪个提示用户安装（`brew install imagemagick`），不要静默跳过。

---

## 工作流程

### Step 1：定位表格

读取目标文件（默认 `draft.md`），找到要转换的 Markdown 表格（表头行 + `---` 分隔行 + 数据行）。

### Step 2：为每个表格生成 HTML

在 scratchpad 目录下为每个表格写一个独立的 `.html` 文件，用内联 `<style>` 渲染成简洁表格样式：

- 深色表头（`#2b2f38` 背景 + 白字）
- 斑马纹行（偶数行 `#f6f7f9`）
- 边框 `1px solid #d9d9d9`
- 字号 20px 左右，中文字体走 `-apple-system, "PingFang SC", "Helvetica Neue", Arial, sans-serif`
- 首列左对齐，其余列居中
- 如果表格里有明显的"最优值"（用户指出或上下文能推断），可以用一个 `.best` class 标绿加粗，不确定就不加

`<body>` 用 `display:inline-block` + `padding:32px`，方便后续截图后按内容裁剪。

### Step 3：截图

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --force-device-scale-factor=2 --hide-scrollbars \
  --screenshot="<name>_raw.png" --window-size=1400,700 "file://<path>/<name>.html"
```

`--window-size` 给够余量即可，多余空白靠下一步裁掉。`--force-device-scale-factor=2` 保证图片清晰（Retina 效果）。

### Step 4：裁边距

```bash
magick "<name>_raw.png" -trim +repage -bordercolor white -border 24 "<name>.png"
```

### Step 5：确认效果

用 Read 工具查看生成的 PNG，确认文字无遮挡、无溢出、对齐正常。有问题就回到 Step 2 调整样式重来。

### Step 6：存放位置

图片存到**目标文件同级目录**（跟 `draft.md` 平级），不要放 `assets/images/`——那个目录被 `.gitignore` 排除，是给 `cova` agent 同步 R2 用的独立流程，跟随文章一起提交的图片不走那条路。

文件命名要能看出对应哪个表格，例如 `<主题>-table.png`。

### Step 7：替换 Markdown 表格

用 Edit 把原表格文本替换成：

```markdown
![<表格内容简述>](<图片文件名>.png)
```

alt text 用中文简述表格内容（比如"机器人主题测试评分表"），不要写"表格"这种空泛描述。

### Step 8：提交

调用 `commit-edit` skill 提交图片文件 + draft.md 改动，commit message 说明"为什么用图片替代 Markdown 表格"（例如 HTML 样式在目标编辑器失效）。

---

## 注意事项

- 每个表格单独一张图，不要把多个表格拼进一张图
- 不要在图片里加水印、logo 等额外元素，除非用户要求
- 生成过程产生的中间文件（`*_raw.png`、`.html`）留在 scratchpad 目录，不要拷到项目里
