/* English-II precision reading: desktop interactions, phrases, and sentence study. */
(function () {
    'use strict';
    const KEYS = { mode: 'english2_precision_mode_v1', sentences: 'english2_sentences_v1', overrides: 'english2_context_overrides_v1' };
    const $ = (s, root = document) => root.querySelector(s);
    const $$ = (s, root = document) => Array.from(root.querySelectorAll(s));
    const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    const norm = s => String(s || '').replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, ' ').trim();
    const wordKey = s => norm(s).toLowerCase().replace(/[\u2010\u2011]/g, '-').replace(/[^a-z'\s-]/g, '').trim();
    const wordData = window.EnglishWordForms || { words: {}, index: {} };
    const meanings = window.EnglishMeanings;
    const lexicalData = window.EnglishLexicalData || { words: {}, phrases: {} };
    const posName = pos => ({ n: '名词', v: '动词', vt: '动词', vi: '动词', a: '形容词', adj: '形容词', adv: '副词', ad: '副词', prep: '介词', conj: '连词', pron: '代词', aux: '助动词', art: '冠词', num: '数词', inf: '不定式标记', interj: '感叹词', phrase: '词组' }[pos] || pos || '');
    const reviewed = window.EnglishReviewedTranslations || { articles: [] };
    const reviewedIndex = new Map();
    const translationKey = value => norm(value).replace(/[\u201c\u201d]/g, '"').replace(/[\u2010\u2011\u2013\u2014]/g, '-').replace(/\s+([,.!?;:])/g, '$1').replace(/^[\s"']+|[\s"'.!?;:,]+$/g, '').toLowerCase();
    const articleKey = value => norm(value).split('/').pop().replace(/\s+/g, '').toLowerCase();
    for (const article of reviewed.articles || []) {
        const register = (item, fragment) => {
            const key = translationKey(item.en);
            if (!reviewedIndex.has(key)) reviewedIndex.set(key, []);
            reviewedIndex.get(key).push({ ...item, exam: article.exam, article: article.article, fragment });
        };
        for (const item of article.sentences || []) register(item, false);
        for (const item of article.fragments || []) register(item, true);
        const paragraphs = new Map();
        for (const item of article.sentences || []) {
            if (!paragraphs.has(item.paragraph)) paragraphs.set(item.paragraph, []);
            paragraphs.get(item.paragraph).push(item);
        }
        for (const items of paragraphs.values()) register({ en: items.map(item => item.en).join(' '), zh: items.map(item => item.zh).join('') }, false);
    }
    for (const item of window.EnglishMeaningReviews && window.EnglishMeaningReviews.sentences || []) {
        if (!item.zh) continue;
        const key = translationKey(item.en);
        if (!reviewedIndex.has(key)) reviewedIndex.set(key, []);
        reviewedIndex.get(key).unshift({ en: item.en, zh: item.zh, exam: item.exam, article: item.article || '', fragment: false });
    }
    function reviewedText(value, source) {
        return (reviewedIndex.get(translationKey(value)) || []).find(item =>
            (!source || !source.exam || item.exam === source.exam) &&
            (!source || !source.article || !item.article || articleKey(source.article) === articleKey(item.article)) &&
            (!item.fragment || source && source.exam && source.article));
    }
    const phrasePatternsFor = phrases => Object.keys(phrases).map(key => ({ key, parts: key.split(' ') })).sort((a, b) => b.parts.length - a.parts.length);
    function read(key, fallback) { try { const v = JSON.parse(localStorage.getItem(key)); return v == null ? fallback : v; } catch (_) { return fallback; } }
    function write(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch (_) { toast('保存失败，请先导出数据腾出空间', 'error'); return false; } }
    function toast(s, type) { if (window.EnglishApp) window.EnglishApp.toast(s, type || 'success'); }
    let enabled = read(KEYS.mode, false) === true;
    let saved = read(KEYS.sentences, []);
    if (!Array.isArray(saved)) saved = [];
    let overrides = read(KEYS.overrides, {});
    const lexicon = { phrases: lexicalData.phrases, words: lexicalData.words };
    let phrasePatterns = phrasePatternsFor(lexicon.phrases);
    let currentExam = null;
    let records = new Map();
    let renderJob = Promise.resolve();
    let renderSequence = 0;
    let selected = null;
    let clickTimer = 0;
    let popover = null;
    let selectionBar = null;
    let contextMenu = null;
    let analysis = null;
    let library = null;
    let practice = null;
    let practiceQueue = [];
    let practiceIndex = 0;
    let practiceRevealed = false;
    let previousFocus = null;
    let lookupSequence = 0;
    const dataCache = new Map();
    const translationCache = new Map();
    const localFile = window.location && window.location.protocol === 'file:';
    const lexiconReady = Promise.resolve();

    async function browserPrecisionData(examId) {
        if (!window.EnglishPrecisionBrowser || !window.EnglishPrecisionBrowser[examId]) {
            await new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = 'data/precision-browser/' + encodeURIComponent(examId) + '.js?v=' + (meanings && meanings.revision || '1');
                script.onload = resolve;
                script.onerror = reject;
                document.head.appendChild(script);
            });
        }
        const data = window.EnglishPrecisionBrowser && window.EnglishPrecisionBrowser[examId];
        if (!data) throw new Error('Missing exam context');
        return { blocks: Object.fromEntries(Object.entries(data.blocks).map(([text, refs]) => [text, refs.map(([id, a, b]) => ({ ...data.sentences[id], a, b }))])) };
    }

    function fallbackSentences(text) {
        const segmenter = new Intl.Segmenter('en', { granularity: 'sentence' });
        return Array.from(segmenter.segment(text), item => {
            const lead = item.segment.match(/^\s*/)[0].length;
            const en = item.segment.trim();
            const tokens = Array.from(en.matchAll(/[A-Za-z0-9][A-Za-z0-9'-]*/g), m => ({ a: m.index, b: m.index + m[0].length, w: m[0], l: m[0].toLowerCase(), m: '', q: 'missing', g: 1 }));
            return { a: item.index + lead, b: item.index + lead + en.length, en, zh: '', tokens, groups: [], core: [] };
        }).filter(x => x.en);
    }

    const formCache = new Map();
    function wordForms(token) {
        const raw = norm(token.w).toLowerCase(), cacheKey = raw + '|' + token.l + '|' + token.p;
        if (formCache.has(cacheKey)) return formCache.get(cacheKey);
        const forms = new Set([raw, wordKey(raw)]);
        if (meanings) forms.add(meanings.lemmaFor(raw, token));
        formCache.set(cacheKey, forms); return forms;
    }

    function phraseMatches(sentence) {
        const tokens = sentence.tokens.filter(t => /[A-Za-z0-9]/.test(t.w));
        const explicit = meanings ? meanings.phrases({ ...sentence, source: { ...sentence.source, exam: currentExam && currentExam.exam_id } }) : [];
        const matches = explicit.filter((item, i, all) => !all.some((other, j) => j < i && item.a < other.b && item.b > other.a));
        const used = new Set(tokens.flatMap((token, i) => matches.some(item => token.a < item.b && token.b > item.a) ? [i] : []));
        const equal = (token, part) => token && wordForms(token).has(part);
        for (let i = 0; i < tokens.length; i++) {
            if (used.has(i)) continue;
            for (const pattern of phrasePatterns) {
                if (!equal(tokens[i], pattern.parts[0])) continue;
                const slice = tokens.slice(i, i + pattern.parts.length);
                if (slice.length !== pattern.parts.length || slice.some((t, j) => !equal(t, pattern.parts[j]) || used.has(i + j))) continue;
                if (slice.some((t, j) => j && !/^[\s-]*$/.test(sentence.en.slice(slice[j - 1].b, t.a)))) continue;
                matches.push({ key: pattern.key, a: slice[0].a, b: slice[slice.length - 1].b, meaning: lexicon.phrases[pattern.key] });
                slice.forEach((_, j) => used.add(i + j));
                break;
            }
        }
        // Separable phrasal verbs: retain the object as ordinary words and link
        // only the verb / particle pieces under one canonical phrase key.
        const separable = ['take into account', 'take for granted', 'keep in mind', 'put off', 'point out', 'carry out', 'hold back', 'bring about', 'set up', 'turn down', 'take over', 'give up', 'cut off', 'spin off', 'spin out', 'brush off', 'shrug off', 'infuse with'];
        for (let i = 0; i < tokens.length; i++) {
            if (used.has(i)) continue;
            for (const key of separable) {
                const parts = key.split(' ');
                if (!equal(tokens[i], parts[0])) continue;
                let found = -1;
                for (let j = i + 2; j <= Math.min(i + 7, tokens.length - parts.length + 1); j++) {
                    if (/[;.!?,]/.test(sentence.en.slice(tokens[i].b, tokens[j].a))) break;
                    if (parts.slice(1).every((p, k) => equal(tokens[j + k], p)) && !used.has(j)) { found = j; break; }
                }
                if (found < 0) continue;
                const last = tokens[found + parts.length - 2];
                matches.push({ key, a: tokens[i].a, b: tokens[i].b, meaning: lexicon.phrases[key] });
                matches.push({ key, a: tokens[found].a, b: last.b, meaning: lexicon.phrases[key] });
                used.add(i); for (let j = found; j <= found + parts.length - 2; j++) used.add(j);
                break;
            }
        }
        return matches.sort((a, b) => a.a - b.a);
    }

    function sentenceHtml(sentence, id, number) {
        // Reading and lookup follow written words, not the parser's subword tokens.
        const words = meanings.writtenWords(sentence.en);
        const phrases = phraseMatches(sentence).filter(p => !words.some(w => (p.a > w.a && p.a < w.b) || (p.b > w.a && p.b < w.b) || (p.a === w.a && p.b === w.b && /[-\u2010\u2011]/.test(w.key))));
        const items = [];
        for (const p of phrases) items.push({ a: p.a, b: p.b, key: p.key, kind: 'phrase', meaning: p.meaning });
        for (const word of words) {
            if (phrases.some(p => word.a >= p.a && word.b <= p.b)) continue;
            items.push(word);
        }
        items.sort((a, b) => a.a - b.a);
        let text = '', cursor = 0;
        for (const item of items) {
            if (item.a < cursor) continue;
            text += esc(sentence.en.slice(cursor, item.a));
            const isSaved = window.EnglishApp && !!window.EnglishApp.state().words[wordKey(item.key)];
            text += '<span class="word precision-word' + (item.kind === 'phrase' ? ' precision-phrase' : /[-\u2010\u2011]/.test(item.key) ? ' precision-compound' : '') + (isSaved ? ' collected' : '') + '" data-word="' + esc(item.key) + '" data-kind="' + item.kind + '" data-start="' + item.a + '" data-end="' + item.b + '"' + (enabled ? ' tabindex="0" role="button" aria-label="查看' + esc(item.key) + '的语境义"' : '') + '>' + esc(sentence.en.slice(item.a, item.b)) + '</span>';
            cursor = item.b;
        }
        text += esc(sentence.en.slice(cursor));
        return '<span class="precision-sentence" data-sentence-id="' + id + '"' + (sentence.readingId ? ' data-reading-id="' + sentence.readingId + '"' : '') + '><button class="sentence-no" type="button" data-no="' + number + '"' + (sentence.readingId ? ' title="' + sentence.readingId + '"' : '') + ' aria-label="' + (sentence.readingId ? '精翻 ' + sentence.readingId : '翻译第' + number + '句') + '"' + (enabled ? '' : ' disabled') + '></button><span class="sentence-body">' + text + '</span></span>';
    }

    async function onRendered(exam) {
        currentExam = exam;
        const sequence = ++renderSequence;
        hideFloating();
        renderJob = (async () => {
            await lexiconReady;
            if (window.EnglishReading) await window.EnglishReading.ready(exam.exam_id);
            let data = dataCache.get(exam.exam_id);
            if (!data) {
                try {
                    if (localFile) data = await browserPrecisionData(exam.exam_id);
                    else {
                        try { const r = await fetch('data/precision/' + encodeURIComponent(exam.exam_id) + '.json?v=' + meanings.revision); if (!r.ok) throw new Error(); data = await r.json(); }
                        catch (_) { data = await browserPrecisionData(exam.exam_id); }
                    }
                    dataCache.set(exam.exam_id, data);
                } catch (_) { data = { blocks: {} }; toast('句法资料暂未加载，仍可阅读和收藏', 'warn'); }
            }
            if (sequence !== renderSequence) return;
            enhance(exam, data);
        })();
        return renderJob;
    }

    function enhance(exam, data) {
        const root = $('#examContent');
        if (!root) return;
        records = new Map();
        const headings = $$('.section-title,.part-title,.text-title', root);
        const paragraphCounts = new Map();
        const nodes = $$('p.paragraph,p.paragraph-option,.directions,.question-text,.option,.option-inline,.choice-body', root).filter(n => !n.querySelector('.choice-body,.option-inline'));
        nodes.forEach((node, blockIndex) => {
            const clone = node.cloneNode(true);
            $$('.question-num,.option-letter,.choice-letter,.sentence-no', clone).forEach(x => x.remove());
            const raw = norm(clone.textContent);
            if (!raw) return;
            let article = '', section = '';
            for (const heading of headings) {
                if (!(heading.compareDocumentPosition(node) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
                if (heading.matches('.section-title')) { section = heading.textContent.trim(); article = ''; }
                if (heading.matches('.part-title')) article = heading.textContent.trim();
                if (heading.matches('.text-title')) article = heading.textContent.trim();
            }
            const articleKey = section + ' / ' + article;
            const isParagraph = node.matches('p.paragraph,p.paragraph-option,.choice-body');
            const paragraph = isParagraph ? (paragraphCounts.get(articleKey) || 0) + 1 : 0;
            if (isParagraph) paragraphCounts.set(articleKey, paragraph);
            let sentences = data.blocks[raw] || fallbackSentences(raw);
            const articleNode = node.closest('[data-study-article]');
            const readingParagraph = node.matches('p.paragraph') && window.EnglishReading && window.EnglishReading.paragraph(exam.exam_id, articleNode && articleNode.dataset.studyArticle, raw);
            if (readingParagraph) {
                node.id = readingParagraph.id;
                sentences = readingParagraph.sentences.map(item => ({ ...(sentences.find(s => s.en === item.en) || fallbackSentences(item.en)[0]), a: item.a, b: item.b, en: item.en, readingId: item.id }));
            }
            const prefix = Array.from(node.children).filter(x => x.matches('.question-num,.option-letter,.choice-letter')).map(x => x.outerHTML).join('');
            node.classList.toggle('precision-paragraph', isParagraph);
            node.classList.toggle('precision-compact', !isParagraph);
            node.dataset.blockKey = raw;
            node.innerHTML = prefix + sentences.map((sentence, i) => {
                const id = exam.exam_id + '-' + blockIndex + '-' + i;
                const source = { exam: exam.exam_id, year: exam.year, article: [section, article].filter(Boolean).join(' / '), paragraph, sentence: i + 1, block: raw, ...(sentence.readingId ? { readingId: sentence.readingId, readingArticleId: articleNode.dataset.readingArticle } : {}) };
                const correction = reviewedText(sentence.en, source);
                records.set(id, { id, ...sentence, zh: correction ? correction.zh : sentence.zh, source });
                return sentenceHtml({ ...sentence, source }, id, i + 1);
            }).join(' ');
        });
        applyMode();
        markSavedSentences();
        if (window.EnglishReading) window.EnglishReading.decorate();
    }

    function trackHeaderHeight() {
        const nav = $('.snav'), header = $('.app-header');
        if (!nav || !header) return;
        const measure = () => {
            const navHeight = Math.ceil(nav.getBoundingClientRect().height);
            const totalHeight = navHeight + Math.ceil(header.getBoundingClientRect().height);
            document.documentElement.style.setProperty('--precision-nav-height', navHeight + 'px');
            document.documentElement.style.setProperty('--reading-header-height', totalHeight + 'px');
        };
        measure();
        const observer = new ResizeObserver(measure);
        observer.observe(nav); observer.observe(header);
    }

    function applyMode() {
        document.body.classList.toggle('precision-enabled', enabled);
        const button = $('#precisionModeBtn');
        if (button) { button.textContent = enabled ? '精翻中 · 退出' : '进入精翻'; button.setAttribute('aria-pressed', String(enabled)); }
        const hint = enabled ? '精翻中：单击查义 · 双击收藏词语 · 点句子编号查看分块精翻 · 划选后右键收藏长难句' : '普通阅读：点击右上角「进入精翻」开启查词、词组学习和长难句收藏';
        const sub = $('.brand-sub'); if (sub) sub.textContent = enabled ? '精翻模式 · 单击查义，双击收藏词语' : '普通阅读 · 进入精翻后单击查义，双击收藏';
        const bar = $('#examContent .hint-bar'); if (bar) bar.textContent = hint;
        $$('.sentence-no').forEach(b => { b.disabled = !enabled; });
        $$('#examContent .precision-word').forEach(w => {
            if (enabled) { w.tabIndex = 0; w.setAttribute('role', 'button'); w.setAttribute('aria-label', '查看' + w.dataset.word + '的语境义'); }
            else { w.removeAttribute('tabindex'); w.removeAttribute('role'); w.removeAttribute('aria-label'); }
        });
        if (!enabled) { hideFloating(); closeAnalysis(); }
    }

    function hash(s) { let h = 2166136261; for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619); return (h >>> 0).toString(36); }
    function contextKey(record, start, word) { return hash(record.source.exam + '|' + record.en + '|' + start + '|' + wordKey(word)); }
    function phraseSense(key, record, start, end) {
        const found = meanings.lookup({ word: key, kind: 'phrase', record, start, end });
        return { meaning: found.meaning, quality: found.quality, lemma: found.lemma };
    }
    function wordEntry(lemma) { return meanings.entry(lemma); }
    function wordMorphology(info) {
        const phrase = info.kind === 'phrase', parts = info.lemma.split(' '), head = phrase ? parts[0] : info.lemma;
        const family = wordData.words[head];
        const surface = wordKey(info.element && info.element.textContent || info.word);
        const writtenHead = phrase ? surface.split(' ')[0] : surface;
        const matches = (wordData.index[writtenHead] || []).filter(item => item.lemma === head && (!info.token || !info.token.p || item.p === info.token.p));
        const labels = writtenHead === head ? [] : [...new Set(matches.map(item => item.label).filter(label => label !== '原形'))];
        const tail = phrase ? parts.slice(1).join(' ') : '';
        const forms = family && (!phrase || family.pos.includes('v')) ? family.forms.filter(item => !phrase || ['第三人称单数', '过去式', '过去分词', '现在分词／动名词', '现在式'].includes(item.label)).map(item => ({ label: item.label, words: item.words.map(word => tail ? word + ' ' + tail : word) })) : [];
        return { lemma: info.lemma, labels, forms };
    }
    function morphologyHtml(info) {
        const morphology = wordMorphology(info);
        const label = info.kind === 'phrase' ? '词组原形' : info.lemma.includes("'") && !wordData.words[info.lemma] ? '当前词形' : '原形';
        return '<div class="precision-lemma"><span>' + label + '</span><b>' + esc(morphology.lemma) + '</b>' + (morphology.labels.length ? '<small>当前为' + esc(morphology.labels.join('／')) + '</small>' : '') + '</div>';
    }
    function formsHtml(info) {
        const morphology = wordMorphology(info);
        return '<section class="precision-word-forms"><label>相关词形</label>' + (morphology.forms.length ? '<dl>' + morphology.forms.map(item => '<div><dt>' + esc(item.label) + '</dt><dd>' + esc(item.words.join(' / ')) + '</dd></div>').join('') + '</dl>' : '<p class="precision-note">暂无其他已收录的词形</p>') + '</section>';
    }
    function wordInfo(element) {
        const record = records.get(element.closest('.precision-sentence').dataset.sentenceId);
        if (!record) return null;
        const word = element.dataset.word, start = Number(element.dataset.start), end = Number(element.dataset.end);
        const token = record.tokens.find(t => t.a === start) || record.tokens.find(t => t.a <= start && t.b > start);
        const kind = element.dataset.kind === 'phrase' ? 'phrase' : 'word';
        const found = meanings.lookup({ word, record, token, kind, start, end });
        const overrideKey = contextKey(record, start, word), override = found.quality === 'manual' ? found.meaning : overrides[overrideKey];
        return { ...found, record, token: found.token, key: overrideKey, element,
            meaning: override || found.meaning, quality: override ? 'manual' : found.quality };
    }
    function meaningLabel(info) {
        return { reviewed: '本文义', manual: '本文义 · 你的校正', grammar: '本句语法作用',
            dictionary: '词典释义 · 按本句词性', phrase: '词典释义 · 词组', name: '名称释义', missing: '中文释义' }[info.quality] || '词典释义';
    }
    function position(box, anchor) {
        const r = anchor && anchor.getBoundingClientRect ? anchor.getBoundingClientRect() : anchor;
        if (!r) return;
        box.style.display = 'block';
        const width = box.offsetWidth, height = box.offsetHeight;
        box.style.left = Math.max(12, Math.min(r.left, innerWidth - width - 12)) + 'px';
        box.style.top = Math.max(12, Math.min(r.bottom + 8, innerHeight - height - 12)) + 'px';
    }
    function ensurePopover() {
        if (popover) return popover;
        popover = document.createElement('section'); popover.className = 'precision-popover'; popover.setAttribute('role', 'dialog'); popover.setAttribute('aria-label', '词语释义'); document.body.appendChild(popover); return popover;
    }
    function showWord(element) {
        if (!enabled) return;
        const info = wordInfo(element); if (!info) return;
        lookupSequence++;
        renderWordPopover(info, { ...wordEntry(info.lemma), common: info.common, ph: info.ph }, false);
    }
    function renderWordPopover(info, common, loading) {
        const element = info.element;
        const box = ensurePopover();
        const alternatives = common && common.common || [];
        const others = alternatives.filter(s => s.m !== info.meaning).slice(0, 3);
        box.innerHTML = '<div class="precision-pop-head"><div><strong>' + esc(info.word) + '</strong><span>' + (info.kind === 'phrase' ? '词组' : esc(common && common.ph || '')) + '</span></div><button data-action="close" class="precision-icon-close" aria-label="关闭释义">×</button></div>' +
            morphologyHtml(info) +
            '<div class="precision-current" aria-live="polite"><label>' + meaningLabel(info) + '</label><p>' + esc(info.meaning || '这个词暂未收录，可查看词典或补充本句释义。') + '</p></div>' +
            (info.explanation ? '<p class="precision-word-explanation">' + esc(info.explanation) + '</p>' : '') +
            (others.length ? '<div class="precision-common"><label>其他常见义</label>' + others.map(s => '<p><span class="precision-sense-pos">' + esc(posName(s.p)) + '</span>' + esc(s.m) + '</p>').join('') + '</div>' : '') +
            formsHtml(info) +
            '<div class="precision-pop-actions"><button data-action="collect">收藏' + (info.kind === 'phrase' ? '整个词组' : '单词') + '</button><button data-action="sentence">句子精翻</button><button data-action="edit">改本句释义</button></div>' +
            '<div class="precision-dictionary-links"><a href="https://dict.youdao.com/result?word=' + encodeURIComponent(info.lemma) + '&amp;lang=en" target="_blank" rel="noreferrer">有道核对</a><a href="https://dictionary.cambridge.org/dictionary/english-chinese-simplified/' + encodeURIComponent(info.lemma.replace(/ /g, '-')) + '" target="_blank" rel="noreferrer">剑桥核对</a></div>';
        box.onclick = async event => {
            const button = event.target.closest('[data-action]'); if (!button) return;
            if (button.dataset.action === 'close') hidePopover();
            if (button.dataset.action === 'retry') showWord(element);
            if (button.dataset.action === 'collect') collectInfo(info);
            if (button.dataset.action === 'sentence') openAnalysis(selectionFromRecords([info.record], info.record.en));
            if (button.dataset.action === 'edit') {
                lookupSequence++;
                const current = $('.precision-current', box);
                current.innerHTML = '<label for="contextMeaningInput">本句语境义</label><input id="contextMeaningInput" value="' + esc(info.meaning) + '" placeholder="输入这个词在本句中的意思"><button type="button" id="saveContextMeaning">保存本句释义</button>';
                $('#contextMeaningInput', box).focus();
                $('#saveContextMeaning', box).onclick = () => {
                    const value = $('#contextMeaningInput', box).value.trim(); if (!value) return;
                    const next = { ...overrides, [info.key]: value };
                    if (!write(KEYS.overrides, next)) return;
                    overrides = next;
                    if (window.EnglishReading) window.EnglishReading.setWord(info.record, Number(element.dataset.start), Number(element.dataset.end), { lemma: info.lemma, meaning: value, kind: info.kind });
                    const collected = window.EnglishApp.state().words[wordKey(info.word)];
                    if (collected && collected.sentence === info.record.en) window.EnglishApp.collect(info.word, { meaning: value, meaningQuality: 'manual' }, { silent: true });
                    toast('已保存这处语境义'); showWord(element);
                };
            }
        };
        position(box, element);
    }
    function collectInfo(info) {
        if (!info) return;
        const reading = window.EnglishReading && window.EnglishReading.current(window.EnglishReading.match(info.record));
        const details = () => ({ kind: info.kind, lemma: info.lemma, meaning: info.meaning, meaningQuality: info.quality, sentence: info.record.en, translation: reading && reading.status === 'reviewed' ? reading.translation : info.record.zh, source: info.record.source, contextToken: info.token ? { ...info.token, a: Number(info.element.dataset.start), b: Number(info.element.dataset.end) } : null });
        window.EnglishApp.collect(info.word, details());

    }
    function hidePopover() { lookupSequence++; if (popover) popover.style.display = 'none'; }
    function hideSelection() { if (selectionBar) selectionBar.style.display = 'none'; if (contextMenu) contextMenu.style.display = 'none'; }
    function hideFloating() { clearTimeout(clickTimer); hidePopover(); hideSelection(); selected = null; }

    function selectionFromRecords(list, text) { return { text: text.trim(), context: list.map(r => r.en).join(' '), segments: list.map(r => ({ en: r.en, zh: r.zh, tokens: r.tokens, groups: r.groups, core: r.core })), source: list[0] && list[0].source, sourceIds: list.map(r => r.id), ranges: list.map(r => ({ en: r.en, a: 0, b: r.en.length, source: r.source })) }; }
    function selectionSegments(payload) {
        const segments = payload.segments || [];
        const ranges = savedRanges(payload);
        const clipped = ranges.flatMap(range => {
            const segment = segments.find(s => norm(s.en) === norm(range.en));
            if (!segment || !Number.isInteger(range.a) || !Number.isInteger(range.b)) return [];
            let a = Math.max(0, range.a), b = Math.min(segment.en.length, range.b);
            while (a < b && /\s/.test(segment.en[a])) a++;
            while (b > a && /\s/.test(segment.en[b - 1])) b--;
            if (b <= a) return [];
            if (a === 0 && b === segment.en.length) return [segment];
            const en = segment.en.slice(a, b);
            const tokens = (segment.tokens || []).filter(t => t.a < b && t.b > a).map(t => ({ ...t, a: Math.max(a, t.a) - a, b: Math.min(b, t.b) - a, w: segment.en.slice(Math.max(a, t.a), Math.min(b, t.b)) }));
            const ids = new Set(tokens.map(t => t.g));
            const hasWord = word => word && tokens.some(t => t.w === word);
            const groups = (segment.groups || []).filter(g => ids.has(g.id)).map(g => ({ ...g, label: hasWord(g.head) ? g.label : '选区片段', head: hasWord(g.head) ? g.head : '', attach: hasWord(g.attach) ? g.attach : '', parent: ids.has(g.parent) ? g.parent : null }));
            const core = (segment.core || []).filter(c => en.includes(c.text));
            return [{ en, zh: '', tokens, groups, core }];
        });
        // Unmatched old imports still translate only their saved selection.
        return clipped.length && norm(clipped.map(s => s.en).join(' ')) === norm(payload.text) ? clipped : [{ en: norm(payload.text), zh: '', tokens: [], groups: [], core: [] }];
    }
    function captureSelection() {
        const selection = window.getSelection(); const root = $('#examContent');
        if (!selection || selection.isCollapsed || !selection.rangeCount || !root.contains(selection.anchorNode) || !root.contains(selection.focusNode)) return null;
        const range = selection.getRangeAt(0);
        const list = [], ranges = [];
        $$('.precision-sentence', root).forEach(el => {
            const body = $('.sentence-body', el), record = records.get(el.dataset.sentenceId);
            if (!body || !record || !range.intersectsNode(body)) return;
            const bounds = document.createRange(); bounds.selectNodeContents(body);
            const clipped = range.cloneRange();
            if (clipped.compareBoundaryPoints(Range.START_TO_START, bounds) < 0) clipped.setStart(bounds.startContainer, bounds.startOffset);
            if (clipped.compareBoundaryPoints(Range.END_TO_END, bounds) > 0) clipped.setEnd(bounds.endContainer, bounds.endOffset);
            const prefix = document.createRange(); prefix.selectNodeContents(body); prefix.setEnd(clipped.startContainer, clipped.startOffset);
            const a = prefix.toString().length, b = a + clipped.toString().length;
            if (b <= a) return;
            list.push(record); ranges.push({ en: record.en, a, b, source: record.source });
        });
        if (!list.length) return null;
        const text = norm(ranges.map(r => r.en.slice(r.a, r.b)).join(' '));
        if (!/[A-Za-z]/.test(text) || !/\s/.test(text)) return null;
        return { ...selectionFromRecords(list, text), ranges, rect: range.getBoundingClientRect() };
    }
    function showSelectionToolbar(payload, rightClick) {
        selected = payload; hidePopover();
        let box = rightClick ? contextMenu : selectionBar;
        if (!box) {
            box = document.createElement('div'); box.className = rightClick ? 'precision-context-menu' : 'precision-selection-bar'; box.setAttribute('role', rightClick ? 'menu' : 'toolbar');
            document.body.appendChild(box); if (rightClick) contextMenu = box; else selectionBar = box;
        }
        box.innerHTML = '<button data-action="translate">翻译选区</button><button data-action="save">收藏到长难句</button><button data-action="phrase">收藏为词组</button>';
        bindSentenceSaveButton($('[data-action="save"]', box), payload);
        box.onmousedown = e => e.preventDefault();
        box.onclick = e => {
            const b = e.target.closest('button'); if (!b || !selected) return;
            const item = selected;
            if (b.dataset.action === 'translate') openAnalysis(item);
            if (b.dataset.action === 'save') saveSentence(item);
            if (b.dataset.action === 'phrase') collectSelectionPhrase(item);
            hideSelection();
        };
        if (rightClick && selectionBar) selectionBar.style.display = 'none';
        position(box, payload.rect);
    }
    function collectSelectionPhrase(payload) {
        const value = norm(payload.text);
        if (value.split(/\s+/).length > 12 || /[.!?;]/.test(value)) { toast('这段内容较长，请收藏到长难句', 'warn'); return; }
        const sentence = fallbackSentences(value)[0];
        const matched = sentence && phraseMatches(sentence).find(p => p.a === 0 && p.b === value.length);
        const key = matched ? matched.key : wordKey(value);
        const record = { en: payload.context, zh: '', source: payload.source || {} };
        const sense = phraseSense(key, record);
        window.EnglishApp.collect(matched ? key : value, { kind: 'phrase', lemma: key, meaning: sense.meaning, meaningQuality: sense.meaning ? sense.quality : 'missing', sentence: payload.context, translation: payload.selectionTranslation && payload.selectionTranslation.en === value ? payload.selectionTranslation.zh : '', source: payload.source });
    }

    const circled = id => id <= 20 ? String.fromCodePoint(0x2460 + id - 1) : '(' + id + ')';
    function structureHtml(segment) {
        if (!segment.groups || !segment.groups.length) return '<p class="precision-note">这段内容暂未收录句法结构，可以保留原文与译文继续练习。</p>';
        const tokens = segment.tokens;
        let result = '', cursor = 0, lastGroup = null;
        const seen = new Set();
        for (const t of tokens) {
            const group = segment.groups.find(g => g.id === t.g) || segment.groups[0];
            result += esc(segment.en.slice(cursor, t.a));
            let marker = '';
            if (group.id !== lastGroup && /[A-Za-z]/.test(t.w)) {
                marker = '<span class="grammar-marker">' + (seen.has(group.id) ? '续' + circled(group.id) : circled(group.id) + group.label) + '</span>';
                seen.add(group.id); lastGroup = group.id;
            }
            result += '<span class="grammar-token grammar-color-' + ((group.id - 1) % 6) + '" title="' + esc(circled(group.id) + ' ' + group.label + (group.attach ? '，连接 ' + group.attach : '')) + '">' + marker + esc(segment.en.slice(t.a, t.b)) + '</span>';
            cursor = t.b;
        }
        result += esc(segment.en.slice(cursor));
        const core = (segment.core || []).map(c => '<span><small>' + esc(c.role) + '</small>' + esc(c.text) + '</span>').join('<b class="grammar-arrow">→</b>');
        const links = segment.groups.filter(g => g.id !== 1 && g.head && g.attach && g.parent).map(g => '<li><span class="grammar-label grammar-color-' + ((g.id - 1) % 6) + '">' + circled(g.id) + ' ' + esc(g.label) + '</span><span>以 <b>' + esc(g.head) + '</b> 为中心，连接 ' + circled(g.parent) + ' 中的 <b>' + esc(g.attach) + '</b></span></li>').join('');
        return (core ? '<div class="grammar-core">' + core + '</div>' : '') + '<div class="grammar-text">' + result + '</div>' + (links ? '<ul class="grammar-links">' + links + '</ul>' : '') + '<p class="precision-note">同号、同色属于同一结构；“续”表示越过插入部分后接回原结构。句法为自动分析，可结合译文校对。</p>';
    }

    function makeOverlay(className, title) {
        const overlay = document.createElement('div'); overlay.className = 'precision-overlay ' + className;
        overlay.innerHTML = '<section class="precision-modal" role="dialog" aria-modal="true" aria-label="' + esc(title) + '"><header><div><span class="precision-eyebrow">ENGLISH II · 精翻</span><h2>' + esc(title) + '</h2></div><button class="precision-icon-close" data-close aria-label="关闭">×</button></header><div class="precision-modal-body"></div></section>';
        document.body.appendChild(overlay);
        overlay.addEventListener('click', e => { if (e.target === overlay || e.target.closest('[data-close]')) closeOverlay(overlay); });
        overlay.addEventListener('keydown', e => {
            if (e.key !== 'Tab') return;
            const focusable = $$('button:not([disabled]),input,textarea,a[href],summary,select', overlay).filter(x => x.offsetParent !== null);
            if (!focusable.length) return;
            if (e.shiftKey && document.activeElement === focusable[0]) { e.preventDefault(); focusable[focusable.length - 1].focus(); }
            else if (!e.shiftKey && document.activeElement === focusable[focusable.length - 1]) { e.preventDefault(); focusable[0].focus(); }
        });
        return overlay;
    }
    function showOverlay(overlay) { if (!overlay.classList.contains('is-open')) previousFocus = document.activeElement; overlay.hidden = false; overlay.classList.add('is-open'); document.body.classList.add('precision-modal-open'); $('[data-close]', overlay).focus(); }
    function closeOverlay(overlay) {
        if (!overlay) return;
        overlay.classList.remove('is-open'); overlay.hidden = true;
        if (!$('.precision-overlay.is-open')) document.body.classList.remove('precision-modal-open');
        if (previousFocus && previousFocus.isConnected) previousFocus.focus({ preventScroll: true });
    }
    async function fetchTranslation(url) {
        const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 12000);
        try {
            const response = await fetch(url, { signal: controller.signal, credentials: 'omit', referrerPolicy: 'no-referrer' });
            if (!response.ok) throw new Error('Translation unavailable');
            return await response.json();
        } finally { clearTimeout(timer); }
    }
    async function translateExactText(text) {
        const correction = reviewedText(text);
        if (correction) return correction.zh;
        let local = null;
        try { local = await window.EnglishApp.translate(text); } catch (_) {}
        if (local && local.mode === 'exact' && local.zh) return local.zh;
        // MyMemory limits each query to 500 UTF-8 bytes. Every query contains
        // only the selected text; no containing sentence is substituted.
        const chunks = [], encoder = new TextEncoder(); let rest = text;
        while (encoder.encode(rest).length > 450) {
            let end = Math.min(450, rest.length);
            while (encoder.encode(rest.slice(0, end)).length > 450) end--;
            const space = rest.lastIndexOf(' ', end); if (space > 0) end = space;
            chunks.push(rest.slice(0, end)); rest = rest.slice(end).trim();
        }
        if (rest) chunks.push(rest);
        const translations = [];
        try {
            for (const chunk of chunks) {
                const data = await fetchTranslation('https://api.mymemory.translated.net/get?' + new URLSearchParams({ q: chunk, langpair: 'en|zh-CN' }));
                const zh = data.responseData && data.responseData.translatedText;
                if (Number(data.responseStatus) !== 200 || data.quotaFinished || !zh) throw new Error('Translation unavailable');
                const decoded = document.createElement('textarea'); decoded.innerHTML = zh;
                translations.push(decoded.value);
            }
            return translations.join('');
        } catch (_) {
            const data = await fetchTranslation('https://translate.googleapis.com/translate_a/single?' + new URLSearchParams({ client: 'gtx', sl: 'en', tl: 'zh-CN', dt: 't', q: text }));
            const zh = Array.isArray(data[0]) ? data[0].map(part => part && part[0] || '').join('') : '';
            if (!zh) throw new Error('Translation unavailable');
            return zh;
        }
    }
    async function fillSelectionTranslation(payload) {
        const text = norm(payload.text);
        if (window.EnglishReading && window.EnglishReading.scope({ source: payload.source })) {
            if (payload.selectionTranslation && payload.selectionTranslation.kind === 'manual' && payload.selectionTranslation.en === text) return payload.selectionTranslation.zh;
            await window.EnglishReading.ready(payload.source.exam);
            const item = window.EnglishReading.current(window.EnglishReading.match({ en: text, source: payload.source }));
            if (item && (item.manualTranslation || item.status === 'reviewed' && item.article.source.status === 'verified')) {
                payload.selectionTranslation = { en: text, zh: item.translation, kind: item.manualTranslation ? 'manual' : 'reviewed', readingId: item.id };
                return item.translation;
            }
            return '';
        }
        let correction = reviewedText(text, payload.source);
        const segments = selectionSegments(payload);
        if (!correction) {
            const corrected = segments.map(segment => reviewedText(segment.en, payload.source));
            if (corrected.length && corrected.every(Boolean) && norm(segments.map(segment => segment.en).join(' ')) === text) correction = { zh: corrected.map(item => item.zh).join('\n\n') };
        }
        // Checked text supersedes earlier machine output, including saved selections.
        if (correction) {
            payload.selectionTranslation = { en: text, zh: correction.zh, kind: 'reviewed', revision: reviewed.revision };
            return correction.zh;
        }
        if (payload.selectionTranslation && payload.selectionTranslation.en === text && payload.selectionTranslation.zh) return payload.selectionTranslation.zh;
        let zh = segments.every(s => s.zh) ? segments.map(s => s.zh).join('\n\n') : '';
        if (!zh) {
            if (!translationCache.has(text)) translationCache.set(text, translateExactText(text).catch(() => { translationCache.delete(text); return ''; }));
            zh = await translationCache.get(text);
        }
        if (zh) payload.selectionTranslation = { en: text, zh, kind: 'reference' };
        return zh;
    }
    function sourceLabel(source) { return source ? source.year + ' 英语二 · ' + source.article + (source.paragraph ? ' · 第' + source.paragraph + '段' : '') + ' 第' + source.sentence + '句' : '自选长难句'; }
    function closeAnalysis() { if (analysis) closeOverlay(analysis); }
    function sentenceSaveId(payload) { return hash((payload.source && payload.source.exam || '') + '|' + payload.text.trim()); }
    function syncSentenceSaveButtons() {
        const ids = new Set(saved.map(item => item.id));
        $$('[data-save-sentence-id]').forEach(button => {
            const collected = ids.has(button.dataset.saveSentenceId);
            button.textContent = collected ? '已收录长难句' : '收藏到长难句';
            button.disabled = collected;
            button.classList.toggle('precision-sentence-saved', collected);
        });
    }
    function bindSentenceSaveButton(button, payload) {
        button.dataset.saveSentenceId = sentenceSaveId(payload);
        syncSentenceSaveButtons();
    }
    async function openAnalysis(payload) {
        hideFloating();
        if (!analysis) analysis = makeOverlay('precision-analysis', '句子精翻');
        const body = $('.precision-modal-body', analysis);
        const reading = window.EnglishReading;
        const original = reading && reading.match({ en: payload.text, source: payload.source });
        const item = original && reading.current(original);
        const complete = item && item.status === 'reviewed' && item.article.source.status === 'verified';
        const translation = item && (complete || item.manualTranslation) ? item.translation : '';
        const editor = item ? '<details class="reading-editor"><summary>纠正本句翻译</summary><form id="readingCorrectionForm">' +
            (complete ? item.chunks.map((chunk, i) => '<label><span lang="en">' + esc(chunk.en) + '</span><textarea data-chunk="' + i + '" rows="2">' + esc(chunk.zh) + '</textarea></label>').join('') : '') +
            '<label for="readingReorderInput">语序调整<textarea id="readingReorderInput" rows="2">' + esc(item.reorder || '') + '</textarea></label>' +
            '<label for="readingTranslationInput">完整翻译<textarea id="readingTranslationInput" rows="4">' + esc(translation) + '</textarea></label><button class="precision-primary" type="submit">保存本句校正</button><p class="precision-note">保存到当前浏览器，随完整备份和纠错文件一起导出。</p></form></details>' : '';
        body.innerHTML = '<p class="precision-source">' + esc(item ? item.id + ' · ' + (item.article.source.status === 'verified' ? '原文已核对' : '原文待核对') : sourceLabel(payload.source)) + '</p>' +
            '<div class="precision-selected"><label>你选中的内容</label><p>' + esc(payload.text) + '</p></div>' +
            (item && item.sourceNote ? '<p class="reading-source-note">' + esc(item.sourceNote) + '</p>' : '') +
            '<div class="precision-analysis-actions"><button id="saveAnalyzedSentence" class="precision-primary">收藏到长难句</button><button type="button" id="exportReadingCorrections">导出纠错记录</button></div>' +
            '<section class="reading-translation-section"><h3>分块对照</h3>' + (complete ? '<table class="reading-chunks"><thead><tr><th>英文</th><th>中文</th></tr></thead><tbody>' + item.chunks.map(chunk => '<tr><td lang="en">' + esc(chunk.en) + '</td><td>' + esc(chunk.zh) + '</td></tr>').join('') + '</tbody></table>' : '<p class="reading-pending">尚未整理</p>') + '</section>' +
            '<section class="reading-translation-section"><h3>语序调整</h3><p>' + esc(item && (complete || item.custom) && item.reorder || '尚未整理') + '</p></section>' +
            '<section class="reading-translation-section"><h3>完整翻译</h3><p class="precision-translation">' + esc(translation || '尚未整理') + '</p></section>' + editor +
            (!item ? '<p class="precision-note">这段选区尚未单独整理；保留实际选区，不自动扩展到整句，也不填入机译。</p>' : '');
        if (translation) payload.selectionTranslation = { en: norm(payload.text), zh: translation, kind: item.manualTranslation ? 'manual' : 'reviewed', readingId: item.id };
        $('#saveAnalyzedSentence', body).onclick = () => saveSentence(payload);
        bindSentenceSaveButton($('#saveAnalyzedSentence', body), payload);
        $('#exportReadingCorrections', body).onclick = () => reading && reading.downloadCorrections();
        const form = $('#readingCorrectionForm', body);
        if (form) form.onsubmit = event => {
            event.preventDefault();
            const patch = { translation: $('#readingTranslationInput', form).value.trim(), reorder: $('#readingReorderInput', form).value.trim() };
            if (complete) patch.chunks = item.chunks.map((chunk, i) => ({ a: chunk.a, b: chunk.b, zh: $('[data-chunk="' + i + '"]', form).value.trim() }));
            if (!patch.translation || complete && patch.chunks.some(chunk => !chunk.zh)) { toast('请填写完整译文和每块中文', 'warn'); return; }
            if (reading.setEdit(original, patch)) { toast('已保存本句校正'); openAnalysis(payload); }
        };
        showOverlay(analysis);
        const savedItem = saved.find(s => s.id === sentenceSaveId(payload));
        if (savedItem && payload.selectionTranslation) persistItem(savedItem, { selectionTranslation: payload.selectionTranslation });
    }

    function saveSentence(payload) {
        const text = payload.text.trim(); if (!text) return;
        const id = sentenceSaveId(payload);
        if (saved.some(s => s.id === id)) { syncSentenceSaveButtons(); toast('这条长难句已经收录'); return; }
        const item = { id, text, context: payload.context, segments: payload.segments, source: payload.source, ranges: payload.ranges, selectionTranslation: payload.selectionTranslation, createdAt: Date.now(), draft: '', reference: '', reviews: 0, nextReviewAt: 0, level: 0 };
        const next = [item, ...saved];
        if (!write(KEYS.sentences, next)) return;
        saved = next; updateBookCount(); toast('已收藏到长难句');
    }
    // Older collections stored the selected text and complete context, without offsets.
    function savedRanges(item) {
        if (Array.isArray(item.ranges)) return item.ranges;
        const segments = item.segments || [];
        const context = segments.map(s => norm(s.en)).join(' '), text = norm(item.text);
        if (!text) return [];
        let start = context.indexOf(text), end = start + text.length;
        if (start < 0) {
            const positions = [], chars = [];
            for (let i = 0; i < context.length; i++) if (!/\s/.test(context[i])) { positions.push(i); chars.push(context[i]); }
            const compact = text.replace(/\s/g, ''), match = chars.join('').indexOf(compact);
            if (match < 0) return [];
            start = positions[match]; end = positions[match + compact.length - 1] + 1;
        }
        let offset = 0;
        return segments.flatMap(segment => {
            const en = norm(segment.en), a = Math.max(0, start - offset), b = Math.min(en.length, end - offset);
            offset += en.length + 1;
            return b > a ? [{ en, a, b }] : [];
        });
    }
    function markSavedSentences() {
        const root = $('#examContent'); if (!root || !currentExam) return;
        $$('.precision-saved-text', root).forEach(mark => { const parent = mark.parentNode; mark.replaceWith(...mark.childNodes); parent.normalize(); });
        const byText = new Map(), highlights = new Map();
        for (const record of records.values()) {
            const key = norm(record.en);
            if (!byText.has(key)) byText.set(key, []);
            byText.get(key).push(record);
        }
        for (const item of saved) {
            if (item.source && item.source.exam !== currentExam.exam_id) continue;
            for (const range of savedRanges(item)) {
                if (!Number.isInteger(range.a) || !Number.isInteger(range.b)) continue;
                const source = range.source || item.source;
                for (const record of byText.get(norm(range.en)) || []) {
                    if (source && (source.exam && source.exam !== record.source.exam || source.article && source.article !== record.source.article)) continue;
                    if (range.source && (range.source.block !== record.source.block || range.source.sentence !== record.source.sentence)) continue;
                    const a = Math.max(0, range.a), b = Math.min(record.en.length, range.b);
                    if (b <= a) continue;
                    if (!highlights.has(record.id)) highlights.set(record.id, []);
                    highlights.get(record.id).push({ a, b });
                }
            }
        }
        for (const [id, ranges] of highlights) {
            const body = $('[data-sentence-id="' + id + '"] .sentence-body', root); if (!body) continue;
            const merged = [];
            for (const range of ranges.sort((a, b) => a.a - b.a)) {
                const last = merged[merged.length - 1];
                if (last && range.a <= last.b) last.b = Math.max(last.b, range.b); else merged.push({ ...range });
            }
            const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT), nodes = [];
            while (walker.nextNode()) nodes.push(walker.currentNode);
            let offset = 0;
            for (const node of nodes) {
                const value = node.textContent, start = offset; offset += value.length;
                const overlaps = merged.filter(r => r.a < offset && r.b > start);
                if (!overlaps.length) continue;
                const fragment = document.createDocumentFragment(); let cursor = 0;
                for (const range of overlaps) {
                    const a = Math.max(0, range.a - start), b = Math.min(value.length, range.b - start);
                    fragment.appendChild(document.createTextNode(value.slice(cursor, a)));
                    const mark = document.createElement('mark'); mark.className = 'precision-saved-text'; mark.title = '已收藏到长难句'; mark.textContent = value.slice(a, b); fragment.appendChild(mark);
                    cursor = b;
                }
                fragment.appendChild(document.createTextNode(value.slice(cursor))); node.replaceWith(fragment);
            }
        }
    }
    function updateBookCount() { const count = $('#sentenceBookCount'); if (count) count.textContent = saved.length; syncSentenceSaveButtons(); markSavedSentences(); }
    function persistItem(item, change) { const next = saved.map(s => s.id === item.id ? { ...s, ...change } : s); if (write(KEYS.sentences, next)) { saved = next; Object.assign(item, change); } }
    function openLibrary() {
        hideFloating(); closeAnalysis();
        if (!library) library = makeOverlay('precision-library', '我的长难句');
        renderLibrary(); showOverlay(library);
    }
    function renderLibrary() {
        const body = $('.precision-modal-body', library);
        const due = saved.filter(s => !s.nextReviewAt || s.nextReviewAt <= Date.now()).length;
        body.innerHTML = '<div class="sentence-library-summary"><div><strong>' + saved.length + '</strong> 条收藏 <span>· 今天待练 ' + due + ' 条</span></div><button id="practiceAllSentences" class="precision-primary"' + (!saved.length ? ' disabled' : '') + '>开始练习</button></div><label class="precision-search-label">搜索原文或出处<input id="sentenceSearch" placeholder="输入句子、年份或文章编号"></label><div id="sentenceLibraryList"></div>';
        $('#practiceAllSentences', body).onclick = () => startPractice(saved.filter(s => !s.nextReviewAt || s.nextReviewAt <= Date.now()).length ? saved.filter(s => !s.nextReviewAt || s.nextReviewAt <= Date.now()) : saved);
        $('#sentenceSearch', body).oninput = e => drawSentenceList(e.target.value);
        drawSentenceList('');
    }
    function drawSentenceList(query) {
        const list = $('#sentenceLibraryList', library);
        const matches = saved.filter(s => (s.text + ' ' + sourceLabel(s.source)).toLowerCase().includes(query.toLowerCase()));
        if (!matches.length) { list.innerHTML = '<div class="precision-empty">' + (saved.length ? '没有匹配的长难句' : '精翻时选中任意长度的原文，右键选择“收藏到长难句”。') + '</div>'; return; }
        list.innerHTML = matches.map(item => '<article class="sentence-saved-card" data-id="' + item.id + '"><p class="precision-source">' + esc(sourceLabel(item.source)) + '</p><p class="sentence-saved-text">' + esc(item.text) + '</p><footer><span>' + (item.reviews ? '已练 ' + item.reviews + ' 次 · ' + (item.nextReviewAt <= Date.now() ? '待复习' : '下次 ' + new Date(item.nextReviewAt).toLocaleDateString('zh-CN')) : '尚未练习') + '</span><div><button data-action="practice">练这句</button><button data-action="source">回到原文</button><button data-action="remove">删除</button></div></footer></article>').join('');
        list.onclick = async e => {
            const b = e.target.closest('[data-action]'); if (!b) return;
            const item = saved.find(s => s.id === b.closest('[data-id]').dataset.id); if (!item) return;
            if (b.dataset.action === 'practice') startPractice([item]);
            if (b.dataset.action === 'source') {
                closeOverlay(library); closeOverlay(practice);
                if (item.source && currentExam && item.source.exam !== currentExam.exam_id) await window.EnglishApp.selectExam(item.source.exam);
                await renderJob;
                const rec = Array.from(records.values()).find(r => r.en === item.segments[0].en && (!item.source || r.source.article === item.source.article));
                const target = rec && $('[data-sentence-id="' + rec.id + '"]');
                if (target) { target.scrollIntoView({ block: 'center', behavior: 'smooth' }); target.classList.add('precision-located'); setTimeout(() => target.classList.remove('precision-located'), 2400); }
                else toast('该句仍在收藏中，原文位置暂未匹配到', 'warn');
            }
            if (b.dataset.action === 'remove' && confirm('从长难句本删除这条收藏？')) { const next = saved.filter(s => s.id !== item.id); if (write(KEYS.sentences, next)) { saved = next; updateBookCount(); renderLibrary(); } }
        };
    }
    function startPractice(items) {
        closeOverlay(library); closeAnalysis();
        practiceQueue = items.map(s => s.id); practiceIndex = 0; practiceRevealed = false;
        if (!practice) practice = makeOverlay('precision-practice', '长难句练习');
        renderPractice(); showOverlay(practice);
    }
    function renderPractice() {
        const body = $('.precision-modal-body', practice);
        const item = saved.find(s => s.id === practiceQueue[practiceIndex]);
        if (!item) { body.innerHTML = '<div class="precision-practice-done"><h3>这组长难句练完了</h3><p>译文草稿和复习进度已保存在本机。</p><button id="backToSentenceBook" class="precision-primary">回到长难句本</button></div>'; $('#backToSentenceBook', body).onclick = () => { closeOverlay(practice); openLibrary(); }; return; }
        const segments = selectionSegments(item);
        const translation = item.selectionTranslation && item.selectionTranslation.en === norm(item.text) ? item.selectionTranslation.zh : '';
        body.innerHTML = '<div class="sentence-practice-progress"><span>第 ' + (practiceIndex + 1) + ' / ' + practiceQueue.length + ' 条</span><span>先自己翻译，再对照结构</span></div><p class="precision-source">' + esc(sourceLabel(item.source)) + '</p><p class="practice-prompt">' + esc(item.text) + '</p><label class="practice-draft-label">我的译文<textarea id="sentenceDraft" rows="5" placeholder="在这里写下你的翻译或分析，草稿会自动保存…">' + esc(item.draft || '') + '</textarea></label>' +
            (practiceRevealed ? '<div class="practice-answer"><h3>参考译文</h3><p class="precision-translation">' + esc(item.reference || translation || '所选内容暂时无法翻译，可在下方补充参考译文。') + '</p><details><summary>补充或修改参考译文</summary><textarea id="sentenceReference" rows="3">' + esc(item.reference || '') + '</textarea><button id="saveSentenceReference">保存参考译文</button></details>' + segments.map(s => '<h3>选区结构</h3>' + structureHtml(s)).join('') + '</div><div class="practice-ratings"><button data-rating="again">还没理解 · 再练</button><button data-rating="hard">基本理解 · 明天复习</button><button data-rating="good" class="precision-primary">理解了 · 延后复习</button></div>' : '<button id="revealSentenceAnswer" class="precision-primary practice-reveal">对照译文与结构</button>');
        $('#sentenceDraft', body).oninput = e => persistItem(item, { draft: e.target.value });
        const reveal = $('#revealSentenceAnswer', body);
        if (reveal) reveal.onclick = async () => { reveal.disabled = true; reveal.textContent = '正在翻译所选内容…'; await fillSelectionTranslation(item); if (item.selectionTranslation) persistItem(item, { selectionTranslation: item.selectionTranslation }); practiceRevealed = true; renderPractice(); };
        const saveReference = $('#saveSentenceReference', body);
        if (saveReference) saveReference.onclick = () => { persistItem(item, { reference: $('#sentenceReference', body).value.trim() }); toast('参考译文已保存'); renderPractice(); };
        $$('[data-rating]', body).forEach(b => b.onclick = () => {
            const rating = b.dataset.rating; const level = rating === 'good' ? Math.min((item.level || 0) + 1, 5) : 0;
            const days = rating === 'again' ? 0 : rating === 'hard' ? 1 : [1, 3, 7, 14, 30, 60][level];
            persistItem(item, { reviews: (item.reviews || 0) + 1, level, nextReviewAt: Date.now() + days * 86400000, lastPracticedAt: Date.now() });
            if (rating === 'again') practiceQueue.push(item.id);
            practiceIndex++; practiceRevealed = false; renderPractice();
        });
    }

    function studyEntry(word) {
        const key = wordKey(word), item = window.EnglishApp && window.EnglishApp.state().words[key];
        const corrected = item && reviewedText(item.sentence || '', item.source);
        const record = { en: item && item.sentence || '', zh: corrected ? corrected.zh : item && item.translation || '', tokens: [], source: item && item.source || {} };
        const found = meanings.lookup({ word: item && item.word || word, kind: item && item.kind || 'word', record, token: item && item.contextToken });
        const values = [];
        const customKey = item && item.contextToken && Number.isFinite(item.contextToken.a) ? contextKey(record, item.contextToken.a, item.word || word) : '';
        const custom = found.quality === 'manual' ? found.meaning : customKey && overrides[customKey] || item && item.meaningQuality === 'manual' && item.meaning;
        if (custom) values.push({ p: '本文', t: custom });
        else if (found.meaning) values.push({ p: found.quality === 'reviewed' ? '本文' : found.quality === 'grammar' ? '语法' : found.quality === 'name' ? '名称' : '词典', t: found.meaning });
        for (const sense of found.common) if (!values.some(value => value.t === sense.m)) values.push({ p: sense.p, t: sense.m });
        return values.length ? { ph: found.ph, s: values.slice(0, 3) } : null;
    }
    function exportData() { return { version: 1, sentences: saved, overrides, mode: enabled }; }
    function importData(data) {
        if (Array.isArray(data.sentences)) { saved = data.sentences.filter(s => s && typeof s.text === 'string' && typeof s.id === 'string' && Array.isArray(s.segments)); write(KEYS.sentences, saved); }
        if (data.overrides && typeof data.overrides === 'object' && !Array.isArray(data.overrides)) { overrides = data.overrides; write(KEYS.overrides, overrides); }
        if (typeof data.mode === 'boolean') { enabled = data.mode; write(KEYS.mode, enabled); }
        updateBookCount();
    }

    function init() {
        const root = $('#examContent'); if (!root) return;
        trackHeaderHeight();
        $('#precisionModeBtn').onclick = () => { enabled = !enabled; write(KEYS.mode, enabled); applyMode(); };
        $('#sentenceBookBtn').onclick = openLibrary;
        root.addEventListener('click', event => {
            const number = event.target.closest('.sentence-no');
            const word = event.target.closest('.precision-word');
            if (!number && !word) return;
            event.stopImmediatePropagation();
            if (!enabled) return;
            if (number) { const record = records.get(number.closest('.precision-sentence').dataset.sentenceId); if (record) openAnalysis(selectionFromRecords([record], record.en)); return; }
            if (captureSelection()) return;
            clearTimeout(clickTimer);
            if (event.detail > 1) return;
            clickTimer = setTimeout(() => showWord(word), 300);
        }, true);
        root.addEventListener('dblclick', event => {
            const word = event.target.closest('.precision-word'); if (!word) return;
            event.stopImmediatePropagation(); clearTimeout(clickTimer);
            if (!enabled) return;
            event.preventDefault(); hideFloating();
            const info = wordInfo(word); collectInfo(info);
            const selection = window.getSelection(); if (selection) selection.removeAllRanges();
        }, true);
        root.addEventListener('mouseover', event => { if (event.target.closest('.precision-word')) event.stopImmediatePropagation(); }, true);
        root.addEventListener('contextmenu', event => {
            if (!enabled) return;
            const payload = captureSelection() || selected;
            if (!payload) return;
            event.preventDefault(); event.stopImmediatePropagation();
            payload.rect = { left: event.clientX, bottom: event.clientY };
            showSelectionToolbar(payload, true);
        }, true);
        root.addEventListener('keydown', event => {
            const word = event.target.closest('.precision-word'); if (!word || !enabled) return;
            if (event.key === 'Enter') { event.preventDefault(); showWord(word); }
            if (event.key === ' ' && (event.ctrlKey || event.metaKey)) { event.preventDefault(); collectInfo(wordInfo(word)); }
        });
        root.addEventListener('mouseup', event => {
            if (!enabled || event.button !== 0 || event.detail > 1) return;
            requestAnimationFrame(() => { const payload = captureSelection(); if (payload) { clearTimeout(clickTimer); showSelectionToolbar(payload, false); } else { hideSelection(); selected = null; } });
        });
        document.addEventListener('mousedown', event => {
            if (event.target.closest('.precision-popover,.precision-selection-bar,.precision-context-menu,.precision-overlay')) return;
            hidePopover();
            if (!event.target.closest('#examContent') || !captureSelection()) hideSelection();
        });
        document.addEventListener('keydown', event => {
            if (event.key !== 'Escape') return;
            if ($('.study-overlay.is-open')) return;
            const overlays = $$('.precision-overlay.is-open');
            if (overlays.length) { event.stopImmediatePropagation(); closeOverlay(overlays[overlays.length - 1]); }
            else hideFloating();
        }, true);
        window.addEventListener('scroll', () => { hidePopover(); hideSelection(); }, { passive: true, capture: true });
        applyMode(); updateBookCount();
    }
    window.EnglishPrecision = { onRendered, whenRendered: () => renderJob, studyEntry, exportData, importData, openLibrary };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
