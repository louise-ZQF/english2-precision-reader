# 考研英语二本地版

[打开在线版](https://louise-zqf.github.io/english2-precision-reader/english/) · [GitHub 源码](https://github.com/louise-ZQF/english2-precision-reader)。推送 main 后由 GitHub Pages 自动更新，日常阅读、查词、收藏、文章导读、错题笔记和背词不需要付费接口或 AI 密钥。

本项目是原站 study.aseeker.bio/english 的个人学习改造版，保留来源说明，与原站无关联。仅提供 2010—2026 年英语二的 17 套真题，按桌面阅读使用，不另做手机版。

## 单词与词组

“进入精翻”后单击词语查义、双击收藏，悬停不弹释义。弹窗显示原形、本处词义、其他常见义和已收录的词形，不自动显示整句译文。复合词按完整拼写处理，词组按整体显示、收藏和复习；支持 spinning off 等词形和部分可分离动词短语。

2026 年 10 月重构采用统一的离线词义引擎，原文、生词本和背词使用同一套资料。免费基础词典来自 [ECDICT](https://github.com/skywind3000/ECDICT)，保留 [MIT 许可](reference/licenses/ECDICT-LICENSE.txt)，清除不适合阅读学习的技术领域义项和纯词形说明；简明词义、复合词及语法词另有独立编写的补充。

119 篇文章已逐篇编写导读，并按原文位置保存 4,155 处单词修订与 1,138 处词组修订，包含一词多义、比喻、熟词生义、原形和词性纠正。只有命中这些具体位置的修订才标“本文义”；其余显示“词典释义 · 按本句词性”，保留备选义，不能视为已逐词人工核对。旧的“从整句中文里匹配子串来猜词义”的规则已退出运行，旧自动释义会在展示时重新计算，用户自己的校正优先保留。有道与剑桥按钮用于主动核对，程序不抓取商业词典全文、不调用收费翻译接口。

每篇文章标题旁的“读懂文章”可查看主旨、各段要点、论证脉络和易误解表达，并可展开对照原段或写下自己的理解；原文仍保持自然段连续阅读排版。数据来源、修订范围和维护命令见 [词义重构说明](reference/lexical-refactor.md)。

## 精翻与学习记录

顶栏中央提供 Text 1—4 跳转，精翻开关随顶栏保持可见。句子编号嵌在行内，点编号查看译文与结构；从句、插入成分和修饰关系用颜色、编号和“续”标记表示。句法资料由 spaCy 离线生成，复杂结构仍可能判断错误，日常使用无需安装 NLP 包。

划选任意长度原文后可翻译实际选区，或右键收藏到长难句，不自动扩展到整句。收藏内容在原文中标红，收藏按钮会显示已收录；“长难句”入口提供原文定位、独立练习、草稿和复习进度。准确匹配的本地译文与人工重译优先，其余选区使用免费的 MyMemory 服务，失败时尝试 Google 翻译，仅发送选中文字，网络翻译仍可能不准确。单词查义本身完全离线。

“已翻译”勾选项、文章笔记与“记错题”按钮保留。“学习记录”提供年份 × 文章的翻译热力图、错题本和笔记，可记录自己的答案、正确答案、错因、复盘和订正状态；正确答案由用户核对详解后填写。既有收藏、个人释义、笔记、完成标记和 SRS 复习数据不会因题库更新而清空。

## 使用与备份

可双击同目录的“启动英语二.command”，默认访问 http://127.0.0.1:8766/english/；重复启动会复用服务或选择后续端口，关闭终端可停止。只需现有 Python 3，无需 Node 或 npm。也可直接打开 public/english/index.html，内置题库和精翻资料提供了本地文件模式的脚本副本。

收藏、笔记和学习进度保存在当前浏览器。file://、本地服务地址、在线版地址及不同浏览器分别保存记录，迁移时使用“数据”导出、导入备份。请勿清理浏览器数据代替更新页面。在线版不提供云同步或扫码中转，反馈只保存在当前浏览器；本地服务的反馈写入 .local-data/local.sqlite3。

核心阅读、词典、已收录译文、导读、收藏和背词可离线使用；在线发音、词典核对链接及未收录选区的翻译需要联网。线上 PDF 详解使用原站的公开下载链接，本地版使用 public/english-materials 中的资料，扫描原题仅用于纠正识别错误。

## 维护

主要实现位于 public/english/js/app.js、precision.js、lexical-engine.js、study.js 与 srs-panel.js，样式位于 css/precision.css、study.css。独立编写的词义修订与导读在 data/meaning-review，清理后的免费词典和匹配引擎分别为 js/lexical-data.js 与 js/lexical-engine.js。

运行 python3 scripts/build_lexical_data.py 从 reference/upstream/ecdict.csv 编译词典、所有内置试卷脚本与修订资料；原始 CSV 不提交仓库，来源及 SHA-256 记在重构说明中。修改某年的题文后，用 .venv/bin/python scripts/build_precision.py --exam 2025_english2 生成对应句法资料，再运行 python3 scripts/build_precision_browser.py。最后运行 python3 scripts/refresh_versions.py 刷新 JS/CSS 内容版本。

scripts/build_pages.py 负责 GitHub Pages 子路径打包，原站公开资源的来源与哈希保留在 reference/public-resources.json。旧的 context-senses.js、word-forms.js 仅保留作历史资料和构建输入，阅读页已不再加载旧词义推断规则。不要运行 scripts/prepare.py，它是初次还原脚本，会覆盖 app.js 的定制功能。

本轮仅做数据位置校验、必要语法检查和一次桌面交互核对，未建立大型测试套件或进行手机测试。
