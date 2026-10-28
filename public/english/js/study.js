/* Article translation progress, mistake review and personal notes. */
(function () {
    'use strict';
    const KEY = 'english2_study_records_v1';
    const $ = (s, root = document) => root.querySelector(s);
    const $$ = (s, root = document) => Array.from(root.querySelectorAll(s));
    const esc = value => String(value == null ? '' : value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    const text = value => typeof value === 'string' ? value : '';
    const time = value => Number.isFinite(value) && value > 0 ? value : 0;
    const validId = id => /^[\w-]+_english2\|s\d+-(?:passage|p\d+(?:-t\d+)?)$/.test(id);
    const columns = [['cloze', '完形'], ['text1', 'Text 1'], ['text2', 'Text 2'], ['text3', 'Text 3'], ['text4', 'Text 4'], ['partB', 'Part B'], ['translation', '翻译']];
    function cleanData(data) {
        const result = { version: 1, articles: {}, mistakes: {} };
        if (!data || typeof data !== 'object') return result;
        for (const [id, item] of Object.entries(data.articles || {})) {
            if (!validId(id) || !item || typeof item !== 'object') continue;
            result.articles[id] = { completedAt: time(item.completedAt), note: text(item.note), updatedAt: time(item.updatedAt) };
        }
        for (const item of Object.values(data.mistakes || {})) {
            if (!item || !validId(item.articleId) || !/^\d{1,3}$/.test(String(item.question))) continue;
            const question = String(item.question), id = item.articleId + '|q' + question;
            result.mistakes[id] = { articleId: item.articleId, question, myAnswer: text(item.myAnswer), correctAnswer: text(item.correctAnswer), reason: text(item.reason), note: text(item.note), resolved: item.resolved === true, createdAt: time(item.createdAt), updatedAt: time(item.updatedAt) };
        }
        return result;
    }
    function readData() { try { return cleanData(JSON.parse(localStorage.getItem(KEY))); } catch (_) { return cleanData(null); } }
    let data = readData(), currentExam = null, overlay = null, previousFocus = null, editorArticle = null;
    let dashboardMode = 'heatmap', query = '', yearFilter = '', statusFilter = '';
    const notify = (message, kind) => { if (window.EnglishApp) window.EnglishApp.toast(message, kind || 'success'); };

    function articleList() {
        const exams = window.EnglishApp ? window.EnglishApp.state().exams.slice() : [];
        if (currentExam && !exams.some(exam => exam.exam_id === currentExam.exam_id)) exams.push(currentExam);
        const list = [];
        for (const exam of exams.filter(e => /_english2$/.test(e.exam_id || '')).sort((a, b) => Number(b.year) - Number(a.year))) {
            const add = (key, label, kind, questions) => list.push({ id: exam.exam_id + '|' + key, examId: exam.exam_id, key, year: exam.year, label, kind, questions });
            (exam.sections || []).forEach((section, si) => {
                if (section.passage) {
                    const cloze = !!section.cloze_options, translation = /Translation|翻译/i.test(section.title || '');
                    const questions = cloze ? Object.keys(section.cloze_options).map(num => ({ num, question: '', options: section.cloze_options[num] })) : [{ num: '46', question: '', options: null }];
                    add('s' + si + '-passage', cloze ? '完形填空' : translation ? '翻译' : section.title || '文章', cloze ? 'cloze' : 'translation', questions);
                }
                (section.parts || []).forEach((part, pi) => {
                    (part.texts || []).forEach((item, ti) => add('s' + si + '-p' + pi + '-t' + ti, item.title || 'Text ' + (ti + 1), 'text' + (ti + 1), (item.questions || []).map(q => ({ num: String(q.q_num), question: q.question || '', options: q.options || null }))));
                    if (!part.texts && part.paragraphs && /Part\s*B/i.test(part.title || '')) add('s' + si + '-p' + pi, '阅读 ' + part.title, 'partB', Array.from({ length: 5 }, (_, i) => ({ num: String(41 + i), question: '', options: null })));
                    if (!part.texts && part.passage && /Part\s*C/i.test(part.title || '')) add('s' + si + '-p' + pi, '阅读 ' + part.title, 'translation', [{ num: '46', question: '', options: null }]);
                });
            });
        }
        return list;
    }
    function findArticle(id) { return articleList().find(article => article.id === id); }
    const articleRecord = id => data.articles[id] || { completedAt: 0, note: '' };
    const mistakesFor = id => Object.entries(data.mistakes).filter(([, item]) => item.articleId === id).sort((a, b) => Number(a[1].question) - Number(b[1].question));
    function commit(update) {
        const next = readData(); update(next);
        try { localStorage.setItem(KEY, JSON.stringify(next)); }
        catch (_) { notify('学习记录保存失败，请先导出备份并释放浏览器存储空间', 'error'); return false; }
        data = next; refreshControls(); return true;
    }
    function updateArticle(id, patch) {
        return commit(next => { next.articles[id] = { completedAt: 0, note: '', ...next.articles[id], ...patch, updatedAt: Date.now() }; });
    }
    function setCompleted(id, checked) {
        const previous = articleRecord(id);
        if (!updateArticle(id, { completedAt: checked ? previous.completedAt || Date.now() : 0 })) return false;
        return true;
    }
    function refreshControls() {
        const root = $('#examContent'); if (!root || !currentExam) return;
        for (const block of $$('[data-study-article]', root)) {
            const id = currentExam.exam_id + '|' + block.dataset.studyArticle;
            const record = articleRecord(id), controls = $('.study-article-controls', block);
            block.classList.toggle('study-complete', !!record.completedAt);
            if (!controls) continue;
            if (controls.dataset.articleId !== id) {
                controls.innerHTML = '<label class="study-complete-check"><input type="checkbox" data-study-complete="' + esc(id) + '" aria-label="' + esc(currentExam.year + ' ' + block.dataset.studyLabel + ' 已翻译') + '"><span>已翻译</span></label><button type="button" class="study-note-button" data-study-open="' + esc(id) + '"></button>';
                controls.dataset.articleId = id;
            }
            const checkbox = $('[data-study-complete]', controls); checkbox.checked = !!record.completedAt;
            checkbox.title = record.completedAt ? '完成于 ' + new Date(record.completedAt).toLocaleDateString('zh-CN') + '，可取消勾选' : '翻译完成后勾选';
            const count = mistakesFor(id).length, button = $('[data-study-open]', controls);
            button.textContent = (record.note.trim() ? '已写笔记' : '笔记') + ' / 错题' + (count ? ' ' + count : '');
        }
        for (const block of $$('[data-study-question]', root)) {
            const article = block.closest('[data-study-article]'); if (!article) continue;
            const id = currentExam.exam_id + '|' + article.dataset.studyArticle, num = block.dataset.studyQuestion;
            let button = $('.study-question-button', block);
            if (!button) { button = document.createElement('button'); button.type = 'button'; button.className = 'study-question-button'; block.appendChild(button); }
            button.dataset.studyQuestionOpen = id; button.dataset.question = num;
            const item = data.mistakes[id + '|q' + num];
            button.textContent = item ? item.resolved ? '已订正 · 查看' : '已记错题' : '记错题';
            button.classList.toggle('has-mistake', !!item && !item.resolved);
            button.classList.toggle('is-resolved', !!item && item.resolved);
            button.setAttribute('aria-label', '第' + num + '题 · ' + button.textContent);
        }
    }
    function onRendered(exam) { currentExam = exam; refreshControls(); }

    function ensureOverlay() {
        if (overlay) return;
        overlay = document.createElement('div'); overlay.className = 'study-overlay';
        overlay.innerHTML = '<section class="study-modal" role="dialog" aria-modal="true" aria-labelledby="studyModalTitle"><header><div><span class="precision-eyebrow">ENGLISH II · 学习记录</span><h2 id="studyModalTitle">翻译进度与错题笔记</h2></div><button type="button" class="precision-icon-close" data-study-close aria-label="关闭学习记录">×</button></header><div class="study-modal-body"></div></section>';
        document.body.appendChild(overlay);
        overlay.addEventListener('click', event => {
            if (event.target === overlay || event.target.closest('[data-study-close]')) { close(); return; }
            const button = event.target.closest('button'); if (!button) return;
            if (button.dataset.studyView) { dashboardMode = button.dataset.studyView; renderDashboard(); }
            if (button.dataset.studyOpen) openArticle(button.dataset.studyOpen, button.dataset.question);
            if (button.dataset.studySource) goToSource(button.dataset.studySource, button.dataset.question);
            if (button.dataset.studyQuestionEdit) openArticle(editorArticle.id, button.dataset.studyQuestionEdit);
            if (button.dataset.studyRemove) {
                if (!confirm('删除这道题的错因和笔记？')) return;
                if (commit(next => { delete next.mistakes[button.dataset.studyRemove]; })) renderEditor(editorArticle, $('#studyQuestionNumber', overlay).value);
            }
        });
        overlay.addEventListener('change', event => {
            if (event.target.matches('[data-editor-complete]')) {
                if (!setCompleted(editorArticle.id, event.target.checked)) event.target.checked = !event.target.checked;
            }
            if (event.target.id === 'studyQuestionNumber') renderEditor(editorArticle, event.target.value);
            if (event.target.closest('#studyMistakeForm') && event.target.id !== 'studyQuestionNumber') saveMistakeForm();
            if (event.target.id === 'studyYearFilter' || event.target.id === 'studyStatusFilter') {
                yearFilter = $('#studyYearFilter', overlay).value;
                statusFilter = $('#studyStatusFilter', overlay) ? $('#studyStatusFilter', overlay).value : '';
                renderDashboardList();
            }
        });
        overlay.addEventListener('input', event => {
            if (event.target.id === 'studyArticleNote') {
                const ok = updateArticle(editorArticle.id, { note: event.target.value });
                $('#studyArticleSaveStatus', overlay).textContent = ok ? '已自动保存' : '未保存，请导出当前笔记后重试';
            }
            if (event.target.closest('#studyMistakeForm') && event.target.id !== 'studyQuestionNumber') saveMistakeForm();
            if (event.target.id === 'studySearch') { query = event.target.value; renderDashboardList(); }
        });
        overlay.addEventListener('keydown', event => {
            if (event.key !== 'Tab') return;
            const focusable = $$('button:not([disabled]),input,select,textarea,a[href]', overlay).filter(el => el.getClientRects().length);
            if (!focusable.length) return;
            if (event.shiftKey && document.activeElement === focusable[0]) { event.preventDefault(); focusable[focusable.length - 1].focus(); }
            else if (!event.shiftKey && document.activeElement === focusable[focusable.length - 1]) { event.preventDefault(); focusable[0].focus(); }
        });
    }
    function show() {
        ensureOverlay();
        if (!overlay.classList.contains('is-open')) previousFocus = document.activeElement;
        overlay.classList.add('is-open'); document.body.classList.add('study-modal-open');
        $('[data-study-close]', overlay).focus();
    }
    function close() {
        if (!overlay) return;
        overlay.classList.remove('is-open'); document.body.classList.remove('study-modal-open');
        if (previousFocus && previousFocus.isConnected) previousFocus.focus({ preventScroll: true });
    }
    function title(value) { $('#studyModalTitle', overlay).textContent = value; }
    function openDashboard() { ensureOverlay(); data = readData(); renderDashboard(); show(); }
    function renderDashboard() {
        editorArticle = null; title('翻译进度与错题笔记');
        const articles = articleList(), completed = articles.filter(article => articleRecord(article.id).completedAt).length;
        const pending = Object.values(data.mistakes).filter(item => !item.resolved).length;
        const tabs = [['heatmap', '翻译热力图'], ['mistakes', '错题本'], ['notes', '文章笔记']];
        const body = $('.study-modal-body', overlay);
        body.scrollTop = 0;
        body.innerHTML = '<div class="study-summary"><div><strong>' + completed + '<small> / ' + articles.length + ' 篇</small></strong><span>已完成翻译</span></div><div><strong>' + (articles.length ? Math.round(completed / articles.length * 100) : 0) + '<small>%</small></strong><span>文章完成率</span></div><div><strong>' + pending + '<small> 题</small></strong><span>待订正错题</span></div></div><div class="study-tabs" aria-label="学习记录分类">' + tabs.map(([mode, label]) => '<button type="button" data-study-view="' + mode + '" aria-pressed="' + (dashboardMode === mode) + '">' + label + '</button>').join('') + '</div>';
        if (dashboardMode === 'heatmap') { body.insertAdjacentHTML('beforeend', heatmapHtml(articles)); return; }
        const years = [...new Set(articles.map(article => String(article.year)))];
        body.insertAdjacentHTML('beforeend', '<div class="study-filters"><label>搜索<input id="studySearch" placeholder="年份、文章、题号、错因或笔记" value="' + esc(query) + '"></label><label>年份<select id="studyYearFilter"><option value="">全部年份</option>' + years.map(year => '<option value="' + esc(year) + '"' + (yearFilter === year ? ' selected' : '') + '>' + esc(year) + '</option>').join('') + '</select></label>' + (dashboardMode === 'mistakes' ? '<label>订正状态<select id="studyStatusFilter"><option value="">全部错题</option><option value="pending"' + (statusFilter === 'pending' ? ' selected' : '') + '>待订正</option><option value="resolved"' + (statusFilter === 'resolved' ? ' selected' : '') + '>已订正</option></select></label>' : '') + '</div><div id="studyDashboardList"></div>');
        renderDashboardList();
    }
    function heatmapHtml(articles) {
        const years = [...new Set(articles.map(article => article.year))];
        let html = '<div class="study-map-legend"><span><i></i>未翻译</span><span><i class="is-complete"></i>✓ 已翻译</span><span>格子里的题数为已记录的错题数；点击格子可查看笔记。</span></div><div class="study-map-scroll"><table class="study-heatmap"><caption>英语二文章翻译完成情况 · 年份 × 文章</caption><thead><tr><th scope="col">年份</th>' + columns.map(([, label]) => '<th scope="col">' + label + '</th>').join('') + '<th scope="col">完成</th></tr></thead><tbody>';
        for (const year of years) {
            const row = articles.filter(article => article.year === year), done = row.filter(article => articleRecord(article.id).completedAt).length;
            html += '<tr><th scope="row">' + esc(year) + '</th>';
            for (const [kind] of columns) {
                const article = row.find(item => item.kind === kind);
                if (!article) { html += '<td class="study-map-missing">—</td>'; continue; }
                const record = articleRecord(article.id), count = mistakesFor(article.id).length;
                const label = year + ' ' + article.label + ' · ' + (record.completedAt ? '已翻译' : '未翻译') + (count ? ' · 错题 ' + count + ' 题' : '') + (record.note.trim() ? ' · 有笔记' : '');
                html += '<td><button type="button" class="study-map-cell' + (record.completedAt ? ' is-complete' : '') + '" data-study-open="' + esc(article.id) + '" title="' + esc(label) + '" aria-label="' + esc(label) + '"><span>' + (record.completedAt ? '✓' : '·') + '</span>' + (count ? '<small>' + count + '题</small>' : '') + (record.note.trim() ? '<b class="study-note-dot" aria-hidden="true">记</b>' : '') + '</button></td>';
            }
            html += '<td><span class="study-year-total intensity-' + (done ? Math.ceil(done / row.length * 4) : 0) + '">' + done + '/' + row.length + '</span></td></tr>';
        }
        return html + '</tbody></table></div><p class="study-local-hint">在文章旁勾选“已翻译”后，这里的格子会同步变绿。学习记录保存在当前浏览器，“数据 → 导出”可一并备份。</p>';
    }
    function renderDashboardList() {
        const list = $('#studyDashboardList', overlay); if (!list) return;
        const articles = new Map(articleList().map(article => [article.id, article]));
        const matches = (article, content) => (!yearFilter || String(article.year) === yearFilter) && (article.year + ' ' + article.label + ' ' + content).toLowerCase().includes(query.toLowerCase());
        if (dashboardMode === 'notes') {
            const notes = Object.entries(data.articles).filter(([id, record]) => articles.has(id) && record.note.trim() && matches(articles.get(id), record.note)).sort((a, b) => b[1].updatedAt - a[1].updatedAt);
            list.innerHTML = notes.length ? notes.map(([id, record]) => '<article class="study-record-card"><header><strong>' + esc(articles.get(id).year + ' · ' + articles.get(id).label) + '</strong><span>' + (record.completedAt ? '已翻译' : '未翻译') + '</span></header><p class="study-user-text">' + esc(record.note) + '</p><footer><button type="button" data-study-open="' + esc(id) + '">编辑笔记</button><button type="button" data-study-source="' + esc(id) + '">回到原文</button></footer></article>').join('') : '<p class="study-empty">没有匹配的笔记。点击文章旁的“笔记 / 错题”即可开始记录。</p>';
            return;
        }
        const mistakes = Object.values(data.mistakes).filter(item => articles.has(item.articleId) && matches(articles.get(item.articleId), '第' + item.question + '题 ' + item.myAnswer + ' ' + item.correctAnswer + ' ' + item.reason + ' ' + item.note) && (!statusFilter || item.resolved === (statusFilter === 'resolved'))).sort((a, b) => b.updatedAt - a.updatedAt);
        list.innerHTML = mistakes.length ? mistakes.map(item => mistakeCard(item, articles.get(item.articleId), false)).join('') : '<p class="study-empty">没有匹配的错题。文章中的每道题旁都有“记错题”入口，也可在文章笔记中按题号记录。</p>';
    }
    function mistakeCard(item, article, inEditor) {
        return '<article class="study-record-card"><header><strong>' + esc((inEditor ? '' : article.year + ' · ' + article.label + ' · ') + '第' + item.question + '题') + '</strong><span class="' + (item.resolved ? 'study-resolved' : 'study-pending') + '">' + (item.resolved ? '已订正' : '待订正') + '</span></header>' + (item.myAnswer || item.correctAnswer ? '<p class="study-answer-pair">我的答案：' + esc(item.myAnswer || '未填') + '　正确答案：' + esc(item.correctAnswer || '未填') + '</p>' : '') + '<p class="study-user-text"><b>错因</b>' + esc(item.reason || '尚未补充') + '</p>' + (item.note ? '<p class="study-user-text"><b>笔记</b>' + esc(item.note) + '</p>' : '') + '<footer>' + (inEditor ? '<button type="button" data-study-question-edit="' + esc(item.question) + '">编辑</button><button type="button" data-study-remove="' + esc(item.articleId + '|q' + item.question) + '">删除</button>' : '<button type="button" data-study-open="' + esc(item.articleId) + '" data-question="' + esc(item.question) + '">编辑错题</button><button type="button" data-study-source="' + esc(item.articleId) + '" data-question="' + esc(item.question) + '">回到题目</button>') + '</footer></article>';
    }
    function openArticle(id, question) {
        const article = findArticle(id); if (!article) { notify('这篇文章尚未加载，请稍后重试', 'warn'); return; }
        ensureOverlay(); data = readData(); renderEditor(article, question); show();
    }
    function renderEditor(article, question) {
        editorArticle = article; title(article.year + ' · ' + article.label);
        const record = articleRecord(article.id), questions = article.questions.slice();
        for (const [, item] of mistakesFor(article.id)) if (!questions.some(q => q.num === item.question)) questions.push({ num: item.question, question: '', options: null });
        const num = String(question || questions[0] && questions[0].num || '1');
        const item = data.mistakes[article.id + '|q' + num] || {};
        const questionData = questions.find(q => q.num === num) || { num, question: '', options: null };
        const source = questionData.question || questionData.options ? '<details class="study-question-source"><summary>查看第' + esc(num) + '题题干和选项</summary><p>' + esc(questionData.question) + '</p>' + Object.entries(questionData.options || {}).map(([letter, value]) => '<p>' + esc(letter) + '. ' + esc(value) + '</p>').join('') + '</details>' : '';
        $('.study-modal-body', overlay).innerHTML = '<div class="study-editor-toolbar"><button type="button" data-study-view="' + dashboardMode + '">← 学习记录</button><label class="study-complete-check"><input type="checkbox" data-editor-complete' + (record.completedAt ? ' checked' : '') + '>已翻译</label><button type="button" data-study-source="' + esc(article.id) + '">回到原文</button></div><label class="study-field">文章笔记<textarea id="studyArticleNote" rows="5" placeholder="记录文章主旨、翻译难点、段落逻辑或你的思考…">' + esc(record.note) + '</textarea></label><p id="studyArticleSaveStatus" class="study-save-status" role="status">输入后自动保存</p><div class="study-editor-grid"><section><h3>记录错题</h3><form id="studyMistakeForm"><label class="study-field">题号<select id="studyQuestionNumber">' + questions.map(q => '<option value="' + esc(q.num) + '"' + (q.num === num ? ' selected' : '') + '>第 ' + esc(q.num) + ' 题</option>').join('') + '</select></label>' + source + '<div class="study-answer-fields"><label class="study-field">我的答案<input id="studyMyAnswer" value="' + esc(item.myAnswer) + '" placeholder="例如 A"></label><label class="study-field">正确答案<input id="studyCorrectAnswer" value="' + esc(item.correctAnswer) + '" placeholder="核对详解后填写"></label></div><label class="study-field">为什么做错<textarea id="studyMistakeReason" rows="3" placeholder="例如：把转折后的观点当成作者支持的观点；定位错了段落…">' + esc(item.reason) + '</textarea></label><label class="study-field">复盘笔记<textarea id="studyMistakeNote" rows="4" placeholder="正确解题思路、原文依据，以及下次要注意的地方…">' + esc(item.note) + '</textarea></label><label class="study-complete-check"><input id="studyMistakeResolved" type="checkbox"' + (item.resolved ? ' checked' : '') + '>已订正</label><p id="studyMistakeSaveStatus" class="study-save-status" role="status">' + (data.mistakes[article.id + '|q' + num] ? '已保存，修改会自动保存' : '填写后自动保存为错题；只打开不会新增记录') + '</p></form></section><section><h3>本篇错题 <span id="studyArticleMistakeCount"></span></h3><div id="studyArticleMistakes"></div></section></div>';
        $('#studyMistakeForm', overlay).onsubmit = event => { event.preventDefault(); saveMistakeForm(); };
        $('.study-modal-body', overlay).scrollTop = 0;
        renderArticleMistakes();
    }
    function saveMistakeForm() {
        if (!editorArticle || !$('#studyMistakeForm', overlay)) return;
        const question = $('#studyQuestionNumber', overlay).value, id = editorArticle.id + '|q' + question;
        const item = { articleId: editorArticle.id, question, myAnswer: $('#studyMyAnswer', overlay).value, correctAnswer: $('#studyCorrectAnswer', overlay).value, reason: $('#studyMistakeReason', overlay).value, note: $('#studyMistakeNote', overlay).value, resolved: $('#studyMistakeResolved', overlay).checked };
        if (!data.mistakes[id] && ![item.myAnswer, item.correctAnswer, item.reason, item.note].some(value => value.trim()) && !item.resolved) return;
        const ok = commit(next => { next.mistakes[id] = { ...item, createdAt: next.mistakes[id] && next.mistakes[id].createdAt || Date.now(), updatedAt: Date.now() }; });
        $('#studyMistakeSaveStatus', overlay).textContent = ok ? '已自动保存' : '未保存，请复制当前内容后重试';
        if (ok) renderArticleMistakes();
    }
    function renderArticleMistakes() {
        if (!editorArticle) return;
        const list = $('#studyArticleMistakes', overlay); if (!list) return;
        const mistakes = mistakesFor(editorArticle.id);
        $('#studyArticleMistakeCount', overlay).textContent = mistakes.length;
        list.innerHTML = mistakes.length ? mistakes.map(([, item]) => mistakeCard(item, editorArticle, true)).join('') : '<p class="study-empty">这篇文章还没有错题记录。</p>';
    }
    async function goToSource(id, question) {
        const article = findArticle(id); if (!article) return;
        close();
        const app = window.EnglishApp;
        if (app.state().activeExamId !== article.examId) await app.selectExam(article.examId);
        else if (window.EnglishPrecision) await window.EnglishPrecision.whenRendered();
        const block = document.getElementById('study-article-' + article.key);
        const target = question && block ? $$('[data-study-question]', block).find(el => el.dataset.studyQuestion === question) || block : block;
        if (target) { target.scrollIntoView({ block: 'start', behavior: 'smooth' }); target.classList.add('study-located'); setTimeout(() => target.classList.remove('study-located'), 2200); }
    }
    function exportData() { data = readData(); return JSON.parse(JSON.stringify(data)); }
    function importData(value) {
        if (!value || typeof value !== 'object' || !value.articles || typeof value.articles !== 'object' || Array.isArray(value.articles) || !value.mistakes || typeof value.mistakes !== 'object' || Array.isArray(value.mistakes)) throw new Error('学习记录备份格式不正确');
        const next = cleanData(value); localStorage.setItem(KEY, JSON.stringify(next)); data = next; refreshControls();
    }
    function init() {
        const button = $('#studyRecordsBtn'); if (button) button.onclick = openDashboard;
        const root = $('#examContent'); if (!root) return;
        root.addEventListener('click', event => {
            const button = event.target.closest('[data-study-open],[data-study-question-open]');
            if (button) openArticle(button.dataset.studyOpen || button.dataset.studyQuestionOpen, button.dataset.question);
        });
        root.addEventListener('change', event => {
            if (event.target.matches('[data-study-complete]') && !setCompleted(event.target.dataset.studyComplete, event.target.checked)) event.target.checked = !event.target.checked;
        });
        document.addEventListener('keydown', event => {
            if (event.key === 'Escape' && overlay && overlay.classList.contains('is-open')) { event.preventDefault(); event.stopImmediatePropagation(); close(); }
        }, true);
        window.addEventListener('storage', event => {
            if (event.key !== KEY && event.key !== null) return;
            data = readData(); refreshControls();
            if (overlay && overlay.classList.contains('is-open') && !editorArticle) renderDashboard();
        });
    }
    window.EnglishStudy = { onRendered, exportData, importData, openDashboard };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
