"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2023-T4')
r.lex('''
teenagers~teenager~n=青少年
are~be~v=是；处于所说状态
paradoxical~paradoxical~adj=看似矛盾的
that's~that is~pron+v=那是一种说法
mild~mild~adj=温和的；不激烈的
detached~detached~adj=超然客观的；不带强烈感情的
way~way~n=表达方式
of~of~prep=的（连接修饰关系）
saying~say~v=说；描述
something~something~pron=某种情况
that~that~pron=引导定语从句，指前面的对象
parents~parent~n=父母
often~often~adv=常常
express~express~v=表达；描述
with~with~prep=用（某种措辞）
considerably~considerably~adv=大大地；相当大程度地
stronger~strong~adj=更激烈的
language~language~n=措辞
but~but~conj=但；然而
paradox~paradox~n=矛盾现象
is~be~v=是
scientific~scientific~adj=有科学依据的
as~as~adv=与well as构成“也；还”
well~well~adv=与as well as构成“也；还”
personal~personal~adj=个人感受层面的
in~in~prep=在……时期
adolescence~adolescence~n=青春期
helpless~helpless~adj=无助的
dependent~dependent~adj=依赖他人的
children~child~n=孩子
who~who~pron=引导定语从句，指前面的人
have~have~aux=与过去分词构成现在完成时
relied~rely~v=依靠；依赖
on~on~prep=依靠的对象（rely on）
grown-ups~grown-up~n=成年人
for~for~prep=在……方面（依靠成年人）
just~just~adv=几乎；差不多（just about）
about~about~adv=大约；差不多（just about）
everything~everything~pron=一切事情
become~become~v=成为；变得
independent~independent~adj=独立的
people~person~n=人；个体
can~can~modal=能够
take~take~v=与care of构成“照顾”
care~care~n=照料（take care of）
themselves~themselves~pron=他们自己，指青少年
help~help~v=帮助
each~each~pron=与other构成“彼此”
other~other~pron=与each构成“彼此”
at~at~prep=与the same time构成“与此同时”
same~same~adj=相同的
 time~time~n=时间；时期
once~once~adv=曾经
cheerful~cheerful~adj=开朗的；愉快的
compliant~compliant~adj=顺从的；听话的
rebellious~rebellious~adj=叛逆的
teenage~teenage~adj=青少年的
risk-takers~risk-taker~n=爱冒险的人
new~new~adj=新的
study~study~n=研究
published~publish~v=发表
journal~journal~n=学术期刊
child~child~n=儿童（期刊名组成部分）
development~development~n=发展（期刊名组成部分）
by~by~prep=由（指出研究者）
eveline~Eveline~propn=埃弗琳（研究者名字）
crone~Crone~propn=克罗内（研究者姓氏）
university~university~n=大学
leiden~Leiden~propn=莱顿
colleagues~colleague~n=同事
suggests~suggest~v=表明；提示
positive~positive~adj=积极的；正面的
negative~negative~adj=消极的；负面的
sides~side~n=方面
go~go~v=与hand in hand构成“相伴而行”
hand~hand~n=与hand in hand构成“相伴”
part~part~n=一部分
wave~wave~n=潮流；思潮
thinking~think~n=思考；看法
long~long~adj=长的
scientists~scientist~n=科学家
policy~policy~n=政策
makers~maker~n=制定者
concentrated~concentrate~v=集中关注
idea~idea~n=看法；观点
were~be~v=是；处于所说状态
problem~problem~n=问题
needed~need~v=需要
to~to~inf=不定式标记，后接动词原形
be~be~aux=与solved构成被动语态
solved~solve~v=解决
work~work~n=研究工作
emphasizes~emphasize~v=强调
opportunity~opportunity~n=机遇
risk~risk~n=风险
researchers~researcher~n=研究人员
studied~study~v=研究；考察
prosocial~prosocial~adj=亲社会的；有益于他人的
traits~trait~n=特征；特质
more~more~adv=更多；更高程度
than~than~prep=比；多于（比较标记）
young~young~adj=年轻的
adults~adult~n=成年人
ranging~range~v=范围从……到……
from~from~prep=从（范围起点）
years~year~n=年；岁
old~old~adj=……岁的
participants~participant~n=研究参与者
filled~fill~v=填写（fill out）
out~out~adv=与fill构成“填完”
questionnaires~questionnaire~n=问卷
how~how~adv=多么；多大程度（询问频率或数量）
did~do~v=做
things~thing~n=事情；行为
altruistic~altruistic~adj=利他的；为他人着想的
like~like~prep=例如（引出例子）
sacrificing~sacrifice~v=牺牲
own~own~adj=自己的
interests~interest~n=利益
friend~friend~n=朋友
getting~get~v=变得
 drunk~drunk~adj=醉酒的
staying~stay~v=停留在外；不回家（stay out）
late~late~adv=到很晚
studies~study~n=研究
shown~show~v=表明
behavior~behavior~n=行为
increases~increase~v=增加
teenager~teenager~n=青少年
then~then~adv=随后
fades~fade~v=逐渐消退
away~away~adv=与fade构成“逐渐消退”
grow~grow~v=逐渐变得
older~old~adj=年纪更大的
shows~show~v=表明
interestingly~interestingly~adv=有趣的是
pattern~pattern~n=变化模式
holds~hold~v=适用；成立（hold for）
likely~likely~adj=有可能的
younger~young~adj=年龄较小的
report~report~v=报告；陈述
unselfishly~unselfishly~adv=无私地
most~most~adv=最；尤其
significantly~significantly~adv=重要地（most significantly意为最重要的是）
there~there~adv=引出“存在……”的结构
was~be~v=存在（there was）
correlation~correlation~n=相关性
between~between~prep=在……二者之间
prosociality~prosociality~n=亲社会性
rebelliousness~rebelliousness~n=叛逆性
also~also~adv=也
others~other~pron=他人
good~good~adj=好的；积极的
bad~bad~adj=坏的；消极的
seem~seem~v=似乎
 develop~develop~v=发展
together~together~adv=一起；共同
some~some~det=某种
common~common~adj=共同的
factor~factor~n=因素
underlies~underlie~v=构成……的基础；是……背后的因素
these~these~det=这些
apparently~apparently~adv=看起来；表面上
contradictory~contradictory~adj=相互矛盾的
developments~development~n=发展变化
one~one~det=一种
related~related~adj=有关联的（be related to）
what~what~pron=……的事物（what researchers call）
call~call~v=称作
reward~reward~n=回报；奖励
sensitivity~sensitivity~n=敏感性
decision-making~decision-making~n=决策；作决定
always~always~adv=始终
involves~involve~v=涉及；包含
balancing~balance~v=权衡
rewards~reward~n=回报
risks~risk~n=风险
benefits~benefit~n=收益；好处
costs~cost~n=代价
measures~measure~v=衡量
much~much~det=多少
it~it~pron=形式主语，指获得足够回报这件事
takes~take~v=需要
outweigh~outweigh~v=超过；足以抵偿
particularly~particularly~adv=尤其
sensitive~sensitive~adj=敏感的
social~social~adj=社交的
winning~win~v=赢得
game~game~n=比赛
impressing~impress~v=给……留下深刻印象
boy~boy~n=男生
notice~notice~v=注意到
risk-taking~risk-taking~n=冒险行为
seems~seem~v=似乎
up~up~adv=上升（go up）
down~down~adv=下降
again~again~adv=又；再次
age~age~v=年龄增长
somehow~somehow~adv=不知为何
when~when~conj=当……时
hit~hit~v=达到（某个年龄）
chance~chance~n=可能性
exciting~exciting~adj=令人兴奋的
will~will~modal=会；将
happen~happen~v=发生
party~party~n=聚会
doesn't~do not~aux=否定助动词，不
effort~effort~n=努力；力气
off~off~prep=离开（沙发）
couch~couch~n=沙发
''')
r.word('P1-S2','of','用来……（连接表达方式与所说内容）','of','prep')
r.word('P1-S4','of','与take care of构成“照顾”','of','prep')
r.word('P2-S1','in','在……刊物上','in','prep',occ=1)
r.word('P2-S1','in','与hand in hand构成“相伴而行”','in','prep',occ=2)
r.word('P2-S1','that','引出研究所表明的内容','that','conj')
r.word('P2-S2','about','关于；对于','about','prep')
r.word('P2-S3','for','持续……时间','for','prep')
r.word('P2-S3','that','引出idea的具体内容','that','conj',occ=1)
r.word('P2-S3','on','关注的对象（concentrate on）','on','prep')
r.word('P2-S4','that','引出强调的内容','that','conj')
r.word('P3-S1','in','在……研究对象中','in','prep')
r.word('P3-S1','to','到（年龄范围的终点）','to','prep')
r.word('P3-S2','about','关于；就……方面','about','prep')
r.word('P3-S2','out','在外面（stay out）','out','adv',occ=2)
r.word('P4-S1','other','其他的','other','adj')
r.word('P4-S1','that','引出研究发现','that','conj')
r.word('P4-S1','as','随着；当……时','as','conj')
r.word('P4-S2','that','引出研究发现','that','conj')
r.word('P4-S2','for','对……适用（hold for）','for','prep')
r.word('P4-S3','that','引出报告的内容','that','conj')
r.word('P5-S1','positive','正的（两个变量同向变化）','positive','adj')
r.word('P6-S1','is','存在（is there）','be','v')
r.word('P6-S2','that','引出观点的具体内容','that','conj')
r.word('P6-S2','to','与……有关（be related to）','to','prep')
r.word('P7-S1','to','对……（be sensitive to）','to','prep',occ=1)
r.word('P7-S1','getting','使；让','get','v')
r.word('P7-S1','that','那个（指所喜欢的男生）','that','det')
r.word('P7-S2','like','像……一样','like','prep')
r.word('P7-S2','go','变得（go up指上升）','go','v')
r.word('P7-S2','as','随着','as','conj')
r.word('P7-S3','that','引出chance的具体内容','that','conj',occ=1)
r.word('P7-S3','that','那个','that','det',occ=2)
r.word('P7-S3','at','在（聚会上）','at','prep')
r.word('P7-S3','just','就是；就（强调）','just','adv')
r.word('P7-S3','getting','起身（get up）','get','v')
r.word('P7-S3','up','与get构成“起身”','up','adv')
r.sentence('P3-S2')['chunks'][-1]['zh']='比如喝醉或很晚还不回家。'
r.sentence('P6-S2')['chunks']=chunks(r,'P6-S2','that teenage behavior|is related to|what researchers','一种看法是，|青少年的行为|与……有关，|研究人员称为“奖励敏感性”的特质。')
notes={
'P1-S1':'核定paradoxical为表面矛盾，are系动词，不译自相矛盾逻辑错误。',
'P1-S2':'核定detached超然客观、stronger措辞更激烈，that修饰something，不指父母。',
'P1-S3':'科学层面与个人感受并存，as well as不否定任一项。',
'P1-S4':'两个who各修饰前后不同群体状态；have完成时、for事事、独立能力变化。',
'P1-S5':'once是曾经，compliant听话，risk-takers完整复合词；与前句同时成长。',
'P2-S1':'核定研究作者、莱顿大学及刊名关系，suggests谨慎提示，hand in hand不推出因果。',
'P2-S2':'wave是研究思潮，thinking名词，about为关于而非大约。',
'P2-S3':'首that内容从句、次that定语；need被动不遗漏，长期观念不是作者断言。',
'P2-S4':'work指研究，青春期机遇与风险并存，as well as不可误译只有风险。',
'P3-S1':'200多名、11至28岁范围，prosocial与叛逆两种traits并列。',
'P3-S2':'问卷询问频率，or并列两类行为；staying out late不是一定整夜不归，修正分块。',
'P4-S1':'两个as随年龄阶段，先上升后消退；have shown是完成时非拥有。',
'P4-S2':'same pattern承接先升后降，hold for适用，that引研究结论。',
'P4-S3':'比较的是报告行为的可能性，非保证实际表现；younger/adults两组比较对象。',
'P5-S1':'positive是统计正相关，不是积极相关；correlation不译因果。',
'P5-S2':'more rebellious与more likely并列程度，who限定青少年，保持概率表述。',
'P5-S3':'seem保留不确定语气，develop共同发展不解释成互相导致。',
'P6-S1':'there存在问句，underlie深层基础，apparently修饰矛盾不能说确实矛盾。',
'P6-S2':'修正related to分块对象，what为研究者所称特质，idea非确证结论。',
'P6-S3':'decision-making完整复合词，balancing权衡，两组收益代价并列。',
'P6-S4':'reward名词，how much数量，it takes表示需要，outweigh比较回报与风险。',
'P7-S1':'reward社交认可，getting使男生注意，that指示词；三项举例逐项对应。',
'P7-S2':'Reward词性改名词，like比较与as随年龄分开，go up/down敏感度起落。',
'P7-S3':'hit到年龄，首that内容从句次指示，否定seem与努力比较，非没机会发生新事。'}
r.word('P1-S3','as','与as well as构成“既……也……”','as','conj',occ=1)
r.word('P1-S3','as','与as well as构成“既……也……”','as','conj',occ=2)
r.word('P2-S4','as','与as well as构成“既……也……”','as','conj',occ=1)
r.word('P2-S4','as','与as well as构成“既……也……”','as','conj',occ=2)
done(r,notes)
