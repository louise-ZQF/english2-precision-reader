# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2019-T1'),[f'{y}-T{n}' for y in [2015,2016,2017,2018] for n in range(1,5)])
lex(r,'''unlike/prep=不同于;so-called/a=所谓的;emotions@emotion/n=情绪；情感;sadness/n=悲伤;anger/n=愤怒;guilt/n=内疚；负罪感;emerges@emerge/v=出现；产生;growing@grow/a=逐渐增强的；发展的;grasp/n=理解；领会;social/a=社会的；与社会交往有关的;moral/a=道德的;norms@norm/n=规范；准则;sorry/a=抱歉的；对不起;rather/adv=而是；更确切地说;learn/v=学会；学习;over/prep=在……过程中（over time随时间推移）;time/n=时间;statements@statement/n=表达；说出的话;appease/v=安抚；使平息;own/a=自己的;consciences@conscience/n=良心；道德自觉;regard/v=认为；看待;right/a=适当的；恰当的;amount/n=程度；量;imagination/n=想象；观念;course/n=与of组成当然;gets@get/v=受到（某种评价）；得到;rap/n=评价；名声（bad rap负面评价）;deeply/adv=深深地；极其;uncomfortable/a=令人难受的;it's@it be/v=it is的缩写：它是；这在……方面是;equivalent/n=相当的事物；对应物;wearing@wear/v=穿着;jacket/n=外套;weighted@weight/v=加重；装上重物;stones@stone/n=石头;yet/conj=然而;outdated/a=过时的;revival/n=重新受到关注；重新兴起;rethinking/n=重新思考;serve/v=发挥（作用）;amrisha@Amrisha/name=阿姆里莎（人名）;vaish@Vaish/name=瓦伊什（姓氏）;psychology/n=心理学;researcher/n=研究人员;virginia@Virginia/name=弗吉尼亚（大学名称中的地名）;adding@add/v=补充说;part/n=部分;larger@large/a=更广泛的;recognition/n=认识；认知;binary/a=二元的；非此即彼的;feelings@feeling/n=情绪；感受;advantageous/a=有益的；有利的;one/num=一；某一个;context/n=情境；背景;harmful/a=有害的;jealousy/n=嫉妒;evolved@evolve/v=在进化中形成;alert/v=提醒；使注意到;inequalities@inequality/n=不平等（现象）;too/adv=过于；过量地;happiness/n=快乐；幸福;destructive/a=有破坏性的;by/prep=通过……方式;think/v=思考；反思;goodness/n=善良品行；道德品质;encourage/v=促使；鼓励;humans@human/n=人类；人们;make/v=与up for组成弥补;up/adv=make up for中的副词：弥补;errors@error/n=错误;fix/v=修复；改善;relationships@relationship/n=人际关系;cooperative/a=善于合作的；依靠合作的;glue/n=黏合剂（比喻维系社会的力量）;light/n=角度；看法（in this light从这角度看）;work/n=研究；研究工作;tina@Tina/name=蒂娜（人名）;malti@Malti/name=马尔蒂（姓氏）;toronto@Toronto/name=多伦多（大学名称中的地名）;suggests@suggest/v=提示；表明;deficiency/n=缺乏；不足;shown@show/v=表明；证明;sympathy/n=同情心;represent/v=是；体现为；代表;pathways@pathway/n=途径;cooperation/n=合作;sharing/n=分享;low/a=低的；薄弱的;shortfall/n=不足；欠缺;experiencing@experience/v=产生；体验;rein/v=抑制；约束（rein in）;nastier@nasty/a=更恶劣的；更有伤害性的;impulses@impulse/n=冲动;versa/adv=与vice组成反过来也一样;high/a=较强的；较高的;substitute/v=代替；起补偿作用;study/n=研究;looked@look/v=研究；考察（look at）;caregiver/n=照料者;assessments@assessment/n=评估；评价;self-observations@self-observation/n=自我观察;rated@rate/v=评定；评价;each/det=每一个;her/det=她的;tendency/n=倾向;negative/a=负面的；消极的;transgressions@transgression/n=违规；违反道德准则的行为;handed@hand/v=递给；发给;chocolate/n=巧克力;coins@coin/n=硬币（此处为硬币形巧克力）;chance/n=机会;share/v=分享;anonymous/a=匿名的；身份不透露的;low-sympathy/a=同情心较弱的;shared@share/v=分享;appeared@appear/v=似乎；看起来;turn/v=取决于（turn on），而非打开;guilty/a=内疚的;guilt-prone/a=容易感到内疚的;ones@one/pron=那些孩子（代替kids）;though/conj=与even组成尽管；即使;hadn't@have not/aux=had not缩写，否定过去完成时：并没有;magically/adv=神奇地；像变魔术一样;sympathetic/a=同情的；有同情心的;deprivation/n=匮乏；未得到巧克力的处境;that's@that be/v=that is缩写：那是；这是;prosocial/a=亲社会的；有利于他人和群体的;caused@cause/v=造成；导致;regret/n=懊悔；后悔''')
r.word('P1-S1','as','例如（such as）',pos='prep');r.word('P1-S1','later','更晚一些',lemma='late',pos='adv');r.word('P1-S1','in','与conjunction with组成伴随；随着',pos='prep');r.word('P1-S1','with','与……伴随（in conjunction with）',pos='prep')
r.word('P1-S2','born','天生具有；出生（be born knowing天生就知道）',lemma='bear',pos='v');r.word('P1-S2','knowing','知道',lemma='know',pos='v');r.word('P1-S2','and','也；还（添加孩子自己的良心）',pos='conj',occ=2)
r.word('P1-S3','why','……的原因（承接This is）',pos='adv')
r.word('P2-S1','popular','大众的；公众的',pos='a');r.word('P2-S1','of','与course组成当然',pos='prep')
r.word('P2-S2','emotional','情绪感受上的',pos='a');r.word('P2-S2','it','内疚',pos='pron');r.word('P2-S2','with','加上（石头作为重物）',pos='prep')
r.word('P2-S3','this','这种（把内疚视作坏事的认识）',pos='det')
r.word('P2-S4','been','存在；发生（there has been）',lemma='be',pos='v');r.word('P2-S4','what','什么（内疚是什么）',pos='pron',occ=1);r.word('P2-S4','what','什么样的（作用）',pos='det',occ=2);r.word('P2-S4','this','这种（重新关注）',pos='det');r.word('P2-S4','that','关系代词，指情绪feelings',pos='pron',occ=3);r.word('P2-S4','another','另一种情境（省略context）',pos='pron')
r.word('P2-S5','for','与example组成例如',pos='prep');r.word('P2-S5','to','提醒某人注意……（alert...to）',pos='prep',occ=2)
r.word('P2-S6','much','大量的；很多的（too much整体为过多的）',pos='det')
r.word('P3-S1','and','而；接着说明内疚的积极作用',pos='conj',occ=1);r.word('P3-S1','for','弥补（make up for）的搭配介词',pos='prep')
r.word('P3-S2','hold','使保持（团结）；维系',pos='v');r.word('P3-S2','in','与other words组成换句话说',pos='prep')
r.word('P4-S1','viewed','看待；从某个角度理解',lemma='view',pos='v');r.word('P4-S1','this','这个（角度）',pos='det')
r.word('P4-S2','by','由……开展（研究）',pos='prep');r.word('P4-S2','emotional','情感上的',pos='a');r.word('P4-S2','for','弥补（compensate for）的搭配介词',pos='prep')
r.word('P4-S3','to','通向合作与分享的（途径）',pos='prep')
r.word('P4-S4','that','这种（同情心不足）',pos='det');r.word('P4-S4','more','更多的（内疚感）',pos='det');r.word('P4-S4','for','与make up组成弥补',pos='prep');r.word('P4-S4','in','约束（rein in）的搭配副词',pos='adv',occ=2);r.word('P4-S4','which','更多内疚感（关系代词）',pos='pron')
r.word('P4-S5','vice','与versa组成反过来也一样，不是恶习',pos='adv');r.word('P4-S5','for','代替（substitute for）的搭配介词',pos='prep')
r.word('P5-S1','for','与example组成例如',pos='prep');r.word('P5-S1','at','研究；考察（look at）的搭配介词',pos='prep')
r.word('P5-S2','using','根据；利用（评估资料）',lemma='use',pos='v');r.word('P5-S2','overall','总体的；综合的（同情心水平）',pos='a')
r.word('P5-S3','were','与handed/given构成被动语态',lemma='be',pos='aux');r.word('P5-S3','given','给予（机会）',lemma='give',pos='v');r.word('P5-S3','them','硬币形巧克力',pos='pron');r.word('P5-S3','with','与……分享',pos='prep')
r.word('P5-S4','for','对……而言',pos='prep');r.word('P5-S4','on','取决于（turn on）的搭配介词',pos='prep');r.word('P5-S4','how','多少；多大程度（how much）',pos='adv',occ=1);r.word('P5-S4','how','多么；多大程度（修饰inclined）',pos='adv',occ=2);r.word('P5-S4','much','多少（分享的量）',pos='pron')
r.word('P5-S5','more','更多东西（巧克力，省略宾语名词）',pos='pron',occ=1);r.word('P5-S5','to','同情……（sympathetic to）',pos='prep');r.word('P5-S5','even','与though组成即使；尽管',pos='adv')
ph(r,'P1-S1','in conjunction with','in conjunction with','伴随着；与……同时出现');ph(r,'P2-S1','gets a bad rap','get a bad rap','名声不佳；受到负面评价');ph(r,'P3-S1','make up for','make up for','弥补');ph(r,'P4-S4','rein in','rein in','抑制；约束');ph(r,'P4-S5','vice versa','vice versa','反过来也一样');ph(r,'P5-S4','turn on','turn on','取决于；以……为转移')
checks(r,'''与基本情绪相比内疚稍晚出现，伴随的是规范理解增长，grasp为理解不是抓握。
aren't born knowing否定天生就懂而非否定出生，rather转向后天习得，their own指孩子良心。
right为适量恰当而非权利或方向，限定内疚适量才有益。
popular为大众观念，bad rap是负面名声不是说唱或敲击，保留of course插语。
情绪层面类比穿缀石头的外套，weighted为增加重物，emotional不是情感丰富。
this回指把内疚视作坏事的认识，yet转折保留。
区分两次what间接疑问与that同位和关系从句，binary非简单好坏二分，情境改变利害。
may have evolved保留推测，alert to为提醒注意不平等，非警报本体。
too much为过量快乐，破坏性来自过度而非一概否定快乐。
by给出机制，goodness道德品行，make up for弥补，fix修复关系。
hold...together维系团结而非hold true成立，cooperative修饰物种。
社会黏合剂是比喻内疚的凝聚作用，it回指内疚。
in this light从这一视角理解，opportunity为机会。
work是马尔蒂的研究，by表研究者，suggests提示非建议，may保留可能。
多个研究支持两条合作路径，to介词连接途径与合作，guilt与sympathy不混。
that shortfall回指同情心不足，which指更多内疚，rein in约束恶劣冲动。
vice versa反向关系非恶习，substitute for为同情心补偿低内疚。
2014年244儿童样本不遗漏，looked at是研究而非只观看。
两个评定项目为同情心水平及道德违规后负面情绪倾向，after范围只在后者。
被动发巧克力与给分享机会并列，coins是硬币形巧克力，them指巧克力。
turn on意为取决于，两处how分别对应分享数量与内疚倾向程度。
more第一次指更多巧克力，第二次修饰同情心，deprivation为对方未获巧克力。
that's指补偿机制这一发现，保留说话人马尔蒂。
prosocial译明亲社会行为，因为伤害他人而懊悔可促成此类行为，非定义为内疚本身。''')
r.notes=['独立复核内疚与同情心的互补机制、244儿童研究、让步与指代；重点清除born/hold/vice/given/turn的跨文错误候选义。']
save(r)
