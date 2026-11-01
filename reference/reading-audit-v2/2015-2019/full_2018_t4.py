# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2018-T4'),[f'{y}-T{n}' for y in [2015,2016,2017] for n in range(1,5)]+[f'2018-T{n}'for n in [1,2,3]])

lex(r,'''combat/v=克服；应对;trap/n=陷阱；错误倾向;premium/n=高度重视（put a premium on）；优先地位;cal@Cal/name=卡尔（人名）;newport@Newport/name=纽波特（姓氏）;author/n=作者;focused@focused/a=专注的;distracted@distracted/a=分心的；注意力分散的;recommends@recommend/v=建议;habit/n=习惯;work/n=工作;focus/n=专注；注意力;distraction/n=干扰；分心;mastering@master/v=掌握;art/n=技巧；方法;lengthy/a=长时间的;retreats@retreat/n=远离日常干扰而专注工作的时段;dedicated@dedicate/v=专用于；投入于;task/n=任务;developing@develop/v=养成；形成;daily/a=每日的;ritual/n=固定习惯；例行安排;taking@take/v=采用（某种方式）;journalistic/a=记者式的（随时抓机会开展深度工作）;approach/n=方法；方式;seizing@seize/v=抓住（机会）；利用;moments@moment/n=时机；片刻;throughout/prep=贯穿；在整个……期间;whichever/det=无论哪一种;determine/v=确定；决定;length/n=时长；长度;time/n=时间；时段;stick/v=坚持（stick to）；遵守;interruptions@interruption/n=打断；干扰;get/v=使……完成（get...done）;scheduled@schedule/v=安排；排期;month/n=月;once/conj=一旦;calendar/n=日程表;protect/v=保护；确保不被占用;like/conj=像……一样;doctor's@doctor/n=医生的（所有格）;appointment/n=预约；约诊;meeting/n=会议;getting@get/v=使……完成（get...done）;rethink/v=重新考虑;prioritise/v=安排优先次序;craft/v=精心制定;lists@list/n=清单;harford@Harford/name=哈福德（姓氏）;messy@Messy/name=《混乱》（书名）;power/n=力量；作用;disorder/n=无序；混乱;lives@life/n=生活;divided@divide/v=把……分成;advised@advise/v=建议;set/v=列出（set out）；制定;out/adv=明示出来（set out列出）；外面;told@tell/v=告知；要求;detail/n=细节；详尽程度;by/prep=逐一（day by day一天天地）；按;assumed@assume/v=原以为；假定;well-structured/a=结构严密的；组织有序的;plans@plan/n=计划;effective/a=有效的;came@come/v=涉及；谈到（when it came to）；来到;execution/n=执行；实施;wrong/a=错误的;demotivated@demotivate/v=削弱……的积极性;argues@argue/v=主张；认为;render/v=使处于某种状态;list/n=清单;ineffective/a=无效的;leaving@leave/v=留下；留出;room/n=余地；空间;improvisation/n=临场灵活处理；随机应变;reap/v=获得；取得（成果）;order/n=与in...to组成为了（目的表达）;make/v=使；与the most of组成充分利用;energy/n=精力;need/v=需要;embrace/v=乐于接受；接纳;downtime/n=休息时段；放松时间;suggests@suggest/v=建议;lazy/a=懒散的（此处指放松休息）;idleness/n=闲暇；不做事的状态;vacation/n=假期；休假;indulgence/n=放纵；享乐;vice/n=恶习;indispensable/a=不可或缺的;brain/n=大脑;vitamin/n=维生素;d@D/name=维生素D名称中的字母D;body/n=身体;paradoxically/adv=看似矛盾地；出人意料地;necessary/a=必要的；不可缺少的;srini@Srini/name=斯里尼（人名）;pillay@Pillay/name=皮莱（姓氏）;psychiatry/n=精神病学;school/n=学院（Harvard Medical School哈佛医学院）;counterintuitive/a=有违直觉的;link/n=联系;productivity/n=生产率；工作效率;due/a=由于（be due to）；由……造成;way/n=方式;brains@brain/n=大脑;operate/v=运作；运行;unfocused/a=不专注的;tend/v=往往会；倾向于;realise/v=意识到;complete/v=完成;unfocus/n=非专注状态;circuits@circuit/n=神经回路''')
r.word('P1-S1','putting','给予（高度重视），put a premium on整体为高度重视',lemma='put',pos='v');r.word('P1-S1','on','对……高度重视（put a premium on）',pos='prep');r.word('P1-S1','being','处于忙碌状态（be的动名词）',lemma='be',pos='v');r.word('P1-S1','building','养成（习惯）',lemma='build',pos='v');r.word('P1-S1','focus','专注；集中注意力',pos='v')
r.word('P2-S1','are','有；存在（there are）',lemma='be',pos='v');r.word('P2-S1','to','掌握……的方法（approaches to）',pos='prep',occ=1);r.word('P2-S1','to','专注于（dedicated to）',pos='prep',occ=2);r.word('P2-S1','to','做某事的方法（approach to）',pos='prep',occ=3);r.word('P2-S1','be','无论是（be it列举备选方案）',pos='v');r.word('P2-S1','it','所采用的方法（引出备选项）',pos='pron')
r.word('P2-S2','key','关键；要点',pos='n');r.word('P2-S2','to','坚持（stick to）的搭配介词',pos='prep',occ=2);r.word('P2-S2','it','已确定的专注时段安排',pos='pron')
r.word('P3-S1','more','更多的事情（省略宾语名词）',pos='pron');r.word('P3-S1','less','更少的（修饰时间）',pos='det')
r.word('P3-S2','point','时刻；时间点',pos='n');r.word('P3-S2','have','使……安排好（have...scheduled）',pos='v');r.word('P3-S2','for','为接下来一个月安排',pos='prep')
r.word('P3-S3','on','列入（日程表）',pos='prep');r.word('P3-S3','this','这段（专注时间）',pos='det')
r.word('P4-S1','to','做某事的方法（approach to）',pos='prep',occ=1);r.word('P4-S1','more','更多事情（省略宾语名词）',pos='pron');r.word('P4-S1','less','更少的（修饰时间）',pos='det');r.word('P4-S1','in','与particular组成尤其',pos='prep')
r.word('P4-S2','points','提及；引向（point to）',lemma='point',pos='v');r.word('P4-S2','to','提到（point to）的搭配介词',pos='prep',occ=2);r.word('P4-S2','that','关系代词，指前面的研究',pos='pron');r.word('P4-S2','into','分成（divide into）',pos='prep');r.word('P4-S2','some','一部分学生；一组学生',pos='pron');r.word('P4-S2','were','与advised/told构成被动语态',lemma='be',pos='aux');r.word('P4-S2','study','学习（study activities学习活动）',pos='n',occ=2);r.word('P4-S2','plan','计划；安排',pos='v');r.word('P4-S2','in','以……详细程度（in detail）',pos='prep');r.word('P4-S2','much','大得多（修饰比较级more）',pos='adv')
r.word('P5-S1','while','虽然；尽管（预期与结果转折）',pos='conj');r.word('P5-S1','when','谈到；就……而言（when it came to）',pos='conj');r.word('P5-S1','it','when it came to中的形式主语，不另指具体物',pos='pron');r.word('P5-S1','to','涉及（when it came to）中的介词',pos='prep')
r.word('P5-S2','while','而；相比之下',pos='conj');r.word('P5-S2','for','为……留出（空间）',pos='prep');r.word('P5-S2','best','最好的（结果）',lemma='good',pos='a')
r.word('P6-S1','or','或者说；换种表达（解释休息）',pos='conj');r.word('P6-S1','as','正如……所说',pos='conj');r.word('P6-S1','most','最大程度（make the most of充分利用）',pos='pron')
r.word('P7-S1','as','和……一样（程度）',pos='adv',occ=1);r.word('P7-S1','as','正如；像……一样',pos='conj',occ=2);r.word('P7-S1','to','对于……而言',pos='prep',occ=1);r.word('P7-S1','to','对于……而言',pos='prep',occ=2);r.word('P7-S1','to','对于完成工作而言（necessary to）',pos='prep',occ=3);r.word('P7-S1','it','闲暇',pos='pron')
r.word('P8-S1','this','这种（指休息与效率的联系）',pos='det');r.word('P8-S1','to','由于（due to）中的介词',pos='prep')
r.word('P8-S2','being','处于专注或非专注状态',lemma='be',pos='v');r.word('P8-S2','on','针对（任务），与focused/unfocused搭配',pos='prep');r.word('P8-S2','they','人的大脑',pos='pron')
r.word('P9-S1','these','这些（工作任务）',pos='det');r.word('P9-S1','both','两类都（神经回路）',pos='det');r.word('P9-S1','focus','专注状态（修饰神经回路）',pos='n')
ph(r,'P1-S1','putting a premium on','put a premium on','高度重视；过分推崇');ph(r,'P2-S2','stick to','stick to','坚持；遵守');ph(r,'P4-S2','day by day','day by day','逐日；一天一天地');ph(r,'P5-S1','when it came to','when it comes to','谈到；就……而言');ph(r,'P5-S2','leaving room for','leave room for','为……留出余地')
checks(r,'''put a premium on忙碌是重视的对象，building养成习惯非建造，书名与解释均保留。
三个并列方法均受be it统领，dedicated与两个approach后的to皆介词，最后when只修饰记者式方法。
length为时长，key名词关键，stick to坚持已定时段而不是黏住任务。
get more done中的more指更多事情，less修饰时间，两个目的均保留。
have...scheduled是使工作安排好的结构，不是完成时；范围接下来大约一个月。
once时间条件，like类比守护约诊与会议一样保护工作时段。
前置修饰办法的to为介词，后接getting；craft制定清单而不是工艺。
两组本科生月度与逐日精细计划对照，were被动，study activities为学习活动非研究活动。
while让步说明原以为却错误，most effective最高级，实际结果为削弱积极性。
render使失效，while对比固定计划与灵活余地，reap获得成果非收割作物。
make the most of充分利用，energy为精力，or换述休息而非另一个互斥方案。
not just不是否定休息价值，as...as比较必要程度，indispensable与necessary to后接介词对象。
专名精神病学助理教授保持，may保留可能，due to引出大脑运作方式。
between两种状态切换，they指大脑，more efficient比较效率非更专注。
What主语从句与that表语从句还原，both要用两类回路，不增译成两类同时运转。''')
r.notes=['独立复核深度工作三种方法、月度/每日计划对照及休息与神经回路的因果论证；全部词位置实读核定。']
save(r)
