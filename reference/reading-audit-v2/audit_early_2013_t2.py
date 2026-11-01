from audit_early_base import *
r=article('2013-T2','''
immigrants~immigrant~n=移民
atlantic~Atlantic~name=大西洋
settlers~settler~n=定居者
sojourners~sojourner~n=暂居者
folks~folk~n=人们
permanent~permanent~a=永久的
intention~intention~n=意图；打算
stay~stay~v=留下
money~money~n=钱
arrived~arrive~v=到来
departed~depart~v=离开
quarter~quarter~n=四分之一
italian~Italian~a=意大利的
italy~Italy~name=意大利
affectionate~affectionate~a=亲切的
nickname~nickname~n=绰号
uccelli~uccelli~part=意大利语绰号的一部分，整体意为候鸟
di~di~part=意大利语绰号中的连接词
passaggio~passaggio~part=意大利语绰号的一部分，整体意为候鸟
birds~bird~n=鸟（birds of passage比喻往返移民）
passage~passage~n=迁徙；经过
rigid~rigid~a=僵化的
divide~divide~v=划分
newcomers~newcomer~n=新来者
legal~legal~a=合法的
illegal~illegal~a=非法的
hail~hail~v=称赞；欢迎并称为
brand~brand~v=贴上负面标签
aliens~alien~n=外国人；外来者
kicked~kick~v=驱逐（kicked out）
framework~framework~n=思维框架
contributed~contribute~v=促成
mightily~mightily~adv=极大地
broken~broken~a=失灵的
immigration~immigration~n=移民；移民制度
paralysis~paralysis~n=僵局；无法行动
fix~fix~v=修复
strict~strict~a=严格的
definitions~definition~n=定义
recognize~recognize~v=承认
thriving~thrive~v=生活得好；发展兴旺
gray~gray~a=灰色的；界限不明的
begin~begin~v=开始
solve~solve~v=解决
challenges~challenge~n=难题
crop~crop~n=农作物
pickers~picker~n=采摘工
violinists~violinist~n=小提琴手
construction~construction~n=建筑业
entrepreneurs~entrepreneur~n=创业者
engineers~engineer~n=工程师
health-care~health-care~n=医疗护理（作助手的定语）
aides~aide~n=助手；护理人员
physicists~physicist~n=物理学家
today's~today~n=如今的
energetic~energetic~a=积极的；活跃的
participants~participant~n=参与者
global~global~a=全球的
economy~economy~n=经济
driven~drive~v=推动
flow~flow~n=流动
prefer~prefer~v=更愿意
opportunity~opportunity~n=机会
calls~call~v=召唤（机会出现的比喻）
manage~manage~v=设法做到
place~place~n=地方
permission~permission~n=许可
straddle~straddle~v=跨越不同体系
jurisdictions~jurisdiction~n=司法管辖区；管辖范围
identities~identity~n=身份
ease~ease~n=轻松自如（with ease）
imagine~imagine~v=想象
productive~productive~a=有所作为的
committing~commit~v=作出承诺
staying~stay~v=留下
feel~feel~v=感到
here~here~adv=这里
belong~belong~v=属于
nations~nation~n=国家
honorably~honorably~adv=光明正大地；体面地
accommodating~accommodate~v=适应并容纳
motion~motion~n=人员流动
attitudes~attitude~n=态度
sides~side~n=双方
battle~battle~n=争论；政策对立
logic~logic~n=逻辑
right~right~n=对；正确的一方
wrong~wrong~n=错；错误的一方
opening~open~v=开辟
middle~middle~a=中间的；折中的
ground~ground~n=立场；空间
understanding~understand~v=理解
managing~manage~v=管理
requires~require~v=需要
paths~path~n=路径
outcomes~outcome~n=结果
accomplish~accomplish~v=实现
legally~legally~adv=合法地
existing~exist~a=现行的
''')
ids=[f'{y}-T{t}' for y in range(2010,2013) for t in range(1,5)]+['2013-T1'];inherit(r,ids)
r.word('P1-S2','had','有（意图）',lemma='have',pos='v');r.word('P1-S2','make','建立（永久家园）',lemma='make',pos='v',occ=1);r.word('P1-S2','make','挣（钱）',lemma='make',pos='v',occ=2)
r.word('P1-S3','while','而；同时（流入流出对照）',pos='conj');r.word('P1-S3','about','大约',pos='adv')
r.word('P1-S4','about','大约',pos='adv');r.word('P1-S4','good','永久（for good固定搭配）',lemma='good',pos='n');r.word('P1-S4','for','for good中的成分，整体为永久地',pos='prep',occ=2)
r.word('P1-S5','had','有（绰号）',lemma='have',pos='v')
r.word('P2-S3','as','把……称为',pos='prep');r.word('P2-S3','be','被动助动词（be kicked out）',lemma='be',pos='aux')
r.word('P2-S4','to','促成（contributed to的搭配成分）',pos='prep',occ=1);r.word('P2-S4','over','关于（政治僵局的主题）',pos='prep')
r.word('P2-S7','those','那些人（候鸟式移民）',pos='pron')
r.word('P3-S2','work','工作（流动的就业机会）',lemma='work',pos='n')
r.word('P3-S3','as','随着（机会出现）',pos='conj')
r.word('P3-S4','have','有（工作及家庭）',lemma='have',pos='v');r.word('P3-S4','another','另一个地方（省略place）',pos='pron')
r.word('P4-S1','with','有；获得（许可）',pos='prep',occ=1);r.word('P4-S1','with','以……方式（with ease为轻松自如）',pos='prep',occ=2)
r.word('P4-S2','for','持续（暂居一段时间）',pos='prep');r.word('P4-S2','to','对……作出承诺（committing to）',pos='prep',occ=2);r.word('P4-S2','as','当作（所想象的美国形象）',pos='prep')
r.word('P4-S3','there','那里（另一个国家）',pos='adv');r.word('P4-S3','to','属于（belong to）',pos='prep',occ=2);r.word('P4-S3','both','两个地方都（既这里也那里）',pos='adv')
r.word('P5-S2','up','与opening构成开辟',pos='part');r.word('P5-S2','means','意味着',lemma='mean',pos='v')
phrase(r,'P1-S5','uccelli di passaggio','uccelli di passaggio','候鸟（比喻暂居往返的移民）')
phrase(r,'P4-S1','with ease','with ease','轻松自如地')
checks(r,[
'跨大西洋移民中定居与暂居并列，sojourner不是旅游者职业。',
'倒装came those两类人共同到美国；make home安家与make money挣钱分开。',
'700万到来与200万离开是同一统计期，while对照流量。',
'约四分之一永久回意大利，for good并非为了好处。',
'绰号意大利语候鸟，不要求将外语拼写误当英文词根。',
'rigid为看法僵化而非身体僵硬。',
'合法非法与好坏为当下二分分类，不是作者事实认同。',
'hail与brand褒贬标签相对，alien为外来者不是外星人。',
'框架促成制度失灵与政治僵局，to为contribute搭配，over关于争论。',
'不是要增加类别而是改变思考方式，两need否定与肯定区分。',
'beyond为超越严格分类，不是要求忽视所有法律。',
'gray areas是身份制度界限不明，候鸟式移民在其中生活发展。',
'承认这些移民才可能着手解决，might为可能非保证。',
'七类工作者完整，crop采摘农作物不只水果，physicists物理学家非医生。',
'全球经济由三项流动驱动，work为工作机会非艺术作品。',
'机会召唤是随机会往返，不是真有人打电话命令。',
'在一地工作另一地安家，have为实义有，another代另一个地方。',
'有无许可都跨不同体系，ease轻松与法定许可非同一问题。',
'productive在此有所作为，committing to接动名词，承诺永久留不是必要条件。',
'两个国家都可归属，there为那里非存在结构，honorably光明正大。',
'适应人员流动需争论双方态度改变，不独指移民一方。',
'承认中间空间与多路径多结果，其中部分现制度难合法实现，未声称所有安排皆合法。'])
r.lex('''
bad~bad~a=坏的；不好的一类
both~both~det=双方的
century~century~n=世纪
come~come~v=来
example~example~n=例子（for example为例如）
family~family~n=家庭
forever~forever~adv=永久地
go~go~v=去
home~home~n=家园；家庭
how~how~adv=如何
included~include~v=包括
living~live~v=生活
long~long~a=长期的
making~making~n=形成过程（in the making为逐渐形成中）
many~many~det=许多
much~much~adv=大大地（加强more比较）
need~need~v=需要
new~new~a=新的
one~one~num=一
start~start~v=开始
states~States~name=美国国名United States的一部分
those~those~pron=那些人
united~United~name=美国国名United States的一部分
way~way~n=方式
where~where~adv=关系副词，在所说地方
world~world~n=世界
''')
r.word('P1-S2','home','回原籍国',lemma='home',pos='adv',occ=2)
r.word('P2-S3','out','与kicked构成“驱逐出去”',lemma='out',pos='part')
gaps(r)
if not r.missing():r.save()
