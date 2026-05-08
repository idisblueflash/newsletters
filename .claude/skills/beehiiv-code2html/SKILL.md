---
name: beehiiv-code2html
description: 将 Markdown 文件中的代码块（backtick fences）转换为带内联样式的 HTML，输出到 blocks.md，用于粘贴进 Beehiiv 的 HTML Block。当用户说"转成 HTML 代码块"、"beehiiv 代码块"、"code2html"、"转 beehiiv 代码块"、"帮我转代码块"时，立即激活此技能。
---

# beehiiv Code Block to HTML Converter

将 Markdown 文件中的所有 backtick fence 代码块提取出来，转换为可直接粘贴进 Beehiiv HTML Block 的内联样式 HTML。不修改原始 MD 文件。

---

## 背景

Beehiiv 编辑器不解析 Markdown backtick fences，粘贴后只显示纯文本。
解决方案：将代码块转为带内联样式的 `<pre><code>` HTML，插入 HTML Block 元素。

---

## 样式规范

- 外层 `<pre>` 必须携带所有样式（内联，不用 class）
- 内层 `<code>` 继承字体，不加额外背景
- 代码内容中的 `<`、`>`、`&` 必须转义为 HTML 实体
- 语言标识（` ```python ` 等）只用于标注，不输出到 HTML

HTML 模板：
```html
<pre style="background:#000;padding:16px;border-radius:6px;font-family:'Noto Sans Mono',monospace;font-size:14px;line-height:1.6;color:#fff;overflow-x:auto;white-space:pre;"><code style="font-family:inherit;background:none;padding:0;">转义后的代码内容</code></pre>
```

---

## 工作流程

### Step 1：确定目标文件
- 用户指定了文件路径则用指定路径
- 未指定则默认读取当前目录的 `draft.md`
- 用 Read tool 读取文件全文

### Step 2：提取所有代码块
扫描文件，找出所有 ` ``` ` 开头、` ``` ` 结尾的代码块：
- 记录每个代码块的顺序编号（Block 1、Block 2……）
- 记录语言标识（如有）
- 提取代码块正文（不含首尾的 ` ``` ` 行）

### Step 3：转义 HTML 特殊字符
对每个代码块的正文执行：
- `&` → `&amp;`
- `<` → `&lt;`
- `>` → `&gt;`
- `"` → `&quot;`

### Step 4：生成 HTML 片段
按模板生成每个代码块的 HTML。

### Step 5：写入 blocks.md
在原始 MD 文件同目录下创建（或覆盖）`blocks.md`，格式如下：

```markdown
# Beehiiv Code Blocks

_来源：draft.md_

---

## Block 1（python）

在 Beehiiv 编辑器中输入 `/html` 插入 HTML Block，粘贴以下内容：

​```html
<pre style="..."><code style="...">代码内容</code></pre>
​```

---

## Block 2

​```html
<pre style="..."><code style="...">代码内容</code></pre>
​```
```

### Step 6：输出确认
告知用户：
- 找到了几个代码块
- blocks.md 已写入哪个路径
- 使用方法：在 Beehiiv 编辑器里 `/html` → HTML Block → 粘贴对应块的 HTML
