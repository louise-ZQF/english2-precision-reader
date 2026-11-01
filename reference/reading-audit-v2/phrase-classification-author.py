import json
from pathlib import Path
K=list(json.load(open('/tmp/english2-phrase-candidates.json')))
R={}
def add(text):
 for row in text.strip().splitlines():
  i,code,reason,*canon=row.split('|');i=int(i);assert i not in R,i
  R[i]={'lemma':K[i-1],'reason':reason}
  if code in ('F','V','C','T'):R[i]['category']={'F':'固定表达','V':'固定动词短语','C':'惯用搭配','T':'约定俗成术语'}[code]
  if canon and canon[0]:R[i]['canonical']=canon[0]
  R[i]['_group']='names' if code=='N' else 'rejected' if code=='R' else 'approved'
add('''
1|N|Silver Room Block Party 是特定街区庆典的活动名称
2|N|本文 Block Party 是前述特定庆典的简称，不能据此一律把普通组合标为词组
3|V|shut down 固定表示停业或关闭
4|F|as a whole 是固定状语，表示整体来看
5|T|foot traffic 是零售业常用的客流术语
6|R|gate donation 是本次活动收取捐款的临时名词组合
7|N|Wicker Park Fest 是特定节庆活动名
8|F|upward of 是固定数量表达，表示超过
9|V|scale back 固定表示缩减规模
10|F|by accident 固定表示偶然地
11|V|chip in 固定表示凑钱或出一份力
12|F|out of date 固定表示过时
13|T|life expectancy 为预期寿命的常用人口学术语
14|T|infant mortality 为婴儿死亡率的常用卫生术语
15|C|breaking point 为承受能力的极限这一惯用搭配
16|R|well 只是程度副词修饰 rehearsed，并无独立固定组合
17|T|primary care 为初级医疗保健的通用术语
18|T|social care 为社会照护服务的通用术语
19|T|long-term condition 为长期健康问题的医疗服务术语
20|T|think tank 是智库的约定称呼
21|V|account for 固定表示解释原因或占据比例
22|T|social determinants of health 是健康社会决定因素的完整公共卫生术语
23|C|price tag 是价格标签或价码的惯用组合
24|V|swap out 是换出原部件或替换的固定动词短语
25|F|do one's bit 是尽自己一份力的习语，our 为固定人称槽位|do one's bit
26|T|moral licensing 是道德许可效应这一行为科学术语
27|F|in charge 固定表示负责或掌管
28|R|比较级形容词串加 actions，是本句临时并列修饰
29|R|our governments and industries 是临时宾语，不把整段作为固定词组|hold ... to account
30|T|systemic change 是制度或系统层面改变的常见政策术语
31|T|balance of power 为权力平衡的政治学术语
32|R|trash disposal 是一般对象加动作名词，未形成这里必需整体识别的固定义
33|V|write off 固定表示注销或认定无望
34|R|things 是本句填充宾语；保留规范结构提示而非整个宾语片段|put ... into perspective
35|V|rein in 固定表示约束或控制
36|R|shape 是普通及物动词，collective action 是临时宾语|collective action
37|R|turn over 的宾语 keys 为本句具体事物，不把整段作为词组|turn over
38|R|driving 修饰 privilege，是具体论述中的一般名词组合
39|F|in accordance with 固定表示依照
40|F|in person 固定表示亲自到场
41|R|license renewal 为普通证件加办理动作，未证明整体固定化
42|R|fatal 是普通形容词，crash 是名词，不形成独立固定表达
43|C|be associated with 固定表示与某事有关联|be associated with
44|T|vision test 是视力检查的约定医疗或执照检查术语
45|F|have one's hands full 是忙得不可开交的习语
46|V|follow through 固定表示把行动贯彻到底
47|C|be attuned to 为熟悉或敏锐察觉的固定搭配|be attuned to
48|R|social 对 signals 的一般修饰，在这里不是必须整体解释的专业术语
49|C|cooperate with 为与某人合作的常见动词介词搭配
50|R|non-living 是普通形容词，beings 为一般名词，不能自动合为词组
51|F|on average 固定表示平均而言
52|V|set free 为释放的惯用动词搭配
53|C|bond with 是与某人建立情感联系的惯用搭配
54|C|return the favour 固定表示回报别人的帮助
55|C|refer to ... as ... 是称作某名称的固定框架|refer to ... as ...
56|F|have to 为表示必须的固定半情态结构
57|R|fellow 对 beings 为一般同类修饰，不独立标为词组
58|F|as if 为表示好像的固定连接表达
59|V|turn out 固定表示结果证明或最终成为
60|V|catch up 固定表示赶上
61|R|thought 修饰 processes 是一般思维过程名词组合，从严不标固定词组
62|V|break down 为分解或发生故障等固定动词短语
63|R|jobs gap 是本文对就业缺口的描述性名词组合
64|F|to the brim 是满到边缘的惯用表达，packed 为常见搭配动词|packed to the brim
65|R|并列省略的比较级修饰片段，不是固定词组
66|C|career change 是转行或转换职业的常用搭配
67|R|lessons 是临时宾语，完整片段不是固定词组|gear ... toward ...
68|C|be based on 为以某事为基础的固定搭配|be based on
69|R|high school 是具体退学场所，不把完整填充对象纳入词组|drop out of
70|C|apply to 为适用于或向某处申请的固定搭配
71|R|it 为本句指代，go into it 不作为独立固定表达|go into
72|R|machine 和 producing 填充动词框架，是本句片段|coax ... into doing ...
73|R|biotech 对 industry 为行业限定，普通名词堆叠
74|T|trade group 是行业协会的常见机构类型术语，非具体机构名
75|T|appeals court 是上诉法院这一通用司法机构类型
76|T|breast cancer 为乳腺癌的医学术语
77|T|personalised medicine 为个体化医疗的常用医学术语
78|T|product of nature 在本篇专利法中指天然产物的法律概念
79|R|no less 加入具体表语 product of nature，是句内比较片段|no less
80|C|file a brief 为提交法律意见书这一常用法律搭配
81|N|本篇所指 Supreme Court 为美国最高法院这一特定机构名
82|T|public domain 为公有领域的法律术语
83|F|connect the dots 为把线索联系起来的习语，connecting 是合理词形变化|connect the dots
84|N|Mayo Clinic 是梅奥诊所的机构名称
85|R|shifting 修饰 landscape 为本文比喻性描述，不是固定词组
86|R|完整主谓句，不能作为词组
87|F|for good 固定表示永久地
88|F|birds of passage 为候鸟或来去匆匆者的惯用说法
89|F|意大利语固定说法，字面为候鸟，本文用作 birds of passage 的外语引语
90|F|in the making 固定表示形成或发展中
91|V|kick out 固定表示赶走或开除，kicked 为过去词形|kick out
92|C|gray area 为灰色地带或界限不清领域的惯用比喻|gray area
93|F|come and go 为来来去去的固定并列表达
94|F|with ease 固定表示轻松地
95|F|middle ground 为折中立场的惯用表达
96|R|juries 是 serve on 的具体任职机构类型，不把本句完整宾语作为固定词组|serve on
97|T|cross section 为横截面或具有代表性的抽样群体的约定术语
98|F|on account of 固定表示因为
99|C|be entitled to 为有权获得或享有的固定搭配|be entitled to
100|F|the letter of the law 为法律条文字面含义的固定表达
101|T|jury system 是陪审制度这一法律制度术语
102|T|national origin 为民族或国别来源的反歧视法律概念
103|T|representative democracy 为代议民主制的政治术语
104|R|单个普通单词，不是词组
105|C|take turns 固定表示轮流
106|F|as recently as 为强调某事晚近发生时间的惯用时间结构
107|T|blue-ribbon jury 为由特选成员组成陪审团的法律用语|blue-ribbon jury
108|N|Supreme Court 为美国最高法院的特定机构名
109|C|exempt ... from ... 为豁免某责任的固定动词介词框架|exempt ... from ...
110|V|usher in 为开创或迎来新时期的固定短语，ushering 是变形|usher in
111|F|at random 固定表示随机地
112|R|state 是 level 的一般范围修饰，不构成固定表达
113|V|set off 为引发或出发等固定动词短语
114|R|ten years ago on monday 为本句具体日期，不是固定词组
115|C|run-up to 为某事件之前的准备阶段这一惯用搭配
116|R|generation 是 inspire 的临时宾语
117|T|time trial 为计时赛的体育术语
118|V|mix up 为混淆或卷入的固定短语，mixed 为词形变化|mix up
119|R|本文 common goods 表示一般的共同利益，不能据此等同规范经济学 common goods 术语
120|C|preside over 为主持或掌管的固定搭配
121|C|be prone to 为容易倾向于的固定搭配|be prone to
122|R|单个连字符复合词，应在单词层解释
123|C|snap decision 是仓促决定的惯用搭配|snap decision
124|R|单个派生复合词，不是多词词组
125|F|have little to do with 为与某事几乎无关的固定结构|have little to do with
126|T|real estate agent 为房地产经纪人的职业术语|real estate agent
127|T|thin slice 在本文为薄片观察法的心理学用语
128|R|thick sliced 为与 thin slice 临时对照的被动描述，缺乏稳定独立术语形式
129|V|rise above 固定表示超越某限制
130|C|fuse A to B 为把两者紧密结合的固定动词介词框架
131|R|单个连字符复合词，应在单词层解释
132|R|单个连字符复合词，应在单词层解释
133|F|what is more 固定表示此外或更有甚者
134|R|nursery 修饰 colours 为普通地点用途组合
135|N|Virgin Mary 为圣母玛利亚的人物名称
136|F|come into one's own 为充分发挥作用或显出价值的习语|come into one's own
137|R|core 修饰 beliefs 为一般形容词加名词
138|T|department store 为百货商店的商业业态术语|department store
139|F|stepping stone 为垫脚石或晋身之阶的惯用比喻
140|R|sure-fire 为普通限定形容词，way 为一般名词
141|F|make it 为取得成功等含义的固定表达
142|N|Bermuda triangle 为百慕大三角地名，文中借作比喻
143|F|as well as 为以及或除之外还的固定连接表达
144|C|lose faith 为失去信心的惯用搭配，lost 为过去词形|lose faith
145|F|quick fix 为权宜解决办法的惯用表达
146|F|thanks to 固定表示由于或多亏
147|C|agree on 为就某事达成一致的固定搭配
148|R|quasi-automatic 为本文临时修饰 sanctions 的性质
149|T|fiscal transfer 为财政转移支付的经济政策术语|fiscal transfer
150|R|corporate-tax 修饰 rates 为一般税种加税率组合，不整体标固定词组|corporate tax
151|T|labour cost 为劳动力成本的常用经济术语|labour cost
152|R|原卷 block 应为 bloc，不能把印刷错误确认为固定术语|trading bloc
153|F|at one's best 为在最佳状态或最理想情况下的固定表达|at one's best
154|R|failure 后接不定式是一般语法补足，不是独立固定词组
155|T|trade body 为行业协会这一通用组织类型术语
156|T|net importer 为净进口方的贸易术语
157|C|go far enough 为达到足够程度的惯用搭配
158|C|be exposed to 为接触或暴露于的固定搭配|be exposed to
159|R|productive 为一般形容词修饰 forestry，从严不标独立固定术语
160|F|on the ground 固定表示在现场或实际情况中
161|T|deep work 为深度工作这一专门认知工作概念
162|F|put a premium on 为重视或使更有价值的惯用搭配
163|V|stick to 固定表示坚持或遵守
164|V|set out 固定表示出发或着手
165|F|day by day 固定表示一天天地
166|F|when it comes to 固定表示谈到某事时
167|C|leave room for 为给某事留下余地的惯用搭配
168|T|heat action plan 为高温应对行动计划的公共卫生政策术语
169|V|spell out 固定表示明确说明
170|V|set aside 固定表示留出或暂不考虑
171|R|cold 只是对 ward 的状态修饰，本文一般病房描述
172|R|adequate 为程度评价，funding 为一般名词
173|C|shy of 固定表示不足或未达到某数量
174|T|heat wave 为热浪这一气象术语
175|R|model 修饰 plan 表示示范方案，一般名词组合
176|R|local conditions 为本句具体对象，不把整个动作片段标为词组|adapt to
177|T|vulnerability map 为脆弱性分布图这一风险评估术语
178|R|informal 修饰 dwelling 为本句住房描述，从严不标固定术语
179|R|poorly 与 heat 为本句方式和对象，完整片段不是词组|cope with
180|F|in the event of 固定表示如果发生
181|R|并列时限修饰 measure，是本句临时组合
182|R|最高级评价加普通名词，不是固定词组
183|R|would-be 为单词性修饰语，workers 为本句一般名词
184|V|leave behind 固定表示落下或把某物留在后面
185|F|in demand 固定表示有需求或受欢迎
186|R|core 修饰 skill 为普通范围限定，不标独立固定词组
187|V|let go of 为放开或放弃的固定动词短语
188|T|gold standard 为金本位或权威参照标准的约定术语
189|N|AT&T 为公司名称
190|F|rather than 为而不是的固定连接表达
191|T|skills mismatch 为技能错配的劳动经济学术语
192|V|turn to 固定表示转向或求助于
193|F|at best 固定表示充其量或往最好处说
194|R|generational 修饰 lows 为本句具体比较时段，不是固定词组
195|F|as of 固定表示截至某时点
196|F|of course 固定表示当然
197|F|no matter 为无论如何这一让步框架的固定成分
198|R|all 修饰 concerned 的名词化用法，普通语法组合
199|C|to the benefit of 为使某方受益的惯用介词搭配
200|T|cabin staff 为客舱机组人员的职业称谓
''')
add('''
201|V|start up 固定表示创办或启动
202|V|line up 固定表示排队或安排，lining 为词形变化|line up
203|N|World War II 为第二次世界大战的历史事件名
204|T|common sense 为常识的约定表达，亦在用户清单中
205|F|in combination with 固定表示与某事结合
206|N|Great Depression 为大萧条这一历史时期的名称
207|F|less is more 为少即是多的固定格言
208|R|posts 是 take up 的本句具体宾语，不把完整填充片段作为词组|take up
209|C|derive from 为来源于的固定动词介词搭配
210|F|take ... for granted 为认为理所当然的习语框架|take ... for granted
211|T|laminated wood 为层压木材的材料术语
212|R|architectural 为普通形容词，equivalent 为一般名词
213|R|self-sufficiency 为单个派生复合词，不是多词词组
214|F|contrary to 为与某事相反的固定介词表达
215|T|conventional wisdom 为普遍接受的看法这一约定表达
216|C|hold true 固定表示仍然正确或成立
217|V|kick back 固定表示放松休息
218|F|play catch-up 为努力追赶的惯用表达，playing 为词形变化|play catch-up
219|R|household tasks 为本句具体追赶对象，不把完整片段作为词组|catch up with
220|F|home front 为大后方或家庭事务领域的惯用表达
221|C|draw an income 为领取或获得收入的常用动词搭配
222|F|pretty much 固定表示几乎或差不多
223|R|hours of 后面仍需本句补语，是未完整固定化的填充片段|put in
224|R|life-sustaining 修饰俚语 moola 为本句临时描述
225|V|lay out 固定表示安排、展示或花费
226|C|talk ... into ... 为说服某人做事的固定框架|talk ... into doing ...
227|V|sign up for 为报名或承诺参加的固定动词短语
228|R|it 是本句具体指代宾语，不独立作为词组|take up
229|F|corporate ladder 为企业晋升阶梯的惯用比喻
230|F|glass ceiling 为无形晋升壁垒的固定比喻
231|C|legally binding 为具有法律约束力的惯用法律搭配
232|F|run counter to 为与某事相违背的固定表达
233|R|soft 是对 pressure 的一般性质修饰，本文指非强制压力
234|F|exception to the rule 为常态之外的例外这一惯用表达
235|F|in place 固定表示到位或就绪
236|T|living room 为客厅的约定房间称谓
237|F|in agreement 为意见一致的固定表达
238|C|burst into laughter 为突然大笑的固定搭配
239|R|conversation 是本句填充的宾语，不作为完整固定词组|keep ... going
240|C|tend to 为往往或倾向于的常见动词搭配
241|C|wreak havoc 为造成严重破坏的惯用搭配，wreaking 为词形变化|wreak havoc
242|V|amount to 固定表示相当于或总计
243|R|not 为本句否定，focused not on 是不完整句内片段|focus on
244|V|give up 固定表示放弃
245|F|first and foremost 为首要的是这一固定表达
246|R|AI 是本句具体对象，不把 engage with 的宾语填入词组|engage with
247|R|feeling heard 是本句被理解的状态描述，非固定词组
248|R|broad 修饰 right 是一般形容词加名词
249|C|take note 固定表示留意
250|T|best practice 为最佳实践的通用管理术语
251|V|back away from 固定表示退缩或不再支持
252|C|fall victim 为成为受害者的惯用搭配|fall victim to
253|F|spill the beans 为泄露秘密的固定习语
254|T|desire path 为自发形成便捷路径的规划设计术语
255|T|dirt track 为土路或土质跑道的约定称谓
256|F|cut corners 为图省事而偷工减料的习语
257|N|Ohio State University 为俄亥俄州立大学的机构名称
258|C|adhere to 为遵守或坚持的固定搭配
259|R|designated 修饰 walkways 为一般指定对象描述
260|T|Native American 为美洲原住民的通用族群称谓，非特定个人名
261|N|Whole Foods 为企业或品牌名称
262|R|physical 修饰 product 为普通形容词加名词
263|T|grocery chain 为连锁食品杂货商的商业业态称谓
264|V|go through 固定表示经历或仔细检查
265|T|party whip 为政党督导的政治职位术语
266|T|competition law 为竞争法的法律领域术语
267|R|financial 修饰 disadvantage 为普通范围限定
268|C|take a shortcut 为走捷径的惯用动词搭配
269|F|pay the price 为付出代价的固定比喻
270|R|fake 修饰 grass 是本句通俗描述，不以普通组合代替人工草坪术语|artificial turf
271|N|Royal Horticultural Society 为皇家园艺学会的机构名称
272|F|in line with 为与某事一致的固定表达
273|R|greenwash 为本句具体宾语，不把完整片段标为词组|cut through
274|V|cut through 为穿过或突破表面障碍的固定短语
275|V|call for 固定表示要求或需要
276|V|point out 固定表示指出
277|T|weed killer 为除草剂的约定产品称谓
278|F|in response to 为响应某事的固定介词表达
279|C|comply with 为遵守要求的固定动词介词搭配
280|V|soak up 固定表示吸收
281|V|count on 固定表示指望或依靠
282|R|subtle 为本句临时形容词，不纳入整体词组|strike a balance
283|T|carbon sink 为碳汇的环境科学术语|carbon sink
284|R|long into the future 是一般时间程度片段，不是固定搭配
285|R|the details 为本句宾语，不把整体片段作为词组|figure out
286|V|thin out 固定表示变稀或使减少
287|T|carbon-carrying capacity 为碳承载能力的生态学术语
288|V|fend off 固定表示抵挡或避开
289|R|emissions-permit 修饰 auctions 为本句政策操作组合，未按独立整体术语批准|emissions permit
290|R|woody 修饰 material 为普通物质描述
291|V|lock away 为锁起或封存的固定动词短语
292|F|under way 为正在进行的固定表达
293|F|chances are 为很可能的惯用引导结构
294|T|fitness tracker 为健身或活动追踪器的通用设备名称
295|C|keep track of 为持续掌握进展的固定搭配
296|F|in some shape or form 为以某种形式的固定表达
297|N|Health Insurance Portability and Accountability Act 为特定法律名称
298|R|express 是本句动作，不把具体法律概念作其宾语后的整体标为词组|affirmative consent
299|T|third party 为第三方的法律及一般业务术语
300|T|consent order 为经同意作出的命令这一法律程序术语
301|T|affirmative consent 为明确积极同意的法律隐私术语
302|F|after the fact 固定表示事后
303|T|enforcement action 为执法行动这一法律程序用语
304|C|hit the market 为产品上市的惯用搭配
305|V|shore up 固定表示支撑或加强
306|N|California Consumer Privacy Act 为加州消费者隐私法的特定法律名称
307|F|at the forefront 为处于前沿的固定表达
308|T|labor shortage 为劳动力短缺的经济学术语|labor shortage
309|T|undocumented immigrant 为无合法证件移民的通用法律社会称谓|undocumented immigrant
310|C|be hard on 为使某人难受或苛待的固定搭配|be hard on
311|R|native 和 u.s. 为本句范围限定，整体不是固定词组
312|T|dairy farm 为奶牛场的农业业态称谓|dairy farm
313|T|guest worker 为外来劳工的就业移民政策称谓|guest worker
314|R|numerical 修饰 cap 为本句数量上限的一般描述
315|R|others 为本句宾语，不能把完整填充片段当词组|drive ... underground
316|T|fossil fuel 为化石燃料的能源术语|fossil fuel
317|R|renewable 修饰 sources 为本句省略 energy 的普通名词组合|renewable energy
318|C|pick up momentum 为势头增强的惯用搭配
319|F|on line 为投入运行这一固定表达，语境需与在线义区分
320|C|stem from 为源于的固定搭配，stems 为词形变化|stem from
321|C|play well with 为与某物兼容或相处好的惯用搭配
322|T|storage capacity 为储存容量的技术术语
323|F|around the clock 为全天不间断的固定表达
324|R|big 是本句程度修饰，不把修饰后片段整体标为固定表达|place bets on
325|T|alternative energy 为替代能源的常用能源术语
326|F|by design 固定表示有意地或按设计
327|F|the next big thing 为下一个热门趋势的惯用说法|the next big thing
328|C|make one's debut 为首次亮相的固定搭配
329|F|a dozen 为十二个这一固定数量表达
330|T|regenerative agriculture 为再生农业的农业术语
331|T|greenhouse gas 为温室气体的环境科学术语
332|T|cover crop 为覆盖作物的农业术语
333|C|forage for 为搜寻食物的固定动词介词搭配
334|C|be good for 为有益于的惯用形容词搭配|be good for
335|R|premium 为普通质量档次修饰，offering 为本句产品
336|T|niche product 为面向细分市场产品的营销术语
337|T|plant-based meat 为植物基肉的食品产品术语
338|F|open the floodgates 为打开闸门而使大量涌入的固定比喻
339|N|Pennsylvania State University Brandywine 为宾州州立大学布兰迪万校区的机构名称
340|F|a hard sell 为难以推销或说服的固定表达
341|F|if any 为即使有的话的固定插入表达
342|C|be chalked up to 为被归因为的固定搭配
343|V|chalk ... up to ... 为把某事归因于的固定动词框架|chalk ... up to ...
344|T|food chain 为食物链的生态学术语
345|R|locals 和 tourists 为本句具体并列对象，不能把完整片段当词组|A and B alike
346|F|in terms of 为从某方面而言的固定介词表达
347|R|head 为普通移动动词，holiday 为本句目标，不合并完整片段|on holiday
348|T|media coverage 为媒体报道的新闻传播通用术语
349|N|Ferrovie dello Stato Italiane 为意大利国家铁路的机构名称
350|R|recovery 修饰 fund 为本句资金用途描述，不是独立固定词组
351|R|mixed 修饰 system 为一般性质描述
352|C|spare capacity 为闲置或备用产能的常用搭配
353|F|instead of 为代替或而不是的固定表达
354|V|figure out 固定表示弄清楚
355|V|turn to 固定表示转向或求助，turned 为词形变化|turn to
356|T|skin moisturizer 为润肤霜的通用产品名称|skin moisturizer
357|T|fabric softener 为织物柔顺剂的通用产品名称|fabric softener
358|T|chewing gum 为口香糖的约定名称
359|T|disinfecting wipe 为消毒湿巾的通用产品名称
360|T|air freshener 为空气清新剂的通用产品名称
361|T|water purifier 为净水器的通用产品名称
362|T|teeth whitener 为牙齿美白剂的通用产品名称
363|F|pearly whites 为洁白牙齿的惯用俗称
364|R|cavity-preventing 为单个连字符复合词，应在单词层解释
365|R|far-off 修饰 springs 为本句地点描述
366|F|all day long 为一整天的固定时间表达
367|T|breath freshener 为口气清新剂的通用产品名称
368|C|put on makeup 为化妆的惯用搭配
369|C|commercially viable 为商业上可行的常用搭配
370|F|could do worse than 为不妨做某事这一反说式固定表达
371|V|wear off 固定表示逐渐消退，wears 为词形变化|wear off
372|V|creep in 固定表示悄然出现，creeps 为词形变化|creep in
373|F|with time 为随着时间推移的惯用时间表达
374|F|wage slave 为工资奴隶或打工奴的固定比喻|wage slave
375|F|bang for your buck 为金钱所得回报的固定习语
376|F|better off 为处境更好的固定比较表达
377|R|object of obsession 是本句普通名词后置限定组合
378|C|money well spent 为花得值的钱这一惯用表达
379|N|Great Recession 为大衰退这一特定历史经济事件名称
380|T|life course 为生命历程的社会学术语
381|F|silver lining 为逆境中的希望这一固定比喻|silver lining
382|F|at the very least 为至少的强调式固定表达
383|F|put an end to 为使结束的固定搭配
384|F|for the most part 为大体上或主要地的固定表达
385|T|income inequality 为收入不平等的经济社会术语
386|R|class 修饰 divide 为本句阶层间隔阂的描述，从严不把普通名词组合标固定词组
387|V|leave behind 为落下或遗留的固定短语，left 为词形变化|leave behind
388|C|lean times 为经济不景气时期的惯用搭配
389|T|social fabric 为社会结构与关系网络的社会学惯用术语
390|F|wait and see 为静观其变的固定表达
391|F|all the more so 为更加如此的固定强调表达
392|F|whatever happened to 为某人某物如今如何了的惯用问句框架
393|V|shrug off 为不在乎或摆脱的固定短语，shrugged 为词形变化|shrug off
394|C|return to profit 为扭亏为盈的常用财务搭配|return to profit
395|T|profit margin 为利润率的财务术语|profit margin
396|F|all the same 为尽管如此或仍然的固定表达
397|C|stay afloat 为维持运营或不破产的惯用比喻，stayed 为词形变化|stay afloat
398|R|journalists 为本句具体宾语，完整比喻片段不是固定词组|push ... overboard
399|F|have the nerve to 为竟敢做某事的惯用表达，had 为词形变化|have the nerve to
400|F|according to 为根据的固定介词表达
''')
add('''
401|T|foreign bureau 为新闻媒体驻外分社的行业称谓|foreign bureau
402|F|as a result 固定表示因此或结果
403|R|national 修饰 concern 是本句关注范围的一般组合
404|R|federal tax 修饰 dollars 为本句资金来源描述
405|T|public funds 为公共资金的财政法律通用术语
406|T|public expenditure 为公共支出的财政术语
407|R|把 magnifying glass 具体比喻填入动作框架，不把整段当固定词组|magnifying glass
408|T|magnifying glass 为放大镜的约定器具名称
409|F|at the expense of 为以牺牲某事为代价的固定表达
410|F|go both ways 为双向适用的惯用表达
411|F|out of necessity 为出于必要的固定介词表达
412|V|tease out 为梳理出或逐步理清的固定短语
413|T|above average effect 为高于平均水平效应的心理学术语，本文与 illusory superiority 同指
414|T|illusory superiority 为虚幻优越感的心理学术语
415|F|hot stuff 为了不起的人或事的惯用俗语
416|V|make up for 为弥补的固定动词短语
417|R|self-esteem 为单个派生复合词，应在单词层解释
418|C|make sense 为讲得通的固定搭配，makes 为词形变化|make sense
419|F|the cream of 为最精华部分或佼佼者的惯用比喻
420|T|lingua franca 为通用语言的约定语言学术语
421|N|corporate America 为美国企业界这一集体称呼，按用户要求与普通词组分开
422|V|spin off 为分拆或衍生的固定动词短语
423|N|Fortune 500 为《财富》五百强榜单名称，companies 仅指榜单上的企业
424|F|by coincidence 为巧合地的固定表达
425|R|team-oriented 为单个连字符复合词
426|R|male-dominated 为单个连字符复合词
427|N|corporate America 为美国企业界的集体称呼，与普通词组分开
428|F|big deal 为重要的事的惯用表达
429|F|a big deal 为一件重要的事的惯用表达
430|R|explicitly 为一般程度方式副词修饰 conscious
431|R|themselves 是本句临时反身宾语，不能把完整片段当词组|think of ... as ...
432|C|infuse ... with ... 为使充满某种性质的固定框架|infuse ... with ...
433|T|non-profit organization 为非营利组织的法律社会通用类型|non-profit organization
434|T|work-life balance 为工作与生活平衡的常用社会职场术语
435|C|personal fulfillment 为个人成就感或自我实现满足感的常用搭配
436|N|本文 Lean In 为桑德伯格著作书名，不按普通动词词组解释
437|T|mommy wars 为全职与职场母亲选择争论的约定社会讨论称谓
438|F|have it all 为兼得理想生活各方面的惯用表达
439|F|in one's own right 为凭自身身份或能力的固定表达|in one's own right
440|C|devote oneself to 为投入或献身于的固定搭配
441|F|make fun of 为取笑的固定搭配，makes 为词形变化|make fun of
442|C|office speak 为办公室套话或行话的惯用称呼
443|V|buy into 为相信或接受某观念的固定短语
444|C|relate to 为与某事有关或理解认同的固定搭配
445|C|be indifferent to 为对某事漠不关心的固定搭配|be indifferent to
446|T|outside director 为外部董事的公司治理术语
447|F|under fire 为受到抨击的固定比喻
448|V|take up 为开始从事或占用的固定短语，taking 为词形变化|take up
449|T|chief executive 为首席执行官的职位术语
450|T|proxy statement 为股东投票委托书的证券法律术语
451|C|restate earnings 为重述收益的常用会计搭配
452|T|class-action lawsuit 为集体诉讼的法律术语
453|R|完整具体比喻场景，不能仅因比喻常见就将整个动作宾语片段作为词组|sinking ship
454|V|trade up 为升级更换到较好者的固定短语
455|R|bad news 作主语、breaks 作谓语，是完整主谓片段
456|F|guess what 为你猜怎么着的固定口语引导
457|T|cognitive offloading 为认知卸载的心理学术语
458|T|external hard drive 为外置硬盘的计算机设备术语
459|T|data bank 为数据库或数据资料库的技术术语
460|T|conceptual thinking 为概念思维的认知教育术语
461|C|interfere with 为妨碍或干扰的固定动词介词搭配
462|F|for the better 为向更好方向的固定表达
463|R|mechanical 修饰 memorization 为本句一般学习方式描述
464|C|accepted wisdom 为普遍接受的看法的惯用搭配
465|T|vocational education 为职业教育的教育术语
466|R|academically 为本句临时方面状语，不把完整片段当固定表达|make it
467|F|economic engine 为经济驱动引擎的惯用比喻
468|T|job security 为工作稳定性的职场术语
469|R|more 为本句比较限定，不把可变形容范围纳入固定短语|open doors
470|R|the country 和 political 为本句具体对象与修饰，不整体作为词组|turn ... on its head
471|R|us 为本句具体宾语；规范固定框架可另作搭配解释|stare ... in the face
472|R|that gap 为本句具体宾语，不是完整固定词组|fill a gap
473|F|wake-up call 为警钟或提醒的固定比喻
474|R|retirement 为本句具体时间端点，well into 可修饰任意时段
475|F|at least 固定表示至少
476|V|settle down 固定表示安定下来
477|C|mentally fit 为精神状态良好或头脑健全的常用搭配
478|R|past 后接 retirement 为本句普通时间关系
479|T|labor force 为劳动力人口的经济学术语
480|C|all-time low 为历史最低点的惯用数量搭配
481|T|money manager 为投资管理者的金融职业称谓
482|F|nest egg 为储蓄备用金的固定比喻
483|F|in anticipation of 为预期或为准备某事的固定表达
484|T|retirement account 为退休账户的金融制度术语
485|T|life insurance 为人寿保险的保险术语
486|F|make ends meet 为收支相抵的固定习语
487|C|start a family 为生育建立家庭的惯用搭配
488|C|get married 为结婚的常用固定搭配
489|C|first impression 为第一印象的惯用搭配|first impression
490|T|thin slice 在本文为薄片观察法的心理学用语|thin slice
491|F|not only 为不仅而且结构中的固定关联成分
492|C|correlate with 为与某事相关的固定统计学搭配
493|T|working memory 为工作记忆的认知心理学术语
494|T|social processing 为社会信息加工的认知心理学术语
495|V|write down 固定表示记下
496|C|rely on 为依靠的固定动词介词搭配
497|T|stick shift 为手动挡变速器的汽车术语
498|F|on automatic pilot 为自动驾驶或不加思索行动的惯用表达
499|C|align with 为与某事保持一致的常用搭配
500|F|only if 为只有在某条件下的固定连接表达
501|T|reflective thinking 为反思性思维的认知教育术语
502|T|figure of speech 为修辞格的语言学术语|figure of speech
503|F|spring to mind 为突然想起的固定表达
504|F|up and down the country 为全国各地的惯用表达
505|F|a hive of activity 为一片繁忙景象的固定比喻
506|F|at the heart of 为处于核心的固定表达
507|T|intellectual property 为知识产权的法律术语
508|F|on site 为在现场的固定表达
509|V|carry out 固定表示实施或执行
510|T|GP's surgery 为全科医生诊所的英式医疗称谓|GP's surgery
511|F|in return for 为作为对某事的回报的固定表达|in return for
512|F|no charge 为不收费的惯用表达
513|V|leave alone 为不打扰或不干涉的固定短语
514|R|put something at 是未完成的普通动词补足框架，缺少固定成分
515|R|too 修饰数量 many 是普通程度语法，不作为词组
516|C|raise awareness 为提高认识的惯用搭配
517|T|branding campaign 为品牌推广活动的营销术语
518|R|sign-up 修饰 process 为一般流程限定，不能自动整体标词组
519|C|think about 为考虑某事的常见动词介词搭配
520|T|dark pattern 为暗黑模式的交互设计术语
521|C|catch-all term 为涵盖多种事物的笼统术语的惯用称呼
522|T|hidden cost 为隐性成本的经济或消费术语
523|T|roach motel 为易进难退的特定暗黑交互模式术语
524|V|get out 为离开或逃出的固定动词短语
525|F|gray area 为灰色地带或界限不清领域的惯用比喻
526|C|be aware of 为意识到的固定搭配
527|C|engage in 为从事或参与的常用搭配
528|T|checkout basket 为电商购物结账篮的界面术语
529|R|digital 修饰 deception 为一般方式限定，不是独立固定术语
530|T|Attorney General 为总检察长的通用职务称谓，非具体人的名字
531|V|opt out 为选择退出的固定动词短语
532|V|click through 为点击进入下一页或链接的固定网络动词短语
533|C|hold oneself accountable 为要求自己承担责任的惯用框架
534|R|funding 为本句具体缺口类别，完整片段不作固定词组|plug a gap
535|V|line up 固定表示排队或安排
536|F|in crisis 为处于危机中的固定状态表达
537|R|maintenance 修饰 backlog 为本句积压事项类别，未批准为独立专业术语
538|V|hand over 固定表示移交
539|C|a break from 为暂时摆脱或暂停某活动的惯用搭配
540|R|commercial 对 drumbeat 为本句比喻修饰，不构成固定表达
541|R|funding 为本句具体缺乏对象，不把整体填充片段当词组|starve of
542|C|starve ... of ... 为使缺乏的固定动词介词框架|starve ... of ...
543|C|place a high value on 为高度重视的惯用搭配
544|F|whether or not 为是否或无论是否的固定连接表达
545|C|make sure 为确保或弄清楚的固定搭配
546|F|on top of 为除了某事之外还的固定表达，this 为简单指代|on top of
547|T|carbon sequestration 为碳封存的环境科学术语
548|F|bring ... to life 为使生动或使恢复活力的固定框架|bring ... to life
549|F|on a shoestring 为资金拮据地的固定习语
550|T|stimulus package 为经济刺激方案的政策术语
551|F|with the exception of 为除某事之外的固定表达
552|C|stand at 为数值处于某水平的常见搭配
553|F|in conjunction with 为与某事结合或共同的固定表达
554|F|get a bad rap 为遭受不公指责或恶名的固定俗语
555|R|us 是本句具体宾语，不把填充形式独立列为词组|alert ... to ...
556|R|a cooperative species 为本句具体宾语，完整片段不是固定词组|hold ... together
557|F|social glue 为社会凝聚力量的惯用比喻
558|C|compensate for 为弥补或补偿的固定搭配
559|R|nastier 是比较级修饰 impulses，临时语义组合
560|F|vice versa 为反之亦然的固定外来表达
561|C|substitute ... for ... 为用某物替代的固定框架|substitute ... for ...
562|V|turn on 为打开或转而攻击等固定动词短语
563|F|give or take 为上下相差或大约的固定表达
564|C|hit the streets 为走上街头或投放市场的惯用搭配
565|T|labor market 为劳动力市场的经济学术语
566|F|be about to 为即将做某事的固定结构|be about to
567|R|economic 修饰 train wreck 为本句临时经济灾难比喻|train wreck
568|C|life savings 为毕生积蓄的惯用搭配
569|C|take chances 为冒险的惯用动词搭配
570|F|with ... in mind 为考虑到某事的固定框架
571|R|secure 是普通形容词或动词，employment 为本句一般对象
572|R|inspiring 修饰 purpose 为普通形容词加名词
573|R|serving 为本句动作，不能把动作和具体价值目标整段当词组|the greater good
574|T|gig economy 为零工经济的经济社会术语
575|T|risk averse 为风险厌恶的经济决策术语
576|T|finish line 为终点线的体育术语，文中可借喻
577|R|best 为普通最高程度修饰，served 为一般被动谓语片段
578|R|housing 修饰 patterns 为本句居住方式描述
579|R|achievements 为 signpost 的临时宾语
580|T|mortgage payment 为按揭还款的住房金融术语|mortgage payment
581|F|on one's own 为独立或独自的固定表达|on one's own
582|R|rooms 为本句可变宾语，不把填充对象的完整片段作为词组|rent out
583|R|that 为本句具体指代，不把整个补语作为词组|be capable of
584|T|first-generation college student 为第一代大学生的教育社会术语
585|T|dropout rate 为辍学率的教育统计术语
586|R|economically 为本句一般方面状语，advance 为普通动词
587|T|social class 为社会阶层的社会学术语
588|F|in that 为因为或在于的固定连接表达
589|T|achievement gap 为群体学业成就差距的教育术语
590|R|next-to-no-cost 为单个连字符临时复合修饰词，不是多词词组
591|N|Pell Grants 为佩尔助学金这一特定政府资助项目名称
592|F|rules of the game 为行事或竞争规则的惯用比喻
593|F|take advantage of 为利用或占便宜的固定搭配
594|T|boom and bust cycle 为繁荣与萧条周期的经济术语
595|V|eat up 固定表示耗尽或吞噬，eating 为词形变化|eat up
596|C|hail from 为来自某地的惯用搭配
597|F|in the first place 为起初或首先的固定表达
598|C|leave no room for 为不给某事留下余地的惯用否定搭配
599|C|take initiative 为主动采取行动的惯用搭配
600|R|their 为本句具体人称修饰，不把填充形式作为独立词组|exercise one's imagination
''')
add('''
601|V|touch on 为简要涉及的固定短语，touched 为词形变化|touch on
602|R|machine 为本句比喻对象，race with 的对象可变，不整体标词组
603|R|work 修饰 practices 为本句工作做法的一般组合
604|T|bull run 为牛市持续上涨行情的金融术语
605|R|two 为本句具体数字，不把数量填入固定词组|all but
606|R|last 修饰 victory 为普通时间限定
607|V|call out 为大声说出或公开指出的固定短语，called 为词形变化|call out
608|C|file for bankruptcy 为申请破产的法律惯用搭配，filed 为词形变化|file for bankruptcy
609|C|lose momentum 为失去发展势头的惯用搭配，losing 为词形变化|lose momentum
610|T|auction house 为拍卖行的通用机构类型称谓|auction house
611|V|pay out 固定表示支付或赔付
612|F|at the bottom 为在最底端的惯用位置表达
613|V|keep away 为远离的固定短语，keeping 为词形变化|keep away
614|V|roll out 固定表示推出新产品或政策
615|C|levy fines 为处以罚款的法律惯用搭配
616|F|on one's own 固定表示独自或独立地
617|R|individual 修饰 drivers 为一般范围限定
618|T|ultra-low emission zone 为超低排放区的交通环保政策术语
619|F|far from it 为远非如此的固定表达
620|F|in the face of 为面对某处境的固定表达
621|T|premature birth 为早产的医学术语|premature birth
622|T|heart attack 为心脏病发作的医学惯用术语
623|R|untimely 为普通时间评价修饰 deaths，未整体固定化
624|F|can only do so much 为能做的有限的惯用表达
625|R|into compliance 为动作补语的句内片段，不独立作为固定词组|bring ... into compliance
626|F|everything but 为除了某事以外一切或几乎是的惯用结构
627|V|clean up 固定表示清理或整顿
628|N|Cogs and Monsters 为特定书名
629|T|gig worker 为零工劳动者的就业术语
630|C|social buy-in 为社会接受与支持的常用政策搭配
631|R|in 是本句临时地点介词，不应纳入数量词组|a handful of
632|F|a handful of 为少数几个的固定数量表达
633|V|hold back 固定表示抑制或阻碍
634|C|lie in 为在于的固定动词介词搭配
635|C|tech giant 为科技巨头的惯用新闻称谓
636|C|independent of 为不依赖于的固定形容词搭配
637|C|conceive of 为构想或设想的固定动词介词搭配
638|T|factory-farmed meat 为集约化养殖肉类的食品农业类别术语
639|T|charitable giving 为慈善捐赠的公益领域通用术语
640|C|focus on 为专注于的固定搭配
641|R|meal-card 修饰 purchases 为本文具体调查数据类别
642|C|differ from 为不同于的固定搭配
643|C|hold steady 为保持稳定的惯用搭配
644|T|confounding variable 为混杂变量的统计学术语
645|V|rule out 为排除的固定动词短语
646|F|Easy come, easy go 为来得容易去得快的固定谚语
647|T|social influence 为社会影响的社会心理学术语
648|R|rational 修饰 argument 为普通评价性形容词加名词
649|F|eat one's words 为承认说错话或收回前言的固定习语
650|T|food security 为粮食安全的政策术语
651|C|close to 为接近某地点或数量的惯用搭配
652|C|keep pace 为保持同步的惯用搭配
653|C|make headlines 为成为新闻头条的惯用搭配
654|C|talking point 为讨论要点或引起讨论的话题的惯用称呼
655|C|associate with 为与某事联系或交往的固定搭配
656|R|livestock 修饰 farms 为本句畜牧农场的一般类别描述
657|R|animal 修饰 foods 为本文动物来源食物的一般分类
658|T|animal husbandry 为畜牧业的农业术语
659|C|on a commercial basis 为按商业方式运作的惯用搭配
660|R|arable 修饰 fields 为普通性质描述，不按术语 arable land 整体替换|arable land
661|T|nature reserve 为自然保护区的环保政策术语|nature reserve
662|V|take out 为取出或移除等固定短语
663|T|fresh produce 为生鲜农产品的零售食品类别称谓
664|R|vast 是对 bulk 的一般程度修饰，不整体标固定词组|the bulk of
665|T|calorie intake 为热量摄入的营养学术语
666|C|look for 为寻找的固定动词介词搭配
667|R|you 为本句临时宾语，不把完整片段作为词组|suck in
668|T|still face experiment 为静止脸实验的发展心理学术语
669|R|some work 为本句具体宾语，不整体标固定表达|get ... out of the way
670|F|get a lot out of 为从某事获益良多的惯用搭配
671|C|shoulder the blame 为承担责备的惯用搭配
672|C|politically charged 为政治意味强烈的惯用搭配
673|T|waiting list 为候补名单或待诊名单的通用服务术语|waiting list
674|C|a cap on 为对某数量的上限这一惯用名词介词搭配|a cap on
675|F|down to 为归因于或取决于的固定表达
676|V|face up to 为正视并承担的固定短语
677|C|return to power 为重新执政的政治惯用搭配，returns 为词形变化|return to power
678|R|large-scale 与 public 为本句修饰 grants 的规模和来源，不整体固定化
679|C|be meant to 为本应或旨在做某事的固定搭配
680|F|on one's own 为独自或靠自身的固定表达|on one's own
681|R|a pass 是本句具体名词化许可，给某机构放行的完整片段从严不整体批准|give ... a pass
682|T|report card 为成绩单的教育通用称谓|report card
683|F|no more than 为仅仅或至多的固定数量结构
684|R|across-the-board 为单个连字符复合修饰词，应在单词层解释
685|R|what works best 为本句关系或疑问内容片段，不是固定词组
686|F|put on hold 为暂停处理的固定搭配
687|V|look into 为调查的固定短语，looks 为词形变化|look into
688|T|public hearing 为公开听证会的法律行政程序术语|public hearing
689|V|free up 为腾出资源的固定动词短语
690|R|last thing 缺少其后具体补足，不能把一般最高序位词组一概当习语|the last ... to ...
691|R|well 为一般方式评价，spent 为被动分词，单独两词不构成专有固定表达|money well spent
692|F|in so far as 为在某范围内或就某方面而言的固定连接表达
693|R|it 为本句具体宾语，不把填充形式整体作为词组|slot in
694|T|conveyor belt 为传送带的机械设备术语
695|N|Sacred Time 为盖里·埃伯利所著书名
696|R|yourself 为本句动作对象，不把一般反身动词组合认作固定词组|lose oneself in
697|R|soul time 为本篇作者自造的引语标签，并非通用固定表达
698|R|physical 修饰 books 为本句媒介形态对照，不是独立固定词组
699|V|dip in 为随意翻阅或短暂参与的固定动词短语
700|T|default state 为默认状态的技术及认知模型术语
701|T|lesser prairie chicken 为小草原榛鸡的物种通用名称，非个体专名
702|R|red 是本文具体景观颜色，lend red to 并非固定搭配|lend colour to
703|N|U.S. Fish and Wildlife Service 为美国鱼类和野生动物管理局的机构名称
704|V|crack down on 为严厉打击的固定动词短语
705|V|call for 为要求或需要的固定短语，called 为词形变化|call for
706|T|annual average 为年平均值的统计通用术语
707|F|in the driver's seat 为掌控局面的固定比喻
708|T|unemployment rate 为失业率的经济统计术语
709|T|full employment 为充分就业的经济学术语
710|R|part-time 为单个连字符复合词，应在单词层解释
711|R|full-time 为单个连字符复合词，应在单词层解释
712|T|involuntary part-time work 为非自愿兼职工作的劳动统计术语
713|T|reference week 为调查参考周的统计调查术语
714|R|survey 修饰 taker 为一般参加调查人员描述，不是本篇需要整体解释的固定术语
715|R|employment 为本句 outside of 的对象，不把补语填入词组|outside of
716|T|health insurance 为医疗保险的保险术语
717|C|health condition 为健康状况或健康问题的常见医疗搭配
718|T|textile mill 为纺织厂的工业业态称谓
719|C|make the point 为表达或强调观点的惯用搭配，making 为词形变化|make the point
720|V|stand out 为脱颖而出的固定动词短语
721|R|workers 为 shed 的本句具体宾语，不把普通动宾短语整体固定化
722|F|for sure 为肯定地的固定表达
723|R|post-high school 为本句教育阶段限定，整体不按固定词组批准
724|T|gap year 为空档年或间隔年的教育生活术语
725|V|stay back 为留下或留在后面的固定动词短语
726|C|struggle with 为艰难应对的固定动词介词搭配
727|C|lessen the blow 为减轻打击的惯用比喻搭配
728|V|make up 为组成、化妆或编造等固定动词短语
729|F|late in the game 为事情进程已晚的固定比喻
730|R|倒装虚拟条件句的本句具体谓语，不是固定词组
731|T|nursing school 为护理学校的教育机构类型术语
732|R|things 为本句可变宾语，不整体认作固定词组|figure out
733|F|from the ground up 为从头开始或全面地的固定表达
734|V|stay on 为继续留下的固定动词短语
735|C|feed a hunger for 为满足某种强烈渴望的惯用比喻框架|feed ... hunger for ...
736|V|chew up 为嚼碎或大量耗费的固定动词短语
737|V|close down 为停业关闭的固定动词短语
738|C|mixed feelings 为矛盾复杂感受的惯用搭配
739|R|my 与 selfish 为本句特定角色比喻填充，不把整段当固定词组|put on one's ... hat
740|C|depend on 为依靠或取决于的固定搭配
741|N|Federal Trade Commission 为美国联邦贸易委员会的机构名称
742|V|wade into 为涉入或介入的固定动词短语
743|V|rifle through 为快速翻找的固定动词短语
744|F|beside the point 为不切题的固定表达
745|F|a drop in the ocean 为沧海一粟的固定比喻
746|T|financial reserves 为财务储备的金融通用术语
747|T|venture capital 为风险投资的金融术语
748|C|compared with 为与某事相比的惯用比较搭配
749|C|gain momentum 为势头增强的惯用搭配
750|R|buy and kill 为本文概括并购后关停的引语标签，不从本句标成通用固定表达|killer acquisition
751|T|minimum wage 为最低工资的劳动政策术语
752|T|digital payment system 为数字支付系统的金融技术术语
753|V|creep into 为悄然进入的固定动词短语
754|T|default option 为默认选项的交互设计及决策术语
755|T|tip creep 为小费要求不断蔓延的消费讨论通用称谓
756|V|fizzle out 为逐渐无疾而终的固定动词短语
757|R|the temptation 为本句具体宾语，不能把完整动宾片段认作词组|succumb to
758|C|dissociate from 为与某事脱离或划清联系的固定搭配
759|F|take care of 为照顾或处理的固定搭配
760|F|go hand in hand 为紧密相伴的固定习语
761|C|concentrate on 为集中于的固定动词介词搭配
762|R|late 为本句时间状语，不把含状语片段作为固定词组|stay out
763|V|fade away 为逐渐消失的固定动词短语
764|C|hold for 为对某种情况适用或成立的惯用搭配
765|T|positive correlation 为正相关的统计学术语
766|T|reward sensitivity 为奖赏敏感性的心理学术语
767|T|social reward 为社会奖赏的心理学术语
768|R|CEO 修饰 pay 为本句薪酬主体，普通名词堆叠
769|T|publicly traded 为上市交易的金融法律惯用术语
770|V|go up 为上升的固定动词短语
771|R|limited、CEO 对 talent 为本句临时数量与对象限定
772|F|up one's game 为提升表现的固定习语，their 为固定人称槽位|up one's game
773|T|public relations 为公共关系的传播管理术语
774|T|supply chain 为供应链的经济管理术语|supply chain
775|F|one way or another 为以某种方式或无论如何的固定表达
776|V|rip off 为敲竹杠或剽窃的固定动词短语
777|T|corporate governance 为公司治理的管理法律术语
778|R|corporate 修饰 interest 为本句公司利益的一般范围限定
779|R|insider 修饰 picks 为本句内部挑选人选的临时描述
780|T|stock price 为股价的证券市场术语|stock price
781|R|corporate 修饰 value 为本句一般公司价值描述，不把歧义组合自动批准为术语
782|V|build up 为逐渐积累或增强的固定动词短语
''')
assert len(R)==len(K),(len(R),len(K),set(range(1,len(K)+1))-R.keys())
# Normative framework glosses deliberately exclude the sentence's temporary object.
meanings={
'hold ... to account':'要求……作出解释并承担责任',
'put ... into perspective':'结合整体情况正确看待……',
'bring ... to life':'使……生动起来；赋予……活力',
'set free':'释放；放走',
'feed ... hunger for ...':'满足……对……的强烈渴望',
'bring ... into compliance':'使……达到合规标准',
'get ... out of the way':'先处理完……；排除……这一障碍',
'keep ... going':'使……持续进行',
'exempt ... from ...':'使……免除……义务或责任',
'fuse A to B':'把 A 与 B 紧密结合或绑定',
'put on one\'s ... hat':'以某种角色或立场思考问题',
'starve ... of ...':'使……缺乏……',
'hold ... together':'使……保持团结或结合在一起',
'alert ... to ...':'提醒……注意到……',
'gear ... toward ...':'使……适合或面向……',
'coax ... into doing ...':'劝诱……做……',
'drive ... underground':'迫使……转入地下或隐蔽状态',
'give ... a pass':'对……放行；不追究……',
'stare ... in the face':'明显摆在……眼前',
'put ... on its head':'使……彻底颠倒',
'exercise one\'s imagination':'发挥想象力',
'all but':'几乎；除……之外全都',
'focus on':'专注于；把关注点放在',
'lose momentum':'失去势头',
'give up':'放弃',
'figure out':'弄清楚',
'catch up with':'赶上；及时处理积压事项',
'serve on':'在……机构中任职',
'refer to ... as ...':'把……称为……',
'connect the dots':'把线索联系起来',
'make sense':'有道理；讲得通',
'put on hold':'暂缓；暂停处理',
'be capable of':'能够做；有能力做',
'succumb to':'屈从于；抵挡不住',
'suck in':'把……吸引或卷入',
'drop out of':'从……退学或退出',
'leave room for':'给……留下余地',
'set ... free':'释放……；放走……'
}
for row in R.values():
 key=row.get('canonical',row['lemma'])
 if key in meanings:row['canonicalMeaning']=meanings[key]
 if row['lemma']=='set free':row['canonical']='set ... free';row['canonicalMeaning']=meanings['set ... free']
OUT={g:[] for g in ('approved','names','rejected')}
for i in sorted(R):
 row=dict(R[i]);g=row.pop('_group')
 if 'canonicalMeaning' in row:row['meaning']=row.pop('canonicalMeaning')
 if g=='names':row['kind']='name'
 OUT[g].append(row)
p=Path('/Users/huyawen/Desktop/英语二/考研英语本地版/reference/reading-audit-v2/phrase-classification.json')
p.write_text(json.dumps(OUT,ensure_ascii=False,indent=2)+'\n')
print({g:len(v) for g,v in OUT.items()},'total',sum(map(len,OUT.values())))
