from audit_early_base import *
r=article('2013-T3','''
scientists~scientist~n=科学家
prone~prone~a=容易……的
snap~snap~a=迅速而仓促的
overreactions~overreaction~n=过度反应
react~react~v=反应
negative~negative~a=负面的
effects~effect~n=影响
hard-wired~hard-wired~a=根深蒂固、近乎本能的
responses~response~n=反应
 decisions~decision~n=判断；决定
defense~defense~n=防御
mechanisms~mechanism~n=机制
judging~judge~v=判断
someone~someone~pron=某个人
dangerous~dangerous~a=危险的
brains~brain~n=大脑
bodies~body~n=身体
milliseconds~millisecond~n=毫秒
assess~assess~v=评估
factors~factor~n=因素
accurately~accurately~adv=准确地
tell~tell~v=判断；辨别
sociable~sociable~a=合群的；善于交际的
minute~minute~n=分钟
preferably~preferably~adv=最好
judge~judge~v=判断
complex~complex~a=复杂的
aspects~aspect~n=方面
personality~personality~n=性格
neuroticism~neuroticism~n=神经质倾向（人格特质，非神经疾病）
open~open~a=开放的（open-mindedness中的组成部分）
mindedness~mindedness~n=心态（与open合为思想开放程度）
reaction~reaction~n=反应
rapid~rapid~a=快速的
stimuli~stimulus~n=刺激；刺激信号
aren't~are not~aux=不是（are not缩写）
exclusive~exclusive~a=仅限于……的
interpersonal~interpersonal~a=人际交往的
realm~realm~n=领域
psychologists~psychologist~n=心理学家
toronto~Toronto~name=多伦多
viewing~view~v=观看
fast-food~fast-food~a=快餐的
logo~logo~n=标志
primes~prime~v=预先诱发某种反应；使进入反应状态
read~read~v=阅读
faster~fast~adv=更快地
reading~read~v=阅读
eating~eat~v=吃东西
unconsciously~unconsciously~adv=无意识地
associate~associate~v=将……联系起来
food~food~n=食物
speed~speed~n=速度
impatience~impatience~n=不耐烦
carry~carry~v=带入
impulses~impulse~n=冲动
else~else~adv=其他的
we're~we are~aux=我们正在（we are缩写）
subjects~subject~n=受试者
exposed~expose~v=接触；暴露于
flashes~flash~n=短暂闪现的图像
musical~musical~a=音乐的
piece~piece~n=一首乐曲
lasts~last~v=持续
reverse~reverse~v=扭转
influences~influence~n=影响
overreact~overreact~v=反应过度
consumer~consumer~n=消费者（消费品的定语）
housing~housing~n=住房
options~option~n=可选项目
happy~happy~a=高兴的；带笑的
real~real~a=不动产的（real estate中的成分）
estate~estate~n=地产
agents~agent~n=经纪人
smiling~smile~v=微笑
screeners~screener~n=招聘筛选人员
reject~reject~v=拒绝
applicants~applicant~n=应聘者
understand~understand~v=认识；理解
biases~bias~n=偏见
hire~hire~v=聘用
outside~outside~a=外部的
john~John~name=约翰
gottman~Gottman~name=戈特曼（姓氏）
thin~thin~a=少量的（thin slice整体为凭少量信息迅速判断）
slice~slice~v=截取少量信息作判断（thin slice）
reliably~reliably~adv=可靠地
ground~ground~v=使建立在……基础上
reactions~reaction~n=反应
thick~thick~a=深入的；信息充分的（比喻）
sliced~slice~a=深入分析的（thick sliced修饰研究方式）
long-term~long-term~a=长期的
really~really~adv=确实
couple~couple~n=一对夫妻
invites~invite~v=邀请
island~island~n=岛
retreat~retreat~n=僻静的度假居所
evaluation~evaluation~n=评估
seconds~second~n=秒
ability~ability~n=能力
mute~mute~v=减弱；抑制
pausing~pause~v=停顿
differentiates~differentiate~v=使有别于
animals~animal~n=动物
dogs~dog~n=狗
intermittently~intermittently~adv=断断续续地
minutes~minute~n=分钟
historically~historically~adv=长期以来
spent~spend~v=花费
contemplating~contemplate~v=思考
term~term~n=时期；长远未来
changed~change~v=改变
hasn't~has not~aux=还没有（完成时否定）
imaginative~imaginative~a=想象的
capacity~capacity~n=能力
rise~rise~v=超越（rise above）
temptation~temptation~n=诱惑
high-speed~high-speed~a=一味求快的
''')
ids=[f'{y}-T{t}' for y in range(2010,2013) for t in range(1,5)]+['2013-T1','2013-T2'];inherit(r,ids)
r.word('P1-S1','to','对……的倾向（prone to后接名词）',pos='prep',occ=1);r.word('P1-S1','take','花（一点时间）',lemma='take',pos='v')
r.word('P2-S1','are','进行时助动词（are judging）',lemma='be',pos='aux',occ=1)
r.word('P2-S4','takes','需要；花费（时间）',lemma='take',pos='v');r.word('P2-S4','while','一段时间（名词）',pos='n')
r.word('P3-S1','to','对……的反应（reaction to）',pos='prep',occ=1);r.word('P3-S1','to','仅限于（exclusive to）',pos='prep',occ=2)
r.word('P3-S2','for','持续（几毫秒）',pos='prep');r.word('P3-S2','has','与little to do with构成几乎无关',lemma='have',pos='v');r.word('P3-S2','do','have to do with中的关联义，不独立译做',lemma='do',pos='v')
r.word('P3-S3','with','与……相联系（associate A with B）',pos='prep');r.word('P3-S3','to','接触（exposed to）',pos='prep',occ=1)
r.word('P4-S2','to','对（反应过度的对象）',pos='prep');r.word('P4-S2','before','在……之前（购买）',pos='prep')
r.word('P5-S1','only','只有（only after引出必要前提）',pos='adv')
r.word('P5-S2','to','去；到（岛上度假居所）',pos='prep',occ=2);r.word('P5-S2','for','进行（评估的用途）',pos='prep')
r.word('P6-S1','by','通过（停顿的办法）',pos='prep');r.word('P6-S1','for','持续（几分钟）',pos='prep')
r.word('P6-S2','about','大约（12%）',pos='adv')
r.word('P6-S4','have','具有；拥有（能力）',lemma='have',pos='v');r.word('P6-S4','above','超越（诱惑）',pos='prep')
checks(r,[
'snap形容词仓促并非动词；先想可能反应能减少负面影响，非完全消除全部本能。',
'即时判断防御机制的条件例子完整，毫秒非秒；judging进行时与hard-wired状态分开。',
'其他因素评估需时间，不将snap判断所有功能都否定。',
'一分钟最低且最好五分钟，sociable合群非道德好坏。',
'neuroticism人格倾向非神经疾病，open -mindedness原卷空格保留并有整体词组。',
'不只人际领域，exclusive to限制范围否定正确。',
'观看快餐标志几毫秒与阅读快20%区分，prime诱发反应非首要。',
'受试者subjects与学科不同；piece音乐作品；原卷逗号接两句中文以分号处理。',
'反转影响有可能，reverse动词非相反的形容词。',
'笑脸诱发过度反应，销售与房地产经纪括注是原因例子，不把微笑说成产品本身。',
'女性筛选者更可能拒漂亮女应聘者是条件例子；outside为外部非户外。',
'thin slice为动词凭少量信息快判断，可靠前提是长期深入研究。',
'评估夫妻是否继续共同生活，two days对比two seconds，retreat是居所非撤退。',
'停顿抑制本能是区别；狗思未来时断时续或几分钟，不是完全不能。',
'约12%是每天时间份额，longer term为长远未来非学期。',
'技术可能改变反应但未改天性，has not完成时否定保留。',
'have实义拥有能力，rise above克服诱惑，高速趋势为一味求快。'])
r.lex('''
days~day~n=天
expert~expert~n=专家
few~few~det=几（a few）
good~good~a=优秀的
how~how~adv=如何
just~just~adv=仅仅
like~like~prep=例如
little~little~pron=很少；几乎没有（关联）
long~long~adv=长久地
longer~long~a=时间更长的
moment~moment~n=片刻
much~much~adv=大大地（加强比较）
need~need~v=需要
one~one~num=一个
products~product~n=产品
quickly~quickly~adv=迅速地
reason~reason~n=原因
sales~sales~n=销售（作代表的定语）
show~show~v=表明
such~such~det=这些；这样的
take~take~v=花（时间）
tend~tend~v=往往会
those~those~det=那些
time~time~n=时间
way~way~n=方式
what~what~pron=所……的事物（区别我们的东西）
whatever~whatever~pron=任何（其他事情）
yet~yet~conj=然而
''')
gaps(r)
if not r.missing():r.save()
