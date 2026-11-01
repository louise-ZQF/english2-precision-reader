# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2017-T3'),[f'{y}-T{n}' for y in [2015,2016] for n in range(1,5)]+['2017-T1','2017-T2'])

lex(r,'''widespread/a=普遍存在的;immediately/adv=立即;go/v=去；上（大学）;conjunction/n=结合（in conjunction with为与……一起）；联合;high/a=高的;fast-moving/a=快速变化的;causes@cause/v=使；导致;completely/adv=完全地;overlook/v=忽视;possibility/n=可能性;taking@take/v=安排；利用（一段时间）;gap/n=间隔（gap year指大学前的间隔年）；空档;year/n=年;know/v=认识；知道;going@go/v=去；上学;fall/n=秋季;silly/a=傻的；愚蠢的;back/adv=晚一些；推迟（stay back）;school/n=学校；学院;natural/a=自然的；习惯的;spend/v=花费（时间）;academic/a=学业的；学术的;true/a=属实的；确实的;it's@it be/pron=这是（it is缩写）;condemn/v=否定；谴责;constant/a=持续的；挥之不去的;fear/n=担忧；恐惧;socially/adv=由社会促成或强化地;perpetuated@perpetuate/v=使长期延续；不断强化;graduate/a=研究生阶段的;medical/a=医学的;lucrative/a=收入丰厚的;despite/prep=尽管；与……相反;misconceptions@misconception/n=误解;hinder/v=妨碍;pursuits@pursuit/n=追求；目标;enhances@enhance/v=促进；增强;states@State/name=美国国名United States的一部分;australia@Australia/name=澳大利亚;take/v=安排；经历（间隔年）;prepared@prepare/a=准备充分的;perform/v=表现;pulling@pull/v=拖（后腿）；使落后;pushes@push/v=推动；使进步;ahead/adv=在前面；向前;by/prep=通过;preparing@prepare/v=使做好准备;independence/n=独立生活；独立性;new/a=新的;responsibilities@responsibility/n=责任;first-year/a=一年级的;lessen/v=减轻;blow/n=冲击;adjusting@adjust/v=适应;thrown@throw/v=抛入；突然置身于;brand/adv=全然（brand new为全新的）;environment/n=环境;making@make/v=使；让;easier@easy/a=更容易的;academics/n=学业;acclimation/n=适应新环境;blunders@blunder/n=失误;you're@you be/pron=你是；你处于（you are缩写）;convinced/a=确信的；被说服的;inherent/a=内在的；本身固有的;off/adv=暂停常规学习（一年）；休离;explore/v=探索；了解;interests@interest/n=兴趣;consider/v=考虑;future/a=今后的;choices@choice/n=选择;national/a=国家的（机构名一部分）;center/n=中心;statistics/n=统计（机构名一部分）;percent/n=百分之;majors@major/n=大学主修专业;considering/prep=考虑到；鉴于;basic/a=基础的;mandatory/a=必修的；强制的;leaves@leave/v=使处于某种状态;poor/a=不足的；欠佳的;understanding/n=理解；认识;vast/a=广泛的；大量的;possibilities@possibility/n=可能的选择;await/v=等待；将供……选择;listing@list/v=填列；列出;one/num=一个;applications@application/n=申请；申请表;switching@switch/v=转换；转专业;necessarily/adv=必然地（not necessarily为未必）;bad/a=坏的；不利的;depending@depend/v=取决于;costly/a=花费很大的;credits@credit/n=学分;too/adv=过于;late/adv=迟；晚;boston@Boston/name=波士顿;extra/a=额外的;switch/v=转换；转到;nursing/n=护理（专业）;figure/v=想清楚（figure out）；思考;out/adv=弄明白（figure out）；开始（start out）;initially/adv=最初；一开始;prevent/v=避免；防止;stress/n=压力;save/v=节省;later/adv=以后;toward/prep=朝向（目标）；以……为目标;up/adv=最终（end up）;end/v=最终成为（end up）；结束''')
r.word('P1-S1','to','去往；上（go to college）',pos='prep',occ=2);r.word('P1-S1','with','和……共同作用（in conjunction with）',pos='prep');r.word('P1-S1','in','与conjunction with构成结合、加上',pos='prep',occ=1)
r.word('P1-S2','after','与all组成毕竟',pos='adv');r.word('P1-S2','all','与after组成毕竟',pos='adv');r.word('P1-S2','is','与going构成进行形式表达将来',lemma='be',pos='aux');r.word('P1-S2','to','去往（大学）',pos='prep',occ=1);r.word('P1-S2','it','形式主语，指晚一年入学这件事',pos='pron')
r.word('P1-S3','for','持续（十二年）',pos='prep');r.word('P1-S3','to','去往（学校）',pos='prep',occ=1);r.word('P1-S3','that','关系代词，指非学业的事',pos='pron');r.word('P1-S3',"isn't",'is not的缩写；不是学业方面的',lemma='be',pos='v')
r.word('P2-S1','while','虽然；尽管',pos='conj')
r.word('P2-S2','falling','落后（fall behind）',lemma='fall',pos='v');r.word('P2-S2','on','在这种社会竞争中',pos='prep');r.word('P2-S2','whether','无论（列举不同的人生目标）',pos='conj');r.word('P2-S2','that','竞赛所追求的终点',pos='pron');r.word('P2-S2','to','通向（终点线）',pos='prep');r.word('P2-S2','else','其他的（everyone else指其他所有人）',pos='adv')
r.word('P2-S3','common','常见的',pos='a');r.word('P2-S3','it','间隔年',pos='pron',occ=1);r.word('P2-S3','it','学业追求的成功',pos='pron',occ=2)
r.word('P3-S1','better','更加充分地（修饰prepared）',lemma='well',pos='adv',occ=1);r.word('P3-S1','better','更好地（修饰perform）',lemma='well',pos='adv',occ=2);r.word('P3-S1','for','为大学生活做好准备（宾语college与in共用）',pos='prep');r.word('P3-S1','do','代替take a gap year，未经历间隔年',pos='aux')
r.word('P3-S2','rather','与than组成不是……而是……的对照',pos='adv');r.word('P3-S2','than','与rather组成而不是',pos='conj');r.word('P3-S2','for','为……做好准备',pos='prep');r.word('P3-S2','environmental','环境方面的',pos='a');r.word('P3-S2','with','应对（struggle with）',pos='prep');r.word('P3-S2','that','关系代词，指上述独立生活与责任等事项',pos='pron')
r.word('P3-S3','to','当谈到……（when it comes to）',pos='prep',occ=1);r.word('P3-S3','to','适应……（adjust to）',pos='prep',occ=2);r.word('P3-S3','being','与thrown构成被动语态',lemma='be',pos='aux');r.word('P3-S3','focus','集中精力；关注',pos='v');r.word('P3-S3','it','形式宾语，指更容易关注学业这件事',pos='pron')
r.word('P4-S1','of','确信某物的价值（convinced of）',pos='prep');r.word('P4-S1','then','那么（条件句的结果）',pos='adv');r.word('P4-S1','on','对（学业选择）的影响',pos='prep')
r.word('P4-S2','to','根据（according to）',pos='prep');r.word('P4-S2','for','教育统计中心名称中的用途或领域介词',pos='prep');r.word('P4-S2','once','一次',pos='adv')
r.word('P4-S3',"isn't",'is not缩写；并不令人惊讶',lemma='be',pos='v');r.word('P4-S3','with','使学生具有某种认识状态（leave...with）',pos='prep');r.word('P4-S3','that','关系代词，指大学中广泛的学业选择',pos='pron')
r.word('P4-S4','find','发现',pos='v');r.word('P4-S4','major','主修专业',pos='n');r.word('P4-S4','on','在（申请表）上',pos='prep');r.word('P4-S4','to','转到（另一专业）',pos='prep');r.word('P4-S4','taking','修读（课程）',lemma='take',pos='v')
r.word('P4-S5','on','取决于（depend on）',pos='prep');r.word('P4-S5','make','补足；补修（make up）',pos='v');r.word('P4-S5','up','补足（make up）',pos='adv');r.word('P4-S5','game','过程（比喻大学学业进程）',pos='n')
r.word('P4-S6','for','与example组成例如',pos='prep');r.word('P4-S6','have','必须（have to）',pos='aux');r.word('P4-S6','complete','完成（额外一年学业）',pos='v');r.word('P4-S6','were','倒装虚拟条件助动词，were you to相当于if you were to',lemma='be',pos='aux');r.word('P4-S6','to','转到（护理学院）',pos='prep',occ=3);r.word('P4-S6','department','院系',pos='n')
r.word('P4-S7','on','与later组成以后',pos='adv')
checks(r,'''社会压力与期待共同作用，in conjunction with为加上，gap year为大学前间隔年。
after all为毕竟，上大学的to为地点介词，反问承接延迟入学的社会压力。
for十二年表示持续，that是关系代词，isn't academic为非学业活动。
while为让步，感觉存在也不构成谴责间隔年的充分理由。
falling behind为落后，whether为无论，that指终点，graduate school为研究生院。
common为常见，第二个it指学业成功，不妨碍并可能促进两层意思保留。
prepared for与perform in共用college，better两处副词，比较对象为未间隔者。
环境变化非环保，by解释前进的方式，first-year为大学一年级。
when it comes to是当谈到，adjust to介词，brand new全新的，academics为学业。
convinced of确信，taking year off为暂离学业探索兴趣，then是那么。
80%至少换过一次专业，once为一次，according to根据非不定式。
considering为鉴于，leaves是使处于状态，vast possibilities是广泛选择。
major为名词专业非主要的，find为发现，taking courses为修课。
not necessarily未必，make up credits是补修学分，costly为花费大。
were you to为虚拟条件倒装，complete为动词，department为院系非劳工部。
figure out是想清楚，later on为以后，间隔年可避免后续压力和开支。''')
r.notes=['重审全部词位与间隔年论证，修正to/that/one/once、major、credits、complete等角色，保留研究语气与财务案例条件。']
save(r)
