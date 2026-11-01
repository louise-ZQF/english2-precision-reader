from audit_early_base import *
r=article('2012-T4','''
great~great~a=严重的；大（Great Recession指经济大衰退）
high~high~a=高的
joblessness~joblessness~n=失业率高企；失业状态
beginning~begin~v=开始
ends~end~v=结束
life~life~n=人生
course~course~n=轨迹；发展进程
character~character~n=特征
 generation~generation~n=一代人
adults~adult~n=成年人
ultimately~ultimately~adv=最终；从长远看
reshape~reshape~v=重塑
politics~politics~n=政治
culture~culture~n=文化
society~society~n=社会
tries~try~v=努力尝试
harder~hard~adv=更努力地
jobless~jobless~n=失业者（the jobless）
silver~silver~a=银色的（silver linings比喻一线希望）
linings~lining~n=内衬（silver linings整体比喻积极面）
national~national~a=全国性的
disaster~disaster~n=灾难
unemployment~unemployment~n=失业
extremely~extremely~adv=极其
painful~painful~a=痛苦的
improved~improve~v=改善
materialistic~materialistic~a=物质至上的
financially~financially~adv=在理财方面
prudent~prudent~a=谨慎节制的
aware~aware~a=意识到的；能体会的
struggles~struggle~n=艰难处境；挣扎
others~other~pron=其他人
limited~limited~a=有限的
respects~respect~n=方面
perhaps~perhaps~adv=也许
leave~leave~v=使……处于某种状况
better~well~a=更好的（better off为处境更好）
awoken~awake~v=唤醒
fever~fever~n=狂热（比喻）
dream~dream~n=幻想
riches~riches~n=财富
bigger~big~a=更大的
necessary~necessary~a=必要的
end~end~n=结束
reckless~reckless~a=不计后果的
personal~personal~a=个人的
spending~spending~n=消费；支出
benefits~benefit~n=好处
thin~thin~a=微弱的；不足以令人信服的
uncertain~uncertain~a=不确定的
consequences~consequence~n=后果
historian~historian~n=历史学家
benjamin~Benjamin~name=本杰明
friedman~Friedman~name=弗里德曼（姓氏）
argues~argue~v=指出；论述
u.s.~United States~name=美国
lengthy~lengthy~a=长期的
periods~period~n=时期
stagnation~stagnation~n=经济停滞
decline~decline~n=经济衰退
left~leave~v=使……变得
mean-spirited~mean-spirited~a=刻薄狭隘的
inclusive~inclusive~a=包容的
reversed~reverse~v=逆转；使倒退
advance~advance~n=进步
freedoms~freedom~n=自由
anti-immigrant~anti-immigrant~a=排斥移民的
sentiment~sentiment~n=情绪
typically~typically~adv=通常
conflict~conflict~n=冲突
races~race~n=种族
classes~class~n=社会阶层
income~income~n=收入
inequality~inequality~n=不平等；差距
falls~fall~v=下降；缩小
shrunk~shrink~v=缩小
indeed~indeed~adv=事实上
period~period~n=时期
weakness~weakness~n=经济疲软
reinforce~reinforce~v=加强；加深
class~class~n=社会阶层
divides~divide~n=分隔；阶层鸿沟
decrease~decrease~v=减少
opportunities~opportunity~n=机会
cross~cross~v=跨越
especially~especially~adv=尤其
research~research~n=研究
till~Till~name=蒂尔（人名）
von~Von~name=冯（人名的一部分）
wachter~Wachter~name=瓦赫特（姓氏）
economist~economist~n=经济学家
columbia~Columbia~name=哥伦比亚（大学名称的一部分）
suggests~suggest~v=表明
 graduating~graduate~v=毕业
chances~chance~n=机会；机遇
dimmed~dim~v=使黯淡；削弱
elite~elite~a=顶尖的
universities~university~n=大学
catch~catch~v=追赶（catch up）
fairly~fairly~adv=相当
quickly~quickly~adv=迅速地
otherwise~otherwise~adv=假如没有在衰退时毕业
where~where~adv=所处的状态或水平
 graduated~graduate~v=毕业
masses~mass~n=普通大众；大多数普通毕业生
beneath~beneath~prep=在……之下（相对教育层次）
behind~behind~adv=在后面（left behind为被落下）
internet~internet~n=互联网
resentment~resentment~n=怨恨；不满
hidden~hide~v=隐藏
difficult~difficult~a=困难的
moment~moment~n=眼下；当前时刻
discerning~discern~v=辨明
precisely~precisely~adv=准确地
lean~lean~a=经济困难的
society's~society~n=社会的
affecting~affect~v=影响
socially~socially~adv=在社会层面
tolerant~tolerant~a=宽容的
entering~enter~v=进入
variety~variety~n=多种；若干种
polls~poll~n=民意调查
shown~show~v=显示；得出
mixed~mixed~a=并不一致的
wait~wait~v=等待
exactly~exactly~adv=确切地；究竟
hard~hard~a=困难的
fabric~fabric~n=结构；关系网络（比喻）
extend~extend~v=持续；延长
''')
inherit(r,['2010-T1','2010-T2','2010-T3','2010-T4','2011-T1','2011-T2','2011-T3','2011-T4','2012-T1','2012-T2','2012-T3'])
r.sentence('P2-S1')['chunks'][1]['zh']='努力寻找这场全国性经济灾难中的一线希望'
r.word('P1-S1','over','结束的',pos='a');r.word('P1-S1','is','现在进行时助动词（is beginning）',lemma='be',pos='aux')
r.word('P1-S2','before','在……以前（高失业时期结束前）',pos='conj');r.word('P1-S2','character','性格（年轻一代的性格）',pos='n')
r.word('P1-S3','for','持续（多年）',pos='prep')
r.word('P2-S1','no','没有（no one为没有人）',pos='det');r.word('P2-S1','one','一个人（no one为没有人）',pos='pron')
r.word('P2-S2','many','许多人（省略名词people）',pos='pron');r.word('P2-S2','while','虽然（让步）',pos='conj');r.word('P2-S2','they','他们（失业者）',lemma='they',pos='pron')
r.word('P2-S3','off','与better构成境况更好',pos='part')
r.word('P2-S4','it','它（这场经济衰退）',pos='pron');r.word('P2-S4','to','结束……（put an end to）',pos='prep');r.word('P2-S4','us','我们（美国社会公众）',lemma='we',pos='pron')
r.word('P3-S1','off','遥远的（far off整体为远未实现）',pos='adv')
r.word('P3-S2','inside','在……内部',pos='prep');r.word('P3-S2','outside','在……外部',pos='prep');r.word('P3-S2','rights','权利',lemma='right',pos='n')
r.word('P3-S3','as','同样（引出冲突也增加）',pos='conj');r.word('P3-S3','does','代替前文increases的助动词',lemma='do',pos='aux')
r.word('P4-S1','it','它（收入差距）',pos='pron');r.word('P4-S1','one','一次（这次经济衰退）',pos='pron')
r.word('P4-S2','them','它们（阶层鸿沟）',lemma='they',pos='pron')
r.word('P4-S3','that','引出研究结果',pos='conj',occ=1);r.word('P4-S3','all','所有人（not all为并非所有）',pos='det');r.word('P4-S3','to','到（追赶到的水平）',pos='prep');r.word('P4-S3','left','被落下（left behind）',lemma='leave',pos='v');r.word('P4-S3','are','被动助动词（are left）',lemma='be',pos='aux');r.word('P4-S3','them','他们（名校毕业生）',lemma='they',pos='pron');r.word('P4-S3','it','强调句形式主语',pos='pron')
r.word('P5-S1','it','形式主语，指看见社会怨恨这件事',pos='pron')
r.word('P5-S2','are','现在进行时助动词（are affecting）',lemma='be',pos='aux')
r.word('P5-S4','have','have to表示不得不、需要',lemma='have',pos='v')
r.word('P5-S5','they','这些困难时期',lemma='they',pos='pron');r.word('P5-S5','it','它（社会结构与关系）',pos='pron');r.word('P5-S5','all','与the more so构成更加如此的程度强调',pos='adv')
phrase(r,'P2-S4','put a necessary end to','put an end to','给……画上必要的句号；结束')
phrase(r,'P5-S4','wait and see','wait and see','等待观察；拭目以待')
checks(r,[
'大衰退也许结束但高失业时代可能刚开始，两个推测与转折完整。',
'it指高失业时代；character本句为年轻人性格而非之后社会特征。',
'重塑政治文化社会的持续时间为多年，for为时长。',
'No one harder than表示失业者最努力；第二中文块补回原缺的寻找动作。',
'失业者自述某些改善不是作者断言普遍好处，while让步痛苦保留。',
'有限方面与perhaps双限制，better off为境况改善非单纯更富裕。',
'衰退唤醒狂热消费梦，put an end to为结束时代非放置物品。',
'好处微弱不定且遥远，far off非表示向远处移动。',
'长期停滞衰退会令社会狭隘少包容且阻逆权利进步；国内外都适用。',
'as does倒装为冲突同样增加，非因果；classes为社会阶层。',
'通常衰退减收入差距但本次未减，one指一次衰退。',
'阶层分隔被强化且跨越机会下降，them指分界非年轻人。',
'not all为并非所有；名校追赶本可达到水平，普通毕业生被落下，反事实条件不漏。',
'互联网更易显露既有怨恨，不是网络新创造全部怨恨。',
'倒装more difficult is还原，lean为经济困难，character为社会特征。',
'入衰退时美国比以往更包容，但随后民调结果混杂，不可断言单向恶化。',
'等待观察具体怎样重塑，have to为需要，fabric比喻社会结构非布料。',
'肯定将重塑且持续越久越深，all the more程度不按全部逐字译。'])
r.lex('''
both~both~adv=两者都（美国国内与国外）
degrees~degree~n=学位
easy~easy~a=容易的
far~far~adv=遥远地
find~find~v=寻找
history~history~n=历史
houses~house~n=住宅
how~how~adv=如何
less~little~adv=较不；更少地
longer~long~adv=更久
said~say~v=说
social~social~a=社会的
these~these~det=这些
those~those~pron=那些人
time~time~n=时期
times~time~n=时期
''')
r.word('P4-S3','better','经济形势较好的',lemma='good',pos='a')
phrase(r,'P1-S1','great recession','Great Recession','经济大衰退')
phrase(r,'P1-S2','life course','life course','人生轨迹')
phrase(r,'P4-S1','Income inequality','income inequality','收入不平等；收入差距')
phrase(r,'P4-S2','class divides','class divide','阶层鸿沟')
r.word('P4-S3','up','与catch构成“追赶上（原本生活进度）”',lemma='up',pos='part')
gaps(r)
if not r.missing():r.save()
