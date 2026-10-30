#!/usr/bin/env python3
"""Build offline sentence boundaries, dependency groups, and context glosses.

Run with .venv/bin/python. The website itself has no spaCy runtime dependency.
"""
import collections
import hashlib
import html
import json
import re
from pathlib import Path
import spacy
import argparse
from precision_lexicon import PHRASES, COMMON, RULES
from precision_syntax_overrides import apply_reviewed_syntax

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'public/english/data'
OUT = DATA / 'precision'
OUT.mkdir(exist_ok=True)
DICT = json.loads((DATA / 'dict.json').read_text())['dict']
BANK = json.loads((DATA / 'sentence_translations.json').read_text())['items']
NLP = spacy.load('en_core_web_sm', disable=['ner'])
POS = {'NOUN':'n','PROPN':'n','VERB':'v','AUX':'v','ADJ':'a','ADV':'adv','ADP':'prep','SCONJ':'conj','CCONJ':'conj','PRON':'pron','DET':'art','NUM':'num'}
CLAUSES = {'relcl':'定语从句','advcl':'状语从句','ccomp':'宾语／内容从句','xcomp':'非谓语补充','appos':'同位／插入说明','acl':'后置修饰','parataxis':'插入／并列分句'}
COUNTS = collections.defaultdict(collections.Counter)
EVIDENCE = collections.defaultdict(dict)
SEEN_MEANINGS = set()
parser = argparse.ArgumentParser()
parser.add_argument('--exam', help='Rebuild only this exam, without changing the shared lexicon')
args = parser.parse_args()


def clean(s):
    return re.sub(r'\s+', ' ', str(s).replace('\u2018', "'").replace('\u2019', "'")).strip()


def key(s):
    return re.sub(r'[^\w\u4e00-\u9fff]', '', clean(s).lower())


TRANSLATIONS = {key(x['en']): x for x in BANK if x.get('en') and x.get('zh')}
PREFIX = collections.defaultdict(list)
for item in BANK:
    PREFIX[key(item['en'])[:26]].append(item)


def translate(text):
    k = key(text)
    if k in TRANSLATIONS:
        return TRANSLATIONS[k]['zh']
    # The original bank may include quotation marks / a longer enclosing sentence.
    if len(k) >= 26:
        for item in PREFIX.get(k[:26], []):
            ik = key(item['en'])
            if k == ik or (min(len(k),len(ik))/max(len(k),len(ik)) > .94 and (k in ik or ik in k)):
                return item['zh']
    return ''


def chunks(meaning):
    return [x.strip() for x in re.split(r'[,，;；、]', meaning) if x.strip() and not re.search('过去式|过去分词|现在分词|的复数|第三人称',x)]


def norm_pos(p):
    return 'v' if p in ('v','vt','vi') else 'a' if p in ('a','adj') else 'adv' if p in ('ad','adv') else p


def entry_for(token):
    lemma = token.lemma_.lower().strip()
    for k in (lemma, token.text.lower()):
        e = DICT.get(k)
        if e and any(chunks(s.get('t','')) for s in e.get('s',[]) if norm_pos(s.get('p')) in {'n','v','a','adv','prep','conj','pron','art','num'}):
            return k, e
    return lemma, DICT.get(lemma) or DICT.get(token.text.lower()) or {}


def sense(token, en, zh):
    lemma, entry = entry_for(token)
    pos = POS.get(token.pos_, '')
    alternatives = []
    for p, meaning in COMMON.get(lemma, []):
        if not pos or pos == p:
            alternatives.extend((fragment, p, True) for fragment in chunks(meaning))
    for s in entry.get('s', []):
        p = norm_pos(s.get('p', ''))
        if p not in {'n','v','a','adv','prep','conj','pron','art','num'} or (pos and p != pos):
            continue
        alternatives.extend((fragment,p,False) for fragment in chunks(s.get('t','')))
    if not alternatives:
        # An incomplete dictionary POS is not evidence for a different meaning.
        return lemma, '', 'missing', pos
    matches = []
    for fragment, p, curated in alternatives:
        plain = re.sub(r'的$|地$', '', re.sub(r'[（(].*?[）)]', '', fragment)).strip()
        if len(plain) >= 2 and plain in zh:
            matches.append((len(plain) + int(curated), fragment, p))
    for w, pattern, p, meaning in RULES:
        if lemma == w and pos == p and re.search(pattern,en,re.I):
            # Rule senses are explicitly lexical/POS conditioned, not a guess
            # inferred solely from a sentence's overall topic.
            if w in {'practice','approach'} and matches:
                break
            return lemma, meaning, 'rule', p
    if matches:
        _, meaning, p = max(matches, key=lambda x:x[0])
        return lemma, meaning, 'aligned', p
    if len({x[0] for x in alternatives}) == 1:
        return lemma, alternatives[0][0], 'single', alternatives[0][1]
    # Candidate is visibly labeled as such. Do not claim WSD certainty.
    chosen = list(dict.fromkeys(a[0] for a in alternatives))[:2]
    return lemma, '；'.join(chosen), 'candidate', pos


