# -*- coding: utf-8 -*-
from middle_full_review import *
r=make('2015-T4')
lex(r,'''talked@talk/v=谈到；把……说成;jobs@job/n=就业岗位；工作;new/a=新增的;labor/n=劳动；劳工;department/n=部门（Labor Department为劳工部）;reported@report/v=公布；报告;june@June/name=六月;along/adv=与……一起（along with）;drop/n=下降;unemployment/n=失业;rate/n=比率；比例;percent/n=百分之;good/a=好的；有利的;news/n=消息;right/a=正确的;appears@appear/v=看来；似乎;economy/n=经济;creating@create/v=创造;decent/a=还不错的；相当好的;pace/n=速度;long/a=长的;way/n=路程；进程;go/v=走；继续前进;get/v=达到；恢复（get back）;back/adv=恢复原状（get back）;full/a=充分的；全额的;employment/n=就业;least/adv=至少（at least）;finally/adv=终于;moving@move/v=前进；推进;forward/adv=向前;faster@fast/a=更快的;however/adv=然而;important/a=重要的;part/n=方面；部分;picture/n=总体状况；形势;largely/adv=在很大程度上;overlooked@overlook/v=忽视;big/a=大的;jump/n=大幅增长;number/n=人数；数量;report/v=自述；报告;voluntarily/adv=自愿地;working@work/v=从事工作;part-time/a=非全日制的；兼职的;figure/n=数字；人数;above/prep=高于；超过;year/n=年;ago/adv=以前;level/n=水平;explaining@explain/v=解释;connection/n=联系;obamacare@Obamacare/name=奥巴马医改；《平价医疗法案》的通称;worth/a=值得的；有必要的;making@make/v=作出（区分）；做;distinction/n=区分;actually/adv=实际上;want/v=想要;full-time/a=全职的；全日制的;take/v=接受（工作）;increase/n=增加;involuntary/a=非自愿的；被迫的;evidence/n=证据；表现;weakness/n=疲软；状况不佳;market/n=市场;means@mean/v=意味着;having@have/v=经历；面临;hard/a=艰难的;time/n=时期；时段;ends@end/n=收支的两头（make ends meet整体为维持生计）;meet/v=使相接（make ends meet整体为收支相抵）;general/a=总体的;direction/n=方向；趋势;down/adv=下降;far/adv=远远地（加强比较）;higher@high/a=更高的;recession/n=经济衰退;by/prep=以……幅度；由;difference/n=区别;voluntary/a=自愿的;tell/v=告诉;survey/n=调查;used@use/v=采用；使用;asks@ask/v=询问;worked@work/v=工作;hours@hour/n=小时;reference/a=供统计参照的;week/n=周;answer/n=回答;yes/adv=是；肯定回答;classified@classify/v=分类；归类;wanted@want/v=想要;choice/n=选择;workers@worker/n=工作者;taker/n=调查执行者（survey taker整体为调查员）;chose@choose/v=选择;issue/n=问题；讨论的议题;relates@relate/v=有关联；相关;one/num=一个；一项;main/a=主要的;purposes@purpose/n=目的;allow/v=让；使能够;insurance/n=医疗保险;outside/prep=在……之外；不依附于;especially/adv=尤其;serious/a=严重的;health/n=健康;conditions@condition/n=疾病；健康问题;family/n=家人；家庭;members@member/n=成员;through/prep=通过；经由;job/n=工作;provided@provide/v=提供;allowed@allow/v=使能够;million/num=百万;either/conj=或者（either...or）;medicaid@Medicaid/name=医疗补助计划（美国项目名）;exchanges@exchange/n=医保交易平台;previously/adv=此前;felt@feel/v=觉得；感到;need/n=必要性;order/n=目的（in order to整体表示为了）;cover/v=为……提供保险保障;themselves/pron=他们自己;families@family/n=家人；家庭;longer/adv=更久（no longer整体为不再）;link/n=联系；绑定关系;know/v=知道；分辨''')
r.word('P1-S1','of','谈到的对象（talk of）',pos='prep');r.word('P1-S1','for','对应（六月的统计）',pos='prep');r.word('P1-S1','to','降至；达到某数值',pos='prep');r.word('P1-S1','as','当作；认为是',pos='prep')
r.word('P1-S3','for','与now组成for now，表示眼下；目前',pos='prep');r.word('P1-S3','is','助动词，与creating构成进行时',lemma='be',pos='aux');r.word('P1-S3','at','以……速度',pos='prep');r.sentence('P1-S3')['translation']='眼下看来，经济正以还不错的速度创造就业岗位。';r.sentence('P1-S3')['chunks'][0]['zh']='眼下看来，';r.sentence('P1-S3')['reorder']='按“目前看来—创造岗位—速度”顺译，at a decent pace放在“创造”前更自然。'
r.word('P1-S4','have','还有；拥有',pos='v');r.word('P1-S4','to','恢复到（get back to）',pos='prep',occ=3);r.word('P1-S4','are','助动词，与moving构成进行时',lemma='be',pos='aux');r.word('P1-S4','at','以……速度',pos='prep',occ=2);r.word('P1-S4','at','与least组成至少',pos='prep',occ=1)
r.word('P2-S1','there','there be存在句的引导词，不单译',pos='pron');r.word('P2-S1','is','有（there is）',lemma='be',pos='v');r.word('P2-S1','that','关系代词，指就业情况的重要方面',pos='pron');r.word('P2-S1','was','助动词，与overlooked构成被动语态',lemma='be',pos='aux')
r.word('P2-S2','there','there be存在句引导词',pos='pron');r.word('P2-S2','was','出现；有（there was）',lemma='be',pos='v');r.word('P2-S2','in','在人数方面',pos='prep')
r.word('P2-S3','above','高于；比一年前增加（不是总人数）',pos='prep')
r.word('P3-S1','to','与……的联系（connection to）',pos='prep');r.word('P3-S1','it','形式主语，指下文作出区分这件事',pos='pron')
r.word('P3-S2','work','从事；做（某工作）',pos='v')
r.word('P3-S4','in','在……方面（兼职就业的增加）',pos='prep',occ=1);r.word('P3-S4','in','在劳动力市场中',pos='prep',occ=2);r.word('P3-S4','be','助动词，与having构成进行时',pos='aux');r.word('P3-S4','making','设法做到（make ends meet整体指维持生计）',lemma='make',pos='v')
r.word('P4-S1','there','there be存在结构引导词',pos='pron');r.word('P4-S1','was','出现；有（there was）',lemma='be',pos='v')
r.word('P4-S2','by','减少了……（标示降幅）',pos='prep');r.word('P4-S2','from','与……相比（同比参照）',pos='prep')
r.word('P5-S2','by','由（劳工部采用）',pos='prep');r.word('P5-S2','if','是否（引出调查问题）',pos='conj')
r.word('P5-S3','are','与classified构成被动语态',lemma='be',pos='aux');r.word('P5-S3','as','归类为',pos='prep')
r.word('P5-S4','had','有；拥有（have no choice整体为别无选择）',lemma='have',pos='v');r.word('P5-S4','that','那一个（指统计参照周）',pos='det')
r.word('P5-S5','are','与classified构成被动语态',lemma='be',pos='aux');r.word('P5-S5','as','归类为',pos='prep');r.word('P5-S5','if','只有在……条件下（受only限定）',pos='conj');r.word('P5-S5','a','每（a week每周）',pos='det')
r.word('P6-S1','to','与……有关（relate to）',pos='prep',occ=1);r.word('P6-S1','of','其中一个（one of）的范围',pos='prep',occ=2)
r.word('P6-S2','for','对……来说',pos='prep');r.word('P6-S2','with','患有；存在（健康问题）',pos='prep');r.word('P6-S2','that','关系代词，指一份提供医保的工作',pos='pron')
r.word('P7-S1','than','与more组成“超过”',pos='prep');r.word('P7-S1','or','或者（两种医保渠道）',pos='conj')
r.word('P7-S2','have','助动词，与felt构成完成时',pos='aux');r.word('P7-S2','that','关系代词，指提供保险的工作',pos='pron');r.word('P7-S2','in','与order to组成为了',pos='prep')
r.word('P7-S3','with','随着；在实施医改的条件下',pos='prep');r.word('P7-S3','there','there be存在句引导词',pos='pron');r.word('P7-S3','is','存在（there is）',lemma='be',pos='v')
checks(r,'''talk of...as把两个就业指标视为好消息，新增岗位与失业率数据不混。
right指判断正确，they承接对数据乐观的人。
for now按“眼下”处理，is creating进行时，decent为尚可而非道德体面。
仍远离充分就业，但速度加快；least与at组成至少。
that指就业状况的一方面，was overlooked被动表示被忽视。
增长的是自愿兼职人数，不是所有兼职或总就业。
83万为同比增加量、4.4%为增幅，不能译成当前总数。
在说明医保联系前先区分兼职性质，it为形式主语。
做兼职者可能实际想全职，两个岗位时长类型对比保留。
all they can get表示只能找到这类工作，非主动追求兼职。
非自愿兼职增加意味着市场疲软，make ends meet整体为维持生计。
六月单月增长与长期总体下降分开，不以单月代替趋势。
比较基准一为衰退前、一为一年前；64万与7.9%是降幅。
区别基于受访者自述，不凭调查者推断动机。
if为是否，参照周工作不足35小时，不含正好35小时。
回答为是仅归类兼职，尚未区分是否自愿。
再问少于35小时的原因：主动选择或别无选择，had实义有。
only if为必要条件，a week中的a为每，不是不定数量。
主旨是让医保脱离就业依附，outside employment不指工作场所外。
健康状况指疾病，家人有病亦在目标群体，that修饰提供医保的岗位。
Medicaid和exchanges是两类医保渠道，不是证券交易所。
此前为家庭获得保险而需全职，cover是保险保障不是遮盖。
结论依文章历史语境呈现，不当作现行制度保证。''')
lex(r,'work/n=工作')
r.word('P5-S4','work','工作',pos='v')
r.word('P5-S5','work','工作',pos='v')
r.notes=['重审自愿与非自愿兼职、同比增减、调查分类和医改历史语境；所有英文词位置有独立释义。']
save(r)
