# 2020、2021、2025、2026 阅读逐句审读记录

审读日期为2026年10月31日，本批共16篇、297个句子，均已完成英文正文核对、短语或从句分块、完整通俗中文、具体调序说明及词语在本文中的含义。16篇的 source.status 均为 verified，297句的 status 均为 reviewed；共有877个连续覆盖英文的分块、438个单词释义和185个短语释义。此处的“已核对”表示已逐篇对照所列试卷材料，不表示公开整理版具备官方原卷的权威性。

2020年四篇分别为18、19、20、18句，依据用户提供的《2020年考研英语二真题.pdf》第4、6、8、10个PDF页，文件SHA256为 `226bdb2bcac0604eda6f62a16062ce2dffe5bfeff86aae77be3eb0aa7d8d0ba5`。已阅读各页正文抽取并与全文逐句核对，未发现缺句。Text1现稿 colourful 与原卷抽取 colorful 存在英美拼写差异；Text2原卷出现 many mere skills than 及 It's not popular to say. but 等不规范字句，正文不擅自改写，中文按明确的比较和转折关系理解，并在具体词条、来源备注中说明。

2021年四篇分别为19、16、16、21句，依据用户提供的《2021年考研英语二真题.pdf》第4、6、8、10个PDF页，文件SHA256为 `dfadb189b791a7acdb709f18f3a29f3d74e59541e07cdbd4706f65f48e695fd2`。逐篇与本地试卷正文抽取核对后，修复Text1首段将 Research…2022. 与 That is a very short timeline. 误合为一句的阅读句界，英文段落及来源哈希不变。重点核查 reskilling、furlough、dairy、acqui-hires、rationale、battery、tapped 等词在各句中的实际含义，区分短期停职、收购人才及认知任务等语境。

2025年四篇分别为20、18、21、15句，依据用户提供的《2025考研英语二真题.pdf》第4、6、8、10个PDF页，文件SHA256为 `6e486744098ee282ce916ec6378c73a5fb1dde99ff467d4e7377010c1b295d17`。四篇均已实际查看扫描正文页并配合OCR核对。Text3先由主代理按扫描页修正 an HAP、informal dwellings that cope poorly with heat、Chandni Singh，再以修正后的正文开展本次审读；本批另合并 heat alert systems 与 -and 之间误断开的句界，仍完整保留该段英文。Text4首段原卷印为 desires paths，保留这个多出的s，按全文 desire paths 的一致用法解释为自发小径。

2025词条并非直接沿用旧词表即视作完成：逐条区分 tip/tips 的名词“小费”、tip/tipped 的动词“给小费”、传统收取小费的服务及适用于收小费员工的基本工资，修正 triggering thresholds 中 triggering 的修饰作用、alerts 与 heat wave alert threshold 中 alert 的名词“预警”，并补充示范计划、按本地情况调整、高温下难以应对的非正规住房等在正文明确位置的释义。癌症死亡率、婴儿死亡率以及高温预警门槛的数字与比较方向也已复核。

2026年四篇分别为19、21、18、18句，实际通过内置网页读取及 Agent Reach 网页渠道阅读[聚英公开试卷PDF](https://m.juyingonline.com/upload/202512/22/202512221526106084.pdf)，随后下载并读取PDF正文，PDF文件SHA256为 `12caa6867036c58ff5724f5080d54869dfe4a25daf2af6abe547c6f6e395b74b`。证据页为Text1第5—6页、Text2第8—9页、Text3第11—12页、Text4第13—14页；这些是PDF物理页码。该材料是非官方公开整理版，Text2存在重复句、information误拼，Text3存在跨行断句、Head大写及与现稿 investments 的版本差异，因此未把这些问题重新写回现稿，已保留来源局限。It gains Microsoft broad rights 中 gain 可以带双宾语，按“使微软获得广泛使用权”理解，未擅改为 gives。Text3原先将 …said Ferrovie. 与 RFI… 合并的记录已拆成真实的两句；mixed system means 中 means 已核准为动词“意味着”，与第一段交通 means 的名词“方式”分开。

完成后仅调用 scripts/build_reading.py 的 expected_articles 与 validate 校验本批16篇，全部通过。校验包括英文段落与既定来源逐字一致、来源文本哈希一致、句子完整覆盖段落、分块无遗漏或重叠且重建全部英文、词语与短语偏移精确绑定到原文、中文和调序说明及审读日期完整。本批未运行全局构建、浏览器测试、提交或推送，交由主代理统一整合。
