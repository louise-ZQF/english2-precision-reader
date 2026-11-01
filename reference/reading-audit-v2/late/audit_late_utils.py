import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'scripts'))
from reading_audit import Review,tokens

def phrase(r,sid,word,meaning,lemma=None):
 s=r.sentence(sid);a=s['en'].index(word);b=a+len(word);s['phrases']=[w for w in s['phrases'] if(w['a'],w['b'])!=(a,b)]+[dict(a=a,b=b,word=word,lemma=lemma or word.lower(),meaning=meaning)]
def chunks(r,sid,starts,zh):
 s=r.sentence(sid);cs=[0];cur=0
 for marker in starts.split('|') if starts else []:
  at=s['en'].index(marker,cur+1);cs.append(at);cur=at
 cs.append(len(s['en']));zs=zh.split('|');assert len(zs)==len(cs)-1
 return [dict(a=a,b=b,en=s['en'][a:b],zh=z) for a,b,z in zip(cs,cs[1:],zs)]
def done(r,notes):
 for sid,note in notes.items():r.checked(sid,note)
 print('missing',r.d['id'],r.missing());r.save()
