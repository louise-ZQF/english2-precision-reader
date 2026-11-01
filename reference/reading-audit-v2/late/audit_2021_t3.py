"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2021-T3')
r.lex('''
when~when~conj=当……时
microsoft~Microsoft~name=微软公司
bought~buy~v=收购
task~task~n=任务
management~management~n=管理
app~app~n=应用程序
wunderlist~Wunderlist~name=Wunderlist（任务管理应用名）
mobile~mobile~a=手机端的
calendar~calendar~n=日历应用
sunrise~Sunrise~name=Sunrise（日历应用名）
in~in~prep=在……范围或时期中
it~it~pron=它（微软公司）
picked~pick~v=选中
two~two~num=两个
newcomers~newcomer~n=新出现的应用或企业
that~that~pron=关系词，指前面所述对象
were~be~aux=构成过去进行或被动结构
attracting~attract~v=引起；吸引
considerable~considerable~a=相当大的
buzz~buzz~n=热议；关注
silicon~Silicon~name=硅（Silicon Valley指硅谷）
valley~Valley~name=谷（Silicon Valley地名部分）
microsoft's~Microsoft~name=微软公司的
own~own~a=自己的
office~Office~name=Office（微软办公软件产品）
dominates~dominate~v=主导；占据优势
market~market~n=市场
for~for~prep=对应于；面向
productivity~productivity~n=办公效率
software~software~n=软件
but~but~conj=但是
start-ups~start-up~n=初创企业
represented~represent~v=代表
new~new~a=新的
wave~wave~n=浪潮；一批
technology~technology~n=技术
designed~design~v=设计的
from~from~prep=从
 ground~ground~n=基础（from the ground up指从头）
up~up~adv=与ground构成从基础起；与动词构成搭配
smartphone~smartphone~n=智能手机
world~world~n=世界；时代
both~both~a=两个都
apps~app~n=应用程序
however~however~adv=然而
later~later~adv=后来
scrapped~scrap~v=停用；终止运营
after~after~conj=在……之后
said~say~v=表示
had~have~aux=构成过去完成时
used~use~v=使用
best~good~a=最好的
features~feature~n=产品功能
its~its~pron=微软自己的
products~product~n=产品
teams~team~n=团队
of~of~prep=……的（所属或部分范围）
engineers~engineer~n=工程师
stayed~stay~v=留任（stay on）
on~on~adv=继续留下（stay on）
making~make~v=使成为
many~many~a=许多
acqui-hires~acqui-hire~n=以获取人才团队为目的的收购
biggest~big~a=规模最大的
companies~company~n=公司
have~have~aux=构成现在完成时
to~to~inf=不定式标记，连接动作
feed~feed~v=满足（需求）
great~great~a=巨大的
hunger~hunger~n=强烈需求（比喻）
tech~tech~n=科技
 talent~talent~n=人才
critics~critic~n=批评者
fates~fate~n=命运
are~be~v=是
examples~example~n=例证
remorseless~remorseless~a=毫不留情的
drive~drive~n=扩张动力；行动势头
by~by~prep=由（引出实施者）
big~Big~a=大型的（Big Tech指大型科技公司）
chew~chew~v=吞并（chew up比喻）
any~any~a=任何的
innovative~innovative~a=有创新能力的
lie~lie~v=位于；处在
path~path~n=前进道路
seedlings~seedling~n=幼苗；比喻刚起步的企业
closed~close~v=关闭
 down~down~adv=彻底关闭（close down）
complained~complain~v=抱怨说
paul~Paul~name=保罗
arnold~Arnold~name=阿诺德
partner~partner~n=投资机构合伙人
at~at~prep=任职于
san~San~name=圣（San Francisco地名部分）
francisco-based~Francisco-based~a=位于旧金山的（与San连用）
switch~Switch~name=Switch（投资机构名称部分）
ventures~Ventures~name=Ventures（投资机构名称部分）
putting~put~v=使结束（put an end to）
end~end~n=终结
businesses~business~n=企业
might~might~aux=可能
one~one~a=某一；有朝一日（one day）
day~day~n=一天（one day指有朝一日）
turn~turn~v=变成
into~into~prep=成为；进入
competitors~competitor~n=竞争对手
declined~decline~v=拒绝
comment~comment~v=发表评论；置评
like~like~prep=像；与……一样
other~other~a=其他的
start-up~start-up~a=初创企业的
investors~investor~n=投资者
mr~Mr.~n=先生（称谓）
arnold's~Arnold~name=阿诺德的
business~business~n=生意；业务
 often~often~adv=常常
depends~depend~v=依赖（depend on）
selling~sell~v=出售
larger~large~a=更大的
though~though~conj=不过；尽管
admits~admit~v=承认
mixed~mixed~a=复杂矛盾的
feelings~feeling~n=感受
about~about~prep=对于；关于
result~result~n=结果
think~think~v=认为
these~these~a=这些
things~thing~n=交易；这里指公司收购
good~good~a=有利的
if~if~conj=如果
put~put~v=戴上（put…hat on为换立场的比喻）
selfish~selfish~a=自利的；只考虑自身利益的
hat~hat~n=帽子；比喻看问题的立场
american~American~a=美国的
economy~economy~n=经济
don't~do~aux=不（do not）
know~know~v=知道
us~US~name=美国（US）
federal~Federal~a=联邦的（机构名部分）
trade~Trade~n=贸易（机构名部分）
commission~Commission~n=委员会
says~say~v=说；表示
wants~want~v=希望
find~find~v=找到
answer~answer~n=答案
question~question~n=问题
this~this~a=这个；本周
week~week~n=周
asked~ask~v=要求；索取
five~five~num=五
most~much~adv=最
valuable~valuable~a=市值高的
information~information~n=信息
small~small~a=小规模的
acquisitions~acquisition~n=收购交易
over~over~prep=在……期间
past~past~a=过去的
decade~decade~n=十年
although~although~conj=尽管
only~only~adv=仅仅
research~research~n=研究
project~project~n=项目
stage~stage~n=阶段
request~request~n=要求
has~have~aux=构成现在完成时
raised~raise~v=引出；带来
prospect~prospect~n=可能性
regulators~regulator~n=监管机构
wading~wade~v=介入；涉足（wade into）
early-stage~early-stage~a=早期发展阶段的
markets~market~n=市场
until~until~prep=直到
now~now~adv=现在
been~be~v=一直处于所述状态
beyond~beyond~prep=超出
reach~reach~n=监管触及的范围
given~given~prep=考虑到
combined~combined~a=合计的
value~value~n=价值；市值
more~more~a=更多的（more than表示超过）
than~than~conj=比；超过
trillion~trillion~num=万亿
rifling~rifle~v=逐一翻查；翻检
through~through~prep=遍查的范围（rifle through）
such~such~a=这样的
deals~deal~n=交易
much~much~adv=程度大得多
less~little~adv=较少地
prominent~prominent~a=引人注意的
seem~seem~v=似乎
beside~beside~prep=偏离；无关（beside the point）
point~point~n=重点
between~between~prep=合计而言（between them）
spent~spend~v=花费
average~average~n=平均
billion~billion~num=十亿
year~year~n=年
sub~sub-~prefix=低于（金额前缀）
years~year~n=年
drop~drop~n=一滴；比喻微小的一部分
ocean~ocean~n=海洋（a drop in the ocean比喻沧海一粟）
compared~compare~v=与……相比
with~with~prep=与（比较对象）
massive~massive~a=庞大的
financial~financial~a=资金方面的
reserves~reserve~n=储备
venture~venture~n=风险（venture capital为风险投资）
capital~capital~n=投资资金
was~be~aux=构成过去被动语态
invested~invest~v=投入；投资
last~last~a=上一个的
say~say~v=说；认为
use~use~v=使用；通过
buy~buy~v=收购
threatening~threatening~a=构成威胁的
potential~potential~a=潜在的
before~before~conj=在……之前
chance~chance~n=机会
gain~gain~v=获得；积累
momentum~momentum~n=发展势头
some~some~a=某些
cases~case~n=情况
as~as~prep=作为
part~part~n=一部分
kill~kill~v=扼杀；使终止
 tactic~tactic~n=策略
simply~simply~adv=直接；仅仅
close~close~v=关闭
''')
r.word('P2-S1','it','微软公司','it','pron')
r.word('P2-S2','them','这两次收购（以被收购团队留下说明）','they','pron')
r.word('P2-S2','for','需求所指向的对象（hunger for）','for','prep')
r.word('P2-S2','that','关系词，指为人才收购的交易','that','pron')
r.word('P3-S1','To','在……看来','to','prep',occ=1)
r.word('P3-S1','up','与chew合成彻底吞并','up','adv')
r.word('P3-S2','to','使终结的对象（put an end to）','to','prep')
r.word('P4-S1','on','依赖的对象（depend on）','on','prep',occ=1)
r.word('P4-S1','to','出售给的买方','to','prep',occ=1)
r.word('P4-S1','to','对于；承认某种感受（admit to）','to','prep',occ=2)
r.word('P4-S1','on','戴上（put hat on的一部分）','on','adv',occ=2)
r.word('P4-S1','for','对……有利','for','prep')
r.word('P4-S2','for','对……有利','for','prep')
r.word('P4-S3','know','知道答案','know','v')
r.word('P5-S1','it','美国联邦贸易委员会','it','pron')
r.word('P5-S1','to','问题所对应的答案（answer to）','to','prep',occ=2)
r.word('P5-S1','that','那个关于收购是否有利经济的问题','that','a')
r.word('P5-S2','for','向企业索取的内容（ask for）','for','prep')
r.word('P5-S2','it','美国联邦贸易委员会','it','pron')
r.word('P5-S3','at','在当前阶段','at','prep')
r.word('P5-S3','that','关系代词，指早期科技市场','that','pron')
r.word('P6-S1','than','超过（more than）','than','conj',occ=1)
r.word('P6-S2','a','每（a year表示每年）','a','art',occ=1)
r.word('P6-S2','on','用于；支出用途（spend on）','on','prep')
r.word('P6-S2','that','关系代词，指风险投资资金','that','pron')
r.word('P7-S1','have','拥有（发展的机会）','have','v')
r.word('P7-S1','them','这些被收购的初创企业','they','pron')
r.sentence('P4-S2')['chunks']=chunks(r,'P4-S2','good for','但它们，|对美国经济也有利吗？')
r.sentence('P6-S2')['chunks'][1]['zh']='每年平均只花费34亿美元，'
r.sentence('P6-S2')['chunks'][2]['zh']='在过去五年用于10亿美元以下的收购——'
done(r,{
'P1-S1':'两项收购对象是应用新秀，newcomers原型为newcomer，buzz指关注热议非蜂鸣。',
'P1-S2':'Office为产品名，productivity是办公效率，from ground up强调为手机从头设计。',
'P2-S1':'停止应用在微软表示采用功能之后，features为功能而非面部特征。',
'P2-S2':'团队留下使收购成为人才收购案例，them指收购，feed hunger比喻满足人才需求。',
'P3-S1':'To为在批评者看来，drive名词扩张势头，chew up为吞并而非字面咀嚼。',
'P3-S2':'seedlings比喻初创企业，原型seedling非seedle；put an end为终止未来竞争者。',
'P3-S3':'decline为拒绝置评，不是业绩下降。',
'P4-S1':'depends on表业务依赖，admit to是承认感受，戴帽比喻从自利角度思考。',
'P4-S2':'they指上述收购交易，for为对经济有利，修正第一块提前译入比较对象。',
'P4-S3':'don’t否定知道，保留上一疑问的不确定回答。',
'P5-S1':'it指联邦贸易委员会，首to不定式第二to为answer to搭配。',
'P5-S2':'most valuable为市值最高，for information为索取信息，过去十年为收购范围。',
'P5-S3':'研究只是目前阶段，介入早期市场为可能性，reach为监管触及范围。',
'P6-S1':'合计市值5.5万亿美元对照小收购，引人关注程度低于Wunderlist而非市值一定更低。',
'P6-S2':'34亿美元为合计年均支出，低于10亿美元为单笔收购，1300亿美元为风险投资。',
'P7-S1':'批评者观点与作者陈述区分，before指壮大前收购，some cases不扩为所有交易。'})
