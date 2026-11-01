# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2016-T3'),['2015-T1','2015-T2','2015-T3','2015-T4','2016-T1','2016-T2'])

lex(r,'''everyone's@everyone be/pron=每个人都……（everyone is缩写）;busy/a=忙碌的;days@day/n=日子；时期;cliché/n=老生常谈;specific/a=具体的；特定的;complaint/n=抱怨;made@make/v=提出；表达;mournfully/adv=哀怨地;there's@there be/pron=有；存在（there is缩写）;time/n=时间;read/v=阅读;thornier@thorny/a=更棘手的;usual/a=通常的;time-management/a=时间管理的;techniques@technique/n=技巧;seem/v=似乎;sufficient/a=足够的;web's@web be/n=网络上是……（web is缩写）;articles@article/n=文章;offering@offer/v=提供;tips@tip/n=窍门；建议;making@make/v=腾出；安排（时间）;give/v=放弃（give up）;tv@TV/n=电视节目;carry/v=携带;book/n=书;times@time/n=时间；时刻;methods@method/n=方法;free/v=腾出；使空出;up/adv=空出来（free up）;odd/a=零星的；偶尔空出的;minutes@minute/n=分钟;work/v=奏效；起作用;sit/v=坐;down/adv=下来（sit down）；回到阅读状态（drop down）;flywheel/n=飞轮（比喻不停转动的思绪）;work-related/a=与工作有关的;thoughts@thought/n=思绪;keeps@keep/v=保持；持续;spinning@spin/v=旋转;else/adv=否则；其他的;exhausted/a=疲惫不堪的;challenging/a=费脑力的；有难度的;book's@book be/n=书是……（book is缩写）;last/a=最不想要的（the last thing）；最后的;need/v=需要;modern/a=现代的;mind/n=头脑；心智;tim@Tim/name=蒂姆（人名）;parks@Parks/name=帕克斯（姓氏）;novelist/n=小说家;critic/n=评论家;overwhelmingly/adv=极其；压倒性地;inclined/a=倾向于的;communication/n=交流;simply/adv=仅仅；只是;interrupted@interrupt/v=被打断;one/pron=人；人们（泛指）;interruption/n=打断；干扰;deep/a=深入的;reading@reading/n=阅读;special/a=特殊的;obtained@obtain/v=获得;merely/adv=仅仅;by/prep=通过；凭借;becoming@become/v=变得;efficient/a=高效的;thinking@think/v=把……看作（think of...as）；思考;resource/n=资源;maximised@maximise/v=尽量充分利用;instrumentally/adv=作为达成目的的工具地;judging@judge/v=评判；认为;given/a=某一特定的；任意给定的;moment/n=时刻;well/adv=好地；值得地;spent@spend/v=花费；度过;far/adv=程度（in so far as整体为以……为限）;advances@advance/v=推进;immersive/a=沉浸式的;contrast/n=对比（by contrast整体为相比之下）;depends@depend/v=取决于；依赖;willing/a=愿意的;risk/v=冒……风险;inefficiency/n=低效率;goallessness/n=没有目标;time-wasting/n=浪费时间;slot/v=把……安排进；塞进;to-do/a=待办的;list/n=清单;item/n=一项安排;manage/v=做到；进行;goal-focused/a=目标导向的;useful/a=有用的;sometimes/adv=有时;fulfilling/a=令人满足的;comes@come/v=到来；涌来;like/prep=像……一样;empty/a=空的;bottles@bottle/n=瓶子;unstoppable/a=无法停止的;nearly/adv=几乎;conveyor/n=传送装置（conveyor belt为传送带）;belt/n=带（conveyor belt为传送带）;gary@Gary/name=加里（人名）;eberle@Eberle/name=埃伯利（姓氏）;sacred/a=神圣的（书名一部分）;pressure/n=压力;different-sized/a=大小不一的;pass/v=经过；流逝;get/v=过去；溜走（get by）；使;filled@fill/v=填满;wasted@waste/v=浪费;mind-set/n=心态；思维方式;worse@bad/a=更糟的;losing@lose/v=沉浸；忘我（lose oneself in）；失去;perhaps/adv=也许;scheduling@schedule/n=安排时间；排期;you'd@you would/pron=你会；你也许会（you would缩写）;think/v=以为；思考;fuel/v=助长；加强;efficiency/n=效率;ritualistic/a=仪式性的；形成固定仪式的;behaviour/n=行为;helps@help/v=帮助;step/v=迈步（step outside比喻走出）；走出;outside/prep=在……之外;time's@time/n=时间的（所有格）;flow/n=流动；流;soul/n=心灵;limit/v=减少；限制;distractions@distraction/n=干扰;single-purpose/a=单一用途的;e-readers@e-reader/n=电子阅读器;providing/conj=只要；条件是;dip/v=翻阅；短时投入阅读（dip in）;default/a=默认的；常态的;temporarily/adv=暂时地;surface/v=浮出；暂时抽身;take/v=处理（take care of）;care/n=照管；处理（take care of）；关照;business/n=事务；事情;dropping@drop/v=重新沉入（阅读）;back/adv=返回；回去;day/n=一天;feels@feel/v=感觉起来;everything/pron=一切事物''')
r.word('P1-S1','that','主语从句连接词，将整句话作主语',pos='conj')
r.word('P1-S2','one','一项',pos='num');r.word('P1-S2','is','与made构成被动语态',lemma='be',pos='aux')
r.word('P2-S1','makes','使；让',lemma='make',pos='v');r.word('P2-S1','what','使问题更棘手的因素',pos='pron')
r.word('P2-S2','full','满是……的（full of）',pos='a');r.word('P2-S2','up','放弃（give up）',pos='adv');r.word('P2-S2','with','随身携带（with you）',pos='prep');r.word('P2-S2','at','在任何时候（at all times）',pos='prep')
r.word('P2-S3','in','根据；就经验而言',pos='prep')
r.word('P2-S4','and','就；于是（祈使句后接结果）',pos='conj');r.word('P2-S4','or','要不然（or else）',pos='conj');r.word('P2-S4','that','引出so...that的结果“以至于”',pos='conj');r.word('P2-S4',"you're",'you are的缩写；你已经处于疲惫状态',lemma='you be',pos='v')
r.word('P2-S5','toward','倾向于（inclined toward）',pos='prep')
r.word('P2-S6','is','与interrupted构成被动语态',lemma='be',pos='aux',occ=2);r.word('P2-S6','to','倾向于（inclined to）',pos='prep')
r.word('P2-S7','requires','需要',lemma='require',pos='v');r.word('P2-S7','but','而是（not just...but）',pos='conj');r.word('P2-S7','be','与obtained构成被动语态',pos='aux')
r.word('P3-S2','of','把……看作（think of...as）',pos='prep');r.word('P3-S2','be','与maximised构成被动语态',pos='aux');r.word('P3-S2','approach','对待；处理',pos='v');r.word('P3-S2','as','看作（think of...as或judge...as）',pos='prep',occ=1);r.word('P3-S2','as','视为（judge...as）',pos='prep',occ=2);r.word('P3-S2','as','与in so far组成仅限于／只有在……范围内',pos='conj',occ=3)
r.word('P3-S3','by','在by contrast中表示相比之下',pos='prep');r.word('P3-S3','on','取决于（depend on）',pos='prep')
r.word('P3-S4','and','那么；结果就（条件到结果）',pos='conj');r.word('P3-S4','in','把阅读安排进去（slot in）',pos='adv');r.word('P3-S4','it','沉浸式阅读',pos='pron')
r.word('P3-S5','future','未来',pos='n');r.word('P3-S5','along','沿着',pos='prep');r.word('P3-S5','at','向……而来（come at）',pos='prep');r.word('P3-S5','as','当……经过时',pos='conj');r.word('P3-S5','for','因为（解释前述压力）',pos='conj');r.word('P3-S5','by','过去；溜走（get by）',pos='adv');r.word('P3-S5','being','与filled构成被动语态',lemma='be',pos='aux')
r.word('P3-S6','for','对沉浸阅读这件事而言',pos='prep');r.word('P3-S6','could','可能（否定比较加强最坏程度）',pos='aux')
r.word('P4-S1','so','那么；于是',pos='adv');r.word('P4-S1','what','什么办法（疑问代词）',pos='pron')
r.word('P4-S2','regular','定期的；固定的',pos='a');r.word('P4-S2','for','用于（阅读）',pos='prep')
r.word('P4-S4','physical','实体的；纸质的',pos='a');r.word('P4-S4','on','使用某设备阅读',pos='prep')
r.word('P4-S5','too','也',pos='adv');r.word('P4-S5','in','投入阅读中（dip in）',pos='adv');r.word('P4-S5','so','与that组成以便／从而',pos='conj');r.word('P4-S5','that','与so组成从而',pos='conj');r.word('P4-S5','state','状态',pos='n');r.word('P4-S5','from','从阅读常态中抽身',pos='prep')
r.word('P4-S6','on','在……一天',pos='prep');r.word('P4-S6','as','与if组成仿佛／好像',pos='conj');r.word('P4-S6','if','与as组成仿佛／好像，而非条件如果',pos='conj')
checks(r,'''That主语从句概括老生常谈，everyone's为everyone is。
is made被动说明哀怨地抱怨，there's表示存在，never否定阅读时间。
makes是使问题更棘手，thornier比较级与通常方法不足之间的关系明确。
Give up为放弃电视，full of不是充分的，tips为建议而非小费。
odd半小时为零星时间，work为奏效；不按奇怪或劳动释义。
祈使句and引出结果，or else为要不然，challenging是费脑而非法律挑战。
插入作者身份不打断主语mind与谓语is inclined。
第二个is为被动interrupted，最后inclined to是倾向受打扰，one泛指人。
所需是特殊时间，不能仅靠效率获得；be obtained被动和否定保留。
提高效率本身成为问题的一部分，part不指就业方面。
approach是动词对待，工具化时间以推进目标为唯一评判标准。
沉浸阅读需容许无效率无目标，与前句工具化时间对照。
条件祈使句and表示那么，list是清单，最满足的阅读不等于最有用。
未来与瓶子传送带类比，for为因为，as为当……时，by是溜过。
No...worse为没有更糟即最坏心态，losing oneself是沉浸非迷失。
what疑问什么办法，does为强调，work为奏效。
regular是固定有规律而非普通，答案为安排阅读时间。
fuel比喻助长，ritualistic行为帮助进入心灵时间，非真的停止时钟。
physical books为纸质书，on表示用阅读器，by为方法。
providing为只要，too为也，state为状态，take care of business为处理事务。
as if为仿佛，不是如果；把阅读变常态、其他事另腾时间的转变保留。''')
r.notes=['逐词重审阅读与时间工具化的比喻；纠正work、approach、state、physical、challenging等熟词生义，覆盖所有位置。']
save(r)
