# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2017-T4'),[f'{y}-T{n}' for y in [2015,2016] for n in range(1,5)]+[f'2017-T{n}'for n in [1,2,3]])

lex(r,'''viewed@view/v=看作;states@state/n=州;frequency/n=频率;wildfires@wildfire/n=野火；林地火灾;national/a=全国性的;concern/n=关切的问题;tax/n=税收;dollars@dollar/n=美元；资金;max@Max/name=马克斯（人名）;moritz@Moritz/name=莫里茨（姓氏）;specialist/n=专家;fire/n=火；火灾;ecology/n=生态学;forest/n=森林;half/n=一半;billion/num=十亿;budget/n=预算;fighting@fight/v=扑灭；对抗（火灾）;fires@fire/n=火灾;double/a=两倍的;percentage/n=百分比;efforts@effort/n=努力；工作;effect/n=实际效果（in effect为实际上）;funds@fund/n=资金;going@go/v=被用于；流向（资金）;towards/prep=用于；流向;agency's@agency/n=该机构的（所有格）;work/n=工作;watershed/n=流域;cultural/a=文化的;infrastructure/n=基础设施;upkeep/n=维护;nationwide/a=全国性的;construction/n=建设;fire-prone/a=易发生火灾的;districts@district/n=地区;building@build/v=建造;lost@lose/v=毁掉；失去;wildfire/n=野火;it's@it be/pron=这是（it is缩写）;already/adv=已经;huge/a=巨大的;expenditure/n=财政支出；开支;perspective/n=角度；视角;whole/a=整个的;country/n=国家;need/v=需要;take/v=拿；采用（放大镜比喻审视）;magnifying@magnify/a=放大的;glass/n=镜片（magnifying glass为放大镜）;like/adv=例如（口语引出例子）；好比;wait/v=等一下;minute/n=分钟（wait a minute为稍等）；片刻;ok@OK/a=合适的；可以接受的;redirect/v=重新调配；改变方向;concentrate/v=集中;lower-hazard/a=风险较低的;parts@part/n=地区；部分;require/v=需要;corresponding/a=相应的;shift/n=转变;way/n=方式;society/n=社会;views@view/v=看待;conversations@conversation/n=讨论;one/num=一个;inclusive/a=涵盖广泛的；全面的;over/prep=在……期间；对于（具体搭配）；decade/n=十年;focus/n=重点；关注;climate/n=气候;warming@warming/n=变暖;earth@Earth/name=地球;greenhouse/n=温室（greenhouse gases为温室气体）;gases@gas/n=气体;leading@lead/v=导致;conditions@condition/n=环境条件;worsen/v=加剧；使更糟;element/n=因素;shouldn't@should/aux=不应该;come/v=发生；出现（come at the expense of整体为以……为代价）;expense/n=代价（at the expense of）；费用;equation/n=问题的整体因素组合（比喻）；并非数学方程;human/a=人类的;systems@system/n=系统;landscapes@landscape/n=自然环境；地貌;live/v=生活;linked@link/v=关联；连接;go/v=发生作用；朝向;ways@way/n=方向;recognize/v=认识到;overly/adv=过度地;simplified@simplify/a=简化的;solutions@solution/n=解决办法;perception/n=认识；看法;limited/a=局限的;treat/v=看作；对待;event/n=事件;wholly/adv=完全地;controlled@control/v=控制;unleashed@unleash/v=释放；允许使用;necessity/n=必要性;balch@Balch/name=鲍尔奇（姓氏）;colorado@Colorado/name=科罗拉多（州名）;acknowledging@acknowledge/v=承认；正视;fire's@fire/n=火的（所有格）;inevitable/a=不可避免的;presence/n=存在;attitude/n=态度;crucial/a=至关重要的;laws@law/n=法律;policies@policy/n=政策;practices@practice/n=具体做法;make/v=使；让;safe/a=安全的;possible/a=可能的;we've@we have/pron=我们已……（we have缩写）；完成时;disconnected@disconnect/v=切断联系；疏离;ourselves/pron=我们自己;tease/v=梳理清楚（tease out）；仔细分离;out/adv=查明；梳理清楚（tease out）；出于（out of necessity）;time/n=时间；时刻;same/a=相同的'''.replace('；decade/n',';decade/n'))
r.word('P1-S1','though','虽然；尽管',pos='conj');r.word('P1-S1','for','对西部各州而言',pos='prep');r.word('P1-S1','growing','不断增加的',lemma='grow',pos='a');r.word('P1-S1','on','对于财政资金使用的影响',pos='prep')
r.word('P2-S1','US','美国（United States缩写）',lemma='US',pos='name');r.word('P2-S1','for','与the first time组成首次',pos='prep');r.word('P2-S1','than','与more组成超过',pos='prep')
r.word('P2-S2','in','与effect组成实际上',pos='prep');r.word('P2-S2','are','与going构成进行时',lemma='be',pos='aux');r.word('P2-S2','as','例如（such as）',pos='prep');r.word('P2-S2','that','关系代词，指其他公共管理工作',pos='pron')
r.word('P3-S1','are','与going构成进行时',lemma='be',pos='aux')
r.word('P3-S2','as','正如',pos='conj');r.word('P3-S2','puts','表达；说（put it）',lemma='put',pos='v');r.word('P3-S2','are','与building构成进行时',lemma='be',pos='aux',occ=1);r.word('P3-S2','that','关系代词，指homes',pos='pron');r.word('P3-S2','be','与lost构成被动语态',pos='aux');r.word('P3-S2','to','毁于（野火）',pos='prep',occ=2)
r.word('P4-S1','for','对全国而言',pos='prep')
r.word('P4-S2','that','前述财政资金使用问题',pos='pron');r.word('P4-S2','to','对准（放大镜），比喻审视的对象',pos='prep',occ=2)
r.word('P4-S4','instead','转而；改为',pos='adv')
r.word('P5-S1','US','美国（United States缩写）',lemma='US',pos='name')
r.word('P6-S1','for','与one thing组成首先',pos='prep')
r.word('P6-S2','over','在过去十年期间',pos='prep');r.word('P6-S2','change','变化（climate change为气候变化）',pos='n');r.word('P6-S2','is','与leading构成进行时',lemma='be',pos='aux');r.word('P6-S2','to','导致（lead to）',pos='prep');r.word('P6-S2','that','关系代词，指环境条件',pos='pron')
r.word('P7-S1','while','虽然；尽管',pos='conj');r.word('P7-S1','at','与the expense of组成以……为代价',pos='prep');r.word('P7-S1','rest','其余部分（指其他因素）',pos='n')
r.word('P8-S1','on','生活在（某环境）上',pos='prep');r.word('P8-S1','are','与linked构成被动形式',lemma='be',pos='aux');r.word('P8-S1','both','两个方向都（both ways）',pos='det')
r.word('P8-S2','that','人类系统与环境双向关联这件事',pos='pron');r.word('P8-S2','to','导致（lead to）',pos='prep',occ=2)
r.word('P9-S1','that','关系代词，指event即火这种现象',pos='pron');r.word('P9-S1','be','与controlled/unleashed构成被动语态',pos='aux')
r.word('P9-S2','to','对制定法规等至关重要（crucial to）',pos='prep');r.word('P9-S2','developing','制定；形成（法规政策）',lemma='develop',pos='v');r.word('P9-S2','that','关系代词，指法规政策与做法',pos='pron');r.word('P9-S2','as','尽可能……（as safe as possible）',pos='adv',occ=1);r.word('P9-S2','as','与前一个as组成尽可能安全',pos='conj',occ=2)
r.word('P10-S2','and','接在try后相当于to，表示设法做',pos='conj',occ=2)
checks(r,'''野火频发因联邦税收支出成为全国议题，fire为火非解雇。
55亿美元预算中超过一半用于灭火，近两倍指预算占比而非预算总额。
其他工作资金减少，that指森林流域文化资源及设施维护工作。
询问公共资金是否投向火灾高风险地区建设，whether为是否。
put it为表达，homes likely lost to wildfire为可能毁于野火。
public expenditure perspective为公共财政支出角度，for全国而言。
放大镜为仔细审视财政使用的比喻，that为指示代词。
引号内Wait是等等，OK问合不合适，不是确认正确答案。
redirect重新调配资金，lower-hazard为较低火灾风险地区。
views是动词看待，US为美国，shift为观念转变。
for one thing是首先，inclusive要求讨论更多因素。
climate change是气候变化，leading to导致，conditions环境条件非疾病。
while让步，equation指整体问题因素，不能只关注气候而忽视其他因素。
人类系统与自然环境相互关联，go both ways双向作用。
that指双向关联事实，fail to recognize为未认识到，lead to介词。
对问题与办法的认识都会受限，limited为局限的状态。
火被看成需控制且只在必要时释放的现象，be双重被动。
crucial to后接动名词，develop为制定法规，as safe as possible尽可能安全。
we've为we have完成时，disconnected表示与火共处的联系被疏离。
try and tease out为设法梳理，第二个and相当于不定式连接。''')
r.notes=['逐词复核财政、火生态和环境系统语境；明确US/it、fire、conditions、equation、dollars及比较数量，所有词位覆盖。']
save(r)
