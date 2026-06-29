---
name: beehiiv-draft2html
description: 将整篇文章 draft.md 转换为可直接粘贴进 Beehiiv 编辑器的 HTML。处理标题、段落、列表、引用、代码块、表格、脚注，剥离内部脚手架（[CITE:] 标记、Flow sidecar、frontmatter）。当用户说"转成 HTML"、"转 beehiiv"、"draft2html"、"把文章转成 HTML 粘贴到 Beehiiv"、"整篇转 HTML"时激活。只处理单个表格请用 beehiiv-table2html。
---

# beehiiv Draft to HTML Converter

把一篇完整的 Markdown 文章转换成 Beehiiv 编辑器能正确渲染的 HTML，用户复制粘贴即可发布。

---

## 适用范围

- **本技能**：整篇文章（draft.md 或指定 MD 文件）→ 完整 HTML 文档。
- **beehiiv-table2html**：只转单个/几个 Markdown 表格时用那个。
- 目标文件由用户指定，未指定时默认当前文章目录的 `draft.md`。

---

## 输出位置

在目标文件同目录写入 `beehiiv.html`（与 draft.md 并列）。不要打印整段 HTML 到对话里——文件写好后给一句使用说明即可。

---

## 转换规则

### 元素映射

| Markdown | HTML |
|---|---|
| `## 标题` | `<h2>` （H1 文章标题**省略**，Beehiiv 单独设标题） |
| 段落 | `<p>` |
| `**粗体**` / `*斜体*` | `<strong>` / `<em>` |
| `- 项` / `1. 项` | `<ul><li>` / `<ol><li>` |
| `> 引用` | `<blockquote>`，内部块（段落/列表/表格）正常嵌套 |
| ` ```代码``` ` | `<pre><code>` （原样保留，不转义内部的中文标点） |
| 表格 | 见下方「表格」 |
| `[^1]` 脚注 | 正文用 `<sup><a href="#fn1">[1]</a></sup>`，定义移到文末 `<p id="fn1"><small>…</small></p>` |
| `[文字](url)` | `<a href="url">文字</a> |
| `---` 分隔线 | `<hr>` |
| 软换行（引用内多行） | `<br>` |

### 表格（关键）

Beehiiv 把裸 MD 表格渲染成黑底黑字。必须转成每个单元格都带内联样式的 HTML，强制指定颜色：

```html
<table style="border-collapse:collapse;width:100%;margin:0.5em 0;color:#111;background-color:#fff;">
<thead>
<tr>
<th style="border:1px solid #ccc;padding:8px;text-align:left;color:#111;background-color:#f2f2f2;">列标题</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border:1px solid #ccc;padding:8px;color:#111;background-color:#fff;">内容</td>
</tr>
</tbody>
</table>
```

- **`background-color` 必须写在每个 `<th>`/`<td>` 上，不能只写在 `<table>` 或 `<tr>` 上**。Beehiiv 把暗色背景强加到单元格本身，table/tr 级的背景盖不住 → 还是黑底黑字。表头单元格用 `#f2f2f2`，数据行交替 `#fff`／`#fafafa`。
- 每个单元格同时带 `color:#111`。不能依赖 `<style>` 标签（粘贴时会被剥掉）。
- 单元格内的 `**粗体**` 仍转 `<strong>`。

**表格必须当作独立顶层块，并通过 Custom HTML Block 插入**——这是 Beehiiv 表格能正常显示的唯一可靠办法，原理（已查官方文档证实）：

- Beehiiv 在 sanitize 时**保留行内 `style=""`**，但**剥掉 `<style>` 标签、`<link>`、以及 CSS class**（class 不删但没样式表加载，等于无效）。所以所有样式必须写成行内。
- 但行内样式只在 **Custom HTML Block** 里生效。如果把表格**粘进富文本编辑器**，Beehiiv 会把 `<table>` 转成**原生表格块**，丢掉行内样式 → 套用主题色（深色）→ 黑底黑字/文字消失。散文/列表能正常粘是因为它们干净映射到原生块，表格不行。
- 嵌在 `<li>` 或 `<blockquote>` 里的 `<table>` 还会被直接**丢弃**（表格消失）。

因此转换时：把每个 `<table>` 提到**顶层独立块**（前面的 `<blockquote>`／`<ul>` 先收掉，表格后另起），每个单元格行内样式带 `color:#111 !important` + `background-color:#fff/#fafafa/#f2f2f2 !important`（`!important` 防 Beehiiv 注入的 CSS）。

**给用户的粘贴说明必须写清两步**：① 散文/列表正常粘进富文本编辑器；② 每个表格的位置改用 `/html` 插入 **Custom HTML Block**，只把那段 `<table>…</table>` 粘进去。不这么做表格必然黑底黑字。

代价：表格会脱离引用块缩进、和上面的 bullet 视觉分家。这是硬限制，可见性优先，不要为缩进把表格塞回 `<li>`／`<blockquote>`。

### 必须剥离的内部脚手架（不进 HTML）

- **frontmatter**（`---` 之间的 slug/title/status 等）。
- **重复的 H1 文章标题**（Beehiiv 单独设标题）。
- **`[CITE: ...]` 标记**——内部引用占位符，删除。
- **Flow sidecar / 其他指向 drafts 内部文件的元信息块**——不是给读者看的，删除。
- 真正的学术**脚注（`[^1]`）保留**，移到文末。

剥离前若不确定某块是不是内部脚手架，先问用户，不要擅自删读者可见内容。

---

## 工作流程

1. **Read** 目标文件全文。
2. 识别并列出要剥离的内部脚手架块，在回复里简短说明删了什么、为什么（让用户能否决）。
3. 按上面的规则逐段转换，**Write** 到同目录 `beehiiv.html`。
4. 给使用说明：复制 `beehiiv.html` 全文，粘贴进 Beehiiv 编辑器；Beehiiv 保留行内 `style=""` 属性但可能剥掉 `<style>` 标签，所以表格用的是行内样式，能存活。

---

## 注意

- 写作风格规范：避免破折号（——）——但这是**转换**任务，原文用了破折号就**原样保留**，不要替作者改写正文。
- 不改动正文措辞，只做格式转换 + 剥离脚手架。
