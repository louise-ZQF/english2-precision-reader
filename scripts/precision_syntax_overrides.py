"""Reviewed fixes for constructions the small dependency model misreads."""
def apply_reviewed_syntax(sentence):
    en = sentence['en']
    if not en.startswith('In her new book Cogs and Monsters:') or 'Diane Coyle' not in en:
        return sentence
    book_start = en.index('Cogs and Monsters:')
    book_end = en.index(', Diane Coyle')
    appos_start = en.index('an economist')
    appos_end = en.index(', argues')
    object_start = en.index('that the digital economy')
    sentence['groups'] = [
        {'id':1,'label':'主干','head':'argues','attach':'','parent':None},
        {'id':2,'label':'前置介词状语','head':'In','attach':'argues','parent':1},
        {'id':3,'label':'书名同位说明','head':'Cogs and Monsters','attach':'book','parent':2},
        {'id':4,'label':'同位／插入说明','head':'economist','attach':'Coyle','parent':1},
        {'id':5,'label':'宾语／内容从句','head':'requires','attach':'argues','parent':1},
    ]
    for token in sentence['tokens']:
        a=token['a']
        token['g'] = 3 if book_start<=a<book_end else 2 if a<book_start else 4 if appos_start<=a<appos_end else 5 if a>=object_start else 1
    sentence['core'] = [{'role':'主语','text':'Diane Coyle'},{'role':'谓语','text':'argues'},{'role':'宾语／补足语','text':'〔⑤ 宾语／内容从句〕'}]
    sentence['reviewed'] = True
    return sentence
