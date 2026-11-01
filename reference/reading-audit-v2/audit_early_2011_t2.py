from audit_early_base import *
r=article('2011-T2','''
whatever~whatever~pron=究竟；到底（反问曾预言的情况怎么没了下文）
happened~happen~v=发生
death~death~n=消亡（报纸衰亡的比喻）
newspapers~newspaper~n=报纸；报社
seemed~seem~v=似乎
near~near~a=近的；即将到来的
recession~recession~n=经济衰退
threatened~threaten~v=威胁着；可能导致
remove~remove~v=夺走；使失去
advertising~advertising~n=广告收入或业务
readers~reader~n=读者
fled~flee~v=转移；逃离
internet~internet~n=互联网
like~like~prep=例如；像……这样的
san~San~name=San Francisco（旧金山）地名的一部分
francisco~Francisco~name=San Francisco（旧金山）地名的一部分
chronicle~Chronicle~name=《纪事报》（报纸名称的一部分）
chronicling~chronicle~v=记录；报道
own~own~a=自身的
doom~doom~n=衰亡；毁灭
america's~America~name=美国的
federal~federal~a=联邦的
trade~trade~n=贸易
commission~commission~n=委员会
launched~launch~v=发起
round~round~n=一轮
talks~talk~n=讨论；会谈
save~save~v=拯救
become~become~v=成为
charitable~charitable~a=慈善性质的
corporations~corporation~n=公司
state~state~n=政府
subsidize~subsidize~v=给予财政补贴
hold~hold~v=召开
another~another~det=另一个；又一次
meeting~meeting~n=会议
soon~soon~adv=不久
discussions~discussion~n=讨论
now~now~adv=如今
seem~seem~v=似乎
date~date~n=时效（out of date为过时）
little~little~det=几乎没有
sign~sign~n=迹象
crisis~crisis~n=危机
german~German~a=德国的
brazilian~Brazilian~a=巴西的
papers~paper~n=报纸；报社
shrugged~shrug~v=摆脱；不受影响（shrug off）
off~off~part=与shrugged构成摆脱
american~American~a=美国的
inhabit~inhabit~v=身处
troubled~troubled~a=陷入困境的
corner~corner~n=一部分；处境
 global~global~a=全球的
industry~industry~n=报业
survived~survive~v=存活下来
returned~return~v=恢复；回到
profit~profit~n=利润；盈利
margins~margin~n=利润率
routine~routine~a=常见的；惯常的
same~same~a=相同的（all the same整体为尽管如此）
fun~fun~n=愉快；乐趣
stayed~stay~v=保持
 afloat~afloat~a=维持经营的；未破产的
pushing~push~v=推（比喻裁员）
journalists~journalist~n=记者
overboard~overboard~adv=到船外（比喻被裁员出局）
society~society~n=协会
news~news~n=新闻
editors~editor~n=编辑
newsroom~newsroom~n=新闻编辑部
jobs~job~n=岗位
gone~go~v=消失；被裁撤
paying~pay~v=支付
slimmer~slim~a=更薄的；版面更少的
products~product~n=产品（这里指报纸）
nerve~nerve~n=胆量
refuse~refuse~v=拒绝
delivery~delivery~n=投递
distant~distant~a=偏远的
suburbs~suburb~n=郊区
yet~yet~conj=然而
desperate~desperate~a=迫于困境采取的
measures~measure~n=措施
proved~prove~v=证明是
right~right~a=正确的
ones~one~pron=那些（措施）
sadly~sadly~adv=令人难过的是
pushed~push~v=推行
further~far~adv=进一步
becoming~become~v=变得；成为
balanced~balanced~a=结构均衡的
businesses~business~n=企业
healthier~healthy~a=更健康的；更合理的
mix~mix~n=搭配；组合
revenues~revenue~n=营业收入
advertisers~advertiser~n=广告商
long~long~adv=长期以来
highly~highly~adv=极为
unusual~unusual~a=不同寻常的
reliance~reliance~n=依赖
ads~ad~n=广告
fully~fully~adv=整整；高达
came~come~v=来自
according~according~prep=与to构成据……所说
organization~organization~n=组织
economic~economic~a=经济的
cooperation~cooperation~n=合作
development~development~n=发展
oecd~OECD~name=经济合作与发展组织
japan~Japan~name=日本
proportion~proportion~n=比例
surprisingly~surprisingly~adv=令人意外地（not surprisingly为不出所料）
japanese~Japanese~a=日本的
stable~stable~a=稳定的
whirlwind~whirlwind~n=风暴（比喻剧烈冲击）
swept~sweep~v=席卷
newsrooms~newsroom~n=新闻编辑部
harmed~harm~v=伤害
 everybody~everybody~pron=所有人
damage~damage~n=损害
concentrated~concentrate~v=集中
areas~area~n=领域
where~where~adv=关系副词，指前面的领域
least~little~adv=最少；最不（独特）
distinctive~distinctive~a=有特色的
car~car~n=汽车
film~film~n=电影
reviewers~reviewer~n=评论员
science~science~n=科学
general~general~a=综合性的
business~business~n=商业
reporters~reporter~n=记者
foreign~foreign~a=驻外的
bureaus~bureau~n=分社；记者站
savagely~savagely~adv=大幅度地；猛烈地
cut~cut~v=裁撤
complete~complete~a=全面的
result~result~n=结果
completeness~completeness~n=面面俱到；全面性
longer~long~adv=更久（no longer为不再）
virtue~virtue~n=优点
''')
inherit(r,['2010-T1','2010-T2','2010-T3','2010-T4','2011-T1'])
r.word('P1-S1','to','对于……的情况（happened to）',pos='prep');r.word('P1-S1','the','特指曾被预言的报纸消亡',lemma='the',pos='art')
r.word('P1-S3','that','关系代词，指广告业务和读者',pos='pron');r.word('P1-S3','to','转向（互联网）',pos='prep',occ=2)
r.word('P1-S4','were','过去进行时助动词（were chronicling）',lemma='be',pos='aux')
r.word('P1-S6','they','它们（报社）',lemma='they',pos='pron')
r.word('P1-S7','them','它们（报社）',lemma='they',pos='pron')
r.word('P1-S8','it','它（联邦贸易委员会）',pos='pron')
r.word('P1-S9','out','out of date中的搭配成分，整体为过时',pos='part');r.word('P1-S9','of','out of date中的搭配成分，不单译',pos='prep')
r.word('P2-S1','much','大部分',pos='pron');r.word('P2-S1','there','there is存在结构形式成分',pos='pron');r.word('P2-S1','is','有；存在',lemma='be',pos='v')
r.word('P2-S3','but','不仅……而且……中的而且',pos='conj');r.word('P2-S3','to','恢复至（盈利状态）',pos='prep')
r.word('P2-S4','that','关系代词，指20%利润率',pos='pron');r.word('P2-S4','all','all the same中的成分，整体为尽管如此',pos='adv')
r.word('P3-S1','it','报业求生的过程',pos='pron')
r.word('P3-S2','by','通过；靠（裁员手段）',pos='prep')
r.word('P3-S4','are','现在进行时助动词（are paying）',lemma='be',pos='aux');r.word('P3-S4','for','购买（付钱所得的对象）',pos='prep')
r.word('P3-S5','had','有（have the nerve to为敢于）',lemma='have',pos='v');r.word('P3-S5','to','向（投递目的地）',pos='prep',occ=2)
r.word('P3-S6','be','被动助动词（be pushed）',lemma='be',pos='aux');r.word('P3-S6','they','这些措施',lemma='they',pos='pron');r.word('P3-S6','for','对……而言（记者的感受）',pos='prep')
r.word('P4-S1','are','现在进行时助动词（are becoming）',lemma='be',pos='aux')
r.word('P4-S2','on','对（广告的依赖）',pos='prep')
r.word('P4-S3','to','according to中的依据介词，整体为根据',pos='prep');r.word('P4-S3','for','组织名称中的连接词，不单译',pos='prep')
r.word('P5-S1','that','关系代词，指冲击风暴',pos='pron');r.word('P5-S1','been','完成时被动助动词（been concentrated）',lemma='be',pos='aux')
r.word('P5-S3','so','也是如此（承接同样被裁掉）',pos='adv')
r.word('P5-S4','been','完成时被动助动词（been cut off）',lemma='be',pos='aux');r.word('P5-S4','off','与cut构成裁撤',pos='part')
r.word('P5-S5','as','与a result构成因此',pos='prep')
phrase(r,'P1-S1','Whatever happened to','whatever happened to','说好的……怎么没下文了？')
phrase(r,'P1-S9','out of date','out of date','过时的')
phrase(r,'P4-S3','according to','according to','根据；据……所说')
checks(r,[
'反问报纸死亡预言怎么没了下文，并非直接询问某人死亡原因。',
'一年前末日似乎接近，与如今复苏形成时间对照。',
'广告读者仍未逃向互联网的限定不漏；fled转向不是实际逃难。',
'Chronicle报纸专名与chronicling记录双关分开，doom为自身衰亡。',
'联邦贸易委员会发起的是讨论轮次，trade为贸易不是交易换工作。',
'报社是否改慈善公司保留问句；they指报社。',
'state为政府非美国某一州，subsidize是财政补贴。',
'It为委员会，不是报社；another为另一次会议。',
'out of date为讨论已过时，不是日期超出范围。',
'世界大部分地区几乎无危机迹象，little保留否定数量。',
'shrugged off为摆脱衰退冲击，不是肩膀运动字面义。',
'not only but为不仅而且；困境最深的是美国报业部分，返回盈利未等于恢复旧利润率。',
'20%为过去惯常利润率，but profit all the same强调仍盈利。',
'It指求生过程不愉快，不是报纸没有娱乐内容。',
'船上求生隐喻对应裁减记者，afloat保持形容词状态。',
'自2007年以来消失13500岗位，gone不是转职去向不明。',
'花钱更多与报纸更薄形成反差，slimmer指版面不是身材。',
'had the nerve是竟敢，投递拒绝目标为偏远郊区。',
'已证明措施正确且可进一步推行；they为措施非记者。',
'均衡来自读者与广告收入结构，不是报道立场政治均衡。',
'长期不同寻常之处为广告依赖程度，ads即广告。',
'整整87%是广告收入比例，年份与OECD来源均保留。',
'日本35%承接广告收入占比，未偷换成读者占比。',
'not surprisingly否定意外，much more比较稳定程度。',
'风暴喻冲击；关系词where定位缺少独特性的业务领域。',
'汽车及影评岗位被裁，不是作品本身消失。',
'So have倒装承接同样被裁，科学及综合商业记者也受影响。',
'Foreign bureaus为驻外分社，cut off为大幅裁撤非断电。',
'less complete指报纸内容不再全面，结果关系明确。',
'no longer否定面面俱到是一项优点，virtue不是道德美德。'])
r.lex('''
end~end~n=末日；终结
few~few~det=一些（a few years指几年前）
how~how~adv=如何
less~little~adv=较不；较少
often~often~adv=常常；很多情况下
through~through~prep=穿过；席卷过
year~year~n=年
''')
gaps(r)
if not r.missing():r.save()
