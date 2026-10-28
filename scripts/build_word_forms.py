#!/usr/bin/env python3
"""Compile attested English-II word forms for the browser (no runtime NLP)."""
import collections
import json
import re
from pathlib import Path
import spacy

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/english/data'
lexicon = json.loads((DATA / 'precision/lexicon.json').read_text())['words']
sentences = set()
for file in (DATA / 'precision').glob('*_english2.json'):
    for block in json.loads(file.read_text())['blocks'].values():
        sentences.update(sentence['en'] for sentence in block)

LABELS = {'NNS': '名词复数', 'NNPS': '名词复数', 'VBZ': '第三人称单数', 'VBD': '过去式', 'VBN': '过去分词', 'VBG': '现在分词／动名词', 'JJR': '比较级', 'RBR': '比较级', 'JJS': '最高级', 'RBS': '最高级', 'VBP': '现在式'}
POS = {'NOUN': 'n', 'PROPN': 'n', 'VERB': 'v', 'AUX': 'v', 'ADJ': 'a', 'ADV': 'adv'}
families = collections.defaultdict(lambda: collections.defaultdict(set))
index = collections.Counter()
pos_index = collections.defaultdict(set)

def add(lemma, word, pos, label):
    if not re.fullmatch(r"[a-z]+(?:['-][a-z]+)*", lemma):
        return
    pos_index[lemma].add(pos)
    index[(word, lemma, pos, label)] += 1
    if label != '原形':
        families[lemma][label].add(word)

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
for doc in nlp.pipe(sorted(sentences), batch_size=128):
    for token in doc:
        word, lemma, pos = token.text.lower(), token.lemma_.lower(), POS.get(token.pos_, '')
        if not pos or not re.fullmatch(r'[a-z]+', word):
            continue
        label = LABELS.get(token.tag_, '原形') if word != lemma else '原形'
        add(lemma, word, pos, label)
        # Regular -ed forms serve as both past tense and past participle.
        if token.tag_ in {'VBD', 'VBN'} and word.endswith('ed'):
            add(lemma, word, pos, '过去式' if token.tag_ == 'VBN' else '过去分词')
        if pos == 'a' and token.i and doc[token.i - 1].lower_ in {'more', 'most'}:
            add(lemma, doc[token.i - 1].lower_ + ' ' + word, pos, '比较级' if doc[token.i - 1].lower_ == 'more' else '最高级')
    # Keep written compounds intact; record comparisons only when attested.
    for match in re.finditer(r'[A-Za-z]+(?:-[A-Za-z]+)+', doc.text):
        word = match.group().lower()
        add(word, word, 'a', '原形')
        prefix = doc.text[:match.start()].lower()
        comparison = re.search(r'\b(more|most)\s+$', prefix)
        if comparison:
            form = comparison[1] + ' ' + word
            add(word, form, 'a', '比较级' if comparison[1] == 'more' else '最高级')