def serialize_sentence(sent, offset, exam_id):
    text = sent.text
    start = sent.start_char
    zh = translate(text)
    toks = list(sent)
    index = {t.i:i for i,t in enumerate(toks)}
    clause_heads = []
    for t in toks:
        dep = t.dep_
        if dep in CLAUSES or (dep == 'conj' and t.pos_ in {'VERB','AUX'} and any(c.dep_ in {'nsubj','nsubjpass','csubj'} for c in t.children)):
            nodes = {x.i for x in t.subtree if x.i in index}
            if len(nodes) >= 2:
                clause_heads.append((t, nodes, CLAUSES.get(dep,'并列分句')))
    clause_heads.sort(key=lambda x:min(x[1]))
    groups = [{'id':1,'label':'主干','head':sent.root.text,'attach':'','parent':None}]
    token_groups = {t.i:1 for t in toks}
    group_for_head = {}
    for n,(t,nodes,label) in enumerate(clause_heads,2):
        group_for_head[t.i] = n
        groups.append({'id':n,'label':label,'head':t.text,'attach':t.head.text,'parent':1})
    # Smaller/deeper subtrees supersede enclosing clauses. A group can occur in
    # multiple separated spans and is always given the same number and color.
    for t,nodes,label in sorted(clause_heads,key=lambda x:len(x[1]),reverse=True):
        g = group_for_head[t.i]
        for i in nodes:
            token_groups[i] = g
    for g,(t,nodes,label) in zip(groups[1:], clause_heads):
        g['parent'] = token_groups.get(t.head.i,1)
        if g['parent'] == g['id']:
            g['parent'] = 1
    tokens = []
    for t in toks:
        lemma, meaning, confidence, pos = sense(t,text,zh) if re.search('[A-Za-z]',t.text) else ('','','', '')
        occurrence = (exam_id, text, lemma, meaning, pos)
        if meaning and confidence in {'aligned','rule','single'} and t.pos_ not in {'DET','PRON','AUX','ADP','CCONJ','SCONJ'} and occurrence not in SEEN_MEANINGS:
            SEEN_MEANINGS.add(occurrence)
            COUNTS[lemma][(meaning,pos)] += 1
            EVIDENCE[lemma].setdefault(meaning, {'exam':exam_id,'en':text,'zh':zh})
        tokens.append({'a':t.idx-start,'b':t.idx-start+len(t),'w':t.text,'l':lemma,'p':pos,'d':t.dep_,'h':index.get(t.head.i,index[t.i]),'g':token_groups[t.i], 'm':meaning,'q':confidence})
    root = sent.root
    subjects = [t for t in root.children if t.dep_ in {'nsubj','nsubjpass','csubj','expl'}]
    objects = [t for t in root.children if t.dep_ in {'dobj','attr','oprd','acomp','dative','ccomp','xcomp'}]
    def main_text(t):
        children = sorted((x for x in t.subtree if x.i in index and token_groups[x.i] == 1 and not x.is_punct),key=lambda x:x.i)
        return ' '.join(x.text for x in children)
    verb = ' '.join(t.text for t in sorted([root] + [x for x in root.children if x.dep_ in {'aux','auxpass','neg','prt'}],key=lambda t:t.i))
    core = []
    if subjects:
        core.append({'role':'主语','text':' / '.join(main_text(t) or t.text for t in subjects)})
    core.append({'role':'谓语','text':verb})
    for t in objects:
        gid = group_for_head.get(t.i)
        core.append({'role':'宾语／补足语','text':('〔'+str(gid)+' '+groups[gid-1]['label']+'〕') if gid else (main_text(t) or t.text)})
    return apply_reviewed_syntax({'a':start-offset,'b':sent.end_char-offset,'en':text,'zh':zh,'tokens':tokens,'groups':groups,'core':core})


