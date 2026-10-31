# 2016—2019 阅读原文核对记录

核对日期为 2026-10-31。逐篇读取了这四年 Text 1—4 的完整英文、逐句候选译文与对应的 meaning-review 上下文词义，并对照本地原卷提取文本和四张正文渲染页；每年四篇对应 PDF 物理页 4、6、8、10（卷面页码 3、5、7、9）。未修改英文、段落、句子编号或原文 textSHA256。各篇 JSON 的 source.evidence 记录了原卷文件名、物理页码和 SHA256，四个 PDF 的文件哈希也已独立重新计算确认。

2016 年原卷为 `2016年考研英语二真题.pdf`，SHA256 为 `ba222df975d03a7f5c681c646673e3379de0dda7b89b7fe913b184132d545acf`。提取层将 Seehorn、midwestern、environmentalists、modern、communication、instrumentally 等识成形似字，并漏掉加下划线的 coax；对照原卷渲染可确认现有英文完整正确。Text 1 的 packed to the brim 指课堂人数爆满，不是课程内容密集；Text 2 保留 threatened 与 endangered 的保护等级区别；Text 3 的 No mind-set could be worse 表示所述效率心态最不利于沉浸阅读；Text 4 的双亲 outside the home 指双方外出工作，sixties 指六十多岁。

2017 年原卷为 `2017年考研英语二真题.pdf`，SHA256 为 `ad82f30feaf16b8066430d656ca4c1ab7e67ab448b93d333880b28e94c829362`。前三篇提取与现有英文一致，Text 4 的 greenhouse 在提取层漏字，已用原卷渲染确认。Text 1 中第三段开头原卷自身确实印作 Parkun，保留原文未擅自改为 Parkrun。Text 2 的 very white 表示所述观念的白人社会文化色彩，不是“白人至上”；Text 3 的 gap year 主要指大学入学前暂缓一年，不是已入大学后休学；Text 4 的 equation 指影响火灾问题的综合因素，并非数学方程。

2018 年原卷为 `2018年考研英语二真题.pdf`，SHA256 为 `1ef8f8d43a882358d66377033a824fe5c64ee474ff3b7756c824df710140e62f`。四篇全文及原卷渲染均已读取，Text 3 的 13.5bn 中数字 5 在提取层被识成 s；当前英文金额正确。四篇均已完成逐句内容，并另行复核词性、分块对应和比较语义。

2019 年原卷为 `2019年考研英语二真题.pdf`，SHA256 为 `817934cbd6801be0ddfa2d58de6e452655ed4cb2e4c01d0e8d05c6d0fc0b4dcd`。Vaish、turn、corn、environment 在提取层分别出现形似字，均已凭原卷渲染核清，没有缺句。Text 1 的 turn on 是“取决于”，deprivation 指另一名孩子未得到巧克力的匮乏处境；Text 2 保留短期降低碳承载能力以改善长期碳汇的反常逻辑及具体年度目标；Text 3 的 more than doubled 译为增加一倍多，并区分签证申请量与签发量，raisin growers 指种植制干葡萄的生产者；Text 4 区分消费者个人举措与公民问责，保留作者对制度结构改革与个人参与并行的主张。

2016、2017、2019 的十二篇共 238 句均已逐句写入分块、真实语序说明、整句译文及位置绑定词语，并在全部完成后再次扫描所有词条和较长分块，纠正了 sharing 的生硬中文、systemic change 的词组释义、struck 的语境义、otherwise 的条件指代等。通过模块 validate 核验原文与哈希、句子边界、分块连续覆盖、词条边界。最终随全量阅读资料统一编译发布。
