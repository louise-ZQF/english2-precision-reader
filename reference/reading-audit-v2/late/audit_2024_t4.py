"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2024-T4')
r.lex('''
if~if~conj=如果
look~look~v=看
at~at~prep=看……（look at）
apps~app~n=应用程序
on~on~prep=在……上
phone~phone~n=手机
chances~chance~n=可能性（chances are表示很可能）
are~be~v=是
have~have~v=有；装有
least~least~adv=最少（at least至少）
one~one~pron=一个，指应用
related~related~adj=有关的
to~to~prep=与……相关（related to）
health~health~n=健康
probably~probably~adv=很可能
several~several~pron=好几个，指应用
whether~whether~conj=无论（列举可能的工具）
it~it~pron=它，指所用的应用或设备
is~be~v=是
mental~mental~adj=心理的
app~app~n=应用程序
fitness~fitness~n=健身；身体健康
tracker~tracker~n=追踪记录工具
connected~connected~adj=联网的
device~device~n=设备
something~something~pron=某种东西
else~else~adv=其他的
many~many~pron=许多人
 taking~take~v=利用（take advantage of）
advantage~advantage~n=有利条件（take advantage of利用）
of~of~prep=的（连接所属或修饰关系）
this~this~det=这种（技术）
technology~technology~n=技术
keep~keep~v=持续了解；追踪（keep track of）
better~well~adv=更好地
track~track~n=记录；了解情况（keep track of）
in~in~prep=以（某种方式）
some~some~det=某种
shape~shape~n=形式（some shape or form）
form~form~n=形式
recent~recent~adj=近期的
research~research~n=研究
from~from~prep=来自
organization~organization~n=组织
for~for~prep=以……为宗旨（组织名）
review~review~n=评审
care~care~n=医疗
applications~application~n=应用程序
found~find~v=发现
that~that~conj=引出研究或指控的内容
were~be~v=是；处于某种状态
available~available~adj=可获得的；可使用的
market~market~n=市场
which~which~pron=指前述应用程序
launched~launch~v=推出；上线
alone~alone~adv=仅仅（限定2020年）
while~while~conj=尽管（让步）
these~these~det=这些（应用）
great~great~adj=大的（a great deal大量）
deal~deal~n=量（a great deal大量）
offer~offer~v=提供
always~always~adv=总是
clear~clear~adj=清楚的
how~how~adv=如何
personal~personal~adj=个人的
information~information~n=信息
input~input~v=输入
collected~collect~v=收集
safeguarded~safeguard~v=保护；保障安全
shared~share~v=分享
online~online~adv=在线上；通过网络
existing~existing~adj=现行的；现有的
privacy~privacy~n=隐私
law~law~n=法律
such~such~det=这样的（such as表示例如）
as~as~prep=例如（such as）
insurance~insurance~n=保险
portability~portability~n=可携带性；流通性（法律名称用词）
accountability~accountability~n=责任；问责（法律名称用词）
act~act~n=法案；法律
primarily~primarily~adv=主要地
focused~focused~adj=关注于；以……为重点的
way~way~n=方式
hospitals~hospital~n=医院
doctors~doctor~n=医生
offices~office~n=诊所（doctor's office）
clinics~clinic~n=门诊机构；诊所
companies~company~n=公司
store~store~v=保存；存储
records~record~n=档案；记录
data~data~n=数据
tracking~track~n=追踪记录（修饰可穿戴设备用途）
wearables~wearable~n=可穿戴设备
collecting~collect~v=收集
typically~typically~adv=通常
does~do~aux=与not构成否定
receive~receive~v=获得
same~same~adj=同样的
legal~legal~adj=法律上的
protections~protection~n=保护措施；保护
without~without~prep=如果没有；缺少
additional~additional~adj=额外的
place~place~n=适当位置（in place此处指已建立生效）
may~may~modal=可能
share~share~v=分享
potentially~potentially~adv=可能地
monetize~monetize~v=变现；从中获利
consumers~consumer~n=消费者
authorized~authorize~v=授权；许可
anticipated~anticipate~v=预料到
flo~Flo~propn=Flo（公司名称）
faced~face~v=面临
federal~federal~adj=联邦的
trade~trade~n=贸易（机构名组成部分）
commission~commission~n=委员会
ftc~FTC~abbr=美国联邦贸易委员会
investigation~investigation~n=调查
alleged~allege~v=指控；声称（未在此直接断定为事实）
complaint~complaint~n=投诉书；指控文书
despite~despite~prep=尽管
express~express~adj=明确的；明示的
claims~claim~n=声明；声称
company~company~n=公司
took~take~v=取得；掌握（take control of）
control~control~n=控制
users~user~n=用户
sensitive~sensitive~adj=敏感的；需要谨慎保护的
fertility~fertility~n=生育；生殖健康
with~with~prep=与（分享给某人）
third~third~num=第三（third parties第三方）
parties~party~n=一方；参与方
settled~settle~v=达成和解；解决争议
matter~matter~n=此事；争议
consent~consent~n=同意；许可
order~order~n=命令；执行命令
requiring~require~v=要求
get~get~v=取得
affirmative~affirmative~adj=明确表示肯定的
before~before~prep=在……之前
sharing~share~v=分享
well~well~adv=与as well as构成“也；还”
instruct~instruct~v=指示；要求
delete~delete~v=删除
had~have~aux=与obtained构成过去完成时
obtained~obtain~v=取得
section~section~n=法律条款
empowers~empower~v=授权
initiate~initiate~v=启动
enforcement~enforcement~n=执法
action~action~n=行动
against~against~prep=针对
unfair~unfair~adj=不公平的
deceptive~deceptive~adj=欺骗性的
acts~act~n=行为
meaning~mean~v=意味着
can~can~modal=能够
only~only~adv=只能；仅仅
after~after~prep=在……之后
fact~fact~n=事情发生（after the fact事后）
company's~company~n=公司的（所有格）
practices~practice~n=做法
misleading~misleading~adj=误导性的
cause~cause~v=造成
unjustified~unjustified~adj=无正当理由的；不合理的
consumer~consumer~n=消费者
harm~harm~n=损害
doing~do~v=做
what~what~pron=……的事情（what it can即其力所能及之事）
ensure~ensure~v=确保
keeping~keep~v=履行（keep promises）
promises~promise~n=承诺
around~around~prep=关于
handling~handling~n=处理；管理
rate~rate~n=速度
hitting~hit~v=进入（hit the market上市）
demonstrates~demonstrate~v=显示
just~just~adv=正是；到底（强调程度）
immense~immense~adj=巨大的
challenge~challenge~n=挑战
prospects~prospect~n=前景
legislation~legislation~n=立法
commentators~commentator~n=评论人士
suggest~suggest~v=认为；指出
comprehensive~comprehensive~adj=全面的
seems~seem~v=似乎
unlikely~unlikely~adj=不太可能的
short~short~adj=短的
term~term~n=时期（in the short term短期内）
states~state~n=州
begun~begin~v=开始
implementing~implement~v=实施
own~own~adj=自己的
solutions~solution~n=解决方案
shore~shore~v=加强；巩固（shore up）
up~up~adv=与shore构成“加强”
consumer-generated~consumer-generated~adj=消费者自行产生的
california~California~propn=加利福尼亚州
has~have~aux=与过去分词构成现在完成时
been~be~v=一直处于
forefront~forefront~n=前列；领先位置
state~state~n=州（修饰州级行动或法律）
efforts~effort~n=努力；行动
virginia~Virginia~propn=弗吉尼亚州
colorado~Colorado~propn=科罗拉多州
utah~Utah~propn=犹他州
also~also~adv=也
recently~recently~adv=最近
passed~pass~v=通过（法律）
''')
r.word('P1-S1','at','至少（at least）','at','prep',occ=2)
r.word('P1-S2','are','与taking构成现在进行时','be','aux')
r.word('P1-S2','to','不定式标记，表利用技术的目的','to','inf')
r.word('P1-S2','of','与take advantage构成“利用”','of','prep',occ=2)
r.word('P1-S2','of','所追踪的对象（keep track of）','of','prep',occ=3)
r.word('P1-S3','in','在（某年）','in','prep')
r.word('P1-S3','of','其中的（90000个应用）','of','prep',occ=2)
r.word('P2-S1','to','不定式标记（有许多可提供的内容）','to','inf')
r.word('P2-S1','it','形式主语，指信息如何收集保护分享的过程','it','pron')
r.word('P2-S1','is','与collected safeguarded shared构成被动语态','be','aux',occ=2)
r.word('P2-S2','on','所关注的对象（focused on）','on','prep')
r.word('P2-S3','are','与collecting构成进行时','be','aux')
r.word('P3-S1','have','与authorized和anticipated构成完成时','have','aux')
r.word('P3-S2','in','在（某年）','in','prep')
r.word('P3-S3','in','在（投诉书）中','in','prep')
r.word('P3-S3','it','它，指生育数据','it','pron')
r.word('P3-S3','of','所掌控的对象（take control of）','of','prep')
r.word('P3-S4','with','通过；借助（同意令）','with','prep')
r.word('P3-S4','to','不定式标记（要求取得同意）','to','inf',occ=1)
r.word('P3-S4','to','不定式标记（要求指示第三方）','to','inf',occ=2)
r.word('P3-S4','to','不定式标记（指示第三方删除）','to','inf',occ=3)
r.word('P3-S4','as','与as well as构成“也；还”','as','conj')
r.word('P3-S4','they','它们，指第三方','they','pron')
r.word('P3-S4','their','他们的，指应用用户的','their','det')
r.word('P4-S1','to','不定式标记（授权启动执法）','to','inf')
r.word('P4-S1','act','采取行动','act','v',occ=2)
r.word('P4-S2','is','与doing构成进行时','be','aux',occ=1)
r.word('P4-S2','it','它，指联邦贸易委员会','it','pron')
r.word('P4-S2','to','不定式标记（表尽力做事的目的）','to','inf',occ=1)
r.word('P4-S2','to','对（消费者作出的承诺）','to','prep',occ=2)
r.word('P4-S2','are','与keeping或hitting构成现在进行时','be','aux')
r.word('P4-S2','at','以（某种上市速度，at which修饰rate）','at','prep')
r.word('P4-S2','which','引导定语从句，指上市速度rate','which','pron')
r.word('P4-S2','how','多么（强调挑战的巨大程度）','how','adv')
r.word('P4-S2','this','这，指确保应用兑现隐私承诺的工作','this','pron')
r.word('P5-S1','as','至于（as to）','as','prep')
r.word('P5-S1','to','与as构成“至于”','to','prep')
r.word('P5-S1','for','……的（立法前景）','for','prep')
r.word('P5-S1','in','在……期间','in','prep')
r.word('P5-S2','have','与begun构成现在完成时','have','aux')
r.word('P5-S2','to','不定式标记，表加强保护的目的','to','inf')
r.word('P5-S2','for','保护的对象','for','prep')
r.word('P5-S3','at','处于（前列）','at','prep')
r.word('P5-S3','with','凭借；通过（这部法律）','with','prep')
r.word('P5-S4','have','与passed构成现在完成时','have','aux')
r.sentence('P1-S1')['chunks'][-1]['zh']='而且很可能有好几个。'
r.sentence('P3-S4')['chunks'][0]['zh']='Flo Health与联邦贸易委员会解决了此事，'
r.sentence('P3-S4')['chunks'][1]['zh']='通过一项同意令，'
notes={
'P1-S1':'chances are很可能非机会；at least至少与probably several好几个分开，修正末块数量含义。',
'P1-S2':'whether无论列举工具，taking advantage利用、keep track追踪、some shape or form某种方式，非身体形状。',
'P1-S3':'35万总数与9万2020新增对应，which apps、alone只限定2020；组织名称内care医疗。',
'P2-S1':'not always并非总是清楚，have实义拥有可提供内容，第二is为三个并列动词被动助动词。',
'P2-S2':'act法律，portability/accountability法律名称用义；doctor offices诊所非普通办公室，不扩大法律适用范围。',
'P2-S3':'主干信息通常不得同等保护，are collecting插入定语，wearables名词而tracking追踪用途。',
'P3-S1':'may及potentially两层可能，have完成助动词，授权及预料的否定不混淆企业实际是否获利。',
'P3-S2':'faced面临调查不等于已判责任，Federal Trade Commission机构名逐词释义不当固定词组。',
'P3-S3':'alleged保留指控性质，express明确形容词，fertility生育数据，it该数据，third parties法律第三方。',
'P3-S4':'express词性从旧v改adj，before分享前取得同意、指示第三方删除并列；修正首块提前且重复翻译命令。',
'P4-S1':'第一Act法律、后act行动，only after fact限制事后执法，if具体违法损害条件，非万能预防权。',
'P4-S2':'首is进行末is系词，两are进行；around关于、at which上市速度，how巨大程度，it委员会与this工作分清。',
'P5-S1':'as to话题、in short term时间，seems unlikely保留判断可能性而非永远不立法。',
'P5-S2':'have begun完成时，shore up加强保护，consumer-generated完整复合词指消费者产生数据。',
'P5-S3':'has been完成时持续领先，forefront领先位置，with法律作为体现方式，不译与法律在一起。',
'P5-S4':'三州名各自核定，have passed完成时，state州级不误读动词陈述。'}
r.word('P3-S1','in','处于到位生效状态（in place）','in','prep',occ=1)
r.word('P1-S2','of','……当中的（我们当中许多人）','of','prep',occ=1)
r.word('P3-S2','Health','Health，Flo Health公司名称的一部分','Health','propn')
r.word('P3-S4','Health','Health，Flo Health公司名称的一部分','Health','propn')
done(r,notes)
