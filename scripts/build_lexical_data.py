#!/usr/bin/env python3
"""Build a free, offline learner dictionary and exact-occurrence review data.

ECDICT is MIT licensed. Keep its raw CSV in reference/upstream/ecdict.csv (ignored).
This build filters dictionary data; it does NOT claim to review word senses.
Only the separately authored meaning-review records become context corrections.
"""
import argparse
import collections
import csv
import hashlib
import json
import re
from pathlib import Path
from precision_lexicon import PHRASES

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public/english'
parser = argparse.ArgumentParser()
parser.add_argument('--ecdict', type=Path, default=ROOT / 'reference/upstream/ecdict.csv')
parser.add_argument('--dictionary-only', action='store_true', help='Build lexical source while the article reviews are still being authored')
args = parser.parse_args()
manual = json.loads((ROOT / 'scripts/lexical_overrides.json').read_text())
supplement_file = ROOT / 'scripts/lexical_missing.json'
supplement = json.loads(supplement_file.read_text()) if supplement_file.exists() else {'words': {}, 'aliases': {}}
old = json.loads((PUBLIC / 'data/dict.json').read_text())['dict']
form_source = (PUBLIC / 'js/word-forms.js').read_text()
form_data = json.loads(form_source.split(' = ', 1)[1].rstrip(';\n'))
POS = {'vt': 'v', 'vi': 'v', 'adj': 'a', 'ad': 'adv', 'det': 'art', 'int': 'interj'}
FORM_LABELS = {'s': '名词复数', '3': '第三人称单数', 'p': '过去式', 'd': '过去分词', 'i': '现在分词／动名词', 'r': '比较级', 't': '最高级'}
FUNCTION_WORDS = {
    'a': [('art', '一个；某一类中的一个（不定冠词）')], 'an': [('art', '一个；某一类中的一个（用于元音音素前）')],
    'the': [('art', '表示特指、上文提过或双方已知的人或事物；通常不单独译出')],
    'will': [('aux', '将；会；愿意'), ('n', '意志；意愿；遗嘱')], 'would': [('aux', '会；愿意；表示假设、过去习惯或委婉语气')],
    'shall': [('aux', '将；应当')], 'should': [('aux', '应该；应当')], 'can': [('aux', '能；能够；可以'), ('n', '罐；容器')],
    'could': [('aux', '能；可能；可以（也可表示委婉或假设）')], 'may': [('aux', '可能；可以')],
    'might': [('aux', '可能；也许'), ('n', '强大的力量')], 'must': [('aux', '必须；一定（表示必要或推断）')],
    'ought': [('aux', '应该；应当（通常与 to 连用）')], 'be': [('v', '是；处于；存在'), ('aux', '构成进行时或被动语态')],
    'have': [('v', '有；拥有；经历'), ('aux', '构成完成时')], 'do': [('v', '做；进行'), ('aux', '用于疑问、否定或强调')],
    'to': [('prep', '到；向；对于'), ('inf', '不定式标记，连接后面的动词原形')],
    'of': [('prep', '……的；表示所属、部分、内容或关联')], 'for': [('prep', '为了；对于；持续（一段时间）'), ('conj', '因为（用于说明理由）')],
    'with': [('prep', '和；与；带有；用；随着')], 'by': [('prep', '由；通过；在……旁；不迟于')],
    'in': [('prep', '在……里；在……期间；以……方式')], 'on': [('prep', '在……上；关于；处于……状态')],
    'at': [('prep', '在（地点或时刻）；以（速度或价格）；针对')], 'from': [('prep', '从；来自；由……起')],
    'as': [('conj', '当……时；因为；正如；按……方式'), ('prep', '作为；当作'), ('adv', '同样地（用于比较）')],
    'that': [('pron', '那个；那件事'), ('conj', '引导从句，通常不单独译出')],
    'which': [('pron', '哪一个；引导定语从句时指代前面的事物')], 'who': [('pron', '谁；引导定语从句时指代人')],
    'whom': [('pron', '谁（宾格）；定语从句中指代人')], 'whose': [('pron', '谁的；……的（表示所属）')],
    'what': [('pron', '什么；所……的事物')], 'where': [('adv', '在哪里；在……的地方')],
    'when': [('adv', '何时'), ('conj', '当……时；在……情况下')], 'why': [('adv', '为什么；……的原因')],
    'how': [('adv', '如何；怎样；多么')], 'while': [('conj', '当……时；而；虽然'), ('n', '一段时间')],
    'since': [('conj', '自从；既然；因为'), ('prep', '自……以来'), ('adv', '此后；从那时起')],
    'if': [('conj', '如果；是否；即使（视结构而定）')], 'whether': [('conj', '是否；不论……还是……')],
    'and': [('conj', '和；并且；表示并列或承接')], 'or': [('conj', '或者；否则；即（用于解释）')],
    'but': [('conj', '但是；而；表示转折'), ('prep', '除……以外')], 'nor': [('conj', '也不；用于连接否定内容')],
    'not': [('adv', '不；没有')], 'no': [('art', '没有；任何……都不'), ('adv', '不；不是')],
    'than': [('conj', '比；用于比较结构')], 'though': [('conj', '虽然；尽管'), ('adv', '不过；然而')],
    'although': [('conj', '虽然；尽管')], 'unless': [('conj', '除非；如果不')], 'until': [('conj', '直到……才／为止'), ('prep', '直到')],
    'because': [('conj', '因为')], 'before': [('prep', '在……之前'), ('conj', '在……之前；还没来得及……就')],
    'after': [('prep', '在……之后'), ('conj', '在……之后')], 'during': [('prep', '在……期间')],
    'through': [('prep', '通过；穿过；经历；自始至终')], 'throughout': [('prep', '遍及；贯穿……始终')],
    'into': [('prep', '进入；变为；表示变化的结果')], 'onto': [('prep', '到……上；向……上')],
    'over': [('prep', '在……上方；超过；关于；在……期间'), ('adv', '结束；翻转过来')],
    'under': [('prep', '在……下面；在……条件下；受……支配')], 'between': [('prep', '在……之间')],
    'among': [('prep', '在……之中；在群体内部')], 'against': [('prep', '反对；对抗；靠着；与……相比')],
    'without': [('prep', '没有；不；在缺少……的情况下')], 'within': [('prep', '在……以内；在……内部')],
    'about': [('prep', '关于'), ('adv', '大约；差不多')], 'off': [('adv', '离开；停止；断开'), ('prep', '离……；从……脱离')],
    'up': [('adv', '向上；增加；完全（常构成动词短语）')], 'down': [('adv', '向下；减少；记下（常构成动词短语）')],
    'i': [('pron', '我')], 'me': [('pron', '我（宾格）')], 'my': [('pron', '我的')], 'mine': [('pron', '我的（人或东西）')],
    'you': [('pron', '你；你们；泛指任何人')], 'your': [('pron', '你的；你们的')], 'yours': [('pron', '你的／你们的（人或东西）')],
    'he': [('pron', '他')], 'him': [('pron', '他（宾格）')], 'his': [('pron', '他的')], 'she': [('pron', '她')],
    'her': [('pron', '她（宾格）；她的')], 'hers': [('pron', '她的（人或东西）')], 'it': [('pron', '它；这件事；也可作形式主语或形式宾语')],
    'its': [('pron', '它的')], 'we': [('pron', '我们')], 'us': [('pron', '我们（宾格）')], 'our': [('pron', '我们的')],
    'ours': [('pron', '我们的（人或东西）')], 'they': [('pron', '他们；她们；它们；也可泛指某人')],
    'them': [('pron', '他们／她们／它们（宾格）')], 'their': [('pron', '他们的；她们的；它们的')],
    'this': [('pron', '这个；这件事')], 'these': [('pron', '这些')], 'those': [('pron', '那些')],
    'there': [('adv', '那里；there be 结构中表示存在')], 'here': [('adv', '这里；在这里')],
    'such': [('art', '这样的；如此的')], 'each': [('art', '每一；各个')], 'every': [('art', '每个；所有的')],
    'any': [('art', '任何的；一些（用于否定、疑问等结构）')], 'some': [('art', '一些；某些')],
    'all': [('art', '所有；全部')], 'both': [('art', '两者；双方')], 'either': [('art', '两者中的任一个'), ('adv', '也（用于否定句）')],
    'neither': [('art', '两者都不')], 'other': [('a', '其他的；另外的')], 'another': [('art', '另一个；再一个')],
    'same': [('a', '相同的；同一的')], 'own': [('a', '自己的'), ('v', '拥有')],
}

