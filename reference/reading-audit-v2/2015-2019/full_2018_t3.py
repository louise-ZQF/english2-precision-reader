# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2018-T3'),[f'{y}-T{n}' for y in [2015,2016,2017] for n in range(1,5)]+['2018-T1','2018-T2'])

lex(r,'''power/n=权力；实力;ambition/n=野心；雄心;astonishing/a=令人吃惊的;amazon@Amazon/name=亚马逊（公司名）;purchase/n=收购；购买;upmarket/a=高端的;grocery/n=食品杂货;foods@Foods/name=全食超市名称Whole Foods的一部分;paid@pay/v=支付;acquire/v=收购；取得;whatsapp@WhatsApp/name=WhatsApp（即时通信服务名）;messaging/n=即时消息通信;physical/a=实体的;product/n=产品；商品;intricate/a=错综复杂的;finely/adv=精细地;detailed/a=详尽的;web/n=关系网络;users@user/n=用户;friendships@friendship/n=朋友关系;promised@promise/v=承诺;european/a=欧洲的（European Commission指欧盟委员会）;commission/n=委员会;phone/n=电话;numbers@number/n=号码;identities@identity/n=身份;broke@break/v=违背（承诺）；破坏;promise/n=承诺;soon/adv=很快；立刻;deal/n=交易；收购交易;went@go/v=获准；完成（go through）；通过;through/adv=完成；顺利通过（go through）;knowing@know/v=了解；知道;messages@message/n=消息；通信内容;sent@send/v=发送;whom/pron=谁（宾格，指消息接收者）;enormously/adv=极大地；非常;revealing/a=能揭示重要情况的;journalist/n=记者;party/n=政党;whip/n=党鞭（负责议员党纪及投票的职务）;know/v=知道；了解;makeup/n=组成；成员构成;theresa@Theresa/name=特雷莎（人名）;may's@May/name=梅的（姓氏所有格）;enemies@enemy/n=政敌；对手;currently/adv=目前;plotting@plot/v=秘密谋划;shops@shop/n=门店;owns@own/v=拥有;records@record/n=记录;customers@customer/n=客户；顾客;purchased@purchase/v=购买;competition/n=竞争（competition law为竞争法）;law/n=法律;address/v=处理；应对;imbalances@imbalance/n=失衡;way/n=途径；办法;clumsy/a=笨拙的；不灵活的;one/num=一个;slow/a=缓慢的;compared@compare/v=与……相比;change/n=变化;within/prep=在……之内;by/prep=到……时；由;time/n=时间；时刻;addressed@address/v=处理;remedied@remedy/v=纠正；补救;vanished@vanish/v=消失;marketplace/n=市场;replaced@replace/v=被替代；取代;new/a=新的;abuses@abuse/n=滥用权力的行为;deeper@deep/a=更深层的;conceptual/a=概念上的;too/adv=也;presently/adv=目前;interpreted@interpret/v=解释；适用（法律）；deals@deal/v=处理（deal with）；涉及;disadvantage/n=不利；损害;consumers@consumer/n=消费者;advertising/n=广告;google@Google/name=谷歌（公司名）;virtual/a=网络上的；数字世界的;dominate/v=主导；支配;media@nmedium/n=媒体;entertainment/n=娱乐;they're@they be/aux=they are缩写，与selling构成进行时；它们正在;convert/v=转化;ants@ant/n=蚂蚁;farm/v=饲养（比喻培育用户以获取数据）;bugs@bug/n=昆虫；小虫;aphids@aphid/n=蚜虫;honeydew/n=蜜露（蚜虫分泌的含糖液体）;feed/v=进食；觅食;farms@farm/v=饲养；以获取数据为目的培育（比喻）;yield/v=产生；产出;predatory/a=捕食性的;insects@insect/n=昆虫;away/adv=远离；赶走;gmail@Gmail/name=Gmail（电子邮箱服务名）;spammers@spammer/n=垃圾邮件发送者;inboxes@inbox/n=收件箱;out/adv=在外面；排除在外;like/prep=像……一样;democratic/a=民主的；以平等参与为基础的;relationship/n=关系;sides@side/n=双方中的一方'''.replace('；deals@deal',';deals@deal').replace('media@nmedium','media@medium'))
r.word('P1-S1','just','刚刚',pos='adv');r.word('P1-S1','chain','连锁店；连锁经营体系',pos='n');r.word('P1-S1','whole','Whole Foods品牌名的一部分，中文全食',lemma='Whole',pos='name');r.word('P1-S1','for','以……价格（收购金额）',pos='prep');r.word('P1-S1','that','前面亚马逊收购全食的金额',pos='pron');r.word('P1-S1','have','拥有（实体产品）',pos='v');r.word('P1-S1','service','服务（即时通信服务）',pos='n');r.word('P1-S1','at','与all组成根本、完全',pos='prep');r.word('P1-S1','all','与not at构成根本没有',pos='adv')
r.word('P1-S2','social','社交的',pos='a');r.word('P1-S2','lives','生活',lemma='life',pos='n')
r.word('P2-S1','then','当时',pos='adv');r.word('P2-S1','link','关联；绑定',pos='v');r.word('P2-S1','to','把号码与身份关联（link...to）',pos='prep');r.word('P2-S1','as','与soon as组成一……就……',pos='conj')
r.word('P2-S2','who','谁（引出发送者信息，不是定语关系词）',pos='pron');r.word('P2-S2','knowledge','所掌握的信息；了解的情况',pos='n');r.word('P2-S2','to','给（消息接收者）',pos='prep')
r.word('P2-S3','what','哪个（反问，限定记者或党鞭）',pos='det');r.word('P2-S3','are','与plotting构成进行时',lemma='be',pos='aux')
r.word('P2-S4','it','形式主语，指后文关于价值的判断',pos='pron',occ=1);r.word('P2-S4','it','全食超市',pos='pron',occ=2);r.word('P2-S4','whole','Whole Foods全食超市品牌的一部分',lemma='Whole',pos='name');r.word('P2-S4','to','对于亚马逊而言',pos='prep');r.word('P2-S4','which','哪些（限定customers，间接疑问）',pos='det');r.word('P2-S4','what','什么东西（购买对象）',pos='pron');r.word('P2-S4','but','与其……不如……中的后项',pos='conj')
r.word('P3-S1','only','唯一的',pos='a')
r.word('P3-S3','for','与one thing组成首先',pos='prep');r.word('P3-S3','to','与……相比（compared to）',pos='prep')
r.word('P3-S4','been','与addressed/remedied构成被动语态',lemma='be',pos='aux');r.word('P3-S4','be','与replaced构成被动语态',pos='aux')
r.word('P3-S5','there','存在句引导词',pos='pron');r.word('P3-S5','is','有；存在（there is）',lemma='be',pos='v')
r.word('P3-S6','as','按……解释方式',pos='conj');r.word('P3-S6','with','处理（deal with）中的搭配介词',pos='prep');r.word('P3-S6','to','消费者受到的（不利）',pos='prep');r.word('P3-S6','for','为服务付费（pay for）',pos='prep');r.word('P3-S6','this','消费者的经济损失',pos='pron')
r.word('P3-S8','that','真正的客户（承接前句的customers）',pos='pron');r.word('P3-S8','buy','购买（广告）',pos='v');r.word('P3-S8','to','造成不利结果（to the disadvantage of）',pos='prep')
r.word('P4-S1','to','把生活转化为数据（convert...to）',pos='prep');r.word('P4-S1','benefit','利益；益处',pos='n')
r.word('P4-S2','as','正如（just as...so类比）',pos='conj');r.word('P4-S2','so','同样地（与just as对应）',pos='adv');r.word('P4-S2','called','叫作；名为',lemma='call',pos='v');r.word('P4-S2','that','关系代词，指data',pos='pron')
r.word('P4-S3','keep','使……远离（keep away）',pos='v');r.word('P4-S3','keeps','阻挡；使……在外（keep out）',lemma='keep',pos='v')
r.word('P4-S4','human','尊重人的；人性化的',pos='a');r.word('P4-S4','if','与even组成即使',pos='conj')
checks(r,'''135亿美元收购全食与更高价收购WhatsApp分清，that指金额，physical是实体。
web为用户社交关系网，lives为生活非生命数，what引提供的内容。
link是动词绑定，then当时，as soon as一……就，go through交易完成。
who与whom是发送和接收者的间接疑问，still不是将来。
what反问哪个，makeup为成员构成，党鞭whip并非鞭子。
which customers是哪些顾客，not so much...but为价值重心对比。
address动词处理，power为权力，only形容唯一。
it指竞争法，clumsy指法律工具应对不灵活。
compared to比较反应速度，for one thing为首先。
问题解决时旧问题已消失又被新滥权替代，完成被动与结果不定式分清。
还有概念问题，too为也，there is存在句。
as为按目前解释，deal with为处理，this指经济损失，pay for服务付费。
免费服务使用者与广告付费客户不是同一群体，not保留。
That指真正客户，buy为购买，virtual为网络上的，结果使其他媒体不利。
product为出售产品，benefit名词利益，convert to转化为。
just as...so类比蚂蚁养蚜虫与谷歌获取数据，called为名叫。
keep away赶走捕食者，keep out挡垃圾邮件，延续保护与养育类比。
human为尊重人的主体地位，even if让步仍保持作者批评。''')
r.notes=['独立再审免费用户与广告客户的区分、法律经济损失与数据权力比喻；所有词位置核定，无词典自动义项冒充。']
save(r)
