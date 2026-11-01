"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2023-T2')
r.lex('''
it's~it is~v=形式主语结构，相当于这件事是（it is）
easy~easy~a=容易的
to~to~inf=不定式标记，连接动作
dismiss~dismiss~v=不予考虑；斥为
as~as~prep=当作；作为
absurd~absurd~a=荒唐的
federal~federal~a=联邦的
government's~government~n=政府的
ideas~idea~n=想法；办法
for~for~prep=为了；用于
plugging~plug~v=填补
chronic~chronic~a=长期存在的
funding~funding~n=资金；拨款
gap~gap~n=缺口
of~of~prep=……的（所属、内容或部分关系）
national~national~a=国家的；国家级的
parks~park~n=公园
can~can~aux=会；能够（反问中的可能性）
anyone~anyone~pron=任何人
really~really~adv=真的
think~think~v=认为
good~good~a=好的
idea~idea~n=主意
allow~allow~v=允许
amazon~Amazon~name=亚马逊公司
deliveries~delivery~n=送货服务
tent~tent~n=帐篷
in~in~prep=在……中；在所述地点
yosemite~Yosemite~name=优胜美地（国家公园名）
food~food~n=食物
trucks~truck~n=餐车（food trucks）
line~line~v=排成队（line up）
up~up~adv=与line合成排队
under~under~prep=在……下面
redwood~redwood~n=红杉
trees~tree~n=树木
at~at~prep=在所说地点
sequoia~Sequoia~name=红杉（Sequoia National Park公园名部分）
park~Park~n=公园
but~but~conj=但是
government~government~n=政府
is~be~v=是；处于所说状态
right~right~a=正确的
about~about~prep=关于；在某方面
one~one~a=一个
thing~thing~n=事情
u.s.~U.S.~name=美国
are~be~v=处于某状态；是
crisis~crisis~n=危机
collectively~collectively~adv=合计起来
have~have~v=有
maintenance~maintenance~n=维护；维修
backlog~backlog~n=积压的未完成事项
more~more~adv=超过（more than）
than~than~conj=超过；比
billion~billion~num=十亿
roads~road~n=道路
trails~trail~n=步道
restrooms~restroom~n=公共厕所
visitor~visitor~n=游客
centers~center~n=中心
other~other~a=其他的
infrastructure~infrastructure~n=基础设施
crumbling~crumble~v=日渐破败
privatizing~privatize~v=使私有化
commercializing~commercialize~v=使商业化
campgrounds~campground~n=露营地
would~would~aux=会；愿意（依本句假设或意愿）
be~be~v=是
cure-all~cure-all~n=万能解决办法
tiny~tiny~a=极小的
portion~portion~n=一部分
overall~overall~a=全部的；整体的
businesses~business~n=商家
hand~hand~v=交出；上缴（hand over）
over~over~adv=交出（hand over的一部分）
on~on~prep=与average合成平均而言
average~average~n=平均
only~only~adv=仅仅
revenues~revenue~n=营业收入
service~Service~n=管理局（National Park Service机构名部分）
moreover~moreover~adv=此外
increased~increase~a=程度提高的
privatization~privatization~n=私有化
certainly~certainly~adv=肯定
undercut~undercut~v=削弱
major~major~a=主要的
reasons~reason~n=原因
why~why~conj=为何；引出游客前来的原因
million~million~num=百万
visitors~visitor~n=游客
come~come~v=来到
each~each~a=每一
year~year~n=年
enjoy~enjoy~v=享受
nature~nature~n=大自然
get~get~v=获得（get a break为暂时摆脱）
break~break~n=暂时的休息；摆脱
from~from~prep=从；摆脱的对象
commercial~commercial~a=商业的
drumbeat~drumbeat~n=连绵不断的宣传喧嚣
that~that~conj=从句连接词，引出论述内容
overwhelms~overwhelm~v=充斥；淹没
daily~daily~a=日常的
life~life~n=生活
real~real~a=真正的
problem~problem~n=问题
been~be~aux=构成被动完成结构
chronically~chronically~adv=长期地
starved~starve~v=严重缺乏
conducted~conduct~v=开展
comprehensive~comprehensive~a=全面的
survey~survey~n=调查
examining~examine~v=考察
how~how~adv=如何
residents~resident~n=居民
view~view~v=看待
found~find~v=发现
americans~American~n=美国人
place~place~v=给予（place value on表示重视）
very~very~adv=非常
high~high~a=高的
value~value~n=价值
whether~whether~conj=是否（whether or not为无论是否）
actually~actually~adv=确实；实际地
visit~visit~v=游览
peer-reviewed~peer-reviewed~a=经过同行评审的
economic~economic~a=经济学的
taxpayers~taxpayer~n=纳税人
by~by~prep=通过
mail~mail~n=邮寄
internet~internet~n=互联网
also~also~adv=也；还
people~people~n=人们
willing~willing~a=愿意的
pay~pay~v=支付
significant~significant~a=相当可观的
amount~amount~n=金额
money~money~n=钱
make~make~v=使得（make sure为确保）
sure~sure~a=确定（make sure为确保）
programs~program~n=项目
kept~keep~v=使保持；保留
intact~intact~a=完整无损的
some~some~adv=约（置于比例前）
respondents~respondent~n=受访者
said~say~v=表示
additional~additional~a=额外的
taxes~tax~n=税款
next~next~a=接下来的
years~year~n=年
avoid~avoid~v=避免
any~any~a=任何的
cuts~cut~n=削减
a provide~provide~v=提供
provide~provide~v=提供
great~great~a=巨大的
both~both~adv=两个方面都（both…and）
places~place~n=地方
escape~escape~v=逃离日常压力；暂离日常生活
symbols~symbol~n=象征
top~top~n=与on、of构成除此之外
this~this~pron=前述公园的价值
produce~produce~v=创造；产生
extensive~extensive~a=广泛的
educational~educational~a=教育的
positive~positive~a=积极的
impact~impact~n=影响
climate~climate~n=气候
through~through~prep=通过
carbon~carbon~n=碳
sequestration~sequestration~n=封存；固定（碳）
contribution~contribution~n=贡献
cultural~cultural~a=文化的
artistic~artistic~a=艺术的
course~course~n=与of构成当然
tourism~tourism~n=旅游业
help~help~v=帮助
keep~keep~v=使保持
america's~America~name=美国的
past~past~n=过去；历史
alive~alive~a=鲜活的
working~work~v=合作；开展工作
with~with~prep=与（合作对象）
thousands~thousand~num=数千
local~local~a=地方的
jurisdictions~jurisdiction~n=管辖区
around~around~prep=遍及
country~country~n=全国
protect~protect~v=保护
historical~historical~a=历史的
sites~site~n=遗址
including~including~prep=包括
ellis~Ellis~name=埃利斯（地名部分）
island~Island~n=岛（地名部分）
gettysburg~Gettysburg~name=葛底斯堡
bring~bring~v=使……生动呈现（bring to life）
stories~story~n=故事
these~these~a=这些
 do~do~v=做；完成
all~all~a=所有的
shoestring~shoestring~n=微薄经费（on a shoestring）
congress~Congress~name=美国国会
allocates~allocate~v=拨款；分配
system~system~n=系统
has~have~aux=构成现在完成时
flat~flat~a=持平的
since~since~prep=自……以来
inflation-adjusted~inflation-adjusted~a=经通胀调整的
dollars~dollar~n=美元
exception~exception~n=例外
onetime~onetime~a=一次性的
boost~boost~n=增加
as~as~prep=作为
part~part~n=一部分
obama~Obama~name=奥巴马
stimulus~stimulus~n=刺激（经济刺激）
package~package~n=一揽子计划
meanwhile~meanwhile~adv=与此同时
number~number~n=人数；数量
annual~annual~a=每年的
now~now~adv=现在
stands~stand~v=达到（数值）
per~per~prep=每
''')
r.word('P1-S2','to','送达的目的地','to','prep',occ=2)
r.word('P2-S2','they','这些国家公园','they','pron')
r.word('P2-S3','are','构成现在进行时（are crumbling）','be','aux')
r.word('P3-S2','to','上缴给的接收机构','to','prep')
r.word('P4-S1','one','其中一个原因','one','pron')
r.word('P4-S1','to','游客来到的目的地','to','prep',occ=1)
r.word('P4-S1','that','关系代词，指商业喧嚣','that','pron')
r.word('P5-S1','have','构成完成时','have','aux')
r.word('P5-S2','they','美国居民','they','pron')
r.word('P5-S2','them','国家公园','they','pron')
r.word('P5-S2','on','重视的对象（place value on）','on','prep')
r.word('P5-S3','are','构成被动语态（are kept）','be','aux')
r.word('P5-S4','they','受访者','they','pron')
r.word('P5-S4','for','持续（接下来的十年）','for','prep')
r.word('P5-S4','to','受到削减的对象','to','prep',occ=3)
r.word('P6-S1','to','价值提供给的受益者','to','prep',occ=1)
r.word('P6-S2','On','与top of构成除此之外','on','prep',occ=1)
r.word('P6-S2','on','给气候带来影响的对象','on','prep',occ=2)
r.word('P6-S2','to','作出贡献的领域','to','prep')
r.word('P6-S2','they','国家公园','they','pron')
r.word('P6-S3','to','与life合成让故事鲜活的状态','to','prep',occ=3)
r.word('P7-S1','on','以微薄经费（on a shoestring）','on','prep')
r.word('P7-S2','a','每（a year为每年）','a','art',occ=1)
r.word('P7-S2','to','拨款给的接收者','to','prep')
r.word('P7-S2','that','关系代词，指拨款金额','that','pron')
r.word('P7-S2','been','一直处于持平状态','be','v')
r.word('P7-S2','with','除……之外（with the exception of）','with','prep')
r.word('P7-S3','increased','增加','increase','v')
r.word('P7-S3','by','增加的幅度','by','prep')
r.word('P7-S3','at','处于某个数值','at','prep')
r.sentence('P7-S3')['chunks'][0]['zh']='与此同时，每年游客人数，'
r.sentence('P7-S3')['chunks'][1]['zh']='自1980年以来增加了50%以上，'
done(r,{
'P1-S1':'dismiss as absurd为斥为荒唐，plug为填补长期资金缺口非塞住实体洞。',
'P1-S2':'两个to分别允许动作和送达目的地，餐车排队为反问例子非作者支持主张。',
'P2-S1':'right为说得正确，冒号解释公园处于危机而非给予权利。',
'P2-S2':'12 billion为120亿美元维护积压成本，不是已有预算。',
'P2-S3':'trails为步道，infrastructure是基础设施，crumbling为逐渐破败。',
'P3-S1':'not否定万能解决办法，私有化商业化两个措施共同作主语。',
'P3-S2':'revenues为营业收入非利润，5%为平均上缴比例，hand over为上缴。',
'P4-S1':'one of为一个主要原因，商业drumbeat比喻喧嚣，that修饰喧嚣。',
'P5-S1':'starved of为严重匮乏，have been为完成被动，非字面饿死公园。',
'P5-S2':'people是否去过公园不影响其高度评价，them为公园，they为美国居民。',
'P5-S3':'700纳税人样本由邮寄网络进行，peer-reviewed为同行评审，支付用于保全公园项目。',
'P5-S4':'81%受访者愿未来十年多缴税，cuts为经费服务削减而非砍树。',
'P6-S1':'两个as列出公园提供价值的两种身份，escape为远离日常压力。',
'P6-S2':'四项教育固碳文化旅游价值并列，carbon sequestration为固碳，climate影响在其对应块。',
'P6-S3':'jurisdictions为地方辖区，Ellis和Gettysburg为遗址例子，bring to life是讲活故事。',
'P7-S1':'on a shoestring为经费微薄而非鞋带物品。',
'P7-S2':'30亿美元为年拨款，按通胀实际值自2001持平，2009一次增加为例外。',
'P7-S3':'增幅超过50%非增加到50%，现3.3亿年人次，移回第二块since 1980。'})
