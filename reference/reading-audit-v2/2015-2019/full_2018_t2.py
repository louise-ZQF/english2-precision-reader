# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2018-T2'),[f'{y}-T{n}' for y in [2015,2016,2017] for n in range(1,5)]+['2018-T1'])

lex(r,'''fossil/a=化石的（fossil fuels为化石燃料）;fuels@fuel/n=燃料;coal/n=煤炭;oil/n=石油;gas/n=天然气;generate/v=产生；供应（能源）；发电;roughly/adv=大约;percent/n=百分之;world's@world/n=世界的（所有格）;energy/n=能源；能量;supply/n=供应;it's@it be/pron=这是（it is缩写）;clearer@clear/a=更清楚的;ever/adv=以往任何时候;future/n=未来;belongs@belong/v=属于;renewable/a=可再生的;sources@source/n=能源来源；电源;wind/n=风能；风;solar/a=太阳能的;move/n=转型；转变;renewables@renewable/n=可再生能源;picking@pick/v=增强（pick up momentum）；获得;up/adv=增强（pick up）；加快（speed up）;momentum/n=势头；动力;account/v=占（比例，account for）;new/a=新增的；新的;power/n=电力；发电量;going@go/v=投入（go on line整体为投入运行）;line/n=运行状态（on line整体）；线路;growth/n=增长;stems@stem/v=源于（stem from）;commitment/n=承诺;by/prep=由；以……幅度;farsighted/a=有远见的;fund/v=资助；提供资金;cleaner@clean/a=更清洁的;story/n=主要原因；关键情况;plummeting@plummet/a=急剧下降的;prices@price/n=价格;cost/n=成本;panels@panel/n=太阳能板;dropped@drop/v=下降;turbines@turbine/n=涡轮机；风力发电机;one-third/num=三分之一;eight/num=八;principal/a=主要的;scotland@Scotland/name=苏格兰;electricity/n=电力;rest/n=其余部分;takes@take/v=取得（take the lead为领先）；做;lead/n=领先地位;notably/adv=特别是；尤其;china@China/name=中国;europe@Europe/name=欧洲;states@State/name=United States国名一部分；美国;seeing@see/v=经历；出现;remarkable/a=显著的;march@March/name=三月;time/n=次；时间;accounted@account/v=占（比例，account for）；generated@generate/v=产生（电力）；发电;information/n=信息（机构名一部分）;administration/n=管理署（机构名一部分）;trump@Trump/name=特朗普（人名）;underlined@underline/v=着重强调;path/n=途径；路径;recent/a=最近的;speech/n=演讲;iowa@Iowa/name=爱荷华州;dismissed@dismiss/v=不屑地否定；不予看好;unreliable/a=不可靠的;message/n=说法；观点;did@do/aux=助动词，与not形成过去时否定；play/v=被接受；产生反响（play well with）;well/adv=好地（play well with为受到欢迎）；dot/v=遍布；点缀;state's@state/n=该州的（所有格）;giants@giant/n=巨头（大公司）;like/prep=例如；像……这样的;microsoft@Microsoft/name=微软（公司名）;attracted@attract/v=吸引;availability/n=可获取性；供应条件;clean/a=清洁的;data/n=数据;centers@center/n=中心;question/n=问题;happens@happen/v=发生；出现;sun/n=太阳;shine/v=照耀；发光;put-down/n=反驳或贬低的话;skeptics@skeptic/n=怀疑者;boost/n=提升；增长;storage/n=储存（电能）;batteries@battery/n=电池;ability/n=能力;flowing@flow/v=持续供应；流动;making@make/v=使；让;driven@drive/v=推动;vehicle/n=车辆;manufacturers@manufacturer/n=制造商;placing@place/v=进行（押注）；投入;big/a=巨大的;bets@bet/n=押注；寄予厚望的投资;battery-powered/a=电池驱动的;electric/a=电动的;vehicles@vehicle/n=车辆;although/conj=虽然;cars@car/n=汽车;rarity/n=少见的事物;roads@road/n=道路;massive/a=巨额的；大规模的;investment/n=投资;change/v=改变;rapidly/adv=迅速地;coming@coming/a=未来的；即将到来的;long/a=漫长的;way/n=路程；进程;go/v=走；前进;trend/n=趋势;spiking@spike/v=急剧上升;speeding@speed/v=加快;meaningful/a=实质性的；有意义的;slowing@slow/v=减缓;washington@Washington/name=美国联邦政府（以首都代称）;alternative/a=替代的；非传统的;global/a=全球的'''.replace('；generated@generate',';generated@generate').replace('；play/v',';play/v').replace('；dot/v',';dot/v'))
r.word('P1-S1','while','虽然；尽管',pos='conj');r.word('P1-S1','to','属于（belong to）',pos='prep');r.word('P1-S1','as','例如（such as）',pos='prep')
r.word('P1-S2','to','转向（可再生能源）',pos='prep');r.word('P1-S2','is','与picking构成进行时',lemma='be',pos='aux');r.word('P1-S2','around','遍及；在全世界各地',pos='prep');r.word('P1-S2','for','占（account for）中的搭配介词',pos='prep');r.word('P1-S2','on','与line组成投入运行',pos='prep')
r.word('P2-S1','from','源自（stem from）',pos='prep')
r.word('P2-S3','close','接近的（close to）',pos='a');r.word('P2-S3','to','接近（close to）',pos='prep');r.word('P2-S3','by','下降了……（降幅）',pos='prep')
r.word('P3-S2','for','与example组成例如',pos='prep');r.word('P3-S2','power','为……供电',pos='v');r.word('P3-S2','enough','足够的（电力）',pos='det')
r.word('P3-S3','while','虽然；尽管',pos='conj');r.word('P3-S3','is','与seeing构成进行时',lemma='be',pos='aux')
r.word('P3-S4','US','美国（United States缩写）',lemma='US',pos='name');r.word('P3-S4','for','与the first time组成首次',pos='prep',occ=1);r.word('P3-S4','for','占（account for）',pos='prep',occ=2)
r.word('P4-S1','to','通向（经济增长）的途径',pos='prep')
r.word('P4-S3','that','那种（前文对风能的说法）',pos='det');r.word('P4-S3','with','受到谁的欢迎（play well with）',pos='prep');r.word('P4-S3','fields','田野',pos='n');r.word('P4-S3','generation','发电；发电量',pos='n');r.word('P4-S3','are','助动词，与being attracted构成进行时',lemma='be',pos='aux');r.word('P4-S3','being','与attracted构成被动语态',lemma='be',pos='aux');r.word('P4-S3','by','被清洁能源供应所吸引',pos='prep');r.word('P4-S3','power','为数据中心供电',pos='v')
r.word('P5-S1','blow','吹；刮（风）',pos='v');r.word('P5-S1','what','会怎样（疑问）',pos='pron');r.word('P5-S1','for','供怀疑者使用（反驳的话）',pos='prep')
r.word('P5-S2','capacity','容量（储电容量）',pos='n');r.word('P5-S2','is','与making构成进行时',lemma='be',pos='aux');r.word('P5-S2','around','与the clock组成昼夜不停',pos='prep')
r.word('P6-S1','advance','进步；进展',pos='n');r.word('P6-S1','is','与driven构成被动语态',lemma='be',pos='aux');r.word('P6-S1','are','与placing构成进行时',lemma='be',pos='aux');r.word('P6-S1','on','押注于（place bets on）',pos='prep')
r.word('P6-S2','on','在道路上',pos='prep')
r.word('P7-S1','while','虽然；尽管',pos='conj');r.word('P7-S1','lines','趋势线',lemma='line',pos='n');r.word('P7-S1','are','与spiking构成进行时',lemma='be',pos='aux')
r.word('P7-S2','change','转变；变化',pos='n');r.word('P7-S2','be','与speeding构成进行时',pos='aux');r.word('P7-S2','have','产生（影响）',pos='v');r.word('P7-S2','just','恰好；正好',pos='adv');r.word('P7-S2','effect','影响；效果',pos='n')
r.word('P7-S3','does','做；采取行动',lemma='do',pos='v');r.word('P7-S3','do','做；采取行动',pos='v');r.word('P7-S3','mean','具有意义；产生影响',pos='v');r.word('P7-S3','thought','观念；思想',pos='n')
checks(r,'''while让步，energy为能源，as举例，未来属于可再生能源的to为介词。
account for占比，on line投入运行，新增电源份额非总供电量份额。
fund为动词资助而非基金，增长由政府与企业承诺支持。
story指增长原因，plummeting价格暴跌，而非虚构故事。
八年内成本分别下降80%和近三分之一，by为降幅，close to为接近。
principal是主要的，不是校长或本金。
power动词供电，95%对应家庭，足够电量并非已连接家庭数调查。
while对照先行地区与美国转变，seeing为经历而非视觉。
首次超过10%为三月发电占比，US缩写非代词，for两处功能不同。
underlined为强调，as把化石燃料看作增长途径，非下划线动作。
dismissed为否定看法，unreliable为不可靠，保留是演讲者观点。
play well with为被接受，fields田野，generation发电，are being attracted进行被动。
blow是刮风，put-down反驳之辞，what happens疑问并非冲击名词。
capacity为储电容量非精力，around the clock昼夜供电，is making进行时。
advance名词进步，is driven被动，汽车商大举押注电动车。
rarity为少见，巨额投资可能改变而非确定改变，coming未来几年。
虽然前路漫长但趋势急升，line为趋势线而非终点线。
have effect为产生影响，能源转变加快或能及时减缓气候变化。
does/do均实义采取行动，Washington借指联邦政府，less and less为影响渐小。''')
lex(r,'part/n=部分（in part为部分地）')
r.notes=['逐词核定能源语境，纠正energy/field/generation/power/advance/fund/blow和account for等定位义与词性；保留历史数据时点。']
save(r)
