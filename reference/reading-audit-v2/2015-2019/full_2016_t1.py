# -*- coding: utf-8 -*-
from middle_full_review import *
r=reuse(make('2016-T1'),['2015-T1','2015-T2','2015-T3','2015-T4'])

lex(r,'''it's@it be/pron=这是（it is缩写）;true/a=确实的；属实的;high-school/a=高中的;coding@coding/n=编程;classes@class/n=课程;aren't@be/v=不是；并非（are not缩写）;essential/a=必不可少的;learning@learn/v=学习;computer/n=计算机;science/n=科学（computer science为计算机科学）;experience/n=经验;few/det=少数几个（a few）;introductory/a=入门的;courses@course/n=课程;tom@Tom/name=汤姆（人名）;cortina@Cortina/name=科蒂纳（姓氏）;assistant/a=副的；助理的;dean/n=学院院长;carnegie@Carnegie/name=卡内基（大学名称一部分）;mellon's@Mellon/name=梅隆的（大学名所有格）;school/n=学院；学校;early/a=早期的；及早的;exposure/n=接触；初步体验;beneficial/a=有益的;younger@young/a=年龄较小的;kids@kid/n=孩子;confusing/a=令人困惑的;endless/a=无穷无尽的;string/n=一串；一系列;letters@letter/n=字母;numbers@number/n=数字;tool/n=工具;build/v=开发；创建;apps@app/n=应用程序;create/v=创作；创建;artwork/n=艺术作品;test/v=检验；测试;hypotheses@hypothesis/n=假设;transform/v=改变；转变;thought/n=思维；思考;processes@process/n=过程;older@old/a=年龄较大的;breaking@break/v=拆分；分解;problems@problem/n=问题;bite-sized/a=小而易处理的;chunks@chunk/n=小块；部分;using@use/v=使用;code/n=代码;solve/v=解决;normal/a=正常的；习惯性的;giving@give/v=给予；让……接受;training/n=训练;increase/v=增加;interested/a=感兴趣的;field/n=领域;fill/v=填补;benefit/v=受益;something/pron=某些知识；某种东西;get/v=到达；获得;computer-science/a=计算机科学的;packed@pack/v=挤满；塞满;brim/n=边缘（packed to the brim形容人满为患）;drive/v=使离开；使退缩（drive away）;less-experienced/a=经验较少的;determined/a=坚定的；有决心的;away/adv=离开（drive away）；退缩;flatiron@Flatiron/name=弗拉特艾恩（学校名）;pay/v=付费;programming/n=编程;bootcamps@bootcamp/n=集中训练营;popular/a=受欢迎的；流行的;adults@adult/n=成年人;looking@look/v=寻找；寻求;career/n=职业;change/n=转变；转行;high-schoolers@high-schooler/n=高中生;same/a=相同的;curriculum/n=课程体系;try/v=尽力；尝试;gear/v=使适合；围绕……调整;lessons@lesson/n=课程;toward/prep=面向；针对;things@thing/n=事物;they're@they be/v=他们是；他们处于（they are缩写）;victoria@Victoria/name=维多利亚（人名）;friedman@Friedman/name=弗里德曼（姓氏）;instructor/n=讲师;instance/n=例子（for instance整体为例如）;one/num=一个；一款;developing@develop/v=开发;movies@movie/n=电影;mood/n=心情;probably/adv=大概；可能;won't@will/aux=不会（will not缩写）;high/a=高中的（high school）;next/a=下一个;facebook@Facebook/name=脸书（公司名）;languages@language/n=语言;quick/a=快速的;turnover/n=更新换代;ruby@Ruby/name=Ruby（编程技术名一部分）;rails@Rails/name=Rails（技术框架名）;language/n=语言;learned@learn/v=学过；学习;relevant/a=适用的；相关的;by/prep=到……时；由;time/n=时刻;enter/v=进入;skills@skill/n=技能;logically/adv=有条理地；合乎逻辑地;organize/v=组织；整理;results@result/n=结果;apply/v=适用;deborah@Deborah/name=黛博拉（人名）;seehorn@Seehorn/name=西霍恩（姓氏）;consultant/n=顾问;state/n=州;north@North/name=北（州名一部分）;carolina@Carolina/name=卡罗来纳（州名一部分）;indeed/adv=事实上;go/v=进入；从事;future/a=未来的;army/n=大批；队伍（比喻）;coders@coder/n=程序员;sole/a=唯一的;surrounded@surround/v=包围；环绕;computers@computer/n=计算机;pockets@pocket/n=口袋;homes@home/n=家;rest/n=剩余部分；余下的时间;lives@life/n=一生；生活;coax/v=引导；设法使……按要求运作;machine/n=机器;producing@produce/v=产生；生成;earlier@early/adv=更早地;power/n=能力;out/adv=退出（drop out）''')
r.word('P1-S1','for','对于学习计算机科学来说',pos='prep')
r.word('P1-S2','catch','赶上（catch up）',lemma='catch',pos='v');r.word('P1-S2','up','赶上（catch up）',pos='adv')
r.word('P2-S2','learn','认识到；了解到',pos='v',occ=2);r.word('P2-S2','but','而是（not just...but）',pos='conj')
r.word('P2-S3','as','像……一样（not as...as比较）',pos='adv',occ=1);r.word('P2-S3','as','与……一样（比较对象连接词）',pos='conj',occ=2);r.word('P2-S3','for','对……而言',pos='prep')
r.word('P2-S4','down','分解开（break down）',pos='adv');r.word('P2-S4','into','分解成（若干小块）',pos='prep')
r.word('P2-S5','in','对……感兴趣（interested in）',pos='prep');r.word('P2-S5','gap','人才供需缺口',pos='n')
r.word('P3-S1','to','到达大学（get to）',pos='prep',occ=1);r.word('P3-S1','to','直到……边缘；达到满员（to the brim）',pos='prep',occ=2);r.word('P3-S1','are','助动词，与packed构成被动形式',lemma='be',pos='aux');r.word('P3-S1','where','关系副词，指大学这个场所',pos='adv');r.word('P3-S1','which','关系代词，指入门课人满为患这一情况',pos='pron')
r.word('P4-S1',"that's",'that has的缩写；关系词that指训练营，has构成完成时',lemma='that have',pos='pron');r.word('P4-S1','for','对成年人而言',pos='prep',occ=1);r.word('P4-S1','for','寻找（look for）中的搭配介词',pos='prep',occ=2)
r.word('P4-S2','in','对……感兴趣（interested in）',pos='prep')
r.word('P4-S3','for','与instance组成例如',pos='prep');r.word('P4-S3','are','助动词，与developing构成进行时',lemma='be',pos='aux');r.word('P4-S3','suggests','推荐（电影）',lemma='suggest',pos='v');r.word('P4-S3','on','依据（based on）',pos='prep')
r.word('P5-S1','class','课程；教学班',pos='n');r.word('P5-S1','drop','退出学业；辍学（drop out of）',pos='v');r.word('P5-S1','school','学校（high school为高中）',pos='n')
r.word('P5-S2','have','具有；发生',pos='v');r.word('P5-S2','so','所以',pos='conj');r.word('P5-S2','on','Ruby on Rails技术名称的组成部分',pos='prep')
r.word('P5-S3','think','思考',pos='v');r.word('P5-S3','to','适用于（apply to）',pos='prep',occ=2);r.word('P5-S3','for','为（州）提供顾问服务',pos='prep')
r.word('P6-S1','IT','信息技术（Information Technology缩写）',lemma='IT',pos='name');r.word('P6-S1','at','与all组成not at all“根本不”',pos='prep');r.word('P6-S1','all','与not at组成根本不',pos='adv')
r.word('P6-S2','creating','培养；造就（程序员队伍）',lemma='create',pos='v');r.word('P6-S2','purpose','目的',pos='n')
r.word('P6-S3','are','与going to组成将来表达',lemma='be',pos='aux');r.word('P6-S3','going','与are/to组成“将会”，不是前往',lemma='go',pos='aux');r.word('P6-S3','be','助动词，与surrounded构成被动语态',pos='aux');r.word('P6-S3','by','被……包围的施事',pos='prep');r.word('P6-S3','for','持续（此后一生）',pos='prep')
r.word('P6-S4','the','与比较级组成越……越……结构，不是定冠词特指',pos='adv');r.word('P6-S4','think','思考；运作（拟人化计算机）',pos='v');r.word('P6-S4','have','具有；拥有（能力）',pos='v');r.word('P6-S4','do','做；实现',pos='v');r.word('P6-S4','that','做到前述让机器生成结果的事',pos='pron',occ=2);r.word('P6-S4','into','引导……做（coax...into）',pos='prep')
checks(r,'''高中编程并非大学学习计算机科学的必要条件，aren't的否定保留。
catch up为赶上，副院长所属卡内基梅隆计算机学院，不套商学院释义。
exposure为及早接触，不是暴露风险。
第二个learn为认识到，not just...but为不只是而且是，三项工具用途并列。
not as hard as表示较小孩子转变思维更容易，比较方向核清。
break down/into组成分解成小块，down不是下降，code为代码。
interested in限定人群，jobs gap为人才缺口而非学业差距。
packed to the brim指课堂人满为患；which指这一情况，-determined承接less。
that's此处为that has而非that is，训练营流行于希望转行的成年人。
gear...toward按兴趣调整课程，get是获得课程而非达到地点。
suggests在此为推荐电影而非表明，based on说明推荐依据。
class是教学班，drop out of为辍学，build Facebook比喻创办公司。
turnover为更新换代，on属于技术名称，by the time为到……时。
思维组织技能适用于任何语言，to接apply时为介词。
IT为信息技术缩写而非代词it，not at all为根本不。
培养程序员并非唯一目的，sole与not的限定保留。
are going to be surrounded为将来被动，for the rest持续此后一生。
the比较级结构为越早越好，do为实义动词，最后that回指让机器产出。''')
r.notes=['逐词复核并纠正首次复用候选中science期刊义、school商学院义、class阶层义、IT代词误义，所有功能词按位置判定。']
save(r)
