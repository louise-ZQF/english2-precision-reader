# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2017-T1'),[f'{y}-T{n}' for y in [2015,2016] for n in range(1,5)])

lex(r,'''saturday@Saturday/name=星期六;morning/n=早晨;am@am/abbr=上午（a.m.）；不是be动词;runners@runner/n=跑步者;set/v=出发（set off）;off/adv=出发离开（set off）;run/v=跑步;around/prep=绕着；围绕;local/a=当地的;park/n=公园;parkrun@Parkrun/name=公园跑（活动名称）;phenomenon/n=现象;began@begin/v=开始;friends@friend/n=朋友;inspired@inspire/v=带动；促成;events@event/n=活动;uk@UK/name=英国;abroad/adv=在国外;free/a=免费的;staffed@staff/v=配备工作人员;by/prep=由；以……幅度；在by contrast中表对比;thousands@thousand/n=数千;volunteers@volunteer/n=志愿者;range/v=在……范围内变化;old/a=……岁的;grandparents@grandparent/n=祖父母辈;andrew@Andrew/name=安德鲁（人名）;baddeley's@Baddeley/name=巴德利的（姓氏所有格）;world/n=世界;record/n=纪录;seconds@second/n=秒;hour/n=小时;succeeding@succeed/v=取得成功;london's@London/name=伦敦的（地名所有格）;olympic/a=奥林匹克的;legacy/n=遗产；长期影响;failing@fail/v=失败；未能奏效;ten/num=十;monday@Monday/name=星期一;announced@announce/v=宣布;games@Games/name=奥运会（the Games简称）;olympiad@Olympiad/n=一届奥运会；奥林匹克周期;london@London/name=伦敦;planning@planning/n=规划;documents@document/n=文件;pledged@pledge/v=承诺;great/a=重大的；显著的;lever/v=撬动；带动;nation/n=国家；国民;sport/n=体育运动;lovers@lover/n=爱好者;couches@couch/n=沙发;fitter@fit/a=体能更好的;healthier@healthy/a=更健康的;produce/v=产生；培养;winners@winner/n=优胜者;happened@happen/v=发生；实现;weekly/a=每周的;did@do/aux=确实（强调后面的rise）;rise/v=增加;run-up/n=筹备期；前期;growing@grow/v=增长;falling@fall/v=下降;accelerating@accelerate/a=不断加快的;opposition/n=反对党;claims@claim/v=声称;primary/a=小学的;school/n=学校;pupils@pupil/n=小学生;halved@halve/v=减半;obesity/n=肥胖;risen@rise/v=上升；增加;among/prep=在……群体中;official/a=官方的;retrospections@retrospection/n=回顾；反思;failed@fail/v=未能做到;inspire/v=激励;offers@offer/v=提供;answers@answer/n=答案;parkun@Parkrun/name=公园跑（原卷Parkrun的误拼）;race/n=竞赛；比输赢的比赛;time/n=用时；时间;trial/n=测试（time trial为计时测试）;competitor/n=竞争对手;clock/n=时钟；计时;ethos/n=理念；宗旨;welcomes@welcome/v=欢迎;anybody/pron=任何人;joy/n=喜悦;puffed-out/a=气喘吁吁的;first-timer/n=初次参加者;clapped@clap/v=鼓掌欢迎；以掌声鼓励;top/a=顶尖的;talent/n=人才；优秀选手;shining@shine/v=表现出色；大放异彩;bidders@bidder/n=申办者;get/v=让；促使;elite/a=精英的；顶尖的;athletes@athlete/n=运动员;dual/a=双重的;aim/n=目标;mixed@mix/v=混合；混淆;up/adv=混在一起（mix up）；达到上限;stress/n=强调；重视;taking@take/v=参与（take part）;part/n=参与（take part）；部分;intimidating/a=让人望而却步的;newcomers@newcomer/n=新参加者;little/adv=稍微；一点（a little）;absurd/a=荒谬的;state/n=国家；政府;involved@involved/a=参与其中的;grassroots/a=基层自发的；草根的;concept/n=理念；构想;associations@association/n=协会;role/n=作用;providing@provide/v=提供;common/a=公共的；共同的;goods@good/n=资源；公共物品;making@make/v=使；确保（make sure）;sure/a=确定的；有保障的;space/n=空间；场地;playing@play/v=进行运动（playing fields为运动场）;fields@field/n=运动场地;pave/v=铺设（场地）；铺路;tennis/n=网球;netball/n=篮网球;courts@court/n=球场;encouraging@encourage/v=鼓励;provision/n=提供;activities@activity/n=活动;schools@school/n=学校;successive/a=历届的；相继的;presided@preside/v=主持；掌权见证（preside over）；主管;over/prep=关于；胜于；越过（按具体搭配）；selling@sell/v=出售;green/a=绿色的；有植被的;spaces@space/n=空间；场地;squeezing@squeeze/v=挤压；削减（资金）;authorities@authority/n=当局；地方政府;declining@decline/a=下降的；减少的;attention/n=重视；关注;instead/adv=代替（instead of整体为与其……不如……）;wordy/a=冗长的；话多的;worthy/a=立意良好的；值得肯定的;future/a=未来的;need/v=需要;thrive/v=蓬勃发展'''.replace('；selling@sell',';selling@sell'))
r.word('P1-S1','than','与more组成超过',pos='prep');r.word('P1-S1','every','每个',pos='det')
r.word('P1-S2','more','另外的活动场次；更多场次（不表明超过英国400场）',pos='pron');r.sentence('P1-S2')['translation']='公园跑起初只有十二位朋友参加，如今已带动英国开展400场活动，国外也另有开展。';r.sentence('P1-S2')['chunks'][-1]['zh']='国外也另有开展。'
r.word('P1-S4','times','完赛用时',lemma='time',pos='n');r.word('P1-S4','to','到（范围终点）',pos='prep');r.word('P1-S4','up','与to组成最高达到',pos='adv')
r.word('P2-S1','is','与succeeding或failing构成进行时',lemma='be',pos='aux')
r.word('P2-S2','on','在星期一',pos='prep');r.word('P2-S2','it','形式主语，指后文宣布的奥运举办内容',pos='pron');r.word('P2-S2','was','与announced构成被动语态',lemma='be',pos='aux');r.word('P2-S2','would','过去将来助动词，将会',pos='aux')
r.word('P2-S3','away','离开（沙发）',pos='adv')
r.word('P2-S4','more','更多的（优胜者）',pos='det')
r.word('P2-S6','by','增加了……（增长幅度）',pos='prep');r.word('P2-S6','to','在……之前的筹备期（run-up to）',pos='prep');r.word('P2-S6','was','与growing构成进行时',lemma='be',pos='aux')
r.word('P2-S7','are','与falling构成进行时',lemma='be',pos='aux');r.word('P2-S7','at','以……速度',pos='prep');r.word('P2-S7','rate','速度',pos='n');r.word('P2-S7','numbers','参加体育运动的人数',lemma='number',pos='n')
r.word('P2-S8','a','每（每周）',pos='det');r.word('P2-S8','at','与least组成至少',pos='prep')
r.word('P2-S10','as','与to组成关于；对于',pos='prep');r.word('P2-S10','to','与as组成关于',pos='prep',occ=1)
r.word('P3-S1','but','而是（not...but）',pos='conj');r.word('P3-S1','only','唯一的',pos='a')
r.word('P3-S3','is','有；存在（there is）',lemma='be',pos='v');r.word('P3-S3','as','同样程度地（as much...as）',pos='adv',occ=1);r.word('P3-S3','as','与……一样（比较连接词）',pos='conj',occ=2);r.word('P3-S3','being','与clapped构成被动语态',lemma='be',pos='aux');r.word('P3-S3','over','因……感到高兴',pos='prep',occ=1);r.word('P3-S3','over','跨过（终点线）',pos='prep',occ=2)
r.word('P3-S4','by','与contrast组成相比之下',pos='prep');r.word('P3-S4','more','更多的',pos='det')
r.word('P3-S5','was','与mixed up构成被动语态',lemma='be',pos='aux',occ=1);r.word('P3-S5','over','胜过；超过（重成功甚于参与）',pos='prep');r.word('P3-S5','on','对于（成功）的重视',pos='prep');r.word('P3-S5','for','对新参加者而言',pos='prep')
r.word('P4-S1','getting','变得；开始处于参与状态',lemma='get',pos='v');r.word('P4-S1','as','例如（such...as）',pos='prep')
r.word('P4-S2','there','there be存在结构引导词',pos='pron');r.word('P4-S2','is','有；存在（there is）',lemma='be',pos='v');r.word('P4-S2','be','与getting构成进行形式',pos='aux');r.word('P4-S2','getting','开始参与（get involved）',lemma='get',pos='v');r.word('P4-S2','for','政府发挥作用的方面',pos='prep',occ=1);r.word('P4-S2','for','供（运动场）使用的空间',pos='prep',occ=2)
r.word('P4-S3','over','主持；在其任内发生（preside over）',pos='prep');r.word('P4-S3','from','从地方当局预算中挤减资金',pos='prep')
r.word('P4-S4','do','做；采取（行动）',pos='v');r.word('P4-S4','conditions','条件',pos='n');r.sentence('P4-S4')['translation']='与其提出冗长而立意良好的战略，未来政府更需要多做实事，为体育蓬勃发展创造条件。';r.sentence('P4-S4')['chunks'][0]['zh']='与其提出冗长而立意良好的战略'
r.word('P4-S5','them','体育发展的条件',pos='pron')
checks(r,'''am为上午缩写非be，set off为出发，more than修饰五万人。
more abroad表示国外另有活动，不能无依据断言海外场次超过英国400场。
free为免费而非腾出，staffed by是由志愿者配备工作人员。
range为动词从……到……不等，times为完赛时间，纪录与一小时为两端。
两处is均构成进行时，公园跑成功与奥运遗产失败对照。
过去宣布奥运地点，would为过去将来；十周年时间关系保留。
lever为带动国民离开沙发，legacy为长期运动收益而非遗产财物。
more winners为更多优胜者，三个预期益处并列。
it指前面预期的奥运长期效益，not happened是未实现。
人数虽增近两百万但总人口增长更快，增长绝对量不等于比例改善。
falling进行时，rate为下降速度，accelerating说明加速。
反对党声称的是每周至少两小时运动的小学生人数几乎减半。
成年人和儿童肥胖增加，不把risen误成抬起物体。
as to为关于，官方反思未能激励一代人的原因。
offers为提供，Parkrun成功与前述官方失败形成答案关系。
原卷Parkun误拼保留，not race but time trial指仅与自身时间比较。
ethos为活动理念，anybody为任何人。
as much joy as比较两类参与者带来的相同喜悦，over分别是因为与跨过。
申办者既要大众参与又要精英成绩，by contrast为相比之下。
stress为强调非压力，over表偏重成功超过参与，was mixed up被动。
state为政府非州，grassroots指基层自发性，as举社区协会例子。
providing为动词提供，common goods为公共资源，courts为球场非法院。
preside over意为任内主持见证，三项政府作为均被批评。
conditions此处是体育发展条件非疾病，worthy不粗暴译成伪善。
them回指体育发展条件，at least为至少，worse比较级保留。''')
r.notes=['重新核定全部词位置，修复more abroad的过度比较、worthy的过强贬义，并纠正courts、state、conditions等跨语境义。']
save(r)
