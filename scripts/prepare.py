#!/usr/bin/env python3
"""Apply the small, documented adaptations needed to run the snapshot locally."""
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
RAW = ROOT / 'reference/upstream'
changes = []


def html_adapt(s):
    def clean_script(match):
        script = match[0]
        if any(marker in script for marker in ('__rum', 'visitor_registered', 'zz.bdstatic.com', 'api.indexnow.org')):
            return '<!-- Local snapshot: upstream telemetry / search-engine submission removed. -->'
        return script
    return re.sub(r'<script\b[^>]*>[\s\S]*?</script>', clean_script, s, flags=re.I)


def english2_html(s):
    s = re.sub(r'<li>\s*<a href="/english/paper/\d+_english1/">[\s\S]*?</li>', '', s)
    s = re.sub(r'<a class="snav-link" href="/biochem/">.*?</a>', '', s)
    s = s.replace('考研学习站', '考研英语二')
    s = s.replace('考研英语真题', '考研英语二真题')
    s = s.replace('考研英语单词本', '考研英语二单词本')
    s = s.replace('英语一/二', '英语二').replace('考研英语一、英语二', '考研英语二')
    s = s.replace('英一英二', '英语二')
    return s


# The word-detail pages use the original template, with sources and examples scoped
# to English II. No new translations are generated.
example_pairs = []
for paper in sorted((RAW / 'english/paper').glob('*_english2/index.html')):
    content = paper.read_text()
    for en, zh in re.findall(r'<p class="s">(.*?)</p>\s*<p class="zh">(.*?)</p>', content, re.S):
        en_text = html.unescape(re.sub('<[^>]*>', '', en))
        example_pairs.append((en_text, en, zh))
word_stats = {}
word_sources = {}
for source in (RAW / 'english/words').glob('*/index.html'):
    s = source.read_text()
    block = re.search(r'<h2>真题出处</h2>\s*<ul>(.*?)</ul>', s, re.S)
    if not block:
        continue
    rows = re.findall(r'<li>.*?</li>', block[1], re.S)
    rows = [r for r in rows if '_english2/' in r]
    if rows:
        total = sum(int(re.search(r'出现 (\d+) 次', row)[1]) for row in rows)
        word_stats[source.parent.name] = (total, len(rows))
        word_sources[source.parent.name] = rows


for source in RAW.rglob('*.html'):
    rel = source.relative_to(RAW)
    if not str(rel).startswith('english/') or '_english1' in str(rel):
        continue
    target = PUBLIC / rel
    original = source.read_text()
    modified = english2_html(html_adapt(original))
    if rel.parts[:2] == ('english', 'words') and len(rel.parts) == 4:
        word = source.parent.name
        if word not in word_stats:
            if target.exists():
                target.unlink()
            continue
        total, coverage = word_stats[word]
        rows = word_sources[word]
        modified = re.sub(r'<h2>真题出处</h2>\s*<ul>.*?</ul>', '<h2>真题出处</h2>\n<ul>' + '\n'.join(rows) + '</ul>', modified, flags=re.S)
        modified = re.sub(r'历年真题累计出现 \d+ 次 · 覆盖 \d+ 套真题', f'英语二真题累计出现 {total} 次 · 覆盖 {coverage} 套真题', modified)
        modified = re.sub(r'出现在 \d+ 套考研英语真题中', f'出现在 {coverage} 套考研英语二真题中', modified)
        examples = []
        matcher = re.compile(r'(?<![A-Za-z])' + re.escape(html.unescape(word)) + r'(?![A-Za-z])', re.I)
        seen = set()
        for text, en, zh in example_pairs:
            if matcher.search(text) and text not in seen:
                examples.append('<div class="card"><p class="s">' + en + '</p><p class="zh">' + zh + '</p></div>')
                seen.add(text)
                if len(examples) == 5:
                    break
        modified = re.sub(r'(<h2>真题例句（含翻译）</h2>)[\s\S]*?(<nav class="nav">)', lambda m: m[1] + '\n' + '\n'.join(examples) + '\n' + m[2], modified)
    if rel.parts[:2] == ('english', 'paper'):
        year = int(rel.parts[2][:4])
        nav = []
        if year > 2010:
            nav.append(f'<a href="/english/paper/{year-1}_english2/">← {year-1} 英语（二）</a>')
        if year < 2026:
            nav.append(f'<a href="/english/paper/{year+1}_english2/">{year+1} 英语（二） →</a>')
        modified = re.sub(r'<nav class="nav" aria-label="前后卷">.*?</nav>', '<nav class="nav" aria-label="前后卷">' + ''.join(nav) + '</nav>', modified)
    # Keep the supplied visual design; only localize dependencies and hidden metadata.
    modified = modified.replace('https://cdn.bootcdn.net/ajax/libs/gsap/3.12.7/gsap.min.js', '/vendor/gsap.min.js')
    modified = modified.replace('https://cdn.bootcdn.net/ajax/libs/gsap/3.12.7/ScrollTrigger.min.js', '/vendor/ScrollTrigger.min.js')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(modified)
    if modified != original:
        changes.append(str(rel))

