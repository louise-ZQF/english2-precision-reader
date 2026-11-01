"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2022-T2')
r.lex('''
more~more~a=更多的
americans~American~n=美国人
are~be~aux=构成现在进行时
opting~opt~v=选择
to~to~inf=不定式标记，连接要做的动作
work~work~v=工作
well~well~adv=远远地；很长一段时间
into~into~prep=进入并持续到（退休时期）
retirement~retirement~n=退休；退休生活
growing~grow~a=不断扩大的
trend~trend~n=趋势
that~that~pron=关系代词，指前述趋势
threatens~threaten~v=可能导致；有……的势头
upend~upend~v=颠覆
old~old~a=传统的
workforce~workforce~n=劳动力人口
model~model~n=模式
one~one~num=一人；一个
in~in~prep=在……人群或时期中
three~three~num=三
who~who~pron=关系代词，指前述的人
at~at~prep=与least连用，表示至少
least~little~adv=最低限度（at least为至少）
have~have~v=拥有；从事（工作）
plan~plan~v=计划
job~job~n=工作
prepare~prepare~v=作准备
for~for~prep=为……作准备
longer~long~a=更长的
life~life~n=寿命；人生
according~according~prep=与to连用表示根据
survey~survey~n=调查
conducted~conduct~v=开展
by~by~prep=由（引出调查实施者）
harris~Harris~name=哈里斯
poll~Poll~name=民调（Harris Poll机构名部分）
td~TD~name=TD（证券公司名称部分）
ameritrade~Ameritrade~name=德美利证券（公司名）
even~even~adv=更加；甚至
surprising~surprising~a=令人惊讶的
is~be~v=是
than~than~conj=超过；比
half~half~n=一半
of~of~prep=……的（所属、部分或内容）
unretirees~unretiree~n=退休后仍工作或重返职场的人
those~those~pron=那些人
went~go~v=返回（went back）
back~back~adv=回去；重新
 after~after~prep=在……之后
retiring~retire~v=退休
said~say~v=说
would~would~aux=仍会；将会（表示过去的意愿）
be~be~aux=构成被动语态（be employed）
employed~employ~v=就业；受雇工作
later~late~a=晚年的
years~year~n=岁月；年岁
if~if~conj=即使（与even连用）
had~have~v=拥有
enough~enough~a=足够的
money~money~n=钱
settle~settle~v=安定下来（settle down）
down~down~adv=settle down的一部分，表示安定下来
showed~show~v=显示
financial~financial~a=经济、财务方面的
needs~need~n=需要
aren't~be~v=并不是（are not）
only~only~a=唯一的
culprit~culprit~n=诱因；问题的原因
unretirement~unretirement~n=退休不退工；退休后再工作
other~other~a=其他的
reasons~reason~n=原因；理由
study~study~n=研究
include~include~v=包括
personal~personal~a=个人的
fulfillment~fulfillment~n=满足感；自我实现带来的充实感
such~such~a=这样的（such as为例如）
as~as~prep=例如（such as）
staying~stay~v=保持
mentally~mentally~adv=在心理、头脑状态方面
fit~fit~a=状态良好、头脑活跃的
preventing~prevent~v=避免；预防
boredom~boredom~n=无聊
avoiding~avoid~v=避免
depression~depression~n=抑郁；情绪低落
concept~concept~n=观念
evolving~evolve~v=逐渐变化
christine~Christine~name=克里斯蒂娜
russell~Russell~name=拉塞尔
senior~senior~a=高级的
manager~manager~n=经理
it's~it is~v=退休这件事是（it is的缩写）
just~just~adv=仅仅
about~about~prep=关于；涉及
finances~finance~n=个人经济状况；钱财
value~value~n=价值
also~also~adv=也；还
driving~drive~v=促使
folks~folk~n=人们
continue~continue~v=继续
working~work~v=工作
past~past~prep=在退休年龄之后
reason~reason~n=原因
change~change~n=变化
patterns~pattern~n=模式
living~live~v=活着；生活
older~old~a=年长的
fastest-growing~fast-growing~a=增长最快的
segment~segment~n=群体；组成部分
u.s.~U.S.~name=美国
percentage~percentage~n=占比；百分比
retirement-age~retirement-age~a=达到退休年龄的
people~people~n=人们
labor~labor~n=劳动力
force~force~n=人群（labor force为劳动力人口）
has~have~aux=构成现在完成时
doubled~double~v=翻了一番；增至两倍
over~over~prep=在……期间
 decades~decade~n=十年；几十年
were~be~v=处于所述状态
february~February~n=二月
up~up~adv=上升；高于此前水平
from~from~prep=从（此前的水平）
all-time~all-time~a=有史以来的
low~low~n=最低水平
january~January~n=一月
united~United~name=United（资产管理机构名称部分）
income~Income~name=Income（资产管理机构名称部分）
because~because~conj=因为（与of组成由于）
spans~span~n=跨度（life spans为寿命）
boosting~boost~v=增加
savings~saving~n=积蓄；储蓄
preserve~preserve~v=保住；维持
nest~nest~n=与eggs组成养老储备金的习语
 eggs~egg~n=与nest组成养老储备金的习语
which~which~pron=关系代词，指调查研究
surveyed~survey~v=调查了
adults~adult~n=成年人
between~between~prep=在……年龄范围之间
six~six~num=六
increasing~increase~v=增加
anticipation~anticipation~n=预期；预先作准备
among~among~prep=在……之中
most~much~adv=最
popular~popular~a=常用的；受欢迎的
ways~way~n=办法
doing~do~v=这样做；增加储蓄
this~this~pron=增加储蓄这件事
company~company~n=公司
reducing~reduce~v=减少
overall~overall~a=总的；全部的
expenses~expense~n=开支
securing~secure~v=购置；获得（保险）
insurance~insurance~n=保险
maximizing~maximize~v=尽可能增加
contributions~contribution~n=缴款；存入账户的钱
accounts~account~n=账户
unfortunately~unfortunately~adv=遗憾的是
many~many~a=许多
preparing~prepare~v=准备
do~do~v=做（指退休后继续工作）
so~so~adv=这样；指退休后继续工作
worried~worried~a=担心的
making~make~v=使做到（make ends meet）
ends~end~n=收支两端（make ends meet为维持生计）
meet~meet~v=相接；相抵（make ends meet搭配）
brent~Brent~name=布伦特
weiss~Weiss~name=韦斯
co-founder~co-founder~n=联合创始人
baltimore-based~Baltimore-based~a=总部位于巴尔的摩的
financial-planning~financial-planning~a=财务规划的
firm~firm~n=公司
facet~Facet~name=Facet（公司名称部分）
wealth~Wealth~name=Wealth（公司名称部分）
suggested~suggest~v=建议
preretirees~preretiree~n=临近退休的人
should~should~aux=应当
speak~speak~v=交谈；咨询
with~with~prep=与（交谈的对象）
adviser~adviser~n=顾问
set~set~v=设定
long-term~long-term~a=长期的
goals~goal~n=目标
challenging~challenging~a=具有挑战性的
moments~moment~n=时刻
getting~get~v=进入某状态（get married指结婚）
married~married~a=已婚的（get married指结婚）
starting~start~v=开始建立
family~family~n=家庭
ultimately~ultimately~adv=最终
 decision~decision~n=决定
but~but~conj=而且；也是（not just…but）
emotional~emotional~a=情感上的
believe~believe~v=认为
can't~can~aux=不能；无法（can not）
retire~retire~v=退休
''')
r.word('P2-S1','are','处于至少40岁的年龄','be','v')
r.word('P2-S1','for','代表客户开展调查','for','prep',occ=2)
r.word('P2-S1','to','根据（according to）','to','prep',occ=3)
r.word('P2-S2','more','更加（修饰惊讶程度）','more','adv',occ=1)
r.word('P2-S2','more','超过一半（more than half）','more','adv',occ=2)
r.word('P2-S2','that','从句连接词，引出令人惊讶的事实','that','conj')
r.word('P2-S2','to','重返工作的方向（back to work）','to','prep',occ=2)
r.word('P3-S1','for','造成该趋势的原因对象','for','prep')
r.word('P3-S2','to','根据（according to）','to','prep')
r.word('P4-S1','is','构成进行时（is evolving）','be','aux')
r.word('P4-S1','retirement','退休业务','retirement','n',occ=2)
r.word('P4-S1','at','任职于','at','prep')
r.word('P4-S3','is','构成进行时（is driving）','be','aux')
r.word('P4-S3','work','工作的价值；劳动','work','n')
r.word('P5-S1','longer','活得更久','long','adv')
r.word('P5-S1','for','说明变化原因的对象','for','prep')
r.word('P5-S2','are','是（说明增长最快群体）','be','v')
r.word('P5-S3','past','过去的','past','a')
r.word('P5-S4','about','大约','about','adv')
r.word('P5-S4','to','根据（according to）','to','prep')
r.word('P6-S1','of','与because构成由于','of','prep',occ=1)
r.word('P6-S1','to','到（年龄范围终点）','to','prep',occ=2)
r.word('P6-S2','of','预期和准备所针对的对象（anticipation of）','of','prep')
r.word('P6-S3','by','通过（说明储蓄的方法）','by','prep')
r.word('P6-S3','to','缴入的账户','to','prep')
r.word('P7-S1','are','处于担心状态','be','v',occ=3)
r.word('P7-S1','at','任职于','at','prep')
r.word('P7-S2','that','从句连接词，引出建议内容','that','conj')
r.word('P8-S1','are','是（列举挑战性时刻）','be','v')
r.word('P8-S1','most','最','most','adv')
r.word('P8-S2','one','一个决定（代decision）','one','pron')
r.sentence('P4-S2')['chunks']=chunks(r,'P4-S2','just about','“这并不，|仅仅是钱的问题。')
done(r,{
'P1-S1':'well into是退休后很长时间，threatens为可能颠覆的趋势，非实际威胁某人。',
'P2-S1':'三分之一为至少40岁群体，第二个for指调查客户，第三个to是according to。',
'P2-S2':'两处more分别程度和超过一半，back to work为介词to，even if保留有钱仍工作的让步。',
'P3-S1':'culprit为趋势诱因非罪犯，only修饰原因单一性，不是经济毫无作用。',
'P3-S2':'reasons为原因，mentally fit为头脑状态良好，personal fulfillment与抑郁避免为非经济动机。',
'P4-S1':'第二处retirement为经理负责的退休业务，evolving是观念逐渐变化。',
'P4-S2':'修正not所在块提前带入just的只；全句为不仅钱财问题。',
'P4-S3':'work名词工作价值，driving为促使非驾驶，past retirement指退休后。',
'P5-S1':'longer为活得更久的副词，不是退休模式更长，冒号解释原因。',
'P5-S2':'segment为劳动力人口的组成群体，fastest-growing为增长最快而非年龄最大。',
'P5-S3':'doubled为增至两倍，retirement-age为达到退休年龄，past三十年为时间范围。',
'P5-S4':'20%与10%为不同年份就业占比，money manager是资产管理机构，Income为名称部分。',
'P6-S1':'nest eggs为养老储备金，which指研究，between 40 to 79按原卷年龄范围理解。',
'P6-S2':'六成为增加储蓄者，anticipation为预先作准备而非兴奋期待。',
'P6-S3':'三项减少开支购买寿险和增退休缴款并列，contributions为缴款非一般贡献。',
'P7-S1':'前两are构成进行时第三are联系担心状态，make ends meet为维持生计。',
'P7-S2':'that引出建议，preretirees临近退休，financial adviser为理财顾问。',
'P8-S1':'getting married与starting family和retiring均为人生阶段，are不是进行时。',
'P8-S2':'one代替decision，不仅经济且涉及情感，but不是否定情感的转折。',
'P8-S3':'believe是自我看法，不能写成已证实无法退休。'})
