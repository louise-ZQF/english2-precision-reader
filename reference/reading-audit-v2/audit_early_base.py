import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'scripts'))
from reading_audit import Review,tokens
COMMON='''
of~of~prep=……的（连接修饰成分）
in~in~prep=在……中
on~on~prep=在……上
at~at~prep=在（所述地点或时点）
to~to~inf=不定式标记，引出后面的动作
for~for~prep=为了（引出目的或对象）
from~from~prep=从；来自
with~with~prep=与……一起；伴随
by~by~prep=由（引出动作执行者）
as~as~conj=当……时
but~but~conj=但是（转折）
that~that~conj=引出所说的内容，不单译
this~this~pron=这；这个（指所述事物）
it~it~pron=它；这件事（承接上文）
its~its~pron=它的
is~be~v=是；处于（联系主语与状态）
are~be~v=是；处于（联系主语与状态）
was~be~v=是；处于（过去时）
were~be~v=是；处于（过去时）
be~be~v=是；处于
been~be~aux=be的过去分词，参与完成时结构
have~have~aux=完成时助动词，不单译为“有”
has~have~aux=完成时助动词，不单译为“有”
had~have~aux=过去完成时助动词，说明此前已发生
will~will~aux=将；会（表示将来）
would~would~aux=会（表示假设或过去视角）
can~can~aux=能够；可以
could~could~aux=可能；能够（按本句语气）
may~may~aux=可能
might~might~aux=可能；也许
should~should~aux=应该
must~must~aux=必须
which~which~pron=关系代词，指前面的事物
who~who~pron=关系代词，指前面的人
when~when~conj=当……时
than~than~conj=比（引出比较对象）
if~if~conj=如果（引出条件）
because~because~conj=因为
though~though~conj=尽管；虽然
although~although~conj=尽管；虽然
while~while~conj=当……时
since~since~prep=自……以来
then~then~adv=那时；随后
all~all~det=全部；所有
any~any~det=任何；无论哪一种
some~some~det=一些；有些
other~other~a=其他的
more~more~adv=更多；更（比较程度）
most~most~adv=最（最高程度）
very~very~adv=很；非常
so~so~adv=如此；这样
no~no~det=没有；不存在
only~only~adv=仅仅；只有
also~also~adv=也；还
up~up~adv=向上；增加（按所处搭配理解）
out~out~adv=向外（按所处搭配理解）
about~about~prep=关于
into~into~prep=进入；转为
or~or~conj=或者（连接备选内容）
'''
def article(id,lex):
 r=Review(id);r.lex(COMMON);r.lex(lex);return r

def checks(r,notes):
 for s,note in zip(r.ss,notes):r.checked(s['id'],note)
 assert len(notes)==len(r.ss),(r.d['id'],len(notes),len(r.ss))

def phrase(r,sid,word,lemma,meaning):
 s=r.sentence(sid);a=s['en'].index(word);s['phrases']=[w for w in s['phrases'] if (w['a'],w['b'])!=(a,a+len(word))]+[dict(a=a,b=a+len(word),word=word,lemma=lemma,meaning=meaning)]

def gaps(r):print(r.d['id'],'MISSING',r.missing())

def inherit(r,ids):
 """Reuse already authored spellings/lemmas only as editorial candidates; all new sentences still require actual review and occurrence overrides."""
 pool={}
 for ident in ids:
  d=json.loads((ROOT/f'public/english/data/reading/{ident}.json').read_text())
  assert d.get('auditV2'),ident
  for p in d['paragraphs']:
   for s in p['sentences']:
    for w in s['words']:
     pool.setdefault(w['word'].lower(),set()).add((w['lemma'],w['pos'],w['meaning']))
 for word,opts in pool.items():
  if word not in r.map and len(opts)==1:r.map[word]=next(iter(opts))
 return r
