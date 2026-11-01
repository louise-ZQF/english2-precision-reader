# -*- coding: utf-8 -*-
from middle_full_review import *
r=make('2015-T2')
lex(r,'''years@year/n=年;studies@study/n=研究;found@find/v=发现;first-generation/a=家中第一代上大学的;college/n=大学;students@student/n=学生;parent/n=父亲或母亲中的一人;degree/n=学位;lag/v=落后于;range/n=一系列；范围;education/n=教育;achievement/n=学业成就;factors@factor/n=指标；因素;grades@grade/n=成绩;lower@low/a=更低的;dropout/n=辍学;rates@rate/n=比例；比率;higher@high/a=更高的;since/conj=因为;likely/a=有可能的;advance/v=改善境况；向上发展;economically/adv=在经济状况方面;succeed/v=取得成功;colleges@college/n=大学;universities@university/n=大学;pushed@push/v=积极推动；努力;decades@decade/n=十年;recruit/v=招收（学生）;created@create/v=造成；形成;paradox/n=悖论；看似矛盾的局面;recruiting@recruit/v=招收（学生）;watching@watch/v=眼看着；看着;fail/v=失败；未取得成功;means@mean/v=意味着;continued@continue/v=继续;reproduce/v=重复造成；再生产;widen/v=扩大（差距）;rather/adv=而是（rather than）;close/v=缩小；弥合（差距）;gap/n=差距;based@base/v=基于;social/a=社会的;class/n=阶层;according/adv=根据（according to）;depressing/a=令人沮丧的;beginning/n=开头;paper/n=论文;forthcoming/a=即将发表的;journal/n=学术期刊;psychological/a=心理学的（期刊名一部分）;science/n=科学（期刊名一部分）;article/n=文章；论文;actually/adv=实际上;quite/adv=相当;optimistic/a=乐观的;outlines@outline/v=概述；勾勒;potential/a=可能的；潜在的;solution/n=解决办法;problem/n=问题;suggesting@suggest/v=提出；表明;approach/n=方法；干预办法;involves@involve/v=包含；涉及;one-hour/a=一小时的;next-to-no-cost/a=几乎零成本的;program/n=项目；干预活动;percent/n=百分比（与数字连用）；百分之;measured@measure/v=衡量;authors@author/n=作者;different/a=不同的;findings@finding/n=研究结果;study/n=研究;involving@involve/v=涉及；包含;completed@complete/v=完成;project/n=研究项目;unnamed/a=未具名的;private/a=私立的;university/n=大学;first/num=第一;generation/n=一代人;defined@define/v=定义；界定;having@have/v=拥有;four-year/a=四年制的;recipients@recipient/n=获得者；受助者;pell@Pell/name=佩尔（助学金名称一部分）;grants@grant/n=助学金；补助金;federal/a=联邦政府的;grant/n=助学金；补助金;undergraduates@undergraduate/n=本科生;financial/a=经济方面的;need/n=困难；需要（此处指经济资助需求）;true/a=属实的；同样如此;least/adv=至少（at least）;one/num=一个；一位;thesis/n=论点；核心主张;relatively/adv=相对地;modest/a=不大的；适度的;intervention/n=干预措施;big/a=大的;impact/n=影响;view/n=看法;lacking@lack/v=缺乏;practical/a=实用的；实践层面的;knowledge/n=知识;deal/v=应对（deal with）;issues@issue/n=问题；实际困难;face/v=面临（问题作主语时表示摆在……面前）;cite/v=援引；引用;past/a=过去的;research/n=研究;several/det=几位；若干;show/v=说明；表明;narrowed@narrow/v=缩小;struggle/v=艰难地努力;navigate/v=摸索应对；适应（文化环境）;middle-class/a=中产阶级的;culture/n=文化;learn/v=学习;rules@rule/n=规则;game/n=游戏（rules of the game比喻隐性规则）;take/v=利用（take advantage of）;advantage/n=有利条件（take advantage of整体为利用）;resources@resource/n=可利用的资源;write/v=写道;becomes@become/v=变成；成为;don't@do/aux=不（do not缩写）;talk/v=谈论;advantages@advantage/n=优势;disadvantages@disadvantage/n=劣势;groups@group/n=群体;us@US/name=美国;seldom/adv=很少;acknowledge/v=承认；正视;affect/v=影响;educational/a=教育方面的;experiences@experience/n=经历;lack/v=缺乏;insight/n=深入认识；理解;struggling@struggle/v=处境艰难；努力应对;understand/v=理解;improve/v=改善；进步;by/prep=通过；依据''')
r.word('P1-S1','for','持续（多年）',pos='prep');r.word('P1-S1','do','助动词，构成do not have否定',pos='aux');r.word('P1-S1','have','拥有（学位）',pos='v',occ=2);r.word('P1-S1','with','拥有；具有（大学学位）',pos='prep');r.word('P1-S1','on','在……指标方面',pos='prep')
r.word('P1-S3','for','持续（几十年）',pos='prep');r.word('P1-S3','in','在高等教育领域',pos='prep');r.word('P1-S3','higher','高等的（higher education固定说法）',lemma='high',pos='a');r.word('P1-S3','most','最（限定经济上提升的可能性）',pos='adv')
r.word('P1-S4','in','在in that结构中，与that合起来表示“因为”',pos='prep');r.word('P1-S4','that','和in组成“原因在于”',pos='conj',occ=1);r.word('P1-S4','higher','高等的（higher education）',lemma='high',pos='a');r.word('P1-S4','on','依据；以社会阶层为基础',pos='prep');r.word('P1-S4','to','根据（according to）',pos='prep',occ=2)
r.word('P2-S1','as','因为',pos='conj',occ=1);r.word('P2-S1','as','例如（such...as）',pos='prep',occ=2);r.word('P2-S1','to','针对；关于（solution to this problem）',pos='prep');r.word('P2-S1','by','通过……指标衡量',pos='prep');r.word('P2-S1','can','能够（研究提出的潜在效果）',pos='aux')
r.word('P3-S1','are','系动词，说明来自不同大学',lemma='be',pos='v',occ=1);r.word('P3-S1','are','助动词，与based构成被动形式',lemma='be',pos='aux',occ=2);r.word('P3-S1','on','依据（based on）',pos='prep')
r.word('P3-S2','was','被动语态助动词，与defined连用',lemma='be',pos='aux');r.word('P3-S2','as','定义为',pos='prep');r.word('P3-S2','with','具有（四年制学位）',pos='prep')
r.word('P3-S3','most','大多数（指第一代学生）',pos='pron');r.word('P3-S3','were','系动词；是助学金获得者',lemma='be',pos='v');r.word('P3-S3','for','面向；提供给（本科生）',pos='prep',occ=1);r.word('P3-S3','for','对于另一组学生而言',pos='prep',occ=2);r.word('P3-S3','while','而；相比之下',pos='conj');r.word('P3-S3','with','有（经济需求或父母学位背景）',pos='prep');r.word('P3-S3','at','与least连用表示至少',pos='prep')
r.word('P4-S1','was','被动形式助动词，与based连用',lemma='be',pos='aux');r.word('P4-S1','on','以……为依据（based on）',pos='prep');r.word('P4-S1','that','解释thesis的同位语从句连接词',pos='conj',occ=1);r.word('P4-S1','that','解释view的同位语从句连接词',pos='conj',occ=2);r.word('P4-S1','that','关系代词，指前面的issues',pos='pron',occ=3);r.word('P4-S1','potential','潜力',pos='n');r.word('P4-S1','be','与lacking构成处于缺乏的状态',pos='v');r.word('P4-S1','with','对付；处理（deal with中的介词）',pos='prep');r.word('P4-S1','most','大多数（大学生）',pos='det')
r.word('P4-S2','that','引出说明的内容',pos='conj',occ=1);r.word('P4-S2','that','关系代词，指gap',pos='pron',occ=2);r.word('P4-S2','be','与narrowed构成被动语态',pos='aux');r.word('P4-S2','by','由（研究的作者）',pos='prep')
r.word('P5-S1','higher','高等的（higher education）',lemma='high',pos='a');r.word('P5-S1','of','……的（文化、游戏规则）；take advantage of中的搭配介词',pos='prep')
r.word('P5-S2','when','如果；在……情况下',pos='conj');r.word('P5-S2','more','更加严重（more of a problem）',pos='adv')
r.word('P5-S3','how','……如何影响／如何改善（引出理解的内容）',pos='adv');r.word('P5-S3','are','助动词，与struggling构成进行时',lemma='be',pos='aux');r.word('P5-S3','like','像……一样',pos='prep');r.word('P5-S3','why','……为什么（引出不理解的原因）',pos='adv')
# Add the one remaining comparison word explicitly.
lex(r,'like/prep=像……一样')
checks(r,'''第一代定义是父母均没有大学学历，lag为动词，of限定学业指标。
成绩较低和辍学率较高同时保留，两个比较方向不反转。
since为原因、if为条件，higher education是高等教育，for为持续时间。
悖论是招收后仍失败，rather than与close对照，according to指论文出处。
as为因为，63%是缩小的差距比例不是降到63%，括号修饰对象准确。
147指完成项目者，研究在未具名私立大学，不能扩大样本。
not having a parent表示父母无一人有学位，不是只有一位家长。
59.1%和8.6%分别对应两组获助学金比例，while为对比。
potential此处是名词潜力，不是前句形容词可能的；缺的是实用知识。
this gap指实用知识差距，与后面的学业差距并非同一个层次。
struggle统领三项任务，navigate是文化适应而非导航。
条件是高校避谈阶层优劣，这会加重问题，不是改变社会阶层。
how/why分别引出阶层影响、困难原因与改善办法，US为美国。''')
r.notes=['独立再审全部句块与学业研究结论；按每词位置保存词义、词性及原形，助动词与实义have另核定。']
save(r)
