from audit_early_base import *
r=article('2013-T4','''
europe~Europe~name=欧洲
gender-equality~gender-equality~n=性别平等（作天堂的定语）
heaven~heaven~n=理想之地；乐园
particular~particular~a=特别的（in particular为尤其）
corporate~corporate~a=企业的
workplace~workplace~n=职场
completely~completely~adv=完全地
family-friendly~family-friendly~a=有利于兼顾家庭的
senior~senior~a=高层的
management~management~n=管理层；管理
europe's~Europe~name=欧洲的
top~top~a=最高层的
corporate-governance~corporate-governance~n=公司治理（作职位的定语）
positions~position~n=职位；席位
overwhelmingly~overwhelmingly~adv=绝大多数地
male~male~a=男性的
hold~hold~v=占据（席位）
per~per~prep=每（per cent整体为百分比）
cent~cent~n=百分之一（per cent）
boards~board~n=董事会
considering~consider~v=考虑
legislation~legislation~n=立法
compel~compel~v=强制要求
maintain~maintain~v=保持
proposed~propose~a=拟议的
mandate~mandate~n=强制规定
born~bear~v=产生；源自（born of）
frustration~frustration~n=挫败感
vice~vice~a=副的（副主席的头衔）
president~president~n=主席
viviane~Viviane~name=薇薇安
reding~Reding~name=雷丁（姓氏）
issued~issue~v=发出
call~call~n=呼吁
voluntary~voluntary~a=自愿的
action~action~n=行动
sign~sign~v=签约承诺（sign up for）
balance~balance~n=平衡
 goals~goal~n=目标
membership~membership~n=成员构成；成员身份
appeal~appeal~n=呼吁
failure~failure~n=失败
quotas~quota~n=配额；规定的名额比例
climb~climb~v=攀升；晋升
ladder~ladder~n=阶梯（企业晋升阶梯）
fairly~fairly~adv=公平地
personally~personally~adv=就个人而言
like~like~v=喜欢
what~what~pron=所……的事物（配额带来的作用）
get~get~v=促成；带来
break~break~v=打破；突破
glass~glass~n=玻璃（glass ceiling借喻无形晋升障碍）
ceiling~ceiling~n=天花板（比喻晋升障碍）
seen~see~v=见到；出现
binding~binding~a=有约束力的
provisions~provision~n=法律规定
placing~place~v=安排进入（职位）
understand~understand~v=理解
reding's~Reding~name=雷丁的
reluctance~reluctance~n=不情愿；顾虑
either~either~adv=也（用于否定句）
run~run~v=与counter to构成相违背
counter~counter~adv=相反；与……相违背
meritocracy~meritocracy~n=按能力与业绩选拔的制度
governance~governance~n=治理；管理
capable~capable~a=有能力的
considers~consider~v=考虑
obstacles~obstacle~n=障碍
achieving~achieve~v=实现
meritocratic~meritocratic~a=按能力与业绩选拔的
fairer~fair~a=更公平的
ordered~order~v=以强制规定促成
shown~show~v=表明
evading~evade~v=回避落实
hiring~hire~n=聘用
promotion~promotion~n=晋升；提拔
matter~matter~n=no matter how中的成分，整体为无论多少
soft~soft~a=非强制性的
pressure~pressure~n=压力
upon~upon~prep=对；向（施压对象）
summit~summit~n=权力顶峰
power~power~n=权力
sheryl~Sheryl~name=谢丽尔
sandberg~Sandberg~name=桑德伯格（姓氏）
facebook~Facebook~name=脸书
attract~attract~v=吸引
massive~massive~a=巨大的
attention~attention~n=关注
policies~policy~n=政策
ceos~CEO~n=首席执行官
caregivers~caregiver~n=照料者
newsworthy~newsworthy~a=有新闻价值的
person~person~n=人
just~just~a=公平公正的
''')
ids=[f'{y}-T{t}' for y in range(2010,2013) for t in range(1,5)]+['2013-T1','2013-T2','2013-T3'];inherit(r,ids)
r.word('P1-S2','are','成为；参与（part of）',lemma='be',pos='v');r.word('P1-S3','on','在（董事会中）',pos='prep')
r.word('P2-S1','is','进行时助动词（is considering）',lemma='be',pos='aux');r.word('P2-S1','to','到；达（up to 60%）',pos='prep',occ=3)
r.word('P2-S2','was','被动助动词（was born）',lemma='be',pos='aux')
r.word('P2-S3','to','对行动的呼吁（call to action）',pos='prep')
r.word('P2-S4','for','承诺参加（sign up for）的搭配成分',pos='prep');r.word('P2-S4','up','与sign构成承诺加入',pos='part')
r.word('P2-S5','was','被动助动词（was considered）',lemma='be',pos='aux');r.word('P2-S5','took','响应（took up）',lemma='take',pos='v');r.word('P2-S5','up','与took构成响应',pos='part')
r.word('P3-S1','do','一般现在时疑问助动词，不单译',lemma='do',pos='aux');r.word('P3-S1','as','在……同时（女性兼顾工作家庭）',pos='conj');r.word('P3-S1','balance','兼顾；平衡（工作与家庭）',lemma='balance',pos='v')
r.word('P4-S2','do','产生；带来（配额的作用）',lemma='do',pos='v')
r.word('P4-S3','they','它们（配额）',lemma='they',pos='pron');r.word('P4-S3','to','通往（平等）',pos='prep',occ=1);r.word('P4-S3','to','according to中的依据介词',pos='prep',occ=2);r.word('P4-S3','through','打破；突破（break through搭配成分）',pos='part');r.word('P4-S3','on','关于（有关女性任高层的规定）',pos='prep')
r.word('P5-S2','by','由（治理者）',pos='prep');r.word('P5-S2','the','使capable名词化，指有能力的人',pos='art')
r.word('P5-S3','does','强调助动词，表示确实',lemma='do',pos='aux');r.word('P5-S3','be','被动助动词（be ordered）',lemma='be',pos='aux');r.word('P5-S3','to','实现……的障碍（obstacles to）',pos='prep')
r.word('P6-S1','are','进行时助动词（are evading）',lemma='be',pos='aux');r.word('P6-S1','to','向；进入（高层职位）',pos='prep');r.word('P6-S1','is','被动助动词（is put）',lemma='be',pos='aux')
r.word('P6-S2','do','强调助动词，表示确实',lemma='do',pos='aux');r.word('P6-S2','did','代替前文突破到高层的助动词',lemma='do',pos='aux');r.word('P6-S2','to','到（权力顶峰）',pos='prep',occ=1);r.word('P6-S2','to','相对于（常态的例外）',pos='prep',occ=2)
r.word('P7-S1','were','虚拟条件中的系动词，假如政策已经就位',lemma='be',pos='v');r.word('P7-S1','no','不（no more ... than为并不更……）',pos='adv');r.word('P7-S1','whether','无论……还是……（涵盖两类女性）',pos='conj')
checks(r,[
'欧洲并非平等天堂，heaven为比喻而非宗教论述。',
'职场家庭友好有待女性参与高管决策，当前高层男性占绝大多数，never until不漏否定。',
'14%为女性董事会席位比例，hold占据席位非举行会议。',
'正考虑立法并非已经实施；up to原文最高60%，不擅改成最低60%。',
'mandate拟议强制规定，born of源自挫败感，不是出生地点。',
'President欧委会主席头衔非大学校长；呼吁为自愿行动。',
'40%为先前自愿目标，sign up for承诺参加，不混到后述60%上限。',
'只有24企业响应说明失败，took it up非拿起实物。',
'Do为问句助动词；配额是否需要的疑问与女性兼顾家庭晋升的目的完整。',
'个人不喜欢配额，保留引语而非作者断言所有人反对。',
'what quotas do为配额带来效果，do为实义动词，不是疑问助动。',
'打破玻璃天花板指晋升壁垒；法律有约束力，placing女性进入高层。',
'作者理解不情愿及挫败两者，不是只理解其中之一。',
'meritocracy为任人唯贤，governance一般治理而非仅公司治理。',
'does强调确实，ordered为以规定暂时促成，非订购或排序。',
'四十年证据支持作者指责；no matter how让步，soft非强制压力。',
'巨大关注因为仍为少数例外，because不用于解释女性成功原因。',
'were和would虚拟条件，不宣称政策已到位；no more newsworthy并不比别人更值得报道。'])
r.lex('''
board~board~n=董事会
corporations~corporation~n=企业
equality~equality~n=平等
example~example~n=例子
family~family~n=家庭
four~four~num=四
how~how~adv=多少（no matter how much）
ideal~ideal~n=理想
indeed~indeed~adv=的确
last~last~a=上一年的
living~live~v=生活在
much~much~det=多少（软性压力）
need~need~v=需要
one~one~pron=人们（泛指考虑问题的人）
open~open~v=开辟
public~public~a=公共的
recently~recently~adv=最近
said~say~v=说
society~society~n=社会
through~through~part=突破（break through搭配成分）
way~way~n=道路；通道
women~woman~n=女性
work~work~n=工作
world~world~n=世界
year~year~n=年
''')
r.word('P2-S1','certain','一定的（比例）',pos='det')
r.word('P7-S1','their','她们的（女性的孩子）',lemma='their',pos='pron')
r.word('P2-S1','up','up to搭配表示“最高达；多达”',lemma='up',pos='adv')
gaps(r)
if not r.missing():r.save()