app_path = PUBLIC / 'english/js/app.js'
original = (RAW / 'english/js/app.js').read_text()
modified = original.replace("showToast('反馈已提交，感谢你的建议！', 'success');", "showToast('反馈已保存在本机', 'success');")
modified = re.sub(r"^\s*'data/exam_\d+_english1\.json',?\n", '', modified, flags=re.M)
modified = modified.replace("state.exams = raw ? JSON.parse(raw) : [];", "state.exams = (raw ? JSON.parse(raw) : []).filter(e => /_english2$/.test(e.exam_id || '')); // Local scope: English II only")
app_path.write_text(modified)
correction = PUBLIC / 'english/js/correction.js'
correction.write_text((RAW / 'english/js/correction.js').read_text().replace("'✓ 已提交，感谢反馈！'", "'✓ 纠错已保存在本机'"))

# app.js checks this hash to guard against stale copies, so keep the local tag coherent.
versions = json.loads((RAW / 'english/data/version.json').read_text())
versions['app'] = hashlib.md5(app_path.read_bytes()).hexdigest()[:10]
versions['exams'] += '-english2'
(PUBLIC / 'english/data/version.json').write_text(json.dumps(versions, ensure_ascii=False, indent=2))
index = PUBLIC / 'english/index.html'
index.write_text(re.sub(r'js/app\.js\?v=[0-9a-zA-Z._-]+', 'js/app.js?v=' + versions['app'], index.read_text()))
index.write_text(index.read_text().replace('（5408 词条页）', f'（{len(word_stats)} 词条页）'))

# Rebuild the existing TOP 500 table from English-II-only word counts.
word_index = PUBLIC / 'english/words/index.html'
word_html = word_index.read_text()
dictionary = json.loads((PUBLIC / 'english/data/dict.json').read_text())['dict']
table_rows = []
for word, (total, coverage) in sorted(word_stats.items(), key=lambda item: (-item[1][0], item[0]))[:500]:
    entry = dictionary.get(html.unescape(word), {})
    ph = html.escape(entry.get('ph', ''))
    senses = '；'.join(s.get('p', '') + ' ' + s.get('t', '') for s in entry.get('s', []))[:140]
    tags = ''.join('<span class="tag">' + label + '</span>' for key, label in [('ky', '考研'), ('cet4', '四级'), ('cet6', '六级')] if key in entry.get('tag', []))
    table_rows.append(f'<tr><td><a href="/english/words/{word}/">{html.escape(html.unescape(word))}</a>{tags}</td><td>{ph}</td><td>{html.escape(senses)}</td><td>{total}</td><td>{coverage}</td></tr>')
word_html = re.sub(r'<table>.*?</table>', '<table><tr><th>单词</th><th>音标</th><th>释义</th><th>累计词频</th><th>覆盖卷数</th></tr>' + ''.join(table_rows) + '</table>', word_html, count=1, flags=re.S)
word_html = re.sub(r'覆盖 34 套真题.*?</p>', f'覆盖 17 套真题（2010-2026 英语二），按英语二累计词频排序，提供 {len(word_stats)} 个词条详情页。</p>', word_html, count=1)
word_index.write_text(word_html)

materials = json.loads((RAW / 'english-materials/manifest.json').read_text())
materials = [f for f in materials if '英二' in f['name']]
(PUBLIC / 'english-materials/manifest.json').write_text(json.dumps(materials, ensure_ascii=False, indent=2))

# Remove only generated, out-of-scope files inside this new local project.
for tree in [PUBLIC, RAW]:
    for f in list(tree.rglob('*')):
        if f.is_file() and ('_english1' in str(f.relative_to(tree)) or '英一' in f.name):
            f.unlink()
for directory in ['about', 'vendor', 'img']:
    if (PUBLIC / directory).exists():
        shutil.rmtree(PUBLIC / directory)
for name in ['index.html', 'fonts.css', 'updates.json']:
    if (PUBLIC / name).exists():
        (PUBLIC / name).unlink()

(ROOT / 'reference/local-scope.json').write_text(json.dumps({'subject': '英语（二）', 'years': [2010, 2026], 'papers': 17, 'materials': len(materials), 'word_pages': len(word_stats)}, ensure_ascii=False, indent=2))

launcher = ROOT / '启动英语二.command'
launcher.write_text('#!/bin/zsh\ncd "${0:A:h}"\nexec ' + "'" + sys.executable.replace("'", "'\\''") + "'" + ' server.py --open\n')
launcher.chmod(0o755)
print(json.dumps({'adapted_html': len(changes), 'app_version': versions['app'], 'launcher': str(launcher)}, ensure_ascii=False))
