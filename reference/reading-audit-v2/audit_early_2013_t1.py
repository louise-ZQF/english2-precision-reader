from audit_early_base import *
r=article('2013-T1','''
essay~essay~n=文章
entitled~entitle~v=题为；命名为
author~author~n=作者
adam~Adam~name=亚当
davidson~Davidson~name=戴维森
relates~relate~v=讲述
joke~joke~n=笑话
country~country~n=产区（cotton country为棉花产区）
textile~textile~n=纺织业（作工厂的定语）
mill~mill~n=纺织厂
automated~automate~v=使自动化
average~average~a=普通水平的
employees~employee~n=员工
dog~dog~n=狗
feed~feed~v=喂养
davidson's~Davidson~name=戴维森的
article~article~n=文章
appeared~appear~v=发表；出现
point~point~n=观点
stubbornly~stubbornly~adv=持续顽固地（居高不下）
high~high~a=高的
unemployment~unemployment~n=失业率
 declining~decline~a=下降的
middle-class~middle-class~a=中产阶级的
incomes~income~n=收入
largely~largely~adv=主要地
drop~drop~n=下降
demand~demand~n=需求
recession~recession~n=经济衰退
advances~advance~n=进展；推进
globalization~globalization~n=全球化
information~information~n=信息
technology~technology~n=技术
revolution~revolution~n=革命；重大变革
rapidly~rapidly~adv=迅速地
replacing~replace~v=取代
labor~labor~n=劳动力
machines~machine~n=机器
foreign~foreign~a=外国的
skills~skill~n=技能
job~job~n=工作
lifestyle~lifestyle~n=生活方式；生活水平
officially~officially~adv=可以宣告地（强调这一判断）
won't~will not~aux=将无法；不会
employers~employer~n=雇主
above~above~prep=超过
cheap~cheap~a=成本低廉的
robotics~robotics~n=机器人技术
software~software~n=软件
automation~automation~n=自动化技术
genius~genius~n=聪明才智；高水平人才
therefore~therefore~adv=因此
needs~need~v=需要
extra~extra~n=过人之处；独特优势
unique~unique~a=独特的
value~value~n=价值
contribution~contribution~n=贡献
stand~stand~v=处于（stand out为脱颖而出）
whatever~whatever~pron=无论哪个
field~field~n=领域
employment~employment~n=就业；职业
yes~yes~part=的确（承认前述事实）
eating~eat~v=吞噬；取代（岗位）
forever~forever~adv=一直以来
there's~there has~aux=there has的缩写，与been组成一直存在
acceleration~acceleration~n=加速
notes~note~v=指出
ending~end~v=结束（截至某年）
factories~factory~n=工厂
shed~shed~v=裁减（员工）
fast~fast~adv=迅速地
erased~erase~v=抹去；抵消
gains~gain~n=增加的就业岗位
previous~previous~a=此前的
roughly~roughly~adv=大约
manufacturing~manufacturing~n=制造业（作岗位的定语）
million~million~num=百万
total~total~n=总计
disappeared~disappear~v=消失
services~service~n=服务
thing~thing~n=事情
know~know~v=知道
sure~sure~a=确定无疑的
advance~advance~n=进展
require~require~v=要求
t~technology~name=技术（I.T.缩写中的T）
better~good~a=更好的
things~thing~n=事情
support~support~v=支持
important~important~a=重要的
passing~pass~v=通过（法案）
kind~kind~n=种类
ensures~ensure~v=确保
post-high~post-high~a=高中之后的（post-high school education指高中后教育）
''')
ids=[f'{y}-T{t}' for y in range(2010,2013) for t in range(1,5)];inherit(r,ids)
r.word('P1-S1','making','取得成功；立足（Making It）',lemma='make',pos='v');r.word('P1-S1','it','Making It固定搭配成分，不单译',pos='pron');r.word('P1-S1','just','究竟；到底（加强how）',pos='adv');r.word('P1-S1','has','有（两名员工）',lemma='have',pos='v',occ=2);r.word('P1-S1','much','多大程度',pos='pron')
r.word('P1-S2','there','在那里（说明人和狗各自职责）',pos='adv')
r.word('P2-S1','pieces','文章',lemma='piece',pos='n');r.word('P2-S1','have','面临；存在（失业率与收入问题）',lemma='have',pos='v',occ=2);r.word('P2-S1','making','阐明；提出（观点）',lemma='make',pos='v');r.word('P2-S1','with','用（机器或外国工人替代）',pos='prep');r.word('P2-S1','are','进行时助动词（are replacing）',lemma='be',pos='aux')
r.word('P3-S2','average','普通水平；普通的时代（名词化）',lemma='average',pos='n');r.word('P3-S2','over','结束的',pos='a')
r.word('P3-S3','being','处于普通水平（动名词主语的系动词）',lemma='be',pos='v');r.word('P3-S3','what','所……的收入',pos='pron');r.word('P3-S3','used','过去常常（used to）',lemma='used to',pos='aux')
r.word('P3-S4','have','有；能获得（使用机会）',lemma='have',pos='v');r.word('P3-S4','to','获得……的机会（access to）',pos='prep');r.word('P3-S4','it','普通水平带来过去收入这件事',pos='pron');r.word('P3-S4','when','在……背景下（解释为何不能）',pos='conj')
r.word('P3-S5','out','与stand构成脱颖而出',pos='part')
r.word('P4-S1','been','完成进行时助动词（been eating）',lemma='be',pos='aux')
r.word('P4-S3','out','one out of three中的比例成分',pos='prep');r.word('P4-S3','about','大约（600万）',pos='adv');r.word('P4-S3','that','so fast that的结果连接词',pos='conj')
r.word('P5-S1','be','存在；有（there be）',lemma='be',pos='v')
r.word('P5-S2','for','for sure中的搭配成分，整体为确定无疑',pos='prep');r.word('P5-S2','i','信息（I.T.缩写中的I）',lemma='information',pos='name');r.word('P5-S2','have','接受；具备（教育）',lemma='have',pos='v')
r.word('P6-S1','average','普通水平；普通的时代（名词化）',lemma='average',pos='n');r.word('P6-S1','are','存在；有（there are）',lemma='be',pos='v');r.word('P6-S1','i','G.I.福利法案缩写的一部分，不是代词我',lemma='I',pos='name');r.word('P6-S1','has','有；享有（教育机会）',lemma='have',pos='v');r.word('P6-S1','to','享有……的机会（access to）',pos='prep',occ=3)
checks(r,[
'Making It为在美国立足；textile定语名词；第二has实义有员工而非完成时。',
'人喂狗、狗防人碰机器构成笑话，there为在那里而非there be形式。',
'原因主要需求下降另有全球化技术革命；which两进程，用机器或外劳替代原劳动力。',
'三处average都普通水平，earn lifestyle为挣得某种生活，不译成获得生活方式发明。',
'average名词化指普通水平的时代，officially为作者强调并无官方通告。',
'used to为过去常常，what省略的收入；won\'t否定今后凭普通水平挣得旧收入。',
'access为可获取性而非通道，cheap修饰低成本资源，robotics原型保留robotics。',
'extra在此名词过人之处，value贡献使人职业领域脱颖而出。',
'eating jobs比喻替代就业，forever为一直以来，will省略继续取代。',
'there\'s为there has非there is（后接been），只是加速非新出现。',
'10年内裁员抹去此前70年岗位增加，约三分之一即总计600万，非比例增加600万。',
'there be存在结构，变化具体列新岗位产品和服务。',
'I.T.的I为信息，have教育是接受教育，with每次进步引背景。',
'最重要莫过于通过21世纪福利法案，不是唯一可做之事；确保高中后教育机会。'])
r.lex('''
america~America~name=美国
best~good~a=最好的
both~both~adv=两者都
century~century~n=世纪
do~do~v=做
ever~ever~adv=以往任何时候
find~find~v=找到
great~great~a=大的；严重的（经济大衰退）
how~how~adv=多大程度；如何
just~just~adv=就是；确实（加强判断）
keep~keep~v=使……保持（远离机器）
make~make~v=使
many~many~det=许多
much~much~det=大量的
need~need~v=需要
new~new~a=新的
one~one~num=一个
over~over~a=结束的
products~product~n=产品
reason~reason~n=原因
recently~recently~adv=最近
school~school~n=学校
such~such~det=如此的
there~there~pron=存在结构there be的形式成分
where~where~adv=关系副词，指这样的世界
world~world~n=世界
''')
gaps(r)
if not r.missing():r.save()
