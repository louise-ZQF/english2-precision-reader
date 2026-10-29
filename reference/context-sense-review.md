# 单词语境义校正（2026-10-29）

`public/english/js/context-senses.js` 维护独立编写的简明中文义项、同义表达及原文搭配规则。输入为当前单词的原形、词性、依存关系、在句中的确切位置、原句和当前整句译文；不向外部接口发送文章或用户数据。

优先次序为用户自己的校正、特定文章的校正、定位到该词的明确搭配规则、本句语法作用、词性一致且能由当前译文唯一支持的义项、其余参考义。规则中的捕获范围限定目标词的位置，例如同一句中的 `covering the whole country` 和 `cover all our meat and dairy needs` 分别表示覆盖与满足需求。匹配多个义项时不会仅凭更长的中文子串强行确认。未核对的自动候选继续明确标注，不将本次修改称为全部文章逐词人工校勘。

本轮重点核查了 `address` 的讲话／处理问题、`draw` 的获取收入／吸收水分／绘图、`cover` 的报道／保障／满足需求／走完路程、`account for` 的比例／原因／考虑因素，以及 `state`、`note`、`express`、`subject`、`charge` 等词在真题中的实际用法，并补充多义词的常用义和情态助动词的解释。其他义项与整句译文的对应由程序筛选，界面标为“结合本句译文匹配”。词典定义只用于查证义项，中文表达为本项目自行编写，未复制网站词条正文或例句。

已阅读的原始词典页面（查阅日 2026-10-29）：[Cambridge address](https://dictionary.cambridge.org/dictionary/english/address)、[Cambridge charge](https://dictionary.cambridge.org/dictionary/english/charge)、[Cambridge practice](https://dictionary.cambridge.org/dictionary/english/practice)、[Cambridge firm](https://dictionary.cambridge.org/dictionary/english/firm)。查询通过 Agent Reach 的通用网页阅读路由完成；这些页面分别确认不同动词用法、费用／指控／负责、实践／惯例／练习以及公司／坚定等义项。

`scripts/build_precision_browser.py` 从现有精翻 JSON 编译各年份的经典脚本副本，位置为 `public/english/data/precision-browser/`；只在直接打开本地文件或 JSON 加载失败时按当前年份读取。它保留原有的分句、词性、依存关系和句译，使查词不会在 file:// 模式下退化为按拼写查询词典的首义。生成过程不读取收藏、笔记或复习进度。在线版仍优先使用原 JSON。
