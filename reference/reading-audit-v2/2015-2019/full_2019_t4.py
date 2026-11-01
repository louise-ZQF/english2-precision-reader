# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2019-T4'),[f'{y}-T{n}' for y in [2015,2016,2017,2018] for n in range(1,5)]+['2019-T1','2019-T2','2019-T3'])
lex(r,'''arnold@Arnold/name=阿诺德（人名）;schwarzenegger@Schwarzenegger/name=施瓦辛格（姓氏）;dia@Dia/name=迪娅（人名）;mirza@Mirza/name=米尔扎（姓氏）;adrian@Adrian/name=阿德里安（人名）;grenier@Grenier/name=格雷尼尔（姓氏）;it's@it be/v=it is缩写：这是；这件事是;beat/v=战胜；解决（塑料污染问题）;plastic/n=塑料；塑料制品;they're@they be/v=they are缩写：他们是;part/n=其中一部分；成员;bunch/n=一群；一众;celebrities@celebrity/n=名人；明星;starring@star/v=主演；出演;new/a=新的;video/n=视频;swap/v=替换（swap out）；换掉;out/adv=与swap组成替换掉；换出;single-use/a=一次性使用的;staples@staple/n=常用必需品;like/prep=例如；像……这样的;straws@straw/n=吸管;cutlery/n=餐具；刀叉等用餐器具;plastics@plastic/n=塑料制品;crisis/n=危机;key/a=主要的；关键的;put/v=汇集；组织（put together）;include/v=包括;enact/v=制定（法律）；使成为法律;legislation/n=法律；立法;curb/v=限制；遏制;overarching/a=总的；居主导地位的;directed@direct/v=面向；针对（信息传达对象）;up/adv=交由决定（up to）；由……负责;individual/n=个人;limited/a=有限的;sense/n=认识；理解;achieved@achieve/v=实现；达成;own/a=自己的;taking@take/v=带；携带;bags@bag/n=袋子；购物袋;store/n=商店;quitting@quit/v=停止使用；放弃;accomplish/v=取得；实现;little/pron=很少的事；很少的付出;detrimental/a=有害的;satisfying@satisfy/v=满足;need/n=需要；心理需求;bit/n=自己的一份（do one's bit尽一份力）;progressing@progress/v=进展；迈进;onto/prep=迈向；进入（下一阶段行动）;bigger@big/a=更大的；规模更大的;bolder@bold/a=更大胆的;actions@action/n=行动;licensing/n=许可（moral licensing道德许可心理）;allays@allay/v=缓解；减轻;concerns@concern/n=担忧;stops@stop/v=阻止；使不再;asking@ask/v=要求；提出要求;charge/n=掌管；负责（in charge掌权的）；管理;conversation/n=讨论；谈论;around/prep=围绕；关于;toward/prep=对于；对;centered@center/v=集中；围绕（centered on）;shopping/n=购物;ignoring@ignore/v=忽略；无视;power/n=权力;implies@imply/v=暗示；意味着;shop/v=购物;sustainably/adv=以可持续的方式；不损害环境地;rather/adv=与than组成而不是;citizens@citizen/n=公民;hold/v=要求（hold...to account使问责）；使承担责任;real/a=真正的;systemic/a=系统性的；涉及整个制度体系的;change/n=改变；变革;isn't@be not/v=is not缩写：不是;priority/n=优先事项；首要考虑的事;expect/v=期望；指望;her/det=她的;good/a=善良的；好的;environmental/a=环境的；涉及环境的;wellesley@Wellesley/name=韦尔斯利（学院名）;elizabeth@Elizabeth/name=伊丽莎白（人名）;r@R/name=人名中间名首字母R;desombre@DeSombre/name=德松布尔（姓氏）;best@good/a=最好的;way/n=办法；方式;collectively/adv=整体地；通过集体方式;behavior/n=行为;large/a=大量的；大的;numbers@number/n=数量（large numbers of大量的）;structural/a=结构性的；制度层面的;mean/v=意味着;implementing@implement/v=实施；推行;policy/n=政策;adds@add/v=增加；加上;environmentally/adv=从环境角度；对环境而言;problematic/a=有问题的；有害的;banning@ban/v=禁止;altogether/adv=完全地；一概地;india@India/name=印度;eliminate/v=消除；淘汰;by/prep=到……为止;incentive-based/a=以激励为基础的;making@make/v=使；让;better@good/a=更好的；对环境更有益的;ensuring@ensure/v=确保;recycling/n=回收利用;trash/n=垃圾;disposal/n=处理；丢弃;saying@say/v=说；主张;caring@care/v=关心；在意;too/adv=太；过于;approach/n=方法；途径;none/pron=没有一个；全都不;writing@write/v=否定（write off）；不再重视;off/adv=与write组成否定；不予考虑;putting@put/v=放置（put...into perspective结合全局正确看待）;time/n=时间;progressive/a=推动进步的；促进改革的;shape/v=引导；塑造;collective/a=集体的;polluting@pollute/v=污染（修饰企业）；造成污染;alongside/prep=与……同时；与……一起;engaged/a=积极参与的;need/v=需要''')
r.word('P1-S1','have','有（要传达的信息）',pos='v');r.word('P1-S1','message','信息；要传达的话',pos='n');r.word('P1-S1','for','给（受众）',pos='prep')
r.word('P1-S2','day','节日（World Environment Day世界环境日）',pos='n');r.word('P1-S2','plastic','塑料（名词作定语，塑料制的）',pos='n')
r.word('P2-S1','messages','宣传信息；宣传主张',lemma='message',pos='n');r.word('P2-S1','that','关系代词，指主要信息',pos='pron');r.word('P2-S1','been','与put构成完成被动',lemma='be',pos='aux');r.word('P2-S1','do','确实（强调后面的include）',pos='aux');r.word('P2-S1','call','呼吁；要求',pos='n');r.word('P2-S1','day','节日（World Environment Day世界环境日）',pos='n')
r.word('P2-S2','message','宣传主张；信息',pos='n');r.word('P2-S2','is','与directed构成被动语态',lemma='be',pos='aux');r.word('P2-S2','at','面向；针对（directed at）',pos='prep')
r.word('P3-S1','concern','担忧',pos='n');r.word('P3-S1','with','对……的担忧（concern with）',pos='prep');r.word('P3-S1','leaving','把……交由（leave it up to）',lemma='leave',pos='v');r.word('P3-S1','to','交由谁决定或负责（up to）',pos='prep',occ=1);r.word('P3-S1','be','与achieved构成被动语态',pos='aux')
r.word('P3-S2','own','单独；靠自己（on their own）',pos='pron',occ=1);r.word('P3-S2','to','带到（商店）',pos='prep');r.word('P3-S2','for','与example组成例如',pos='prep');r.word('P3-S2','of','要求某人付出（require...of us）',pos='prep')
r.word('P3-S3','more','更多的事情（do more）',pos='pron',occ=2);r.word('P3-S3','more','更高的要求（ask more）',pos='pron',occ=3);r.word('P3-S3','that','关系代词，指道德许可心理',pos='pron');r.word('P3-S3','of','向……提出要求（ask...of）',pos='prep')
r.word('P4-S1',"we're",'we are缩写，与ignoring构成进行时：我们在忽略',lemma='we be',pos='aux');r.word('P4-S1','that','关系代词，指权力格局',pos='pron',occ=1);r.word('P4-S1','to','问责（hold...to account）中的介词',pos='prep',occ=1);r.word('P4-S1','account','责任说明；交代（hold to account问责）',pos='n');r.word('P4-S1','for','要求；争取（push for）',pos='prep')
r.word('P5-S1',"everyone's",'每个人的（everyone所有格），不是everyone is缩写',lemma='everyone',pos='pron');r.word('P5-S1','most','大多数的（人）',pos='det');r.word('P5-S1','or','甚至（递进到大多数人）',pos='conj')
r.word('P5-S2','it','环境（是否成为首要事项）',pos='pron')
r.word('P5-S3','do','做；做出（行为，书名）',pos='v');r.word('P5-S3','change','改变（人群行为）',pos='v',occ=1);r.word('P5-S3','change','改变；变革',pos='n',occ=2);r.word('P5-S3','for','引出不定式主语the change，通常不单译',pos='prep')
r.word('P6-S1','as','例如（such as）',pos='prep');r.word('P6-S1','that','关系代词，指塑料税',pos='pron');r.word('P6-S1','to','给……增加（成本，add...to）',pos='prep')
r.word('P6-S2','just','刚刚',pos='adv')
r.word('P6-S3','are','有；存在（there are）',lemma='be',pos='v');r.word('P6-S3','ways','办法；方式',lemma='way',pos='n');r.word('P6-S3','as','例如（such as）',pos='prep',occ=1);r.word('P6-S3','as','同样地；一样地（修饰easy）',pos='adv',occ=2);r.word('P6-S3','as','和……一样（引出比较）',pos='conj',occ=3)
r.word('P7-S1',"isn't",'is not缩写，与saying构成进行时否定：并不是在说',lemma='be not',pos='aux')
r.word('P7-S2','individual','个人的',pos='a');r.word('P7-S2','that','那种做法（依靠个人行动）',pos='pron',occ=2);r.word('P7-S2','for','引出不定式主语that（too...for...to结构）',pos='prep');r.word('P7-S2','only','唯一的',pos='a');r.word('P7-S2','primary','主要的；首要的',pos='a');r.word('P7-S2','to','改变……的途径（approach to）',pos='prep',occ=2)
r.word('P8-S2','into','与put...perspective组成放到整体中正确看待',pos='prep');r.word('P8-S3','have','有（可等待的时间）',pos='v');r.word('P8-S3','wait','等待',pos='v')
r.word('P8-S4','that','关系代词，指政策',pos='pron');r.word('P8-S4','in','约束（rein in）的搭配副词',pos='adv');r.word('P8-S4','for','争取；推动（push for）',pos='prep')
r.sentence('P3-S1')['chunks'][3]['zh']='究竟需要实现什么目标'
r.sentence('P3-S3')['chunks'][1]['zh']='它们满足了我们觉得自己已经尽了一份力的心理需要'
r.sentence('P8-S2')['translation']='只是要从整体上恰当地看待个人行动的作用。'
r.sentence('P8-S2')['chunks'][0]['zh']='只是要从整体上恰当地看待个人行动的作用'
r.sentence('P8-S2')['reorder']='put...into perspective 指结合全局判断作用，things 按本段话题译明个人行动。'
ph(r,'P1-S2','swap out','swap out','替换掉；换掉');ph(r,'P2-S1','put together','put together','汇集；组织起来');ph(r,'P3-S1','leaving it up to','leave it up to','把这件事交给……负责或决定');ph(r,'P3-S2','On their own','on one’s own','仅靠自身；单独');ph(r,'P3-S3','done our bit','do one’s bit','尽自己的一份力');ph(r,'P3-S3','moral licensing','moral licensing','道德许可（做了一件好事后便觉得可以少做或放松要求的心理）');ph(r,'P4-S1','hold our governments and industries to account','hold...to account','要求政府与产业承担责任；向其问责');ph(r,'P8-S1','writing off','write off','否定；认为没有价值');ph(r,'P8-S2','putting things into perspective','put...into perspective','从整体上恰当地看待事物的作用');ph(r,'P8-S4','rein in','rein in','约束；限制')
checks(r,'''三位人物传达宣传信息，have为有，it形式主语，beat plastic在文中为解决塑料污染。
staples常用必需品非订书钉，like举例，swap out换掉，single-use完整复合词。
that关系从句前置，完成被动put together汇集，do强调确实包括政府立法诉求。
overarching主导信息，directed at面向个人受众非指路。
leave it up to交由个人，what为需要实现目标，块译末去除重复的认识有限。
on their own仅靠这些个人举措，自带袋子与不用吸管两个例子，little两次分别成果与付出。
done our bit仅尽一份力而非尽全力，道德许可缓担忧抑制行动及对掌权者要求，两者都保留。
while环境讨论局限，that关系词与宾语引导词区分，hold to account问责非占比，消费者与公民行动对照。
everyone's为每个人的所有格不是everyone is，not everyone至not even most递进否定。
it指环境，be后省略成为所有人或大多数人优先事项，不扩成无人关心。
书名do实义做，首change动词次change名词，集体改变行为须结构性变革。
税增加有害环境行为成本或完全禁用两政策，that修饰税，to是add to介词。
just刚刚，宣布到2022的承诺按报道时间保留，不声称现实已兑现。
激励让更环保选择更容易，至少与垃圾丢弃一样便利，三个as角色分清。
isn't saying否定这种解读，不是倡导停止环保，care about为关心。
too slow for...to个人行动太慢不宜唯一或主要途径，primary非小学，that指个人行动。
write off全盘否定个人，None否定该解读，并非取消政策责任。
put into perspective结合整体恰当判断，不是将物品摆到物理位置；整译改得自然。
have实义有，don't have time无时间可等，紧迫性保留。
政策引导集体行动兼约束污染企业，同时需要参与公民，alongside并非二者替代。''')
r.notes=['复核消费者/公民、个人/制度变革之间的论证范围；逐位置改正primary小学、everyone’s缩写、account占比等错误候选，保留报道时点的政策承诺。']
save(r)
