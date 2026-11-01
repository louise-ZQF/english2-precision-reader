# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2016-T4'),['2015-T1','2015-T2','2015-T3','2015-T4','2016-T1','2016-T2','2016-T3'])

lex(r,'''against/prep=在……背景下（against a backdrop）;backdrop/n=背景;drastic/a=剧烈的；重大的;changes@change/n=变化;population/n=人口;structure/n=结构;americans@American/n=美国人;drawing@draw/v=绘制;new/a=新的;21st-century/a=二十一世纪的;road/n=道路（road map比喻路线规划）;map/n=图；规划;success/n=成功;latest@late/a=最新的;poll/n=民意调查;across/prep=跨越；不分（世代）;generational/a=代际的；世代的;lines@line/n=界限；分界;continue/v=继续;prize/v=珍视；重视;same/a=相同的;milestones@milestone/n=里程碑；标志性事件;successful/a=成功的;including@include/prep=包括;getting@get/v=开始处于某状态（get married/started）;married/a=已婚的（get married结婚）;having@have/v=生育（孩子）;owning@own/v=拥有;home/n=住房；家庭;retiring@retire/v=退休;sixties/n=六十多岁;young/a=年轻的;old/a=年长的;mostly/adv=大体上；主要地;agree/v=同意；意见一致;constitutes@constitute/v=构成；算作;finish/n=终点（finish line）;line/n=线（finish line为终点线）;offer/v=提出；给出;strikingly/adv=显著地；鲜明地;paths@path/n=路径；途径;reaching@reach/v=达到；实现;prioritize/v=优先考虑;believe/v=认为；相信;careers@career/n=职业发展;regularly/adv=经常地；定期地;changing@change/v=更换；改变;favor/v=偏爱；赞同;communities@community/n=社区;public/a=公共的;services@service/n=服务;couples@couple/n=夫妇；伴侣;financially/adv=经济上;secure/a=稳定有保障的;maintain/v=主张；坚持认为;best@well/adv=最有利地；最好地;served@serve/v=利益得到满足或照顾;two/num=二;parents@parent/n=父母;working@work/v=工作;outside/prep=在……之外;work/n=工作;by/prep=通过；由;community/n=社区;contrasts@contrast/n=差异；对照;suggest/v=表明;aftermath/n=后果；事后时期;searing/a=造成深重痛苦的;great@Great/a=大（Great Recession特指大衰退）;starting@start/v=开始；起步;out/adv=开始开展（start out）；出去;defining@define/v=界定；确立;priorities@priority/n=优先事项;expectations@expectation/n=期望;spread/v=扩散；传播;virtually/adv=几乎；差不多;aspects@aspect/n=方面;american/a=美国的;consumer/n=消费者;preferences@preference/n=偏好;housing/n=住房;patterns@pattern/n=模式;politics/n=政治;converge/v=趋于一致；取得一致;one/num=一个;key/a=关键的;point/n=问题；要点;overwhelming/a=压倒性的；极大的;majorities@majority/n=大多数;get/v=开始；进入某状态（get started）;generations@generation/n=几代人；世代;somewhat/adv=有点；稍微;elders@elder/n=长辈；年长者;prospects@prospect/n=前景;big/a=大的（此处修饰多数，意为绝大多数）;tougher@tough/a=更艰难的;climb/n=攀登；比喻奋斗历程;signpost/a=标志性的;achievements@achievement/n=成就;securing@secure/v=获得;good-paying/a=薪酬不错的;job/n=工作;debt/n=债务;finding@find/v=找到;affordable/a=负担得起的;pete@Pete/name=皮特（人名）;schneider@Schneider/name=施奈德（姓氏）;considers@consider/v=认为;year-old/a=……岁的;27-year-old/a=27岁的;auto/n=汽车（作定语）;technician/n=技师;chicago@Chicago/name=芝加哥（城市名）;suburbs@suburb/n=郊区;struggled@struggle/v=艰难地努力;find/v=找到;graduating@graduate/v=毕业;steadily/adv=稳定地;afford/v=负担得起;monthly/a=每月的;mortgage/n=房屋抵押贷款；房贷;payments@payment/n=还款；支付款项;rent/v=出租;rooms@room/n=房间;make/v=使；让;happen/v=发生；实现;back/adv=回头；回顾;struck@strike/a=惊讶的；深受触动的;provide/v=提供;comfortable/a=舒适富足的;though/conj=尽管（even though）;neither/pron=两者都不（指父母双方）；无一;grew@grow/v=成长；长大;up/adv=长大成人（grow up）；成长;upper/a=上层的；较高的;degrees@degree/n=学位;think/v=认为;capable/a=有能力的;anymore/adv=再；如今不再（与否定连用）''')
r.word('P1-S1','are','助动词，与drawing构成进行时',lemma='be',pos='aux');r.word('P1-S1','to','通向（成功）',pos='prep')
r.word('P2-S1','in','在六十多岁时',pos='prep')
r.word('P2-S2','while','虽然；尽管',pos='conj');r.word('P2-S2','young','年轻人（形容词名词化）',pos='n');r.word('P2-S2','old','老年人（形容词名词化）',pos='n');r.word('P2-S2','on','在……问题上意见一致',pos='prep');r.word('P2-S2','for','用于达到目标（paths for reaching）',pos='prep');r.word('P2-S2','it','圆满人生的目标',pos='pron')
r.word('P3-S1','are','助动词，与getting构成进行时',lemma='be',pos='aux',occ=1);r.word('P3-S1','are','助动词，与served构成被动语态',lemma='be',pos='aux',occ=2);r.word('P3-S1','by','通过经常换工作',pos='prep',occ=1);r.word('P3-S1','by','由（双亲外出工作带来益处）',pos='prep',occ=2);r.word('P3-S1','more','更多的（公共服务）',pos='det',occ=2);r.word('P3-S1','most','最能；最大程度地（推进事业）',pos='adv')
r.word('P4-S1','to','到；及至（from...to...列举范围）',pos='prep');r.word('P4-S1','are','助动词，与defining构成进行时',lemma='be',pos='aux');r.word('P4-S1','that','关系代词，指优先事项与期望',pos='pron',occ=2);r.word('P4-S1','through','遍及；传遍',pos='prep');r.word('P4-S1','just','刚刚',pos='adv')
r.word('P5-S1','young','年轻人',pos='n');r.word('P5-S1','old','老年人',pos='n');r.word('P5-S1','for','对……而言',pos='prep');r.word('P5-S1','earlier','以前的；较早的',lemma='early',pos='a');r.word('P5-S1','it','形式主语，指人生起步这件事',pos='pron')
r.word('P5-S2','while','虽然；尽管',pos='conj');r.word('P5-S2','for','对于人生起步者而言',pos='prep');r.word('P5-S2','just','刚刚',pos='adv');r.word('P5-S2','face','面对；面临',pos='v');r.word('P5-S2','earlier','以前的；较早的',lemma='early',pos='a');r.word('P5-S2','as','例如（such...as）',pos='prep');r.word('P5-S2','starting','组建（家庭）；开始',lemma='start',pos='v',occ=2)
r.word('P6-S3','now','与that组成既然如今；目前已经',pos='adv');r.word('P6-S3','that','与now组成now that，交代目前的情况',pos='conj',occ=1);r.word('P6-S3','is','与working构成进行时',lemma='be',pos='aux');r.word('P6-S3','on','与my own组成独自地',pos='prep');r.word('P6-S3','own','自己（on my own为独自）',pos='pron');r.word('P6-S3','so','所以',pos='conj');r.word('P6-S3','have','必须（have to）',pos='aux');r.word('P6-S3','out','出租出去（rent out）',pos='adv');r.word('P6-S3','to','租给（某人）',pos='prep',occ=3);r.word('P6-S3','that','还清每月房贷这件事',pos='pron',occ=2)
r.word('P6-S4','looking','回顾（look back）',lemma='look',pos='v');r.word('P6-S4','is','系动词，说明受到触动的状态',lemma='be',pos='v');r.word('P6-S4','for','为孩子提供',pos='prep');r.word('P6-S4','even','与though组成即使；尽管',pos='adv');r.word('P6-S4','could','能够（过去父母有能力）',pos='aux')
r.word('P6-S5','have','拥有（学位）',pos='v');r.word('P6-S5','home','家庭（阶层背景）',pos='n');r.word('P6-S5','with','有这样的父母；伴随父母背景',pos='prep')
r.word('P6-S6','that','父母无大学学位也能维持中上阶层生活这件事',pos='pron');r.word('P6-S6','of','具备做某事的能力（capable of）',pos='prep')
checks(r,'''against a backdrop表背景而非反对，drawing是绘制成功路线比喻。
across generational lines为跨代共识，prize动词珍视，sixties为六十多岁。
while让步，young/old名词化，两代人终点相似但路径不同。
长句五项观点皆来自调查群体；best served双亲外出工作须保留原文而非常识改写。
that后者指优先事项与期望，through为扩散遍及，virtually为几乎而非虚拟地。
两代人在起步更难上达成共识，earlier为较早世代，for为对谁而言。
while是略乐观但仍认为更艰难的让步，as列举标志成就，climb为奋斗比喻。
considers为认为，tougher是比较而非绝对最难。
27-year-old为年龄，汽车技师从芝加哥郊区来，毕业后求职艰难。
have to为必须，on my own为独自，rent out为出租，that指偿还房贷。
look back为回顾，struck为惊讶不是击打，neither指父母两人均无毕业。
have为拥有学位，不是完成时助动词；still形成父母背景与家庭阶层反差。
think否定迁移保持原意，that回指无学历仍能养家的生活，非连接词。''')
r.notes=['逐词复核世代差异长句、原文五项观念、年龄与家庭经济比较；所有词义、原形和词性按出现位置保存。']
save(r)
