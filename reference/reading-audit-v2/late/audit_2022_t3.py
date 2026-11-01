"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2022-T3')
r.lex('''
have~have~aux=构成现在完成时
all~all~adv=都
encountered~encounter~v=遇到；遭遇
in~in~prep=在……中
both~both~a=两者都
personal~personal~a=个人的
professional~professional~a=职业上的
lives~life~n=生活
think~think~v=想一想
about~about~prep=关于；围绕
times~time~n=那些经历；时候
felt~feel~v=感到
tricked~trick~v=被欺骗
frustrated~frustrate~a=心烦受挫的
by~by~prep=因为；因……而
membership~membership~n=会员服务
subscription~subscription~n=订阅服务
that~that~pron=关系词，指前面所述事物
had~have~v=具有
seamless~seamless~a=顺畅无阻的
sign-up~sign-up~n=注册；开通
process~process~n=流程
but~but~conj=但；却
was~be~v=处于所说状态
later~later~adv=后来
difficult~difficult~a=困难的
to~to~inf=不定式标记，连接动作
cancel~cancel~v=取消
something~something~pron=某件事情
should~should~aux=应当
be~be~v=是；呈现所说状态
simple~simple~a=简单的
transparent~transparent~a=透明易懂的
can~can~aux=可能
complicated~complicate~v=被弄得复杂
intentionally~intentionally~adv=有意地
unintentionally~unintentionally~adv=无意地
ways~way~n=方式
impair~impair~v=妨碍；损害
consumer~consumer~n=消费者
choice~choice~n=选择
these~these~a=这些
are~be~v=是
examples~example~n=例子
of~of~prep=……的（内容、所属或对象关系）
dark~dark~a=具有欺骗性的（dark patterns术语部分）
patterns~pattern~n=设计模式
first~first~adv=最初；首次
coined~coin~v=创造（词语）
user~user~n=用户
experience~experience~n=体验
expert~expert~n=专家
harry~Harry~name=哈里
brignull~Brignull~name=布里格纳尔
is~be~v=是
catch-all~catch-all~a=包罗多种情况的；统称性的
term~term~n=术语；称谓
for~for~prep=所指向或针对的对象
practices~practice~n=做法；设计手法
manipulate~manipulate~v=操控
interfaces~interface~n=界面
influence~influence~v=影响
decision-making~decision-making~n=决策
ability~ability~n=能力
users~user~n=用户
identifies~identify~v=列举；识别
types~type~n=类型
common~common~a=常见的
ranging~range~v=范围从……到
from~from~prep=从
misdirection~misdirection~n=误导
hidden~hide~a=隐藏的
costs~cost~n=费用
roach~roach~n=蟑螂（roach motel比喻易进难出设计）
motel~motel~n=汽车旅馆（roach motel为设计陷阱名称）
where~where~conj=引出这种设计中的具体情形
seems~seem~v=显得；看起来
easy~easy~a=容易的
intuitive~intuitive~a=直观易用的
at~at~prep=在……时
start~start~n=开始
turns~turn~v=变得
when~when~conj=当……时
tries~try~v=试图
get~get~v=离开；出去（get out）
out~out~adv=退出；离开
study~study~n=研究
product~product~n=产品
pages~page~n=页面
websites~website~n=网站
researchers~researcher~n=研究人员
found~find~v=发现
one~one~num=一个（one in ten为十分之一）
employs~employ~v=采用；使用
design~design~n=设计
though~though~conj=虽然
widely~widely~adv=广泛地
prevalent~prevalent~a=普遍存在的
concept~concept~n=概念
still~still~adv=仍然
well~well~adv=充分地
understood~understand~v=被理解
business~business~n=企业；商界
nonprofit~nonprofit~a=非营利的
leaders~leader~n=负责人
aware~aware~a=了解的；意识到的
try~try~v=努力；尽量
avoid~avoid~v=避开
 gray~gray~a=界限不明的（gray areas为灰色地带）
areas~area~n=领域；地带
engender~engender~v=产生；造成
line~line~n=界限
between~between~prep=在……二者之间
ethical~ethical~a=合乎伦理的
persuasive~persuasive~a=有说服力的
businesses~business~n=企业
engage~engage~v=开展；参与（engage in）
conversations~conversation~n=沟通；讨论
with~with~prep=与……一起
it~IT~name=信息技术（IT缩写）
compliance~compliance~n=合规
risk~risk~n=风险
legal~legal~a=法律方面的
teams~team~n=团队
review~review~v=审查
privacy~privacy~n=隐私
policy~policy~n=政策
include~include~v=将……纳入
 discussion~discussion~n=讨论
customer~customer~n=客户
designers~designer~n=设计师
coders~coder~n=程序员
responsible~responsible~a=负责的
company's~company~n=公司的
interface~interface~n=界面
as~as~conj=以及（as well as搭配）
marketers~marketer~n=营销人员
advertisers~advertiser~n=广告人员
sign-ups~sign-up~n=注册；开通
checkout~checkout~n=结账；结算
baskets~basket~n=购物篮
pricing~pricing~n=定价
promotions~promotion~n=促销
any~any~a=任何一个
play~play~v=发挥（作用）
role~role~n=作用
creating~create~v=造成；创造
avoiding~avoid~v=避免
digital~digital~a=数字化的
deception~deception~n=欺骗
lawmakers~lawmaker~n=立法者
regulators~regulator~n=监管机构
slowly~slowly~adv=逐步地
starting~start~v=开始
address~address~v=处理；应对
ambiguity~ambiguity~n=模糊地带；界限不清
around~around~prep=围绕；关于
most~much~adv=最；最近的强调程度
recently~recently~adv=最近
state~state~n=州
level~level~n=层级
march~March~n=三月
california~California~name=加利福尼亚州
attorney~attorney~n=法律官员（Attorney General整体指总检察长）
general~General~a=总的；首席的（职称部分）
announced~announce~v=宣布
approval~approval~n=批准
additional~additional~a=补充的
regulations~regulation~n=规定
under~under~prep=依据（法律）
act~Act~n=法案
ccpa~CCPA~name=加利福尼亚州消费者隐私法的简称
ensure~ensure~v=确保
consumers~consumer~n=消费者
will~will~aux=会
confused~confuse~v=感到困惑；被弄糊涂
misled~mislead~v=受到误导
seeking~seek~v=寻求
exercise~exercise~v=行使（权利）
data~data~n=数据
rights~right~n=权利
aim~aim~v=旨在
ban~ban~v=禁止
this~this~pron=禁止暗黑模式这件事
means~mean~v=意味着
prohibiting~prohibit~v=禁止
companies~company~n=企业
using~use~v=使用
confusing~confusing~a=让人困惑的
language~language~n=措辞；语言
unnecessary~unnecessary~a=不必要的
steps~step~n=步骤
such~such~a=这样的（such as表例如）
forcing~force~v=强迫
click~click~v=点击
through~through~prep=逐一经过；浏览各个页面
multiple~multiple~a=多个的
screens~screen~n=页面；屏幕
listen~listen~v=听取
reasons~reason~n=理由
why~why~conj=为什么（解释理由内容）
shouldn't~should~aux=不应该（should not，所听劝说的内容）
opt~opt~v=选择
more~more~a=更多的
states~state~n=州
consider~consider~v=考虑
promulgating~promulgate~v=颁布
there~there~pron=存在句形式词，表示有
need~need~n=需要
 greater~great~a=更强的；更多的
accountability~accountability~n=责任承担；问责
within~within~prep=在……内部
community~community~n=群体；界别
also~also~adv=也
addressed~address~v=得到处理
on~on~prep=通过；以某种基础或方式
self-regulatory~self-regulatory~a=自律的
basis~basis~n=基础；方式
only~only~adv=只有；仅
if~if~conj=如果；前提是
organizations~organization~n=组织
hold~hold~v=使保持；要求承担（hold accountable）
themselves~themselves~pron=它们自己
accountable~accountable~a=承担责任的
just~just~adv=仅仅
requirements~requirement~n=要求
industry~industry~n=行业
best~good~a=最佳的
standards~standard~n=标准
''')
r.word('P1-S4','These','这些情况','these','pron')
r.word('P1-S3','be','构成被动语态（be complicated）','be','aux',occ=2)
r.word('P2-S1','by','由（引出术语创造者）','by','prep')
r.word('P2-S2','to','从……到……的范围终点','to','prep',occ=1)
r.word('P3-S1','that','从句连接词，引出研究发现','that','conj')
r.word('P3-S1','about','大约','about','adv')
r.word('P3-S2','is','构成被动语态（is understood）','be','aux')
r.word('P3-S3','they','暗黑模式','they','pron')
r.word('P4-S1','Where','在哪里','where','adv')
r.word('P4-S2','in','参与某事（engage in）','in','prep',occ=1)
r.word('P4-S2','for','负责的对象（responsible for）','for','prep')
r.word('P4-S2','well','与as合成以及（as well as）','well','adv')
r.word('P4-S3','all','所有的','all','a')
r.word('P5-S1','are','构成现在进行时','be','aux')
r.word('P5-S2','that','从句连接词，引出确保的内容','that','conj',occ=2)
r.word('P5-S2','be','构成被动语态（be confused/misled）','be','aux')
r.word('P5-S3','as','例如（such as）','as','prep')
r.word('P5-S3','from','禁止做某事（prohibit from）','from','prep')
r.word('P5-S3','to','听取的对象（listen to）','to','prep',occ=3)
r.word('P5-S3','them','消费者','they','pron')
r.word('P5-S3','they','消费者','they','pron')
r.word('P6-S1','As','随着','as','conj')
r.word('P6-S1','is','有；存在（there is）','be','v')
r.word('P6-S1','for','所需加强的内容','for','prep')
r.word('P6-S2','be','构成被动语态（be addressed）','be','aux')
r.word('P6-S2','can','可以','can','aux')
r.word('P6-S2','to','对……负责；遵从相应标准','to','prep')
r.sentence('P1-S4')['chunks']=chunks(r,'P1-S4','','这些都是暗黑模式的例子。')
done(r,{
'P1-S1':'them回指下文暗黑模式，both将个人与工作两个领域并列，have构成完成时。',
'P1-S2':'had表示具有流程非完成时，was difficult为系表，服务易开难退是受骗烦恼原因。',
'P1-S3':'两个that都修饰事物或方式，be simple为系表而be complicated为被弄复杂。',
'P1-S4':'合并短句避免把examples拆成两个重复中文块，These为这些情况。',
'P2-S1':'coined指创造术语，catch-all为统称，manipulate为操控用户界面非一般操作。',
'P2-S2':'range from…to列出12类范围，roach motel比喻易进难退，where引出这种设计情形。',
'P3-S1':'53,000页面与11,000网站为样本，one in ten为约十分之一，employ为采用非雇用。',
'P3-S2':'虽然普遍却未充分理解，not well不译成完全不懂，understood被动。',
'P3-S3':'they指暗黑模式，engender灰色地带；负责人被要求了解并避开。',
'P4-S1':'Where疑问在哪里，line为伦理界限，persuasive不直接等同欺骗。',
'P4-S2':'IT为信息技术缩写，两处responsible for分别管设计开发与营销广告人员。',
'P4-S3':'any or all为单个或全体团队，creating与avoiding相反，数字欺骗为宾语。',
'P5-S1':'address为着手处理，state为州而非国家，最近州级行动未扩大到全国统一。',
'P5-S2':'首that修饰补充规定，第二that引ensure内容，exercise为行使权利非锻炼。',
'P5-S3':'means为动词意味着，them和they为消费者，听劝不退出是被禁止的阻碍方式。',
'P6-S1':'As为随着，community为商界群体，问责应从内部加强。',
'P6-S2':'only if为自律有效前提，to为对法律及行业标准负责，不仅依法也符合最佳实践。'})
