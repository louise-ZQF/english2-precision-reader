# -*- coding: utf-8 -*-
from pathlib import Path
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from reading_audit import Review
r=Review('2025-T3')
# Every listed sense was checked against this article, including repeated grammatical words.
spec='''able~able~a=能够;about~about~prep=关于;according~according~prep=根据（according to整体）;action~action~n=应对行动;adapted~adapt~v=作调整以适应;adequate~adequate~a=足够的;advise~advise~v=向……提供建议;advises~advise~v=建议;alert~alert~n=预警;alerts~alert~n=预警;all~all~art=所有;alone~alone~adv=仅仅；单看;already~already~adv=已经;also~also~adv=还；也;among~among~prep=在……之中（among other things引出其他要点）;amplified~amplify~v=加剧；放大;april~April~name=四月;are~be~aux=被动语态助动词;areas~area~n=地区;as~as~prep=作为;aside~aside~part=与set组成专门留出的搭配;at~at~prep=在（时刻或风险状态）;authorities~authority~n=主管部门;be~be~aux=被动助动词;been~be~aux=完成进行时助动词;best~good~a=最佳的;bolstered~bolster~v=加强支持；增强应对能力;break~break~n=休息；暂停;builders~builder~n=建筑商；施工单位;building~building~n=建筑;but~but~conj=但；而;by~by~prep=由；由于（被动施事或原因）;calls~call~v=要求（与for搭配）;can~can~aux=能够;centers~center~n=中心；服务场所;centre~Centre~name=中心（机构名的一部分）;ceremony~ceremony~n=仪式;chandni~Chandni~name=钱德妮（研究者名）;cities~city~n=城市;city~city~n=城市;climate~climate~n=气候;coastal~coastal~a=沿海的;cold~cold~a=凉爽的；用于降温的;communities~community~n=社区;complex~complex~a=复杂的;conditions~condition~n=情况；条件;construction~construction~n=建筑施工;cooler~cool~a=更凉爽的;cooling~cool~a=用于降温避暑的;cope~cope~v=应对；抵御（与with搭配）;could~can~aux=可以；可能;create~create~v=绘制；创建;created~create~v=绘制；创建;customized~customize~v=按当地情况针对性调整;day's~day~n=那一天的;days~day~n=天；日子;daytime~daytime~n=白天;deaths~death~n=死亡事件;doesn't~do not~aux=不（does not缩写）;dwellings~dwelling~n=住所；住房;effects~effect~n=影响;efforts~effort~n=工作；努力;elderly~elderly~a=年老的;emergency~emergency~n=紧急情况;enabled~enable~v=使……能够;even~even~adv=哪怕；即使只;event~event~n=情况（in the event of表示如果发生）;example~example~n=例子（for example整体为例如）;existing~exist~a=现有的;factor~factor~n=因素;few~few~art=少数几个;focus~focus~v=集中（应对工作）;for~for~prep=针对；为了;found~find~v=研究发现;from~from~prep=从；离开;funding~funding~n=资金支持;gauge~gauge~n=衡量标准；指标;general~general~n=概括情况（in general整体为一般来说）;get~get~v=获得;give~give~v=给予；安排;good~good~a=好的;guide~guide~v=指导;hap~HAP~abbr=高温应对行动计划;haps~HAP~abbr=高温应对行动计划（复数）;has~have~aux=完成时助动词;have~have~aux=完成进行时助动词;heat~heat~n=高温；热;heatstroke~heatstroke~n=中暑;help~help~v=帮助;high~high~a=高的;highlighted~highlight~v=凸显；表明;highs~high~n=最高气温;homes~home~n=住宅;hospitals~hospital~n=医院;hot~hot~a=炎热的;how~how~adv=如何；以何种方式;humidity~humidity~n=湿度;implementation~implementation~n=实施；落实;important~important~a=重要的;improve~improve~v=改进;in~in~prep=在（地区或时间范围内）;include~include~v=包括;india~India~name=印度;informal~informal~a=非正规建设的（住房）;instance~instance~n=例子（for instance整体为例如）;institutions~institution~n=机构;is~be~aux=与working构成进行时;issue~issue~v=发布（预警）;it~it~pron=该报告（回指研究报告）;it's~it is~pron=它是（it is缩写，指减少死亡这一目标）;just~just~adv=仅仅；只;key~key~a=关键的;kotharkar~Kotharkar~name=科塔卡尔（研究者姓）;kotharkar's~Kotharkar~name=科塔卡尔的;laborers~laborer~n=工人;lack~lack~v=缺乏;large~large~a=数量多的；规模大的;late-morning~late-morning~a=上午较晚时段的；临近中午的;local~local~a=当地的;localized~localize~a=符合当地具体情况的;long-term~long-term~a=长期的;looking~look~v=考察（与at搭配）;lowest~low~a=最低限度的;make~make~v=使；让;many~many~pron=许多计划;map~map~n=分布图；地图;mapping~mapping~n=绘制分布图;measures~measure~n=措施;medium-to~medium-to~a=中期到……（与long-term连读）;meteorological~meteorological~a=气象的;might~may~aux=可能;model~model~a=示范性的;modify~modify~v=修改;more~more~adv=更加;most~most~adv=最；程度最高;mumbai's~Mumbai~name=孟买的;nagpur~Nagpur~name=那格浦尔;nagpur's~Nagpur~name=那格浦尔的;national~national~a=国家的;need~need~v=需要;neglected~neglect~v=被忽视;neighborhoods~neighborhood~n=社区；街区;nighttime~nighttime~n=夜间;nuanced~nuanced~a=细致地考虑差异的;of~of~prep=……的（限定关系）;officials~official~n=官员;often~often~adv=经常；往往;on~on~prep=在（日期或工作对象）;other~other~art=其他的;out~out~part=与spell构成明确说明的搭配;outdoor~outdoor~a=户外的;outlines~outline~v=概述；梳理;parameters~parameter~n=参数；评估指标;past~past~a=过去的;patients~patient~n=患者;places~place~n=地区；地方;plan~plan~n=计划;planner~planner~n=规划师;plans~plan~n=计划;plant~plant~v=种植;policy~Policy~n=政策（机构名的一部分）;poorly~poorly~adv=不好地；应对能力差地;population~population~n=人口；人群;populations~population~n=人群;practices~practice~n=做法；实践;project~project~n=项目;proliferating~proliferate~v=迅速增多;provide~provide~v=提供;rajashree~Rajashree~name=拉贾什里（姓名）;recommend~recommend~v=建议；提出;reducing~reduce~v=减少;regulations~regulation~n=规定；法规;report~report~n=报告;research~Research~n=研究（机构名的一部分）;researcher~researcher~n=研究人员;researchers~researcher~n=研究人员;responses~response~n=应对措施;retrofit~retrofit~v=改造既有住宅以改善性能;risk~risk~n=风险;roughly~roughly~adv=大约;say~say~v=表示；指出;says~say~v=说；指出;serve~serve~v=充当；作为（serve as）;set~set~v=设置；规定;shade~shade~n=遮阴；阴凉处;short-term~short-term~a=短期的;should~should~aux=应该;shouldn't~should not~aux=不应该;shy~shy~a=尚未达到；差一点的;singh~Singh~name=辛格（姓）;some~some~art=一些;special~special~a=专门的；针对性的;spells~spell~v=明确说明（与out连用）;such~such~art=这样的；这种;summer~summer~n=夏季;systems~system~n=系统;target~target~n=目标;team~team~n=团队;tell~tell~v=告诉;temperature~temperature~n=气温;temperatures~temperature~n=气温;that~that~pron=关系代词，指前面的事物;things~thing~n=事项；要点;this~this~art=这个；今年的;threshold~threshold~n=预警门槛；阈值;thresholds~threshold~n=预警门槛；阈值;to~to~part=不定式标记，不单译;treating~treat~v=治疗;trees~tree~n=树木;trigger~trigger~n=触发预警的条件;triggering~trigger~a=用于触发预警的;uneven~uneven~a=参差不齐的;urban~urban~a=城市的;useful~useful~a=有用的;very~very~adv=非常;vulnerability~vulnerability~n=易受伤害的程度；脆弱性;wards~ward~n=病房;warnings~warning~n=预警;was~be~v=是；处于;wave~wave~n=热浪（heat wave搭配）;were~be~aux=过去时被动助动词;when~when~adv=何时;where~where~adv=在哪里;which~which~pron=关系代词，指前面内容;with~with~prep=具有；带有;work~work~n=工作;working~work~v=致力于制定（与on连用）;years~year~n=年'''
r.lex(spec.replace(';','\n'))
r.word('P1-S1','or','即；也称（解释同一名称）',pos='conj')
r.word('P1-S1','in','在印度（地点）',occ=1)
r.word('P1-S2','alert','通知；提醒',pos='v')
r.word('P1-S3','for','例如（for instance搭配）',occ=1)
r.word('P1-S3','for','要求（call for搭配的介词）',occ=2)
r.word('P1-S3','set','专门留出（set aside搭配）')
r.word('P1-S3','from','从工作中暂时脱离；暂停工作',pos='prep')
r.word('P2-S1','been','与has构成完成时，说明已存在的状态',pos='v')
r.word('P2-S1','to','根据（according to搭配）',pos='prep')
r.word('P2-S3','to','按……情况调整（customized to搭配）',pos='prep')
r.word('P2-S5','as','程度比较标记（as important ... as）',pos='adv',occ=1)
r.word('P2-S5','as','和……一样（引出白天最高气温作比较）',pos='conj',occ=2)
r.word('P2-S5','be','是；可作为（系动词）',pos='v')
r.word('P3-S1','need','需要；必要性',pos='n')
r.word('P3-S1','more','更加（修饰细致和因地制宜）',pos='adv')
r.word('P3-S2','That','那一天的（指前述死亡事件发生日）',pos='art')
r.word('P3-S3','by','由于（引出加剧高温影响的因素）',pos='prep')
r.word('P3-S3','lack','缺乏；缺少',pos='n')
r.word('P4-S1','to','根据……调整（adapted to搭配）',pos='prep',occ=2)
r.word('P4-S2','on','针对；集中于（focus on搭配）',pos='prep')
r.word('P5-S1','be','处于某种状态（不需要复杂）',pos='v')
r.word('P5-S2','by','通过（绘图方法）',pos='prep')
r.word('P5-S2','at','考察（look at搭配）',pos='prep')
r.word('P5-S3','with','应对（cope with搭配）',pos='prep',occ=2)
r.word('P5-S4','which','这（指前述绘制出分布图的结果）',pos='pron',occ=1)
r.word('P5-S4','which','哪些（需要重点关注的社区）',pos='art',occ=2)
r.word('P6-S2','been','与has able构成一直能够的完成时',pos='v')
r.word('P6-S4','have','设定；拥有（某个目标）',pos='v')
r.word('P6-S4','is','是（联系行为与目标）',pos='v')
notes=['HAPs为同位简称，or表示即而非选择；完成进行时表近年持续增多。','alert在本句为通知的动词，不是预警名词；spell out为明确说明。','三个for分别表示例如、要求、治疗用途；break from work为暂停工作。','according to为报告出处，implementation为执行情况并非计划数量。','Many指许多计划、it指报告，lack为动词且并不表示所有计划无钱。','triggering为触发预警的修饰语，to表示按当地气候调整。','alone指单看白天气温，trigger为名词条件，might保留可能性。','as两处构成同等程度比较，highs为白天最高气温而非高地。','need此处是必要性名词；localized为因地制宜，保持归属研究者意见。','核对36与差1摄氏度的方向，shy of不是害羞；That限定当天。','by的两个原因由插入语隔开，湿度和缺少遮阴都加剧热影响。','model为示范性计划，adapt to local conditions表示可作调整而非获得许可。','focus responses on为重点应对高风险人群，most at risk后置说明。','Such回指绘图，does not否定的是需要复杂而非不需要绘图。','by looking at为方法，even a few为即使少数参数也能绘图。','that修饰住房，非正规住房应对热能力差；or给出两个可获支持的渠道。','第一个which概括绘图结果，第二个which询问哪些社区，需区别词义。','不只短期紧急响应还包括中长期降温，否定只限制just。','plant为种树动词，where为建议种植的位置，shade为遮阴。','retrofit是改造现有房屋，modify为修改建筑规定，两个不定式并列。','have为设定目标而非助动词，最低限度目标不等于无意义目标。']
for s,note in zip(r.ss,notes):r.checked(s['id'],note)
s=r.sentence('P4-S1');s['translation']=s['translation'].replace('并允许根据当地情况作出调整','并可根据当地情况作出调整')
print('Missing:',r.missing());r.save()
