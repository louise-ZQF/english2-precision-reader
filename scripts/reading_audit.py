#!/usr/bin/env python3
"""Authoring helper for occurrence-complete reading reviews; never imports a dictionary sense as reviewed."""
import json,re,hashlib,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'public/english/data/reading'
PATTERN=re.compile(r'''(?<![A-Za-z0-9'’])(?:\d+(?:st|nd|rd|th)(?:[-‐‑][A-Za-z]+)+|(?:[A-Za-z]\.){2,}|[A-Za-z][A-Za-z0-9]*(?:['’][A-Za-z]+)*(?:["”]?[-‐‑][A-Za-z0-9]+(?:['’][A-Za-z]+)*)*)''')
RUNONS={"part-there's",'script-literally','figuratively-means',"anyway-aren't",'catch-up-with-household'}
def tokens(en):
 out=[]
 for m in PATTERN.finditer(en):
  if m[0].lower() in RUNONS:
   a=m.start()
   for word in m[0].split('-'):out.append(dict(a=a,b=a+len(word),word=word));a+=len(word)+1
  else:out.append(dict(a=m.start(),b=m.end(),word=m[0]))
 return out
# Only these unambiguous grammatical items can be shared. Polysemous auxiliaries,
# prepositions and relative words must be explicitly authored and checked in each article.
BASIC={
 'a':('a','art','不定冠词，指一个或某一类；通常不单译'),
 'an':('an','art','不定冠词，指一个或某一类；通常不单译'),
 'the':('the','art','定冠词，限定所说对象；通常不单译'),
 'and':('and','conj','和；并且（连接并列或承接的内容）'),
 'or':('or','conj','或者（连接可选择的内容）'),
 'not':('not','adv','不；没有（否定后面的内容）'),
 'i':('I','pron','我'), 'my':('my','pron','我的'), 'me':('I','pron','我（宾格）'),
 'our':('our','pron','我们的'), 'we':('we','pron','我们'), 'us':('we','pron','我们（宾格）'),
 'your':('your','pron','你的；你们的'), 'you':('you','pron','你；你们（也可泛指人们）'),
 'he':('he','pron','他'), 'she':('she','pron','她'), 'his':('his','pron','他的'),
 'they':('they','pron','他们；它们（承接本句所指对象）'), 'their':('their','pron','他们的；它们的'),
 'them':('they','pron','他们；它们（宾格）'),
}
class Review:
 def __init__(self,ident):
  self.path=DATA/(ident+'.json');self.d=json.loads(self.path.read_text());self.ss=[s for p in self.d['paragraphs'] for s in p['sentences']];self.map=dict(BASIC);self.patches={};self.notes=[];self.seen=set()
 def lex(self,text):
  for line in text.strip().splitlines():
   if not line.strip() or line.lstrip().startswith('#'):continue
   key,meaning=line.split('=',1);parts=[x.strip() for x in key.split('~')];word=parts[0].lower();lemma=parts[1] if len(parts)>1 and parts[1] else word;pos=parts[2] if len(parts)>2 else ''
   assert meaning.strip(),line
   self.map[word]=(lemma,pos,meaning.strip())
  return self
 def word(self,sid,word,meaning,lemma=None,pos=None,occ=None):
  s=self.sentence(sid);matches=[i for i,t in enumerate(tokens(s['en'])) if t['word'].lower()==word.lower()];assert matches,(s['id'],word)
  if occ is not None:matches=[matches[occ-1]]
  for i in matches:self.patches[(s['id'],i)]=(lemma,pos,meaning)
 def sentence(self,sid):
  return next(s for s in self.ss if s['id']==sid or s['id'].split(self.d['id']+'-')[-1]==sid)
 def checked(self,sid,note,**patch):
  s=self.sentence(sid);assert len(note.strip())>=6,(sid,'specific review note needed');self.seen.add(s['id']);s.update(patch);s['auditV2']={'date':'2026-11-01','note':note,'sentenceSHA256':hashlib.sha256(s['en'].encode()).hexdigest()}
 def missing(self):
  return sorted({t['word'].lower() for s in self.ss for i,t in enumerate(tokens(s['en'])) if t['word'].lower() not in self.map and (s['id'],i) not in self.patches})
 def save(self):
  assert not self.missing(),(self.d['id'],'unauthored words',self.missing())
  assert len(self.seen)==len(self.ss),(self.d['id'],'sentences not rechecked',set(s['id'] for s in self.ss)-self.seen)
  total=0
  for s in self.ss:
   rows=[]
   for i,t in enumerate(tokens(s['en'])):
    lemma,pos,meaning=self.map.get(t['word'].lower(),(t['word'].lower(),'',''))
    if (s['id'],i) in self.patches:
     le,po,meaning=self.patches[(s['id'],i)];lemma=le or lemma;pos=po or pos
    assert meaning and lemma and pos,(s['id'],t,'meaning, lemma and POS all required')
    rows.append({**t,'lemma':lemma,'pos':pos,'meaning':meaning,'reviewVersion':2})
   # Every visible written word has exactly one reviewed record. Phrase records
   # remain separately reviewed, and can combine these words in the interface.
   s['words']=rows;s['auditV2']['words']=len(rows);s['auditV2']['phrases']=len(s['phrases']);total+=len(rows)
  self.d['auditV2']={'version':2,'date':'2026-11-01','sourceHash':self.d['source']['textSHA256'],'sentences':len(self.ss),'wordOccurrences':total,'notes':self.notes}
  spec=importlib.util.spec_from_file_location('builder',ROOT/'scripts/build_reading.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.validate(self.d,m.expected_articles())
  self.path.write_text(json.dumps(self.d,ensure_ascii=False,indent=2)+'\n');print(self.d['id'],len(self.ss),total,'fully covered')
def inspect(ident):
 d=json.loads((DATA/(ident+'.json')).read_text());seen={}
 for p in d['paragraphs']:
  print('\n'+p['id'])
  for s in p['sentences']:
   print(s['id'],s['en']);print('译：'+s['translation']);print('序：'+s['reorder']);print('块：'+' / '.join(c['en']+'='+c['zh'] for c in s['chunks']));print('词：'+'; '.join(w['word']+'~'+w['lemma']+'~'+w.get('pos','')+'='+w['meaning'] for w in s['words']));print('组：'+'; '.join(w['word']+'='+w['meaning'] for w in s['phrases']))
   for t in tokens(s['en']):seen.setdefault(t['word'].lower(),[]).append(s['id'])
 print('\n待逐项编写（除基础语法词）：\n'+' '.join(k for k in sorted(seen) if k not in BASIC))
if __name__=='__main__':
 import sys
 inspect(sys.argv[1])
