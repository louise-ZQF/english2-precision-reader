# -*- coding: utf-8 -*-
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from reading_audit import Review
r=Review('2025-T2')
r.lex('''
about~about~prep=关于
accounts~account~v=占（比例，与for连用）
acute~acute~a=严重的；尖锐的（形容压力）
aims~aim~n=目标
already~already~adv=已经
answers~answer~n=解决办法
any~any~art=任何一个
are~be~aux=构成进行或被动结构的助动词
as~as~conj=随着
ask~ask~v=探讨；提出问题
at~at~prep=在……方面或层面
be~be~aux=被动结构助动词，不单译
become~become~v=变得
becoming~become~v=变得
begin~begin~v=开始
behind~behind~prep=落后于
better~good~a=更好的；做得更好的
breaking~break~v=崩溃（breaking point指承受极限）
by~by~prep=由；得到……支持
calling~call~v=呼吁（与for连用）
cancer~cancer~n=癌症
cannot~can~aux=不能
capacity~capacity~n=服务能力
care~care~n=医疗与照护服务
centre~centre~n=中央政府层面
challenges~challenge~n=挑战
clear~clear~a=明确的；清楚的
communities~community~n=社区
conditions~condition~n=疾病；健康问题
continues~continue~v=继续
conversation~conversation~n=讨论；对话
cost~cost~n=成本
create~create~v=创造；促进
crisis~crisis~n=危机
cross-government~cross-government~a=跨政府部门的
date~date~n=时代（out of date整体表示过时）
decades~decade~n=十年
demand~demand~n=医疗服务需求
despite~despite~prep=尽管
determinants~determinant~n=决定因素
diabetes~diabetes~n=糖尿病
different~different~a=不同的
distributed~distribute~v=分配
diverting~divert~v=分流（服务需求）
dominant~dominant~a=主要的
entitled~entitle~v=名为；题为
established~establish~v=建立；成立
estimated~estimate~v=据估算
example~example~n=例子（for example整体表示例如）
expectancy~expectancy~n=预期寿命（life expectancy的一部分）
facing~face~v=面临
failed~fail~v=未能做到
fix~fix~v=修补；解决既有体系的问题
for~for~prep=针对；对于
former~former~a=前任的
from~from~prep=从（范围起点）
functions~function~n=公共医疗卫生职能
future~future~n=未来
given~give~v=交给；赋予
greater~great~a=更强大的；更大的
grow~grow~v=增长
growing~grow~a=不断增加的
have~have~aux=完成时助动词，不译为有
health~health~n=健康
healthcare~healthcare~n=医疗服务
heavy~heavy~a=高昂的（费用）
high-quality~high-quality~a=优质的
honest~honest~a=坦诚的
hospital-centric~hospital-centric~a=以医院为中心的
hospitals~hospital~n=医院
how~how~adv=如何
illnesses~illness~n=疾病
important~important~a=重要的
improving~improve~v=改善
in~in~prep=在……中；在……方面
inaccessible~inaccessible~a=难以获得的
increasingly~increasingly~adv=日益；越来越
infant~infant~n=婴儿
invested~invest~v=投入（资源）
investment~investment~n=投资；资源投入
is~be~v=是；处于所说的状态
it~it~pron=它（指NHS体系）
lagging~lag~v=落后
launching~launch~v=启动；推出
leaders~leader~n=地方领导者
left~leave~v=使……不得不承担（费用）
life~life~n=寿命（life expectancy搭配）
like~like~prep=例如
live~live~v=生活
living~live~v=患有；与疾病共存（living with搭配）
local~local~a=地方的
long-term~long-term~a=长期的；慢性的
major~major~a=重大的
make~make~v=取得（进展）
managing~manage~v=管理；应付
many~many~pron=许多
maximise~maximise~v=尽可能提升
meaningful~meaningful~a=实质性的
meet~meet~v=满足（需求）
million~million~num=百万
ministers~minister~n=大臣；部长
model~model~n=服务模式
more~more~adv=更加
mortality~mortality~n=死亡（mortality rates指死亡率）
much~much~adv=大大地；程度上的强调
must~must~aux=必须
nation~nation~n=全国民众；国家
national~national~a=全国的；国家的
near~near~prep=接近
nearly~nearly~adv=将近
need~need~v=需要
needs~need~n=需求
new~new~a=新的
nhs~NHS~abbr=英国国民医疗服务体系
no~no~art=没有
number~number~n=数量
obesity~obesity~n=肥胖
of~of~prep=……的（连接限定关系）
offering~offer~v=提供
often~often~adv=通常
on~on~prep=在……方面
only~only~adv=只；仅仅
open~open~a=公开的；开放的
opt~opt~v=选择
other~other~art=其他的
out~out~part=与squeeze构成挤占；与of date构成过时
outcomes~outcome~n=最终健康状况；健康结果
pay~pay~v=付费
peers~peer~n=可比较的同类国家
people~person~n=人们
places~place~n=环境；所处场所
point~point~n=极限点（breaking point搭配）
policies~policy~n=政策
population~population~n=所服务的居民
populations~population~n=当地居民
power~power~n=权力
pressures~pressure~n=压力
price~price~n=费用（price tag搭配）
primary~primary~a=基层的；初级的（医疗）
private~private~a=私人的；私营的
programme~programme~n=计划
progress~progress~n=进展
providing~provide~v=提供
public~public~a=公共的
question~question~n=问题
rates~rate~n=比率
rather~rather~adv=而是（rather than整体表示而非）
reduce~reduce~v=减少
reducing~reduce~v=减少
reform~Reform~name=Reform智库（机构名）
reforms~reform~n=改革
rehearsed~rehearse~v=被反复讨论过；被反复提出
reimagining~reimagine~v=重新构想（工作计划名称中的词）
reliance~reliance~n=依赖
remain~remain~v=保留；继续留在
resources~resource~n=资源
responsible~responsible~a=负责的
result~result~v=由此产生
retain~retain~v=保留；继续沿用
rethink~rethink~n=重新审视
scrapped~scrap~v=取消；废止
served~serve~v=为……提供服务
service~service~n=服务；医疗服务体系
services~service~n=公共服务；医疗服务
should~should~aux=应该
simply~simply~adv=仅仅
social~social~a=社会的
socialise~socialise~v=社交
squeezing~squeeze~v=挤占（与out连用）
strategies~strategy~n=策略；行动计划
strategy~strategy~n=策略；行动计划
support~support~v=支持；为……提供照护
supported~support~v=得到支持
system~system~n=体系
 tag~tag~n=标价（price tag借指费用）
tank~tank~n=智库（think tank的一部分）
taxpayers~taxpayer~n=纳税人
ten~ten~num=十
than~than~conj=比；而非（rather than结构）
that~that~art=那个（指前述模式）
there~there~pron=there be存在结构的引导词，不译为那里
these~these~art=这些
think~think~n=思想研究（think tank整体为智库）
this~this~pron=这（指讨论与改革工作）
those~those~pron=那些人
 timely~timely~a=及时的
to~to~part=不定式标记，不单译
together~together~adv=共同地
treating~treat~v=治疗
treatment~treatment~n=治疗
two~two~num=二；两个
uk~UK~abbr=英国
understanding~understanding~n=了解；理解
urgent~urgent~a=迫切的；紧急的
very~very~adv=很；非常
visionary~visionary~a=有远见的
waitlists~waitlist~n=就医等候名单
wants~want~v=希望
was~be~v=是（过去时）
well~well~adv=充分地；已被反复地（修饰rehearsed）
what~what~art=哪些
when~when~conj=当……时
which~which~pron=关系代词，指前述医疗工作人员
who~who~pron=关系代词，指前述无法选择私人医疗的人
why~why~adv=为什么；……的原因
will~will~aux=将会
with~with~prep=随着；在……背景下
work~work~n=工作
workforce~workforce~n=医疗工作人员
worse~bad~adv=更糟的是
years~year~n=年
yet~yet~conj=然而；但是
''')
r.word('P1-S1','was','与established构成过去时被动语态',pos='aux',occ=1)
r.word('P1-S2','on','过去以后；经过（75 years on整体表示75年后）',pos='adv')
r.word('P1-S2','it','形式主语，指后面模式已经过时这一判断',pos='pron')
r.word('P1-S2','of','与out、date构成过时的固定表达，不单译',pos='prep')
r.word('P2-S1','to','到（范围的另一端）',pos='prep')
r.word('P2-S2','on','在……名单上',pos='prep')
r.word('P2-S2','than','超过（more than结构）',pos='conj')
r.word('P2-S2','is','与becoming构成进行时',pos='aux',occ=1)
r.word('P2-S2','is','与squeezing构成进行时',pos='aux',occ=2)
r.word('P2-S2','for','为……付费（pay for搭配）',pos='prep',occ=2)
r.word('P2-S3','is','处于接近极限的状态',pos='v')
r.word('P3-S1','to','针对；解决……的（answers to搭配）',pos='prep')
r.word('P3-S2','it','医疗服务需求（回指demand）',pos='pron')
r.word('P3-S3','needs','需要',lemma='need',pos='v')
r.word('P3-S3','more','更多资源（省略resource等名词）',pos='pron')
r.word('P3-S4','needs','需要',lemma='need',pos='v',occ=1)
r.word('P3-S4','be','联系服务能力与更强这一状态的系动词',pos='v')
r.word('P4-S2','That','这（指前述改革长期未能取得进展）',pos='pron')
r.word('P4-S2','is','与launching构成正在进行的动作',pos='aux',occ=2)
r.word('P4-S3','for','呼吁的内容（call for搭配的一部分）',pos='prep')
r.word('P5-S2','It','形式主语，不单译；真正内容在that从句中',pos='pron')
r.word('P5-S2','is','与estimated构成被动语态',pos='aux')
r.word('P5-S2','that','引出估算的内容从句，不单译',pos='conj')
r.word('P5-S2','for','与accounts构成占某比例的搭配，不单译',pos='prep',occ=2)
r.word('P5-S3','are','系动词，是（主语places置于其后）',pos='v')
r.word('P5-S3','is','与there构成存在句，表示有',pos='v')
r.word('P5-S4','are','与left构成被动，使纳税人不得不承担',pos='aux',occ=2)
r.word('P5-S4','that','关系代词，指疾病，result为这些疾病由此产生',pos='pron')
r.word('P6-S2','to','交给（give to搭配）',pos='prep')
r.word('P6-S2','that','关系代词，指有助于健康的公共服务',pos='pron')
notes=[
'复核NHS成立时的愿景与实际提供的服务；首个was为被动，第二个为系动。',
'核对75年后与英国健康挑战变化，that限定旧模式，不当作内容从句引导词。',
'核对范围起止与两个死亡率，peers指同类国家，不是同龄个人。',
'区分医疗难以获得的人群与公共投资被挤占的后果；不能选择不直接等同付不起。',
'which指医护人员而非压力，破折号说明已接近极限，acute是严重而非急性疾病。',
'answers是解决办法，well rehearsed为早已反复讨论，不是排练医疗。',
'减少、分流需求与仅仅管理需求对比，it回指需求。',
'Much more省略资源内容，needs为动词需要，不夸成强制义务。',
'capacity是社会照护能力，long-term conditions为慢性病，living with非地点。',
'保留any目标均未取得进展的否定范围，二十年策略与改革为背景。',
'Reform为智库专名、reforms为改革普通名词须区分；两处is结构不同。',
'纠正首块提前译入后块内容，两个呼吁事项并列，retain说明目前沿用。',
'区分改善全国民众健康与只修补NHS体系，rather than为选择对比。',
'校正分块不提前借用health outcomes，that引出估算内容，20%保持约数。',
'前半为倒装，后半there be存在句；yet保留缺少跨部门策略的转折。',
'取消政策后带来的疾病治疗费用由纳税人承担，result为关系从句动词。',
'how内容为医疗系统内权力资源分配，修正分块不提前译入地点限定。',
'两类职能按中央与地方对照，后置修饰说明地方负责人职责和认知优势。']
for s,note in zip(r.ss,notes):r.checked(s['id'],note)
s=r.sentence('P4-S3');s['chunks'][0]['zh']='我们共同呼吁，';s['chunks'][1]['zh']='就英国健康事业的未来进行更公开、更坦诚的讨论，'
s=r.sentence('P5-S2');s['chunks'][1]['zh']='医疗服务，';s['chunks'][2]['zh']='对健康结果的作用只占约20%。'
s=r.sentence('P6-S1');s['chunks'][1]['zh']='权力和资源，';s['chunks'][2]['zh']='应当如何在我们的医疗体系中分配。'
s=r.sentence('P2-S2');s['translation']=s['translation'].replace('无力选择付费私人医疗','无法选择自费私人医疗');s['chunks'][1]['zh']='对于无法选择自费私人医疗的人，医疗服务越来越难获得；'
s=r.sentence('P3-S3');s['translation']=s['translation'].replace('必须','需要');s['chunks'][0]['zh']=s['chunks'][0]['zh'].replace('必须','需要')
print('Missing:',r.missing());r.save()
