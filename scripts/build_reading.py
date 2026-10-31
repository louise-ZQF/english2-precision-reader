#!/usr/bin/env python3
"""Extract, validate, export and compile the separately edited reading files.

No translation generation or online API. Existing editorial files are never
overwritten during extraction. Source verification precedes reviewed content.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/english/data'
READING = DATA / 'reading'
BROWSER = DATA / 'reading-browser'

def clean(value):
    return re.sub(r'\s+', ' ', value.replace('’', "'").replace('‘', "'")).strip()

def paragraphs(values):
    result = []
    for value in values:
        value = clean(value)
        if not value:
            continue
        if result and not re.search(r'''[.!?](?:\s*["'”’)\]])*$''', result[-1]):
            result[-1] += ' ' + value
        else:
            result.append(value)
    return result

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()

def expected_articles():
    result = {}
    for file in sorted(DATA.glob('exam_*_english2.json')):
        exam = json.loads(file.read_text())
        for si, section in enumerate(exam['sections']):
            for pi, part in enumerate(section.get('parts', [])):
                for ti, text in enumerate(part.get('texts', []), 1):
                    ident = f'{exam["year"]}-T{ti}'
                    result[ident] = {'exam': exam['exam_id'], 'year': int(exam['year']), 'text': ti,
                                     'articleKey': f's{si}-p{pi}-t{ti-1}', 'paragraphs': paragraphs(text['paragraphs'])}
    return result

def extract(expected):
    READING.mkdir(exist_ok=True)
    for ident, item in expected.items():
        target = READING / (ident + '.json')
        if target.exists():
            continue
        bank = json.loads((DATA / 'precision' / (item['exam'] + '.json')).read_text())['blocks']
        rows = []
        for pi, en in enumerate(item['paragraphs'], 1):
            if en not in bank:
                raise ValueError(f'{ident}-P{pi}: missing source sentence boundaries')
            sentences = [{'id': f'{ident}-P{pi}-S{si}', 'a': s['a'], 'b': s['b'], 'en': s['en'],
                          'status': 'pending', 'chunks': [], 'reorder': '', 'translation': '', 'words': [], 'phrases': []}
                         for si, s in enumerate(bank[en], 1)]
            rows.append({'id': f'{ident}-P{pi}', 'en': en, 'sentences': sentences})
        payload = {'version': 1, 'id': ident, 'exam': item['exam'], 'year': item['year'], 'text': item['text'],
                   'articleKey': item['articleKey'], 'source': {'status': 'pending', 'textSHA256': digest(item['paragraphs']),
                   'evidence': [], 'notes': []}, 'paragraphs': rows}
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')

def validate(article, expected):
    ident = article['id']
    assert ident in expected, f'Unknown article {ident}'
    assert article['exam'] == expected[ident]['exam']
    source = [p['en'] for p in article['paragraphs']]
    assert source == expected[ident]['paragraphs'], f'{ident}: source changed; verify before re-editing translations'
    assert digest(source) == article['source']['textSHA256'], f'{ident}: source hash changed'
    for pi, p in enumerate(article['paragraphs'], 1):
        assert p['id'] == f'{ident}-P{pi}'
        cursor = 0
        for si, s in enumerate(p['sentences'], 1):
            label = f'{p["id"]}-S{si}'
            assert s['id'] == label
            assert not p['en'][cursor:s['a']].strip(), f'{label}: omitted source text'
            assert p['en'][s['a']:s['b']] == s['en'], f'{label}: sentence offset mismatch'
            cursor = s['b']
            if s['status'] == 'reviewed':
                assert article['source']['status'] == 'verified', f'{label}: verify English first'
                assert s.get('translation') and s.get('reorder') and s.get('reviewedAt'), f'{label}: unfinished review'
                end = 0
                for chunk in s['chunks']:
                    assert chunk['a'] == end and chunk['b'] > end, f'{label}: chunk gap/overlap'
                    assert s['en'][chunk['a']:chunk['b']] == chunk['en'] and chunk['zh'], f'{label}: chunk mismatch'
                    end = chunk['b']
                assert end == len(s['en']), f'{label}: chunks do not reconstruct the full English sentence'
            for word in s.get('words', []) + s.get('phrases', []):
                assert 0 <= word['a'] < word['b'] <= len(s['en']), f'{label}: invalid word offset'
                assert s['en'][word['a']:word['b']] == word['word'], f'{label}: word bound to wrong position'
                assert word.get('lemma') and word.get('meaning'), f'{label}: missing word meaning'
            for word in s.get('words', []):
                assert word['a'] == 0 or not s['en'][word['a']-1].isalnum(), f'{label}: word starts inside another word'
                assert word['b'] == len(s['en']) or not s['en'][word['b']].isalnum(), f'{label}: word ends inside another word'
        assert not p['en'][cursor:].strip(), f'{p["id"]}: omitted trailing sentence'

def merge(path, articles):
    payload = json.loads(path.read_text())
    assert payload.get('app') == 'english2-reading-corrections' and payload.get('version') == 1
    lookup = {s['id']: (a, s) for a in articles for p in a['paragraphs'] for s in p['sentences']}
    touched = set()
    for ident, edit in payload.get('records', {}).items():
        assert ident in lookup, f'Unknown sentence {ident}'
        a, s = lookup[ident]
        assert edit.get('en') == s['en'] and edit.get('sourceHash') == a['source']['textSHA256'], f'{ident}: stale source; review manually'
        for field in ('translation', 'reorder'):
            if field in edit:
                assert isinstance(edit[field], str)
                s[field] = edit[field]
                if field == 'translation':
                    s['translationStatus'] = 'corrected'
        if edit.get('chunks'):
            assert len(edit['chunks']) == len(s['chunks'])
            for new, old in zip(edit['chunks'], s['chunks']):
                assert (new['a'], new['b']) == (old['a'], old['b'])
                old['zh'] = str(new['zh'])
        for word in edit.get('words', []):
            assert s['en'][word['a']:word['b']] == word['word']
            field = 'phrases' if word.get('kind') == 'phrase' else 'words'
            s[field] = [old for old in s[field] if (old['a'], old['b']) != (word['a'], word['b'])] + [word]
        s['lastCorrectionAt'] = edit.get('updatedAt')
        touched.add(a['id'])
    # Validate the entire merge before writing any article.
    expected = expected_articles()
    for a in articles:
        validate(a, expected)
    for a in articles:
        if a['id'] in touched:
            (READING / (a['id'] + '.json')).write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
    return touched

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract', action='store_true')
    parser.add_argument('--export', metavar='YEAR-TEXT', help='Print an article with numbered English sentences, e.g. 2012-T3')
    parser.add_argument('--merge', type=Path, help='Merge a browser correction export, with exact source checks')
    args = parser.parse_args()
    expected = expected_articles()
    if args.extract:
        extract(expected)
    articles = [json.loads(f.read_text()) for f in sorted(READING.glob('*.json'))]
    assert len(articles) == len(expected) == 68, 'Expected 68 distinct reading articles'
    assert len({a['id'] for a in articles}) == 68
    if args.merge:
        print('Merged:', ', '.join(sorted(merge(args.merge, articles))))
    if args.export:
        a = next(a for a in articles if a['id'] == args.export)
        print(f'# {a["id"]} / source: {a["source"]["status"]}\n')
        for p in a['paragraphs']:
            for s in p['sentences']:
                print(s['id'] + '\n' + s['en'] + '\n')
        return
    BROWSER.mkdir(exist_ok=True)
    manifest, total, reviewed = [], 0, 0
    for a in articles:
        validate(a, expected)
        ss = [s for p in a['paragraphs'] for s in p['sentences']]
        ready = sum(s['status'] == 'reviewed' for s in ss)
        total += len(ss); reviewed += ready
        payload = json.dumps(a, ensure_ascii=False, separators=(',', ':'))
        revision = hashlib.sha256(payload.encode()).hexdigest()[:12]
        (BROWSER / (a['id'] + '.js')).write_text('window.EnglishReadingFiles = window.EnglishReadingFiles || {};\nwindow.EnglishReadingFiles[' + json.dumps(a['id']) + '] = ' + payload + ';\n')
        manifest.append({'id': a['id'], 'exam': a['exam'], 'text': a['text'], 'articleKey': a['articleKey'], 'source': a['source']['status'], 'sentences': len(ss), 'reviewed': ready, 'revision': revision})
    report = {'articles': len(articles), 'sentences': total, 'reviewedSentences': reviewed, 'verifiedArticles': sum(a['source']['status'] == 'verified' for a in articles), 'items': manifest}
    (DATA / 'reading-manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'public/english/js/reading-manifest.js').write_text('window.EnglishReadingManifest = ' + json.dumps(report, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'items'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