def strings(obj):
    if isinstance(obj,str):
        if len(obj.strip()) > 1 and re.search('[A-Za-z]',obj):
            yield clean(obj)
    elif isinstance(obj,list):
        for x in obj:yield from strings(x)
    elif isinstance(obj,dict):
        for k,v in obj.items():
            if k not in {'exam_id','section_id','text_id','q_num','year','subject','code','title'}:
                yield from strings(v)


def repair_paragraphs(paragraphs):
    out = []
    for p in paragraphs:
        p=clean(p)
        if out and not re.search(r"""[.!?](?:\s*["'\u201d\u2019)\]])*$""",out[-1]):
            out[-1] += ' '+p
        else:out.append(p)
    return out


all_data = []
for file in sorted(DATA.glob('exam_*_english2.json')):
    if args.exam and file.stem != 'exam_' + args.exam:
        continue
    exam = json.loads(file.read_text())
    blocks = set(strings(exam))
    def add_passages(obj):
        if isinstance(obj,dict):
            for k,v in obj.items():
                if k=='passage' and isinstance(v,str):
                    blocks.update(repair_paragraphs(v.split('\n\n')))
                add_passages(v)
        elif isinstance(obj,list):
            for v in obj:add_passages(v)
    add_passages(exam)
    for section in exam.get('sections',[]):
        for part in section.get('parts',[]):
            for article in part.get('texts',[]):
                blocks.update(repair_paragraphs(article.get('paragraphs',[])))
    for raw in list(blocks):
        stripped = re.sub(r'\s*\|\s*(?:[\[(]\s*([A-Ha-h])\s*[\])]|([A-Ha-h]))\s*([.、．)）]?)\s*', lambda m:' ' if m[1] or not m[3] else '. ', raw)
        stripped = re.sub(r'^\s*(?:[\[（(]\s*[A-Ha-h]\s*[\]）)][.、．]?|[A-Ha-h]\s*[.、．)）])\s*', '', stripped)
        blocks.add(clean(stripped))
    ordered = sorted(blocks)
    lookup = {}
    for raw,doc in zip(ordered,NLP.pipe(ordered,batch_size=48)):
        lookup[raw] = [serialize_sentence(sent,0,exam['exam_id']) for sent in doc.sents]
    output = {'exam':exam['exam_id'],'engine':'spaCy en_core_web_sm 3.8.0','blocks':lookup}
    (OUT/(exam['exam_id']+'.json')).write_text(json.dumps(output,ensure_ascii=False,separators=(',',':')))
    all_data.append(output)
    print(exam['exam_id'],len(lookup),'blocks',sum(len(x) for x in lookup.values()),'sentences',flush=True)

if args.exam:
    raise SystemExit(0)

lexicon = {}
for lemma,entry in DICT.items():
    if ' ' in lemma:continue
    measured = COUNTS.get(lemma,{})
    common=[]
    for (meaning,pos),count in sorted(measured.items(),key=lambda x:-x[1])[:3]:
        common.append({'m':meaning,'p':pos,'count':count,'example':EVIDENCE[lemma][meaning]})
    if not common:
        for pos,meaning in COMMON.get(lemma,[])[:2]:
            common.append({'m':meaning,'p':pos,'count':0})
    if not common:
        order=entry.get('rk',[]) or list(range(len(entry.get('s',[]))))
        for i in order:
            if i >= len(entry.get('s',[])):continue
            sense_=entry['s'][i];pos=norm_pos(sense_.get('p',''))
            if pos not in {'n','v','a','adv','prep','conj','pron','art','num'}:continue
            bits=chunks(sense_.get('t',''))[:2]
            if bits:common.append({'m':'；'.join(bits),'p':pos,'count':0})
            if len(common)==2:break
    if common:lexicon[lemma]={'ph':entry.get('ph',''),'common':common}
(OUT/'lexicon.json').write_text(json.dumps({'phrases':PHRASES,'words':lexicon,'engine':'spaCy en_core_web_sm 3.8.0','note':'语境义基于本句词性、译文匹配及明确词汇规则；候选义单独标注。次数为英语二语境匹配次数，非人工义项统计。'},ensure_ascii=False,separators=(',',':')))
(DATA.parent/'js/precision-phrases.js').write_text('/* Generated from scripts/precision_lexicon.py; available before JSON loading. */\nwindow.EnglishPhraseBank = '+json.dumps(PHRASES,ensure_ascii=False,separators=(',',':'))+';\n')
print('DONE',len(lexicon),'words;',len(PHRASES),'phrases',flush=True)
