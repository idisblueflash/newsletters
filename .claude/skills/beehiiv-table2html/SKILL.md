---
name: beehiiv-table2html
description: 将 Markdown 表格转换为带内联样式的 HTML 表格，用于解决 Beehiiv 编辑器中 MD 表格文字不可见（黑底黑字）的问题。当用户说"转成 HTML 表格"、"beehiiv 表格"、"帮我转 beehiiv 表格"、"table2html"、"MD 表格转 HTML"时，立即激活此技能。只要用户提交了一段 Markdown 表格并希望在 Beehiiv 中正常显示，就应该使用此技能。
---

# beehiiv Table to HTML Converter

将 Markdown 表格转换为 Beehiiv 可用的内联样式 HTML 表格。

---

## 背景

Beehiiv 编辑器对 Markdown 表格存在渲染 bug：单元格会继承黑色背景，导致文字不可见。
解决方案是改用 HTML Block 并在每个单元格上写内联样式，强制覆盖 Beehiiv 的默认样式。

---

## 样式规范

- 每个 `<th>` 和 `<td>` 必须带内联样式，不能依赖 `<style>` 标签（邮件客户端会剥掉）
- 颜色强制指定：`color:#000`、`background-color:#fff`（或交替行用 `#fafafa`）
- 表头行背景：`#f0f0f0`
- 边框：`1px solid #ccc`
- 内边距：`padding:8px 12px`
- 表格宽度：`width:100%`，`border-collapse:collapse`，`font-family:inherit`
- Markdown 中的 `**粗体**` 转换为 `<strong>` 标签

---

## 工作流程

### Step 1：解析 Markdown 表格
读取用户提供的 MD 表格，识别：
- 表头行（第一行）
- 分隔行（`---` 行，忽略）
- 数据行（其余行）
- 每列的单元格内容，处理 `**粗体**` 等内联格式

### Step 2：生成 HTML

按以下模板输出，数据行交替使用 `#fff` 和 `#fafafa` 背景：

```html
<table style="width:100%; border-collapse:collapse; font-family:inherit;">
  <thead>
    <tr style="background-color:#f0f0f0;">
      <th style="border:1px solid #ccc; padding:8px 12px; text-align:left; color:#000;">列标题</th>
      <!-- 更多列 -->
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#fff;">
      <td style="border:1px solid #ccc; padding:8px 12px; color:#000;">内容</td>
      <!-- 更多列 -->
    </tr>
    <tr style="background-color:#fafafa;">
      <td style="border:1px solid #ccc; padding:8px 12px; color:#000;">内容</td>
      <!-- 更多列 -->
    </tr>
    <!-- 更多行 -->
  </tbody>
</table>
```

### Step 3：输出

直接输出 HTML 代码块，附一句使用说明：在 Beehiiv 编辑器中输入 `/html` 插入 HTML Block，粘贴即可。
