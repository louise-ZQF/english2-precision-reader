# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2016-T2'),['2015-T1','2015-T2','2015-T3','2015-T4','2016-T1'])

lex(r,'''biologists@biologist/n=生物学家;estimate/v=估计;million/num=百万;lesser/a=较小的（物种名lesser prairie chicken的一部分）;prairie/n=草原;chickens@chicken/n=松鸡（此处指草原松鸡）；鸟;kind/n=种类;bird/n=鸟;living@live/v=生活；栖息;stretching@stretch/v=延伸；绵延;grasslands@grassland/n=草原;once/adv=曾经;lent@lend/v=增添（颜色）；给予;red/n=红色;grey/a=灰色的；灰暗的;landscape/n=景色；地貌;midwestern/a=美国中西部的;southwestern/a=西南部的;united@United/name=联合的（United States美国国名一部分）;states@state/n=州;birds@bird/n=鸟;remain/v=剩下；继续存在;occupying@occupy/v=占据；分布于;species/n=物种;historic/a=历史上的;range/n=分布范围;crash/n=数量骤减;major/a=主要的;reason/n=原因;u.s.@U.S./name=美国;fish/n=鱼类（机构名一部分）;wildlife/n=野生动物;service/n=管理局（机构名一部分）;usfws@USFWS/name=美国鱼类及野生动物管理局;decided@decide/v=决定;formally/adv=正式地;list/v=列为；列入名录;threatened/a=受威胁的（保护等级）;chicken/n=松鸡（物种名中的chicken）;desperate/a=危急的;situation/n=处境;director/n=局长;daniel@Daniel/name=丹尼尔（人名）;ashe@Ashe/name=阿什（姓氏）;environmentalists@environmentalist/n=环保人士;disappointed/a=失望的;agency/n=机构；管理局;designate/v=认定；指定;endangered/a=濒危的（较受威胁更高的保护等级）;status/n=保护等级；地位;gives@give/v=赋予；给予;officials@official/n=官员;greater@great/a=更大的;regulatory/a=监管的;power/n=权力;crack/v=严厉打击（crack down on）;down/adv=加强限制（crack down on中的小品词）;threats@threat/n=威胁;others/pron=其他人;argued@argue/v=主张；认为;tag/n=标签；分类;gave@give/v=给予;government/n=政府;flexibility/n=灵活处理的余地;new/a=新的;potentially/adv=可能地;confrontational/a=对抗性的；易引发冲突的;conservation/n=保护（自然环境或物种）;approaches@approach/n=办法；方式;particular/a=具体的（in particular整体为尤其、具体来说）;called@call/v=呼吁（call for）;forging@forge/v=建立；形成;closer@close/a=更密切的;collaborations@collaboration/n=合作关系;western/a=西部的;governments@government/n=政府;uneasy/a=不安的；有顾虑的;action/n=行动;landowners@landowner/n=土地所有者;control/v=掌控；控制;estimated@estimate/v=估计的;chicken's@chicken/n=松鸡的（所有格）;habitat/n=栖息地;under/prep=根据；依照;plan/n=计划;example/n=例子（for example整体为例如）;prosecute/v=起诉;businesses@business/n=企业;unintentionally/adv=无意地；非故意地;kill/v=杀死;harm/v=伤害;disturb/v=惊扰;long/adv=与as...as组成只要;signed@sign/v=签署;range-wide/a=覆盖整个分布区的;management/n=管理;restore/v=恢复;negotiated@negotiate/v=协商制定;by/prep=由（被动动作的发出者）；到……程度;requires@require/v=要求;individuals@individual/n=个人;damage/v=破坏;operations@operation/n=经营活动;fund/n=基金;replace/v=替换；补偿;every/det=每一个;acre/n=英亩（面积单位）;destroyed@destroy/v=破坏;acres@acre/n=英亩; suitable/a=适宜的;used@use/v=使用；用于;compensate/v=补偿;set/v=留出；设定;aside/adv=专门留出（set aside）;interim/a=阶段性的；暂时的;goal/n=目标;restoring@restore/v=恢复;populations@population/n=种群数量;annual/a=每年的;average/n=平均数;association/n=协会;agencies@agency/n=机构;wafwa@WAFWA/name=西部鱼类及野生动物机构协会;coalition/n=联盟;monitoring@monitor/v=监测;progress/n=进展;overall/adv=总体而言;let/v=让；使;driver's@driver/n=驾驶者的（比喻掌舵者）;seat/n=座位（driver's seat比喻主导地位）;managing@manage/v=管理;buys@buy/v=相信；认同;win-win/a=双赢的;rhetoric/n=说辞；修辞;congress@Congress/name=美国国会;trying@try/v=试图;block/v=阻止;dozen/n=一打；十二个;industry/n=行业;four/num=四;three/num=三;environmental/a=环保的;challenging@challenge/v=对……提出法律挑战;court/n=法院;surprisingly/adv=令人意外地;generally/adv=普遍地；一般而言;argue/v=主张；认为;goes@go/v=达到某种程度；推行;too/adv=过于;enough/adv=足够地;responsibility/n=责任;industries@industry/n=行业;pushing@push/v=推动；逼向;extinction/n=灭绝;says@say/v=说；指出;biologist/n=生物学家;jay@Jay/name=杰伊（人名）;lininger@Lininger/name=利宁格（姓氏）;out/adv=尝试实施（try out中的小品词）；go/v=推行；达到某程度;same/a=同一个；恰恰这些'''.replace('；go/v',';go/v'))
r.word('P1-S1','as','与many as组成多达',pos='adv',occ=1);r.word('P1-S1','as','与as many组成多达',pos='conj',occ=2);r.word('P1-S1','to','给……增添（lent red to）',pos='prep');r.word('P1-S1','on','在草原上',pos='prep');r.word('P1-S1','states','United States国名一部分，合指美国',lemma='State',pos='name')
r.word('P1-S2','some','大约（修饰数字）',pos='adv');r.word('P1-S2','about','大约',pos='adv')
r.word('P2-S1','as','认定为；列为',pos='prep')
r.word('P2-S4','pushed','敦促；推动（机构采取行动）',lemma='push',pos='v');r.word('P2-S4','as','认定为',pos='prep');r.word('P2-S4','that','关系代词，指status保护等级',pos='pron');r.word('P2-S4','on','针对（crack down on）',pos='prep')
r.word('P2-S6','in','与particular组成具体来说',pos='prep');r.word('P2-S6','for','呼吁（call for）中的搭配介词',pos='prep');r.word('P2-S6','with','与……合作',pos='prep',occ=1);r.word('P2-S6','with','对联邦行动感到不安（uneasy with）',pos='prep',occ=2);r.word('P2-S6','with','与……合作',pos='prep',occ=3);r.word('P2-S6','private','私人的；非政府所有的',pos='a')
r.word('P3-S1','for','与example组成例如',pos='prep');r.word('P3-S1','that','关系代词，指土地所有者和企业',pos='pron');r.word('P3-S1','as','与long as组成只要',pos='conj');r.word('P3-S1','it','美国鱼类及野生动物管理局',pos='pron')
r.word('P3-S2','that','关系代词，指个人与企业',pos='pron');r.word('P3-S2','with','用……替代（replace...with）',pos='prep');r.word('P3-S2','into','向基金缴入',pos='prep')
r.word('P3-S3','be','助动词，与used构成被动语态',pos='aux');r.word('P3-S3','set','专门留出（set aside）',pos='v')
r.word('P3-S4','set','设定（目标）',pos='v');r.word('P3-S4','to','恢复到（数量目标）',pos='prep');r.word('P3-S4','over','在接下来十年期间',pos='prep')
r.word('P3-S5','it','上述管理计划',pos='pron');r.word('P3-S5','job','任务',pos='n')
r.word('P3-S6','remain','继续处于（主导地位）',pos='v');r.word('P3-S6','for','在管理该物种方面',pos='prep')
r.word('P4-S2','are','助动词，构成进行时',lemma='be',pos='aux');r.word('P4-S2','at','与least组成至少',pos='prep')
r.word('P4-S3','far','远；力度大（go far比喻干预程度）',pos='adv');r.word('P4-S3','it','该管理计划',pos='pron')
r.word('P4-S4','is','与giving构成进行时',lemma='be',pos='aux');r.word('P4-S4','are','与pushing构成进行时',lemma='be',pos='aux');r.word('P4-S4','to','向；交给',pos='prep',occ=1);r.word('P4-S4','to','推向（灭绝）',pos='prep',occ=2);r.word('P4-S4','that','关系代词，指前面的industries',pos='pron');r.word('P4-S4','for','关于管理这种鸟的责任',pos='prep');r.word('P4-S4','it','这种草原松鸡',pos='pron')
ph(r,'P2-S1','U.S. Fish and Wildlife Service','U.S. Fish and Wildlife Service','美国鱼类及野生动物管理局')
ph(r,'P3-S6',"in the driver's seat",'in the driver\'s seat','掌握主导权；处于决策主导地位')
checks(r,'''as many as表示多达，lesser prairie chicken为物种名，lent red to指增添红色。
some和about均限定约数，16%对应栖息分布范围而非存活率。
crash为种群数量锐减，USFWS是机构，threatened为受威胁保护等级。
desperate指物种处境危急，非人的绝望心情。
环保人士失望源于保护等级不够严厉，未把were误判被动动作。
endangered为濒危，严于threatened；that修饰status，power为监管权力。
较低保护等级被认为有利于尝试少对抗方案，potentially保留可能性。
合作对象为州政府和私人地主，which与who各有明确先行词。
as long as为只要，签约是免予起诉的条件，并非无条件允许伤害。
每破坏一英亩补偿两英亩，pay into为缴入基金，比例不反转。
be used为被动，补偿对象是专门留出栖息地的土地所有者。
67,000是未来十年目标的年均种群数量，非每年增加该数。
it指计划，WAFWA为州机构联盟，job是监测任务。
driver's seat比喻决策主导权，remain此处不是剩余数量。
Not everyone为部分否定，buys是认同而非购买。
三类主体在联邦法院挑战计划，至少十二个仅限定行业团体数量。
行业与州认为干预过度，环保人士认为力度不足，两立场不能混同。
is giving和are pushing为进行时，it指鸟，to为交给和推向。''')
r.notes=['逐词重审保护等级、栖息范围、州与联邦权力和一比二补偿条款；复核全部句块及比喻。']
save(r)
