# 2015—2019 全词位与逐句第二轮审查

2026-11-01 完成这五年的全部20篇：2015年77句、1626词位，2016年70句、1603词位，2017年76句、1610词位，2018年76句、1580词位，2019年92句、1631词位，合计391句、8050个可点击词位置。每句话实际重读英文、全部分块、语序说明和整译，按句记录具体语义核对点；每个位置均写入本文义、原形、词性和offset，不把旧有少数词义的数量当成全词审查。对同篇不同用法和跨文不同用法按位置覆盖。

本目录的20份 full_YYYY_tN.py 和 middle_full_review.py 是作者脚本，保留手写释义、逐位置修订和逐句核对说明。reuse只借用此前实际编写且形式、原型、词性、释义完全一致的单一义项作为编辑候选；每篇仍按英文语境读完全部候选词并改正不适用项，新词均手写，而非调用词典猜测填满。词位提取使用共享最新tokenizer，包含开引号后的首词、José等Latin重音字母、27-year-old和60-day等完整数字复合词。作者脚本用于追溯内容编辑，不应在最终统一词组分类后直接整批重跑，以免恢复旧phrases清单。

原文沿用已完成原卷核对的锁定版本和source.evidence，保留20篇textSHA256，没有改变英文、段落或句号边界，也没有边修英文边生成翻译。2016—2019原卷物理页4、6、8、10与提取层形似字的具体说明见上级reference/reading-audit-2016-2019.md。2015各篇已有原卷证据和独立作者记录。当前再审没有将自动OCR结果覆盖原卷有效文本；2017原卷Parkun的排字、2015 catch-up-with-household的连字符保持。

本轮明确改动的整译包括2015-T4-P1-S3改为“眼下看来，经济正以还不错的速度创造就业岗位”，避免把For now误当因为；2017-T1-P1-S2改为“公园跑起初只有十二位朋友参加，如今已带动英国开展400场活动，国外也另有开展”，不把more abroad断言成国外场次超过400；2017-T1-P4-S4把worthy strategies从贬义“冠冕堂皇”改为“冗长而立意良好的战略”；2019-T4-P8-S2改为“只是要从整体上恰当地看待个人行动的作用”，让put...into perspective的中文自然。2019-T2-P1-S2、P2-S3、P3-S3去除块译中重复的“威胁能力”“处于领先地位”“恢复能力”，使末块只对应原文不定式或介词短语；2019-T4-P3-S1同样去重，P3-S3把done our bit的块译明确成“尽了一份力”，避免夸大为尽全力。

2015年按语境核定right-brained、spinning off、personal fulfillment、bandwidth、capacity和boundaries，区分医保exchange、保险cover与普通交换/覆盖，buy into与购买分开；2016年区分教学班与阶层、School学院与普通学校、IT与it、suggests推荐与表明，that's become为that has，threatened和endangered的保护等级不同，physical阅读为纸质、challenging阅读为难读、state状态与州、六十多岁与上世纪六十年代分清。2016-T4双亲outside the home保留双方外出工作，不能按想当然把原文改写为一方居家。

2017年按位置核定am上午、time用时、court球场、free免费、state政府、conditions体育发展环境；still face experiment为静止面孔实验，wired为天生倾向，tablets为平板，very white为白人文化色彩而非白人至上；gap year为大学入学前暂缓一年，major专业、credits学分、complete动词与形容词、条件倒装的were you to均区分；森林火灾文章中fire为火、US美国、equation为综合因素，不能沿用解雇、代词或数学式。

2018年区分energy精力与能源、fund资助动词与基金名词、power供电动词与电力名词、generation发电与世代、capacity储电与注意力容量、field田野与运动场。亚马逊数据文章的link是绑定动词、physical实体、virtual网络、Whole Foods专名，who/whom和which customers是间接疑问，farm在蚂蚁/谷歌类比中是养育，benefit名词而buy advertising为购买。深度工作文章be it统领三种方法，have...scheduled是使安排好的结构非完成时，approach to后接动名词，while分别让步/对比，downtime休息、vice恶习、reap获得成果；both神经回路不擅自译成必须同时运转。

2019年内疚文章turn on取决于、deprivation没得到巧克力、hold...together维系、vice versa反过来、given给予，不能沿用打开、贫困诊断、成立、恶习或特定的等旧义。森林文章absorb为物理吸碳、brush灌木、double加倍动词、available可利用、consumed被火烧毁、a year每年、by截止；短期减小碳承载换取长期健康的反常逻辑与年度面积均保持。农场文章farm农场名词不能沿用数据文章的饲养动词，picking采收、consumed消费，it's been中的it's=it has，申请量和签发量、more than doubled增加一倍多、H-2A与H-2B限额、22天平均延误逐一核定。环保文章everyone's是每个人的所有格，primary主要而非小学，account问责名词而非占比动词，个人行动和制度变革并行不译成完全替代；印度2022承诺只按原报道保存，未宣称后来已经兑现。

用户新收紧词组定义后，已向统筹报告旧清单中的临时字符串和名称，统一由全库词组审查处理：Whole Foods、Deep Work书名、U.S. Fish and Wildlife Service等名称不能以词组标签出现；Ten years ago on Monday、were you to switch、nastier impulses、bigger, bolder, more effective actions、shape collective action等不应整体认作固定搭配。hold...to account、put...into perspective等应按可变固定结构处理，而非学习包含本句临时宾语的整串。最终词组清单以统筹统一合并后的分类为准。

本轮只执行保存时单篇内容校验，并在全部20篇保存后做一次本组只读offset/词性/覆盖一致性检查；没有浏览器回归、全局构建、新增测试、提交或推送。程序确认不漏词、不漏句、offset对齐，不能据此宣称语义绝无误差；本记录说明实际复核范围和修改内容。
