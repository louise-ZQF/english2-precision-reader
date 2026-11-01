# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2019-T3'),[f'{y}-T{n}' for y in [2015,2016,2017,2018] for n in range(1,5)]+['2019-T1','2019-T2'])
lex(r,'''farmers@farmer/n=农场主;complaining@complain/v=抱怨;labor/n=劳动力；用工;shortages@shortage/n=短缺;complaints@complaint/n=抱怨;unlikely/a=不大可能的;stop/v=停止;overhaul/n=彻底改革;immigration/n=移民；移民事务;obstructed@obstruct/v=阻挠；阻碍;straightforward/a=简便的；直接明了的;visa/n=签证;agricultural/a=农业的;foreign/a=外国的;change/v=改变；更换;losers@loser/n=受损者；输家;laborers@laborer/n=劳工；工人;undocumented/a=没有合法身份证件的；无合法移民身份的;immigrants@immigrant/n=移民;characteristics@characteristic/n=特征;workforce/n=劳动力；从业人员;today's@today/n=如今的（所有格）;predominantly/adv=大多数地；主要地;born@bear/v=出生;mexico@Mexico/name=墨西哥;settled/a=定居的；稳定居住的;rather/adv=与than组成而非；不是;migrating@migrate/v=迁移；流动;single/a=单身的；未婚的;they're@they be/aux=they are缩写，与后面动词构成进行时或被动；他们正在;aging@age/v=年龄增长；老龄化;start/n=开始；初期;century/n=世纪;crop/n=农作物;over/prep=超过（年龄）;age/n=年龄;crops@crop/n=农作物;bodies@body/n=身体;one/num=一；一个;oft-debated/a=经常被讨论的;cure/n=解决办法；补救办法;shortage/n=短缺;remains@remain/v=仍然是；仍处于;implausible/a=不切实际的；难以成立的;it's@it have/aux=it has缩写，与been构成完成时；它一直;along/adv=一直（all along）；从来;native/a=本土的；本国出生的;returning@return/v=返回；重返;mechanization/n=机械化;isn't@be not/v=is not缩写：不是;production/n=生产;corn/n=玉米;cotton/n=棉花;rice/n=水稻;soybeans@soybean/n=大豆;wheat/n=小麦;mechanized@mechanize/v=使机械化；实现机械化;high-value/a=高价值的;labor-intensive/a=劳动密集型的;strawberries@strawberry/n=草莓;need/v=需要;dairy/n=乳制品（dairy farms奶牛场）;robots@robot/n=机器人;share/n=份额；部分;milking/n=挤奶;long/a=长的；很长的;way/n=路；尚需经历的过程;go/v=走；完成（have a long way to go尚有很长的路要走）;automated@automate/v=使自动化；实现自动化;result/n=结果（as a result因此）;grown@grow/v=逐渐变得;reliant/a=依赖的;temporary/a=临时的；暂时的;guest/n=外来劳工（guest worker客籍劳工）;using@use/v=使用；持有（签证）;h-2a@H-2A/name=H-2A（美国临时农业劳工签证类别）;gaps@gap/n=缺口;starting@start/v=开始；起始;around/adv=大约;requests@request/n=申请；请求;visas@visa/n=签证;rose@rise/v=增加；上升;sharply/adv=急剧地;issued@issue/v=签发；发放;doubled@double/v=增加一倍；翻番;numerical/a=数量上的;cap/n=上限；限额;h-2b@H-2B/name=H-2B（美国临时非农业劳工签证类别）;nonagricultural/a=非农业的;work/n=工作;employers@employer/n=雇主;complain/v=抱怨;given@give/v=给予；提供;process/n=办理过程；流程;cumbersome/a=繁琐的；复杂费事的;expensive/a=昂贵的；成本高的;bureaucratic/a=官僚行政程序的;delays@delay/n=拖延；延误;led@lead/v=导致；致使;worker/n=工人；劳工;arrive/v=到达；到岗;job/n=工作；岗位;compounded@compound/v=加剧；使恶化;by/prep=由；被（引出施动者）;raids@raid/n=突袭执法行动;remove/v=遣走；移走;underground/adv=转入隐蔽状态；躲藏起来;percent/n=百分之……;tree-fruit/n=树生水果（此处修饰果树种植者）;growers@grower/n=种植者;raisin/n=葡萄干（raisin growers为制干葡萄种植者）;berry/n=浆果;short/a=短缺的；缺少的;responded@respond/v=作出应对;fruit/n=水果;imported@import/v=进口;later/adv=之后；后来;imports@import/n=进口水果；进口品;effect/n=与in组成实际上;import/v=进口；引进;food/n=食物；食品;pick/v=采摘；采收''')
r.word('P1-S1','been','与complaining构成完成进行时',lemma='be',pos='aux');r.word('P1-S1','of','抱怨……（complain of）',pos='prep');r.word('P1-S1','for','持续了（好几年）',pos='prep')
r.word('P1-S2','farm','农场；农业（名词修饰workers）',pos='n');r.word('P1-S2','without','如果不；没有（必要改革）',pos='prep')
r.word('P2-S1','create','建立（签证制度）',pos='v');r.word('P2-S1','that','关系代词，指更简便的签证',pos='pron');r.word('P2-S1','longer','更长时间',lemma='long',pos='adv')
r.word('P3-S1','farm','农场；农业（名词修饰laborers）',pos='n')
r.word('P3-S2','as','随着……',pos='conj');r.word('P3-S2','are','与changing构成进行时',lemma='be',pos='aux')
r.word('P3-S3','farm','农场；农业（名词修饰laborers）',pos='n');r.word('P3-S3','while','虽然；尽管',pos='conj')
r.word('P3-S5','this','本（世纪）',pos='det');r.word('P3-S5','about','大约',pos='adv')
r.word('P3-S6','are','超过35岁（补出前句省略表语）',lemma='be',pos='v')
r.word('P3-S7','picking','采摘；采收',lemma='pick',pos='v');r.word('P3-S7','hard','负担重的；吃力的（be hard on）',pos='a');r.word('P3-S7','on','对……构成负担（hard on）',pos='prep')
r.word('P3-S8','as','一样地（修饰implausible）',pos='adv',occ=1);r.word('P3-S8','as','和……一样（引出比较）',pos='conj',occ=2);r.word('P3-S8','been','一直是（不切实际的），完成时中的系动词',lemma='be',pos='v');r.word('P3-S8','all','从来（all along一直）',pos='adv');r.word('P3-S8','be','与returning构成将来进行时',pos='aux');r.word('P3-S8','to','返回到（农场）',pos='prep');r.word('P3-S8','farm','农场',pos='n');r.word('P3-S8','for','解决……（劳动力短缺）的',pos='prep');r.word('P3-S8','this','这种（用工短缺）',pos='det')
r.word('P4-S1','answer','解决办法',pos='n');r.word('P4-S1','either','也（用于否定句）',pos='adv');r.word('P4-S1','yet','还；到目前为止',pos='adv')
r.word('P4-S2','been','与mechanized构成完成被动',lemma='be',pos='aux');r.word('P4-S2','as','例如（such as）',pos='prep')
r.word('P4-S3','farms','农场（dairy farms奶牛场）',lemma='farm',pos='n');r.word('P4-S3','do','承担；完成（挤奶工作）',pos='v');r.word('P4-S3','have','有（尚待走的路）',pos='v');r.word('P4-S3','before','在……之前（距离实现自动化尚需）',pos='conj');r.word('P4-S3',"they're",'they are缩写，与automated构成被动语态；它们实现自动化',lemma='they be',pos='aux')
r.word('P5-S1','as','与a result组成因此',pos='prep');r.word('P5-S1','farms','农场',lemma='farm',pos='n');r.word('P5-S1','on','依赖于（reliant on）',pos='prep')
r.word('P5-S2','for','对……的申请（requests for）',pos='prep');r.word('P5-S2','to','到（时间范围终点）',pos='prep');r.word('P5-S2','more','超过（more than doubled增至两倍多）',pos='adv')
r.word('P5-S3','has','有；具有（无数量上限）',lemma='have',pos='v');r.word('P5-S3','which','关系代词，指H-2B签证',pos='pron');r.word('P5-S3','is','与limited构成被动语态',lemma='be',pos='aux');r.word('P5-S3','limited','限制；限定',lemma='limit',pos='v');r.word('P5-S3','to','限为（数量）',pos='prep');r.word('P5-S3','a','每（一年）',pos='det')
r.word('P5-S4','even','与so组成即便如此',pos='adv');r.word('P5-S4',"aren't",'are not缩写，与given构成被动否定：未能得到全部',lemma='be not',pos='aux')
r.word('P5-S6','average','平均而言的；平均的（劳工）',pos='a');r.word('P5-S6','on','到岗（on the job）',pos='prep');r.word('P5-S6','days','天（22天）',lemma='day',pos='n')
r.word('P5-S7','is','与compounded构成被动语态',lemma='be',pos='aux');r.word('P5-S7','drive','迫使；逼得（进入隐蔽状态）',pos='v')
r.word('P6-S1','of','缺乏（short of）',pos='prep',occ=3)
r.word('P6-S2','by','通过（迁移经营活动）',pos='prep');r.word('P6-S2','moving','迁移；转移',lemma='move',pos='v');r.word('P6-S2','to','到（墨西哥）',pos='prep')
r.word('P6-S3','to','到（时间范围终点）',pos='prep');r.word('P6-S3','consumed','消费；食用',lemma='consume',pos='v');r.word('P6-S3','was','与imported构成被动语态',lemma='be',pos='aux')
r.word('P6-S4','little','仅仅；只（little more than略多于）',pos='adv')
r.word('P7-S1','it','美国',pos='pron',occ=1);r.word('P7-S1','it','所消费的食物',pos='pron',occ=2)
ph(r,'P1-S1','complaining of','complain of','抱怨');ph(r,'P3-S3','rather than','rather than','而不是');ph(r,'P3-S8','all along','all along','一直；始终');ph(r,'P4-S3','have a long way to go','have a long way to go','尚有很长的路要走；仍需努力');ph(r,'P5-S1','As a result','as a result','因此');ph(r,'P5-S4','Even so','even so','即便如此');ph(r,'P6-S1','short of','short of','缺少');ph(r,'P6-S4','Little more than','little more than','仅仅比……多一点；不过');ph(r,'P7-S1','In effect','in effect','实际上')
checks(r,'''完成进行时持续抱怨，for持续几年，farmers农场主，shortages劳动力短缺。
without与unlikely两个否定都保留，overhaul彻底改革，farm名词农业而非饲养。
更简便签证允许长留及行业内换岗，that指visa，would为改革本可允许。
this指改革受阻的局面，losers受损者不硬译失败比赛的人。
Perhaps保留比例估计，undocumented为无合法移民身份，不是没做文档。
as随着与are changing进行时，such指无合法身份劳工。
while让步，more likely两组相对概率并非所有人；settled定居和single未婚区分。
they're are与aging进行时，农业劳工群体老龄化。
世纪初约三分之一、年龄超过35岁，about是大约。
are后省略超过35岁，more than half保留过半。
picking采收，hard on对年长身体负担大，非身体硬。
all along始终，it's为it has，方案一直不现实，won't be returning否定美国本土劳工返农。
either否定句的也，yet还没，将机械化不是方案限定为目前。
五种大宗作物已机械化对照劳动密集高价值草莓仍需人工，both类别不混。
机器人只做少量挤奶，have lexical有，before与被动自动化标示仍有很长路。
therefore因果，grown变得，H-2A临时农业客籍劳工填缺口。
2012起申请上升与2011到2016签发增至两倍多分清，不把翻一倍写成翻两倍。
H-2A无上限对照H-2B非农业每年66000，a每，which指后者。
aren't given all为未得到全部所需，并非一个劳工都没有，even so让步。
process承签证办理流程，三项负面评价逐一保留。
平均劳工延迟22天到岗，不是22个工作日，也不是平均工人数。
compounded被加剧，raids突袭执法使一部分遣走另一部分躲藏，underground不是地下室。
2012样本两组71%与近80%分别果树及制干葡萄和浆果，short of缺少。
by方式为将经营移到墨西哥，moving非笼统前进，operations非手术。
1998到2000消费水果进口比14.5%，consumed消费而非火烧，被动进口。
仅十多年后进口占比25.8%，little more than略多于而非更少。
两个it分别美国与食物，进口食品或引入采收劳工两条选择准确对应。''')
r.notes=['全篇核定无证劳工人口变化、机械化限制与两类签证，申请/签发和翻倍量严格区分；修正farm饲养、picking增强、consumed烧毁等跨文错义。']
save(r)
