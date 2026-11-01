"""Manual word/sentence audit. Preserves existing phrases; central phrase review is separate."""
from audit_late_utils import *
r=Review('2022-T1')
r.lex('''
on~on~prep=在（某一天）
recent~recent~a=最近的
sunny~sunny~a=晴朗的
day~day~n=一天
chickens~chicken~n=鸡
roam~roam~v=自由走动；四处觅食
over~over~prep=在……范围内四处
larry~Larry~name=拉里
brown's~Brown~name=布朗的
windswept~windswept~a=常受风吹的
acres~acre~n=英亩（面积单位）
in~in~prep=在……中；在所述地方或时期
shiner~Shiner~name=沙伊纳（镇名）
texas~Texas~name=得克萨斯州
some~some~pron=有些（鸡）
rest~rest~v=休息
shade~shade~n=阴凉处
of~of~prep=……的（所属、内容或关系）
parked~park~v=停放着的
car~car~n=汽车
others~other~pron=另一些（鸡）
drink~drink~v=喝
water~water~n=水
with~with~prep=与……一起
cows~cow~n=牛
this~this~pron=前述放养鸡的安排
all~all~pron=这一切
seems~seem~v=看起来
random~random~a=随意的
but~but~conj=但；然而
it's~it is~v=这是（it is的缩写）
by~by~prep=出于；按（by design指有意安排）
design~design~n=设计；有意的安排
part~part~n=一部分；一环
what~what~pron=所押注的那个事物
billion~billion~num=十亿
u.s.~U.S.~name=美国
egg~egg~n=鸡蛋
industry~industry~n=行业
bets~bet~v=押注；寄望
will~will~aux=会；将会
be~be~v=成为；是
its~its~pron=该行业的
next~next~a=下一个的
big~big~a=热门的；重要的
thing~thing~n=事物；新潮流
climate-friendly~climate-friendly~a=有利于气候保护的
eggs~egg~n=鸡蛋
these~these~a=这些
which~which~pron=关系代词，指前述鸡蛋
are~be~aux=构成进行或被动结构
making~make~v=首次推出（make debut搭配）
debut~debut~n=首次上市
now~now~adv=如今
shelves~shelf~n=货架
for~for~prep=以……价格
as~as~adv=与much as构成高达
much~much~adv=多；高达（as much as）
dozen~dozen~num=一打；十二个
still~still~adv=仍然
labeled~label~v=贴上标签；标明
organic~organic~a=有机的
animal-friendly~animal-friendly~a=善待动物的
they're~they are~v=它们还来自（they are的缩写）
also~also~adv=也；还
from~from~prep=来自
birds~bird~n=鸟类；这里指鸡
that~that~pron=关系词，指前述对象
live~live~v=生活
farms~farm~n=农场
using~use~v=采用
regenerative~regenerative~a=恢复土壤生态的；再生农业的
agriculture~agriculture~n=农业
special~special~a=特殊的
techniques~technique~n=技术
to~to~inf=不定式标记，连接要做的动作
cultivate~cultivate~v=培育；改良（土壤）
rich~rich~a=肥沃的
soils~soil~n=土壤
can~can~aux=能够
trap~trap~v=吸存；截留
greenhouse~greenhouse~n=温室（greenhouse gases为温室气体）
gases~gas~n=气体
such~such~a=这样的
could~could~aux=可能；可以
marketed~market~v=宣传销售；推销
helping~help~v=有助于
fight~fight~v=应对；对抗
climate~climate~n=气候
change~change~n=变化
i'm~I am~v=我感到（I am缩写）
excited~excited~a=兴奋的
about~about~prep=对于
progress~progress~n=进展
says~say~v=说
brown~Brown~name=布朗
who~who~pron=关系词，指布朗
is~be~aux=构成进行时
adding~add~v=增种；增加
more~more~a=更多的
cover~cover~n=覆盖（cover crops为覆盖作物）
crops~crop~n=作物
draw~draw~v=吸引
worms~worm~n=蠕虫
crickets~cricket~n=蟋蟀
eat~eat~v=吃；啄食
waste~waste~n=粪便；排泄物
then~then~adv=接着
fertilizes~fertilize~v=施肥；使土壤肥沃
fields~field~n=农田
improvements~improvement~n=改进
allow~allow~v=使能够
hens~hen~n=母鸡
forage~forage~v=觅食
higher-quality~high-quality~a=品质更高的
natural~natural~a=天然的
feed~feed~n=饲料
good~good~a=有益的
land~land~n=土地
supply~supply~v=供应
customers~customer~n=顾客
industry's~industry~n=行业的
push~push~n=推动；推广举措
first~first~a=首次的
major~major~a=重要的
 test~test~n=检验
whether~whether~conj=是否；能否
animal~animal~a=动物来源的
products~product~n=产品
become~become~v=成为
premium~premium~a=高端优质的
offering~offering~n=推向市场的商品
barely~barely~adv=仅仅；刚刚超过
than~than~conj=比；超过
decade~decade~n=十年
went~go~v=发生转变（go from…to）
being~be~aux=构成被动语态
dismissed~dismiss~v=轻视；认为不值一提
niche~niche~a=小众的
product~product~n=产品
foods~food~n=食品
stores~store~n=商店
sold~sell~v=被销售
at~at~prep=在（销售地点或任职机构）
walmart~Walmart~name=沃尔玛
recently~recently~adv=近些时候
there~there~pron=存在句形式词，表示有
were~be~v=存在；曾有
a doubts~doubt~n=怀疑
doubts~doubt~n=怀疑
similar~similar~a=类似的
probiotics~probiotic~n=益生菌
plant-based~plant-based~a=以植物为原料的
meats~meat~n=肉类产品
both~both~pron=二者（益生菌和植物肉）
have~have~aux=构成现在完成时
exploded~explode~v=迅速增长；蓬勃发展
into~into~prep=发展成为
supermarket~supermarket~n=超市
categories~category~n=商品类别
if~if~conj=如果
sustainable-egg~sustainable-egg~a=可持续生产的鸡蛋的
rollout~rollout~n=推出；上市推广
successful~successful~a=成功的
it~it~pron=鸡蛋推广成功这件事
open~open~v=打开（比喻开启发展机会）
floodgates~floodgate~n=闸门（比喻大规模发展的入口）
beef~beef~n=牛肉
broccoli~broccoli~n=西蓝花
beyond~beyond~adv=以及更多其他产品
hard~hard~a=难的
sell~sell~n=推销；使人接受的事物
because~because~conj=因为
concept~concept~n=概念
tough~tough~a=困难的
define~define~v=解释清楚；界定
quickly~quickly~adv=迅速地
julie~Julie~name=朱莉
stanton~Stanton~name=斯坦顿
associate~associate~a=副的（职称修饰语）
professor~professor~n=教授
agricultural~agricultural~a=农业的
economics~economics~n=经济学
pennsylvania~Pennsylvania~name=宾夕法尼亚
state~State~name=州立（学校名称的一部分）
university~University~n=大学
brandywine~Brandywine~name=布兰迪万（校区名称）
farming~farming~n=耕作方式
brings~bring~v=带来
minimal~minimal~a=极少的
any~any~pron=任何改善（if any指即使有的话）
improvement~improvement~n=改善
though~though~conj=尽管
producers~producer~n=生产商
say~say~v=说；声称
protein~protein~n=蛋白质
betting~bet~v=押注；认为有前景
same~same~a=同样的；同一批
consumers~consumer~n=消费者
paying~pay~v=支付
attributes~attribute~n=特点
free-range~free-range~a=散养的
non-gmo~non-GMO~a=非转基因的
pasture-raised~pasture-raised~a=牧场放养的
embrace~embrace~v=欣然接受
sustainability~sustainability~n=可持续性
surveys~survey~n=调查
show~show~v=显示
younger~young~a=更年轻的
generations~generation~n=几代人；代际群体
concerned~concerned~a=关心的；关注的
success~success~n=成功
meat~meat~n=肉类产品
chalked~chalk~v=归因于（chalk up to）
up~up~adv=与chalk、to构成归因于
shoppers~shopper~n=购物者
wanting~want~v=希望
signal~signal~v=表明；传递信号
desire~desire~n=意愿
protect~protect~v=保护
environment~environment~n=环境
young~young~a=年轻的
adults~adult~n=成年人
really~really~adv=真的
care~care~v=关心；在乎
planet~planet~n=地球
john~John~name=约翰
brunnquell~Brunnquell~name=布伦奎尔
president~president~n=公司总裁
innovations~Innovations~name=Innovations（公司名部分）
absolutely~absolutely~adv=确实；毫无疑问地
altering~alter~v=改变
food~food~n=食品
chain~chain~n=供应链
think~think~v=认为
 even~even~adv=甚至
understand~understand~v=理解
doing~do~v=做；正在从事的行为
''')
r.word('P1-S4','its','该鸡蛋行业的','its','pron')
r.word('P2-S1','on','在货架或农场上','on','prep')
r.word('P2-S1','a','每（a dozen表示每打）','a','art')
r.word('P2-S2','be','构成被动语态（be marketed）','be','aux')
r.word('P2-S2','as','作为……卖点；以……定位','as','prep')
r.word('P3-S1','for','供……做某事（for chickens to eat）','for','prep')
r.word('P3-S3','for','觅食的目标（forage for）','for','prep',occ=1)
r.word('P3-S3','for','有益于的对象（good for）','for','prep',occ=2)
r.word('P3-S3','to','供应给的接受者','to','prep',occ=2)
r.word('P4-S1','is','是（联系推动举措与检验）','be','v')
r.word('P4-S2','as','被视为（dismiss as）','as','prep')
r.word('P4-S2','to','从小众产品到市场销售的变化终点','to','prep')
r.word('P4-S3','More','程度更近（more recently）','more','adv')
r.word('P4-S4','is','处于成功状态','be','v')
r.word('P4-S4','for','面向随后列举的产品','for','prep')
r.word('P5-S1','is','联系概念与难解释的状态','be','v')
r.word('P5-S2','to','食品获得改善的对象','to','prep')
r.word('P5-S2','some','一些（生产商）','some','a')
r.word('P5-S2','have','含有；拥有','have','v')
r.word('P6-S1','that','从句连接词，引出押注内容','that','conj')
r.word('P6-S1','for','为产品特点支付更高价格','for','prep')
r.word('P6-S1','as','例如（such as）','as','prep')
r.word('P6-S2','that','从句连接词，引出调查结果','that','conj')
r.word('P6-S2','some','部分（植物肉成功原因）','some','pron')
r.word('P6-S2','are','联系年轻人与关注气候的状态','be','v')
r.word('P6-S2','be','构成被动语态（be chalked up）','be','aux')
r.word('P6-S2','to','归因的对象（chalk up to）','to','prep',occ=1)
r.word('P6-S4','beyond','超出；超过某个程度','beyond','prep')
r.word('P6-S4','what','他们所能理解的程度','what','pron',occ=1)
r.word('P6-S4','what','他们正在做的事情','what','pron',occ=2)
r.word('P4-S2','more','超过（十年）','more','adv')
r.word('P6-S1','more','更多的钱','more','pron')
r.word('P6-S2','more','更加','more','adv')
r.word('P6-S3','Egg','Egg Innovations公司名的一部分','Egg','name')
r.word('P6-S4','are','构成进行时（are altering）','be','aux')
r.word('P6-S4',"they're",'他们正在（they are，与doing构成进行时）','they are','aux')
r.sentence('P2-S2')['chunks'][0]['zh']='这类鸡蛋可以被推销，'
r.sentence('P2-S2')['chunks'][1]['zh']='以有助于应对气候变化为卖点。'
r.sentence('P5-S2')['chunks'][0]['zh']='这种耕作方式还会带来，'
r.sentence('P5-S2')['chunks'][1]['zh']='即便有也微乎其微的改善，'
r.sentence('P6-S4')['chunks']=chunks(r,'P6-S4','beyond what','“他们确实正在改变食品供应链，|其程度甚至超出了我认为他们自己能够理解的范围。”')
done(r,{
'P1-S1':'roam为四处走动，over为活动范围，acres英亩与地点后置修饰对应。',
'P1-S2':'Some指部分鸡，shade为阴凉处非颜色深浅，parked为停放着的。',
'P1-S3':'Others为另一些鸡，with cows指与牛一起而非用牛饮水。',
'P1-S4':'by design为有意安排，行业规模61亿美元，what连接押注的新产品。',
'P2-S1':'每打高达8美元，a表示每；using修饰农场、that trap修饰土壤。',
'P2-S2':'marketed为宣传销售，as表卖点，将为的解释保留到实际as原块。',
'P3-S1':'cover crops为覆盖作物，draw为吸引，for chickens to eat为供鸡啄食。',
'P3-S2':'waste是鸡粪而非浪费，fertilizes为给农田增肥，then承接觅食过程。',
'P3-S3':'forage for为觅食，feed名词饲料，good for有益于与supply to顾客分开。',
'P4-S1':'premium为形容词高端非保险费，offering为上市商品，whether保留能否检验。',
'P4-S2':'from…to表市场地位转变，niche为小众，dismissed非解雇，Walmart销售地点。',
'P4-S3':'exploded为迅速发展，both指益生菌和植物肉，categories为超市商品类别。',
'P4-S4':'成功推广是条件，open floodgates比喻引发大规模产品涌入，beyond为更多产品。',
'P5-S1':'hard sell是不好卖，define是解释清概念，associate professor为副教授。',
'P5-S2':'if any强调可能没有改善，移除首块提前译入improvement，蛋白质仅为商家声称。',
'P6-S1':'premium修饰产品特点，free-range等完整复合词，行业押注同批顾客接受可持续性。',
'P6-S2':'chalk up to为归因，signal为表明环保意愿，to分别为归因对象与不定式。',
'P6-S3':'president为公司总裁非国家总统，planet为地球，care about表关心。',
'P6-S4':'food chain为食品供应链，beyond为超出程度，合并嵌套修饰避免逐块中文重复扭曲。'})
