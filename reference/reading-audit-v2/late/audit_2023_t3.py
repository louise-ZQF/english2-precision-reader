"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2023-T3')
r.lex('''
internet~internet~n=互联网
may~may~aux=可能
be~be~aux=构成进行时或被动结构
changing~change~v=改变
merely~merely~adv=仅仅
what~what~pron=所记住的内容
remember~remember~v=记住
capacity~capacity~n=能力
to~to~inf=不定式标记，连接动作
 do~do~v=做（指记忆）
so~so~adv=如此；这样（回指记忆）
suggests~suggest~v=认为；提出看法
columbia~Columbia~name=哥伦比亚（大学名称部分）
university~University~n=大学
psychology~psychology~n=心理学
professor~professor~n=教授
betsy~Betsy~name=贝齐
sparrow~Sparrow~name=斯帕罗
in~in~prep=在……中或所述时期
led~lead~v=主持；带领开展
study~study~n=研究
which~which~pron=关系词，指这项研究
participants~participant~n=参与者
were~be~aux=构成过去被动语态
asked~ask~v=要求
record~record~v=记录；输入
factoids~factoid~n=小知识；零碎事实
computer~computer~n=电脑
ostrich's~ostrich~n=鸵鸟的
eye~eye~n=眼睛
is~be~aux=构成现在进行时
bigger~big~a=更大的
than~than~conj=比
its~its~pron=它的（鸵鸟的）
brain~brain~n=大脑
for~for~prep=与example或instance构成例如
example~example~n=例子
half~half~n=一半
of~of~prep=……的（内容、所属或部分）
told~tell~v=被告知
information~information~n=信息
would~would~aux=会（过去转述或委婉推断）
erased~erase~v=删除
while~while~conj=而（对照另一组）
other~other~a=另一组的；其他的
it~it~pron=这些信息
saved~save~v=保存
guess~guess~v=猜一猜
latter~latter~a=后面提到的
 group~group~n=组
made~make~v=作出；付出
no~no~a=没有的
effort~effort~n=努力
recall~recall~v=回忆
when~when~conj=当……时
quizzed~quiz~v=被提问测试
on~on~prep=关于（被测试内容）
later~later~adv=后来
because~because~conj=因为
knew~know~v=知道
could~could~aux=能够
find~find~v=找到
computers~computer~n=电脑
same~same~a=相同的
was~be~aux=构成过去被动语态
both~both~adv=二者都（both…and）
folders~folder~n=电脑文件夹
stored~store~v=存放
didn't~do~aux=没有（did not）
but~but~conj=但是；而是
remembered~remember~v=记住了
how~how~adv=如何
words~word~n=说法（in other words表示换句话说）
human~human~a=人类的
memory~memory~n=记忆能力
deteriorating~deteriorate~v=退化；变差
adapting~adapt~v=适应
new~new~a=新的
communications~communication~n=通信
technology~technology~n=技术
says~say~v=说
very~very~adv=非常
practical~practical~a=实际的
way~way~n=意义；方式
becoming~become~v=成为
external~external~a=外置的
hard~hard~a=硬的（hard drive指硬盘）
drive~drive~n=硬盘
memories~memory~n=记忆
process~process~n=过程
known~know~v=被称作（known as）
as~as~prep=作为；称作
cognitive~cognitive~a=认知的
offloading~offloading~n=卸载；把任务交给外部工具
traditionally~traditionally~adv=过去；传统上
this~this~a=这种；当前的
role~role~n=角色；作用
fulfilled~fulfill~v=承担
by~by~prep=由（实施者）
data~data~n=数据
banks~bank~n=资料库
libraries~library~n=图书馆
humans~human~n=人
father~father~n=父亲
never~never~adv=从不
birthdays~birthday~n=生日
mother~mother~n=母亲
does~do~v=会记生日（代替remembers birthdays）
instance~instance~n=例子
some~some~pron=有些人
worry~worry~v=担心
that~that~conj=从句连接词，引出陈述内容
having~have~v=产生（影响）
destructive~destructive~a=破坏性的
effect~effect~n=影响
society~society~n=社会
sees~see~v=看到了
upside~upside~n=积极的一面
perhaps~perhaps~adv=也许
trend~trend~n=趋势
will~will~aux=将会
change~change~v=改变
approach~approach~n=方法；方式
learning~learn~n=学习
from~from~prep=从（转变起点）
focus~focus~n=关注重点
individual~individual~a=单个的；零散的
facts~fact~n=事实
memorization~memorization~n=记忆；背记
emphasis~emphasis~n=重视；侧重点
more~more~adv=更加
conceptual~conceptual~a=概念层面的
thinking~think~n=思考
something~something~pron=这种事；概念性思考
available~available~a=可以获得的
personally~personally~adv=就我个人而言
have~have~aux=构成现在完成时
seen~see~v=看出；认为有
all~all~adv=加强程度（all that much为那么多）
much~much~a=很多的；那么多的
intellectual~intellectual~a=智力与思考层面的
value~value~n=价值
memorizing~memorize~v=背记
things~thing~n=东西；内容
adding~add~v=补充说
haven't~have~aux=没有（have not）
lost~lose~v=丧失
ability~ability~n=能力
still~still~adv=还有（still other experts）
experts~expert~n=专家
say~say~v=认为；说
it's~it is~v=形式主语结构（it is）
too~too~adv=过于
soon~soon~adv=早；过早
understand~understand~v=了解
 affects~affect~v=影响
brains~brain~n=大脑
there~there~pron=存在句形式词，表示有
experimental~experimental~a=实验性的
evidence~evidence~n=证据
showing~show~v=表明
interferes~interfere~v=干扰（interfere with）
with~with~prep=干扰的对象（interfere with）
focus~focus~v=集中注意力
wrote~write~v=写道
psychologists~psychologist~n=心理学家
christopher~Christopher~name=克里斯托弗
chabris~Chabris~name=沙布里
daniel~Daniel~name=丹尼尔
j~J.~name=J（姓名中间首字母）
simons~Simons~name=西蒙斯
surfing~surf~v=浏览网络
web~web~n=互联网
exercised~exercise~v=锻炼
reading~read~n=阅读
did~do~v=锻炼了大脑（代前文exercised）
among~among~prep=在……人群中
computer-savvy~computer-savvy~a=熟悉电脑操作的
older~old~a=年长的
adults~adult~n=成年人
involving~involve~v=涉及；有……参与
at~at~prep=在（研究机构）
semel~Semel~name=塞梅尔
institute~Institute~n=研究所
neuroscience~Neuroscience~n=神经科学
behavior~Behavior~n=行为
california~California~name=加利福尼亚
los~Los~name=洛（Los Angeles地名部分）
angeles~Angeles~name=杉矶（Los Angeles地名部分）
costs~cost~n=代价；不利影响
associated~associate~v=相关联的
increased~increase~a=不断增强的
reliance~reliance~n=依赖
i'd~I would~aux=我会（I would缩写，委婉推断）
imagine~imagine~v=推想；认为
overall~overall~adv=总体而言
benefits~benefit~n=益处
are~be~aux=与going to构成将来结构
going~go~aux=与to构成将会
outweigh~outweigh~v=超过；大于
those~those~a=那些
observes~observe~v=指出
benjamin~Benjamin~name=本杰明
storm~Storm~name=斯托姆
seems~seem~v=似乎
pretty~pretty~adv=相当
clear~clear~a=明显的
better~good~a=更好的（for the better指向更好方向）
point~point~n=阶段；时点
don't~do~aux=不（do not）
know~know~v=知道
''')
r.word('P1-S2','is','是（比较眼睛与脑的大小）','be','v')
r.word('P1-S4','what','结果是什么（guess what固定问法）','what','pron')
r.word('P1-S5','on','在电脑中','on','prep',occ=2)
r.word('P1-S8','to','适应的对象（adapt to）','to','prep')
r.word('P2-S1','for','作为记忆的外置工具','for','prep')
r.word('P2-S4','this','将记忆任务交给外部工具的趋势','this','pron')
r.word('P2-S4','on','对……产生影响（effect on）','on','prep')
r.word('P2-S5','to','学习方法所针对的内容（approach to）','to','prep',occ=1)
r.word('P2-S5','to','学习重点转变的目标','to','prep',occ=2)
r.word('P2-S5','on','关注或强调的对象','on','prep')
r.word('P2-S5','is','是；能够获得的状态','be','v')
r.word('P2-S6','that','那么（all that much的程度词）','that','adv',occ=1)
r.word('P2-S6','do','记忆；背记（代前述行为）','do','v')
r.word('P2-S6','it','背记内容这件事','it','pron')
r.word('P3-S2','is','有；存在（there is）','be','v')
r.word('P3-S2','it','互联网','it','pron')
r.word('P3-S3','more','更多地（比较锻炼大脑的程度）','more','adv')
r.word('P3-S3','for','研究所所属研究领域（机构名称中的for）','for','prep')
r.word('P4-S1','be','存在；有（there may be）','be','v')
r.word('P4-S1','with','与……相关联（associated with）','with','prep')
r.word('P4-S1','on','所依赖的对象（reliance on）','on','prep')
r.word('P4-S1','have','不得不；倾向于（have to imagine）','have','v')
r.word('P4-S2','It','形式主语，后接记忆变化这一事实','it','pron',occ=1)
r.word('P4-S2','it','记忆能力','it','pron',occ=2)
r.word('P4-S2','for','向更好的方向（for the better）','for','prep')
r.word('P4-S3','At','在当前时点','at','prep')
r.sentence('P3-S3')['chunks'][0]['zh']='而上网锻炼了大脑，'
done(r,{
'P1-S1':'对比记住的内容与记忆能力，merely范围不扩大成只会伤害记忆。',
'P1-S2':'record为记录，factoids小知识，is bigger为系表比较而非进行时。',
'P1-S3':'前一组删除后一组保存，while为对比，it为信息。',
'P1-S4':'Guess what固定问法问结果，what不单问物品名称。',
'P1-S5':'latter为保存信息那组，on分别为被测试的内容和电脑存放位置。',
'P1-S6':'both包含信息及文件夹，it指信息，was stored in后置关系不丢。',
'P1-S7':'没有记信息却记路径，how to find为记得找到的方法。',
'P1-S8':'not deteriorating but adapting是否定退化转向适应，to为适应对象。',
'P2-S1':'external hard drive为外置硬盘比喻，cognitive offloading为认知卸载，不译成负载机器。',
'P2-S2':'banks为资料库而非银行，fulfilled为承担外部储存角色。',
'P2-S3':'does代替记生日，for instance为举例，父亲不记的原因是母亲会记。',
'P2-S4':'this回指外部记忆趋势，having effect为产生影响，upside为积极面。',
'P2-S5':'approach to为学习方式，from…to为重点转移，on作侧重对象，something指概念思考。',
'P2-S6':'all that much加强“那么多”程度，never不扩大成完全无价值，do it为记忆行为。',
'P3-S1':'too soon为时过早，尚不能判断而非判断互联网绝对有益或有害。',
'P3-S2':'无实验证据不等于证实绝无干扰，it为互联网，interfere with为干扰能力。',
'P3-S3':'样本为24位熟悉电脑的年长者，did代锻炼大脑；移除首块提前的更比较义。',
'P4-S1':'may与I’d have to imagine保留推断，costs为代价，outweigh比较总体利弊。',
'P4-S2':'首It形式主语第二it为记忆，问是否变好不回答已经变好。',
'P4-S3':'at this point为目前认识阶段，不知道的态度完整保留。'})
