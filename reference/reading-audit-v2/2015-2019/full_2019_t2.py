# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2019-T2'),[f'{y}-T{n}' for y in [2015,2016,2017,2018] for n in range(1,5)]+['2019-T1'])
lex(r,'''forests@forest/n=森林;give/v=给予；带来;shade/n=荫凉；树荫;quiet/n=宁静;one/pron=其中一个（挑战）;challenges@challenge/n=挑战；难题;fight/n=斗争；应对的努力;change/n=变化;count/v=指望；依靠（count on）;soak/v=吸收（soak up）;up/adv=与soak组成吸收；吸入;carbon/n=碳;dioxide/n=二氧化物（carbon dioxide二氧化碳）;threatening@threaten/v=损害；威胁;hastening@hasten/v=加速；促使加快;emit/v=排放；释放;thankfully/adv=幸好；值得庆幸的是;way/n=办法；出路;out/adv=摆脱；与way out组成出路;striking@strike/v=取得；达成（strike a balance）;helping@help/v=帮助;flourish/v=茁壮生长；繁茂;valuable/a=宝贵的；有价值的;sinks@sink/n=碳汇；吸收并储存碳的系统;long/adv=长久地；很长时间;future/n=未来;reducing@reduce/v=降低；减少;capacity/n=能力；承载能力;california@California/name=加利福尼亚州;figuring@figure/v=弄清楚（figure out）;details@detail/n=细节；具体做法;proposed@propose/a=拟议中的；提出的;plan/n=计划;aims@aim/v=旨在；以……为目标;thin/v=疏伐；间伐（thin out）；使稀疏;young/a=幼小的；年幼的;trees@tree/n=树木;brush/n=灌木丛;lowers@lower/v=降低;carbon-carrying/a=碳承载的；能够储存碳的;remaining@remain/a=剩余的；留下的;moisture/n=水分；湿气;grow/v=生长;forest's@forest/n=森林的（所有格）;pull/v=吸取；吸收;air/n=空气;healthy/a=健康的;better@well/adv=更好地；更能;fend/v=抵御（fend off）；抵挡;off/adv=避开；挡开（fend off）；不让接近;rendered@render/v=使变得；使处于; easily/adv=容易地;burnable/a=可燃的；容易燃烧的;fire/n=火灾;consumed@consume/v=被火烧毁；吞噬;need/n=需要；需求;urgent/a=迫切的;drought/n=干旱;killed@kill/v=使死亡；杀死;over/prep=超过;alone/adv=仅仅；单单（仅那一年）;burned@burn/v=烧毁；燃烧;hundreds@hundred/num=数百（hundreds of thousands数十万）;by/prep=到……为止;financed@finance/v=提供资金；资助;proceeds/n=所得款项；收入;emissions-permit/n=排放许可；排污许可;auctions@auction/n=拍卖;that's@that be/v=that is缩写：那是；这是;small/a=小的；少量的;total/a=全部的；总计的;acreage/n=以英亩计算的土地面积;benefit/v=受益；得益;vital/a=至关重要的;areas@area/n=地区；区域;greatest@great/a=最大的；最高的;strategy/n=策略;ensure/v=确保;woody/a=木质的;material/n=材料；物质;removed@remove/v=移除；清除;locked@lock/v=封存；锁住（lock away）；储存;away/adv=封存起来（lock away）；存放一旁;form/n=形式;solid/a=实心的；实体的;lumber/n=木材；锯材;biofuel/n=生物燃料;otherwise/adv=否则；如果不用生物燃料的话;new/a=新的;transportation/n=运输；交通;biofuels@biofuel/n=生物燃料;state/n=州；州一级;well/adv=非常；很;accustomed/a=习惯的；熟悉的;traditionally/adv=传统上；历来;they've@they have/aux=they have缩写，与focused构成完成时；它们已经;watersheds@watershed/n=流域；集水区;opportunities@opportunity/n=机会;recreation/n=娱乐；休闲活动;recently/adv=最近;part/n=作用；角色;play/v=发挥；起（作用）;storing@store/v=储存;california's@California/name=加利福尼亚州的（所有格）;expected@expect/v=预计；预期;finalized@finalize/v=最终确定；定稿;governor/n=州长;model/n=范例；可借鉴的模式''')
r.word('P1-S1','against','对抗；应对（气候变化）',pos='prep');r.word('P1-S1','and','也带来（从益处转至挑战）',pos='conj')
r.word('P1-S2','even','与as组成即使在……之时；正当',pos='adv');r.word('P1-S2','as','当……时（even as）',pos='conj');r.word('P1-S2','on','指望（count on）的搭配介词',pos='prep');r.word('P1-S2','good','相当大的；可观的（a good share）',pos='a');r.word('P1-S2','share','份额；部分',pos='n');r.word('P1-S2','produce','产生；排放（二氧化碳）',pos='v');r.word('P1-S2','are','与threatening构成进行时',lemma='be',pos='aux');r.word('P1-S2','do','完成；做到（do so替代吸收二氧化碳）',pos='v');r.word('P1-S2','so','那样（指吸收二氧化碳）',pos='adv')
r.word('P1-S3','are','与hastening构成进行时',lemma='be',pos='aux');r.word('P1-S3','one','某一个（one day有朝一日）',pos='det');r.word('P1-S3','leave','使……处于（某种境况）',pos='v');r.word('P1-S3','with','使我们面对……（leave us with）',pos='prep');r.word('P1-S3','that','关系代词，指森林',pos='pron');r.word('P1-S3','more','更多的（排放的碳）',pos='det');r.word('P1-S3','absorb','吸收（碳）',pos='v')
r.word('P2-S1','is','有；存在（there is）',lemma='be',pos='v');r.word('P2-S1','this','这个（排碳森林困境）',pos='det');r.word('P2-S1','trap','困境；陷阱',pos='n');r.word('P2-S1','subtle','微妙的；需要精细把握的',pos='a')
r.word('P2-S2','into','延续到（未来）',pos='prep');r.word('P2-S2','absorb','吸收（碳）',pos='v')
r.word('P2-S3','is','与leading构成进行时',lemma='be',pos='aux');r.word('P2-S3','leading','引领；率先行动（lead the way）',lemma='lead',pos='v');r.word('P2-S3','as','正如……一样',pos='conj');r.word('P2-S3','does','这样做（替代引领气候行动）',lemma='do',pos='v');r.word('P2-S3','out','与figure组成弄清楚',pos='adv')
r.word('P3-S1','double','加倍；使增加一倍',pos='v');r.word('P3-S1','out','与thin组成疏伐',pos='adv');r.word('P3-S1','clear','清除；清理',pos='v')
r.word('P3-S3','share','份额；所占部分',pos='n');r.word('P3-S3','draw','吸取（水分）',pos='v');r.word('P3-S3','available','可获得的；可利用的（水分）',pos='a');r.word('P3-S3','so','因此；所以',pos='conj');r.word('P3-S3','thrive','茁壮成长',pos='v')
r.word('P3-S5','landscape','林地环境；整片林地',pos='n');r.word('P3-S5','is','与rendered构成被动语态',lemma='be',pos='aux');r.word('P3-S5','less','更不……（修饰easily的程度）',pos='adv')
r.word('P3-S6','even','即使；哪怕',pos='adv');r.word('P3-S6','event','情况（in the event of若发生）',pos='n');r.word('P3-S6','are','与consumed构成被动语态',lemma='be',pos='aux')
r.word('P4-S1','for','对……的需求（need for）',pos='prep')
r.word('P4-S2','since','自从（2010年）以来',pos='prep');r.word('P4-S2','most','大多数（指死亡的树木）',pos='pron');r.word('P4-S2','them','被干旱和害虫杀死的树木',pos='pron')
r.word('P5-S1','plans','计划；打算',lemma='plan',pos='v');r.word('P5-S1','treat','治理；进行森林管理处理',pos='v');r.word('P5-S1','a','每（一年）',pos='det')
r.word('P5-S2','share','份额；部分',pos='n');r.word('P5-S2','that','关系代词，指可受益林地面积',pos='pron');r.word('P5-S2','about','大约',pos='adv');r.word('P5-S2','all','全部（in all合计）',pos='pron');r.word('P5-S2','so','因此；所以',pos='conj');r.word('P5-S2','it','形式主语，真正内容为优先治理高风险地区',pos='pron');r.word('P5-S2','risk','风险',pos='n');r.word('P5-S2','at','处于（最高风险）',pos='prep')
r.word('P6-S1','is','与locked/burned构成被动语态',lemma='be',pos='aux');r.word('P6-S1','that','关系代词，指车辆',pos='pron',occ=2);r.word('P6-S1','run','运行；行驶',pos='v');r.word('P6-S1','on','以……为动力（run on）',pos='prep')
r.word('P6-S2','under','与way组成正在进行',pos='prep')
r.word('P7-S1','state','州一级的（以名词修饰governments）',pos='n');r.word('P7-S1','to','习惯于（accustomed to）后的介词',pos='prep');r.word('P7-S1','focused','着重关注（focus on）',lemma='focus',pos='v');r.word('P7-S1','on','关注（focus on）的搭配介词',pos='prep');r.word('P7-S1','for','用于（休闲）',pos='prep')
r.word('P7-S2','come','逐渐；开始（come to see逐渐认识到）',pos='v');r.word('P7-S2','see','认识到；理解',pos='v');r.word('P7-S2','have','不得不；必须（have to）',pos='aux',occ=2);r.word('P7-S2','in','在……方面（发挥作用）',pos='prep')
r.word('P7-S3','is','与expected构成被动语态',lemma='be',pos='aux');r.word('P7-S3','be','与finalized构成被动语态',pos='aux');r.word('P7-S3','by','由（州长执行）',pos='prep');r.word('P7-S3','serve','充当（serve as）',pos='v')
r.sentence('P1-S2')['chunks'][2]['zh']='完成这一任务（指吸收二氧化碳）'
r.sentence('P2-S3')['chunks'][2]['zh']='在弄清具体做法方面'
r.sentence('P3-S3')['chunks'][3]['zh']='从空气中吸收碳'
ph(r,'P1-S2','count on','count on','指望；依靠');ph(r,'P1-S2','soak up','soak up','吸收');ph(r,'P2-S1','striking a subtle balance','strike a balance','取得一种微妙的平衡');ph(r,'P2-S3','leading the way','lead the way','走在前列；引领');ph(r,'P3-S1','thin out','thin out','疏伐；间伐');ph(r,'P3-S4','fend off','fend off','抵御；挡开');ph(r,'P3-S6','in the event of','in the event of','如果发生；遇到');ph(r,'P6-S1','in the form of','in the form of','以……的形式');ph(r,'P6-S2','under way','under way','正在进行');ph(r,'P7-S3','serve as','serve as','充当；起……作用')
checks(r,'''三项并列中quiet为宁静名词，against是应对气候变化，第三项挑战另行展开。
even as标出依赖与破坏的矛盾，good share相当多，so回指吸碳；删块译末重复的威胁能力。
当前人为加速气候变化，未来可能使森林排放超过吸收，could不写成定论。
striking a balance为取得平衡，不是敲击；this trap回指排碳超过吸收的困境。
看似反常但必须保留长期碳汇与现在降低能力对照，absorb物理吸收。
lead the way领先而非导致，does替代行为，as插语与in figuring领域连接；块译末不重复主干。
加倍的是疏伐清灌工作，不是树木数量；double和clear都是动词，brush灌木。
This指疏伐清灌，temporarily只暂时降低碳承载能力。
draw吸水，available可利用水分，so因果与restoring结果相接；最后块只译吸碳而非重复恢复能力。
fend off抵抗害虫，better修饰able保持比较含义。
landscape为整片林地环境，render被动引起可燃性降低，less修饰easily。
in the event of火灾让步，consumed烧毁而非消费，fewer比较损失。
need名词需求，planning管理规划，urgent迫切性增加。
since2010是时间而非原因，一亿多死树、大多在2016年、数十万英亩烧毁三组量不混。
a year每年，两目标为截至2020年35000和2030年60000英亩年度治理量，资金拍卖所得非排放数量。
总可受益面积约五十万英亩不是每年治理总量，risk名词，so推论优先高风险。
removed限定木质材料，封存与生物燃料利用二选，otherwise为不采用生物燃料的车辆原来能源。
under way为正在开展而非按某办法，transportation修饰燃料用途。
state州政府，accustomed to介词后动名词，传统关注野生动物流域及休闲。
Only recently倒装表示直到最近才，come to see逐渐认识，第二have是have to必须非完成时。
计划预计由州长明年定稿，by施动者，serve as为充当范例；明年沿原报道时间。''')
r.notes=['全篇重读短期减碳能力换取长期森林健康的因果链；按词位核定物理吸碳、疏伐、碳汇、拍卖融资与年度面积，消除三个重复块译。']
save(r)
