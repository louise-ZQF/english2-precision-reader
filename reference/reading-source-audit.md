# 英语二阅读原文核对记录（2026-10-31）

正文按年、Text、段落、句子分别保存在 `public/english/data/reading/`。每篇的 `source.evidence` 记录核对用PDF文件、页码与文件SHA-256，`source.textSHA256` 锁定用于编辑的英文。原卷排版本身不完整的表达保留并加说明，不能根据中文猜补英文。2010—2025主要依据用户提供的历年原卷；2026使用公开整理版，来源与局限另见该年各篇source记录。

对照原卷发现的旧题库实质差异及处理：2022 Text 1删去原卷没有的生产商背景；Text 2删去额外统计，恢复2019与2,000。2023 Text 1修正environmental、problems及spend an average of £500 on等录入错误；Text 2补回调查方法、是否实际参观的限定、埃利斯岛与葛底斯堡实例及2009经济刺激计划，恢复$3 billion；Text 4修正questionnaires、that needed及漏句号。2024 Text 1删去原卷未收录的新闻导语与额外背景；Text 2补回生产性林业观念、灰松鼠破坏及土地所有者投资犹豫的两句，恢复biodiversity health；Text 3恢复开头比较结构、keys、older、too many及原卷段界；Text 4将误录的sensitivity fertility恢复为sensitive fertility。2025 Text 3依原卷修正an HAP、informal dwellings that cope poorly with heat、Chandni Singh，合并插入语处误断的句界。

句界单独复核：2010 Text 1的拍卖展标题被误切成两句，2011 Text 4的冒号续句被误断；在阅读文件内合回，不改变段落英文。类似修订保持段落哈希不变，句子编号按真实句界重新排列。编号与英文一起检查，不能只凭旧编号把旧词义强行迁移。

旧 `meaning-review` 中45条已不再匹配校正原文的记录，存入 `reference/reading-legacy-retired-20261031.json` 供追溯，并退出运行时旧词义表。对应阅读的翻译与词义由新的逐篇文件负责；用户浏览器中的收藏、个人校正、笔记与完成状态不作清理。

内容编辑重点包括否定、比较、指代、数字范围、固定搭配及词性：例如reasons在“三个理由”中为“理由”，confounding variable中的variable为“变量”，beyond what表示“超出”，而不是把同词在另一句中的解释套过来。完整译文独立检查中文语序；分块英文须逐字符拼回原句，程序只检查完整性和位置，不替代语义审读。
