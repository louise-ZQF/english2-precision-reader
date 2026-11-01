"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2024-T1')
r.lex('''
in~in~prep=在……中
her~her~det=她的，指科伊尔
new~new~adj=新的
book~book~n=书
cogs~cog~n=齿轮（书名的一部分）
monsters~monster~n=怪物（书名的一部分）
what~what~pron=什么（书名中的问句）
economics~economics~n=经济学
is~be~v=是
it~it~pron=它，指经济学
should~should~modal=应当
be~be~v=是
 diane~Diane~propn=黛安娜（人名）
coyle~Coyle~propn=科伊尔（经济学家姓氏）
economist~economist~n=经济学家
at~at~prep=在（任职机构）
cambridge~Cambridge~propn=剑桥
university~university~n=大学
argues~argue~v=提出观点；主张
that~that~conj=引出具体观点或结论
digital~digital~adj=数字技术的
economy~economy~n=经济；经济体系
requires~require~v=需要；要求
ways~way~n=方式
of~of~prep=的（连接所属或修饰关系）
thinking~think~n=思考
about~about~prep=关于；对于
progress~progress~n=进步
whatever~whatever~pron=无论……什么（让步）
mean~mean~v=指的是；理解为
by~by~prep=说到……时（mean by）
growing~grow~v=增长
things~thing~n=事情；生活状况
getting~get~v=变得
better~good~adj=更好的
gains~gain~n=经济发展成果；收益
will~will~modal=会；将
have~have~v=必须（have to）
to~to~inf=不定式标记
more~more~adv=更加
evenly~evenly~adv=公平地；均匀地
shared~share~v=分享；分配
than~than~conj=比（引出比较对象）
recent~recent~adj=近来的
past~past~n=过去一段时期
writes~write~v=写道
tech~tech~n=科技行业
millionaires~millionaire~n=百万富翁
billionaires~billionaire~n=亿万富翁
gig~gig~n=零工（修饰劳动者）
workers~worker~n=劳动者
with~with~prep=伴随；其中有……（补充状态）
middle-income~middle-income~adj=中等收入的
jobs~job~n=工作；就业岗位
undercut~undercut~v=削弱；冲击
 automation~automation~n=自动化
politically~politically~adv=从政治上看
sustainable~sustainable~adj=能够长期维持的
improving~improve~v=提高；改善
living~living~n=生活（living standards）
standards~standard~n=水平（living standards）
increasing~increase~v=增加；提高
prosperity~prosperity~n=富足；繁荣
for~for~prep=为了；使……受益
people~person~n=人们
require~require~v=需要
greater~great~adj=更大程度的
use~use~n=采用；使用
technologies~technology~n=技术
boost~boost~v=提高；促进
productivity~productivity~n=生产率
various~various~adj=不同的；各种各样的
sectors~sector~n=经济行业
including~including~prep=包括
health~health~n=健康（health care构成医疗保健）
care~care~n=护理；照护（health care）
construction~construction~n=建筑业
says~say~v=说；表示
but~but~conj=但；而
can't~cannot~modal=不能
expected~expect~v=指望；期待
embrace~embrace~v=接受；支持
changes~change~n=变化
if~if~conj=如果
they're~they are~pron+aux=他们正在，指人们（与seeing构成进行时）
seeing~see~v=看到
benefits~benefit~n=好处；收益
just~just~adv=只是；仅仅
good~good~adj=好的
being~be~aux=与destroyed构成被动语态
destroyed~destroy~v=摧毁；使消失
interview~interview~n=采访
said~say~v=表示；说
fears~fear~v=担心
tech's~tech~n=科技的（所有格）
inequality~inequality~n=不平等
problem~problem~n=问题
could~could~modal=可能
roadblock~roadblock~n=障碍
 deploying~deploy~v=部署；投入应用
ai~AI~abbr=人工智能
we're~we are~pron+aux=我们正在（与talking构成进行时）
talking~talk~v=谈论
disruption~disruption~n=颠覆性变化；对既有模式的冲击
these~these~pron=这些，指人工智能等技术
are~be~v=是
transformative~transformative~adj=带来深刻变革的
change~change~v=改变
spend~spend~v=使用；花费（时间）
time~time~n=时间
every~every~det=每一
day~day~n=天
business~business~n=商业（修饰模式）
models~model~n=模式
succeed~succeed~v=成功
make~make~v=作出；实现（改变）
such~such~det=这样的
tremendous~tremendous~adj=巨大的
adds~add~v=补充说
need~need~v=需要
social~social~adj=社会的
buy-in~buy-in~n=认同；支持
instead~instead~adv=相反
resentment~resentment~n=不满；怨愤
simmering~simmer~v=暗中酝酿；积聚
among~among~prep=在……人群中
many~many~pron=许多人
as~as~conj=因为
perceived~perceive~v=被认为；被视为
go~go~v=流向
elites~elite~n=精英群体
handful~handful~n=少量（a handful of）
prosperous~prosperous~adj=繁荣的
cities~city~n=城市
according~accord~v=与to构成“根据”
brookings~Brookings~propn=布鲁金斯（学会名称）
institution~institution~n=学会（布鲁金斯学会名称组成部分）
short~short~adj=短的；数量不多的
list~list~n=名单
 eight~eight~num=八
american~American~adj=美国的
included~include~v=包括
san~San~propn=圣（城市名称组成部分）
francisco~Francisco~propn=弗朗西斯科（San Francisco即旧金山）
jose~Jose~propn=何塞（San Jose即圣何塞）
boston~Boston~propn=波士顿
seattle~Seattle~propn=西雅图
had~have~v=拥有
roughly~roughly~adv=大约
all~all~det=全部的
particularly~particularly~adv=尤其
concentrated~concentrated~adj=集中的
brookings's~Brookings~propn=布鲁金斯学会的（所有格）
mark~Mark~propn=马克（人名）
muro~Muro~propn=穆罗（姓氏）
sifan~Sifan~propn=思凡（人名）
liu~Liu~propn=刘（姓氏）
estimate~estimate~v=估计
account~account~v=占（比例；account for）
two-thirds~two-thirds~num=三分之二
assets~asset~n=资产
capabilities~capability~n=能力
united~United~propn=United States名称的一部分
states~States~propn=United States即美国
dominance~dominance~n=主导地位
few~few~det=少数几个
invention~invention~n=发明
commercialization~commercialization~n=商业化
means~mean~v=意味着
geographical~geographical~adj=地理区域之间的
disparities~disparity~n=差距
wealth~wealth~n=财富
continue~continue~v=继续
soar~soar~v=大幅上升；迅速扩大
only~only~adv=仅仅（not only为不仅）
this~this~pron=这种情况，指地区财富差距扩大
foster~foster~v=滋生；促成
political~political~adj=政治的
unrest~unrest~n=动荡
suggests~suggest~v=指出；提示
hold~hold~v=阻碍（hold back）
back~back~adv=与hold构成“阻碍”
sorts~sort~n=种类
needed~need~v=需要
regional~regional~adj=地区的
economies~economy~n=经济；经济体
grow~grow~v=增长；发展
part~part~n=一部分
solution~solution~n=解决办法
lie~lie~v=在于（lie in）
somehow~somehow~adv=设法；用某种办法
loosening~loosen~v=减弱；松动
stranglehold~stranglehold~n=牢牢的控制
big~big~adj=大型的（Big Tech指科技巨头）
has~have~v=拥有
on~on~prep=对……的（控制）
defining~define~v=制定；确定
agenda~agenda~n=议程；发展方向
likely~likely~adv=很可能
take~take~v=需要
increased~increased~adj=增加了的
federal~federal~adj=联邦政府的
funding~funding~n=资金；拨款
research~research~n=研究
independent~independent~adj=独立的；不受控制的
giants~giant~n=巨头（指大型科技公司）
immediate~immediate~adj=直接的；眼下可做的
response~response~n=应对办法
broaden~broaden~v=拓宽
imaginations~imagination~n=想象力
conceive~conceive~v=构想（conceive of）
don't~do not~aux=不（否定助动词）
simply~simply~adv=仅仅
replace~replace~v=取代
expand~expand~v=扩大
opportunities~opportunity~n=机会
different~different~adj=不同的
parts~part~n=地区；部分
country~country~n=国家；这里指美国
most~most~adv=最
like~like~prep=例如
education~education~n=教育
manufacturing~manufacturing~n=制造业
''')
r.word('P1-S1','that','引出argues主张的内容','that','conj')
r.word('P1-S2','be','与shared构成被动语态','be','aux')
r.word('P1-S3','by','由（指出冲击来源）','by','prep')
r.word('P1-S3','be','处于可持续的状态','be','v')
r.word('P2-S1','for','使……受益；让更多人……','for','prep')
r.word('P2-S1','more','更多的（人）','more','det')
r.word('P2-S2','be','与expected构成被动语态','be','aux')
r.word('P3-S1','to','对于……是障碍（roadblock to）','to','prep')
r.word('P3-S3','that','引导定语从句，指变革性技术','that','pron',occ=1)
r.word('P3-S3','that','引导定语从句，仍指变革性技术','that','pron',occ=2)
r.word('P3-S3','that','引导定语从句，指商业模式','that','pron',occ=3)
r.word('P4-S1','is','与simmering构成现在进行时','be','aux')
r.word('P4-S1','are','与perceived构成被动语态','be','aux')
r.word('P4-S1','to','向；到（收益流向精英）','to','prep',occ=2)
r.word('P5-S1','to','与according构成“根据”','to','prep')
r.word('P5-S1','that','引导定语从句，指八座城市','that','pron')
r.word('P5-S1','by','截至；到……时为止','by','prep')
r.word('P5-S2','for','与account构成“占比例”','for','prep')
r.word('P6-S2','as','正如（引出科伊尔的观点）','as','conj')
r.word('P6-S2','it','它，指地区财富差距扩大','it','pron')
r.word('P6-S2','for','供……；让……（不定式的逻辑主语标记）','for','prep')
r.word('P7-S1','in','在于（lie in）','in','prep')
r.word('P7-S1','that','引导定语从句，指牢牢的控制','that','pron')
r.word('P7-S2','that','这，指减弱科技巨头控制的做法','that','pron')
r.word('P7-S2','for','用于；支持','for','prep')
r.word('P7-S2','of','与independent of构成“独立于”','of','prep')
r.word('P8-S1','more','更（修饰直接）','more','adv')
r.word('P8-S1','of','与conceive of构成“构想”','of','prep',occ=1)
r.word('P8-S1','that','引导定语从句，指人工智能技术','that','pron',occ=1)
r.word('P8-S1','that','引导定语从句，指相关行业','that','pron',occ=2)
r.word('P8-S1','care','关心（care about）','care','v',occ=1)
r.word('P8-S1','about','关心的对象（care about）','about','prep')
r.sentence('P1-S3')['translation']='“如果一种经济中，一边是科技百万富翁或亿万富翁，一边是零工劳动者，而中等收入岗位又受到自动化冲击，这种经济在政治上将难以持续。”'
notes={
'P1-S1':'分清书名两个what疑问、同位语经济学家身份、主句that内容；economics单数经济学。',
'P1-S2':'两个by为mean by含义对象，have to必须且be shared被动；evenly分配更公平非增长更均匀。',
'P1-S3':'原句无only，删译文擅加“只有”，保留两端收入结构与中层岗位冲击及政治不可持续。',
'P2-S1':'greater use名词、more people数量，to boost目的，prosperity富足不是单纯GDP。',
'P2-S2':'两if解释相同不获益情形，being destroyed被动，不能指望接受不等于禁止变化。',
'P3-S1':'fears/could保持担忧与可能，roadblock to中to介词后跟deploying。',
'P3-S2':'we are进行时，disruption指技术对经济模式冲击，不是普通混乱中断。',
'P3-S3':'三个that前两指技术、最后指模式，时间使用和何种商业模式成功两方面变化。',
'P3-S4':'buy-in社会认同非买入，to make目标，she adds为插入说话人。',
'P4-S1':'is simmering进行、are perceived被动，as因果，many人群，to go与go to两个to区分。',
'P5-S1':'roughly修饰38%，by截至2019，had拥有非完成助动词，八城中的四个例子不漏。',
'P5-S2':'AI缩略语、two-thirds复合数量，account for占比，刘思凡人名与研究机构归属。',
'P6-S1':'means动词，disparities地区财富差距，will继续扩大的推断非历史既成数据。',
'P6-S2':'not only倒装与but并列，it回指差距扩大，as插入比较，needed后置修饰技术。',
'P7-S1':'lie in在于，has拥有，on表示控制对象，that所指stranglehold，未把科技巨头当词组添加。',
'P7-S2':'That指前句减弱控制，take需要，independent of修饰research非联邦资金。',
'P8-S1':'两个to分别表语方式及目的；dont simply but非完全排除替代岗位，care动词与health care名词分开。'}
r.word('P6-S1','in','在……领域（发明和商业化）','in','prep',occ=1)
r.word('P6-S1','in','在……方面（财富差距）','in','prep',occ=2)
done(r,notes)
