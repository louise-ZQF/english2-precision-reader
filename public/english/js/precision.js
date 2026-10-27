/* English-II precision reading: desktop interactions, phrases, and sentence study. */
(function () {
    'use strict';
    const KEYS = { mode: 'english2_precision_mode_v1', sentences: 'english2_sentences_v1', overrides: 'english2_context_overrides_v1' };
    const $ = (s, root = document) => root.querySelector(s);
    const $$ = (s, root = document) => Array.from(root.querySelectorAll(s));
    const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    const norm = s => String(s || '').replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, ' ').trim();
    const wordKey = s => norm(s).toLowerCase().replace(/[\u2010\u2011]/g, '-').replace(/[^a-z'\s-]/g, '').trim();
    function read(key, fallback) { try { const v = JSON.parse(localStorage.getItem(key)); return v == null ? fallback : v; } catch (_) { return fallback; } }
    function write(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch (_) { toast('保存失败，请先导出数据腾出空间', 'error'); return false; } }
    function toast(s, type) { if (window.EnglishApp) window.EnglishApp.toast(s, type || 'success'); }
    let enabled = read(KEYS.mode, false) === true;
    let saved = read(KEYS.sentences, []);
    if (!Array.isArray(saved)) saved = [];
    let overrides = read(KEYS.overrides, {});
    let lexicon = { phrases: {}, words: {} };
    let phrasePatterns = [];
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
    const lexiconReady = fetch('data/precision/lexicon.json?v=1').then(r => { if (!r.ok) throw new Error(); return r.json(); }).then(data => {
        lexicon = data;
        phrasePatterns = Object.keys(data.phrases).map(key => ({ key, parts: key.split(' ') })).sort((a, b) => b.parts.length - a.parts.length);
    }).catch(() => { toast('精翻词库加载失败，请刷新重试', 'error'); });

    function fallbackSentences(text) {
        const segmenter = new Intl.Segmenter('en', { granularity: 'sentence' });
        return Array.from(segmenter.segment(text), item => {
            const lead = item.segment.match(/^\s*/)[0].length;
            const en = item.segment.trim();
            const tokens = Array.from(en.matchAll(/[A-Za-z][A-Za-z'-]*/g), m => ({ a: m.index, b: m.index + m[0].length, w: m[0], l: m[0].toLowerCase(), m: '', q: 'missing', g: 1 }));
            return { a: item.index + lead, b: item.index + lead + en.length, en, zh: '', tokens, groups: [], core: [] };
        }).filter(x => x.en);
    }

    function phraseMatches(sentence) {
        const tokens = sentence.tokens.filter(t => /[A-Za-z]/.test(t.w));
        const matches = [];
        const used = new Set();
        const equal = (token, part) => token && (wordKey(token.w) === part || token.l === part);
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
        const separable = ['take into account', 'take for granted', 'keep in mind', 'put off', 'point out', 'carry out', 'hold back', 'bring about', 'set up', 'turn down', 'take over', 'give up', 'cut off'];
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
        const words = Array.from(sentence.en.matchAll(/[A-Za-z]+(?:['\u2018\u2019][A-Za-z]+)*(?:[-\u2010\u2011][A-Za-z]+(?:['\u2018\u2019][A-Za-z]+)*)*/g), m => ({ a: m.index, b: m.index + m[0].length, key: m[0], kind: 'word' }));
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
        return '<span class="precision-sentence" data-sentence-id="' + id + '"><button class="sentence-no" type="button" data-no="' + number + '" aria-label="翻译和分析第' + number + '句"' + (enabled ? '' : ' disabled') + '></button><span class="sentence-body">' + text + '</span></span>';
    }

    async function onRendered(exam) {
        currentExam = exam;
        const sequence = ++renderSequence;
        hideFloating();
        renderJob = (async () => {
            await lexiconReady;
            let data = dataCache.get(exam.exam_id);
            if (!data) {
                try { const r = await fetch('data/precision/' + encodeURIComponent(exam.exam_id) + '.json?v=1'); if (!r.ok) throw new Error(); data = await r.json(); dataCache.set(exam.exam_id, data); }
                catch (_) { data = { blocks: {} }; toast('句法资料暂未加载，仍可阅读和收藏', 'warn'); }
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
            const prefix = Array.from(node.children).filter(x => x.matches('.question-num,.option-letter,.choice-letter')).map(x => x.outerHTML).join('');
            node.classList.toggle('precision-paragraph', isParagraph);
            node.classList.toggle('precision-compact', !isParagraph);
            node.dataset.blockKey = raw;
            node.innerHTML = prefix + sentences.map((sentence, i) => {
                const id = exam.exam_id + '-' + blockIndex + '-' + i;
                records.set(id, { id, ...sentence, source: { exam: exam.exam_id, year: exam.year, article: [section, article].filter(Boolean).join(' / '), paragraph, sentence: i + 1, block: raw } });
                return sentenceHtml(sentence, id, i + 1);
            }).join(' ');
        });
        applyMode();
        markSavedSentences();
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
        const hint = enabled ? '精翻中：单击查义 · 双击收藏词语 · 点句子编号翻译和拆解 · 划选后右键收藏长难句' : '普通阅读：点击右上角「进入精翻」开启查词、词组学习和长难句收藏';
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
    function phraseSense(key, record) {
        const meaning = lexicon.phrases[key] || '';
        if (key === 'account for' && /\d|percent|quarter|third|half/.test(record.en)) return { meaning:'占……比例', quality:'phrase' };
        if (key === 'take up' && /time|space|room/.test(record.en)) return { meaning:'占用（时间或空间）', quality:'phrase' };
        const parts = meaning.split('；');
        const matched = parts.filter(p => {
            const main = p.replace(/（.*?）|的$|地$/g,'').replace(/……/g,'').trim();
            return main.length > 1 && record.zh.includes(main);
        });
        return { meaning:matched.length ? matched.join('；') : meaning, quality:matched.length || parts.length===1 ? 'phrase' : 'candidate' };
    }
    function wordInfo(element) {
        const record = records.get(element.closest('.precision-sentence').dataset.sentenceId);
        if (!record) return null;
        const word = element.dataset.word, start = Number(element.dataset.start);
        const token = record.tokens.find(t => t.a === start) || record.tokens.find(t => t.a <= start && t.b > start);
        const isPhrase = element.dataset.kind === 'phrase';
        const wholeWord = !isPhrase && (/[-\u2010\u2011]/.test(word) || token && Number(element.dataset.end) > token.b && wordKey(word) !== wordKey(token.w));
        const phrase = isPhrase ? phraseSense(wordKey(word), record) : null;
        const overrideKey = contextKey(record, start, word);
        const override = overrides[overrideKey];
        const lemma = isPhrase || wholeWord ? wordKey(word) : (token && token.l) || wordKey(word);
        const entry = wholeWord && lexicon.words[lemma];
        const wholeMeaning = entry && entry.common && entry.common[0] && entry.common[0].m || '';
        return { word, kind: isPhrase ? 'phrase' : 'word', wholeWord, record, token, key: overrideKey, lemma, meaning: override || (phrase ? phrase.meaning : wholeWord ? wholeMeaning : token && token.m) || '', quality: override ? 'manual' : phrase ? phrase.quality : wholeWord ? wholeMeaning ? 'candidate' : 'missing' : token && token.q || 'missing', element };
    }

    async function completeWholeWord(info) {
        if (!info.wholeWord || info.meaning) return;
        try {
            const entry = await window.EnglishApp.lookup(info.word);
            if (entry && !entry._partial && entry.s && entry.s.length) { info.meaning = entry.s[0].t; info.quality = 'candidate'; return; }
            const payload = { text: info.word, segments: [] };
            const zh = await fillSelectionTranslation(payload);
            if (zh) { info.meaning = zh; info.quality = 'machine'; }
        } catch (_) {}
    }
    function meaningLabel(info) { return info.quality === 'machine' ? '完整词译义 · 在线翻译' : info.quality === 'candidate' ? '本句候选义 · 待确认' : info.quality === 'missing' ? '本句语境义 · 待补充' : info.quality === 'phrase' ? '本句词组义' : '本句语境义'; }
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
    async function showWord(element) {
        if (!enabled) return;
        const info = wordInfo(element); if (!info) return;
        const request = ++lookupSequence;
        await completeWholeWord(info);
        if (request !== lookupSequence) return;
        let common = lexicon.words[info.lemma];
        if (!info.meaning && !common && window.EnglishApp) {
            const entry = await window.EnglishApp.lookup(info.word);
            if (request !== lookupSequence) return;
            const senses = (entry && (!info.wholeWord || !entry._partial) && entry.s || []).filter(s => /^(n|v|vt|vi|a|adj|ad|adv|prep|conj|pron)$/.test(s.p));
            common = { ph: entry && entry.ph || '', common: senses.slice(0, 2).map(s => ({ m: s.t.split(/[,，;；]/).slice(0, 2).join('；'), p: s.p, count: 0 })) };
        }
        const box = ensurePopover();
        const others = (common && common.common || []).filter(s => s.m !== info.meaning).slice(0, 2);
        box.innerHTML = '<div class="precision-pop-head"><div><strong>' + esc(info.word) + '</strong><span>' + (info.kind === 'phrase' ? '词组' : esc(common && common.ph || '')) + '</span></div><button data-action="close" class="precision-icon-close" aria-label="关闭释义">×</button></div>' +
            '<div class="precision-current"><label>' + meaningLabel(info) + '</label><p>' + esc(info.meaning || '当前语境尚无可靠释义，可以手动补充。') + '</p></div>' +
            (others.length ? '<div class="precision-common"><label>英语二其他用法</label>' + others.map(s => '<p>' + esc(s.m) + (s.count ? '<small>英语二语境匹配 ' + s.count + ' 句</small>' : '<small>常用义参考</small>') + '</p>').join('') + '</div>' : '') +
            '<div class="precision-example"><p>' + esc(info.record.en) + '</p><p class="precision-zh">' + esc(info.record.zh || '点「整句翻译与结构」查看句库匹配结果') + '</p></div>' +
            '<div class="precision-pop-actions"><button data-action="collect">收藏' + (info.kind === 'phrase' ? '整个词组' : '单词') + '</button><button data-action="sentence">整句翻译与结构</button><button data-action="edit">改本句释义</button></div>';
        box.onclick = async event => {
            const button = event.target.closest('[data-action]'); if (!button) return;
            if (button.dataset.action === 'close') hidePopover();
            if (button.dataset.action === 'collect') collectInfo(info);
            if (button.dataset.action === 'sentence') openAnalysis(selectionFromRecords([info.record], info.record.en));
            if (button.dataset.action === 'edit') {
                const current = $('.precision-current', box);
                current.innerHTML = '<label for="contextMeaningInput">本句语境义</label><input id="contextMeaningInput" value="' + esc(info.meaning) + '" placeholder="输入这个词在本句中的意思"><button type="button" id="saveContextMeaning">保存本句释义</button>';
                $('#contextMeaningInput', box).focus();
                $('#saveContextMeaning', box).onclick = () => {
                    const value = $('#contextMeaningInput', box).value.trim(); if (!value) return;
                    const next = { ...overrides, [info.key]: value };
                    if (!write(KEYS.overrides, next)) return;
                    overrides = next; toast('已保存这处语境义'); showWord(element);
                };
            }
        };
        position(box, element);
    }
    function collectInfo(info) {
        if (!info) return;
        const details = () => ({ kind: info.kind, lemma: info.lemma, meaning: info.meaning, meaningQuality: info.quality, sentence: info.record.en, translation: info.record.zh, source: info.record.source });
        window.EnglishApp.collect(info.word, details());
        if (info.wholeWord && !info.meaning) completeWholeWord(info).then(() => {
            const savedWord = window.EnglishApp.state().words[wordKey(info.word)];
            if (info.meaning && savedWord && !savedWord.meaning && savedWord.sentence === info.record.en) window.EnglishApp.collect(info.word, details(), { silent: true });
        });
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
        box.innerHTML = '<button data-action="translate">翻译与结构</button><button data-action="save">收藏到长难句</button><button data-action="phrase">收藏为词组</button>';
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
        const known = lexicon.phrases[wordKey(value)] || '';
        window.EnglishApp.collect(value, { kind: 'phrase', lemma: wordKey(value), meaning: known, meaningQuality: known ? 'phrase' : 'missing', sentence: payload.context, translation: payload.selectionTranslation && payload.selectionTranslation.en === value ? payload.selectionTranslation.zh : '', source: payload.source });
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
            const focusable = $$('button:not([disabled]),input,textarea,a[href]', overlay).filter(x => x.offsetParent !== null);
            if (!focusable.length) return;
            if (e.shiftKey && document.activeElement === focusable[0]) { e.preventDefault(); focusable[focusable.length - 1].focus(); }
            else if (!e.shiftKey && document.activeElement === focusable[focusable.length - 1]) { e.preventDefault(); focusable[0].focus(); }
        });
        return overlay;
    }
    function showOverlay(overlay) { previousFocus = document.activeElement; overlay.hidden = false; overlay.classList.add('is-open'); document.body.classList.add('precision-modal-open'); $('[data-close]', overlay).focus(); }
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
        const local = await window.EnglishApp.translate(text);
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
        if (payload.selectionTranslation && payload.selectionTranslation.en === text && payload.selectionTranslation.zh) return payload.selectionTranslation.zh;
        const segments = selectionSegments(payload);
        let zh = segments.every(s => s.zh) ? segments.map(s => s.zh).join('\n\n') : '';
        if (!zh) {
            if (!translationCache.has(text)) translationCache.set(text, translateExactText(text).catch(() => { translationCache.delete(text); return ''; }));
            zh = await translationCache.get(text);
        }
        if (zh) payload.selectionTranslation = { en: text, zh };
        return zh;
    }
    function sourceLabel(source) { return source ? source.year + ' 英语二 · ' + source.article + (source.paragraph ? ' · 第' + source.paragraph + '段' : '') + ' 第' + source.sentence + '句' : '自选长难句'; }
    function closeAnalysis() { if (analysis) closeOverlay(analysis); }
    async function openAnalysis(payload) {
        hideFloating();
        if (!analysis) analysis = makeOverlay('precision-analysis', '句子精翻');
        const body = $('.precision-modal-body', analysis);
        const segments = selectionSegments(payload);
        body.innerHTML = '<p class="precision-source">' + esc(sourceLabel(payload.source)) + '</p>' +
            '<div class="precision-selected"><label>你选中的内容</label><p>' + esc(payload.text) + '</p></div>' +
            '<div class="precision-analysis-actions"><button id="saveAnalyzedSentence" class="precision-primary">收藏到长难句</button></div>' +
            '<section class="precision-analysis-segment"><h3>选区译文</h3><p class="precision-translation" data-selection-translation>正在翻译所选内容…</p><h3>选区结构</h3>' + segments.map(structureHtml).join('') + '</section>';
        $('#saveAnalyzedSentence', body).onclick = () => saveSentence(payload);
        const translation = $('[data-selection-translation]', body);
        showOverlay(analysis);
        const zh = await fillSelectionTranslation(payload);
        if (translation.isConnected) translation.textContent = zh || '所选内容暂时无法翻译，请稍后重试。';
        const item = saved.find(s => s.id === hash((payload.source && payload.source.exam || '') + '|' + payload.text.trim()));
        if (item && payload.selectionTranslation) persistItem(item, { selectionTranslation: payload.selectionTranslation });
    }

    function saveSentence(payload) {
        const text = payload.text.trim(); if (!text) return;
        const id = hash((payload.source && payload.source.exam || '') + '|' + text);
        if (saved.some(s => s.id === id)) { toast('这条长难句已经收藏'); return; }
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
    function updateBookCount() { const count = $('#sentenceBookCount'); if (count) count.textContent = saved.length; markSavedSentences(); }
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
        const key = wordKey(word); const item = window.EnglishApp && window.EnglishApp.state().words[key];
        const entry = lexicon.words[item && item.lemma || key]; const phrase = lexicon.phrases[key];
        const meanings = [];
        if (item && item.meaning) meanings.push({ p: item.meaningQuality === 'candidate' ? '候选' : item.meaningQuality === 'machine' ? '整词' : item.kind === 'phrase' ? '词组' : '本句', t: item.meaning });
        else if (phrase) meanings.push({ p: '词组', t: phrase });
        if (entry) for (const s of entry.common) if (!meanings.some(m => m.t === s.m)) meanings.push({ p: s.p, t: s.m });
        return meanings.length ? { ph: entry && entry.ph || '', s: meanings.slice(0, 3) } : null;
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