def clean_senses(raw):
    result = []
    for line in raw.replace('\\r\\n', '\n').replace('\\n', '\n').replace('\\r', '').splitlines():
        line = line.strip()
        if not line or re.search(r'\[(?:计|医|法|化|经|机|电|建|生|物|地|数|军|纺|商|航|农|冶|核|光|自|语|心理|植|动)[^\]]*\]', line):
            continue
        match = re.match(r'^(n|v|vt|vi|a|adj|ad|adv|aux|prep|conj|pron|art|num|interj|int)\.\s*(.*)', line)
        pos, meaning = (POS.get(match[1], match[1]), match[2]) if match else ('', line)
        if re.search(r'过去式|过去分词|现在分词|第三人称|的复数|复数形式', meaning):
            continue
        meaning = re.sub(r'\[[^\]]*\]', '', meaning).strip()
        fragments = [value.strip(' .。;；') for value in re.split(r'[,，;；、]', meaning) if value.strip(' .。;；')]
        fragments = list(dict.fromkeys(fragments))[:3]
        value = {'p': pos, 'm': '；'.join(fragments)}
        if value['m'] and value not in result:
            result.append(value)
    return result[:6]

needed = set(old) | set(form_data['words']) | set(form_data['index']) | set(manual['words']) | set(manual['compounds']) | set(supplement['words']) | {item['lemma'] for item in supplement['aliases'].values()}
raw_entries = {}
with args.ecdict.open(encoding='utf-8') as stream:
    for row in csv.DictReader(stream):
        key = row['word'].lower()
        if key in needed and (key not in raw_entries or row['word'] == key):
            raw_entries[key] = row
