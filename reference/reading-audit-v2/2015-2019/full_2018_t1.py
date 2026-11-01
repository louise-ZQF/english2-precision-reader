# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2018-T1'),[f'{y}-T{n}' for y in [2015,2016,2017] for n in range(1,5)])

lex(r,'''curious/a=令人奇怪的;stephen@Stephen/name=斯蒂芬（人名）;koziatek@Koziatek/name=科齐亚特克（姓氏）;almost/adv=几乎;though/conj=与as组成仿佛；好像;justify/v=说明正当性；为……辩解;give/v=给予；让……拥有;better@good/a=更好的;future/n=未来;mr@Mr/title=先生;part/n=部分（be part of表示参与其中）;pioneering/a=具有开创性的;teacher/n=教师;new/a=新的;hampshire@Hampshire/name=罕布什尔（州名一部分）;high/a=高中的（high school）；高的;school/n=学校;tests@test/n=考试;mechanical/a=机械式的；不加理解的;memorization/n=背记；记忆;accepted@accepted/a=被普遍接受的;able/a=有能力的;name/v=说出……的名字;president/n=总统;states@State/name=美国国名United States的一部分;utterly/adv=完全地;overwhelmed@overwhelmed/a=无所适从的；束手无策的;by/prep=面对；由于；通过（依语境）；broken@broken/a=断裂的；坏了的;bike/n=自行车;chain/n=链条;knows@know/v=知道;nothing/pron=没有任何东西；没有任何益处;gained@gain/v=获得;forcing@force/v=强迫;learn/v=学习;geometry/n=几何学;graffitied@graffiti/a=有涂鸦的;desk/n=课桌;stuck@stick/v=粘着；附着;discarded@discard/v=丢弃;chewing@chew/n=咀嚼（chewing gum合指口香糖）;gum/n=口香糖;assembling@assemble/v=组装;bicycle/n=自行车;he's@he have/pron=他已经……（he has缩写）；完成时;insidious/a=隐蔽而有害的;prejudice/n=偏见;working@work/v=劳动；工作;hands@hand/n=手;seen@see/v=被看作；视为;mark/n=标志;inferiority/n=低人一等；较差的地位;vocational/a=职业教育的;stereotype/n=刻板印象;it's@it be/pron=它是；这是（it is缩写）;make/v=取得成功（make it）；做到;academically/adv=在学业上;one/num=一个;viewpoint/n=观点;logical/a=合乎逻辑的;product/n=产物;america's@America/name=美国的（所有格）;america@America/name=美国;evolution/n=发展演变;manufacturing/n=制造业;economic/a=经济的;engine/n=引擎；驱动力;once/adv=曾经;job/n=工作；就业;security/n=保障；稳定性;offered@offer/v=提供;graduates@graduate/n=毕业生;evaporated@evaporate/v=消失（比喻）；蒸发;principle/n=信条；原则;rightfully/adv=合理地；理所应当地;headlong/a=盲目急进的；不加审慎考虑的;push/n=推动；倡导;bachelor's@bachelor/n=学士的（bachelor's degree合指学士学位）;subtle/a=不易察觉的；隐性的;devaluing@devalue/n=贬低价值;anything/pron=任何事物；所有其他较低学历;misses@miss/v=忽略；漏掉;that's@that be/pron=那是（that is缩写，指学士学位）；指代前述路径;opens@open/v=打开；带来（机会）;doors@door/n=机会（比喻）；门;percent/n=百分之;middle-skill/a=中等技能的;high-skill/a=高技能的;adequately/adv=充分地；达到要求地;trained@train/v=接受培训;class/n=阶级；阶层;turned@turn/v=颠覆（turn...on its head）；转变;political/a=政治的;head/n=头（on its head比喻颠覆）；frustrated/a=失望受挫的;opportunity/n=机会;vanishing@vanish/v=消失;obvious/a=显而易见的;staring@stare/v=摆在眼前（stare...in the face，比喻）；凝视;face/n=面前；脸;gap/n=缺口；差距;working-class/a=工人阶级的；蓝领的;equipped@equip/a=具备所需技能的；准备就绪的;koziatek's@Koziatek/name=科齐亚特克的（所有格）;manchester@Manchester/name=曼彻斯特（地名）;technology/n=技术;wake-up/a=警醒的（wake-up call）；唤醒的;call/n=警示；提醒（wake-up call整体）；呼唤;one-size-fits-all/a=一刀切的；不顾个体差异的;risks@risk/v=冒着……风险；有可能造成;overlooking@overlook/v=忽视;nation's@nation/n=国家的（所有格）;diversity/n=多样性;gifts@gift/n=天赋；才能;need/v=需要;time/n=时间'''.replace('；broken@broken',';broken@broken'))
r.word('P1-S1','as','与though组成仿佛；好像',pos='conj');r.word('P1-S1','has','必须（has to），非完成时',lemma='have',pos='aux');r.word('P1-S1','it','形式主语，指需要为改善学生未来作辩解这件事',pos='pron')
r.word('P2-S2','new','新（New Hampshire州名一部分）',lemma='New',pos='name');r.word('P2-S2','learning','学习（名词）',lemma='learning',pos='n');r.word('P2-S2','but','而是（not...but）',pos='conj')
r.word('P2-S3','when','何时（疑问）',pos='adv');r.word('P2-S3','did','助动词，构成过去时疑问',lemma='do',pos='aux');r.word('P2-S3','by','面对（自行车链条问题而束手无策）',pos='prep');r.word('P2-S3','be','处于……状态，连接able/overwhelmed',pos='v')
r.word('P3-S1','as','正如',pos='conj');r.word('P3-S1','there','there be存在结构引导词',pos='pron');r.word('P3-S1','is','有；存在（there is）',lemma='be',pos='v');r.word('P3-S1','learning','可以学到的知识（名词）',lemma='learning',pos='n');r.word('P3-S1','just','与about组成几乎',pos='adv');r.word('P3-S1','about','大约；几乎（just about）',pos='adv')
r.word('P3-S2','is','与gained构成被动语态',lemma='be',pos='aux');r.word('P3-S2','by','通过强迫学习这一方式',pos='prep');r.word('P3-S2','generations','一届又一届学生（比喻）',lemma='generation',pos='n');r.word('P3-S2','with','附着；粘有（口香糖）',pos='prep')
r.word('P3-S3','by','通过组装自行车',pos='prep')
r.word('P4-S2','with','用（双手）',pos='prep');r.word('P4-S2','is','与seen构成被动语态',lemma='be',pos='aux');r.word('P4-S2','as','看作；当作',pos='prep')
r.word('P4-S3','family','体系；同类学校群体（比喻）',pos='n');r.word('P4-S3','have','有；背负着（刻板印象）',pos='v');r.word('P4-S3','that','这样的（指示限定词，修饰stereotype）',pos='det',occ=1);r.word('P4-S3','that','引出刻板印象的具体内容',pos='conj',occ=2);r.word('P4-S3','for','面向；为……开办的',pos='prep');r.word('P4-S3','it','make it搭配中的形式宾语，整体表示成功',pos='pron')
r.word('P5-S1','on','与one hand组成一方面',pos='prep');r.word('P5-S1','that','那种（指前述低看动手劳动的观点）',pos='det')
r.word('P5-S2','that','关系代词，指过去充当的经济引擎',pos='pron')
r.word('P5-S3','that','关系代词，指job security就业保障',pos='pron');r.word('P5-S3','US','美国（United States缩写）',lemma='US',pos='name');r.word('P5-S3','to','提供给（高中毕业生）',pos='prep')
r.word('P5-S4','more','更多的（教育）',pos='det')
r.word('P5-S5','more','更多更好的发展机会',pos='pron');r.word('P5-S5','for','为孩子',pos='prep')
r.word('P6-S1','less','程度更低的；低于学士学历的',pos='a');r.word('P6-S1','all','所有人',pos='pron');r.word('P6-S1','only','唯一的',pos='a')
r.word('P6-S2','yes','的确；诚然（承认前述观点有道理）',pos='interj');r.word('P6-S2','more','更多的（机会）',pos='det')
r.word('P6-S3','as','例如（such as）',pos='prep');r.word('P6-S3','construction','建筑业',pos='n')
r.word('P6-S4','are','与trained构成被动语态',lemma='be',pos='aux')
r.word('P7-S1','working','工人的（working class）',lemma='work',pos='a');r.word('P7-S1','that','关系代词，指机会',pos='pron',occ=2);r.word('P7-S1','is','与vanishing/staring构成进行时',lemma='be',pos='aux');r.word('P7-S1','on','颠覆（turn...on its head）',pos='prep')
r.word('P7-S2','do','做；胜任这些工作',pos='v');r.word('P7-S2','most','最需要；程度最高',pos='adv')
r.word('P7-S3','is','与trying构成进行时',lemma='be',pos='aux');r.word('P7-S3','that','上述岗位与技能缺口（指示限定词）',pos='det')
checks(r,'''curious为令人奇怪，has to为必须而非完成时，as though为仿佛。
pioneering形容开创性，be part of参与其中不直译成一个人的一部分。
New属于州名，learning为名词，not...but对照书本死记与实践。
when疑问何时，did助动疑问，name为动词说出总统名，be overwhelmed为束手无策。
as正如，learning名词知识，just about几乎，非关于。
Nothing necessarily gained是否定确定收益，by为方式，generations指历届学生。
by组装自行车是另一种学习几何方式，不遗漏also。
he's此处he has，found完成时，insidious指隐蔽有害。
seen as被动看作，with为用手，inferiority描述社会偏见而非事实。
family为职业教育体系，have实义背负，make it是学业成功。
that为指示限定词，America's为国家演变背景而非企业界。
经济引擎的过去现在对比，not不扩大为制造业完全没作用。
security为就业保障，US为美国，offered to给毕业生，has完成时。
more为更多教育，principle为新的普遍信条。
more指更好前途，rightfully承认家长期待合理。
anything less指低于学士层次，not only保留经济还需其他技能。
doors为机会比喻，yes让步承认学位确有优势。
54%岗位为中等技能，原文同时列高技能制造业，不擅自改分类。
44%劳动者受过足够培训，are trained被动，only限制比例。
frustrated修饰工人阶级，两个that区分原因与机会限定，政治格局被颠覆。
空缺岗位与技能不匹配，do为实义胜任，them指工作。
that指前述技能缺口，学校尝试填补，is trying进行时。
wake-up call为警示，不是闹钟叫醒电话。
gifts为天赋非礼物，one-size-fits-all为一刀切，风险在忽视多样性。''')
r.notes=['逐词复核教育与劳动力匹配论证，保留原文制造业岗位分类，纠正give、family、name、security、gifts与US等跨篇候选义。']
save(r)
