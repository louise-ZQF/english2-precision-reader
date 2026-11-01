from audit_early_base import *
r=article('2012-T1','''
homework~homework~n=家庭作业
never~never~adv=从不；向来没有
terribly~terribly~adv=非常（not terribly为不太）
parents~parent~n=家长
recent~recent~a=近年的
scorned~scorn~v=不屑；鄙视
school~school~n=学校
 districts~district~n=学区
across~across~prep=遍及；在各处
country~country~n=全国
most~most~adv=最近（与recently构成时间强调）
recently~recently~adv=最近
los~Los~name=洛杉矶地名的一部分
angeles~Angeles~name=洛杉矶地名的一部分
unified~Unified~name=联合（洛杉矶联合学区名称的一部分）
revising~revise~v=重新考虑；修订
thinking~thinking~n=看法
educational~educational~a=教育方面的
ritual~ritual~n=惯例；例行做法
unfortunately~unfortunately~adv=遗憾的是
l.a.~Los Angeles~name=洛杉矶（缩写）
produced~produce~v=制定；出台
inflexible~inflexible~a=僵化的；缺乏弹性的
policy~policy~n=政策
mandates~mandate~v=强制规定
exception~exception~n=例外
advanced~advanced~a=高阶的
courses~course~n=课程
count~count~v=在评分中占比；计入成绩
student's~student~n=学生的
academic~academic~a=学业的
grade~grade~n=成绩
rule~rule~n=规定
meant~mean~v=旨在（be meant to）
address~address~v=解决；应对
difficulty~difficulty~n=困难
impoverished~impoverished~a=贫困的
chaotic~chaotic~a=生活混乱的
homes~home~n=家庭
completing~complete~v=完成
unclear~unclear~a=不清楚的
contradictory~contradictory~a=自相矛盾的
certainly~certainly~adv=当然
assigned~assign~v=布置（作业）
complete~complete~v=完成
expensive~expensive~a=昂贵的
equipment~equipment~n=设备
district~district~n=学区
essentially~essentially~adv=实际上；本质上
giving~give~v=给予（giving a pass为不追究）
pass~pass~n=免于追究；放过
complicated~complicated~a=复杂的
family~family~n=家庭
lives~life~n=生活状况
going~go~v=趋向；变得
riskily~riskily~adv=危险地
close~close~a=接近的
implication~implication~n=隐含意思
standards~standard~n=要求；标准
need~need~v=需要
lowered~lower~v=降低
poor~poor~a=贫困的
children~child~n=儿童
administrators~administrator~n=管理人员
say~say~v=说
schooling~schooling~n=学校教育
teachers~teacher~n=教师
allowed~allow~v=获准；被允许
assign~assign~v=布置（作业）
counting~count~v=在成绩中占比
grades~grade~n=成绩
easily~easily~adv=轻易地
skip~skip~v=不做；省略
half~half~det=一半的
see~see~v=看到；发现
little~little~det=很少；几乎没有
difference~difference~n=变化；差别
report~report~n=学业成绩报告（report card为成绩单）
cards~card~n=卡片（report cards整体为成绩单）
state~state~n=州
 tests~test~n=考试
do~do~v=做；完成
performed~perform~v=表现
did~do~v=做；完成（作业）
quite~quite~adv=相当；很
possible~possible~a=可能的
helped~help~v=起到帮助作用
empowering~empower~v=赋予自主权
find~find~v=寻找；发现
works~work~v=有效；起作用
best~well~adv=最好地；最适合
imposes~impose~v=强加
flat~flat~a=统一无差别的
across-the-board~across-the-board~a=一刀切的；统一适用的
addresses~address~v=解决；应对
none~none~pron=一个也没有
thorny~thorny~a=棘手的
questions~question~n=问题
finds~find~v=认为；判定
unimportant~unimportant~a=不重要的
achievement~achievement~n=学业成就；成绩
move~move~v=采取行动
reduce~reduce~v=减少
eliminate~eliminate~v=取消
assignments~assignment~n=布置的作业
conversely~conversely~adv=反过来说
matters~matter~v=重要；有实际作用
account~account~v=占（account for表比例）
significant~significant~a=相当大的
portion~portion~n=部分；比例
meanwhile~meanwhile~adv=同时
ensure~ensure~v=确保
receive~receive~v=收到；被布置
meaningful~meaningful~a=有意义的
appropriate~appropriate~a=适合的
subject~subject~n=学科
assigning~assign~v=布置作业
willing~willing~a=愿意的
review~review~v=审阅；批改
correct~correct~v=纠正；批改
put~put~v=使置于（put on hold为暂停）
hold~hold~n=暂停状态（on hold）
board~board~n=学区教育委员会
responsible~responsible~a=负责的
setting~set~v=制定
looks~look~v=调查（look into）
matter~matter~n=问题；事情
conducts~conduct~v=举行
hearings~hearing~n=听证会
right~right~adv=正确地；妥善地
''')
inherit(r,['2010-T1','2010-T2','2010-T3','2010-T4','2011-T1','2011-T2','2011-T3','2011-T4'])
r.word('P1-S1','with','受到（学生和家长欢迎的对象）',pos='prep');r.word('P1-S1','been','has been popular完成时中的系动词',lemma='be',pos='aux',occ=1);r.word('P1-S1','been','完成时被动助动词（been scorned）',lemma='be',pos='aux',occ=2)
r.word('P1-S2','are','现在进行时助动词（are revising）',lemma='be',pos='aux');r.word('P1-S2','on','关于（家庭作业的看法）',pos='prep')
r.word('P1-S3','which','关系代词，指政策',pos='pron');r.word('P1-S3','may','可以；在否定中表示不得',lemma='may',pos='aux');r.word('P1-S3','for','占（count for的搭配成分）',pos='prep');r.word('P1-S3','more','超过（more than）',pos='adv')
r.word('P2-S1','is','be meant to结构成分，整体为旨在',lemma='be',pos='aux');r.word('P2-S1','that','关系代词，指困难',pos='pron');r.word('P2-S1','have','遇到；存在（困难）',lemma='have',pos='v')
r.word('P2-S3','be','被动助动词（be assigned）',lemma='be',pos='aux');r.word('P2-S3','that','关系代词，指作业',pos='pron');r.word('P2-S3','on','on their own整体为独立地',pos='prep');r.word('P2-S3','do','完成；做',lemma='do',pos='v')
r.word('P2-S4','is','现在进行时助动词',lemma='be',pos='aux');r.word('P2-S4','to','向（不追究的学生）',pos='prep',occ=1);r.word('P2-S4','do','一般现在时否定助动词',lemma='do',pos='aux',occ=1);r.word('P2-S4','do','做；完成（作业）',lemma='do',pos='v',occ=2);r.word('P2-S4','to','接近于（close to）',pos='prep',occ=2);r.word('P2-S4','be','被动助动词（be lowered）',lemma='be',pos='aux');r.word('P2-S4','it','这（学区放过这些学生的做法）',pos='pron')
r.word('P3-S1','are','被动助动词（are allowed）',lemma='be',pos='aux');r.word('P3-S1','as','as much as中的程度成分',pos='adv',occ=1);r.word('P3-S1','as','as much as的比较连接词',pos='conj',occ=2);r.word('P3-S1','it','它（家庭作业）',pos='pron')
r.word('P3-S2','with','在……条件下（作业只占10%）',pos='prep');r.word('P3-S2','for','占（counting for）',pos='prep');r.word('P3-S2','no','不（no more than为不超过）',pos='adv')
r.word('P3-S3','do','表现（do well为表现好）',lemma='do',pos='v');r.word('P3-S3','on','在……中（考试）',pos='prep');r.word('P3-S3','what','……又如何（what about的提问成分）',pos='pron')
r.word('P3-S4','it','形式主语，后面that是可能的内容',pos='pron')
r.word('P3-S5','than','rather than整体为而不是',pos='conj');r.word('P3-S5','what','所……的办法（能奏效的方法）',pos='pron');r.word('P3-S5','for','对……而言（学生）',pos='prep')
r.word('P4-S2','to','对于（学生学业的作用）',pos='prep',occ=2);r.word('P4-S2','them','它们（作业）',lemma='they',pos='pron');r.word('P4-S2','for','占（count for的搭配成分）',pos='prep')
r.word('P4-S3','for','占（account for的搭配成分）',pos='prep')
r.word('P4-S4','does','做；采取（does nothing指无所作为）',lemma='do',pos='v');r.word('P4-S4','to','适合于（appropriate to）',pos='prep',occ=2);r.word('P4-S4','are','现在进行时助动词（are assigning）',lemma='be',pos='aux',occ=1)
r.word('P5-S1','be','被动助动词（be put on hold）',lemma='be',pos='aux');r.word('P5-S1','for','负责（responsible for）',pos='prep');r.word('P5-S1','into','与looks构成调查',pos='prep');r.word('P5-S1','while','在……期间（调查及听证期间暂缓）',pos='conj')
r.word('P5-S2','it','形式主语，指妥善处理作业这件事',pos='pron');r.word('P5-S2','for','对（行动主体学区）',pos='prep')
# Distinguish the noun matter from the verb matters; the previous corpus conflated them.
r.sentence('P5-S1')['translation']='这些家庭作业规定应当暂缓实施，让负责制定教育政策的学区教育委员会调查这一问题，并举行公开听证会。'
phrase(r,'P2-S1','is meant to','be meant to','旨在；目的是')
phrase(r,'P3-S2','no more than','no more than','不超过')
phrase(r,'P3-S5','what works best','what works best','最能奏效的方法')
checks(r,[
'never terribly popular为向来不太受欢迎，not terribly的程度不能译成完全无人喜欢。',
'学区插入例子与重新思考的主干区分，educational ritual为惯例非宗教仪式。',
'仅高阶课例外，may否定为不得，占分不超过10%而非占10%以上。',
'旨在解决学生做作业的困难；that关系词，have为遇到困难。',
'作者认为政策不清且矛盾，两个判断并列，不自动替政策作解释。',
'两处cannot限定不宜布置的作业，独立完成与不借昂贵设备分别保留。',
'giving a pass为不追究，do前后助动与实义分开；隐含降低标准非明文已降低。',
'教师获准自主安排作业量，as much as为想多少多少，it为作业。',
'作业占分不超过10%导致少做一半分差很小，不能将little译成没有任何差别。',
'州统考表现和完成作业两项同时成立的学生被提问，what about反问保留。',
'possible保留可能性而非已证因果，helped为起了帮助作用。',
'works动词起作用非作品；flat与across-the-board均为一刀切，不是平坦或董事会。',
'none为一个也未解决，thorny棘手非荆棘植物。',
'若不重要则应减取消，不应仅令占分近零；两项政策建议对照。',
'matters动词重要；account for为占比，非解释或账户。',
'未确保意义、适龄科目和批改工作量三方面，review与correct均动词。',
'matter此处问题非重要；school board为学区教育委员会，暂缓与调查听证并行。',
'not too late为仍来得及，right为正确妥善地而非权利或右边。'])
r.lex('''
cannot~cannot~aux=不能；无法
make~make~v=使
much~much~det=多少（作业量）
own~own~pron=自己（on their own）
public~public~a=公开的
same~same~a=同一的
students~student~n=学生
time~time~n=时间；时候
want~want~v=想要；愿意
yet~yet~conj=然而
''')
gaps(r)
if not r.missing():r.save()
