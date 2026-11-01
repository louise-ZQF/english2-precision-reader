"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2020-T1')
r.lex('''
rats~rat~n=老鼠
other~other~a=其他的
animals~animal~n=动物
need~need~v=需要
 to~to~inf=不定式标记，连接要做的动作
be~be~v=处于所说的状态
highly~highly~adv=高度地；十分
attuned~attune~a=敏锐察觉并回应的
social~social~a=社交的；会进行社交互动的
signals~signal~n=社交信号
from~from~prep=来自
others~other~pron=其他个体
so~so~conj=这样一来；从而
can~can~aux=能够
identify~identify~v=辨认出
friends~friend~n=伙伴；朋友
cooperate~cooperate~v=合作
with~with~prep=与……一起
enemies~enemy~n=敌人
avoid~avoid~v=避开；躲避
find~find~v=查明（与out连用）
out~out~adv=弄清楚（find out的一部分）
if~if~conj=是否
this~this~pron=这种识别社交信号的能力
extends~extend~v=延伸；也适用
non-living~non-living~a=非生命的
beings~being~n=存在的个体；对象
laleh~Laleh~name=拉莱（研究者名字）
quinn~Quinn~name=奎因（研究者姓氏）
at~at~prep=任职于；在
university~university~n=大学
of~of~prep=……的（表示所属或关系）
california~California~name=加利福尼亚
san~San~name=圣（San Diego地名的一部分）
diego~Diego~name=迭戈（San Diego地名的一部分）
her~her~pron=她的
colleagues~colleague~n=同事
tested~test~v=测试；检验
whether~whether~conj=是否
detect~detect~v=识别；察觉
robotic~robotic~a=机器制成的；机器人式的
housed~house~v=把……安置在一起饲养
eight~eight~num=八
adult~adult~a=成年的
two~two~num=两
types~type~n=类型
rat~rat~n=老鼠
one~one~pron=一种（机器鼠）
asocial~asocial~a=不进行社交互动的
for~for~prep=持续（所说的时间）
four~four~num=四
days~day~n=天
robot~robot~n=机器人；这里指机器鼠
were~be~v=处于所说的状态
quite~quite~adv=相当；十分
minimalist~minimalist~a=设计极简的
resembling~resemble~v=看起来像
chunkier~chunky~a=更粗厚的
version~version~n=版本；形态
computer~computer~n=电脑
mouse~mouse~n=鼠标
wheels~wheel~n=轮子
move~move~v=移动
around~around~adv=四处
colourful~colourful~a=彩色的
markings~marking~n=外部花纹；标记
during~during~prep=在……期间
experiment~experiment~n=实验
followed~follow~v=跟随
living~living~a=活的；真实的
played~play~v=玩耍
same~same~a=同样的
toys~toy~n=玩具
opened~open~v=打开
cage~cage~n=笼子
doors~door~n=门
let~let~v=让
trapped~trap~v=被困住的；被关住的
escape~escape~v=逃出
meanwhile~meanwhile~adv=与此同时
simply~simply~adv=只是
moved~move~v=移动
forwards~forward~adv=向前
backwards~backward~adv=向后
side~side~n=一侧（side to side指左右）
next~next~adv=接下来
researchers~researcher~n=研究人员
robots~robot~n=机器人；这里指机器鼠
in~in~prep=在……里面
cages~cage~n=笼子
gave~give~v=给予
opportunity~opportunity~n=机会
release~release~v=放出；解救
by~by~prep=通过
pressing~press~v=按压
lever~lever~n=操纵杆；杠杆
across~across~prep=在……全部试验中
trials~trial~n=试验轮次
each~each~pron=每一只（参与试验的老鼠）
per~per~prep=每（per cent构成百分比）
cent~cent~n=百分之一（per cent表示百分比）
more~more~adv=更；程度更高
likely~likely~a=有可能的
on~on~prep=用于on average，表示平均而言
average~average~n=平均（on average表示平均而言）
set~set~v=使处于某状态（set free指放走）
free~free~a=自由的；不再被关着的
than~than~conj=比；与……相比
suggests~suggest~v=表明；提示
that~that~conj=引导所表明的内容，不单译
perceived~perceive~v=把……看作
as~as~prep=作为；视为
genuine~genuine~a=真正的
being~being~n=个体；伙伴
says~say~v=说；指出
may~may~aux=可能
have~have~aux=构成完成时，不单译
bonded~bond~v=建立亲近关系
because~because~conj=因为
it~it~pron=它（机器鼠）
displayed~display~v=表现出
behaviors~behavior~n=行为
like~like~prep=例如；像
communal~communal~a=共同进行的
exploring~explore~v=探索
playing~play~v=玩耍
could~could~aux=可能
lead~lead~v=导致；使产生（与to连用）
better~well~adv=更清楚地
remembering~remember~v=记得
having~have~aux=构成完成式，表示先前已做
freed~free~v=放出；解救
earlier~early~adv=此前
wanting~want~v=希望
return~return~v=回报
favour~favour~n=帮助；恩惠
when~when~conj=当……时
get~get~aux=构成被动状态，表示被困住
been~be~aux=与shown构成被动语态
shown~show~v=被研究证明；被显示
engage~engage~v=参与；进行（与in连用）
multiple~multiple~a=多种的
forms~form~n=形式
reciprocal~reciprocal~a=相互的；互惠的
help~help~n=帮助
cooperation~cooperation~n=合作
including~including~prep=包括
what~what~pron=所称的事物；所说的那种形式
is~be~aux=构成被动语态
referred~refer~v=被称为（refer to as）
direct~direct~a=直接的
reciprocity~reciprocity~n=互惠；相互回报
where~where~conj=引出直接互惠的具体情形
will~will~aux=会
another~another~a=另一只
has~have~aux=构成现在完成时
previously~previously~adv=先前；以前
helped~help~v=帮助过
readiness~readiness~n=乐意；积极意愿
befriend~befriend~v=与……交朋友
was~be~v=是；呈现所说的状态
surprising~surprising~a=令人吃惊的
given~given~prep=考虑到；鉴于
its~its~pron=它的（机器鼠的）
minimal~minimal~a=极其简约的
design~design~n=设计
size~size~n=大小
regular~regular~a=普通的
but~but~conj=但是
resembled~resemble~v=看起来像
simple~simple~a=简单的
plastic~plastic~a=塑料制的
box~box~n=盒子
we'd~we would~aux=我们原本会需要（we would的缩写）
assumed~assume~v=原以为
 give~give~v=给……装上
moving~move~a=能动的
head~head~n=头
tail~tail~n=尾巴
facial~facial~a=面部的
features~feature~n=外形特征
put~put~v=放上；添加
scent~scent~n=气味
make~make~v=使；让
smell~smell~v=闻起来
real~real~a=真实的
wasn't~be~v=并非；并不（was not）
necessary~necessary~a=必要的
janet~Janet~name=珍妮特（研究者名字）
wiles~Wiles~name=怀尔斯（研究者姓氏）
queensland~Queensland~name=昆士兰
 Australia~Australia~name=澳大利亚
who~who~pron=关系词，指代前面的研究者
research~research~n=研究
finding~finding~n=研究发现
shows~show~v=表明
how~how~adv=多么（强调敏感程度）
sensitive~sensitive~a=敏感的；善于察觉的
are~be~v=处于所说的状态
cues~cue~n=社交线索；信号
even~even~adv=即使（与when连用表示让步）
come~come~v=来自；产生
basic~basic~a=结构简单的
similarly~similarly~adv=同样地
children~child~n=孩子
tend~tend~v=往往；倾向于
treat~treat~v=对待
fellow~fellow~a=同类的
 display~display~v=表现出
only~only~adv=仅；只
humans~human~n=人类
seem~seem~v=似乎
fascinated~fascinate~a=着迷的；被吸引的
turns~turn~v=结果是；事实证明（turn out）
too~too~adv=也一样
''')
r.word('P1-S1','to','对；对于（attuned to搭配）','to','prep',occ=2)
r.word('P1-S2','To','为了；表目的','to','inf',occ=1)
r.word('P1-S2','to','也适用于的对象（extend to）','to','prep',occ=2)
r.word('P2-S2','with','带有；装着','with','prep')
r.word('P3-S1','with','玩耍所用的对象（play with）','with','prep')
r.word('P6-S3','with','帮助进行（help with）','with','prep')
r.word('P3-S2','to','到另一侧（side to side表示左右来回）','to','prep')
r.word('P4-S2','one','那一只机器鼠（代前面的asocial robot）','one','pron')
r.word('P4-S3','being','个体；这里指具有社交性的伙伴','being','n')
r.word('P4-S5','to','导致的结果（lead to搭配）','to','prep',occ=1)
r.word('P5-S1','help','帮助','help','v')
r.word('P5-S1','that','关系代词，指先前帮过自己的另一只老鼠','that','pron')
r.word('P5-S1','is','构成被动语态（is referred to as）','be','aux')
r.word('P5-S1','to','refer to as的一部分，表示称作','to','prep',occ=2)
r.word('P5-S1','in','engage in的一部分，表示进行','in','prep')
r.word('P6-S2','as','与……同样（the same size as）','as','conj')
r.word('P6-S2','on','装有；由轮子支撑','on','prep')
r.word('P6-S3',"We'd",'我们此前已经（we had，构成过去完成时）','we had','aux',occ=1)
r.word('P6-S3','have','不得不（have to的一部分）','have','v')
r.word('P6-S3','to','表示必须做的动作（have to）','to','inf',occ=1)
r.word('P6-S3','on','在……上','on','prep')
r.word('P6-S3','that','那一套复杂设计','that','pron')
r.word('P7-S1','they','这些社交信号','they','pron')
r.word('P7-S1','to','对……敏感（sensitive to搭配）','to','prep')
r.word('P7-S2','as','仿佛（as if的一部分）','as','conj')
r.word('P7-S2','if','仿佛（as if的一部分）','if','conj')
r.word('P7-S2','they','机器人','they','pron')
r.word('P7-S3','by','使……着迷的对象；被……吸引','by','prep')
r.word('P7-S3','it','形式主语，指后面动物也会着迷这一发现','it','pron')
r.word('P7-S3','out','turn out搭配，表示结果发现','out','adv')
done(r,{
'P1-S1':'合作伙伴与敌人两类对象对应两个不定式；attuned to的介词与need to分开。',
'P1-S2':'this回指识别社交信号的能力；to find是目的、extends to是适用范围。',
'P2-S1':'八只真鼠、两类机器鼠、四天的数量及housed饲养义均保持。',
'P2-S2':'mouse为电脑鼠标；with表示带轮子而非与轮子合作，极简不是最低主义。',
'P3-S1':'会社交机器鼠三项行为并列，trapped修饰被困真鼠，let后为逃出。',
'P3-S2':'仅前后左右移动对比社交行为；side to side为左右来回。',
'P4-S1':'被放出的them指机器鼠；by pressing是释放方式，不是由杠杆研究。',
'P4-S2':'52%为相对可能性增幅而非52个百分点，each指每只真鼠。',
'P4-S3':'perceived as是看作；genuine social being指社交伙伴而非单纯生命物体。',
'P4-S4':'may保留可能性；it为机器鼠，communal表共同探索和玩耍。',
'P4-S5':'记得先前解救与期待回报并列；自己被困为期望机器鼠回报的时间。',
'P5-S1':'have been shown为研究被证明；that指曾帮助自己的另一只鼠，them回指施助鼠。',
'P6-S1':'given为鉴于，minimal design是惊讶的背景，readiness为乐意并非准备程度。',
'P6-S2':'same size as比较大小，on wheels为装有轮子，与普通鼠外观不相同。',
'P6-S3':'首个We’d为had，第二个为would；have to义务与that指复杂设计分别核清。',
'P7-S1':'how强调敏感程度，they回指线索；原卷句点不据此丢掉说话人。',
'P7-S2':'as if为仿佛，两个they都指机器人；只简单信号为让步。',
'P7-S3':'be fascinated by为着迷，turns out表事实发现，too指其他动物也着迷。'})
