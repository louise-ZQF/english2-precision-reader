/* One offline lexical pipeline shared by reading, collections and review.
 * Context meanings are keyed to a written occurrence; dictionary definitions
 * remain dictionary definitions. No Chinese-substring word-sense guessing.
 */
(function () {
    'use strict';
    const data = window.EnglishLexicalData || { words: {}, index: {}, phrases: {} };
    const review = window.EnglishMeaningReviews || { sentences: [], articles: [] };
    const normalize = value => String(value || '').replace(/[‘’]/g, "'").replace(/[‐‑–—]/g, '-').replace(/\s+/g, ' ').trim();
    const key = value => normalize(value).toLowerCase();
    const pos = value => ({ vt: 'v', vi: 'v', adj: 'a', ad: 'adv' }[value] || value || '');
    const sentenceKey = (exam, en) => exam + '|' + normalize(en);
    const sentences = new Map(), guides = new Map();
    for (const item of review.sentences) {
        const id = sentenceKey(item.exam, item.en), existing = sentences.get(id);
        if (existing) { existing.words.push(...item.words || []); existing.phrases.push(...item.phrases || []); }
        else sentences.set(id, { ...item, words: [...item.words || []], phrases: [...item.phrases || []] });
    }
    for (const item of review.articles) guides.set(item.id.includes('|') ? item.id : item.exam + '|' + item.id, item);
    const contractions = {
        "i'm": ['I am', '我是；我正处于……状态（I am 的缩写）'],
        "you're": ['you are', '你／你们是；你／你们正在……（you are 的缩写）'],
        "we're": ['we are', '我们是；我们正在……（we are 的缩写）'],
        "they're": ['they are', '他们是；他们正在……（they are 的缩写）'],
        "i've": ['I have', '我已经……（I have 的缩写，用于完成时）'],
        "you've": ['you have', '你／你们已经……（you have 的缩写，用于完成时）'],
        "we've": ['we have', '我们已经……（we have 的缩写，用于完成时）'],
        "they've": ['they have', '他们已经……（they have 的缩写，用于完成时）'],
        "he's": ["he's", 'he is 或 he has 的缩写：他是／他正在……；或他已经……，具体取决于后面的结构'],
        "she's": ["she's", 'she is 或 she has 的缩写：她是／她正在……；或她已经……，具体取决于后面的结构'],
        "it's": ["it's", 'it is 或 it has 的缩写：它是／这是；或它已经……，具体取决于后面的结构'],
        "that's": ["that's", 'that is 或 that has 的缩写：那是；或那已经……，具体取决于后面的结构'],
        "there's": ["there's", 'there is 或 there has 的缩写：有／存在；或已经有……'],
        "can't": ['can', '不能；无法（can not 的缩写）'], "cannot": ['can', '不能；无法'],
        "won't": ['will', '不会；不愿意（will not 的缩写）'], "wouldn't": ['would', '不会；不愿意'],
        "don't": ['do', '不（do not 的缩写）'], "doesn't": ['do', '不（does not 的缩写）'], "didn't": ['do', '没有；不（did not 的缩写）'],
        "isn't": ['be', '不是；没有（is not 的缩写）'], "aren't": ['be', '不是；没有（are not 的缩写）'],
        "wasn't": ['be', '不是；没有（was not 的缩写）'], "weren't": ['be', '不是；没有（were not 的缩写）'],
        "haven't": ['have', '还没有（have not 的缩写）'], "hasn't": ['have', '还没有（has not 的缩写）'], "hadn't": ['have', '此前没有（had not 的缩写）'],
        "shouldn't": ['should', '不应该'], "couldn't": ['could', '不能；无法'], "mustn't": ['must', '不许；禁止']
    };
    const acronyms = { US: '美国', USA: '美国', UK: '英国', EU: '欧盟', AI: '人工智能', CEO: '首席执行官', CEOs: '首席执行官（复数）', GDP: '国内生产总值', NHS: '英国国民医疗服务体系', IT: '信息技术', DNA: '脱氧核糖核酸；遗传物质', FTC: '美国联邦贸易委员会', EPA: '美国环境保护署', RSPB: '英国皇家鸟类保护协会', RHS: '英国皇家园艺学会', MBA: '工商管理硕士', PhD: '博士学位', PDF: '便携式文档格式' };
    function reviewedSentence(record) {
        return record && record.source && sentences.get(sentenceKey(record.source.exam, record.en));
    }
    function locate(word, record, token, start, end) {
        if (Number.isFinite(start) && Number.isFinite(end)) return { ...token, a: start, b: end };
        if (token && Number.isFinite(token.a) && Number.isFinite(token.b)) return token;
        const matches = writtenWords(record && record.en).filter(match => key(match.key) === key(word));
        return matches.length === 1 ? { ...token, a: matches[0].a, b: matches[0].b } : { ...token };
    }
    function correction(word, record, token, kind) {
        const sentence = reviewedSentence(record);
        if (!sentence || !Number.isFinite(token.a) || !Number.isFinite(token.b)) return null;
        const all = kind === 'phrase' ? [...sentence.phrases, ...sentence.words] : [...sentence.words, ...sentence.phrases];
        return all.find(item => item.a === token.a && item.b === token.b && normalize(sentence.en.slice(item.a, item.b)) === normalize(record.en.slice(token.a, token.b))) || null;
    }
    function compatible(p, wanted) { return !wanted || !p || pos(p) === pos(wanted) || wanted === 'v' && p === 'aux' || wanted === 'art' && p === 'pron'; }
    function lemmaFor(word, token, corrected) {
        if (corrected && corrected.lemma) return key(corrected.lemma);
        if (contractions[key(word)]) return contractions[key(word)][0];
        const written = key(word).replace(/'s$|s'$/g, match => match === "s'" ? 's' : '');
        const original = key(token && token.l);
        const allCandidates = (data.index[written] || []).filter(item => item.lemma !== written || item.label === '原形');
        const candidates = allCandidates.filter(item => compatible(item.p, token && token.p));
        const explicit = candidates.find(item => item.source === 'reviewed');
        if (explicit) return explicit.lemma;
        const dictionaryCandidates = candidates.filter(item => item.source === 'ECDICT');
        const dictionaryLemmas = [...new Set(dictionaryCandidates.map(item => item.lemma))];
        const trusted = dictionaryCandidates.find(item => item.lemma === original);
        if (trusted) return trusted.lemma;
        if (dictionaryLemmas.length === 1) return dictionaryLemmas[0];
        if (data.words[written] && data.words[written].common.some(item => compatible(item.p, token && token.p))) return written;
        // A participle may be tagged as an adjective, and a short option may
        // receive the wrong POS. Attested forms still outrank an empty lemma.
        if (!data.words[written] || !data.words[written].common.length) {
            const known = [...new Set(allCandidates.filter(item => ['ECDICT', 'reviewed'].includes(item.source) && data.words[item.lemma] && data.words[item.lemma].common.length).map(item => item.lemma))];
            if (known.length === 1) return known[0];
        }
        if (/[-‐‑]/.test(word)) return written;
        if (original && original !== written && data.words[original] && (!token || !token.w || key(token.w) === key(word))) return original;
        const unique = [...new Set(candidates.map(item => item.lemma))];
        return unique.length === 1 ? unique[0] : original && data.words[original] ? original : written;
    }
    function grammar(word, record, token, lemma) {
        const written = key(word), dep = token.d || '';
        if (contractions[written]) return { meaning: contractions[written][1], quality: 'grammar', lemma: contractions[written][0] };
        if (/^(the|a|an)$/.test(written)) return { meaning: written === 'the' ? '定冠词，表示特指；通常不单独译出' : '不定冠词，表示一个或一类；通常不单独译出', quality: 'grammar' };
        if (dep === 'neg') return { meaning: '不；没有（否定词）', quality: 'grammar' };
        if (dep === 'aux' || dep === 'auxpass') {
            if (lemma === 'to') return { meaning: '不定式标记；在此不单独译为“到／向”', quality: 'grammar' };
            if (dep === 'auxpass') return { meaning: '助动词，构成被动语态；不单独译出', quality: 'grammar' };
            if (lemma === 'have') return { meaning: '助动词，构成完成时；不单独译为“有”', quality: 'grammar' };
            if (lemma === 'be') return { meaning: '助动词，构成进行时；不单独译出', quality: 'grammar' };
            if (lemma === 'do') return { meaning: '助动词，用于疑问、否定或强调；不单独译为“做”', quality: 'grammar' };
            const modal = (data.words[lemma] && data.words[lemma].common || []).find(item => item.p === 'aux');
            if (modal) return { meaning: modal.m + '（情态助动词）', quality: 'grammar' };
        }
        const head = record.tokens && record.tokens[token.h];
        if (written === 'that' && dep === 'mark') return { meaning: '从句引导词，连接后面的内容；通常不单独译出', quality: 'grammar' };
        if (['which', 'who', 'whom', 'that', 'whose'].includes(written) && head && head.d === 'relcl') return { meaning: written === 'whose' ? '关系词，表示与先行词的所属关系；相当于“……的”' : '关系词，指代前面的人或事物，并引导定语从句；不是疑问词', quality: 'grammar' };
        if (lemma === 'be' && token.p === 'v') return { meaning: record.tokens && record.tokens.some(t => t.d === 'expl' && t.h === token.h) ? '有；存在（there be 结构）' : '是；处于；联系主语与后面的身份或状态', quality: 'grammar' };
        return null;
    }
    function entry(lemma) { return data.words[key(lemma)] || null; }
    function phraseLemma(value) {
        const written = key(value);
        if (data.phrases[written]) return written;
        const parts = written.split(' ');
        if (parts.length < 2) return written;
        const candidate = [lemmaFor(parts[0], { p: 'v' }), ...parts.slice(1)].join(' ');
        return data.phrases[candidate] ? candidate : written;
    }
    function lookup(input) {
        const word = input.word || '', record = input.record || { en: '', tokens: [] }, kind = input.kind || 'word';
        const token = locate(word, record, input.token, input.start, input.end);
        const fixed = correction(word, record, token, kind);
        let lemma = kind === 'phrase' ? phraseLemma(fixed && fixed.lemma || word) : lemmaFor(word, token, fixed);
        const correctedToken = { ...token, l: lemma, p: fixed && fixed.pos || token.p };
        const base = entry(lemma);
        const phraseDefinition = data.phrases[lemma] || '';
        const common = base && base.common.length ? base.common : kind === 'phrase' ? phraseDefinition.split('；').filter(Boolean).map(m => ({ p: 'phrase', m })) : [];
        const result = { word, lemma, kind, token: correctedToken, common, ph: base && base.ph || '', meaning: '', quality: 'missing', explanation: '' };
        if (fixed) return { ...result, meaning: fixed.meaning, quality: 'reviewed', explanation: fixed.explanation || '' };
        const abbreviation = word.replace(/\./g, '').replace(/['’]s$/, '');
        if (acronyms[abbreviation]) return { ...result, lemma: abbreviation, common: [], ph: '', meaning: acronyms[abbreviation], quality: 'name' };
        const shortForms = { 'e.g.': '例如（for example）', 'i.e.': '也就是；换句话说（that is）', 'etc.': '等等（and so on）', 'vs.': '与……相对；对比' };
        if (shortForms[key(word)]) return { ...result, lemma: word, meaning: shortForms[key(word)], quality: 'grammar' };
        if (kind === 'phrase') {
            const meaning = data.phrases[lemma] || '';
            return { ...result, meaning, quality: meaning ? 'phrase' : 'missing' };
        }
        const grammatical = grammar(word, record, correctedToken, lemma);
        if (grammatical) return { ...result, ...grammatical };
        if (/^[A-Z]$/.test(word)) return { ...result, lemma: word, meaning: word === 'I' ? '我（第一人称单数）' : '字母 ' + word + '；可用作选项编号或姓名首字母，结合原文理解', quality: 'name' };
        if (/^[A-H]-[A-H]$/.test(word)) return { ...result, meaning: '从 ' + word[0] + ' 到 ' + word[2] + ' 的选项', quality: 'grammar' };
        let choices = common.filter(item => compatible(item.p, correctedToken.p));
        if (!choices.length) choices = common;
        // Keep genuine alternatives visible; do not pick a Chinese substring
        // from an unrelated part of the sentence and label it a context sense.
        if (choices.length) return { ...result, meaning: [...new Set(choices.slice(0, 2).map(item => item.m))].join('；'), quality: 'dictionary' };
        if (/^[A-Z][A-Za-z]+$/.test(word) && token.p === 'n') return { ...result, lemma: word, meaning: '专名；人名、地名或机构名称的一部分', quality: 'name' };
        return result;
    }
    function phrases(record) {
        const sentence = reviewedSentence(record);
        return sentence ? sentence.phrases.map(item => ({ a: item.a, b: item.b, key: phraseLemma(item.lemma || sentence.en.slice(item.a, item.b)), meaning: item.meaning, reviewed: true })) : [];
    }
    function dictionaryLookup(word) {
        const found = lookup({ word });
        const base = entry(found.lemma);
        if (!base || !base.common.length) return null;
        return { ph: base.ph, s: base.common.map(item => ({ p: item.p, t: item.m })) };
    }
    function writtenWords(en) {
        const matches = Array.from(String(en || '').matchAll(/(?<![A-Za-z0-9'’])(?:\d+(?:st|nd|rd|th)(?:[-‐‑][A-Za-z]+)+|(?:[A-Za-z]\.){2,}|[A-Za-z][A-Za-z0-9]*(?:['’][A-Za-z]+)*(?:["”]?[-‐‑][A-Za-z0-9]+(?:['’][A-Za-z]+)*)*)/g));
        const runOns = new Set(["part-there's", 'script-literally', 'figuratively-means', "anyway-aren't", 'catch-up-with-household']);
        return matches.flatMap(match => {
            if (!runOns.has(key(match[0]))) return [{ a: match.index, b: match.index + match[0].length, key: match[0], kind: 'word' }];
            let offset = match.index;
            return match[0].split('-').map(value => { const item = { a: offset, b: offset + value.length, key: value, kind: 'word' }; offset += value.length + 1; return item; });
        });
    }
    window.EnglishMeanings = { lookup, entry, lemmaFor, phrases, writtenWords, dictionaryLookup, guide: id => guides.get(id) || null,
        revision: review.revision || data.revision, stats: { dictionary: Object.keys(data.words).length, articles: guides.size, contextSentences: sentences.size } };
})();
