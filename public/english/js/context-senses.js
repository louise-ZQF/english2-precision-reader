/* Context glosses: independently written learner senses and occurrence-scoped rules.
 * Chinese cue matching selects among senses of THIS lemma and POS; it never
 * extracts an arbitrary phrase from the sentence translation as a definition.
 */
(function () {
    'use strict';
    const normalize = value => String(value || '').replace(/[‘’]/g, "'").replace(/[‐‑–—]/g, '-').replace(/\s+/g, ' ').trim().toLowerCase();
    const words = {};
    // lemma | part of speech | concise meaning | equivalent Chinese expressions
    const rows = `
address|v|处理；应对；设法解决|处理/应对/解决
address|v|向……讲话；对……发表演说|讲话/发表演说/致辞/演讲
address|n|地址|地址
account|n|账户；账号|账户/账号/帐户
account|n|叙述；描述|叙述/描述/记述
account|v|解释；说明原因|解释/说明原因
account|v|占……比例|占比/占到/占据/占了
account|v|考虑到；把……计入|考虑/计入
practice|n|做法；惯例|做法/惯例/习惯做法
practice|n|实践；实际应用|实践/实际应用/实施
practice|n|练习；训练|练习/训练
practice|v|练习；训练|练习/训练
practice|v|实行；践行|实行/践行/从事
firm|n|公司；企业；事务所|公司/企业/事务所
firm|a|坚定的；牢固的|坚定/牢固/坚实
plant|n|植物|植物/植被
plant|n|工厂；生产设施|工厂/电厂/厂房
plant|v|种植；栽种|种植/栽种/植树
charge|n|费用；收费|费用/收费/免费
charge|n|指控；罪名|指控/罪名/起诉
charge|n|负责；掌管|负责/掌管/掌权
charge|v|收费；索价|收费/收取/要价
charge|v|指控；控告|指控/控告/起诉
charge|v|充电|充电
subject|n|受试者；研究对象|受试者/被试/实验对象/研究对象
subject|n|学科；科目|学科/科目/课程
subject|n|主题；话题|主题/话题/题材
subject|a|受……影响的；受……支配的|受制于/取决于/受影响/支配
subject|v|使遭受；使承受|遭受/承受
issue|n|问题；议题|问题/议题/事项
issue|n|（报刊的）一期|期刊/这一期/本期
issue|v|发布；发出；颁布|发布/发出/颁布/签发
issue|v|产生；导致|产生/导致/最终形成
concern|n|担忧；顾虑|担忧/顾虑/担心/忧虑
concern|n|关注；关切|关注/关切
concern|n|事务；事情|事务/事情
concern|v|涉及；与……有关|涉及/有关/相关
concern|v|使担忧；使担心|担忧/担心/忧虑
term|n|用语；术语；措辞|术语/词语/用语/词汇/措辞
term|n|时期；期限|时期/期限/长期/短期/长远
term|n|条件；条款|条件/条款/协议
term|n|学期|学期
term|n|任期；（法庭的）开庭期|任期/开庭期/庭期
figure|n|数字；数据|数字/数据/数值
figure|n|人物|人物/专家/名人
figure|n|图形；形象|图形/形象/身影
figure|v|弄清；想出|弄清/想出/理清/理解
figure|v|认为；估计|认为/估计/计算
case|n|情况；情形|情况/情形/场合
case|n|案件；诉讼案|案件/此案/诉讼/判例
case|n|病例|病例
case|n|论据；理由|论据/论点/理由
case|n|实例；事例|实例/事例/案例
cover|v|覆盖；遮盖|覆盖/遮盖/遮住
cover|v|报道|报道
cover|v|涵盖；涉及|涵盖/涉及/包含
cover|v|足以支付；承担（费用）|支付/负担/承担费用
cover|v|满足（需求）；提供保障|满足/保障/保险
cover|v|走完（一段路程）|走完/行驶/行程
draw|v|画；绘制|绘制/画出/画图
draw|v|吸引|吸引
draw|v|获取；吸取；提取|获取/吸取/取得/获得/吸收/提取
draw|v|得出（结论）|得出/作出结论
draw|v|拉；拖|拉动/拖动/拉开
drive|v|驾驶；开车|驾驶/开车
drive|v|推动；促使|推动/促使/促进/带动
drive|v|迫使；逼迫|迫使/逼迫
drive|n|动力；强烈愿望|动力/驱动力/愿望/冲动
drive|n|硬盘；驱动器|硬盘/驱动器
reflect|v|反映；体现|反映/体现/折射
reflect|v|认真思考；反思|反思/思考/反省
reflect|v|反射|反射
observe|v|观察；注意到|观察/注意到/发现
observe|v|说；指出；评论|指出/表示/评论/提到
observe|v|遵守|遵守
observe|v|庆祝；纪念|庆祝/纪念
deliver|v|送达；递送|送达/递送/送货/配送
deliver|v|带来；实现；产生|带来/实现/产生/提供
deliver|v|发表（讲话）；作（报告）|发表/演讲/讲话
deliver|v|传递；输送|传递/输送/传输
allow|v|允许；准许|允许/准许/许可
allow|v|使能够；让……得以|使得/能够/使我们/使人们/让人们/以便
claim|v|声称；宣称|声称/宣称/自称/主张
claim|v|索取；申领|索取/申领/领取/认领
claim|n|说法；主张；声称|说法/主张/声称/声明
claim|n|索赔；索取权|索赔/索取权
rest|n|其余；剩余部分|其余/其他/剩余
rest|n|休息|休息
rest|v|休息|休息
rest|v|依靠；取决于|依靠/依赖/取决于
sound|n|声音；声响|声音/声响/发音
sound|v|听起来；给人以……印象|听起来/显得
sound|v|发出声音|发出声音/鸣响
sound|a|合理的；可靠的|合理/可靠/健全
sense|n|感觉；意识|感觉/感到/意识/成就感/责任感/参与感
sense|n|理解；认识|理解/认识/了解
sense|n|意义；意思|意义/意思
sense|v|感觉到；察觉到|察觉/感觉到/感知
cause|n|原因；起因|原因/起因/根源
cause|n|事业；共同目标|事业/共同目标
cause|v|导致；造成；引起|导致/造成/引起/使得
course|n|课程|课程
course|n|过程；进程；轨迹|过程/进程/轨迹
course|n|路线；方向|路线/方向/正轨
course|n|（一餐中的）一道菜|道菜
state|n|州|各州/州级/该州/州政府/州法律/州考试/个州/一些州
state|n|国家；政府|国家/政府
state|n|状态；状况|状态/状况/处境
state|v|陈述；说明；规定|陈述/说明/规定/表示/宣布
line|n|界限；分界|界限/分界/代际
line|n|路线；线路；轨道|线路/路线/轨道
line|n|系列；产品线|系列/产品线
line|n|线；线条|线条/曲线/趋势线
line|n|（等候的）队伍|排队/队伍
line|n|终点线|终点线
note|v|指出；提到；注意到|指出/提到/注意到/表示/告诫
note|v|记录；记下|记录/记下
note|n|笔记；记录|笔记/记录/便条
object|n|物体；东西|物体/物品/东西
object|n|对象；目标|对象/目标
object|v|反对|反对
current|a|目前的；现有的|目前/当前/现有/现在
current|n|水流；气流；电流|水流/气流/电流
express|v|表达；表示|表达/表示/体现
express|a|明确的；明示的|明确/明示
affect|v|影响|影响
effect|n|影响；效果|影响/效果
effect|n|效应|效应
effect|v|实现；使发生|实现/使发生/带来
engage|v|参与；从事|参与/从事/投入
engage|v|使参与；吸引|吸引/使参与/调动
engage|v|与……互动；接触|互动/交流/接触
assume|v|以为；假定；认为|以为/假定/假设/认为/前提
assume|v|承担（责任）；担任|承担/担任
assume|v|呈现（某种形态）；采取|呈现/组成/采取
appreciate|v|理解；认识到|理解/认识到/领会/意识到
appreciate|v|欣赏；重视|欣赏/重视
appreciate|v|感激；感谢|感激/感谢
appreciate|v|升值|升值
critical|a|关键的；至关重要的|关键/至关重要
critical|a|批判的；批评的|批判/批评
critical|a|危急的；严重的|危急/病危/危重
objective|n|目标|目标/目的
objective|a|客观的|客观
interest|n|兴趣|兴趣
interest|n|利益|利益
interest|n|利息|利息
interest|v|使感兴趣|使感兴趣/引起兴趣
value|n|价值|价值
value|n|价值观|价值观
value|v|重视；珍视|重视/珍视/看重
value|v|给……估价|估价/估值
right|n|权利|权利/权益
right|n|右边；右方|右边/右方
right|a|正确的；合适的|正确/合适/恰当
right|adv|正好；恰好|正好/恰好
capital|n|资本；资金|资本/资金
capital|n|首都；首府|首都/首府
capital|a|大写的|大写
company|n|公司；企业|公司/企业
company|n|陪伴；相伴|陪伴/相伴/为伴
business|n|企业；商业；生意|企业/商业/生意/商家
business|n|事情；事务|事情/事务/公务
mean|v|意味着；意思是|意味着/意思/表示
mean|v|打算；意在|打算/旨在/意在
mean|n|平均值|平均值
means|n|方式；手段|方式/手段/方法
poor|a|贫穷的|贫穷/贫困/穷人
poor|a|差的；不足的|较差/糟糕/低劣/不足/不佳
sentence|n|句子|句子/语句
sentence|n|判决；刑罚|判决/刑罚/刑期
sentence|v|判刑|判刑
work|n|工作|工作/劳动
work|n|作品；著作|作品/著作/艺术品
work|v|工作；劳动|工作/劳动
work|v|起作用；奏效；有效|起作用/奏效/有效/管用
work|v|运转；运行|运转/运行
follow|v|跟随；沿着|跟随/沿着/跟上
follow|v|遵循；遵守|遵循/遵守/按照
follow|v|理解；听懂|理解/听懂
follow|v|接着发生；随后到来|随后/接着/紧接
following|a|下列的；接下来的|下列/以下/接下来
sheet|n|纸张；表单|纸/表单/答题卡/答题纸
sheet|n|床单|床单
point|n|观点；要点|观点/要点/论点
point|n|分数；点数|分数/得分/百分点
point|n|时刻；阶段；位置|时刻/阶段/位置
point|v|指出|指出
character|n|性格；品格|性格/品格/品性
character|n|人物；角色|人物/角色
character|n|特点；特征|特点/特征
character|n|文字；字符|文字/字符/汉字
letter|n|信；信件|信件/写信/来信/一封信
letter|n|字母|字母
letter|n|字面含义；条文|条文/字面
faculty|n|教职员工；全体教师|教师/教职员工
faculty|n|能力；机能|能力/机能/官能
fine|a|好的；令人满意的|良好/很好/满意/精美
fine|a|细微的；精细的|细微/精细/细小
fine|n|罚款|罚款
fine|v|处以罚款|罚款
scale|n|规模；程度|规模/程度
scale|n|体重秤；秤|体重秤/秤上/称重
scale|n|量表；等级|量表/等级/评分
scale|v|扩大规模|扩大/扩展/规模化
fashion|n|时尚；流行风尚|时尚/流行/风尚
fashion|n|方式；办法|方式/办法
order|n|订单|订单/订购
order|n|顺序；秩序|顺序/秩序/次序
order|n|命令；指令|命令/指令/法令
order|v|命令；要求|命令/要求
order|v|订购；点（餐）|订购/点餐/点菜
power|n|权力；控制力|权力/控制力/掌权
power|n|能力；力量|能力/力量/购买力
power|n|电力；能源|电力/能源/发电
power|v|为……提供动力；供电|供电/提供动力/驱动
yield|v|产生；带来|产生/带来/收获
yield|v|屈服；让步|屈服/让步
yield|n|产量；收益|产量/收益/回报
check|v|核查；检查|核查/检查/查看
check|v|抑制；遏制|抑制/遏制/制止
check|n|支票|支票
check|n|检查；核查|检查/核查
sentence|n|句子|语句
spring|n|春天；春季|春天/春季
spring|n|泉；泉水|泉水/温泉
spring|v|突然出现；涌现|涌现/突然出现
measure|n|措施；办法|措施/办法/举措
measure|n|尺度；衡量标准|尺度/衡量标准/指标
measure|v|测量；衡量|测量/衡量/测定
minute|n|分钟|分钟
minute|a|微小的；细微的|微小/细微
novel|n|小说|小说
novel|a|新颖的；新奇的|新颖/新奇/新型
fine|adv|很好；令人满意地|很好/不错
block|v|阻止；阻碍|阻止/阻碍/封锁
block|n|街区|街区
block|n|障碍；阻碍|障碍/阻碍
board|n|董事会；委员会|董事会/委员会
board|n|木板；板|木板/板上
board|v|登上（交通工具）|登上/上车/登机
present|v|呈现；展示；提出|呈现/展示/提出/提供
present|a|在场的；出席的|在场/出席
present|a|目前的；现有的|目前/现有/当前
present|n|礼物|礼物/礼品
present|n|现在；当前|现在/当前
content|n|内容|内容
content|a|满意的；满足的|满意/满足
minute|n|分钟|分钟
bill|n|法案|法案/立法
bill|n|账单；费用|账单/费用/支出
bill|n|纸币|纸币/钞票
stock|n|股票|股票/股市/股价
stock|n|存量；库存；储备|存量/库存/储备
stock|v|储备；备货|储备/备货
market|n|市场|市场
market|v|营销；推销|营销/推销
sentence|v|判刑|判处
rate|n|比率；率|比率/比例/利率/增长率/离婚率
rate|n|价格；费用|价格/费用/收费
rate|v|评价；评定|评价/评定/评为/评分
return|v|返回；回到|返回/回到
return|v|归还|归还
return|n|回报；收益|回报/收益
fine|a|晴朗的|晴朗
admit|v|承认|承认
admit|v|准许进入；录取；收治|录取/收治/入院/准许进入
admission|n|大学录取；入学|录取/入学/招生
admission|n|承认|承认
admission|n|入场；入场费|入场/门票
support|v|支持；赞同|支持/赞同
support|v|供养；维持生活|供养/养活/维持生活
support|n|支持；帮助|支持/帮助
maintain|v|维持；保持|维持/保持
maintain|v|坚持认为；主张|认为/主张/坚称
maintain|v|维护；保养|维护/保养/维修
hold|v|持有；握住|持有/握住/拿着
hold|v|举行；举办|举行/举办
hold|v|保持；维持|保持/维持/持续
hold|v|认为；相信|认为/相信
hold|v|容纳；装得下|容纳/装得下
strike|v|打击；击中|打击/击中
strike|v|使突然想到；给……印象|突然想到/印象/引人
strike|v|达成；取得|达成/取得
strike|n|罢工|罢工
match|n|比赛|比赛
match|n|匹配；相配的人或物|匹配/相配
match|v|匹配；相符合|匹配/符合/相配
match|v|比得上；与……相当|比得上/相当/媲美
lean|a|艰难的；不景气的|艰难/不景气/萧条
lean|a|精简的；精益的|精简/精益
lean|v|倾斜；倚靠|倾斜/倚靠/靠在
fuel|n|燃料|燃料
fuel|v|加剧；助长；推动|加剧/助长/推动/促进
shed|v|减少；摆脱；裁减|减少/摆脱/裁员/裁减
shed|v|流出；脱落|流出/脱落/脱下
capacity|n|能力；承受能力|能力/承受/精力
capacity|n|容量；产能；运力|容量/产能/运力
capacity|n|身份；职位|身份/职位
vision|n|愿景；远见|愿景/远见/设想
vision|n|视力；视觉|视力/视觉
mission|n|使命；任务|使命/任务
passion|n|热情；热爱|热情/热爱/激情
fulfillment|n|自我实现带来的满足感；成就感|满足感/成就感/自我实现
fulfillment|n|履行；实现|履行/完成
bandwidth|n|时间和精力的余量|时间余量/精力/时间和精力
bandwidth|n|带宽|带宽
boundary|n|界限；分界|界限/分界/边界
gain|v|获得；取得|获得/取得/得到
gain|v|增加；增长|增加/增长/增重
gain|n|收益；好处；进步|收益/好处/进步/成果
condition|n|条件；环境|条件/环境
condition|n|状况；状态|状况/状态
condition|n|疾病；健康问题|疾病/病情/患有
discipline|n|学科；专业领域|学科/专业/领域
discipline|n|纪律；自律|纪律/自律
discipline|v|训练；约束|训练/约束
facility|n|设施；场所|设施/场所/设备
facility|n|能力；熟练|能力/熟练
traffic|n|交通；车流|交通/车流
traffic|n|人流；访问量|人流/访问量/客流
traffic|v|非法交易；贩运|贩运/非法交易
tip|n|小费|小费
tip|n|建议；窍门|建议/窍门/贴士
tip|n|顶端；尖端|顶端/尖端
tip|v|给小费|小费
tip|v|倾斜；倾倒|倾斜/倾倒
book|n|书；著作|书/著作
book|v|预订|预订/预约
bank|n|银行|银行
bank|n|河岸|河岸/岸边
court|n|法院；法庭|法院/法庭
court|n|球场|球场
court|v|设法获得；争取|争取/招徕
fine|n|罚金；罚款|罚金
feature|n|特征；特点|特征/特点/特色/功能
feature|n|五官；面部特征|五官/面部特征
feature|v|以……为特色；包含|特色/包含/展示
article|n|文章|文章
article|n|物品；物件|物品/物件
article|n|条款|条款
authority|n|当局；主管部门|当局/政府部门/主管部门
authority|n|权威；权力|权威/权力/权限
authority|n|专家|专家/权威人士
argue|v|认为；论证；主张|认为/论证/主张/指出
argue|v|争论；争吵|争论/争吵/辩论
argument|n|论点；理由|论点/理由/论据
argument|n|争论；争吵|争论/争吵/讨论
suggest|v|建议；提议|建议/提议
suggest|v|表明；暗示|表明/暗示/显示
suggestion|n|建议|建议/提议
suggestion|n|迹象；暗示|迹象/暗示
concerned|a|担心的；忧虑的|担心/担忧/忧虑
concerned|a|有关的；相关的|有关/相关
involve|v|涉及；包含|涉及/包含
involve|v|使参与；让……加入|参与/加入
charge|n|电荷；电量|电荷/电量
interest|n|利益；权益|权益
figure|n|身材；体形|身材/体形
profile|n|简介；概况|简介/概况/资料
profile|n|知名度；公众形象|知名度/公众形象/曝光度
profile|v|介绍；描绘|介绍/描绘
prospect|n|前景；可能性|前景/可能性
prospect|n|有希望的人；潜在客户|潜在客户/有希望
secure|a|安全的；有保障的|安全/保障/稳定
secure|v|获得；确保|获得/确保/取得
contract|n|合同；契约|合同/契约
contract|v|收缩；缩小|收缩/缩小
contract|v|感染；患上|感染/患上
constitution|n|宪法|宪法
constitution|n|体质；构成|体质/构成
major|a|主要的；重大的|主要/重大
major|n|大学主修专业|主修/专业
major|v|主修|主修
minor|a|次要的；较小的|次要/较小/轻微
minor|n|未成年人|未成年
average|n|平均数；平均水平|平均
average|a|平均的|平均
average|a|普通的；一般的|普通/一般/平常
general|a|总体的；一般的|总体/一般/普遍
general|n|将军|将军
individual|n|个人；个体|个人/个体
individual|a|个人的；单独的|个人/单独/各自
likely|a|可能的|可能
likely|adv|很可能|可能
novelty|n|新奇；新鲜感|新奇/新鲜感
revenue|n|收入；营收|收入/营收/税收
regular|a|定期的；有规律的|定期/规律
regular|a|普通的；常规的|普通/常规
regular|a|经常的；频繁的|经常/频繁
form|n|形式；类型|形式/类型
form|n|表格|表格/表单
form|v|形成；组成|形成/组成
fine|a|精细的|精致
head|v|前往；朝……行进|前往/驶向/走向
head|v|领导；主持|领导/主持
head|n|头；头部|头部/脑袋/转头
head|n|负责人；首脑|负责人/首脑/校长
sentence|n|句子|句子
company|n|公司；企业|企业
force|n|力量；力|力量/作用力
force|n|部队；军队|部队/军队
force|v|迫使；强迫|迫使/强迫
ground|n|地面；土地|地面/土地/地上
ground|n|理由；根据|理由/根据/依据
ground|v|使建立在……基础上|建立/奠定/基于
spring|n|弹簧|弹簧
leave|v|离开|离开/离职
leave|v|留下；使处于|留下/使得/使我们/让人
leave|n|休假；假期|休假/假期
tax|n|税；税款|税收/税款/纳税
tax|v|征税|征税/课税
tax|v|使负担沉重；使费尽|负担/费尽/耗费
issue|n|问题；议题|问题
sound|a|稳健的|稳健
powerful|a|强大的；有影响力的|强大/影响力/有权力
fair|a|公平的；公正的|公平/公正
fair|a|相当好的；尚可的|尚可/相当好
fair|n|展览会；交易会|展览会/交易会/招聘会
affair|n|事情；事务|事情/事务/事件
affair|n|婚外情|婚外情/外遇
attention|n|注意；关注|注意/关注
physical|a|身体的；体力的|身体/体力/生理
physical|a|物理的；实体的|物理/实体
mental|a|心理的；精神的|心理/精神
mental|a|脑力的；思维的|脑力/思维
labour|n|劳动；劳动力|劳动/劳动力
labor|n|劳动；劳动力|劳动/劳动力
labour|n|工党|工党
labor|n|工党|工党
school|n|学校；学院|学校/学院/校园
school|n|学派；流派|学派/流派
author|n|作者|作者/笔者
people|n|人；人们|人们/人群/人类
people|n|民族；人民|民族/人民
child|n|孩子；儿童|孩子/儿童/子女
food|n|食物；食品|食物/食品/饮食
year|n|年；年份|年份/每年/去年/今年
time|n|时间|时间/时候/时刻
time|n|次；回|次数/一次/多次
time|n|时代；时期|时代/时期/岁月
take|v|拿；取|拿/取走
take|v|花费；需要|花费/需要/耗时
take|v|采取；接受|采取/接受
make|v|制造；制作|制造/制作/生产
make|v|使；让|使得/让人/使人/导致
give|v|给予；提供|给予/提供/给出
get|v|获得；得到|获得/得到
get|v|变得；成为|变得/成为
get|v|理解；明白|理解/明白
set|v|设定；制定；确立|设定/制定/确立/设置
set|v|放置；摆放|放置/摆放
set|n|一组；一套|一组/一套/系列
put|v|放置；使处于|放置/置于/使处于
put|v|表达；表述|表达/表述/说法
see|v|看见；看到|看见/看到
see|v|理解；认为|理解/认为/视为
see|v|经历；见证|经历/见证/出现
find|v|发现；找到|发现/找到
find|v|认为；觉得|认为/觉得
run|v|跑；奔跑|跑步/奔跑
run|v|经营；管理；运营|经营/管理/运营
run|v|运行；运转|运行/运转
run|n|跑步；一段路程|跑步/路程
turn|v|转变；变成|转变/变成/转向
turn|v|转动；转身|转动/转身/转头
turn|n|轮流的机会|轮流/轮到
raise|v|提高；增加|提高/增加/上涨
raise|v|提出（问题）|提出/引起
raise|v|筹集；募得|筹集/募集
raise|v|抚养；养育|抚养/养育
read|v|阅读；读|阅读/读书
read|v|解读；理解|解读/理解
say|v|说；表示|表示/说道/声称
write|v|写；撰写|撰写/写下/写信
talk|v|谈论；交谈|谈论/交谈/讨论
talk|n|谈话；讨论|谈话/讨论
thought|n|想法；思想|想法/思想/思考
way|n|方式；方法|方式/方法/办法
way|n|道路；方向|道路/方向/路程
word|n|词；单词；措辞|词汇/单词/词语/措辞
word|n|消息；话语|消息/话语/诺言
text|n|文章；文本|文章/文本/正文
text|n|短信|短信
home|n|家；家庭|家庭/家中/家里/住房
home|adv|在家；回家|在家/回家
great|a|很大的；重大的|重大/很大/巨大
great|a|出色的；很好的|出色/很好/优秀
good|a|好的；有益的|良好/有益/优秀/健康
good|n|好处；公益|好处/公益/公共利益
high|a|高的|高昂/较高/高度
low|a|低的|较低/低廉/低下
long|a|长的；长时间的|长时间/漫长/长期
long|adv|长时间地；很久|很久/长时间
long|v|渴望|渴望
last|a|最后的；上一次的|最后/上次/去年
last|v|持续|持续
meanwhile|adv|与此同时|同时/与此同时
still|adv|仍然；依然|仍然/依然/还是
still|a|静止的；不动的|静止/不动
just|adv|仅仅；只是|仅仅/只是/才
just|adv|恰好；正好|恰好/正好/刚刚
just|a|公正的|公正/正义
even|adv|甚至；即使|甚至/即使
even|a|平稳的；均匀的|平稳/均匀
quite|adv|相当；很|相当/十分/非常
only|adv|仅仅；只|仅仅/只有/只要
only|a|唯一的|唯一
most|adv|最；非常|最为/最重要/非常
most|a|大多数的；最多的|大多数/多数/最多
more|adv|更；更加|更加/更为
more|a|更多的|更多
less|adv|较少地；程度较低地|不那么/较少/更少
less|a|较少的|较少/更少
much|adv|很；更加|更加/得多/很多
much|a|许多的；大量的|许多/大量/很多
well|adv|很好地；有效地|很好/良好/有效
well|a|健康的；身体好的|健康/身体好
well|n|井|水井/油井
free|a|免费的|免费
free|a|自由的；不受限制的|自由/不受限制
free|a|空闲的|空闲/闲暇
free|v|使摆脱；释放|摆脱/释放/解放
short|a|短的；短期的|短期/短暂/较短
short|a|不足的；短缺的|不足/短缺
dear|a|亲爱的|亲爱
false|a|错误的；虚假的|错误/虚假/不实
true|a|真实的；正确的|真实/正确/属实
public|a|公共的；公众的|公共/公众/公开
public|n|公众；大众|公众/大众
private|a|私人的；私下的|私人/私下/私有
private|a|私营的；民营的|私营/民营
sound|n|声音；声响|声音
common|a|共同的|共同
common|a|常见的；普遍的|常见/普遍/普通
share|n|份额；比例|份额/比例/部分
share|n|股票；股份|股票/股份
share|v|分享；共享|分享/共享
share|v|具有同样的；共同承担|同样/共同/分担
change|n|变化；改变|变化/改变
change|n|零钱|零钱
change|v|改变；变化|改变/变化/更换
cost|n|费用；成本；代价|费用/成本/代价
cost|v|花费；付出代价|花费/代价/损失
paper|n|论文；文章|论文/文章
paper|n|报纸|报纸
paper|n|试卷；纸张|试卷/纸张/纸质
act|v|行动；做事|行动/做事/表现
act|n|法案；法令|法案/法令
act|n|行为；举动|行为/举动
move|n|举措；行动|举措/行动/措施
move|n|搬家；迁移|搬家/迁移/迁居
move|v|移动；搬迁|移动/搬迁/搬家
move|v|促使；使感动|促使/感动
conduct|v|开展；进行；实施|开展/进行/实施/组织
conduct|v|指挥；引导|指挥/引导
conduct|n|行为；举止|行为/举止/品行
promote|v|促进；推动|促进/推动/增进
promote|v|推销；宣传|推销/宣传/推广
promote|v|晋升；提拔|晋升/提拔
exercise|n|锻炼；运动|锻炼/运动
exercise|n|练习；作业|练习/作业
exercise|v|行使；运用|行使/运用
exercise|v|锻炼；运动|锻炼/运动
approach|n|方法；方式|方法/方式/策略
approach|n|接近；临近|接近/临近/到来
approach|v|接近；靠近|接近/靠近/临近
approach|v|着手处理；探讨|着手/处理/探讨/看待
treat|v|对待；看待|对待/看待/视为
treat|v|治疗；医治|治疗/医治/诊治
treat|v|处理；治理|处理/治理/清理
treat|v|款待；犒劳|款待/犒劳/请客
treatment|n|治疗；疗法|治疗/疗法
treatment|n|待遇；对待方式|待遇/对待
treatment|n|处理；处置|处理/处置
subject|n|主题；话题|主题
fit|v|适合；符合|适合/符合/匹配
fit|v|安装；装配|安装/装配
fit|a|健康的；身体好的|健康/健壮
suit|n|诉讼；官司|诉讼/官司
suit|n|西装；套装|西装/套装
suit|v|适合；满足需要|适合/合适/满足需要
consent|n|同意；许可|同意/许可
consent|v|同意；允许|同意/允许
lead|v|引领；带领|引领/带领/领先
lead|v|导致；通向|导致/通向/引起
lead|n|领先地位；带头作用|领先/带头
lead|n|线索|线索
field|n|领域；学科|领域/学科/行业
field|n|田地；旷野|田地/田野/旷野
field|n|场地；赛场|场地/赛场
model|n|模型；模式|模型/模式
model|n|榜样；典范|榜样/典范
model|n|型号；款式|型号/款式
model|v|模拟；建模|模拟/建模
model|v|模仿；仿效|模仿/仿效
coach|n|教练；指导者|教练/指导者
coach|n|长途客车|长途客车/大巴
coach|v|指导；训练|指导/训练
policy|n|政策；方针；规定|政策/方针/规定
policy|n|保险单；保单|保单/保险单
compound|v|使加重；使恶化|加重/加剧/恶化
compound|n|化合物|化合物
compound|a|复合的|复合
fashion|v|制作；塑造|制作/塑造
balance|n|平衡|平衡
balance|n|余额|余额
balance|v|平衡；兼顾|平衡/兼顾
spot|n|地点；场所|地点/场所/位置
spot|n|斑点；污点|斑点/污点
spot|v|发现；认出|发现/认出
fairly|adv|相当；颇为|相当/颇为
fairly|adv|公平地；公正地|公平/公正
novelty|n|新奇；新鲜感|新奇/新鲜感
responsibility|n|责任；职责|责任/职责
responsible|a|负有责任的；负责的|责任/负责
responsible|a|造成……的；是……的原因|造成/导致/原因
life|n|生命；一生；生活|生命/一生/生活
serve|v|服务；为……效力|服务/效力
serve|v|担任；起……作用|担任/起到/充当/作用
serve|v|供应（食物）；端上|供应/端上
serve|v|服（刑）|服刑/刑期
figure|n|图表|图表
`.trim().split('\n');
    for (const row of rows) {
        const [lemma, p, m, cues] = row.split('|');
        const entry = words[lemma] || (words[lemma] = []);
        const previous = entry.find(item => item.p === p && item.m === m);
        if (previous) previous.cues.push(...cues.split('/'));
        else entry.push({ p, m, cues: cues.split('/') });
    }
    const rules = [];
    const add = (lemma, p, pattern, meaning) => rules.push({ lemma, p, re: new RegExp(pattern, 'ig'), meaning });
    const ruleRows = [
        ['address', '', '(address(?:ed|es|ing)?)\\s+(?:a\\s+small\\s+)?(?:gathering|audience|meeting|crowd)', '向……讲话；对……发表演说'],
        ['address', '', '(address(?:ed|es|ing)?)\\s+(?:(?:these|the|our|an?|urgent|truly|thorny|none of)\\s+){0,6}(?:problems?|issues?|questions?|needs?|difficulty|difficulties|imbalances?|ambiguity|gap)', '处理；应对；设法解决'],
        ['address', '', '(?:problem|gap|issue|need|difficulty)\\b[^.!?;]{0,55}\\b(addressed)', '处理；解决（所述问题）'],
        ['account', '', '(account(?:s|ed|ing)?\\s+for)\\s+(?:(?:more|less|about|nearly|approximately|two|one|a|significant|than)\\b|\\d)', '占……比例'],
        ['account', '', '(account(?:s|ed|ing)?\\s+for)\\s+(?:human factors|these things|such factors)', '考虑到；把……纳入考虑'],
        ['account', '', '(?:take|takes|taking|taken|took)\\b[^.!?;]{0,60}\\binto\\s+(account)', '考虑；计入（take … into account 的一部分）'],
        ['account', '', 'on\\s+(account)\\s+of', '由于；因为（on account of 的一部分）'],
        ['account', '', '(?:hold|holds|holding)\\b[^.!?;]{0,60}\\bto\\s+(account)', '追究责任；要求负责（hold … to account 的一部分）'],
        ['account', 'n', '(?:bank|Twitter|social media|savings)\\s+(accounts?)', '账户；账号'],
        ['practice', '', 'put\\s+into\\s+(practice)', '实践；实施'],
        ['practice', 'n', '(practice)\\s+of\\s+(?:selecting|tips|tipping)', '做法；惯例'],
        ['firm', '', '(?:law|research|consulting|accounting)\\s+(firms?)', '公司；事务所'],
        ['plant', '', '(?:transformer|manufacturing|power|industrial|car)\\s+(plants?)', '工厂；生产设施'],
        ['plant', '', '(plant(?:s|ed|ing)?)\\s+(?:the\\s+right\\s+|more\\s+|native\\s+)?trees', '种植；栽种'],
        ['charge', '', '(charg(?:e|es|ed|ing))\\s+(?:points?|stations?|batteries|electric vehicles)', '充电'],
        ['charge', '', 'in\\s+(charge)(?:\\s+of)?', '负责；掌管'],
        ['charge', '', '(?:free of|no)\\s+(charge)', '费用；收费（此处表示不收费）'],
        ['subject', '', '(subjects?)\\s+(?:exposed|who discussed|quickly chose)', '受试者；研究对象'],
        ['subject', '', '(?:student|experimental|research)\\s+(subjects?)', '受试者；研究对象'],
        ['subject', '', '(subject)\\s+to\\s+(?:family influence|regulation|change|approval)', '受……影响的；受……约束的'],
        ['issue', '', '(issu(?:e|es|ed|ing))\\s+(?:a |an |heat )?(?:warning|call|visa|statement|order|report)', '发布；发出；签发'],
        ['issue', '', 'visas?\\s+(issued)', '签发（签证）'],
        ['issue', '', '(issu(?:e|es|ed|ing))\\s+in\\s+the\\s+formation', '最终形成；产生'],
        ['concern', '', 'all\\s+(concerned)', '所有相关的人；各有关方面'],
        ['concern', '', '(concern(?:s|ed|ing)?)\\s+(?:the amount|the use|the question)', '涉及；关于'],
        ['term', '', '(terms?)\\s+like', '用语；措辞'],
        ['term', '', '(?:long|longer|short|medium)[- ]+(terms?)', '时期；期限（此处构成长／短期）'],
        ['term', '', 'come\\s+to\\s+(terms)\\s+with', '接受；与……达成谅解（come to terms with 的一部分）'],
        ['term', '', 'in\\s+(terms)\\s+of', '就……而言；从……方面说（in terms of 的一部分）'],
        ['term', '', '(?:Supreme Court|court)\\b[^.!?;]{0,50}\\bnext\\s+(term)', '（法庭的）下一开庭期'],
        ['figure', '', '(figur(?:e|es|ed|ing))\\s+out', '弄清楚；想明白'],
        ['figure', '', '(?:medical|epochal|political|public)\\s+(figures?)', '人物；专家'],
        ['figure', '', '(figures?)\\s+of\\s+speech', '修辞手法（figure of speech 的一部分）'],
        ['case', '', '(?:Myriad|Strauder)\\s+(case)', '案件；诉讼案'],
        ['case', '', '(case)\\b[^.!?;]{0,30}\\b(?:Supreme Court|court)', '案件；诉讼案'],
        ['case', '', '(?:build|built|building|make|makes)\\s+(?:your|their|a|the)\\s+(case)', '论据；支持某一主张的理由'],
        ['case', '', 'on\\s+the\\s+(case)', '正在处理此事（on the case 的一部分）'],
        ['cover', '', '(cover(?:s|ed|ing)?)\\s+the\\s+[^.!?;]{0,25}side of the war', '报道（战争的某一侧面）'],
        ['cover', '', '(cover(?:s|ed|ing)?)\\s+the\\s+\\d+\\s*km', '走完；行驶（一段路程）'],
        ['cover', '', '(cover(?:s|ed|ing)?)\\s+all\\s+our\\s+meat\\s+and\\s+dairy\\s+needs', '满足（全部肉类和乳制品需求）'],
        ['cover', '', '(cover)\\s+themselves\\s+and\\s+their\\s+families', '为自己和家人提供医疗保险保障'],
        ['cover', '', '(cover(?:s|ed|ing)?)\\s+(?:our|their|the)\\s+(?:bodies|faces)', '遮盖；遮住'],
        ['draw', '', '(draw(?:s|n|ing)?|drew)\\s+(?:an?\\s+)?(?:income|salary|support|moisture|life-sustaining)', '获得；获取；吸取'],
        ['draw', '', '(draw(?:s|n|ing)?|drew)\\s+out\\s+life-sustaining', '获得；赚取（维持生活的钱）'],
        ['draw', '', '(draw(?:s|n|ing)?|drew)\\s+(?:a new 21st-century |a new |a |the )?(?:pictures?|road map|map)', '画；绘制'],
        ['draw', '', '(draw(?:s|n|ing)?|drew)\\s+(?:a\\s+)?(?:greater share|further support)', '获取；获得'],
        ['drive', '', '(driv(?:e|es|en|ing)|drove)\\s+up', '推高；使上涨'],
        ['drive', '', '(driv(?:e|es|en|ing)|drove)\\s+down', '压低；使下降'],
        ['drive', '', '(?:hard|external hard)\\s+(drive)', '硬盘；存储设备'],
        ['drive', '', '(driv(?:e|es|en|ing)|drove)\\s+(?:others|workers)\\s+underground', '迫使……转入地下／隐蔽状态'],
        ['drive', '', '(driv(?:e|es|en|ing)|drove)\\s+foot\\s+traffic', '带动；吸引（客流）'],
        ['drive', '', '(driving)\\s+(?:a route|because they)', '驾驶；开车'],
        ['observe', '', '(?:Hacker|he|she|researcher)\\s+(observed|observes)', '指出；评论说'],
        ['deliver', '', '(deliver(?:s|ed|ing)?)\\s+(?:real |some |financial |health |substantial )*(?:benefits|improvements|results)', '带来；产生（好处、改善或结果）'],
        ['deliver', '', '(deliver)\\s+the\\s+same\\s+heat', '输送；传递（热量）'],
        ['deliver', '', '(deliver)\\s+works\\s+of\\s+art', '将（艺术品）带入市场；促成流通'],
        ['rest', '', '(rest)\\s+of', '其余；剩余部分'],
        ['rest', '', '(rest(?:s|ed|ing)?)\\s+on', '依赖；以……为基础'],
        ['sound', 'v', '(sound(?:s|ed|ing)?)\\s+(?:great|strange|overly|like|good|reasonable)', '听起来；显得'],
        ['sense', '', '(?:make|makes|making|made)\\s+(?:absolute |perfect |good )?(sense)', '有道理；说得通（make sense 的一部分）'],
        ['sense', '', '(?:clearer|limited)\\s+(sense)\\s+of', '理解；认识'],
        ['sense', '', '(sense)\\s+of\\s+(?:responsibility|accomplishment|achievement|involvement|control|ownership)', '……感；对……的意识（与后文合译）'],
        ['course', '', 'of\\s+(course)', '当然（of course 的一部分）'],
        ['course', '', 'in\\s+due\\s+(course)', '在适当时候；到时候'],
        ['course', '', '(?:three|four|five)[- ](course)', '（一餐中的）一道菜'],
        ['course', '', 'life\\s+(course)', '人生历程；生活轨迹'],
        ['course', '', 'on\\s+(course)\\s+for', '正确方向；预定进程'],
        ['state', '', '(States)\\s+(?:have begun|consider)', '（美国的）州'],
        ['state', '', '(?:every|each|several|some|four|western|many|most|various)\\s+(states?)', '（美国的）州'],
        ['state', '', '(states?)\\s+(?:laws?|tests?|governments?|juries|privacy|consumer|level)', '州；州一级的（修饰后面的名词）'],
        ['state', '', '(states)\\s+(?:to use|made women|automatically exempted|ought to conform|generally argue)', '（美国的）各州'],
        ['state', '', '(states?)\\s+(?:require|consider|are challenging|have gained)', '（美国的）州'],
        ['state', '', '(states?)\\s*(?:\'s|’s)\\s+(?:electricity|emissions|proposed|privacy)', '该州；州的'],
        ['state', '', '(State)\\s+University', '州立的（大学名称的一部分）'],
        ['state', '', '(state)\\s+that\\s+new\\s+residential', '规定；明确说明'],
        ['state', '', 'secretary\\s+of\\s+(state)', '国务（secretary of state 指国务卿）'],
        ['line', '', '(?:clothing|product)\\s+(line)', '（服装或产品）系列'],
        ['line', '', '(?:finish|finishing)\\s+(line)', '终点线（此处也比喻人生目标）'],
        ['line', '', 'over\\s+the\\s+(line)', '终点线'],
        ['line', '', '(?:generational)\\s+(lines)', '代际界限；不同年龄群体'],
        ['line', '', '(line)\\s+between', '界限；分界'],
        ['line', '', 'same\\s+(line)\\s+at\\s+any', '铁路线路；轨道'],
        ['line', '', 'in\\s+(line)\\s+with', '符合；与……一致（in line with 的一部分）'],
        ['line', '', 'on\\s+(line)', '投入使用；上线（此处指电力设施）'],
        ['note', '', '(?:As|as)\\s+[^.!?;]{1,35}?\\s+(notes)', '指出；提到'],
        ['note', '', '(notes)\\s+(?:Tanya|that)', '指出；提到'],
        ['note', '', '(?:she|he|Eberle|Davidson|Hagel|Norris)\\s+(notes)', '指出；提到'],
        ['note', '', '(?:take|takes|taking|taken)\\s+(note)', '注意到；留意（take note 的一部分）'],
        ['express', '', '(express)\\s+(?:affirmative consent|privacy claims|consent)', '明确的；明示的'],
        ['engage', '', '(engag(?:e|es|ed|ing))\\s+(?:stakeholders|citizens|coworkers|participants)', '使……参与；吸引……加入'],
        ['engage', '', '(engag(?:e|es|ed|ing))\\s+with', '与……互动；接触'],
        ['engage', '', '(engag(?:e|es|ed|ing))\\s+in', '参与；从事'],
        ['engage', '', '(engaged)\\s+citizens', '积极参与（公共事务）的'],
        ['assume', '', '(assume)\\s+an\\s+inverted\\s+V-formation', '采取；形成（倒 V 字形队列）'],
        ['appreciate', '', '(appreciate)\\s+the\\s+economic\\s+realities', '理解；充分认识到'],
        ['critical', '', '(critical)\\s+(?:assessment|thinking|analysis|review)', '批判性的；审慎分析的'],
        ['critical', '', '(critical)\\s+(?:importance|issue|years|role|factor)', '关键的；至关重要的'],
        ['objective', '', '(?:more|truly|fully)\\s+(objective)', '客观的'],
        ['will', 'v', '(will|would|\'ll|\'d)\\s+(?:be|have|see|make|allow|help|change|never|not|also|still|eventually)', '助动词，表示将来、推测或假设；不译作“意志”'],
        ['sheet', '', 'ANSWER\\s+(SHEET)', '答题纸；答题卡'],
        ['point', '', '(?:\\d+|forty|twenty)\\s+(points)', '分（题目分值）'],
        ['following', '', '(following)\\s+(?:four|questions|text|passage|table|chart)', '下列的；以下的'],
        ['follow', '', '(following)\\s+(?:four|questions|text|passage|table|chart)', '下列的；以下的'],
        ['letter', '', '(letter)\\s+of\\s+the\\s+law', '法律条文的字面含义'],
        ['lean', '', '(lean)\\s+times', '经济困难的；不景气的'],
        ['shed', '', '(shed)\\s+workers', '裁减；裁员'],
        ['hold', '', '(held)\\s+steady', '保持稳定'],
        ['ground', '', '(ground)\\s+such\\s+snap\\s+reactions', '使建立在……基础上'],
        ['cause', '', 'problem\\s+fake\\s+grass\\s+(causes)', '造成；引起'],
        ['sense', '', 'in\\s+the\\s+(sense)\\s+of', '从……意义上说'],
        ['assume', '', '(assuming)\\s+(?:he says yes|they demonstrated)', '假如；以……为前提'],
        ['head', '', '(Head)\\s+on\\s+holiday', '前往；出发去（度假）'],
        ['condition', '', '(?:long-term|chronic)\\s+(conditions)', '慢性疾病；长期健康问题'],
        ['charge', '', '(charged)\\s+with', '被指控；被控告'],
        ['charge', '', 'politically\\s+(charged)', '充满政治争议的；具有政治敏感性的'],
        ['power', '', '(power)\\s+their\\s+data\\s+centers', '为……供电'],
        ['allow', '', '(allow)\\s+for', '使……成为可能；为……留出余地'],
        ['interest', '', 'earn\\s+(interest)', '利息'],
        ['state', '', 'United\\s+(States)', '美国（United States 国名的一部分）']
    ];
    // Specific rules precede general translation evidence; target capture prevents
    // one use of a repeated word from changing the other use in the same sentence.
    for (const row of ruleRows) add(...row);
    function occurrenceRule(lemma, record, token) {
        const en = record.en || '';
        const start = Number.isFinite(token && token.a) ? token.a : null;
        const end = Number.isFinite(token && token.b) ? token.b : null;
        for (const rule of rules) {
            if (rule.lemma !== lemma || rule.p && token && token.p && rule.p !== token.p) continue;
            rule.re.lastIndex = 0;
            let match;
            while ((match = rule.re.exec(en))) {
                const target = match[1];
                if (!target) break;
                const a = match.index + match[0].toLowerCase().indexOf(target.toLowerCase());
                if (start !== null && (a <= start && start < a + target.length || end !== null && start <= a && end > a)) return { meaning: rule.meaning, quality: 'context' };
            }
        }
        return null;
    }
    function grammar(word, token) {
        const key = normalize(word), lemma = normalize(token && token.l || key);
        if (!token) return null;
        const contracted = { "can't": '不能；无法（can not 的缩写）', "cannot": '不能；无法', "won't": '将不；不会（will not 的缩写）', "don't": '不（do not 的缩写）', "doesn't": '不（does not 的缩写）', "didn't": '没有；不（did not 的缩写）', "isn't": '不是；没有（is not 的缩写）', "aren't": '不是；没有（are not 的缩写）', "wasn't": '不是；没有（was not 的缩写）', "weren't": '不是；没有（were not 的缩写）', "haven't": '还没有（have not 的缩写）', "hasn't": '还没有（has not 的缩写）', "hadn't": '此前没有（had not 的缩写）', "wouldn't": '不会；不愿意（would not 的缩写）', "shouldn't": '不应该（should not 的缩写）', "couldn't": '不能；无法（could not 的缩写）', "mustn't": '不许；禁止（must not 的缩写）' };
        if (contracted[key]) return { meaning: contracted[key], quality: 'grammar' };
        if (token.d === 'aux' || token.d === 'auxpass') {
            const modal = { can: '能；能够；可以', could: '能；可能；可以（也可表示委婉或假设）', may: '可能；可以', might: '可能；也许', must: '必须；一定（表示必要或推断）', should: '应该；应当', shall: '将；应当', ought: '应该；应当', will: '将；会', would: '会；愿意；（在假设条件下）将会', "'ll": '将；会', "'d": '会（would 的缩写）' };
            const meaning = key === "'d" && lemma === 'have' ? null : modal[key] || modal[lemma];
            if (meaning) return { meaning: meaning + '（情态助动词，结合本句理解）', quality: 'grammar' };
            if (token.d === 'auxpass') return { meaning: '助动词，构成被动语态；不单独译出', quality: 'grammar' };
            if (lemma === 'have') return { meaning: '助动词，构成完成时；不单独译为“有”', quality: 'grammar' };
            if (lemma === 'be') return { meaning: '助动词，构成进行时；不单独译出', quality: 'grammar' };
            if (lemma === 'do') return { meaning: '助动词，用于否定、疑问或强调；不单独译为“做”', quality: 'grammar' };
            if (lemma === 'to') return { meaning: '不定式标记；不单独译为“到／向”', quality: 'grammar' };
        }
        if (token.d === 'neg') return { meaning: '不；没有（否定词）', quality: 'grammar' };
        if (lemma === 'be' && token.p === 'v') return { meaning: token.d === 'ROOT' && /\bthere\s+(?:is|are|was|were)\b/i.test(token.context || '') ? '有；存在（there be 结构）' : '是；处于；成为（联系主语和后面的状态或身份）', quality: 'grammar' };
        if (lemma === 'have' && token.p === 'v') return { meaning: '有；拥有；具有', quality: 'lexical' };
        return null;
    }
    function candidates(lemma, pos) {
        const all = words[lemma] || [];
        const compatible = all.filter(item => !pos || item.p === pos || pos === 'adj' && item.p === 'a');
        return compatible.length ? compatible : all.length === 1 ? all : [];
    }
    function lookup(word, record, token, lemma) {
        lemma = normalize(lemma || token && token.l || word);
        // Older vocabulary entries have no saved offset. Only recover an offset
        // when the written form occurs once; repeated forms remain ambiguous.
        if ((!token || !Number.isFinite(token.a)) && word && record.en) {
            const key = normalize(word);
            const matches = Array.from(record.en.matchAll(/[A-Za-z]+(?:['’][A-Za-z]+)*(?:-[A-Za-z]+)*/g)).filter(match => normalize(match[0]) === key);
            if (matches.length === 1) token = { ...token, a: matches[0].index, b: matches[0].index + matches[0][0].length };
        }
        const fixed = occurrenceRule(lemma, record, token);
        if (fixed) return fixed;
        const grammatical = grammar(word, token && { ...token, l: lemma, context: record.en });
        if (grammatical) return grammatical;
        const options = candidates(lemma, token && token.p);
        if (!options.length) return null;
        const zh = String(record.zh || '');
        // A Chinese cue shared by different senses is not disambiguating evidence.
        const scored = options.map(item => ({ item, score: Math.max(0, ...item.cues.filter(cue => cue.length >= 2 && zh.includes(cue) && !options.some(other => other !== item && other.cues.includes(cue))).map(cue => cue.length)) })).filter(item => item.score);
        scored.sort((a, b) => b.score - a.score);
        if (scored.length === 1) return { meaning: scored[0].item.m, quality: 'translation' };
        // With multiple senses in one translated sentence, use only an already
        // aligned token sense that identifies exactly one of the curated senses.
        if (scored.length > 1 && token && token.q === 'aligned') {
            const existing = options.filter(item => item.cues.some(cue => cue.length >= 2 && String(token.m || '').includes(cue)));
            if (existing.length === 1 && scored.some(item => item.item === existing[0])) return { meaning: existing[0].m, quality: 'translation' };
            return null;
        }
        if (options.length === 1) return { meaning: options[0].m, quality: 'lexical' };
        return null;
    }
    function common(lemma) { return (words[normalize(lemma)] || []).filter((item, i, all) => all.findIndex(other => other.p === item.p && other.m === item.m) === i).map(({ p, m }) => ({ p, m, count: 0 })); }
    window.EnglishContextSenses = { lookup, common, normalize, revision: '20261029-context-1' };
})();
