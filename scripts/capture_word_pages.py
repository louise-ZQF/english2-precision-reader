#!/usr/bin/env python3
"""Archive the public word-detail pages listed in the English sitemap."""
import concurrent.futures
import json
import re
import urllib.parse
import urllib.request
from capture import ROOT, download

url = 'https://study.aseeker.bio/english/sitemap.xml'
content = urllib.request.urlopen(url, timeout=30).read()
(ROOT / 'reference/english-sitemap.xml').write_bytes(content)
paths = [urllib.parse.urlsplit(u).path for u in re.findall(r'<loc>(.*?)</loc>', content.decode())]
paths = sorted({p for p in paths if re.fullmatch(r'/english/words/[^/]+/', p)})
records = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(download, p): p for p in paths}
    for n, future in enumerate(concurrent.futures.as_completed(futures), 1):
        p = futures[future]
        try:
            records.append(future.result())
        except Exception as e:
            records.append({'url': 'https://study.aseeker.bio' + p, 'error': str(e)})
        if n % 250 == 0 or n == len(paths):
            print(f'Word pages: {n}/{len(paths)}', flush=True)
        if n % 100 == 0:
            (ROOT / 'reference/word-pages-manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
(ROOT / 'reference/word-pages-manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
print(json.dumps({'total': len(paths), 'bytes': sum(r.get('bytes', 0) for r in records), 'errors': [r for r in records if 'error' in r]}, ensure_ascii=False), flush=True)
