#!/usr/bin/env python3
"""Package the existing app for a GitHub Pages project subpath."""
import argparse
import hashlib
import json
import re
import shutil
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--base', required=True, help='Project prefix, for example /english2-precision-reader')
parser.add_argument('--origin', required=True, help='Account Pages origin')
parser.add_argument('--external-materials', action='store_true', help='Use original PDF download links instead of copying PDFs into the site')
args = parser.parse_args()
base = '/' + args.base.strip('/') if args.base.strip('/') else ''
origin = args.origin.rstrip('/')
out = ROOT / '_site'
if out.exists():
    shutil.rmtree(out)
shutil.copytree(ROOT / 'public', out)

def rebase(value):
    if value.startswith('/') and not value.startswith('//'):
        return base + value
    return value

for file in out.rglob('*.html'):
    s = file.read_text()
    s = re.sub(r'((?:href|src|data-src)=["\'])(/[^"\']*)(["\'])', lambda m:m[1]+rebase(m[2])+m[3], s)
    s = s.replace('https://study.aseeker.bio/english/', origin + base + '/english/')
    # Keep source attribution visible without suggesting this is the original site.
    s = re.sub(r'<a[^>]*href="https://beian\.miit\.gov\.cn/"[^>]*>.*?</a>', '<a href="https://study.aseeker.bio/english/" target="_blank" rel="noreferrer">原站参考</a>', s, flags=re.S)
    if file == out / 'english/index.html':
        config = '<script>window.EnglishHosting=' + json.dumps({'mode':'static','base':base},ensure_ascii=False) + ';</script><script src="' + base + '/english/js/hosting.js"></script>'
        s = s.replace('</head>', config + '\n</head>')
        s = s.replace('<a class="snav-brand"', '<span style="font-size:11px;color:#758176;margin-right:12px">个人学习改造版 · 与原站无关联</span><a class="snav-brand"', 1)
        s = s.replace('<body>', '<body><style>#scanShareBtn,#friendBtn{display:none!important}</style>', 1)
    file.write_text(s)

app = out / 'english/js/app.js'
s = app.read_text().replace("const MATERIALS_BASE = '/english-materials/';", "const MATERIALS_BASE = '" + base + "/english-materials/';")
app.write_text(s)
versions_file = out / 'english/data/version.json'
versions = json.loads(versions_file.read_text())
versions['app'] = hashlib.md5(app.read_bytes()).hexdigest()[:10]
versions_file.write_text(json.dumps(versions,ensure_ascii=False,indent=2))
index = out / 'english/index.html'
index.write_text(re.sub(r'js/app\.js\?v=[\w.-]+', 'js/app.js?v='+versions['app'], index.read_text()))
target = base + '/english/'
(out/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>英语二精翻</title><meta http-equiv="refresh" content="0;url='+target+'"><a href="'+target+'">打开英语二精翻</a></html>')
(out/'.nojekyll').touch()
manifest = json.loads((out/'english-materials/manifest.json').read_text())
if args.external_materials:
    for item in manifest:
        item['url'] = 'https://study.aseeker.bio/english-materials/' + urllib.parse.quote(item['name'])
    (out/'english-materials/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    for pdf in (out/'english-materials').glob('*.pdf'):
        pdf.unlink()
missing = [item['name'] for item in manifest if not (out/'english-materials'/item['name']).exists()]
if missing and not args.external_materials:
    raise SystemExit('Missing published materials: '+', '.join(missing))
print(f'Built {out}: {len(manifest)} materials, base={base}')