# Include explicit dictionary lemmas for written forms, not suffix guesses.
for row in list(raw_entries.values()):
    for field in row['exchange'].split('/'):
        if field.startswith('0:'):
            needed.add(field[2:].lower())
if not needed.issubset(set(raw_entries)):
    missing = needed - raw_entries.keys()
    with args.ecdict.open(encoding='utf-8') as stream:
        for row in csv.DictReader(stream):
            if row['word'].lower() in missing and (row['word'].lower() not in raw_entries or row['word'] == row['word'].lower()):
                raw_entries[row['word'].lower()] = row

words, aliases = {}, collections.defaultdict(list)
for lemma in sorted(needed):
    row = raw_entries.get(lemma, {})
    senses = clean_senses(row.get('translation', ''))
    if lemma in manual['words']:
        senses = manual['words'][lemma]
    if lemma in FUNCTION_WORDS:
        senses = [{'p': p, 'm': m} for p, m in FUNCTION_WORDS[lemma]]
    if lemma in supplement['words']:
        senses = supplement['words'][lemma]
    if lemma in manual['compounds']:
        meaning = manual['compounds'][lemma]
        senses = [{'p': senses[0]['p'] if senses and senses[0]['p'] else 'a' if meaning.endswith('的') else 'n', 'm': meaning}]
    # Keep useful untagged original data for names and rare entries, but never
    # restore a rejected domain-specific or purely morphological definition.
    if not senses and not row:
        senses = [s for value in old.get(lemma, {}).get('s', []) for s in clean_senses((value.get('p', '') + '. ' if value.get('p') else '') + value.get('t', ''))]
    base = form_data['words'].get(lemma, {})
    forms = {item['label']: list(item['words']) for item in base.get('forms', [])}
    pos = sorted({item['p'] for item in senses if item['p']} | set(base.get('pos', [])))
    for code, label in FORM_LABELS.items():
        values = next((field.split(':', 1)[1] for field in row.get('exchange', '').split('/') if field.startswith(code + ':')), '')
        if values:
            forms[label] = list(dict.fromkeys(forms.get(label, []) + [v.lower() for v in values.split(',') if v.strip()]))
    words[lemma] = {'ph': row.get('phonetic') or old.get(lemma, {}).get('ph', ''), 'common': senses, 'pos': pos,
                    'forms': [{'label': label, 'words': values} for label, values in forms.items() if values]}
    for item in words[lemma]['forms']:
        p = 'n' if item['label'] == '名词复数' else 'a' if item['label'] in ('比较级', '最高级') else 'v'
        for written in item['words']:
            if re.fullmatch(r"[a-z]+(?:['-][a-z]+)*", written):
                aliases[written].append({'lemma': lemma, 'p': p, 'label': item['label'], 'source': 'ECDICT' if row.get('exchange') else 'corpus'})
for form, entries in form_data['index'].items():
    for item in entries:
        if item['lemma'] in words and not any(value['lemma'] == item['lemma'] and value['p'] == item['p'] and value['label'] == item['label'] for value in aliases[form]):
            aliases[form].append({key: item[key] for key in ('lemma', 'p', 'label')})
