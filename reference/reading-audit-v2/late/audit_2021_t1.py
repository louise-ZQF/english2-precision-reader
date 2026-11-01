"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2021-T1')
r.lex('''
reskilling~reskill~n=为适应新岗位进行技能再培训
is~be~v=是；处于所说状态
something~something~pron=某种事物
that~that~pron=关系词，指前面的事物
sounds~sound~v=听起来
like~like~prep=像
buzzword~buzzword~n=流行词
but~but~conj=但是
actually~actually~adv=实际上
requirement~requirement~n=必要措施；必需之事
if~if~conj=如果
plan~plan~v=计划；打算
to~to~inf=不定式标记，连接要做的动作
have~have~v=拥有；使形成
future~future~n=未来
where~where~conj=引出在该情境中的具体情况
lot~lot~n=很多（a lot of表示许多）
of~of~prep=……的（内容或所属关系）
would-be~would-be~a=希望成为的；即将成为的
workers~worker~n=劳动者；员工
do~do~aux=构成否定助动结构
get~get~aux=构成被动（get left behind）
left~leave~v=被落下；被淘汰
behind~behind~adv=在后面；无法跟上发展
know~know~v=知道
are~be~aux=构成正在进行的动作
moving~move~v=进入；走向
into~into~prep=进入
period~period~n=时期
jobs~job~n=工作；岗位
in~in~prep=在……范围或状态中
demand~demand~n=需求
will~will~aux=将会
change~change~v=变化
rapidly~rapidly~adv=迅速地
as~as~conj=也同样（承接上一变化）
requirements~requirement~n=任职要求
remain~remain~v=继续存在
research~research~n=研究
by~by~prep=由（引出研究机构）
world~World~name=世界（世界经济论坛名称部分）
economic~Economic~a=经济的
aforum~Forum~name=论坛
forum~Forum~name=论坛
finds~find~v=发现
on~on~prep=与average搭配表示平均而言
average~average~n=平均
per~per~prep=每（per cent表示百分比）
cent~cent~n=百分之一（per cent表示百分比）
core~core~a=核心的
skills~skill~n=技能
within~within~prep=在……内部；各岗位之中
job~job~n=岗位
roles~role~n=职责；岗位角色
very~very~adv=非常
short~short~a=短的
timeline~timeline~n=时间跨度；所剩时间
question~question~n=问题
who~who~pron=谁
should~should~aux=应当
pay~pay~v=支付
for~for~prep=为……支付或对应所述对象
thorny~thorny~a=棘手的
one~one~pron=一个问题（替代question）
individual~individual~a=单个的
companies~company~n=公司
temptation~temptation~n=诱惑
always~always~adv=总是
a let~let~v=让
let~let~v=让；放开（let go of指解雇）
go~go~v=离开；放走（let go of搭配）
whose~whose~pron=关系词，表示前述员工的
no~no~adv=不再（no longer）
longer~long~adv=更长时间（no longer指不再）
replace~replace~v=替换
with~with~prep=用……替换；与
those~those~pron=那些人
 does~do~aux=用于否定或强调的助动词
happen~happen~v=发生
at~at~prep=与best连用表示充其量
t~T~name=AT&T名称中的T
 often~often~adv=常常
given~give~v=被举为例子
 gold~gold~n=黄金（gold standard比喻最高标准）
 standard~standard~n=标准；典范
company~company~n=公司
 decided~decide~v=决定
a do~do~v=实施
massive~massive~a=大规模的
program~program~n=项目；计划
rather~rather~adv=与than连用表示而不是
than~than~conj=与rather连用表示而不是
fire-and-hire~fire-and-hire~a=解雇旧员工再招聘新员工的
strategy~strategy~n=策略
other~other~a=其他的
including~including~prep=包括
amazon~Amazon~name=亚马逊公司
disney~Disney~name=迪士尼公司
had~have~aux=构成过去完成时
also~also~adv=也
pledged~pledge~v=承诺
create~create~v=制定；创建
own~own~a=自己的
plans~plan~n=计划
when~when~conj=当……时
mismatch~mismatch~n=供需错配
broader~broad~a=范围更广泛的
economy~economy~n=经济领域
though~though~adv=不过；然而
focus~focus~n=关注焦点
usually~usually~adv=通常
turns~turn~v=转向
government~government~n=政府
 handle~handle~v=处理
efforts~effort~n=努力
canada~Canada~name=加拿大
elsewhere~elsewhere~adv=其他地方
been~be~v=一直处于所述状态
arguably~arguably~adv=可以说；有理由认为
languid~languid~a=迟缓无力的
best~good~a=最好的（at best为充其量）
situation~situation~n=局面
 frequently~frequently~adv=经常
hear~hear~v=听说
employers~employer~n=雇主
begging~beg~v=苦求
 even~even~adv=即使；甚至
times~time~n=时期
regions~region~n=地区
unemployment~unemployment~n=失业率；失业状况
high~high~a=高的
pandemic~pandemic~n=大流行病；此处疫情
indeed~indeed~adv=确实
february~February~n=二月
respectively~respectively~adv=分别；按前述顺序
rates~rate~n=比率；这里为失业率
united~United~name=联合的（United States国名部分）
states~States~name=州（United States指美国）
were~be~v=处于某水平或状态
generational~generational~a=一代人时间内的
lows~low~n=低点
worker~worker~n=劳动者
shortages~shortage~n=短缺
everywhere~everywhere~adv=到处
may~May~n=五月
spiked~spike~v=急剧上升
up~up~adv=向上；上升
a although~although~conj=尽管
although~although~conj=虽然
many~many~a=许多
disappeared~disappear~v=消失
all~all~pron=全部情况
done~do~v=这样做了（替代消失）
so~so~adv=如此；这样
medical~medical~a=医疗的
field~field~n=领域
 take~take~v=举出（例子）
obvious~obvious~a=明显的
example~example~n=例子
meant~mean~v=意味着
there~there~pron=存在句的形式词，表示有
still~still~adv=仍然
clear~clear~a=明显的
doctors~doctor~n=医生
nurses~nurse~n=护士
personnel~personnel~n=专业人员
course~course~n=与of构成当然
it~it~pron=形式词，引出所说的情况或后文内容
can~can~aux=能够
unemployed~unemployed~a=失业的
waiter~waiter~n=服务员
train~train~v=培训
him~he~pron=他（宾格，指服务员）
be~be~v=成为；是
doctor~doctor~n=医生
few~few~a=几；少数的
weeks~week~n=周
matter~matter~v=要紧（no matter表示不论）
pays~pay~v=支付
cannot~can~aux=不能
close~close~v=弥合；缩小（缺口）
gap~gap~n=技能缺口
maybe~maybe~adv=也许
others~other~pron=其他缺口
doing~do~v=这样做；弥合技能缺口
would~would~aux=将会（表示假设的结果）
benefit~benefit~n=益处
concerned~concerned~a=相关的
seems~seem~v=似乎
case~case~n=情况
sweden~Sweden~name=瑞典
forced~force~v=被迫
furlough~furlough~v=让员工暂时停职或无薪休假
cabin~cabin~n=客舱（cabin staff指空乘人员）
staff~staff~n=员工；工作人员
scandinavian~Scandinavian~name=北欧的（航空公司名的一部分）
airlines~Airlines~n=航空公司
start~start~v=启动
retraining~retrain~n=再培训
reskilled~reskill~v=重新培训技能
laid-off~laid-off~a=被暂时解雇或停职的
support~support~v=协助
hospital~hospital~n=医院
effort~effort~n=努力
was~be~v=是
collective~collective~a=多方共同参与的
involved~involve~v=涉及；让……参与
well~well~adv=与as构成也；以及
swedish~Swedish~a=瑞典的
university~university~n=大学
''')
r.word('P1-S1','that','关系词，指技能再培训这一事物','that','pron')
r.word('P1-S2','that','关系代词，指继续存在的岗位','that','pron')
r.word('P1-S3','that','从句连接词，引出研究发现','that','conj')
r.word('P1-S3','by','到……之前；不晚于（2022年）','by','prep',occ=2)
r.word('P1-S4','That','到2022年这一时间跨度','that','pron')
r.word('P2-S1','who','谁（问题中询问付费责任人）','who','pron')
r.word('P2-S2','For','对……而言','for','prep')
r.word('P2-S2','to','不定式标记，连接解雇动作','to','inf')
r.word('P2-S2','are','处于技能受需要的状态','be','v')
r.word('P2-S3','That','企业解雇旧员工再雇新人这一做法','that','pron')
r.word('P2-S4','AT','AT&T（美国电话电报公司）名称部分','AT','name')
r.word('P2-S4','is','构成被动语态（is given）','be','aux')
r.word('P2-S4','who','关系词，指作出决定的公司','who','pron')
r.word('P2-S4','do','实施；开展（培训项目）','do','v')
r.word('P2-S4','as','作为；被举为','as','prep')
r.word('P2-S4','with','采用某种策略（go with）','with','prep')
r.word('P2-S6','to','转向所指望的对象（turn to）','to','prep',occ=1)
r.word('P2-S7','have','构成现在完成时','have','aux')
r.word('P2-S7','given','造成；带来（某种局面）','give','v')
r.word('P2-S7','of','hear of的一部分，表示听说','of','prep',occ=1)
r.word('P2-S7','at','在……时期','at','prep',occ=2)
r.word('P2-S7','for','向其求取的对象（beg for）','for','prep')
r.word('P3-S1','With','随着；在疫情背景下','with','prep')
r.word('P3-S2','at','处于所述失业率数值或低点','at','prep')
r.word('P3-S3','As','截至（as of）','as','prep')
r.word('P3-S3','of','与as构成截至','of','prep')
r.word('P3-S3','to','上升到的终点数值','to','prep')
r.word('P3-S4','take','举出；以……为例','take','v')
r.word('P3-S4','that','从句连接词，引出疫情造成的结果','that','conj')
r.word('P4-S1','for','为培训支付费用','for','prep')
r.word('P4-S1','no','与matter构成不论；不管','no','a')
r.word('P4-S1','it','培训这件事','it','pron',occ=2)
r.word('P4-S2','that','那个（服务员变医生的）技能缺口','that','a')
r.word('P4-S2','to','对……有利（to the benefit of）','to','prep')
r.word('P4-S3','That','重新培训其他岗位也有益这一情况','that','pron',occ=1)
r.word('P4-S3','that','关系代词，指短期再培训项目','that','pron',occ=2)
r.word('P4-S4','one','一项努力（代替effort）','one','pron')
r.word('P4-S4','as','与well as合成以及','as','conj')
# Remove a formerly misplaced advance translation of global demand; keep blocks local.
r.sentence('P3-S2')['chunks'][0]['zh']='2月份，分别为3.5%和5.5%，'
r.notes.append('2021-T1-P3-S2所给原卷本身按Canada、United States顺序列3.5%、5.5%，本文忠实保留原文国家与数字顺序，不据现实历史数据擅改英文。')
done(r,{
'P1-S1':'would-be为希望就业者，get left behind为被落下；if约束再培训必要性。',
'P1-S2':'as will倒装承接也会变化，任职要求对应仍存在的岗位而非新出现岗位。',
'P1-S3':'42%为平均岗位核心技能占比，by 2022为期限而非研究实施者。',
'P1-S4':'That指到2022年这段时间，timeline不是某项日程列表。',
'P2-S1':'who为疑问责任主体，pay for表示支付培训费用，thorny为棘手。',
'P2-S2':'let go of为解雇，whose先旧后新员工技能对应，后are省略in demand。',
'P2-S3':'not always为并非总是，不能译成企业从不这样做。',
'P2-S4':'AT&T整体为公司名，given as为被举为，rather than区分培训与解雇再招聘。',
'P2-S5':'had pledged为此前已承诺，own为各家公司自己的计划，未写已实施完成。',
'P2-S6':'though为插入转折，turn to为指望政府，mismatch是技能供需错配。',
'P2-S7':'languid at best为即使乐观评价也迟缓，失业率高与苦求工人构成反差。',
'P3-S1':'With为疫情背景，indeed强调失业率高，非预测未来情况。',
'P3-S2':'原卷国家与数字顺序保留，generational lows为一代人以来低点，短缺遍在。',
'P3-S3':'as of是截至五月，not all是并非全部短缺消失，保留13.3%与13.7%。',
'P3-S4':'to take是举例用法，there were为存在句，医务人员短缺为具体实例。',
'P4-S1':'not like否定数周培训服务员成医生的可行性，no matter who不论谁付费。',
'P4-S2':'close弥合技能缺口非关闭，others指其他缺口，所有相关者从中受益。',
'P4-S3':'furlough为暂时停职，90%为空乘比例，support指协助医院员工非替代医生。',
'P4-S4':'one替代effort，多方协作包括其他公司和大学，as well as为并列。'})
