/* Sentence bookmarks and retranslation drafts share the study-record backup. */
(function () {
    'use strict';
    const study = window.EnglishStudy;
    const reading = window.EnglishReading;
    const escape = value => String(value ?? '').replace(/[&<>"']/g, character =>
        ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[character]);
    const sentenceId = /^\d{4}-T[1-4]-P\d+-S\d+$/;
    let currentExam = null;
    let restorePending = false;
    let practice = null;
    let active = null;
    let draftTimer = null;
    let previousFocus = null;
    let loadVersion = 0;
    const record = id => study.getArticleRecord(id).reading || {};
    function update(id, patch) {
        return study.updateArticle(id, { reading: patch });
    }
    function articleId(meta) { return meta.exam + '|' + meta.articleKey; }
    function metaFor(id) { return reading.stats.items.find(meta => articleId(meta) === id); }
    function positionLabel(id) {
        const parts = /-P(\d+)-S(\d+)$/.exec(id || '');
        return parts ? '第' + parts[1] + '段第' + parts[2] + '句' : '';
    }
    function examChanged(exam) {
        if (currentExam !== exam.exam_id) restorePending = true;
        currentExam = exam.exam_id;
        if (active && active.meta.exam !== currentExam) closePractice();
    }
    function markPosition(item) {
        const id = articleId(item.article);
        const position = { id: item.id, en: item.en, sourceHash: item.sourceHash, savedAt: Date.now() };
        if (update(id, { position })) {
            decorate();
            window.EnglishApp.toast('已记住，翻到' + positionLabel(item.id), 'success');
            return true;
        }
        return false;
    }
    function clearPosition(id) {
        if (update(id, { position: null })) decorate();
    }
    async function locate(id) {
        if (!sentenceId.test(id)) return false;
        const meta = reading.stats.items.find(row => row.id === id.split('-P')[0]);
        if (!meta) return false;
        document.querySelector('.study-overlay [data-study-close]')?.click();
        document.querySelector('.precision-analysis.is-open [data-close]')?.click();
        if (window.EnglishApp.state().activeExamId !== meta.exam) await window.EnglishApp.selectExam(meta.exam);
        else await window.EnglishPrecision.whenRendered();
        const element = document.querySelector('[data-reading-id="' + id + '"]');
        if (!element) return false;
        const sentence = (await reading.load(meta.id)).paragraphs.flatMap(row => row.sentences).find(row => row.id === id);
        if (!sentence) return false;
        // Only scroll to the matching source when restoring a saved bookmark.
        const position = record(articleId(meta)).position;
        if (position?.id === id && (position.en !== sentence.en || position.sourceHash !==
            (await reading.load(meta.id)).source.textSHA256)) {
            window.EnglishApp.toast('原文有更新，请重新标记翻译位置', 'warn');
            return false;
        }
        element.scrollIntoView({ block: 'center', behavior: 'auto' });
        element.classList.add('study-located');
        element.tabIndex = -1;
        element.focus({ preventScroll: true });
        setTimeout(() => element.classList.remove('study-located'), 2000);
        return true;
    }
    function scheduleReview(id) {
        if (!metaFor(id)) return;
        const existing = record(id);
        if (!existing.reviewDueAt) {
            const tomorrow = new Date();
            tomorrow.setDate(tomorrow.getDate() + 1);
            tomorrow.setHours(0, 0, 0, 0);
            update(id, { reviewDueAt: tomorrow.getTime() });
        }
        decorate();
    }
    function decorate() {
        for (const block of document.querySelectorAll('[data-reading-article]')) {
            const meta = reading.stats.items.find(row => row.id === block.dataset.readingArticle);
            const controls = block.querySelector('.study-article-controls');
            if (!meta || !controls) continue;
            const id = articleId(meta), saved = record(id), completed = study.getArticleRecord(id).completedAt;
            let actions = controls.querySelector('.reading-session-actions');
            if (!actions) {
                actions = document.createElement('span');
                actions.className = 'reading-session-actions';
                controls.appendChild(actions);
            }
            actions.innerHTML = (saved.position ? '<button type="button" class="study-note-button" data-reading-resume="' +
                escape(saved.position.id) + '">继续翻译 · ' + positionLabel(saved.position.id) +
                '</button><button type="button" class="study-note-button" data-clear-reading="' + escape(id) +
                '" aria-label="清除翻译位置">清除位置</button>' : '') +
                (completed ? '<button type="button" class="study-note-button" data-reading-practice="' + escape(id) + '">' +
                (saved.reviewDueAt && !saved.reviewCompletedAt && saved.reviewDueAt <= Date.now() ? '待重翻' : '重翻练习') + '</button>' : '');
            for (const sentence of block.querySelectorAll('[data-reading-id]')) {
                sentence.classList.toggle('reading-position-mark', saved.position?.id === sentence.dataset.readingId);
            }
        }
    }
    function rendered(exam) {
        decorate();
        if (!restorePending || exam.exam_id !== currentExam) return;
        restorePending = false;
        if (location.hash) return;
        const candidates = reading.stats.items.filter(meta => meta.exam === exam.exam_id)
            .map(meta => record(articleId(meta)).position).filter(Boolean)
            .sort((a, b) => b.savedAt - a.savedAt);
        if (candidates.length) void locate(candidates[0].id);
    }
    function reviewCard(article) {
        const saved = record(article.id);
        const status = saved.reviewCompletedAt ? '已完成一次重翻' :
            !saved.reviewDueAt || saved.reviewDueAt <= Date.now() ? '待重翻' :
            '安排于 ' + new Date(saved.reviewDueAt).toLocaleDateString('zh-CN');
        return '<article class="study-record-card"><header><strong>' + escape(article.year + ' · ' + article.label) +
            '</strong><span>' + status + '</span></header><button type="button" data-reading-practice="' +
            escape(article.id) + '">开始重翻</button></article>';
    }
    function ensurePractice() {
        if (practice) return;
        practice = document.createElement('dialog');
        practice.className = 'reading-retranslation';
        practice.setAttribute('aria-labelledby', 'retranslationTitle');
        practice.innerHTML = '<header><h2 id="retranslationTitle">重翻练习</h2><button type="button" data-close-practice aria-label="关闭重翻练习">×</button></header><div class="reading-retranslation-body"></div>';
        document.body.appendChild(practice);
        practice.addEventListener('close', () => { flushDraft(); active = null; loadVersion++; previousFocus?.focus({ preventScroll: true }); });
        practice.addEventListener('cancel', event => { if (!flushDraft()) event.preventDefault(); });
        practice.addEventListener('input', event => {
            if (event.target.id !== 'readingRetranslationDraft') return;
            active.draft = event.target.value;
            clearTimeout(draftTimer);
            draftTimer = setTimeout(flushDraft, 400);
        });
        practice.addEventListener('click', event => {
            const button = event.target.closest('button');
            if (!button) return;
            if (button.hasAttribute('data-close-practice')) closePractice();
            if (!active?.sentences?.length) return;
            if (button.hasAttribute('data-reveal-translation')) {
                practice.querySelector('.reading-retranslation-answer').hidden = false;
                button.hidden = true;
            }
            if (button.dataset.practiceMove) {
                if (!flushDraft()) return;
                active.index += Number(button.dataset.practiceMove);
                update(active.id, { reviewIndex: active.index });
                renderPractice();
            }
            if (button.hasAttribute('data-finish-retranslation')) {
                if (!flushDraft() || !update(active.id, { reviewCompletedAt: Date.now(), reviewIndex: 0 })) return;
                window.EnglishApp.toast('已完成本篇重翻，译文草稿已保存', 'success');
                closePractice();
                decorate();
            }
        });
        window.addEventListener('pagehide', flushDraft);
        document.addEventListener('visibilitychange', () => { if (document.hidden) flushDraft(); });
    }
    function flushDraft() {
        clearTimeout(draftTimer);
        if (!active?.sentences?.length) return true;
        const sentence = active.sentences[active.index];
        const draft = active.draft;
        if (record(active.id).drafts?.[sentence.id] === draft) return true;
        const ok = update(active.id, { drafts: { ...record(active.id).drafts, [sentence.id]: draft }, reviewIndex: active.index });
        const status = practice.querySelector('[data-draft-status]');
        if (status) status.textContent = ok ? '草稿已保存' : '草稿未保存，请复制备份后重试';
        return ok;
    }
    function closePractice() {
        if (!practice) return;
        if (!flushDraft()) return;
        practice.close();
    }
    async function startPractice(id) {
        const meta = metaFor(id);
        if (!meta) return;
        ensurePractice();
        if (!flushDraft()) return;
        previousFocus = document.activeElement;
        document.querySelector('.study-overlay [data-study-close]')?.click();
        const ticket = ++loadVersion;
        active = null;
        if (!practice.open) practice.showModal();
        const body = practice.querySelector('.reading-retranslation-body');
        body.textContent = '正在加载原文…';
        try {
            const article = await reading.load(meta.id);
            if (ticket !== loadVersion || !practice.open) return;
            const sentences = article.paragraphs.flatMap(row => row.sentences);
            const index = Math.min(record(id).reviewIndex || 0, sentences.length - 1);
            active = { id, meta, sentences, index, draft: '' };
            renderPractice();
        } catch (_) {
            body.textContent = '原文加载失败，请关闭后重试。';
        }
    }
    function renderPractice() {
        const sentence = reading.current(reading.match({
            en: active.sentences[active.index].en,
            source: { exam: active.meta.exam, readingId: active.sentences[active.index].id }
        }));
        active.draft = record(active.id).drafts?.[sentence.id] || '';
        const last = active.index === active.sentences.length - 1;
        practice.querySelector('#retranslationTitle').textContent = active.meta.id.replace('-T', ' · Text ') + ' · 重翻练习';
        practice.querySelector('.reading-retranslation-body').innerHTML = '<p>' + positionLabel(sentence.id) + ' · ' +
            (active.index + 1) + ' / ' + active.sentences.length + '</p><p class="reading-retranslation-original" lang="en">' +
            escape(sentence.en) + '</p><label for="readingRetranslationDraft">我的翻译（选填）</label><textarea id="readingRetranslationDraft" rows="5">' +
            escape(active.draft) + '</textarea><span data-draft-status role="status">草稿自动保存</span><button type="button" data-reveal-translation>对照译文</button>' +
            '<section class="reading-retranslation-answer" hidden><h3>分块对照</h3>' + sentence.chunks.map(chunk =>
                '<p><span lang="en">' + escape(chunk.en) + '</span><br>' + escape(chunk.zh) + '</p>').join('') +
            '<h3>语序调整</h3><p>' + escape(sentence.reorder) + '</p><h3>完整翻译</h3><p>' + escape(sentence.translation) +
            '</p></section><footer>' + (active.index ? '<button type="button" data-practice-move="-1">上一句</button>' : '') +
            (last ? '<button type="button" data-finish-retranslation>完成本篇重翻</button>' : '<button type="button" data-practice-move="1">下一句</button>') + '</footer>';
    }
    document.addEventListener('click', event => {
        const button = event.target.closest('[data-reading-resume],[data-reading-practice],[data-clear-reading]');
        if (!button) return;
        if (button.dataset.readingResume) void locate(button.dataset.readingResume);
        if (button.dataset.readingPractice) void startPractice(button.dataset.readingPractice);
        if (button.dataset.clearReading) clearPosition(button.dataset.clearReading);
    });
    window.addEventListener('storage', event => {
        if (event.key === 'english2_study_records_v1' || event.key === null) decorate();
    });
    window.EnglishReadingSession = { examChanged, rendered, decorate, markPosition, locate, scheduleReview, reviewCard };
})();