for form, item in supplement['aliases'].items():
    label = {'复数': '名词复数'}.get(item['label'], item['label'])
    labels = ['过去式', '过去分词'] if label == '过去式／过去分词' else [label]
    aliases[form] = [{'lemma': item['lemma'], 'p': item.get('p', ''), 'label': value, 'source': 'reviewed'} for value in labels] + [value for value in aliases[form] if value['lemma'] != item['lemma']]
    family = words[item['lemma']]
    for value in labels:
        row = next((row for row in family['forms'] if row['label'] == value), None)
        if row is None:
            family['forms'].append({'label': value, 'words': [form]})
        elif form not in row['words']:
            row['words'].append(form)

source_hash = hashlib.sha256(args.ecdict.read_bytes()).hexdigest()
payload = {'revision': '20261029-lexical-v2', 'source': 'ECDICT (MIT) + independently authored learner senses', 'sourceSHA256': source_hash,
           'words': words, 'index': dict(aliases), 'phrases': {**PHRASES, **manual['phrases']}}
(PUBLIC / 'data/ECDICT-LICENSE.txt').write_text((ROOT / 'reference/licenses/ECDICT-LICENSE.txt').read_text())
(PUBLIC / 'js/lexical-data.js').write_text('/* Free offline dictionary; ECDICT MIT license: data/ECDICT-LICENSE.txt. */\nwindow.EnglishLexicalData = ' + json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + ';\nwindow.EnglishWordForms = window.EnglishLexicalData;\n')
if args.dictionary_only:
    print(json.dumps({'dictionaryEntries': len(words), 'writtenForms': len(aliases), 'entriesWithMeanings': sum(bool(entry['common']) for entry in words.values())}))
    raise SystemExit(0)

exams = [json.loads(file.read_text()) for file in sorted((PUBLIC / 'data').glob('exam_*_english2.json'))]
exam_json = json.dumps(exams, ensure_ascii=False, separators=(',', ':'))
exam_revision = hashlib.sha256(exam_json.encode()).hexdigest()[:12]
(PUBLIC / 'js/exams-data.js').write_text('/* Bundled English-II papers for browser and direct local-file use. */\nwindow.EnglishBuiltinExams = ' + exam_json + ';\nwindow.EnglishBuiltinRevision = ' + json.dumps(exam_revision) + ';\n')

reviews = {'version': 2, 'sentences': [], 'articles': []}
corpus = {}
for file in (PUBLIC / 'data/precision').glob('*_english2.json'):
    corpus[file.stem] = {s['en'] for block in json.loads(file.read_text())['blocks'].values() for s in block}
for file in sorted((PUBLIC / 'data/meaning-review').glob('review_*.json')):
    data = json.loads(file.read_text())
    for sentence in data.get('sentences', []):
        if sentence['en'] not in corpus.get(sentence['exam'], set()):
            raise ValueError(f'{file.name}: sentence not in corpus: {sentence["en"][:80]}')
        for item in sentence.get('words', []) + sentence.get('phrases', []):
            if not 0 <= item['a'] < item['b'] <= len(sentence['en']):
                raise ValueError(f'{file.name}: bad offset {item}')
            if item.get('word') and sentence['en'][item['a']:item['b']] != item['word']:
                raise ValueError(f'{file.name}: written word mismatch {item}')
        reviews['sentences'].append(sentence)
    reviews['articles'].extend(data.get('articles', []))
review_json = json.dumps(reviews, ensure_ascii=False, separators=(',', ':'))
reviews['revision'] = hashlib.sha256(review_json.encode()).hexdigest()[:12]
(PUBLIC / 'js/reviewed-meanings.js').write_text('/* Independently authored, occurrence-specific English-II readings and glosses. */\nwindow.EnglishMeaningReviews = ' + json.dumps(reviews, ensure_ascii=False, separators=(',', ':')) + ';\n')
report = {'dictionaryEntries': len(words), 'writtenForms': len(aliases), 'entriesWithMeanings': sum(bool(entry['common']) for entry in words.values()),
          'reviewedArticles': len(reviews['articles']), 'reviewedSentences': len(reviews['sentences']),
          'correctedWords': sum(len(s.get('words', [])) for s in reviews['sentences']), 'reviewedPhrases': sum(len(s.get('phrases', [])) for s in reviews['sentences']),
          'ecdictSHA256': source_hash, 'reviewRevision': reviews['revision']}
(ROOT / 'reference/lexical-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
