# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2017-T2'),[f'{y}-T{n}' for y in [2015,2016] for n in range(1,5)]+['2017-T1'])

lex(r,'''children's@child/n=孩子的（所有格）;screens@screen/n=屏幕设备;screen/n=屏幕；屏幕设备;it's@it be/pron=这是（it is缩写）;easy/a=容易的;own/a=自己的;tech/n=技术产品;designed@design/v=设计;suck/v=吸引住；使沉迷（suck in）;jenny@Jenny/name=珍妮（人名）;radesky@Radesky/name=拉德斯基（姓氏）;her/pron=她的;digital/a=数字化的;play/n=游戏；玩耍;products@product/n=产品;promote/v=促进；促使;maximal/a=最大限度的;engagement/n=投入程度；参与;disengage/v=抽身；停止投入;leads@lead/v=导致;bleed-over/n=蔓延渗透；干扰其他生活领域;routine/n=日常生活；惯常安排;studied@study/v=研究;mobile/a=移动的;phones@phone/n=手机;tablets@tablet/n=平板电脑;mealtimes@mealtime/n=用餐时间;by/prep=通过；由;mother-child/a=母亲与孩子的;pairs@pair/n=一对对组合;food-testing/a=食物测试的;exercise/n=活动；练习;mothers@mother/n=母亲;used@use/v=使用;during/prep=在……期间;per/prep=每（per cent合指百分之）;cent/n=百分之一（per cent合指百分之）;fewer@few/a=更少的;verbal/a=言语的;nonverbal/a=非言语的;interactions@interaction/n=互动;separate/a=另外的；独立的;observation/n=观察;saw@see/v=发现；观察到;became@become/v=成为;source/n=来源；根源;tension/n=紧张关系;looking@look/v=查看（look at）；看;emails@email/n=电子邮件;excited/a=急切的；激动的;bids@bid/n=努力尝试（bid for attention为争取注意）;infants@infant/n=婴儿;wired/a=天生具有某种倾向的（比喻）；生来如此的;look/v=看;faces@face/n=脸；面孔;blank/a=毫无表情的;unresponsive/a=没有回应的;absorbed/a=专注投入的；沉迷的;device/n=电子设备;extremely/adv=极其;disconcerting/a=令人不安的;cites@cite/v=援引；提到;face/n=面孔;experiment/n=实验;devised@devise/v=设计;developmental/a=发展心理学的；发展的;psychologist/n=心理学家;ed@Ed/name=埃德（人名）;tronick@Tronick/name=特罗尼克（姓氏）;mother/n=母亲;asked@ask/v=要求;interact/v=互动;child/n=孩子;putting@put/v=摆出（表情，put on）；放上;expression/n=表情;visual/a=视觉上的;feedback/n=反馈；回应;distressed/a=难过不安的;tries@try/v=尝试；努力;capture/v=吸引；抓住（注意力）;mother's@mother/n=母亲的（所有格）;exquisitely/adv=极其；高度专注地;present/a=在场并投入关注的;needs@need/v=需要;need/n=需要；需求;responsive/a=及时回应的;sensitive/a=敏锐体察的;child's@child/n=孩子的（所有格）;expressions@expression/n=表达;hand/n=方面（on the other hand）;himself/pron=他本人;concerned/a=担心的;worries@worry/n=忧虑;born@bear/v=产生；起源（born out of整体）；出生;oppressive/a=苛刻压人的;ideology/n=观念体系;demands@demand/v=要求;always/adv=始终；总是;interacting@interact/v=互动;fantasised@fantasise/a=想象出来的；不切实际的;white/a=带有白人社会文化色彩的；白人的;upper-middle-class/a=中上阶层的;you're@you be/pron=你正……；你是（you are缩写）;expose/v=使接触（expose...to）；呈现;words@word/n=词语;neglecting@neglect/v=忽视；疏于照顾;believes@believe/v=认为;isn't@be/aux=不（is not缩写）；与learning构成否定进行时;mean/v=意味着;value/n=价值；益处;particularly/adv=尤其;shower/n=淋浴;housework/n=家务;break/n=休息;friend/n=朋友;get/v=得到；处理;work/n=工作;lets@let/v=让；使;available/a=有时间和精力可陪伴的;time/n=时间;times@time/n=时刻;making@make/v=作出；发起;makes@make/v=使；让;out/adv=从……获得；排除掉（依搭配）''')
r.word('P1-S1','with','由于（引出过度关注的背景）',pos='prep');r.word('P1-S1','for','对父母而言',pos='prep');r.word('P1-S1','about','对自身用屏幕的情况（forget about）',pos='prep')
r.word('P1-S2','is','与designed构成被动语态',lemma='be',pos='aux');r.word('P1-S2','in','被吸引进去（suck in）',pos='adv',occ=1);r.word('P1-S2','really','牢牢地；强烈地（加强吸引程度）',pos='adv');r.word('P1-S2','there','be there to结构，表示为实现某目的而存在',pos='adv')
r.word('P1-S3','it','形式宾语，指停止投入这件事',pos='pron',occ=2);r.word('P1-S3','it','数字产品最大化吸引投入的设计',pos='pron',occ=1);r.word('P1-S3','to','导致（lead to）',pos='prep',occ=2)
r.word('P2-S2','started','主动发起（互动）',lemma='start',pos='v');r.word('P2-S2','with','与孩子进行互动',pos='prep')
r.word('P2-S4','would','描写过去观察到的常见行为，会',pos='aux');r.word('P2-S4','be','与looking或making构成进行时',pos='aux');r.word('P2-S4','at','看……的对象（look at）',pos='prep');r.word('P2-S4','while','而；与此同时',pos='conj');r.word('P2-S4','for','争取（父母）的注意',pos='prep')
r.word('P3-S1','are','系动词，说明wired的天生倾向',lemma='be',pos='v',occ=1);r.word('P3-S1','at','看（look at）的对象',pos='prep');r.word('P3-S1','as','正如（插入说明父母用设备时的表情）',pos='conj');r.word('P3-S1','in','沉迷于；专注于（absorbed in）',pos='prep');r.word('P3-S1','for','对孩子而言',pos='prep');r.word('P3-S1','they','父母的脸／面部表情',pos='pron')
r.word('P3-S2','still','静止的；没有表情变化的',pos='a');r.word('P3-S2','by','由（心理学家设计）',pos='prep')
r.word('P3-S3','is','与asked构成被动语态',lemma='be',pos='aux');r.word('P3-S3','way','方式',pos='n');r.word('P3-S3','on','摆出（put on表情）',pos='adv');r.word('P3-S3','them','孩子（泛指，不限定性别）',pos='pron');r.word('P3-S3','as','当……时；同时',pos='conj');r.word('P3-S3','she','这个孩子（女孩）',pos='pron');r.word('P3-S3','her','她自己的（指孩子的母亲）',pos='pron',occ=2)
r.word('P3-S4','have','必须（don’t have to整体为不必）',pos='aux');r.word('P3-S4','need','需要（后接动作）',pos='v',occ=1);r.word('P3-S4','to','对孩子的情感表达（responsive/sensitive to）',pos='prep',occ=4);r.word('P3-S4','there','存在结构，指需要有平衡',pos='pron')
r.word('P4-S1','on','与the other hand构成另一方面',pos='prep',occ=1);r.word('P4-S1','on','依据（based on）',pos='prep',occ=2);r.word('P4-S1','are','与born out of构成起源于的被动形式',lemma='be',pos='aux',occ=1);r.word('P4-S1','are','与neglecting构成进行时',lemma='be',pos='aux',occ=2);r.word('P4-S1','that','关系代词，指oppressive ideology',pos='pron',occ=2);r.word('P4-S1','that','关系代词，指后面的意识形态',pos='pron',occ=4);r.word('P4-S1','be','与interacting构成进行时',pos='aux');r.word('P4-S1',"it's",'it is缩写，it指该观念，is与based构成被动形式',lemma='it be',pos='aux');r.word('P4-S1',"you're",'you are缩写，与failing构成进行时',lemma='you be',pos='aux');r.word('P4-S1','to','使孩子接触（expose...to）',pos='prep',occ=2)
r.word('P4-S2','to','对屏幕使用而言（value to it）',pos='prep',occ=1);r.word('P4-S2','have','洗（have a shower）',pos='v',occ=1);r.word('P4-S2','have','休息（have a break）',pos='v',occ=2);r.word('P4-S2','do','做；处理（家务）',pos='v');r.word('P4-S2','it','孩子使用屏幕这件事',pos='pron')
r.word('P4-S3','get','获得益处（get a lot out of）',pos='v',occ=1);r.word('P4-S3','get','处理掉；完成（get...out of the way）',pos='v',occ=2);r.word('P4-S3','speak','交谈；说话',pos='v');r.word('P4-S3','to','和朋友交谈',pos='prep',occ=2);r.word('P4-S3','way','待处理的事务之列（out of the way比喻处理掉）',pos='n')
r.word('P4-S4','to','对孩子而言；可陪伴的对象',pos='prep');r.word('P4-S4','which','关系代词，指父母更开心这一结果',pos='pron');r.word('P4-S4','them','父母',pos='pron')
ph(r,'P3-S2','still face experiment','still face experiment','静止面孔实验；照护者保持面无表情以观察婴儿反应的实验')
checks(r,'''with引出过度关注儿童屏幕使用的背景，own指父母自己的使用。
is designed为被动，suck in是牢牢吸引，be there to说明设计目的。
第一个it指吸引投入的设计，第二个it形式宾语，lead to是导致。
通过母子食物测试活动研究用餐设备使用，tablets非药片。
20%和39%是母亲主动发起的两类互动减少比例，不能互换。
另一次观察发现家庭紧张来源，不把saw直译为只看见。
would描述常见的过去观察，while是同时的对照，bids非投标。
wired为天生倾向，they指脸部表情，as插入，for对孩子而言。
still是形容词静止，不是仍然，实验由发展心理学家设计。
she指孩子而非母亲；before是先互动后无表情，put on摆表情。
don't have to为不必，最后need名词情感需求，sensitive to为敏锐察觉。
white为白人文化背景而非白人至上，that两处关系词及内容词分开。
not learning不推出无价值，have a shower/break为实义动作。
get a lot out of为获益，speak为动词交谈，get work out of way为完成。
available指可投入陪伴的时间精力，which承接父母快乐状态。''')
r.notes=['重审全部词位置，明确still/face、wired、tablets、bids、white与available的本文义，避免仅沿用科技或心理学通用词典。']
save(r)
