#!/usr/bin/env node
// Deterministic Markdown -> Beehiiv HTML converter.
// Mirrors the rules in beehiiv-draft2html/SKILL.md. No LLM judgment calls:
// scaffolding stripping is limited to frontmatter, the first H1, and [CITE:] markers.

const fs = require('fs');
const path = require('path');

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function inlineFormat(text) {
  // Footnote refs [^1] -> <sup><a href="#fn1">[1]</a></sup>
  text = text.replace(/\[\^(\w+)\]/g, '<sup><a href="#fn$1">[$1]</a></sup>');
  // Links [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  // Bare autolinks <https://...>
  text = text.replace(/<(https?:\/\/[^>\s]+)>/g, '<a href="$1">$1</a>');
  // Bold **text**
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  // Italic *text* (avoid already-consumed ** pairs)
  text = text.replace(/(^|[^*])\*(?!\*)([^*]+?)\*(?!\*)/g, '$1<em>$2</em>');
  // Inline code `code`
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  return text;
}

function stripCiteMarkers(text) {
  return text.replace(/\[CITE:[^\]]*\]/g, '').trim();
}

function convert(mdPath) {
  let raw = fs.readFileSync(mdPath, 'utf8');

  // Strip frontmatter (--- ... ---) at top of file.
  raw = raw.replace(/^---\n[\s\S]*?\n---\n/, '');

  const lines = raw.split('\n');
  const out = [];
  const footnotes = []; // {id, html}
  let i = 0;
  let skippedH1 = false;

  while (i < lines.length) {
    let line = lines[i];

    if (line.trim() === '') { i++; continue; }

    // Drop the first top-level H1 (Beehiiv sets its own title).
    if (!skippedH1 && /^#\s+/.test(line)) {
      skippedH1 = true;
      i++;
      continue;
    }

    // Headings ## -> h2, ### -> h3 etc (min level 2)
    const headingMatch = line.match(/^(#{2,6})\s+(.*)$/);
    if (headingMatch) {
      const level = headingMatch[1].length;
      out.push(`<h${level}>${inlineFormat(stripCiteMarkers(headingMatch[2]))}</h${level}>`);
      i++;
      continue;
    }

    // Horizontal rule
    if (/^---+$/.test(line.trim())) {
      out.push('<hr>');
      i++;
      continue;
    }

    // Footnote definition: [^1]: text
    const fnDefMatch = line.match(/^\[\^(\w+)\]:\s*(.*)$/);
    if (fnDefMatch) {
      footnotes.push({ id: fnDefMatch[1], html: inlineFormat(fnDefMatch[2]) });
      i++;
      continue;
    }

    // Blockquote block
    if (/^>\s?/.test(line)) {
      const quoteLines = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        quoteLines.push(lines[i].replace(/^>\s?/, ''));
        i++;
      }
      out.push(`<blockquote><p>${quoteLines.map(l => inlineFormat(stripCiteMarkers(l))).join('<br>')}</p></blockquote>`);
      continue;
    }

    // Unordered list
    if (/^[-*]\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^[-*]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^[-*]\s+/, ''));
        i++;
      }
      out.push(`<ul>\n${items.map(it => `<li>${inlineFormat(stripCiteMarkers(it))}</li>`).join('\n')}\n</ul>`);
      continue;
    }

    // Ordered list
    if (/^\d+\.\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\d+\.\s+/, ''));
        i++;
      }
      out.push(`<ol>\n${items.map(it => `<li>${inlineFormat(stripCiteMarkers(it))}</li>`).join('\n')}\n</ol>`);
      continue;
    }

    // Code block
    if (/^```/.test(line)) {
      const codeLines = [];
      i++;
      while (i < lines.length && !/^```/.test(lines[i])) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // skip closing fence
      out.push(`<pre><code>${escapeHtml(codeLines.join('\n'))}</code></pre>`);
      continue;
    }

    // Table (GFM pipe table)
    if (/^\|/.test(line.trim()) && i + 1 < lines.length && /^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$/.test(lines[i + 1].trim())) {
      const headerCells = line.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      i += 2; // skip header + separator
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) {
        rows.push(lines[i].trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
        i++;
      }
      out.push(renderTable(headerCells, rows));
      continue;
    }

    // Paragraph (collect consecutive non-blank plain lines)
    const paraLines = [line];
    i++;
    while (
      i < lines.length &&
      lines[i].trim() !== '' &&
      !/^(#{1,6})\s+/.test(lines[i]) &&
      !/^>\s?/.test(lines[i]) &&
      !/^[-*]\s+/.test(lines[i]) &&
      !/^\d+\.\s+/.test(lines[i]) &&
      !/^```/.test(lines[i]) &&
      !/^---+$/.test(lines[i].trim()) &&
      !/^\[\^(\w+)\]:/.test(lines[i]) &&
      !/^\|/.test(lines[i].trim())
    ) {
      paraLines.push(lines[i]);
      i++;
    }
    const paraText = stripCiteMarkers(paraLines.join(' '));
    if (paraText) out.push(`<p>${inlineFormat(paraText)}</p>`);
  }

  // Footnote block at the end.
  for (const fn of footnotes) {
    out.push(`<p id="fn${fn.id}"><small>[${fn.id}] ${fn.html}</small></p>`);
  }

  return out.join('\n\n') + '\n';
}

function renderTable(headerCells, rows) {
  const thStyle = 'border:1px solid #ccc;padding:8px;text-align:left;color:#111 !important;background-color:#f2f2f2 !important;';
  const tdStyleEven = 'border:1px solid #ccc;padding:8px;color:#111 !important;background-color:#fff !important;';
  const tdStyleOdd = 'border:1px solid #ccc;padding:8px;color:#111 !important;background-color:#fafafa !important;';

  const thead = `<thead>\n<tr>\n${headerCells.map(c => `<th style="${thStyle}">${inlineFormat(c)}</th>`).join('\n')}\n</tr>\n</thead>`;
  const tbody = `<tbody>\n${rows.map((row, idx) => {
    const style = idx % 2 === 0 ? tdStyleEven : tdStyleOdd;
    return `<tr>\n${row.map(c => `<td style="${style}">${inlineFormat(c)}</td>`).join('\n')}\n</tr>`;
  }).join('\n')}\n</tbody>`;

  return `<table style="border-collapse:collapse;width:100%;margin:0.5em 0;color:#111 !important;background-color:#fff !important;">\n${thead}\n${tbody}\n</table>`;
}

function main() {
  const mdPath = process.argv[2];
  if (!mdPath) {
    console.error('Usage: draft2html.js <path/to/draft.md>');
    process.exit(1);
  }
  const absPath = path.resolve(mdPath);
  if (!fs.existsSync(absPath)) {
    console.error(`File not found: ${absPath}`);
    process.exit(1);
  }
  const html = convert(absPath);
  const outPath = path.join(path.dirname(absPath), 'beehiiv.html');
  fs.writeFileSync(outPath, html, 'utf8');
  console.log(`Wrote ${outPath}`);
}

main();
