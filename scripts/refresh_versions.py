#!/usr/bin/env python3
"""Refresh content tags after editing JS or CSS; leaves the implementation intact."""
import hashlib
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / 'public/english'
index = (ROOT/'index.html').read_text()
for folder, extension in [('js','js'),('css','css')]:
    for file in (ROOT/folder).glob('*.'+extension):
        stamp = hashlib.md5(file.read_bytes()).hexdigest()[:10]
        path = folder+'/'+file.name
        index = re.sub(re.escape(path)+r'\?v=[A-Za-z0-9._-]+', path+'?v='+stamp, index)
(ROOT/'index.html').write_text(index)
versions = json.loads((ROOT/'data/version.json').read_text())
versions['app'] = hashlib.md5((ROOT/'js/app.js').read_bytes()).hexdigest()[:10]
(ROOT/'data/version.json').write_text(json.dumps(versions,ensure_ascii=False,indent=2))
print('Updated local asset tags.')
