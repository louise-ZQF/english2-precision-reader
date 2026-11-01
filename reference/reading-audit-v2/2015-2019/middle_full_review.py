# -*- coding: utf-8 -*-
import sys,json,re
from pathlib import Path
ROOT=Path('/Users/huyawen/Desktop/英语二/考研英语本地版');sys.path.insert(0,str(ROOT/'scripts'))
from reading_audit import Review,tokens
COMMON='''
this/pron=这；本句所说的事物;it/pron=它；这件事;its/det=它的;these/pron=这些;those/pron=那些人或事物;another/det=另一个;other/det=其他的;all/det=所有的;both/det=两者都;any/det=任何一个;some/det=一些;many/det=许多;more/adv=更；更多;most/adv=最；大多数;much/adv=很大程度；很多;less/adv=更少;only/adv=仅仅；只有;even/adv=甚至;still/adv=仍然;also/adv=也;just/adv=只是;very/adv=非常;so/adv=如此;than/conj=比（引出比较对象）;but/conj=但是;because/conj=因为;when/conj=当……时;if/conj=如果;whether/conj=是否;while/conj=当……时;then/adv=然后;there/adv=存在结构的引导词，本身不单译;now/adv=现在;at/prep=在（地点、时刻或状态）;in/prep=在……中;on/prep=关于；在……方面;of/prep=……的;from/prep=从；来自;with/prep=带有；与……一起;without/prep=没有；不具备;between/prep=在……之间;into/prep=进入……;about/prep=关于;before/prep=在……之前;after/prep=在……之后;to/inf=不定式标记，连接后面的动作；不单译;for/prep=为了；针对;as/prep=作为;that/conj=引出后面的内容；通常不单译;which/pron=关系代词，指代前述事物;who/pron=关系代词，指代前述的人;what/pron=所……的内容;how/adv=如何;why/adv=为什么;where/adv=在……的地方;is@be/v=是；处于所述状态;are@be/v=是；处于所述状态;was@be/v=是；处于所述状态（过去）;were@be/v=是；处于所述状态（过去）;be/v=是；处于所述状态;been@be/aux=完成时中的be；承接后面的状态或语态;being@be/aux=be的-ing形式；承接后面的状态;have/aux=构成完成时，不单独译为“有”;has@have/aux=构成完成时，不单独译为“有”;had@have/aux=构成过去完成时，不单独译为“有”;do/aux=助动词，辅助表达否定、疑问或强调;does@do/aux=助动词，辅助表达否定、疑问或强调;can/aux=能；能够;could/aux=可能；能够;may/aux=可能;might/aux=可能;will/aux=将会;would/aux=会（表示假设或过去将来）;should/aux=应该;must/aux=必须;no/det=没有;never/adv=从不；绝不;really/adv=真正地;often/adv=经常;such/det=这样的;people/person/n=人们
'''.replace('people/person/n','people@person/n')
def lex(r,s):
 for item in re.split(r';|；(?=[^;；\n=]{1,70}/[A-Za-z]+=)',s.replace('\n',';')):
  if not item.strip():continue
  k,v=item.split('=',1);form,p=k.strip().rsplit('/',1)
  w,lemma=form.split('@',1) if '@'in form else (form,form)
  r.lex(f'{w}~{lemma}~{p}={v.strip()}')
 return r
def make(id):
 r=Review(id);lex(r,COMMON);return r
def checks(r,text):
 rows=[x.strip() for x in text.strip().splitlines() if x.strip()];assert len(rows)==len(r.ss),(r.d['id'],len(rows),len(r.ss))
 for s,n in zip(r.ss,rows):r.checked(s['id'],n)
def ph(r,sid,word,lemma,meaning):
 s=r.sentence(sid);a=s['en'].index(word);row=dict(a=a,b=a+len(word),word=word,lemma=lemma,meaning=meaning,reviewVersion=2)
 s['phrases']=[x for x in s['phrases']if(x['a'],x['b'])!=(row['a'],row['b'])]+[row]
def merge(r,sid,first,last,zh):
 s=r.sentence(sid);cs=s['chunks'];a=cs[first]['a'];b=cs[last]['b'];s['chunks']=cs[:first]+[dict(a=a,b=b,en=s['en'][a:b],zh=zh)]+cs[last+1:]
def showmissing(r):
 print(r.d['id'],'missing:',r.missing())
def save(r):
 if r.missing():showmissing(r);raise ValueError('未编写全部词义')
 r.save()
def reuse(r,ids):
 # Reuse only the already-authored, invariant entries explicitly selected by the
 # reviewer. This is an authoring aid; the new article is still read in full and
 # each different use is patched by position before checked/save.
 seen={}
 for id in ids:
  d=json.loads((ROOT/f'public/english/data/reading/{id}.json').read_text())
  for p in d['paragraphs']:
   for s in p['sentences']:
    for w in s['words']:
     if w.get('reviewVersion')==2:seen.setdefault(w['word'].lower(),set()).add((w['lemma'],w['pos'],w['meaning']))
 for word,choices in seen.items():
  if len(choices)==1 and word not in r.map:r.map[word]=next(iter(choices))
 return r
def worksheet(r):
 for s in r.ss:
  print(s['id'].split(r.d['id']+'-')[1],s['en']);print('译',s['translation']);print('块',' / '.join(c['en']+'='+c['zh'] for c in s['chunks']));print('词',';'.join(t['word']+'='+r.map.get(t['word'].lower(),('','','待编写'))[2] for t in tokens(s['en'])))
 print('MISSING',' '.join(r.missing()))
