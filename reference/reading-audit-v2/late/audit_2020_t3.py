"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2020-T3')
r.lex('''
madrid~Madrid~name=马德里
was~be~aux=构成过去时被动语态
hailed~hail~v=被赞誉为
as~as~prep=作为
public~public~a=公众的
health~health~n=健康
beacon~beacon~n=典范；具有指引意义的榜样
last~last~a=上一个的
november~November~n=十一月
when~when~conj=当……时
it~it~pron=该城市或该措施（承接前述对象）
rolled~roll~v=推出（roll out搭配）
out~out~adv=roll out的一部分，表示推出
ambitious~ambitious~a=力度大、目标高的
restrictions~restriction~n=限制措施
on~on~prep=针对
most~much~adv=最
polluting~pollute~a=造成污染的
cars~car~n=汽车
seven~seven~num=七
months~month~n=月
one~one~num=一次
 election~election~n=选举
day~day~n=日；一天
later~later~adv=之后
new~new~a=新上任的；新设的
conservative~conservative~a=保守派的
city~city~n=城市
council~council~n=市议会
suspended~suspend~v=暂停
enforcement~enforcement~n=执行；实施
of~of~prep=……的（所属或对象关系）
clean~clean~a=清洁的
air~air~n=空气
zone~zone~n=区域；文中的限行区
first~first~a=第一的
step~step~n=步骤
toward~toward~prep=朝向；走向
its~its~pron=它的（前述限行区的）
possible~possible~a=可能的
demise~demise~n=终止；被废除
mayor~mayor~n=市长
jos~José~name=何塞（José姓名被旧分词器截取的部分）
josé~José~name=何塞（市长的名字）
luis~Luis~name=路易斯（市长名字的一部分）
martinez-almeida~Martinez-Almeida~name=马丁内斯-阿尔梅达（市长姓氏）
made~make~v=把……作为
opposition~opposition~n=反对
to~to~prep=针对；对于
centrepiece~centrepiece~n=核心议题
campaign~campaign~n=竞选活动
despite~despite~prep=尽管
success~success~n=成功；取得成效
in~in~prep=在……方面或其中
improving~improve~v=改善
quality~quality~n=质量
judge~judge~n=法官
has~have~aux=构成现在完成时
now~now~adv=现在
 overruled~overrule~v=推翻（原先决定）
city's~city~n=该城市的
decision~decision~n=决定
stop~stop~v=停止
levying~levy~v=征收
fines~fine~n=罚款
ordering~order~v=命令
reinstated~reinstate~v=恢复实施
but~but~conj=但是
with~with~prep=在……情况下；伴随
legal~legal~a=法律上的
battles~battle~n=争执；斗争
ahead~ahead~adv=在前方；接下来
zone's~zone~n=该区域的
future~future~n=前景
looks~look~v=看起来
uncertain~uncertain~a=不确定的
at~at~prep=与best连用表示即便往好处看
best~good~a=最好的（at best表示充其量）
among~among~prep=在……之中；除……之外还有
other~other~a=其他的
weaknesses~weakness~n=缺点；弱点
measures~measure~n=措施
cities~city~n=城市
must~must~aux=必须；不得不
employ~employ~v=采用
left~leave~v=被留下独自承担；被放任
tackle~tackle~v=应对；处理
dirty~dirty~a=被污染的
own~own~pron=自己（on their own表示独自）
are~be~v=处于所说的状态
politically~politically~adv=在政治上
contentious~contentious~a=具有争议的
therefore~therefore~adv=因此
vulnerable~vulnerable~a=容易受政治变化冲击的
that's~that is~v=这是（that is的缩写）
because~because~conj=因为
inevitably~inevitably~adv=不可避免地
put~put~v=把……置于；转嫁
costs~cost~n=成本
cleaning~clean~v=净化
individual~individual~a=个人的；个别的
drivers~driver~n=车主；驾驶员
who~who~pron=关系词，指前述的人
pay~pay~v=支付
fees~fee~n=费用
buy~buy~v=购买
better~good~a=更好的；更环保的
vehicles~vehicle~n=车辆
rather~rather~adv=与than连用，表示而不是
than~than~conj=与rather连用，表示而不是
car~car~n=汽车
manufacturers~manufacturer~n=制造商
whose~whose~pron=关系词，表示制造商的
cheating~cheat~n=作弊；违规欺骗行为
is~be~v=是
real~real~a=真正的
cause~cause~n=原因
 toxic~toxic~a=有毒有害的
pollution~pollution~n=污染
it's~it is~v=形式主语结构，相当于这……（it is）
hard~hard~a=困难的
imagine~imagine~v=想象
similar~similar~a=类似的
reversal~reversal~n=政策逆转
happening~happen~v=发生
london~London~name=伦敦
ultra-low~ultra-low~a=超低的
emission~emission~n=排放
ulez~Ulez~name=超低排放区（缩写）
likely~likely~a=可能的
be~be~v=成为；是
big~big~a=重大的
issue~issue~n=议题
next~next~a=下一个的
year's~year~n=一年的（next year's指明年的）
mayoral~mayoral~a=市长选举的
if~if~conj=如果
sadiq~Sadiq~name=萨迪克（市长名字）
khan~Khan~name=汗（市长姓氏）
wins~win~v=赢得选举
extends~extend~v=扩展
north~North~a=北面的（North Circular地名部分）
south~South~a=南面的（South Circular地名部分）
circular~Circular~name=环城的（环城路名称的一部分）
roads~road~n=道路
intends~intend~v=打算；计划
sure~sure~a=必定的
spark~spark~v=引发
intense~intense~a=强烈的
from~from~prep=来自
far~far~adv=远远；程度大得多
larger~large~a=更多的
number~number~n=人数；数量
motorists~motorist~n=车主；驾车者
will~will~aux=将会
then~then~adv=届时
affected~affect~v=受到影响
that~that~conj=引导陈述内容，不单译
such~such~a=这样的（such as表示例如）
london's~London~name=伦敦的
useless~useless~a=无用的
local~local~a=地方的
officials~official~n=官员
using~use~v=使用；动用
levers~lever~n=政策手段
available~available~a=可供使用的
safeguard~safeguard~v=保护
residents~resident~n=居民
face~face~n=面对（in the face of搭配）
serious~serious~a=严重的
threat~threat~n=威胁
zones~zone~n=限行区域
 do~do~aux=强调助动词，表示确实
 deliver~deliver~v=带来；实现
some~some~a=一定程度的
improvements~improvement~n=改善
science~science~n=科学证据
tells~tell~v=告诉；表明
means~mean~v=意味着
benefits~benefit~n=益处
fewer~few~a=更少的
heart~heart~n=心脏
attacks~attack~n=发作（heart attacks指心脏病发作）
strokes~stroke~n=中风
premature~premature~a=过早的（修饰出生时指早产）
births~birth~n=出生；分娩
less~little~a=更少的
cancer~cancer~n=癌症
dementia~dementia~n=痴呆
asthma~asthma~n=哮喘
untimely~untimely~a=过早的
 deaths~death~n=死亡
mayors~mayor~n=市长
councilors~councilor~n=市议员
can~can~aux=能够
only~only~adv=仅；只能
so~so~adv=达到这个程度（so much表有限程度）
much~much~pron=这么多；有限的事情
about~about~prep=针对；关于
problem~problem~n=问题
bigger~big~a=规模更大的
any~any~a=任何的
town~town~n=城镇
acting~act~v=采取行动
national~national~a=国家层面的
 governments~government~n=政府
britain's~Britain~name=英国的
others~other~pron=其他国家的政府
across~across~prep=遍及；在……各地
have~have~aux=构成现在完成时
failed~fail~v=未能做到
keep~keep~v=阻止进入；使留在某处
highly~highly~adv=高度地；严重地
certain~certain~a=某些
areas~area~n=区域
centres~centre~n=中心
school~school~n=学校
streets~street~n=街道
even~even~adv=甚至
response~response~n=应对；反应
absence~absence~n=缺乏
larger~large~a=范围更大的
effort~effort~n=努力；行动
properly~properly~adv=切实地；妥善地
enforce~enforce~v=执行
existing~exist~a=现有的
regulations~regulation~n=规定；法规
require~require~v=要求
auto~auto~n=汽车
companies~company~n=公司
bring~bring~v=使达到（bring into搭配）
into~into~prep=进入；达到（某种状态）
compliance~compliance~n=符合规定；达标
wales~Wales~name=威尔士
introduced~introduce~v=推出；实施
special~special~a=特别的
low~low~a=低的
speed~speed~n=速度
limits~limit~n=限制；限速标准
minimise~minimise~v=尽可能减少
we're~we are~aux=我们正在（we are的缩写）
doing~do~v=采取；做
everything~everything~pron=所有事情
insist~insist~v=坚持要求
up~up~adv=clean up的一部分，表示清除污染
''')
r.lex('europe~Europe~name=欧洲')
r.word('P1-S1','it','马德里这座城市','it','pron')
r.word('P4-S3','it','该超低排放区','it','pron',occ=1)
r.word('P4-S3','it','扩展限行区这件事','it','pron',occ=2)
for sid in ['P2-S2','P7-S1','P7-S2']:r.word(sid,'to','不定式标记，表示要做的动作','to','inf')
r.word('P1-S1','on','针对汽车的限制','on','prep')
r.word('P1-S1','as','誉为（hail as搭配）','as','prep')
r.word('P2-S3','at','即便往好处看（at best）','at','prep')
r.word('P3-S1','to','不定式标记，表应对污染的动作','to','inf')
r.word('P3-S1','on','独自（on their own）','on','prep')
r.word('P3-S2','to','转嫁给的对象（put costs on to）','to','prep')
r.word('P3-S2','that\'s','这就是；这正是','that is','v')
r.word('P3-S2','cleaning','净化（作名词性成分）','clean','v')
r.word('P4-S1','to','不定式标记，连接想象这一动作','to','inf')
r.word('P4-S2','to','不定式标记（likely to be）','to','inf')
r.word('P4-S3','to','扩展到的范围','to','prep',occ=1)
r.word('P4-S3','to','不定式标记，表引发反对','to','inf',occ=2)
r.word('P4-S3','as','按照；如同','as','conj')
r.word('P4-S3','be','构成被动语态（be affected）','be','aux')
r.word('P5-S1','as','例如（such as搭配）','as','prep')
r.word('P5-S2','it','前句“措施没有用”这一说法','it','pron')
r.word('P5-S2','from','与……相去甚远（far from it）','from','prep')
r.word('P5-S3','to','对……而言（available to）','to','prep',occ=1)
r.word('P5-S3','to','不定式标记，表示保护健康的目的','to','inf',occ=2)
r.word('P5-S3','that','关系代词，指可用的政策手段','that','pron')
r.word('P5-S4','that','那件事；指改善空气质量','that','pron')
r.word('P5-S4','to','空气质量改善的对象','to','prep')
r.word('P6-S1','do','做；采取行动','do','v')
r.word('P6-S1','than','比；相较于','than','conj')
r.word('P6-S1','one','一个；一座','one','num')
r.word('P6-S1','that','关系代词，指污染问题','that','pron')
r.word('P6-S2','do','采取行动','do','v')
r.word('P6-S2','to','不定式标记（fail to do）','to','inf')
r.word('P6-S2','so','这样做；指应对空气污染','so','adv')
r.word('P7-S1','that','关系代词，指限制措施','that','pron')
r.word('P7-S1','out','在外；不准进入（keep out of搭配）','out','adv')
r.word('P7-S1','to','针对……的回应（response to）','to','prep',occ=1)
r.word('P7-S3','but','除了；唯独不','but','prep')
r.word('P7-S3','clean','清理污染；降低排放（clean up）','clean','v')
r.sentence('P5-S4')['chunks'][0]['zh']='这些限行区域确实让空气质量有所改善，'
done(r,{
'P1-S1':'被誉为是措施实施后的结果，on管汽车限制，hail不是招呼或冰雹。',
'P1-S2':'七个月和一次选举后的市议会更替，demise指政策废除非人物死亡。',
'P2-S1':'尽管改善空气质量仍反对限行区，make…centrepiece为作为竞选核心。',
'P2-S2':'them指罚款，overrule推翻停罚决定，reinstated为恢复实施。',
'P2-S3':'法律争执尚在前方，at best保留即便乐观看仍不确定的评价。',
'P3-S1':'left为城市被放任独自处理污染；措施政治争议导致容易被推翻。',
'P3-S2':'rather than排除车企承担成本，whose指制造商作弊，保留作者归责观点。',
'P4-S1':'not hard为不难，reversal指政策逆转，London为另一城市。',
'P4-S2':'issue是选举议题，year’s为明年所属，likely保留可能性。',
'P4-S3':'扩至南北环城路为条件；far larger修饰车主人数，as指按计划。',
'P5-S1':'不是说这些措施无用，外层not否定无用判断，不能译成作者反对限行。',
'P5-S2':'far from it否定前述无用观点，不是距离某一物体很远。',
'P5-S3':'levers为可用政策手段，to分别表示可供官员使用与保护居民目的。',
'P5-S4':'do强调确有改善，means是动词意味着；fewer和less分别对应疾病事件及病症。',
'P5-S5':'名词短句补承上文减少，untimely为过早死亡不单指不合时宜。',
'P6-S1':'can only do so much为作用有限，than比较问题规模与单一城市。',
'P6-S2':'they为地方官员，国家政府未行动解释地方接手，do so回指应对污染。',
'P7-S1':'限制措施为更大治理缺位的反应，keep out禁止进入，compliance为排放合规。',
'P7-S2':'low speed limits为降低限速标准，minimise为尽量减少而非彻底消除污染。',
'P7-S3':'but为除了而非转折连词，意为唯独没坚持要求车企清理自身污染。'})