# Confirmed common irregular families fill gaps in this finite corpus.
IRREGULAR = {
    'be': ('is', 'was/were', 'been', 'being'), 'have': ('has', 'had', 'had', 'having'),
    'do': ('does', 'did', 'done', 'doing'), 'go': ('goes', 'went', 'gone', 'going'),
    'come': ('comes', 'came', 'come', 'coming'), 'take': ('takes', 'took', 'taken', 'taking'),
    'give': ('gives', 'gave', 'given', 'giving'), 'make': ('makes', 'made', 'made', 'making'),
    'get': ('gets', 'got', 'got/gotten', 'getting'), 'write': ('writes', 'wrote', 'written', 'writing'),
    'read': ('reads', 'read', 'read', 'reading'), 'see': ('sees', 'saw', 'seen', 'seeing'),
    'say': ('says', 'said', 'said', 'saying'), 'think': ('thinks', 'thought', 'thought', 'thinking'),
    'buy': ('buys', 'bought', 'bought', 'buying'), 'bring': ('brings', 'brought', 'brought', 'bringing'),
    'find': ('finds', 'found', 'found', 'finding'), 'keep': ('keeps', 'kept', 'kept', 'keeping'),
    'hold': ('holds', 'held', 'held', 'holding'), 'leave': ('leaves', 'left', 'left', 'leaving'),
    'feel': ('feels', 'felt', 'felt', 'feeling'), 'hear': ('hears', 'heard', 'heard', 'hearing'),
    'meet': ('meets', 'met', 'met', 'meeting'), 'run': ('runs', 'ran', 'run', 'running'),
    'spin': ('spins', 'spun', 'spun', 'spinning'), 'begin': ('begins', 'began', 'begun', 'beginning'),
    'speak': ('speaks', 'spoke', 'spoken', 'speaking'), 'eat': ('eats', 'ate', 'eaten', 'eating'),
    'drink': ('drinks', 'drank', 'drunk', 'drinking'), 'sit': ('sits', 'sat', 'sat', 'sitting'),
    'stand': ('stands', 'stood', 'stood', 'standing'), 'put': ('puts', 'put', 'put', 'putting'),
    'cut': ('cuts', 'cut', 'cut', 'cutting'), 'set': ('sets', 'set', 'set', 'setting'),
    'lose': ('loses', 'lost', 'lost', 'losing'), 'win': ('wins', 'won', 'won', 'winning'),
    'teach': ('teaches', 'taught', 'taught', 'teaching'), 'know': ('knows', 'knew', 'known', 'knowing'),
    'grow': ('grows', 'grew', 'grown', 'growing'), 'fall': ('falls', 'fell', 'fallen', 'falling'),
    'break': ('breaks', 'broke', 'broken', 'breaking'), 'choose': ('chooses', 'chose', 'chosen', 'choosing'),
    'drive': ('drives', 'drove', 'driven', 'driving'), 'fly': ('flies', 'flew', 'flown', 'flying'),
    'rise': ('rises', 'rose', 'risen', 'rising'), 'wear': ('wears', 'wore', 'worn', 'wearing'),
    'build': ('builds', 'built', 'built', 'building'), 'understand': ('understands', 'understood', 'understood', 'understanding')
}
for lemma, forms in IRREGULAR.items():
    if lemma not in pos_index:
        continue
    for label, values in zip(['第三人称单数', '过去式', '过去分词', '现在分词／动名词'], forms):
        for word in values.split('/'):
            add(lemma, word, 'v', label)
for lemma, comparison in {'good': ('better', 'best'), 'bad': ('worse', 'worst'), 'well': ('better', 'best')}.items():
    if lemma in pos_index:
        for label, word in zip(['比较级', '最高级'], comparison):
            add(lemma, word, 'adv' if lemma == 'well' else 'a', label)

order = ['名词复数', '第三人称单数', '过去式', '过去分词', '现在分词／动名词', '比较级', '最高级', '现在式']
words = {}
for lemma in sorted(pos_index):
    entry = lexicon.get(lemma, {})
    words[lemma] = {
        'ph': entry.get('ph', ''),
        'common': [{k: sense[k] for k in ('m', 'p', 'count') if k in sense} for sense in entry.get('common', [])],
        'pos': sorted(pos_index[lemma]),
        'forms': [{'label': label, 'words': sorted(families[lemma][label])} for label in order if families[lemma].get(label)]
    }
by_form = collections.defaultdict(list)
for (word, lemma, pos, label), count in sorted(index.items(), key=lambda item: -item[1]):
    by_form[word].append({'lemma': lemma, 'p': pos, 'label': label, 'count': count})
output = {'words': words, 'index': dict(by_form)}
target = ROOT / 'public/english/js/word-forms.js'
target.write_text('/* Compiled from English-II corpus forms and confirmed irregular families. */\nwindow.EnglishWordForms = ' + json.dumps(output, ensure_ascii=False, separators=(',', ':')) + ';\n')
print(f'Compiled {len(words)} lemma entries and {len(by_form)} written forms ({target.stat().st_size:,} bytes).')
