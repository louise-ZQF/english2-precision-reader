#!/usr/bin/env python3
"""Capture only the public English app resources referenced by published pages."""
import concurrent.futures
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://study.aseeker.bio'
PUBLIC = ROOT / 'public'
RAW = ROOT / 'reference' / 'upstream'
records = {}


def destination(path):
    p = urllib.parse.unquote(urllib.parse.urlsplit(path).path)
    if p.endswith('/'):
        p += 'index.html'
    if '..' in Path(p).parts:
        raise ValueError(path)
    return p.lstrip('/')


def download(path):
    url = urllib.parse.urljoin(ORIGIN, path)
    rel = destination(path)
    raw = RAW / rel
    if raw.exists():
        content = raw.read_bytes()
    else:
        req = urllib.request.Request(url, headers={'User-Agent': 'English-local-study-snapshot/1.0'})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=45) as response:
                    content = response.read()
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(content)
    out = PUBLIC / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(content)
    return {'path': '/' + rel, 'url': url, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}


def batch(paths):
    paths = sorted(set(paths) - set(records))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(download, p): p for p in paths}
        for future in concurrent.futures.as_completed(futures):
            p = futures[future]
            try:
                records[p] = future.result()
                print(f'OK {p} ({records[p]["bytes"]:,} bytes)', flush=True)
            except Exception as e:
                records[p] = {'url': ORIGIN + p, 'error': str(e)}
                print(f'ERROR {p}: {e}', flush=True)
    (ROOT / 'reference' / 'capture-manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))


def assets(text, base):
    refs = re.findall(r'(?:href|src)=["\']([^"\']+)', text)
    refs += re.findall(r'url\(["\']?([^\)"\']+)', text)
    literals = re.findall(r'["\']([^"\'\n<>]+\.(?:json|png|jpg|jpeg|gif|svg|webp|woff2?|ttf|ico|css|js))(?:\?[^"\']*)?["\']', text)
    for ref in literals:
        if base.endswith('.js'):
            if ref.startswith('data/') or ref.startswith('js/'):
                ref = '/english/' + ref
            elif not ref.startswith('/'):
                continue
        refs.append(ref)
    found = []
    for ref in refs:
        u = urllib.parse.urlsplit(urllib.parse.urljoin(ORIGIN + base, ref))
        if u.netloc != 'study.aseeker.bio':
            continue
        if re.search(r'\.(?:json|png|jpg|jpeg|gif|svg|webp|woff2?|ttf|ico|css|js)$', u.path, re.I):
            if '/api/' not in u.path:
                found.append(u.path)
    return found


def main():
    initial = ['/english/', '/english/words/', '/english/words/health/', '/english/words/time/']
    initial += [f'/english/paper/{y}_english2/' for y in range(2010, 2027)]
    initial += [f'/english/data/exam_{y}_english2.json' for y in range(2010, 2027)]
    initial += ['/english/data/version.json', '/english/data/dict.json', '/english/data/sentence_translations.json', '/english-materials/manifest.json']
    batch(initial)
    for _ in range(4):
        found = []
        for path, record in list(records.items()):
            if 'error' in record or not re.search(r'(?:/|\.(?:html|css|js))$', path):
                continue
            text = (RAW / destination(path)).read_text(errors='replace')
            found.extend(assets(text, path))
        pending = set(found) - set(records)
        if not pending:
            break
        batch(pending)
    manifest_path = RAW / 'english-materials/manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        files = []
        def walk(o):
            if isinstance(o, dict):
                if isinstance(o.get('name'), str) and o['name'].lower().endswith('.pdf') and '英二' in o['name']:
                    files.append('/english-materials/' + urllib.parse.quote(o['name']))
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(manifest)
        batch(files)
    print(json.dumps({'files': len(records), 'bytes': sum(r.get('bytes', 0) for r in records.values()), 'errors': {p:r['error'] for p,r in records.items() if 'error' in r}}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
