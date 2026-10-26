# 考研英语二本地版

这是 https://study.aseeker.bio/english/ 的英语二桌面复刻工程，保留原站公开提供的 HTML、CSS、图片、可读 JavaScript、FSRS 背词程序、词典和翻译句库，并补写了独立运行所需的本地服务。它可以继续修改和增加功能，不依赖作者的 GitHub 仓库。

双击同目录的 **启动英语二.command** 即可打开。当前默认地址是 **http://127.0.0.1:8766/english/**；再次双击会复用已经启动的服务，端口被其他程序占用时会自动选用后续端口。启动窗口需要保持打开，按 Ctrl+C 可以停止。不要直接双击 index.html，浏览器会限制 JSON 文件加载。此工程只需要现有的 Python 3，不需要安装 Node 或 npm 依赖。

本地版只保留 **2010—2026 年英语二的 17 套真题、17 份 PDF 详解、4,358 个英语二词条详情页**，已移除英语一和专业课入口。原站桌面的布局、配色、字号、单词释义气泡、收藏、单词本、复制、备份导入导出、划选翻译和间隔重复背词均沿用其公开实现，页面样式和背词引擎原文件保存在 reference/upstream 中。词条详情页和高频词表中的出处、累计频次及例句已限制为英语二；通用词典和按句检索的翻译库仍保留原始内容，以避免丢失词形与义项。

收藏单词和背词进度保存在当前浏览器的 localStorage 中，同一个网址在不同浏览器中是两份独立数据；原站已有收藏不会自动迁入，可以在原站使用“数据 → 导出数据”，再在本地版导入。反馈和纠错只保存至本机的 .local-data/local.sqlite3，不会发给原站作者，成功提示也已注明“保存在本机”。扫码中转接口按前端协议重写为本地的 24 小时一次性备份接口，默认只监听本机地址。

核心阅读、词典、已收录的逐句翻译、收藏、背词以及 PDF 下载可以离线使用。有道在线发音和必应翻译外链沿用原站方案，需要联网；在线音频失败时回退到浏览器自带朗读。原站的远程访问统计、设备登记和搜索引擎提交脚本已去除。原始服务器的私有程序、管理员系统和数据库不属于可获取的前端文件，本地服务根据公开前端的请求与返回格式独立实现，并非作者私有后端源码。

后续修改主要在 public/english/js/app.js（阅读、查词、收藏、翻译及备份）、public/english/js/srs-panel.js（背词界面）、public/english/js/srs-engine.js（背词调度）、public/english/css/style.css（原站样式）以及 server.py（本地 API）中进行。题库在 public/english/data/exam_*_english2.json，资料在 public/english-materials。修改 app.js 后，应把其 MD5 的前 10 位同步写入 data/version.json 的 app 字段以及 index.html 引用 app.js 的 v 参数，避免原程序的旧版本刷新检查发生误判。

scripts/capture.py 和 scripts/capture_word_pages.py 用于记录原站公开资源，scripts/prepare.py 用于从 reference/upstream 重建本地适配。**普通使用和继续开发无需运行这些脚本**；重新运行 prepare.py 会覆盖 public 中的相应修改，所以增加功能时直接编辑 public，并先保留自己的更改。

reference/local-scope.json 记录交付范围，reference/public-resources.json 记录实际保留资源的来源与 SHA-256。本工程只做还原和英语二范围调整，没有重新校勘原站题文、答案或机器翻译。网站界面、图片和整理内容的来源保留为原站，词典元数据标明 ECDICT 1.0.28（MIT），背词包内保留其上游说明。

按本次要求，仅做了必要的桌面核对：页面加载、年份切换、悬停查词与收藏、背词释义及评分入口；未进行手机测试或建立大型测试套件。
