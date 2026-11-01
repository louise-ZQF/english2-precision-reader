from audit_early_base import *
r=article('2012-T3','''
judge~judge~n=法官
shook~shake~v=震动
biotech~biotech~a=生物技术的
industry~industry~n=生物技术产业
core~core~n=核心；根本（to its core为从根本上）
won~win~v=取得；赢得
patents~patent~n=专利
isolated~isolate~a=分离出来的
dna~DNA~name=脱氧核糖核酸
human~human~a=人类的
genes~gene~n=基因
patented~patent~v=授予专利
march~March~n=三月
ruled~rule~v=作出司法裁定
unpatentable~unpatentable~a=不能授予专利的
executives~executive~n=企业高管
violently~violently~adv=极度地；强烈地
agitated~agitate~a=激动不安的
biotechnology~biotechnology~n=生物技术
organisation~organisation~n=组织
bio~BIO~name=生物技术产业组织
trade~trade~n=行业（作组织的定语）
group~group~n=组织；团体
assured~assure~v=向……保证
members~member~n=成员；会员
preliminary~preliminary~a=初步的
step~step~n=步骤
longer~long~a=更漫长的
battle~battle~n=争斗；法律争议
july~July~n=七月
relieved~relieve~a=松了一口气的
temporarily~temporarily~adv=暂时地
appeals~appeal~n=上诉
court~court~n=法院
overturned~overturn~v=推翻（裁决）
prior~prior~a=先前的
ruling~rule~v=裁定
myriad~Myriad~name=米里亚德（基因公司名称）
genetics~Genetics~name=基因（Myriad Genetics公司名称的一部分）
indeed~indeed~adv=确实
hold~hold~v=持有；拥有（专利）
help~help~v=有助于
forecast~forecast~v=预测
woman's~woman~n=女性的
risk~risk~n=风险
breast~breast~n=乳房；乳腺（breast cancer为乳腺癌）
cancer~cancer~n=癌症
executive~executive~n=执行官
blessing~blessing~n=好事；有利结果
patients~patient~n=患者
alike~alike~adv=两者都；同样地
continue~continue~v=继续
attempts~attempt~n=尝试
personalised~personalise~a=针对个人特征的；个体化的
medicine~medicine~n=医疗
courts~court~n=法院
busy~busy~a=忙碌的
itself~itself~pron=本身
probably~probably~adv=很可能
critics~critic~n=批评者
main~main~a=主要的
arguments~argument~n=论据；反对理由
against~against~prep=反对
gene~gene~n=基因
product~product~n=产物
nature~nature~n=自然
suppress~suppress~v=压制
innovation~innovation~n=创新
reward~reward~v=奖励；给予回报
monopolies~monopoly~n=垄断权
restrict~restrict~v=限制
access~access~n=获得或使用的机会
genetic~genetic~a=基因的
tests~test~n=检测
myriad's~Myriad~name=米里亚德公司的（基因检测）
growing~grow~a=不断增加的
number~number~n=人数
last~last~a=上一年的
 task-force~task-force~n=专门工作组
urged~urge~v=敦促
reform~reform~n=改革
related~relate~a=相关的
october~October~n=十月
department~Department~n=部（Department of Justice为司法部）
justice~Justice~name=司法（司法部名称的一部分）
filed~file~v=正式提交
brief~brief~n=法律意见书
arguing~argue~v=主张；提出论证
molecule~molecule~n=分子
cotton~cotton~n=棉花
fibres~fibre~n=纤维
separated~separate~v=分离
seeds~seed~n=种子（此处棉籽）
despite~despite~prep=尽管
court's~court~n=法院的
unanswered~unanswered~a=尚无答案的
whether~whether~conj=是否
sequencing~sequence~n=测序
whole~whole~a=整个的
genome~genome~n=基因组
violates~violate~v=侵犯
individual~individual~a=单个的
reach~reach~v=到达；上诉到
supreme~Supreme~a=最高的（最高法院名称的一部分）
advances~advance~v=发展；进步
however~however~adv=不过；然而
suits~suit~n=诉讼
unlikely~unlikely~a=不大可能的
file~file~v=提出申请（专利）
molecules~molecule~n=分子
domain~domain~n=领域（public domain为不受专有权限制的公共领域）
studying~study~v=研究
interact~interact~v=相互作用
correlations~correlation~n=相关性
used~use~v=用来；使用
determine~determine~v=确定
causes~cause~n=原因；病因
disease~disease~n=疾病
predict~predict~v=预测
drug's~drug~n=药物的
efficacy~efficacy~n=疗效
eager~eager~a=急于；渴望的
win~win~v=获得
connecting~connect~v=联系起来
dots~dot~n=零散线索（connecting the dots的比喻用法）
explains~explain~v=解释说
hans~Hans~name=汉斯
sauer~Sauer~name=绍尔（姓氏）
lawyer~lawyer~n=律师
success~success~n=成功（指争取关联性专利成功）
determined~determine~v=决定
suit~suit~n=诉讼
issue~issue~n=争议问题
brought~bring~v=提起（诉讼）
mayo~Mayo~name=梅奥（诊所名称的一部分）
clinic~Clinic~n=诊所
hear~hear~v=审理（案件）
term~term~n=开庭期；审理期
held~hold~v=举办；召开（会议）
convention~convention~n=行业大会
included~include~v=包括；安排了
sessions~session~n=专题会议；培训场次
coach~coach~v=指导；培训
lawyers~lawyer~n=律师
shifting~shift~a=不断变化的
landscape~landscape~n=整体形势；制度环境
packed~pack~a=挤满人的；座无虚席的
''')
inherit(r,['2010-T1','2010-T2','2010-T3','2010-T4','2011-T1','2011-T2','2011-T3','2011-T4','2012-T1','2012-T2'])
r.word('P1-S1','to','达到（核心程度，to its core）',pos='prep')
r.word('P1-S2','for','针对（专利覆盖对象）',pos='prep',occ=1);r.word('P1-S2','for','持续（数十年）',pos='prep',occ=2);r.word('P1-S2','by','到……为止（2005年）',pos='prep');r.word('P1-S2','some','大约',pos='adv');r.word('P1-S2','were','被动助动词（were patented）',lemma='be',pos='aux')
r.word('P1-S3','were','系动词，是不能取得专利的',lemma='be',pos='v')
r.word('P1-S4','were','系动词，处于不安状态',lemma='be',pos='v')
r.word('P2-S1','they','他们（企业高管及行业人士）',lemma='they',pos='pron')
r.word('P2-S2','to','对……的专利（专利覆盖的基因）',pos='prep');r.word('P2-S2','that','关系代词，指两个基因',pos='pron',occ=2)
r.word('P2-S3','ruling','裁决（名词）',lemma='ruling',pos='n');r.word('P2-S3','to','对……而言（企业和患者）',pos='prep')
r.word('P3-S1','as','随着（行业发展）',pos='conj');r.word('P3-S1','at','对……的尝试（个体化医疗）',pos='prep');r.word('P3-S1','rather','相当；十分（修饰busy）',pos='adv')
r.word('P3-S2','over','结束的',pos='a')
r.word('P3-S3','may','可以（否定中表示不应授予）',lemma='may',pos='aux');r.word('P3-S3','be','被动助动词（be patented）',lemma='be',pos='aux');r.word('P3-S3','it','它（创新）',pos='pron',occ=2);r.word('P3-S3','to','获得……的机会（access to）',pos='prep');r.word('P3-S3','as','与such构成例如',pos='prep')
r.word('P3-S5','for','针对（专利改革对象）',pos='prep');r.word('P3-S5','to','与……有关（related to）',pos='prep')
r.word('P3-S6','no','与less than构成同样是、并不少于的强调',pos='adv');r.word('P3-S6','been','完成时被动助动词（been separated）',lemma='be',pos='aux');r.word('P3-S6','that','关系代词，指棉纤维',pos='pron',occ=2)
r.word('P4-S2','it','形式主语，指whether引出的疑问内容',pos='pron',occ=1);r.word('P4-S2','it','它（整个基因组）',pos='pron',occ=2)
r.word('P4-S3','yet','仍然；还有可能',pos='adv')
r.word('P5-S1','as','随着（行业进步）',pos='conj');r.word('P5-S1','have','产生；具有（影响）',lemma='have',pos='v')
r.word('P5-S2','for','针对（专利对象DNA分子）',pos='prep');r.word('P5-S2','are','被动助动词（are patented）',lemma='be',pos='aux',occ=2);r.word('P5-S2','most','大多数（人类DNA分子）',pos='pron')
r.word('P5-S3','are','现在进行时助动词（are studying）',lemma='be',pos='aux');r.word('P5-S3','be','被动助动词（be used）',lemma='be',pos='aux')
r.word('P5-S4','for','针对（取得专利的关联发现）',pos='prep',occ=1);r.word('P5-S4','for','为……服务；属于（BIO的律师）',pos='prep',occ=2)
r.word('P6-S1','be','被动助动词（be determined）',lemma='be',pos='aux');r.word('P6-S1','by','取决于；由……决定（诉讼结果）',pos='prep',occ=1);r.word('P6-S1','by','由（提起诉讼的诊所）',pos='prep',occ=2);r.word('P6-S1','which','关系代词，指这场诉讼',pos='pron')
r.word('P6-S2','on','关于（培训内容专利局面）',pos='prep');r.word('P6-S2','for','在……领域（专利）',pos='prep')
r.word('P6-S3','was','系动词，处于满员状态',lemma='be',pos='v')
phrase(r,'P2-S2','breast cancer','breast cancer','乳腺癌')
phrase(r,'P3-S1','personalised medicine','personalised medicine','个体化医疗')
phrase(r,'P6-S1','Mayo Clinic','Mayo Clinic','梅奥诊所')
checks(r,[
'法官裁决引起产业根本震动，to its core表示程度而非搬到核心。',
'patents名词仅为专利，patented动词为授予专利；两处for分别对象与时长。',
'unpatentable明确不可授专利，were是系动词并非被动专利动作。',
'violently程度极强不是暴力动作；agitated为激动不安状态。',
'BIO行业组织安抚成员，this仅初步步骤并不意味其已胜诉。',
'行业人士暂时放心，at least temporarily两层限制均保留。',
'上诉推翻先前裁决；两个基因帮助预测患乳腺癌风险，that修饰genes。',
'ruling本句名词裁决；blessing为好事，alike企业患者双方都受益是公司说法。',
'personalised medicine个体化医疗，法院忙碌与产业发展相联。',
'probably not over是很可能未结束，非案件已经结束。',
'三条反对理由逐项不漏，it第二处创新；专利名词不再混入动词释义。',
'number省略人数，越来越多人似乎赞同，seem保持推测。',
'工作组敦促基因检测专利改革，不是改革基因本身。',
'brief法律意见书；no less than表示同样自然产物，棉纤维关系从句完整。',
'上诉裁决不消除重大未答问题，Despite为让步而非原因。',
'是否测整个基因组侵犯内部单基因专利尚不明，两个it形式与指代不同。',
'案件仍可能到最高法院，may yet非已经审结；Court始终法院。',
'其他诉讼可能影响更大，suits非西装；have为产生影响。',
'file是申请专利非向法院提交；most指DNA分子，公共领域不受该专利专有权限制。',
'研究基因关联以判病因或药效，相关性不冒充确定因果。',
'connecting dots为找出线索关联，for分别专利对象和律师服务机构。',
'两后置修饰都属诉讼，which也指诉讼；term为开庭期而非术语。',
'held为举办会议非持有专利，coach动词指导，landscape为制度形势。',
'每场会议座无虚席，packed形容满员非打包动作。'])
r.lex('''
case~case~n=案件
each~each~det=每一个
example~example~n=例子（for example为例如）
how~how~adv=如何
impact~impact~n=影响
just~just~adv=仅仅
less~little~adv=较少（no less than整体为同样不亚于）
make~make~v=提出（论据）
public~public~a=公共的；可公开使用的
recently~recently~adv=最近
said~say~v=说
such~such~det=这样的（such as引出例子）
year~year~n=年
''')
gaps(r)
if not r.missing():r.save()
