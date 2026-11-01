"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2020-T2')
r.lex('''
it~it~pron=形式主语，引出后面的陈述
is~be~v=是
true~true~a=确实的
that~that~conj=引导所陈述的内容，不单译
ceo~CEO~n=首席执行官
ceos~CEO~n=首席执行官们
pay~pay~n=薪酬；报酬
has~have~aux=构成现在完成时
gone~go~v=已经变得（gone up表示上涨）
up~up~adv=上涨（go up的一部分）
top~top~a=顶尖的
ones~one~pron=那些首席执行官
may~may~aux=可能
make~make~v=挣得；赚取
times~time~n=倍
of~of~prep=……的（所属或范围关系）
typical~typical~a=普通的；一般的
workers~worker~n=员工；劳动者
on~on~prep=与average搭配表示平均而言
average~average~n=平均
since~since~prep=自……以来
mid-1970s~mid-1970s~n=20世纪70年代中期
for~for~prep=对于；对应于
large~large~a=大型的
publicly~publicly~adv=公开地（publicly traded指上市交易）
traded~trade~v=被公开交易的；上市的
american~American~a=美国的
corporations~corporation~n=公司；企业
by~by~prep=根据（估算或衡量标准）
varying~vary~a=各不相同的
estimates~estimate~n=估算
about~about~adv=大约
corporation~corporation~n=公司；企业
now~now~adv=如今
makes~make~v=赚取；收入为
million~million~num=百万
year~year~n=年
best~good~a=最合适的；最佳的
model~model~n=解释框架；模型
understanding~understand~v=理解
growth~growth~n=增长
limited~limited~a=有限的
talent~talent~n=人才；管理能力
in~in~prep=在……中；在所述范围内
world~world~n=环境；世界
where~where~conj=引出该环境下的具体情况
business~business~n=商业；业务
opportunities~opportunity~n=机会
firms~firm~n=公司
are~be~aux=构成进行时或被动结构
growing~grow~v=增长
rapidly~rapidly~adv=迅速地
efforts~effort~n=努力
america~America~name=美国
s~'s~part=名词所有格标记，表示“……的”
highest-earning~highest-earning~a=收入最高的
have~have~aux=构成完成时
been~be~v=一直是
one~one~pron=其中一个
more~more~adv=更；程度较高
 dynamic~dynamic~a=活跃而有推动力的
elements~element~n=因素；组成部分
global~global~a=全球的
economy~economy~n=经济
it's~it is~v=这件事是（it is的缩写）
popular~popular~a=受欢迎的；讨人喜欢的
to~to~inf=不定式标记，连接要做的动作
say~say~v=说；表达
but~but~conj=但是
reason~reason~n=原因
so~so~adv=如此；这么
much~much~adv=程度很大
really~really~adv=确实
upped~up~v=提高；提升
game~game~n=能力与表现（up one's game搭配）
relative~relative~a=相对而言（relative to为相比于）
many~many~a=许多
u.s.~U.S.~name=美国
today~today~adv=如今
at~at~prep=与least搭配，表示至少
least~little~adv=最低限度（at least指至少）
major~major~a=大规模的；主要的
must~must~aux=必须
mere~more~a=原卷疑误作mere，按many…than理解为更多的
skills~skill~n=技能
than~than~conj=与……相比；超过
simply~simply~adv=仅仅
being~be~v=处于所说的状态
able~able~a=能够的
run~run~v=经营；管理
company~company~n=公司
good~good~a=良好的；充分的
sense~sense~n=了解；把握能力
financial~financial~a=金融的
markets~market~n=市场
maybe~maybe~adv=也许
even~even~adv=甚至
how~how~adv=如何
should~should~aux=应当
trade~trade~v=交易
also~also~adv=也；还
need~need~v=需要
better~good~a=更好的
public~public~a=公众的（public relations指公关）
relations~relation~n=关系（public relations指公共关系）
predecessors~predecessor~n=前任
as~as~conj=因为
costs~cost~n=代价；损失
minor~minor~a=小的；轻微的
slipup~slipup~n=失误
can~can~aux=可能
be~be~v=是；呈现某种状态
significant~significant~a=重大的
then~then~adv=此外；还有
there's~there is~v=还有；存在（there is的缩写）
fact~fact~n=事实
companies~company~n=公司
 globalized~globalize~a=全球化的
ever~ever~adv=以往任何时候
before~before~adv=以前
with~with~prep=并且伴有
supply~supply~n=供应
chains~chain~n=链条（supply chains指供应链）
spread~spread~v=分布；延伸
across~across~prep=遍及
larger~large~a=更多的；规模更大的
number~number~n=数量
countries~country~n=国家
lead~lead~v=领导
system~system~n=体系
requires~require~v=需要
knowledge~knowledge~n=知识
fairly~fairly~adv=相当
mind-boggling~mind-boggling~a=复杂庞大得令人难以想象的
plus~plus~adv=此外
virtually~virtually~adv=几乎
all~all~a=所有的
becoming~become~v=变成
tech~tech~n=科技
way~way~n=方式
another~another~pron=另一种方式
beyond~beyond~prep=除了……之外
this~this~pron=前述新增职责与技能
still~still~adv=仍然
 do~do~v=做；处理
day-to-day~day-to-day~a=日常的
work~work~n=工作
always~always~adv=一直
done~do~v=做；承担（工作）
common~common~a=普遍的
idea~idea~n=看法
high~high~a=高的
mainly~mainly~adv=主要地
ripping~rip~v=盘剥；坑骗（rip off搭配）
people~people~n=他人
 off~off~adv=rip off的一部分，表示坑骗或盘剥
doesn't~do~aux=并不（does not）
explain~explain~v=解释
history~history~n=历史情况
very~very~adv=很；十分
well~well~adv=充分地；好地
most~most~a=大多数的
measures~measure~n=衡量标准
corporate~corporate~a=公司的
governance~governance~n=治理；监督制度
become~become~v=变得
lot~lot~n=很大程度（a lot表程度）
tighter~tight~a=更严格的
rigorous~rigorous~a=严格严密的
yet~yet~conj=然而
principally~principally~adv=主要地
during~during~prep=在……期间
period~period~n=时期
stronger~strong~a=更有力的
rising~rise~v=上涨
suggests~suggest~v=表明
broader~broad~a=更全面的；整体的
interest~interest~n=利益
recruit~recruit~v=招募
candidates~candidate~n=候选人；人才
increasingly~increasingly~adv=日益；越来越
tough~tough~a=艰难的；要求高的
jobs~job~n=工作；职位
furthermore~furthermore~adv=此外
highest~high~a=最高的
salaries~salary~n=薪酬
paid~pay~v=支付给
outside~outside~a=外部的
cozy~cozy~a=关系密切、相互照顾的
insider~insider~n=内部人士
picks~pick~n=挑选的人选
sign~sign~n=迹象；表明某事的证据
some~some~a=某种
kind~kind~n=种类
depredation~depredation~n=掠夺；侵占
expense~expense~n=代价（at the expense of表示牺牲）
rest~rest~n=其余的人
stock~stock~n=股票
market~market~n=市场
reacts~react~v=作出反应
positively~positively~adv=积极地；正面地
when~when~conj=当……时
tie~tie~v=把……挂钩
prices~price~n=价格
those~those~a=那些
practices~practice~n=做法；薪酬安排
build~build~v=增加（与up搭配）
value~value~n=价值
just~just~adv=仅仅
''')
r.lex('other~other~a=其他的')
r.word('P3-S6','one','某一种（方式）','one','a')
r.word('P5-S1','another','又一个；另一个','another','a')
r.word('P1-S1','by','增加了（引出增幅）','by','prep',occ=2)
r.word('P1-S2','a','每；每一','a','art',occ=2)
r.word('P2-S1','that','那种模型（替代model）','that','pron',occ=1)
r.word('P2-S1','for','用于；为了（理解）','for','prep',occ=1)
r.word('P2-S2','have','构成现在完成时','have','aux')
r.word('P2-S2','one','其中一个因素','one','pron')
r.word('P2-S4','have','构成现在完成时','have','aux')
r.word('P2-S4','to','相比的对象（relative to）','to','prep')
r.word('P3-S1','have','具备；拥有','have','v')
r.word('P3-S2','have','具备；拥有','have','v')
r.word('P3-S2','in','在……市场中','in','prep')
r.word('P3-S3','as','因为','as','conj')
r.word('P3-S4','are','构成状态说明：全球化程度更高','be','v')
r.word('P3-S5','that','那样的（前述全球化体系）','that','a',occ=1)
r.word('P3-S5','that','关系代词，指knowledge','that','pron',occ=2)
r.word('P3-S5','is','联系知识与其复杂庞大的特点','be','v')
r.word('P3-S7','have','不得不（have to）','have','v',occ=1)
r.word('P3-S7','to','连接have to中的必须做的动作','to','inf')
r.word('P4-S1','about','关于；在于','about','prep')
r.word('P4-S2','a','表示a lot这个程度短语，不指一个个体','a','art')
r.word('P4-S3','it','强调句形式词，不指具体事物','it','pron')
r.word('P4-S3','that','强调句连接词，不单译','that','part')
r.word('P4-S4','That','前句治理强化时薪酬仍上涨这一事实','that','pron')
r.word('P4-S4','it','形式主语，真正主语是后面的招募人才','it','pron')
r.word('P4-S4','in','符合……利益（in the interest）','in','prep')
r.word('P5-S1','to','支付给的接受者','to','prep')
r.word('P5-S1','at','与the expense of连用，表示以……为代价','at','prep')
r.word('P5-S2','to','挂钩的对象（tie to）','to','prep')
r.word('P5-S2','say','例如；比方说（插入举例）','say','v')
r.word('P5-S2','for','使……受益；为……','for','prep')
r.word('P5-S2','up','与build搭配，表示增加','up','adv')
r.sentence('P2-S2')['chunks']=chunks(r,'P2-S2','have been|one of','美国收入最高的1%人群所作的努力，|一直是，|全球经济中较有活力的因素之一。')
r.sentence('P3-S3')['chunks']=chunks(r,'P3-S3','as the costs|can be significant.','他们还需要比前任更好的公关技能，|因为即使是一次小失误造成的代价，|也可能很大。')
r.sentence('P4-S2')['chunks']=chunks(r,'P4-S2','corporate governance|has become','按大多数衡量标准，|公司治理，|自20世纪70年代以来已严格、严密得多。')
r.sentence('P5-S1')['chunks'][-1]['zh']='以公司其他人的利益为代价的。'
done(r,{
'P1-S1':'300倍是薪酬倍数，500%为增长幅度；第一个by是估算依据，第二个是增幅。',
'P1-S2':'1890万美元为年收入，a year中的a为每年，不是某个年份。',
'P2-S1':'that of替代model；where为商业机会增长环境，limited修饰管理人才供给。',
'P2-S2':'美国收入前1%人群为施事，全球经济修饰elements；删除前块提前译入的范围。',
'P2-S3':'不受欢迎的是这种说法，popular不是流行商品；按原卷保留断句。',
'P2-S4':'up one’s game为提高表现，relative to表对比劳动者，不是参加比赛。',
'P3-S1':'原卷mere疑为more，保留源文而按many…than比较解释，have为具备技能。',
'P3-S2':'have a sense为充分了解，trade为金融交易而非行业，them指金融市场。',
'P3-S3':'costs是失误代价，even指即使小失误；修分块让代价和很大对应原文。',
'P3-S4':'全球化程度高于以往，with引出供应链分布，不是与供应链比较。',
'P3-S5':'首that指前述体系，后that为知识的关系词；知识庞大复杂而非领导者发疯。',
'P3-S6':'virtually为几乎，one way or another指不同形式，are becoming为进行变化。',
'P3-S7':'第一个have表示必须，第二个为完成时；日常工作是新增技能之外的职责。',
'P4-S1':'普遍看法的内容不代表作者认可；doesn’t否定这种看法解释历史的能力。',
'P4-S2':'by measures为按标准，治理与自1970年代时间分属各原块，删除提前重复。',
'P4-S3':'it is…that为强调时期，principally是主要而非完全只在该时期。',
'P4-S4':'interest是公司整体利益，形式主语it回接招募高要求职位人才。',
'P5-S1':'outside对比内部关系户，not管掠夺整个短语；末块去重复否定保持对应。',
'P5-S2':'say为插入举例股价；build up是增加公司价值，受益不只是CEO。'})
