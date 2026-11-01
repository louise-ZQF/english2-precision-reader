"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2024-T3')
r.lex('''
one~one~num=一个
of~of~prep=的（连接所属或修饰关系）
biggest~big~adj=最大的
challenges~challenge~n=挑战
in~in~prep=在……方面
keeping~keep~v=使保持某种状态
unsafe~unsafe~adj=不能安全驾驶的
aging~age~adj=年长的；年纪渐大的
drivers~driver~n=驾驶员
off~off~prep=离开（道路）；不在……上
road~road~n=道路
is~be~v=是
convincing~convince~v=说服
that~that~conj=引出所说的具体内容
it's~it is~pron+v=这是（某种情形）
time~time~n=时候
to~to~inf=不定式标记
turn~turn~v=交出（turn over）
over~over~adv=与turn构成“移交；交出”
keys~key~n=车钥匙
complete~complete~adj=彻底的
life-changer~life-changer~n=彻底改变生活的事
when~when~conj=当……时
someone~someone~pron=某个人
stops~stop~v=停止
forced~force~v=强迫
stop~stop~v=停止
driving~drive~v=开车；驾驶
said~say~v=说
former~former~adj=曾经担任的；前任的
risk~risk~n=风险
manager~manager~n=经理；管理者
anne~Anne~propn=安妮（人名）
m~M.~propn=M.（名字首字母）
menke~Menke~propn=门克（姓氏）
american~American~adj=美国的
medical~medical~adj=医学的
association~association~n=协会（美国医学会名称组成部分）
advises~advise~v=建议
physicians~physician~n=医生
situations~situation~n=情形
where~where~pron=引导定语从句，指所说情况下
clear~clear~adj=明确的
evidence~evidence~n=证据
substantial~substantial~adj=严重的；显著的
impairment~impairment~n=能力受损
implies~imply~v=表明；意味着
strong~strong~adj=重大的
threat~threat~n=威胁
patient~patient~n=患者
public~public~adj=公众的
safety~safety~n=安全
physician's~physician~n=医生的（所有格）
advice~advice~n=建议
discontinue~discontinue~v=停止；终止
privileges~privilege~n=获准的权利；驾驶资格
ignored~ignore~v=不理会；忽视
it~it~pron=形式主语，指通知管理部门这件事
desirable~desirable~adj=可取的
ethical~ethical~adj=合乎伦理的
notify~notify~v=通知
department~department~n=管理部门
motor~motor~n=机动车（Motor Vehicles名称组成部分）
vehicles~vehicle~n=车辆
wrote~write~v=写道
some~some~det=有些
states~state~n=州
require~require~v=要求
report~report~v=报告
others~other~pron=另一些（州）
allow~allow~v=允许
but~but~conj=但
 do~do~aux=与not构成否定
mandate~mandate~v=强制要求
reports~report~n=报告行为
while~while~conj=而（并列对比）
few~few~pron=少数几个州
consider~consider~v=认为
breach~breach~n=违反
confidentiality~confidentiality~n=保密义务
there~there~adv=引出存在结构
could~could~modal=可能
be~be~v=存在
liability~liability~n=法律责任
penalties~penalty~n=处罚
if~if~conj=如果
physician~physician~n=医生
does~do~aux=与not构成否定
act~act~v=行事
accordance~accordance~n=一致（in accordance with指依照）
with~with~prep=与（in accordance with构成依照）
state~state~n=州（修饰法律）
laws~law~n=法律
on~on~prep=关于
reporting~report~n=报告行为
counseled~counsel~v=告诫；提醒
part~part~n=一部分
problem~problem~n=问题
older~old~adj=年长的
safe~safe~adj=安全的
difficulties~difficulty~n=困难
are~be~aux=与addressed构成被动语态
addressed~address~v=处理；应对
piecemeal~piecemeal~adv=零散地；缺乏统筹地
by~by~prep=由（指出行为实施者）
different~different~adj=不同的
professions~profession~n=专业群体；专业领域的人士
focuses~focus~n=关注重点
including~including~prep=包括
gerontologists~gerontologist~n=老年学家
highway~highway~n=公路
administration~administration~n=管理
officials~official~n=官员
automotive~automotive~adj=汽车的
engineers~engineer~n=工程师
gerontologist~gerontologist~n=老年学家
elizabeth~Elizabeth~propn=伊丽莎白（名字）
dugan~Dugan~propn=杜根（姓氏）
there's~there is~adv+v=存在；有
national~national~adj=国家的
institute~institute~n=研究所
 driver~driver~n=驾驶员
studies~study~n=研究
need~need~v=需要
better~good~adj=更可靠的
what~what~pron=什么事物（引出需要弄清的内容）
makes~make~v=使……变得
can~can~modal=能够
help~help~v=起帮助作用
thing~thing~n=事情；办法
seem~seem~v=似乎
work~work~v=奏效；起作用
requiring~require~v=要求
person~person~n=人（in person亲自）
for~for~prep=为了；以……为目的
license~license~n=驾照
renewal~renewal~n=换证；续期
mandatory~mandatory~adj=强制性的
in-person~in-person~adj=亲自到场的
was~be~v=与associated构成“与……有关联”
associated~associated~adj=有关联的
per~per~prep=每（per cent构成百分之）
cent~cent~n=百分之一（per cent构成百分之）
reduction~reduction~n=减少
fatal~fatal~adj=致命的
crashes~crash~n=交通碰撞事故
involving~involve~v=涉及
according~accord~v=与to构成“根据”
study~study~n=研究
passing~pass~v=通过（测试）
vision~vision~n=视力
tests~test~n=测试
also~also~adv=也
produced~produce~v=带来；产生
similar~similar~adj=相似的
decline~decline~n=下降
those~those~det=那些，指85岁及以上驾驶员
although~although~conj=尽管；不过
appeared~appear~v=似乎
no~no~det=没有
benefit~benefit~n=好处；额外收益
from~from~prep=从……得到；来自
combining~combine~v=把……结合
two~two~num=两种，指到场换证与视力测试
many~many~det=许多
 don't~do not~aux=不（否定助动词）
see~see~v=就诊；看医生
eye~eye~n=眼睛（eye doctors为眼科医生）
doctors~doctor~n=医生
can't~cannot~modal=不能
 afford~afford~v=负担得起
primary~primary~adj=基层的；初级的（医疗）
care~care~n=医疗；照护
providers~provider~n=服务提供者，指医护人员
have~have~v=有；处于某种状况
hands~hand~n=手（have hands full构成忙不过来）
full~full~adj=满的（have hands full构成忙不过来）
may~may~modal=可能
able~able~adj=能够的
follow~follow~v=跟进（follow through）
through~through~adv=一直到底（follow through持续跟进）
patients~patient~n=患者
who~who~pron=引导定语从句，指患者
trouble~trouble~n=困难
because~because~conj=因为
heads~head~n=头
remember~remember~v=记住
going~go~v=前往
gotten~get~v=变得
shorter~short~adj=身高变矮的
haven't~have not~aux=没有（完成时的否定）
changed~change~v=调整；改变
seat~seat~n=座椅
settings~setting~n=调节设置；位置
sufficiently~sufficiently~adv=充分地
reach~reach~v=够到
car~car~n=汽车
pedals~pedal~n=踏板
easily~easily~adv=轻松地
as~as~conj=与long as构成“只要”
long~long~adv=与as long as构成“只要”
other~other~adj=其他的
cars~car~n=汽车
roads~road~n=道路
self-driving~self-driving~adj=自动驾驶的
won't~will not~modal=不会；不能
solve~solve~v=解决
problems~problem~n=问题
avoiding~avoid~v=避开
dangers~danger~n=危险
posed~pose~v=造成；带来
all~all~det=所有的
human~human~adj=人类的
would~would~modal=就会（假设所需条件）
too~too~adv=过于
algorithms~algorithm~n=算法
more~more~pron=更多的行动
improve~improve~v=改善
we're~we are~pron+aux=我们将要（be going to）
100-year~100-year~adj=长达一百年的
lives~life~n=寿命
90-year-old~90-year-old~n=九十岁的人
drive~drive~v=驾驶
comfortably~comfortably~adv=舒适地
''')
r.word('P1-S1','them','他们，指不再适宜驾驶的年长驾驶员','they','pron')
r.word('P1-S1',"it's",'该是……的时候了（it is time to结构）','it is','pron+v')
r.word('P1-S2','is','与forced构成被动语态','be','aux')
r.word('P2-S1','driving','驾驶的（修饰能力损伤）','driving','adj',occ=1)
r.word('P2-S1','to','对（患者及公众构成威胁）','to','prep',occ=1)
r.word('P2-S1','is','与ignored构成被动语态','be','aux',occ=1)
r.word('P2-S1','in','在……情形下','in','prep')
r.word('P2-S2','report','一项报告行为','report','n',occ=2)
r.word('P2-S3','in','与accordance with构成“按照”','in','prep')
r.word('P3-S1','with','具有（不同关注重点）','with','prep')
r.word('P3-S1','others','其他专业人士','other','pron')
r.word('P3-S3','on','关于（证据内容）','on','prep')
r.word('P4-S1','that','引导定语从句，指办法','that','pron')
r.word('P4-S1','does','确实（强调助动词）','do','aux')
r.word('P4-S1','report','到场；报到','report','v')
r.word('P4-S1','in','与person构成“亲自”','in','prep')
r.word('P4-S2','with','与……有关联（associated with）','with','prep')
r.word('P4-S2','in','在……方面（事故数的下降）','in','prep')
r.word('P4-S2','or','或者；及（85 or older为85岁及以上）','or','conj')
r.word('P4-S2','to','与according构成“根据”','to','prep')
r.word('P4-S3','for','对（该年龄人群而言）','for','prep')
r.word('P4-S3','in','在……方面（事故数下降）','in','prep')
r.word('P5-S2','with','对（跟进服务的患者）','with','prep')
r.word('P5-S2','turn','转动（头部）','turn','v')
r.word('P5-S2','where','往哪里；目的地','where','adv')
r.word('P5-S2','are','与going构成进行时','be','aux')
r.word('P5-S2','have','与gotten构成现在完成时','have','aux',occ=3)
r.word('P6-S1','are','存在（there are）','be','v')
r.word('P6-S1','on','在（道路）上','on','prep')
r.word('P6-S2','many','多的（算法数量）','many','det')
r.word('P6-S2','those','那些（人类驾驶员）','those','det')
r.word('P6-S3','do','做；采取行动','do','v')
r.word('P6-S4','have','拥有（百年寿命）；活到','have','v')
r.word('P6-S4','going','与be going to构成将来打算或预测','go','aux')
r.word('P6-S4','that','引导定语从句，指汽车','that','pron')
r.sentence('P5-S2')['chunks']=chunks(r,'P5-S2','and may|with patients|who have|because|or have gotten|and haven\'t|to reach','基层医疗人员已忙得不可开交，|可能无法持续跟进，|那些患者，|他们在开车方面有困难，|因为他们无法转头或记不住目的地，|或身体变矮了，|却没有充分调整座椅位置，|使自己能轻松踩到踏板。')
notes={
'P1-S1':'unsafe限定不适宜驾驶的群体，并非所有老人；it is time结构与turn over交出钥匙。',
'P1-S2':'life-changer名词，when时间条件，is forced被动，风险经理身份同位语。',
'P2-S1':'两where条件同时满足，驾驶能力严重受损及建议被忽视，it形式主语指notify；不扩大伦理建议。',
'P2-S2':'三个州群体要求/允许不强制/视为违密并列，第二report名词而第一动词。',
'P2-S3':'could可能而非必然，if不依法行事限定责任产生条件，in accordance with固定表达。',
'P3-S1':'gerontologist词性从错误动词改为名词；focuses关注重点，piecemeal零散处理缺乏统筹。',
'P3-S2':'不存在统一研究机构，Older Driver Studies名称含义不当作普通词组。',
'P3-S3':'两个what分别致不安全的原因与有效措施，better证据可靠性，不擅自给出解决答案。',
'P4-S1':'does强调确实，work奏效，report此处到场非报告，for表到场目的。',
'P4-S2':'31%下降非百分点，85及以上，associated with关联非证实因果，was非过去被动事件。',
'P4-S3':'those同85岁以上群体，两措施结合无额外收益，未否定各自效果；vision视力非愿景。',
'P5-S1':'see看医生非看见，afford to省略就诊动作，or两种可能不擅自合并成原因。',
'P5-S2':'have三处前两实义状态第三完成时，where目的地、are going进行；因转头/记忆或变矮未调座椅致困难。',
'P6-S1':'as long as条件，there are存在句，其他车辆仍在路上限定预测，self-driving完整复合词。',
'P6-S2':'posed造成危险，too many过多难以应付，would假设需求而非现实已采用算法。',
'P6-S3':'do实义行动，more代指更多措施，to improve目的不重复翻译need。',
'P6-S4':'100-year与90-year-old完整数字复合词，have寿命实义，be going to将来预测；that汽车定语。'}
r.word('P2-S1','driving','驾驶（作定语修饰损伤或资格）','driving','n')
r.word('P5-S2','be','处于能够的状态（be able to）','be','v')
r.word('P5-S2','have','与their hands full构成忙得不可开交','have','v',occ=1)
r.word('P1-S1','one','其中一个（最大的挑战之一）','one','pron',occ=1)
r.word('P1-S1','of','……之中的（one of表示其中之一）','of','prep',occ=1)
done(r,notes)
