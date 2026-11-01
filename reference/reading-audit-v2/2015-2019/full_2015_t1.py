# -*- coding: utf-8 -*-
from middle_full_review import *
r=make('2015-T1')
lex(r,'''new/a=新的;study/n=研究;suggests@suggest/v=表明;contrary/a=相反的;surveys@survey/n=调查;actually/adv=实际上;stressed@stressed/a=感到压力大的;home/n=家;work/n=工作;researchers@researcher/n=研究人员;measured@measure/v=测量;people's@person/n=人们的（所有格）;cortisol/n=皮质醇;stress/n=压力;marker/n=指标;found@find/v=发现;higher@high/a=更高的;sup p osed/a=应当的;place/n=地方;refuge/n=庇护所；避风港;further/adv=进一步；更;contradicting@contradict/v=与……相矛盾;conventional/a=普遍接受的;wisdom/n=常识；普遍看法;women@woman/n=女性;well/adv=同样地（as well as结构中）;men@man/n=男性;lower@low/a=更低的;levels@level/n=水平;writes@write/v=写道;one/num=一个；一位;sarah@Sarah/name=萨拉（人名）;damaske@Damaske/name=达马斯克（姓氏）;fact/n=事实（in fact整体为“事实上”）;say/v=说；表示;feel/v=感觉;better@good/a=更好的;notes@note/v=指出;report/v=自述；报告;happier@happy/a=更快乐的;surprise/n=意外的事；意外发现;findings@finding/n=研究结果;hold/v=成立（hold true）;true/a=成立的；符合事实的;children@child/n=孩子;nonparents@nonparent/n=没有子女的人;outside/prep=在……之外;health/n=健康状况;doesn't@do/aux=不（does not缩写，构成否定）;measure/v=衡量；考察;doing@do/v=做；从事;they're@they be/aux=他们正在／他们是（they are缩写）;household/a=家务的; brought@bring/v=带来；带回;office/n=办公室；文中也比喻家务工作场所;end/n=结束;workday/n=工作日;time/n=时候；时间;kick/v=放松（kick back整体）;back/adv=放松地（kick back整体）;stay/v=留在；待在;get/v=有机会（get to）;leave/v=离开;playing@play/v=忙于（play catch-up整体）;catch/n=追赶（catch-up整体）;up/adv=赶上（catch-up整体）;tasks@task/n=任务；家务事;blurring@blur/n=界限的模糊;roles@role/n=角色；职责;front/n=家庭层面（home front）;lags@lag/v=落后;behind/prep=落后于;workplace/n=工作场所;making@make/v=作出;adjustments@adjustment/n=调整;working@work/a=有工作的；在职的;it's@it be/pron=这是；这件事是（it is缩写）;surprising/a=令人惊讶的;gender/n=性别;thing/n=事情；问题;pretty/adv=相当；几乎（pretty much整体为基本上）;know/v=知道;money/n=钱;order/n=为达某目的（in order to结构）;draw/v=获取；领取;income/n=收入;bargain/n=交换；交易安排;pure/a=单纯明了的;employee/n=雇员;puts@put/v=投入（put in）;hours@hour/n=小时;physical/a=体力的;mental/a=脑力的;labor/n=劳动;draws@draw/v=获取；领取;out/adv=取出（draw out整体指领取）;life-sustaining/a=维持生计的;moola/n=钱（口语）;however/adv=然而;clarity/n=清晰明确;rare/a=罕见的;division/n=分工;clinically/adv=冷静客观地；不带感情地;methodically/adv=有条理地;laid@lay/v=安排（lay out）;lot/n=大量（a lot of）;done@do/v=完成;inadequate/a=不足的;rewards@reward/n=回报；报酬;colleagues@colleague/n=同事（比喻家人）;family/n=家人；家庭;clear/a=明确的;need/v=需要;talked@talk/v=劝说（talk into）;teenagers@teenager/n=青少年;threatened@threaten/v=威胁;complete/a=全部的；彻底的;removal/n=移除；收走;electronic/a=电子的;devices@device/n=设备;plus/adv=再说；此外;cannot@can/aux=不能;fire/v=解雇;go/v=去；回;apparently/adv=看起来；似乎;infinite/a=无穷无尽的;co-workers@co-worker/n=同事（这里指家人）;harder@hard/a=更困难的;motivate/v=调动……积极性'''.replace('sup p osed','supposed'))
# Function words and repeated words are checked at each use, rather than assigned a dictionary bag of senses.
r.word('P1-S1','to','与……相比／相反（contrary to）',pos='prep');r.word('P1-S1','are','系动词，连接人们与“更有压力”的状态',lemma='be',pos='v')
r.word('P1-S2','is','是',lemma='be',pos='v');r.word('P1-S2','were','处在（工作或家中的状态）',lemma='be',pos='v');r.word('P1-S2','what','本应是庇护所的那个地方（指家）',pos='pron');r.word('P1-S2','be','成为；是（supposed to be中）',pos='v');r.word('P1-S2','it','皮质醇水平',pos='pron');r.word('P1-S2','higher','更高的（家中高于工作时）',lemma='high',pos='a')
r.word('P2-S1','as','和……一样（as well as）',pos='conj');r.word('P2-S1','have','有；承受着',pos='v');r.word('P2-S1','of','……的（限定压力水平或研究者之一）',pos='prep')
r.word('P2-S2','in','在in fact中构成“事实上”',pos='prep')
r.word('P2-S3','it','强调句形式主语，不单译',pos='pron');r.word('P2-S3','who','强调句连接词，突出男性这一主体',pos='pron');r.word('P2-S3','being','感到；处于快乐状态',lemma='be',pos='v')
r.word('P2-S4','that','引出表语内容“结论成立”',pos='conj');r.word('P2-S4','for','对……而言（说明结论适用对象）',pos='prep');r.word('P2-S4','so','如此（指结论在该人群更明显）',pos='adv');r.word('P2-S4','more','更加明显',pos='adv')
r.word('P2-S5','have','拥有；具有',pos='v');r.word('P2-S5','work','工作（动词）',pos='v')
r.word('P3-S1','what','所……的方面（研究未衡量的内容）',pos='pron');r.word('P3-S1','whether','是否',pos='conj',occ=1);r.word('P3-S1','whether','不论是……还是……（whether...or）',pos='conj',occ=2);r.word('P3-S1','are','助动词，与doing构成进行时',lemma='be',pos='aux');r.word('P3-S1',"they're",'they are的缩写；他们处于家中',lemma='they be',pos='v')
for sid in ['P3-S2','P3-S3','P3-S4']:r.word(sid,'for','对……来说',pos='prep')
r.word('P3-S4','and','而且；转向另一类女性',pos='conj');r.word('P3-S4','work','工作（动词）',pos='v');r.word('P3-S4','are','助动词，与playing构成进行时',lemma='be',pos='aux')
r.word('P3-S5','with','随着；由于（引出背景原因）',pos='prep');r.word('P3-S5','well','远远地（强调落后程度）',pos='adv');r.word('P3-S5','in','在……方面',pos='prep');r.word('P3-S5','for','为……作调整',pos='prep')
r.word('P4-S2','much','很大程度地（pretty much整体为基本上）',pos='adv');r.word('P4-S2',"they're",'they are的缩写；构成be supposed to“应该”',lemma='they be',pos='aux');r.word('P4-S2','be','助动词，与doing构成进行时',pos='aux');r.word('P4-S2','working','工作',lemma='work',pos='v');r.word('P4-S2','have','必须（have to）',pos='aux');r.word('P4-S2','do','做；完成任务',pos='v');r.word('P4-S2','in','在in order to中表示目的',pos='prep')
r.word('P4-S3','in','投入到……（put in）',pos='adv');r.word('P4-S3','or','或者（体力与脑力劳动两类）',pos='conj')
r.word('P5-S1','on','在……方面（on the home front）',pos='prep');r.word('P5-S1','have','具有；拥有',pos='v')
r.word('P5-S2','household','家庭；一户人家',pos='n');r.word('P5-S2','in','在……之中（in which指在这种家庭中）',pos='prep');r.word('P5-S2','is','被动语态助动词，与laid out连用',lemma='be',pos='aux',occ=2);r.word('P5-S2','so','如此（说明安排的程度）',pos='adv')
r.word('P5-S3','there','存在结构there be，不单译',pos='pron');r.word('P5-S3','are','有；存在（there be）',lemma='be',pos='v');r.word('P5-S3','be','助动词，to be done表示待完成',pos='aux');r.word('P5-S3','for','对于这些任务而言',pos='prep')
r.word('P5-S4','have','有；得到',pos='v');r.word('P5-S4','for','因……劳动而获得的报酬',pos='prep');r.word('P5-S4','be','被动语态助动词；得被劝说',pos='aux');r.word('P5-S4','into','说服……去做（talk into）',pos='prep');r.word('P5-S4','it','做家务这件事',pos='pron');r.word('P5-S4','or','或者；对于青少年则需要另一办法',pos='conj');r.word('P5-S4',"they're",'they are的缩写；他们是',lemma='they be',pos='v');r.word('P5-S4','with','以没收设备来威胁（threaten with）',pos='prep')
r.word('P5-S5',"they're",'they are的缩写；他们是',lemma='they be',pos='v');r.word('P5-S7','from','从家这个工作场所离开',pos='prep')
r.word('P6-S1','so','所以',pos='conj');r.word('P6-S2','only','和not组成“不仅”',pos='adv');r.word('P6-S2','much','……得多（强调更难）',pos='adv')
checks(r,'''比较方向为家中压力高于工作场所，contrary to与旧调查相反。
皮质醇是压力指标；which指cortisol，it指其水平，refuge指家。
男女都在工作时压力较低；as well as不排除女性。
女性自述在工作时感觉更好，非统计因果结论。
强调主体为男性，不能反译为女性在家更快乐。
两类家庭均适用，无子女者结果更明显，more so所指明确。
who限定外出工作的人，health为健康状况而非医疗服务。
第一个whether是是否，第二个whether...or是不论哪种工作。
对男性的下班放松作概括，kick back不能按踢回直译。
家庭被比作办公室，never说明全职家庭劳动没有真正下班。
catch-up指补做积压家务，不重复翻译追赶和补做。
with引出两个背景原因，well强调家庭调整远落后于职场。
not just保留并非仅是性别问题的转折。
what是应做的内容，have to表必须，draw an income是获取收入。
劳动换报酬的交换关系明确，moola为口语中的钱。
no否定拥有，have块不能提前译出否定造成重复。
Rare倒装突出少见，household为家庭，is laid out为被动。
there be表示存在，for most指多数任务而非大多数人。
家人作为同事比喻，talk into为劝做，removal为收走设备。
Plus补充家人身份这一约束，而非数学加号。
fire是解雇，不是开火或燃烧。
go home from home为文字游戏，指出无法从家务中下班。
So承接前述原因，stressed为感到压力大的。
not only倒装保留两项困难，much修饰比较级harder。''')
r.notes=['逐词重审：每个可点击英文词均有定位义项；介词、助动词、强调结构及家务比喻另按句核定。']
save(r)
