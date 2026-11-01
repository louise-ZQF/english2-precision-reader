"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2020-T4')
r.lex('''
now~now~adv=现在；如今
that~that~conj=与now构成既然；随着这一事实
members~member~n=成员
of~of~prep=……的（所属或内容）
generation~generation~n=一代人
z~Z~name=Z（Z世代名称的一部分）
are~be~aux=构成正在进行的动作
graduating~graduate~v=毕业
college~college~n=大学
this~this~a=这个；本次
spring~spring~n=春季
most~much~adv=最
commonly-accepted~commonly-accepted~a=普遍接受的
definition~definition~n=定义
says~say~v=说明；表述
was~be~aux=与born构成出生的表达
born~bear~v=出生（be born）
after~after~prep=在……之后
give~give~v=give or take的一部分，表示上下相差
 take~take~v=give or take的一部分，表示上下相差
year~year~n=年
attention~attention~n=关注
has~have~aux=构成现在完成时
been~be~aux=与rising构成完成进行时
rising~rise~v=增加
steadily~steadily~adv=持续稳定地
in~in~prep=在……期间或范围内
recent~recent~a=最近的
weeks~week~n=周
gen~generation~n=一代人（generation的缩写）
zs~Z~name=Z世代成员（Z的复数指人）
about~about~a=即将（be about to搭配）
to~to~inf=不定式标记，连接动作
hit~hit~v=走上；进入（hit the streets）
streets~street~n=街道（外出求职的比喻）
looking~look~v=寻找（与for连用）
for~for~prep=寻找、安排或评价所针对的对象
work~work~n=工作
labor~labor~n=劳动力
market~market~n=市场
that's~that is~v=那个市场是（that is的缩写）
tighter~tight~a=劳动力供给更紧张的
than~than~conj=比
it's~it has~aux=它已经（it has的缩写）
decades~decade~n=十年；几十年
employers~employer~n=雇主
planning~plan~v=计划
on~on~prep=plan on的一部分，表示计划做
hiring~hire~v=招聘
percent~percent~n=百分比
more~more~a=更多的
new~new~a=新毕业的
graduates~graduate~n=毕业生
jobs~job~n=职位；工作
u.s.~U.S.~name=美国
last~last~a=上一个的；去年
according~according~prep=与to连用，表示根据
survey~survey~n=调查
conducted~conduct~v=开展
by~by~prep=由（引出实施者）
national~National~a=全国性的（机构名称部分）
association~association~n=协会
colleges~college~n=大学
 everybody~everybody~pron=每个人；人人
wants~want~v=想要
know~know~v=知道
how~how~adv=如何；有什么不同
people~people~n=人们
who~who~pron=关系词，指前面所述的人
will~will~aux=将会
soon~soon~adv=很快
inhabit~inhabit~v=进驻；占用
those~those~a=那些
empty~empty~a=空置的
office~office~n=办公室
cubicles~cubicle~n=办公隔间
differ~differ~v=有差别
from~from~prep=与……相比；来自
came~come~v=先前来到（这里指前辈）
before~before~prep=在……之前
if~if~conj=如果说（引出对比）
entitled~entitled~a=自认为理应享受优待的
is~be~v=是
common~common~a=常用的；常见的
adjective~adjective~n=形容词
fairly~fairly~adv=公平地；公允地
applied~apply~v=用来形容；加诸于
millennials~millennial~n=千禧一代成员
between~between~prep=在……两者之间
catchwords~catchword~n=概括性标签；常用关键词
practical~practical~a=务实的
cautious~cautious~a=谨慎的
career~career~n=职业
counselors~counselor~n=咨询顾问
experts~expert~n=专家
study~study~v=研究
clear-eyed~clear-eyed~a=头脑清醒、认清现实的
economic~economic~a=经济方面的
pragmatists~pragmatist~n=务实主义者
despite~despite~prep=尽管
into~into~prep=进入；正逢某种环境
best~good~a=最好的
economy~economy~n=经济；经济形势
past~past~a=过去的
years~year~n=年
what~what~pron=是什么样子（引导know的内容）
train~train~n=火车（train wreck比喻崩溃）
wreck~wreck~n=严重事故；崩溃
looks~look~v=看起来
like~like~prep=像……样子
were~be~v=处于所述状态
impressionable~impressionable~a=容易受经历影响的
kids~kid~n=孩子
during~during~prep=在……期间
crash~crash~n=经济崩溃；金融危机
when~when~conj=当时（指2008年危机时）
many~many~a=许多
parents~parent~n=父母
lost~lose~v=失去
life~life~n=一生
savings~saving~n=积蓄
both~both~pron=两者（工作与积蓄）
aren't~be~v=并不（are not）
interested~interested~a=感兴趣的；愿意的
taking~take~v=承担（take chances指冒险）
any~any~a=任何的
chances~chance~n=风险（take chances搭配）
booming~booming~a=繁荣的；快速增长的
seems~seem~v=似乎
have~have~aux=构成完成时
done~do~v=起作用（done little指作用不大）
little~little~pron=很少；不多的作用
assuage~assuage~v=缓解
underlying~underlying~a=深层的
 generational~generational~a=属于这一代人的
sense~sense~n=感觉
anxious~anxious~a=焦虑的
urgency~urgency~n=紧迫感
especially~especially~adv=尤其
 debt~debt~n=债务
loan~loan~n=贷款
balances~balance~n=未偿贷款余额
stand~stand~v=达到；处于某数值
at~at~prep=达到所述数值
record~record~a=创纪录的
trillion~trillion~num=万亿
federal~Federal~a=联邦的（Federal Reserve机构名部分）
reserve~Reserve~name=储备（Federal Reserve指美联储）
one~one~num=一；一个
accenture~Accenture~name=埃森哲（咨询公司）
found~find~v=发现
seniors~senior~n=大学毕业班学生
chose~choose~v=选择
major~major~n=大学专业
with~with~prep=带着；考虑到
job~job~n=工作
mind~mind~n=心中（with…in mind表示考虑）
university~University~n=大学
georgia~Georgia~name=佐治亚
students~student~n=学生
meanwhile~meanwhile~adv=与此同时
desirable~desirable~a=值得向往的；最希望具备的
trait~trait~n=特点
future~future~a=未来的
employer~employer~n=雇主
ability~ability~n=能力
 offer~offer~v=提供
secure~secure~a=稳定有保障的
employment~employment~n=就业；工作
followed~follow~v=随后是；其次是
professional~professional~a=职业上的
development~development~n=发展
training~training~n=培训
then~then~adv=然后；再次
inspiring~inspiring~a=鼓舞人心的
purpose~purpose~n=工作目标；事业意义
security~security~n=保障
stability~stability~n=稳定性
second~second~num=第二
important~important~a=重要的
goal~goal~n=目标
work-life~work-life~a=工作与生活的
balance~balance~n=平衡
number~number~n=名次（number one指第一位）
being~be~aux=构成dedicated的状态表达
 dedicated~dedicated~a=献身于、投入某项事业的
cause~cause~n=事业
feel~feel~v=感到
good~good~a=良好的；有满足感的
serving~serve~v=为……服务
greater~great~a=更广泛的
good~good~n=公共利益（the greater good）
big~big~a=很大的
change~change~n=变化
previous~previous~a=上一代的；先前的
wanted~want~v=想要
flexibility~flexibility~n=灵活性
lives~life~n=生活
notes~note~v=指出
tanya~Tanya~name=坦娅（姓名）
michelsen~Michelsen~name=米歇尔森（姓氏）
associate~Associate~a=副的（职称修饰语）
director~Director~n=总监
youthsight~YouthSight~name=YouthSight（英国市场研究机构名）
uk-based~UK-based~a=总部位于英国的
brand~brand~n=品牌
manager~manager~n=管理机构（本文指YouthSight）
conducts~conduct~v=开展
regular~regular~a=定期的
day~day~n=天
60-day~60-day~a=为期60天的
surveys~survey~n=调查
british~British~a=英国的
youth~youth~n=年轻人
findings~finding~n=研究发现
might~might~aux=可能
just~just~adv=同样地；恰恰
as~as~adv=同样地（as well搭配）
well~well~adv=也；同样（as well搭配）
apply~apply~v=适用
american~American~a=美国的
certainty~certainty~n=确定性
because~because~conj=由于（because of搭配）
rise~rise~n=兴起
gig~gig~n=临时短期工作（gig economy指零工经济）
troubles~trouble~n=困难
seeing~see~v=看清；预见
financial~financial~a=财务方面的
quite~quite~adv=相当；很
risk~risk~n=风险
averse~averse~a=不愿面对、倾向规避的
''')
r.word('P1-S1','give','give or take中的固定用法，表示上下相差','give','v')
r.word('P1-S1','or','与give、take合成上下相差的习语','or','conj')
r.word('P1-S1','been','构成完成进行时','be','aux')
r.word('P1-S2','been','一直处于所述状态','be','v')
r.word('P1-S3','about','大约','about','adv')
r.word('P1-S3','to','根据（according to）','to','prep')
r.word('P1-S3','for','为了填补的岗位','for','prep')
r.word('P2-S1','are','联系主语与务实谨慎的特点','be','v')
r.word('P2-S1','to','把形容词用于描述的对象','to','prep')
r.word('P2-S1','or','是否；不论公允与否','or','conj')
r.word('P2-S2','to','据……说（according to）','to','prep')
r.word('P2-S2','are','是（联系主语和务实主义者）','be','v')
r.word('P2-S4','or','或者（连接失业和积蓄损失两种情况）','or','conj')
r.word('P2-S6','have','拥有；背负（债务）','have','v',occ=2)
r.word('P2-S7','to','根据（according to）','to','prep')
r.word('P3-S2','was','是（联系特点与能力）','be','v')
r.word('P3-S3','was','是（说明目标排名）','be','v')
r.word('P3-S3','or','或者说；也就是（近义表述）','or','conj',occ=1)
r.word('P3-S3','to','投身于的对象（dedicated to）','to','prep',occ=1)
r.word('P3-S3','good','满足的；良好的','good','a',occ=1)
r.word('P3-S3','about','对于；因为所做之事','about','prep')
r.word('P4-S1',"That's",'这是一项变化（that is）','that is','v')
r.word('P4-S2','to','适用于的对象','to','prep')
r.word('P4-S3','for','寻找、希望获得的对象（look for）','for','prep')
r.word('P4-S4','have','有；面临（困难）','have','v')
r.word('P4-S4','are','处于所述风险态度','be','v')
r.word('P2-S6','for','对于；对……而言','for','prep')
r.word('P3-S2','by','排在其后的内容（followed by）','by','prep')
r.word('P3-S3','by','排在其后的内容（followed by）','by','prep')
r.sentence('P1-S3')['chunks'][0]['zh']='而雇主正计划招聘，'
r.sentence('P1-S3')['chunks'][1]['zh']='今年为美国岗位招聘的新毕业生比去年多约17%，'
r.sentence('P2-S1')['chunks'][0]['zh']='如果说，“自认为理应受到优待”是最常用的形容词，'
r.sentence('P2-S1')['chunks'][1]['zh']='不论是否公允，被用来形容千禧一代（1981—1995年出生），'
r.sentence('P4-S1')['chunks']=chunks(r,'P4-S1','a big change','这是，|相较上一代很大的变化。')
s=r.sentence('P4-S2');s['translation']=s['translation'].replace('以60天为周期的调查','为期60天的调查');s['chunks'][2]['zh']=s['chunks'][2]['zh'].replace('以60天为周期的调查','为期60天的调查')
done(r,{
'P1-S1':'Now that为背景事实，1995年前后一年的浮动为定义补充，不是整段关注延续一年。',
'P1-S2':'it’s为it has而非it is，tighter指缺劳动力，街道是外出求职的比喻。',
'P1-S3':'17%是较去年多招新毕业生，改块避免把美国今年提前译入planning。',
'P1-S4':'先前来到的人为前辈，两个will分别修饰进驻与差异的将来，不是房屋居住。',
'P2-S1':'entitled为自认为应享优待的形容词，改块让千禧代年份落回对应英文。',
'P2-S2':'pragmatists为人群名词，clear-eyed指清醒认识现实，them为Z世代。',
'P2-S3':'经济train wreck比喻崩溃，与毕业时好经济形成让步对照。',
'P2-S4':'2008为成长记忆，both指失业与损失积蓄二者，不添同时的时间含义。',
'P2-S5':'take chances为冒险，aren’t否定意愿，不是没有机会可得。',
'P2-S6':'第一个have为完成时第二个为背负债务，done little强调缓解有限而非完全无效。',
'P2-S7':'1.5 trillion为1.5万亿美元，balances为未偿余额，record为创纪录。',
'P3-S1':'88%是毕业班学生选专业考虑就业，major为专业非主要的。',
'P3-S2':'稳定就业为最想要雇主特点，括号内职业发展培训其次、意义目标再次。',
'P3-S3':'第一是工作生活平衡、第二是工作保障，cause为事业，greater good为公共利益。',
'P4-S1':'That is仅为这是，比较上一代属于后块，修正中文提前错位。',
'P4-S2':'60-day按持续为期60天翻译，不自造每60天频率；机构身份与适用美国青年分开。',
'P4-S3':'because of为原因，gig economy指短期灵活零工，确定稳定为Z代需求。',
'P4-S4':'have troubles为面临困难，financial future是财务前景，risk averse是不愿冒险。'})
