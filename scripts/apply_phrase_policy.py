#!/usr/bin/env python3
"""Apply the human phrase decisions; never infer new phrases from a dictionary.

Run after authoring, before build_reading.py. Removed rows remain in the report.
The explicitly edited split structures leave their variable objects clickable.
"""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'reference/reading-audit-v2'
DATA = ROOT / 'public/english/data/reading'

def norm(value):
    return value.replace('’', "'").lower().replace('...', ' … ').replace('…', ' … ').strip()

# Exact anchor text from the reviewed source, not a pattern spanning arbitrary
# intervening objects. The meaning belongs to the framework, not its object.
SPLITS = {
 'exempt from': ('exempt … from …', '使……免于……；免除……的义务', ['exempted', 'from']),
 'fuse A to B': ('fuse A to B', '把 A 与 B 紧密结合；将 A 与 B 绑定', ['fuses', 'to']),
 'infuse with': ('infuse … with …', '为……注入……；赋予……某种特质', ['infuse', 'with']),
 'set free': ('set … free', '释放……；让……自由', ['set', 'free']),
 'with…in mind': ('with … in mind', '考虑到……；心里想着……', ['with', 'in mind']),
 'feed a hunger for': ('feed … hunger for …', '满足……对……的强烈需求', ['feed', 'hunger for']),
 'bring to life': ('bring … to life', '使……生动鲜活；使……活起来', ['bring', 'to life']),
 'rip off': ('rip off', '坑骗；盘剥；敲竹杠', ['ripping', 'off']),
 'close down': ('close down', '关闭；关停', ['closed', 'down']),
 'bond with': ('bond with', '与……建立联系或亲近关系', ['bonded', 'with']),
 'correlate with': ('correlate with', '与……相关联', ['correlated', 'with']),
 'align with': ('align with', '与……相匹配；与……一致', ['aligned', 'with']),
 'place a high value on': ('place a high value on', '高度重视……', ['place a', 'high value on']),
 'keep track of': ('keep track of', '持续了解；跟踪……的情况', ['keep', 'track of']),
 'take chances': ('take chances', '冒险', ['taking', 'chances']),
 'put an end to': ('put an end to', '结束；终止', ['put a', 'end to']),
 'turn to': ('turn to', '转而求助于……', ['turns to']),
 'On top of this': ('on top of', '此外；除……之外', ['On top of']),
 'hold...to account': ('hold … to account', '要求……作出解释并承担责任；向……问责', ['hold', 'to account']),
 'put...into perspective': ('put … into perspective', '结合整体情况恰当地看待……', ['putting', 'into perspective']),
 'leave it up to': ('leave … up to …', '把……交给……负责或决定', ['leaving', 'up to']),
}

def apply():
    policy = json.loads((AUDIT / 'phrase-classification.json').read_text())
    policy_hash = hashlib.sha256((AUDIT / 'phrase-classification.json').read_bytes()).hexdigest()
    decisions = {row['lemma']: (kind, row) for kind in ('approved','names','rejected') for row in policy[kind]}
    assert len(decisions) == sum(len(policy[k]) for k in ('approved','names','rejected'))
    for kind in ('approved','names'):
        for row in policy[kind]:
            if row.get('canonical'): decisions.setdefault(row['canonical'], (kind,row))
    for lemma, _, _ in SPLITS.values(): decisions.setdefault(lemma, ('approved', {}))
    additions = json.loads((AUDIT / '2015-2019/common-phrase-additions-reviewed.json').read_text())
    extra = AUDIT / '2020-2024/common-phrase-additions-reviewed.json'
    if extra.exists(): additions += json.loads(extra.read_text())
    by_sentence = {}
    for row in additions: by_sentence.setdefault(row['id'], []).append(row)
    report_path = AUDIT / 'phrase-policy-applied.json'
    previous = json.loads(report_path.read_text()) if report_path.exists() else {}
    removed, split, added = [previous.get(k, []) for k in ('removed','splitStructures','added')]
    counts = {'phrases':0, 'names':0}
    for path in sorted(DATA.glob('*.json')):
        article = json.loads(path.read_text())
        if article.get('phraseReviewPolicy', {}).get('classificationSHA256') == policy_hash:
            for paragraph in article['paragraphs']:
                for sentence in paragraph['sentences']:
                    for row in sentence['phrases']: counts['names' if row.get('kind')=='name' else 'phrases'] += 1
            continue
        for paragraph in article['paragraphs']:
            for sentence in paragraph['sentences']:
                rows = []
                for row in sentence['phrases']:
                    kind, decision = decisions[row['lemma']]
                    if kind == 'rejected':
                        removed.append({'id':sentence['id'], **row, 'reason':decision['reason']})
                        if decision.get('meaning') and decision.get('canonical'):
                            first = next((w for w in sentence['words'] if row['a'] <= w['a'] < row['b']), None)
                            if first:
                                first['explanation'] = '搭配结构：' + decision['canonical'] + '＝' + decision['meaning']
                        continue
                    plan = SPLITS.get(row['lemma'])
                    # Only replace this hand-reviewed expanded occurrence. A
                    # correctly bounded occurrence of the same key stays intact.
                    needs_split = plan and all(piece.lower() in row['word'].lower() for piece in plan[2])
                    if needs_split:
                        lemma, meaning, pieces = plan
                        cursor = 0
                        for piece in pieces:
                            start = row['word'].lower().index(piece.lower(), cursor)
                            end = start + len(piece); cursor = end
                            rows.append({'a':row['a']+start,'b':row['a']+end,'word':row['word'][start:end], 'lemma':lemma,'meaning':meaning,'kind':'phrase','structure':True})
                        split.append({'id':sentence['id'],'original':row['word'],'lemma':lemma,'parts':pieces})
                    else:
                        row['kind'] = 'name' if kind == 'names' else 'phrase'
                        if decision.get('canonical'): row['lemma'] = decision['canonical']
                        rows.append(row)
                for row in by_sentence.get(sentence['id'], []):
                    assert row['en'] == sentence['en'] and sentence['en'][row['a']:row['b']] == row['word'], row
                    if any(row['a'] < x['b'] and row['b'] > x['a'] for x in rows): continue
                    item = {key:row[key] for key in ('a','b','word','lemma','meaning')}
                    item['kind'] = 'phrase'; rows.append(item); added.append({'id':sentence['id'], **item})
                rows.sort(key=lambda row:(row['a'], -row['b']))
                sentence['phrases'] = rows
                sentence['auditV2']['phrases'] = sum(row['kind'] == 'phrase' for row in rows)
                sentence['auditV2']['names'] = sum(row['kind'] == 'name' for row in rows)
                for row in rows: counts['names' if row['kind']=='name' else 'phrases'] += 1
        article['phraseReviewPolicy'] = {'version':1,'date':'2026-11-01','classificationSHA256':policy_hash}
        path.write_text(json.dumps(article, ensure_ascii=False, indent=2)+'\n')
    report = {'date':'2026-11-01','counts':counts,'removed':removed,'splitStructures':split,'added':added}
    (AUDIT / 'phrase-policy-applied.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'counts':counts,'removed':len(removed),'splitStructures':len(split),'added':len(added)},ensure_ascii=False))

if __name__ == '__main__': apply()
