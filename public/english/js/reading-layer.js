/* Numbered reading sources, pre-edited sentence content and portable corrections. */
(function () {
    'use strict';
    const KEY = 'english2_reading_edits_v1', MODE = 'english2_reading_only_v1';
    const manifest = window.EnglishReadingManifest || { items: [] }, loading = new Map();
    const articles = new Map(), sentences = new Map(), byText = new Map();
    const clean = value => String(value || '').replace(/[‘’]/g, "'").replace(/\s+/g, ' ').trim();
    const sentenceKey = (exam, en) => exam + '|' + clean(en);
    let edits;
    try { edits = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (_) { edits = {}; }
    if (typeof edits !== 'object' || Array.isArray(edits)) edits = {};
    const notify = (text, type) => window.EnglishApp && window.EnglishApp.toast(text, type || 'success');
    function persist(next) {
        try { localStorage.setItem(KEY, JSON.stringify(next)); edits = next; return true; }
        catch (_) { notify('纠错保存失败，请先导出备份并释放浏览器存储空间', 'error'); return false; }
    }
    function register(article) {
        if (articles.has(article.id)) return;
        articles.set(article.id, article);
        for (const paragraph of article.paragraphs) for (const item of paragraph.sentences) {
            const sentence = { ...item, article, paragraph: paragraph.id, sourceHash: article.source.textSHA256 };
            sentences.set(item.id, sentence);
            const key = sentenceKey(article.exam, item.en);
            if (!byText.has(key)) byText.set(key, []);
            byText.get(key).push(sentence);
        }
    }
    function load(id) {
        if (articles.has(id)) return Promise.resolve(articles.get(id));
        if (loading.has(id)) return loading.get(id);
        const meta = manifest.items.find(item => item.id === id);
        if (!meta) return Promise.reject(new Error('未知阅读文章：' + id));
        const promise = new Promise((resolve, reject) => {
            const existing = window.EnglishReadingFiles && window.EnglishReadingFiles[id];
            if (existing) { register(existing); resolve(existing); return; }
            const script = document.createElement('script');
            script.src = 'data/reading-browser/' + id + '.js?v=' + meta.revision;
            script.onload = () => {
                const value = window.EnglishReadingFiles && window.EnglishReadingFiles[id];
                if (!value) { reject(new Error('阅读资料未载入')); return; }
                register(value); resolve(value);
            };
            script.onerror = () => { loading.delete(id); reject(new Error('阅读资料未载入')); };
            document.head.appendChild(script);
        });
        loading.set(id, promise); return promise;
    }
    async function ready(exam) {
        const result = await Promise.allSettled(manifest.items.filter(item => item.exam === exam).map(item => load(item.id)));
        if (result.some(item => item.status === 'rejected')) notify('部分阅读资料未载入，未载入的句子会标为尚未整理', 'warn');
    }
    async function prepareWords(words) {
        const ids = new Set();
        for (const word of words) {
            if (!word || typeof word !== 'object') continue;
            const source = word.source || {}, text = /Text\s*([1-4])\b/i.exec(source.article || '');
            const id = source.readingArticleId || (source.readingId && source.readingId.replace(/-P\d+-S\d+$/, '')) || (text && String(source.exam || '').slice(0, 4) + '-T' + text[1]);
            if (id && manifest.items.some(a => a.id === id)) ids.add(id);
        }
        await Promise.allSettled([...ids].map(load));
    }
    function match(record) {
        if (!record) return null;
        const source = record.source || {};
        const direct = source.readingId && sentences.get(source.readingId);
        if (direct && clean(record.en) === direct.en) return direct;
        const list = byText.get(sentenceKey(source.exam, record.en)) || [];
        if (source.readingArticleId) return list.find(s => s.article.id === source.readingArticleId) || null;
        const title = /Text\s*(\d)/i.exec(source.article || '');
        return title ? list.find(s => s.article.text === Number(title[1])) || null : list.length === 1 ? list[0] : null;
    }
    function paragraph(exam, key, en) {
        const meta = manifest.items.find(a => a.exam === exam && a.articleKey === key);
        const article = meta && articles.get(meta.id);
        return article && article.paragraphs.find(p => p.en === clean(en)) || null;
    }
    function scope(record) {
        const source = record && record.source || {};
        return !!(source.readingId || source.readingArticleId || /(?:^|\/)\s*Text\s*[1-4]\b/i.test(source.article || ''));
    }
    function current(sentence) {
        if (!sentence) return null;
        const edit = edits[sentence.id];
        const safe = edit && edit.en === sentence.en && edit.sourceHash === sentence.sourceHash ? edit : {};
        const chunks = sentence.chunks.map(chunk => {
            const changed = (safe.chunks || []).find(row => row.a === chunk.a && row.b === chunk.b);
            return changed ? { ...chunk, zh: changed.zh } : chunk;
        });
        return { ...sentence, ...safe, chunks, custom: !!Object.keys(safe).length || !!sentence.lastCorrectionAt, manualTranslation: typeof safe.translation === 'string' || sentence.translationStatus === 'corrected' };
    }
    function lookup(record, a, b, kind) {
        const sentence = match(record); if (!sentence) return null;
        const edit = edits[sentence.id];
        const custom = edit && edit.en === sentence.en && edit.sourceHash === sentence.sourceHash && (edit.words || []).find(word => word.a === a && word.b === b);
        if (custom) return { ...custom, quality: 'manual' };
        if (sentence.article.source.status !== 'verified') return null;
        const values = kind === 'phrase' ? [...sentence.phrases, ...sentence.words] : [...sentence.words, ...sentence.phrases];
        return values.find(word => word.a === a && word.b === b && word.quality !== 'dictionary') || null;
    }
    function phrases(record) {
        const sentence = match(record);
        return sentence && sentence.article.source.status === 'verified' ? sentence.phrases : [];
    }
    function setEdit(sentence, patch) {
        const previous = edits[sentence.id];
        const row = previous && previous.en === sentence.en && previous.sourceHash === sentence.sourceHash ? previous : {};
        return persist({ ...edits, [sentence.id]: { ...row, ...patch, en: sentence.en, sourceHash: sentence.sourceHash, updatedAt: Date.now() } });
    }
    function setWord(record, a, b, value) {
        const sentence = match(record); if (!sentence) return false;
        const stored = edits[sentence.id];
        const previous = stored && stored.en === sentence.en && stored.sourceHash === sentence.sourceHash ? stored : {};
        const word = { ...value, a, b, word: sentence.en.slice(a, b) };
        if (!(a >= 0 && b > a && b <= sentence.en.length) || !word.meaning || !word.lemma) return false;
        return setEdit(sentence, { words: (previous.words || []).filter(row => row.a !== a || row.b !== b).concat(word) });
    }
    function exportData() { return { app: 'english2-reading-corrections', version: 1, records: edits }; }
    function downloadCorrections() {
        const url = URL.createObjectURL(new Blob([JSON.stringify(exportData(), null, 2)], { type: 'application/json' }));
        const link = document.createElement('a'); link.href = url; link.download = 'english2-reading-corrections-' + new Date().toISOString().slice(0, 10) + '.json';
        document.body.appendChild(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 800);
        notify('已导出阅读纠错记录，可从“数据”导入，或合并回网站');
    }
    async function importData(payload) {
        if (!payload || payload.app !== 'english2-reading-corrections' || payload.version !== 1 || !payload.records || typeof payload.records !== 'object') throw new Error('阅读纠错文件格式不正确');
        const next = { ...edits }; let count = 0;
        for (const [id, value] of Object.entries(payload.records)) {
            if (!/^\d{4}-T[1-4]-P\d+-S\d+$/.test(id) || !value || typeof value !== 'object') throw new Error('阅读句子编号不正确');
            await load(id.replace(/-P\d+-S\d+$/, ''));
            const sentence = sentences.get(id);
            if (!sentence || value.en !== sentence.en || value.sourceHash !== sentence.sourceHash) throw new Error(id + ' 的原文已变化，请人工核对后再导入');
            const row = { en: sentence.en, sourceHash: sentence.sourceHash, updatedAt: Number(value.updatedAt) || Date.now() };
            for (const field of ['translation', 'reorder']) if (typeof value[field] === 'string') row[field] = value[field];
            if (Array.isArray(value.chunks)) {
                if (value.chunks.length !== sentence.chunks.length || value.chunks.some((c, i) => c.a !== sentence.chunks[i].a || c.b !== sentence.chunks[i].b || typeof c.zh !== 'string')) throw new Error(id + ' 的分块位置不一致');
                row.chunks = value.chunks.map(c => ({ a: c.a, b: c.b, zh: c.zh }));
            }
            if (Array.isArray(value.words)) {
                if (value.words.some(w => !Number.isInteger(w.a) || !Number.isInteger(w.b) || w.a < 0 || w.b <= w.a || w.b > sentence.en.length || sentence.en.slice(w.a, w.b) !== w.word || typeof w.lemma !== 'string' || typeof w.meaning !== 'string')) throw new Error(id + ' 的词义位置不一致');
                row.words = value.words.map(w => ({ a: w.a, b: w.b, word: w.word, lemma: w.lemma, meaning: w.meaning, kind: w.kind === 'phrase' ? 'phrase' : 'word', explanation: typeof w.explanation === 'string' ? w.explanation : '' }));
            }
            if (!next[id] || row.updatedAt >= (next[id].updatedAt || 0)) { next[id] = row; count++; }
        }
        if (!persist(next)) throw new Error('阅读纠错保存失败');
        return count;
    }
    function decorate() {
        for (const node of document.querySelectorAll('[data-reading-article]')) {
            const meta = manifest.items.find(a => a.id === node.dataset.readingArticle);
            if (!meta) continue;
            let badge = node.querySelector('.reading-review-status');
            if (!badge) { badge = document.createElement('p'); badge.className = 'reading-review-status'; node.querySelector('.study-article-heading').after(badge); }
            badge.textContent = (meta.source === 'verified' ? '原文已核对' : '原文待核对') + ' · ' + (meta.reviewed ? meta.reviewed + '/' + meta.sentences + ' 句已整理' : '精翻尚未整理');
        }
    }
    function init() {
        const jumps = document.getElementById('readingJumps'); if (!jumps) return;
        const button = document.createElement('button'); button.type = 'button'; button.id = 'readingOnlyBtn'; button.className = 'reading-only-button';
        let only = false;
        try { only = new URLSearchParams(location.search).get('view') === 'reading' || localStorage.getItem(MODE) === 'true'; } catch (_) {}
        const apply = () => { document.body.classList.toggle('reading-only', only); button.textContent = only ? '返回整卷' : '只看阅读'; button.setAttribute('aria-pressed', String(only)); };
        button.onclick = () => {
            only = !only; try { localStorage.setItem(MODE, JSON.stringify(only)); const url = new URL(location.href); if (only) url.searchParams.set('view', 'reading'); else url.searchParams.delete('view'); history.replaceState(null, '', url); } catch (_) {}
            apply(); if (only) document.querySelector('[data-reading-article]')?.scrollIntoView({ block: 'start' });
        };
        const controls = document.querySelector('.snav-links');
        if (controls) controls.prepend(button); else jumps.before(button);
        apply();
    }
    window.EnglishReading = { ready, prepareWords, match, paragraph, scope, current, lookup, phrases, setEdit, setWord, exportData, importData, downloadCorrections, decorate, stats: manifest };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
