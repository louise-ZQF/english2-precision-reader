/* Source-marked reading vocabulary, with the same click gestures as precision mode. */
(function () {
    'use strict';
    const entry = document.getElementById('readingKeywordsBtn');
    if (!entry) return;
    const sources = window.EnglishReadingKeywords || {};
    const reading = window.EnglishReading;
    const years = [...new Set(Object.keys(sources).map(id => id.slice(0, 4)))].sort().reverse();
    const standaloneFunction = new Set(['art', 'prep', 'pron', 'det', 'aux', 'inf', 'num', 'name']);
    const panel = document.createElement('dialog');
    panel.className = 'reading-keywords';
    panel.setAttribute('aria-labelledby', 'readingKeywordTitle');
    panel.innerHTML = '<header class="reading-keywords-head"><div><span class="precision-eyebrow">ENGLISH II · 阅读词汇</span><h2 id="readingKeywordTitle">重点单词</h2></div><form method="dialog"><button class="precision-icon-close" aria-label="关闭重点单词">×</button></form></header>' +
        '<div class="reading-keywords-controls"><label>年份 <select aria-label="年份"></select></label><nav aria-label="选择阅读文章"></nav></div>' +
        '<p class="reading-keywords-help">收录本地资料标出的单词和固定搭配。单击看本文义，双击收藏。</p>' +
        '<p class="reading-keywords-status" role="status"></p><ul class="reading-keywords-list" aria-label="重点单词列表"></ul>';
    document.body.appendChild(panel);
    const yearSelect = panel.querySelector('select'), textNav = panel.querySelector('nav');
    const list = panel.querySelector('ul'), status = panel.querySelector('[role=status]');
    const app = () => window.EnglishApp;
    for (const year of years) yearSelect.add(new Option(year, year));
    let currentText = 1, lastView = null, request = 0, clickTimer;
    for (let text = 1; text <= 4; text++) {
        const button = document.createElement('button');
        button.type = 'button'; button.textContent = 'Text ' + text;
        button.dataset.text = text;
        button.onclick = () => { currentText = text; render(); };
        textNav.appendChild(button);
    }
    function saved(word) { return Object.hasOwn(app().state().words, app().normalizeWord(word)); }
    function card(row, sentence, article) {
        const li = document.createElement('li'), button = document.createElement('button'), word = document.createElement('span'), label = document.createElement('span'), meaning = document.createElement('div');
        const source = { exam: article.exam, year: article.id.slice(0, 4), article: 'Section II Reading Comprehension / Text ' + article.text,
            readingArticleId: article.id, readingId: sentence.id, paragraph: Number(sentence.id.match(/-P(\d+)/)[1]), sentence: Number(sentence.id.match(/-S(\d+)/)[1]) };
        const record = { en: sentence.en, source };
        const details = () => reading.lookup(record, row.a, row.b, row.kind) || row;
        button.type = 'button'; button.className = 'reading-keywords-word'; button.setAttribute('aria-expanded', 'false');
        word.textContent = row.word; word.lang = 'en'; label.className = 'reading-keywords-saved';
        meaning.className = 'reading-keywords-meaning'; meaning.hidden = true; meaning.setAttribute('aria-live', 'polite');
        const markSaved = () => { label.textContent = saved(row.word) ? '已收藏' : ''; };
        const reveal = () => {
            meaning.hidden = !meaning.hidden;
            if (!meaning.hidden) meaning.textContent = '本文义：' + details().meaning;
            button.setAttribute('aria-expanded', String(!meaning.hidden));
        };
        const collect = () => {
            clearTimeout(clickTimer);
            if (saved(row.word)) { app().toast('已在生词本：' + row.word, 'success'); markSaved(); return; }
            const info = details(), item = reading.current(reading.match(record));
            app().collect(row.word, { kind: row.kind || 'word', lemma: info.lemma, meaning: info.meaning,
                meaningQuality: info.quality || 'reviewed', sentence: sentence.en, translation: item ? item.translation : sentence.translation,
                source, examId: article.exam, contextToken: { a: row.a, b: row.b, w: row.word, p: row.pos } });
            markSaved();
        };
        button.onclick = event => {
            clearTimeout(clickTimer);
            if (!event.detail) reveal(); // Keyboard activation does not participate in double-click.
            else if (event.detail === 1) clickTimer = setTimeout(reveal, 300);
        };
        button.ondblclick = event => { event.preventDefault(); collect(); };
        button.onkeydown = event => {
            if (event.code === 'Space' && (event.ctrlKey || event.metaKey)) { event.preventDefault(); collect(); }
        };
        markSaved(); button.append(word, label); li.append(button, meaning); return li;
    }
    function priorityEntries(article, marks) {
        const sentences = new Map(article.paragraphs.flatMap(p => p.sentences).map(s => [s.id, s]));
        const unique = new Set(), entries = [];
        for (const [id, start] of marks) {
            const sentence = sentences.get(id);
            if (!sentence) continue;
            const token = sentence.words.find(w => w.a === start);
            if (!token) continue;
            const phrase = sentence.phrases.find(p => p.kind === 'phrase' && !p.structure && p.a <= token.a && p.b >= token.b
                && (p.b - p.a > token.b - token.a));
            if (!phrase && (standaloneFunction.has(token.pos) || !app().normalizeWord(token.word))) continue;
            const row = phrase || token, key = (row.lemma || row.word).toLowerCase() + '\0' + row.meaning;
            if (unique.has(key)) continue;
            unique.add(key); entries.push([row, sentence]);
        }
        return entries;
    }
    async function render() {
        clearTimeout(clickTimer);
        const ticket = ++request, id = yearSelect.value + '-T' + currentText, marks = sources[id];
        list.replaceChildren(); list.scrollTop = 0;
        for (const button of textNav.children) button.setAttribute('aria-pressed', String(Number(button.dataset.text) === currentText));
        if (!marks || !marks.length) {
            status.textContent = marks ? '这篇暂未提取到资料标出的重点单词。' : '这篇不在这套资料的覆盖范围内。';
            return;
        }
        status.textContent = '正在加载重点单词…';
        try {
            const article = await reading.load(id);
            if (ticket !== request || !panel.open) return;
            const entries = priorityEntries(article, marks);
            list.append(...entries.map(([row, sentence]) => card(row, sentence, article)));
            status.textContent = entries.length ? '共 ' + entries.length + ' 项' + (id === '2022-T1' ? ' · 从该篇的逐词标注中选出' : '') : '这篇暂未提取到资料标出的重点单词。';
        } catch (_) {
            if (ticket === request) status.textContent = '重点单词未能加载，切换文章可重试。';
        }
    }
    yearSelect.onchange = () => { currentText = 1; render(); };
    entry.onclick = () => {
        const exam = app().state().activeExamId;
        if (!lastView || lastView.exam !== exam) {
            const year = String(exam || '').slice(0, 4);
            yearSelect.value = years.includes(year) ? year : years[0];
            currentText = 1;
        }
        lastView = { exam };
        panel.showModal(); render();
    };
    panel.addEventListener('close', () => { clearTimeout(clickTimer); request++; });
})();
