#!/usr/bin/env python3
"""Compile per-exam script fallbacks so file:// retains word context and POS.

The JSON corpus remains the source. Sentence metadata is deduplicated inside
each exam. No NLP regeneration, external request, or user learning data involved.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/english/data/precision'
OUT = DATA.parent / 'precision-browser'
OUT.mkdir(exist_ok=True)
total = 0
for file in sorted(DATA.glob('*_english2.json')):
    source = json.loads(file.read_text())
    sentences, ids, blocks = [], {}, {}
    for text, rows in source['blocks'].items():
        refs = []
        for sentence in rows:
            content = {key: value for key, value in sentence.items() if key not in ('a', 'b')}
            key = json.dumps(content, ensure_ascii=False, separators=(',', ':'))
            if key not in ids:
                ids[key] = len(sentences)
                sentences.append(content)
            refs.append([ids[key], sentence['a'], sentence['b']])
        blocks[text] = refs
    payload = json.dumps({'sentences': sentences, 'blocks': blocks}, ensure_ascii=False, separators=(',', ':'))
    code = '/* Generated from data/precision/' + file.name + '; local-file context fallback. */\n'
    code += 'window.EnglishPrecisionBrowser = window.EnglishPrecisionBrowser || {};\n'
    code += 'window.EnglishPrecisionBrowser[' + json.dumps(source['exam']) + '] = ' + payload + ';\n'
    (OUT / (file.stem + '.js')).write_text(code)
    total += len(code.encode())
print(f'Compiled 17 exam context fallbacks, {total:,} bytes.')
