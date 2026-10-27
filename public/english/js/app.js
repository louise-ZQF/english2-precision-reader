/* ============================================================
   考研英语真题单词本 - 主逻辑
   功能：
   1. 加载/切换真题
   2. 点击英文单词收藏/取消
   3. 单词本抽屉（搜索、删除、清空、复制单词）
   4. 真题详解
   5. 单词背诵（SRS 间隔重复，见 srs-engine.js / srs-panel.js）
   数据持久化：localStorage
   ============================================================ */

(function () {
    'use strict';

    // ==================== 存储 ====================
    const STORAGE_KEY_GROUPS = 'kyc_exam_groups_v1';
    const STORAGE_KEY_TIP_OPEN = 'kyc_tip_open_v1';
    const STORAGE_KEY_WORDS = 'kyc_words_v1';
    const STORAGE_KEY_EXAMS = 'kyc_exams_v1';
    const STORAGE_KEY_ACTIVE = 'kyc_active_exam_v1';
    const BUILTIN_EXAM_PATHS = [
        'data/exam_2010_english2.json',
        'data/exam_2011_english2.json',
        'data/exam_2012_english2.json',
        'data/exam_2013_english2.json',
        'data/exam_2014_english2.json',
        'data/exam_2015_english2.json',
        'data/exam_2016_english2.json',
        'data/exam_2017_english2.json',
        'data/exam_2018_english2.json',
        'data/exam_2019_english2.json',
        'data/exam_2020_english2.json',
        'data/exam_2021_english2.json',
        'data/exam_2022_english2.json',
        'data/exam_2023_english2.json',
        'data/exam_2024_english2.json',
        'data/exam_2025_english2.json',
        'data/exam_2026_english2.json',
    ];

    // ==================== 状态 ====================
    let state = {
        exams: [],
        activeExamId: null,
        words: {},
        groupOpen: loadGroupState(),
        sortMode: 'time',
        freq: null,
        pendingUpload: null
    };

    // ==================== DOM 引用 ====================
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => Array.from(document.querySelectorAll(sel));

    const el = {
        examList: $('#examList'),
        examContent: $('#examContent'),
        tipSection: $('#tipSection'),
        wordCount: $('#wordCount'),
        drawerWordCount: $('#drawerWordCount'),
        drawerFreqTotal: $('#drawerFreqTotal'),
        wordListContainer: $('#wordListContainer'),
        wordListDrawer: $('#wordListDrawer'),
        drawerClose: $('#drawerClose'),
        wordListBtn: $('#wordListBtn'),
        copyBtn: $('#copyBtn'),
        copyBtn2: $('#copyBtn2'),
        clearAllBtn: $('#clearAllBtn'),
        wordSearch: $('#wordSearch'),
        sortToggleBtn: $('#sortToggleBtn'),
        uploadBtn: $('#uploadBtn'),
        uploadModal: $('#uploadModal'),
        uploadClose: $('#uploadClose'),
        uploadCancel: $('#uploadCancel'),
        uploadConfirm: $('#uploadConfirm'),
        uploadZone: $('#uploadZone'),
        fileInput: $('#fileInput'),
        uploadYear: $('#uploadYear'),
        uploadSubject: $('#uploadSubject'),
        materialsBtn: $('#materialsBtn'),
        materialsModal: $('#materialsModal'),
        materialsClose: $('#materialsClose'),
        materialsList: $('#materialsList'),
        friendBtn: $('#friendBtn'),
        friendModal: $('#friendModal'),
        friendClose: $('#friendClose'),
        dblModeBtn: $('#dblModeBtn'),
        uploadForm: $('#uploadForm'),
        uploadStatus: $('#uploadStatus'),
        toast: $('#toast'),
        dictBackdrop: $('#dictBackdrop'),
        dictPanel: $('#dictPanel'),
        dictHandle: $('#dictHandle'),
        dictWord: $('#dictWord'),
        dictCorrect: $('#dictCorrect'),
        dictSpeak: $('#dictSpeak'),
        dictPhonetic: $('#dictPhonetic'),
        dictStar: $('#dictStar'),
        dictClose: $('#dictClose'),
        dictMeta: $('#dictMeta'),
        dictSenses: $('#dictSenses'),
        dictFooter: $('#dictFooter'),
        dictBubble: $('#dictBubble'),
        bubbleWord: $('#bubbleWord'),
        bubbleSpeak: $('#bubbleSpeak'),
        bubblePhonetic: $('#bubblePhonetic'),
        bubbleStar: $('#bubbleStar'),
        bubbleCorrect: $('#bubbleCorrect'),
        bubbleSenses: $('#bubbleSenses'),
        bubbleMore: $('#bubbleMore'),
        feedbackBtn: $('#feedbackBtn'),
        feedbackModal: $('#feedbackModal'),
        feedbackClose: $('#feedbackClose'),
        feedbackText: $('#feedbackText'),
        feedbackCount: $('#feedbackCount'),
        feedbackSubmit: $('#feedbackSubmit')
    };

    // ==================== 工具函数 ====================
    function escapeHtml(s) {
        if (s == null) return '';
        return String(s)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function escapeRegExp(s) {
        return String(s).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    const POS_LABEL = {
        n: '名', v: '动', vt: '动', vi: '动', a: '形', adj: '形',
        ad: '副', adv: '副', prep: '介', conj: '连', pron: '代',
        num: '数', art: '冠', aux: '助', int: '叹',
        计: '计', 网络: '网', 医: '医', 化: '化', 律: '律', 经: '经'
    };

    function posLabel(p) {
        if (!p) return '';
        return POS_LABEL[p] || p;
    }

    function normalizeWord(w) {
        return String(w).toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/[\u2010\u2011]/g, '-').replace(/[^a-z'\s-]/g, '').replace(/\s+/g, ' ').trim();
    }

    // 不规则动词过去式/过去分词 → 原形。
    // lookupWord 与 prepareEntry 共用；**改这里要同步 scripts/english_seo/build.py 的
    // IRREGULAR_VERBS**（那边用同一张表做释义修复）。
    const IRREGULAR_VERBS = {
        stuck: 'stick', upheld: 'uphold', oversaw: 'oversee', struck: 'strike',
        met: 'meet', hidden: 'hide', won: 'win', sat: 'sit', stood: 'stand',
        laid: 'lay', drawn: 'draw', swept: 'sweep', withdrawn: 'withdraw',
        sought: 'seek', brought: 'bring', thought: 'think', bought: 'buy',
        caught: 'catch', taught: 'teach', fought: 'fight', found: 'find',
        held: 'hold', kept: 'keep', left: 'leave', lost: 'lose', made: 'make',
        meant: 'mean', paid: 'pay', ran: 'run', said: 'say', sold: 'sell',
        sent: 'send', spent: 'spend', told: 'tell', took: 'take',
        underwent: 'undergo', went: 'go', written: 'write', wrote: 'write',
        fed: 'feed', felt: 'feel', flew: 'fly', flown: 'fly', grew: 'grow',
        grown: 'grow', knew: 'know', known: 'know', rose: 'rise', risen: 'rise',
        saw: 'see', seen: 'see', shook: 'shake', shaken: 'shake', spoke: 'speak',
        spoken: 'speak', stole: 'steal', stolen: 'steal', swam: 'swim',
        swum: 'swim', threw: 'throw', thrown: 'throw', wore: 'wear',
        worn: 'wear', began: 'begin', begun: 'begin', bore: 'bear',
        borne: 'bear', broke: 'break', broken: 'break', chose: 'choose',
        chosen: 'choose', drove: 'drive', driven: 'drive', ate: 'eat',
        eaten: 'eat', fell: 'fall', fallen: 'fall', gave: 'give',
        given: 'give', hung: 'hang', led: 'lead', lay: 'lie', lain: 'lie',
        rode: 'ride', ridden: 'ride', rang: 'ring', rung: 'ring',
        sang: 'sing', sung: 'sing', sank: 'sink', sunk: 'sink',
        slept: 'sleep', spread: 'spread', sprang: 'spring', sprung: 'spring'
    };

    function isCollected(word) {
        const key = normalizeWord(word);
        return !!state.words[key];
    }

    function showToast(msg, type) {
        type = type || 'success';
        el.toast.textContent = msg;
        el.toast.className = 'toast ' + type + ' show';
        clearTimeout(el.toast._timer);
        el.toast._timer = setTimeout(() => {
            el.toast.classList.remove('show');
        }, 2200);
    }

    // ==================== 存储 ====================
    function loadWords() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_WORDS);
            state.words = raw ? JSON.parse(raw) : {};
        } catch (e) {
            state.words = {};
        }
    }

    function saveWords() {
        try {
            localStorage.setItem(STORAGE_KEY_WORDS, JSON.stringify(state.words));
        } catch (e) {
            showToast('保存失败：浏览器存储空间不足', 'error');
        }
    }

    function loadExams() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_EXAMS);
            state.exams = (raw ? JSON.parse(raw) : []).filter(e => /_english2$/.test(e.exam_id || '')); // Local scope: English II only
        } catch (e) {
            state.exams = [];
        }
    }

    function saveExams() {
        try {
            localStorage.setItem(STORAGE_KEY_EXAMS, JSON.stringify(state.exams));
        } catch (e) {
            showToast('保存失败：存储空间不足', 'error');
        }
    }

    // 内置真题的**内容戳**：与 version.json 的 exams 戳比对。
    // 一致 = 服务器上的真题一个字都没改 → 本地这份可以继续用，一个请求都不用发。
    // 这是把真题从「每次打开都重下 34 套（1.05 MB）」降下来的关键。
    const STORAGE_KEY_EXAMS_STAMP = 'kyc_exams_stamp_v1';

    function storedExamsStamp() {
        try { return localStorage.getItem(STORAGE_KEY_EXAMS_STAMP) || ''; } catch (e) { return ''; }
    }

    function saveExamsStamp(stamp) {
        try { localStorage.setItem(STORAGE_KEY_EXAMS_STAMP, String(stamp || '')); } catch (e) { /* 隐私模式：忽略 */ }
    }

    function examIdFromPath(p) {
        return (String(p).match(/exam_([a-z0-9_]+)\.json/) || [])[1] || '';
    }

    /** 本地存的真题是否"完整可用"：34 套内置题全在、且都带正文 sections。
     *  防止「上次只下到一半就关了页面」被误当成完整缓存。 */
    function builtinsComplete() {
        if (!Array.isArray(state.exams) || !state.exams.length) return false;
        return BUILTIN_EXAM_PATHS.every(function (p) {
            const id = examIdFromPath(p);
            if (!id) return false;
            const e = state.exams.find(function (x) { return x.exam_id === id; });
            return !!(e && e.builtin && Array.isArray(e.sections) && e.sections.length);
        });
    }

    function sortExamsByYearDesc(a, b) {
        return (parseInt(b.year, 10) || 0) - (parseInt(a.year, 10) || 0);
    }

    function loadActiveExamId() {
        state.activeExamId = localStorage.getItem(STORAGE_KEY_ACTIVE) || null;
    }

    function saveActiveExamId() {
        if (state.activeExamId) {
            localStorage.setItem(STORAGE_KEY_ACTIVE, state.activeExamId);
        }
    }

    // ==================== 单词收藏 ====================
    function toggleWord(word) {
        const key = normalizeWord(word);
        if (!key) return;
        if (state.words[key]) {
            delete state.words[key];
            showToast('已取消收藏：' + word, 'warn');
        } else {
            state.words[key] = {
                word: word,
                addedAt: Date.now(),
                examId: state.activeExamId
            };
            showToast('已收藏：' + word, 'success');
        }
        saveWords();
        updateWordCount();
        renderWordList();
        $$('span.word[data-word]').forEach(span => {
            if (normalizeWord(span.dataset.word) === key) {
                span.classList.toggle('collected', !!state.words[key]);
            }
        });
        syncDictStar();
    }

    // ==================== 数据版本（data/version.json） ====================
    // 血泪教训（2026-09-26）：句库/真题/词典的 URL 版本串是**手工维护**的，
    // 而句库又用 `cache: 'force-cache'` 取——版本串忘了 bump，回头用户就永远
    // 吃本地缓存里的旧句库：症状是「阅读选项 ABCD 点了全是暂未收录」，
    // 服务端怎么修都没用（实测：当前代码 + 旧句库快照 → 76/76 选项未收录）。
    // 现在改成：部署时按**文件内容 md5** 生成 data/version.json，
    // 前端用它拼 URL；内容变了 URL 就变，不需要谁记得 bump。
    // 同一个文件还兼作「过期代码自愈」：app 的版本串（index.html 里的 ?v=N）
    // 与 version.json 的 app 不一致时自动刷新一次（手机浏览器长期不关标签页，
    // 页面里跑的还是部署前的旧 JS）。
    const DATA_VERSIONS = { app: '', bank: '4', dict: '6', exams: '3' };
    let dataVersionsPromise = null;

    // 注意：`document.currentScript` **只在脚本同步执行期间**有效，异步回调里是 null。
    // 所以这里在 IIFE 顶层同步取一次并记住（踩过：放在 async init 里取，永远拿到空串，
    // 过期自愈逻辑静默失效）。
    const APP_TAG = (function () {
        try {
            const s = document.currentScript && document.currentScript.src;
            // 版本串从「递增数字」改成**内容戳**（部署时按文件 md5 生成）后，这里必须一并放宽，
            // 否则取不到 tag → guardStaleCode 静默失效（页面里跑旧 JS 也不再自愈）。
            const m = s && s.match(/app\.js\?v=([0-9a-zA-Z._-]+)/);
            return m ? m[1] : '';
        } catch (e) { return ''; }
    })();

    function appTag() { return APP_TAG; }

    function loadDataVersions() {
        if (dataVersionsPromise) return dataVersionsPromise;
        dataVersionsPromise = (async () => {
            try {
                const r = await fetch('data/version.json?t=' + Date.now(), { cache: 'no-store' });
                if (!r.ok) return DATA_VERSIONS;
                const v = await r.json();
                for (const k of ['app', 'bank', 'dict', 'exams']) {
                    if (v && v[k]) DATA_VERSIONS[k] = String(v[k]);
                }
            } catch (e) { /* 拿不到就用默认串，不影响功能 */ }
            return DATA_VERSIONS;
        })();
        return dataVersionsPromise;
    }

    /** 页面里的 JS 比服务端旧（长驻标签页/旧缓存）→ 自动刷新一次。
     *  sessionStorage 记标记，避免刷新循环；同一会话每出现一个新版本最多刷一次。 */
    async function guardStaleCode() {
        const tag = appTag();
        if (!tag) return;
        const v = await loadDataVersions();
        if (!v.app || String(v.app) === String(tag)) return;
        try {
            if (sessionStorage.getItem('aseeker_reloaded_for') === String(v.app)) return;
            sessionStorage.setItem('aseeker_reloaded_for', String(v.app));
        } catch (e) { /* 隐私模式没有 sessionStorage：那就直接刷 */ }
        // 首屏还在加载时不要立刻刷（会白扔掉正在下载的真题），等 load 完再刷
        if (document.readyState === 'complete') location.reload();
        else window.addEventListener('load', () => location.reload(), { once: true });
    }

    // ==================== 单词释义（长按/悬停气泡 + 完整面板） ====================
    // 词典 URL 在**调用时**拼（而不是模块加载时定住），这样 version.json 晚到也能生效
    function dictUrl() { return 'data/dict.json?v=' + DATA_VERSIONS.dict; }
    let dictCache = null;
    let dictPending = null;
    let dictCurrentWord = null;
    let bubbleAnchor = null;
    let suppressClick = false;
    let pressTimer = null;
    let pressStart = null;
    // 最近一次「长按查词」弹词典气泡的时间：翻译模式下 click 兜底不能把刚弹出的词典气泡顶掉
    let lastLongPressAt = 0;
    let hoverTimer = null;
    let keepBubble = false;
    let dictLastEntry = null;
    // 双击行为开关：collect（默认，单击=收藏）| translate（单击单词=整句翻译）
    const DBL_MODE_KEY = 'aseeker_english_dbl_mode';
    let dblMode = loadDblMode();

    function loadDblMode() {
        try { return localStorage.getItem(DBL_MODE_KEY) === 'translate' ? 'translate' : 'collect'; }
        catch (e) { return 'collect'; }
    }
    function saveDblMode(m) {
        try { localStorage.setItem(DBL_MODE_KEY, m); } catch (e) {}
    }
    function applyDblModeUI() {
        const btn = el.dblModeBtn;
        if (!btn) return;
        btn.classList.toggle('is-translate', dblMode === 'translate');
        const st = btn.querySelector('.dbl-mode-state');
        if (st) st.textContent = dblMode === 'translate' ? '翻译' : '收藏';
        btn.setAttribute('aria-pressed', dblMode === 'translate' ? 'true' : 'false');
    }
    const canHover = window.matchMedia && window.matchMedia('(hover: hover)').matches;

    function loadDict() {
        if (dictCache) return Promise.resolve(dictCache);
        if (dictPending) return dictPending;
        dictPending = loadDataVersions().then(() => fetch(dictUrl()))
            .then(r => {
                if (!r.ok) throw new Error('HTTP ' + r.status);
                return r.json();
            })
            .then(data => {
                dictCache = data;
                return data;
            })
            .catch(err => {
                dictPending = null;
                throw err;
            });
        return dictPending;
    }

    function lookupWord(word) {
        if (!dictCache) return null;
        const key = normalizeWord(word);
        const repair = (e) => prepareEntry(key, e);
        let e = dictCache.dict[key];
        if (e) return repair(e);
        const base = key.replace(/'s$/, '').replace(/'$/, '');
        if (base && base !== key && dictCache.dict[base]) return repair(dictCache.dict[base]);
        // 词形还原：ing/ed/es/s 派生形式回查原形
        const stems = [];
        // 复数 y→ies, f/fe→ves
        if (key.endsWith('ies')) {
            stems.push(key.slice(0, -3) + 'y');
        }
        if (key.endsWith('ves')) {
            stems.push(key.slice(0, -3) + 'f', key.slice(0, -3) + 'fe');
        }
        if (key.endsWith('ing')) {
            stems.push(key.slice(0, -3), key.slice(0, -3) + 'e');
            const ib = key.slice(0, -3);
            if (ib.length >= 2 && ib[ib.length - 1] === ib[ib.length - 2]) stems.push(ib.slice(0, -1));
            if (ib.endsWith('e')) stems.push(ib.slice(0, -1));
            if (ib.endsWith('i')) stems.push(ib.slice(0, -1) + 'y');
        }
        if (key.endsWith('ed')) {
            stems.push(key.slice(0, -2), key.slice(0, -1));
            const eb = key.slice(0, -2);
            if (eb.length >= 2 && eb[eb.length - 1] === eb[eb.length - 2]) stems.push(eb.slice(0, -1));
            if (eb.endsWith('i')) stems.push(eb.slice(0, -1) + 'y');
        }
        if (key.endsWith('es')) {
            stems.push(key.slice(0, -2), key.slice(0, -1));
        }
        if (key.endsWith('s')) {
            stems.push(key.slice(0, -1));
        }
        // 不规则动词过去式/过去分词（表在文件上方的 IRREGULAR_VERBS）
        if (IRREGULAR_VERBS[key]) stems.push(IRREGULAR_VERBS[key]);
        for (const st of stems) {
            if (st && st !== key && dictCache.dict[st]) {
                return repair(Object.assign({ _partial: st }, dictCache.dict[st]));
            }
        }
        // 美式/英式拼写变体互查（ize <-> ise）
        if (key.endsWith('ize')) {
            const alt = key.slice(0, -3) + 'ise';
            if (dictCache.dict[alt]) return repair(Object.assign({ _partial: alt }, dictCache.dict[alt]));
        }
        if (key.endsWith('ise')) {
            const alt = key.slice(0, -3) + 'ize';
            if (dictCache.dict[alt]) return repair(Object.assign({ _partial: alt }, dictCache.dict[alt]));
        }
        if (key.indexOf('-') >= 0) {
            // 连字符复合词：真题里有 473 个未收录（self-esteem / public-sector …），
            // 按子词从右往左回查，并把命中子词带上，弹窗会标注「释义参考 <子词>」。
            const parts = key.split('-').filter((p) => p);
            for (let i = parts.length - 1; i >= 0; i--) {
                if (dictCache.dict[parts[i]]) {
                    const hit = dictCache.dict[parts[i]];
                    return repair(Object.assign({ _partial: parts[i] }, hit));
                }
            }
        }
        return null;
    }

    function senseDisplayOrder(entry) {
        const order = [];
        const seen = {};
        const rk = entry.rk || [];
        for (const i of rk) {
            if (i >= 0 && i < entry.s.length && !seen[i]) {
                order.push(i);
                seen[i] = true;
            }
        }
        for (let i = 0; i < entry.s.length; i++) {
            if (!seen[i]) order.push(i);
        }
        return order;
    }

    function senseRowHtml(s, withBadge) {
        return '<div class="sense-row">' +
            '<span class="sense-pos' + (s.p ? '' : ' empty') + '">' + escapeHtml(posLabel(s.p) || '·') + '</span>' +
            '<span class="sense-text">' + escapeHtml(s.t) + '</span>' +
            (withBadge ? '<span class="sense-badge">真题高频</span>' : '') +
            '</div>';
    }

    function topSense(entry) {
        const rk = entry.rk || [];
        if (rk.length && entry.sh && entry.sh[rk[0]] > 0) return rk[0];
        return -1;
    }

    function syncDictStar() {
        if (!dictCurrentWord) return;
        const on = isCollected(dictCurrentWord);
        el.dictStar.classList.toggle('on', on);
        el.bubbleStar.classList.toggle('on', on);
    }

    // ---------- 气泡 ----------
    // 整句包围盒：把气泡锚在“单词所在的整句”上（而不是单词矩形上），
    // 弹窗放在整句的上方/下方，就不会盖住正在阅读的句子。
    function sentenceBox(para, sentence) {
        try {
            if (!para || !sentence) return null;
            const full = para.textContent || '';
            const idx = full.indexOf(sentence);
            if (idx < 0) return null;
            const range = document.createRange();
            let off = 0;
            let startNode = null, startOff = 0, endNode = null, endOff = 0;
            const walker = document.createTreeWalker(para, NodeFilter.SHOW_TEXT);
            let node = null;
            while ((node = walker.nextNode())) {
                const len = (node.textContent || '').length;
                if (startNode === null && off + len > idx) {
                    startNode = node;
                    startOff = idx - off;
                }
                if (endNode === null && off + len >= idx + sentence.length) {
                    endNode = node;
                    endOff = idx + sentence.length - off;
                    break;
                }
                off += len;
            }
            if (!startNode || !endNode) return null;
            range.setStart(startNode, startOff);
            range.setEnd(endNode, endOff);
            let box = null;
            for (const r of range.getClientRects()) {
                if (r.width < 1 || r.height < 1) continue;
                if (!box) box = { left: r.left, top: r.top, right: r.right, bottom: r.bottom };
                else {
                    box.left = Math.min(box.left, r.left);
                    box.top = Math.min(box.top, r.top);
                    box.right = Math.max(box.right, r.right);
                    box.bottom = Math.max(box.bottom, r.bottom);
                }
            }
            return box;
        } catch (e) {
            return null;
        }
    }

    // 通用避让：以“保护盒”（整句/选区）为中心定位气泡——
    // 默认放【下方】，其次上方，两边都放不下时取剩余空间大的一侧；
    // 水平方向只在视口内夹紧，保证气泡与所读句子不重叠。
    function placeBubbleAvoiding(bubble, box) {
        const vw = window.innerWidth;
        const vh = window.innerHeight;
        const bw = bubble.offsetWidth || 300;
        const bh = bubble.offsetHeight || 160;
        const gap = 10;
        let left = box.left + (box.right - box.left) / 2 - bw / 2;
        left = Math.max(12, Math.min(left, vw - bw - 12));
        const spaceAbove = box.top - gap;
        const spaceBelow = vh - box.bottom - gap;
        let top;
        if (spaceBelow >= bh) {
            top = box.bottom + gap;
        } else if (spaceAbove >= bh) {
            top = box.top - bh - gap;
        } else if (spaceBelow >= spaceAbove) {
            top = Math.min(vh - bh - 8, box.bottom + gap);
        } else {
            top = Math.max(8, box.top - bh - gap);
        }
        top = Math.max(8, Math.min(top, vh - bh - 8));
        bubble.style.left = left + 'px';
        bubble.style.top = top + 'px';
    }

    function positionBubble(span) {
        // 按用户要求：单词气泡放在选中单词【下方】（紧贴单词），
        // 下方空间不够时再翻到上方；不需要整句避让。
        const r = span.getBoundingClientRect();
        const bw = el.dictBubble.offsetWidth || 300;
        const bh = el.dictBubble.offsetHeight || 160;
        const gap = 10;
        let left = r.left + r.width / 2 - bw / 2;
        left = Math.max(12, Math.min(left, window.innerWidth - bw - 12));
        let top;
        const spaceAbove = r.top - gap;
        const spaceBelow = window.innerHeight - r.bottom - gap;
        if (spaceBelow >= bh) {
            // 默认放单词下方
            top = r.bottom + gap;
        } else if (spaceAbove >= bh) {
            top = r.top - bh - gap;
        } else {
            // 上下都不够放：取剩余空间大的一侧，避免遮挡单词
            top = spaceBelow > spaceAbove ? (window.innerHeight - bh - 8) : 8;
        }
        top = Math.max(8, Math.min(top, window.innerHeight - bh - 8));
        el.dictBubble.style.left = left + 'px';
        el.dictBubble.style.top = top + 'px';
    }

    function renderBubble(word, entry) {
        el.bubbleWord.textContent = word;
        el.bubblePhonetic.textContent = entry.ph || '';
        syncDictStar();
        const order = senseDisplayOrder(entry);
        const top = topSense(entry);
        let html = '';
        let shown = 0;
        for (const idx of order) {
            html += senseRowHtml(entry.s[idx], idx === top);
            shown++;
            if (shown >= 3) break;
        }
        el.bubbleSenses.innerHTML = html || '<div class="dict-missing">暂未收录</div>';
        el.bubbleMore.style.display = entry.s.length > 1 ? '' : 'none';
        el.bubbleMore.textContent = '查看全部 ' + entry.s.length + ' 个义项';
    }

    function showBubble(word, span) {
        dictCurrentWord = word;
        bubbleAnchor = span;
        el.bubbleWord.textContent = word;
        el.bubblePhonetic.textContent = '';
        el.bubbleSenses.innerHTML = '<div class="dict-loading">加载中…</div>';
        el.dictBubble.classList.add('show');
        positionBubble(span);
        syncDictStar();
        loadDict().then(() => {
            if (dictCurrentWord !== word) return;
            const entry = lookupWord(word);
            if (entry) {
                renderBubble(word, entry);
                if (span.isConnected) positionBubble(span);
            } else {
                // 未收录时给可操作的出路：连字符词告诉用户点哪个子词
                let hint = '';
                const key = normalizeWord(word);
                if (key.indexOf('-') >= 0 && dictCache && dictCache.dict) {
                    const hit = key.split('-').filter((p) => p && dictCache.dict[p]);
                    if (hit.length) {
                        hint = '<div class="dict-missing-hint">这是合成词，可点 ' +
                            hit.map((p) => '<code>' + escapeHtml(p) + '</code>').join(' / ') +
                            ' 查看子词释义</div>';
                    }
                }
                el.bubbleSenses.innerHTML =
                    '<div class="dict-missing">词库暂未收录「' + escapeHtml(word) + '」</div>' + hint;
                if (span.isConnected) positionBubble(span);
            }
        }).catch(() => {
            if (dictCurrentWord !== word) return;
            el.bubbleSenses.innerHTML = '<div class="dict-missing">词库加载失败</div>';
        });
    }

    // ==================== 释义修复（对齐 scripts/english_seo/build.py） ====================
    // 治用户纠错里反复出现的「释义不对/不全」。ECDICT 有两类条目会让弹窗显示
    // 不适用的释义，实测用户点到的词高度集中在这两类：
    //   ① 首义是专业领域标注且语义冷僻：circumstances →「法 事件, 事项, 详细情节」
    //      （用户直接反馈「环境」）、manipulating →「计 手动」、bruising →「化 硬伤」
    //      而它们的**原形**才有通用义：circumstance → n 环境, 状况, 事件
    //   ② 首义只是词形说明、没有实义：stuck →「stick的过去式和过去分词」
    // 修法：能回退到原形就回退；回退不到就把领域义项排到后面。
    // **改这里必须同步 build.py 的 DOMAIN_POS / prepare_entry**，两边口径要一致。
    const DOMAIN_POS = new Set(('法 计 化 医 经 电 机 农 物 生 数 冶 船 建 军 天 地 矿 纺 食 心 哲 逻 律 商 财 会 统 测 aut').split(' '));
    const MORPH_WORD = '(过去式|过去分词|现在分词|第三人称单数|复数形式|复数|变形|比较级|最高级)';
    const MORPH_RE = new RegExp('的' + MORPH_WORD + '|' + MORPH_WORD + '和' + MORPH_WORD);
    const PAREN_RE = /[（(][^）)]*[）)]/g;

    function isMorphHint(entry) {
        if (!entry || !entry.s || !entry.s.length) return false;
        const t = entry.s[0].t || '';
        const stripped = t.replace(PAREN_RE, '').trim();
        if (!MORPH_RE.test(stripped)) return false;
        // 去掉词形说明字样与连接词/标点后，还有中文实义就不算纯词形说明
        const residue = stripped.replace(new RegExp(MORPH_WORD, 'g'), '')
            .replace(/[的和与、,，.。;；:：/·\-—\s]/g, '');
        return !/[\u4e00-\u9fff]/.test(residue);
    }

    function firstSenseDomain(entry) {
        if (!entry || !entry.s || !entry.s.length) return null;
        const p = (entry.s[0].p || '').trim();
        return DOMAIN_POS.has(p) ? p : null;
    }

    function isPlainEntry(entry) {
        return entry && entry.s && entry.s.length && !isMorphHint(entry) && !firstSenseDomain(entry);
    }

    /** 把一条词条修成「适合展示」的形态；修不动就原样返回。 */
    function prepareEntry(word, entry) {
        if (!entry || !entry.s || !entry.s.length) return entry;
        const key = normalizeWord(word);
        if (isMorphHint(entry) || firstSenseDomain(entry)) {
            // 复用 lookupWord 的词干链：找出一个「本身是普通词条」的原形
            for (const st of stemCandidates(key)) {
                const base = dictCache && dictCache.dict[st];
                if (base && isPlainEntry(base)) {
                    return Object.assign({}, base, { _partial: st, _from: st });
                }
            }
        }
        if (firstSenseDomain(entry) && entry.s.length > 1) {
            const plain = entry.s.filter(s => !DOMAIN_POS.has((s.p || '').trim()));
            const domained = entry.s.filter(s => DOMAIN_POS.has((s.p || '').trim()));
            if (plain.length) {
                return Object.assign({}, entry, { s: plain.concat(domained) });
            }
        }
        return entry;
    }

    /** 词形还原候选（供 prepareEntry 复用，与 lookupWord 的规则保持一致）。 */
    function stemCandidates(key) {
        const stems = [];
        if (key.endsWith('ies')) stems.push(key.slice(0, -3) + 'y');
        if (key.endsWith('ves')) stems.push(key.slice(0, -3) + 'f', key.slice(0, -3) + 'fe');
        if (key.endsWith('ing')) {
            const ib = key.slice(0, -3);
            stems.push(ib, ib + 'e');
            if (ib.length >= 2 && ib[ib.length - 1] === ib[ib.length - 2]) stems.push(ib.slice(0, -1));
            if (ib.endsWith('e')) stems.push(ib.slice(0, -1));
            if (ib.endsWith('i')) stems.push(ib.slice(0, -1) + 'y');
        }
        if (key.endsWith('ed') && key.length >= 4) {
            const eb = key.slice(0, -2);
            // **先试「-d」形态（stem+e）再试裸截断**：rated→rate（不是 rat）、
            // used→use（不是 us）、hoped→hope（不是 hop）、cared→care（不是 car）。
            // 旧顺序是反的，用户纠错 #57「13年13题 rated」看到的就是 rat 的释义。
            // 长度 ≥4 才脱：bed/red/led 这类本身是词，不该被拆（它们会先命中精确词条）。
            stems.push(key.slice(0, -1), key.slice(0, -2));
            if (eb.length >= 2 && eb[eb.length - 1] === eb[eb.length - 2]) stems.push(eb.slice(0, -1));
            if (eb.endsWith('i')) stems.push(eb.slice(0, -1) + 'y');
        }
        if (key.endsWith('es')) stems.push(key.slice(0, -2), key.slice(0, -1));
        if (key.endsWith('s')) stems.push(key.slice(0, -1));
        if (IRREGULAR_VERBS[key]) stems.unshift(IRREGULAR_VERBS[key]);
        return stems.filter((s) => s && s !== key);
    }

    function closeBubble() {
        el.dictBubble.classList.remove('show');
        bubbleAnchor = null;
        if (dictCurrentWord && !el.dictPanel.classList.contains('show')) {
            dictCurrentWord = null;
        }
    }

    function isBubbleOpen() {
        return el.dictBubble.classList.contains('show');
    }

    // ---------- 完整面板 ----------
    function renderDictPanel(word, entry) {
        dictLastEntry = entry;
        el.dictWord.textContent = word;
        el.dictPhonetic.textContent = entry.ph || '';
        syncDictStar();

        let meta = '';
        if (entry._partial) meta += '<span class="meta-chip">释义参考 ' + escapeHtml(entry._partial) + '</span>';
        const tags = entry.tag || [];
        if (tags.indexOf('ky') >= 0) meta += '<span class="meta-chip">考研词</span>';
        if (tags.indexOf('cet4') >= 0) meta += '<span class="meta-chip">四级</span>';
        if (tags.indexOf('cet6') >= 0) meta += '<span class="meta-chip">六级</span>';
        el.dictMeta.innerHTML = meta;

        const order = senseDisplayOrder(entry);
        const top = topSense(entry);
        let html = '';
        if (top >= 0) {
            html += '<div class="dict-highlight"><div class="dict-highlight-label">真题高频</div>' +
                senseRowHtml(entry.s[top], false) + '</div>';
        }
        const rest = order.filter(i => i !== top);
        const limit = 4;
        const showAll = el.dictPanel._showAll === true;
        const visible = showAll ? rest : rest.slice(0, limit);
        visible.forEach(idx => {
            html += senseRowHtml(entry.s[idx], false);
        });
        if (rest.length > limit) {
            html += '<button class="dict-collapse-btn" data-collapse>' +
                (showAll ? '收起义项' : '展开全部 ' + rest.length + ' 个义项') + '</button>';
        }
        el.dictSenses.innerHTML = html || '<div class="dict-missing">暂未收录该词释义</div>';

        let foot = '';
        if (entry.hit) foot += '<span class="foot-chip">真题出现 <b>' + entry.hit + '</b> 次</span>';
        if (tags.indexOf('ky') >= 0) foot += '<span class="foot-chip">考研词表</span>';
        if (entry.cl) foot += '<span class="foot-chip">柯林斯 <b>' + '★'.repeat(Math.min(entry.cl, 5)) + '</b></span>';
        if (entry.frq) foot += '<span class="foot-chip">词频 <b>' + entry.frq + '</b></span>';
        el.dictFooter.innerHTML = foot;
    }

    function openDictPanel(word) {
        closeBubble();
        dictCurrentWord = word;
        el.dictPanel._showAll = false;
        el.dictWord.textContent = word;
        el.dictPhonetic.textContent = '';
        el.dictMeta.innerHTML = '';
        el.dictFooter.innerHTML = '';
        el.dictSenses.innerHTML = '<div class="dict-loading">词库加载中…</div>';
        syncDictStar();
        el.dictPanel.classList.add('show');
        el.dictBackdrop.classList.add('show');
        document.body.style.overflow = 'hidden';

        loadDict().then(() => {
            if (dictCurrentWord !== word) return;
            const entry = lookupWord(word);
            if (entry) {
                renderDictPanel(word, entry);
            } else {
                el.dictSenses.innerHTML = '<div class="dict-missing">词库暂未收录「' + escapeHtml(word) +
                    '」<br>可先收藏，之后在生词本中学习。</div>';
            }
        }).catch(() => {
            if (dictCurrentWord !== word) return;
            el.dictSenses.innerHTML = '<div class="dict-missing">词库加载失败，请检查网络后重试</div>';
        });
    }

    function closeDictPanel() {
        el.dictPanel.classList.remove('show');
        el.dictBackdrop.classList.remove('show');
        document.body.style.overflow = '';
        dictCurrentWord = null;
    }

    function speakWord(word) {
        // 优先在线音频（手机 speechSynthesis 常无声），全局 WordSpeak 自带回退
        if (window.WordSpeak) { window.WordSpeak(word); return; }
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(word);
        u.lang = 'en-US';
        u.rate = 0.85;
        window.speechSynthesis.speak(u);
    }

    // ==================== 使用反馈 ====================
    function openFeedback() {
        el.feedbackModal.classList.add('open');
        el.feedbackText.focus();
    }

    function closeFeedback() {
        el.feedbackModal.classList.remove('open');
    }

    // CSRF token（Double-Submit Cookie）：静态站无后端页面会话，
    // 由前端生成并持久化 csrf cookie，POST 时带回 X-CSRF-Token 头。
    // 跨站攻击者无法读取/写入本站 cookie，语义与后端 ensureCsrf 一致。
    function csrfToken() {
        try {
            const m = document.cookie.match(/(?:^|;\s*)csrf=([^;]+)/);
            if (m) return m[1];
            const t = (window.crypto && crypto.randomUUID)
                ? crypto.randomUUID().replace(/-/g, '')
                : (Math.random().toString(36).slice(2) + Date.now().toString(36));
            document.cookie = 'csrf=' + t + '; path=/; max-age=' + (365 * 24 * 3600) + '; SameSite=Strict';
            return t;
        } catch (e) {
            return '';
        }
    }

    function submitFeedback() {
        const content = el.feedbackText.value.trim();
        if (!content) {
            showToast('请先填写反馈内容', 'warn');
            return;
        }
        if (content.length > 1000) {
            showToast('内容不能超过 1000 字', 'warn');
            return;
        }
        el.feedbackSubmit.disabled = true;
        el.feedbackSubmit.textContent = '提交中…';
        fetch('/biochem/api/feedback/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': csrfToken() },
            body: JSON.stringify({ content: content })
        }).then(r => {
            if (r.ok) return r.json();
            return r.json().then(d => { throw new Error(d.error || '提交失败'); });
        }).then(() => {
            showToast('反馈已保存在本机', 'success');
            el.feedbackText.value = '';
            el.feedbackCount.textContent = '0';
            closeFeedback();
        }).catch(err => {
            showToast(err.message || '提交失败，请检查网络', 'error');
        }).finally(() => {
            el.feedbackSubmit.disabled = false;
            el.feedbackSubmit.textContent = '提交反馈';
        });
    }

    function removeWord(word) {
        const key = normalizeWord(word);
        delete state.words[key];
        saveWords();
        updateWordCount();
        renderWordList();
        $$('span.word[data-word]').forEach(span => {
            if (normalizeWord(span.dataset.word) === key) {
                span.classList.remove('collected');
            }
        });
    }

    function clearAllWords() {
        const count = Object.keys(state.words).length;
        if (count === 0) {
            showToast('单词本已经是空的', 'warn');
            return;
        }
        if (!confirm('确定要清空全部 ' + count + ' 个收藏单词吗？此操作不可撤销。')) return;
        state.words = {};
        saveWords();
        updateWordCount();
        renderWordList();
        $$('span.word.collected').forEach(span => span.classList.remove('collected'));
        showToast('已清空全部单词', 'warn');
    }

    function updateWordCount() {
        const n = Object.keys(state.words).length;
        el.wordCount.textContent = n;
        el.drawerWordCount.textContent = n;
    }

    // ==================== 全真题词频索引 ====================
    // 遍历所有真题（完形、阅读、翻译、写作指令、题目与选项）统计每个单词的出现次数
    function buildFrequencyIndex() {
        const total = new Map();
        const perYear = new Map();
        const push = (year, text) => {
            if (!text) return;
            const re = /[A-Za-z][A-Za-z'-]*/g;
            let m;
            while ((m = re.exec(text)) !== null) {
                const t = m[0];
                if (t.length <= 1) continue;
                const key = t.toLowerCase().replace(/[\u2018\u2019]/g, "'");
                total.set(key, (total.get(key) || 0) + 1);
                let ym = perYear.get(key);
                if (!ym) {
                    ym = new Map();
                    perYear.set(key, ym);
                }
                ym.set(year, (ym.get(year) || 0) + 1);
            }
        };
        for (const exam of state.exams) {
            const year = String(exam.year || '');
            for (const section of exam.sections || []) {
                push(year, section.directions);
                push(year, section.passage);
                if (section.cloze_options) {
                    Object.values(section.cloze_options).forEach(opts => {
                        Object.values(opts || {}).forEach(v => push(year, v));
                    });
                }
                for (const part of section.parts || []) {
                    push(year, part.directions);
                    push(year, part.intro);
                    push(year, part.passage);
                    (part.paragraphs || []).forEach(p => push(year, p));
                    for (const t of part.texts || []) {
                        (t.paragraphs || []).forEach(p => push(year, p));
                        for (const q of t.questions || []) {
                            push(year, q.question);
                            if (q.options) {
                                Object.values(q.options).forEach(v => push(year, v));
                            }
                        }
                    }
                }
            }
        }
        state.freq = { total: total, perYear: perYear };
    }

    // ==================== 单词本抽屉 ====================
    function openDrawer() {
        el.wordListDrawer.classList.add('open');
        renderWordList();
        setTimeout(() => el.wordSearch.focus(), 100);
    }

    function closeDrawer() {
        el.wordListDrawer.classList.remove('open');
    }

    function renderWordList() {
        const keyword = (el.wordSearch.value || '').trim().toLowerCase();
        let words = Object.values(state.words);
        if (keyword) {
            words = words.filter(w => w.word.toLowerCase().indexOf(keyword) !== -1);
        }
        const freqOf = (w) => state.freq ? (state.freq.total.get(normalizeWord(w.word)) || 0) : 0;
        if (state.sortMode === 'freq') {
            words.sort((a, b) => (freqOf(b) - freqOf(a)) || ((b.addedAt || 0) - (a.addedAt || 0)));
        } else {
            words.sort((a, b) => (b.addedAt || 0) - (a.addedAt || 0));
        }

        // 汇总统计（基于全部收藏，不受搜索过滤影响）
        const allWords = Object.values(state.words);
        const totalFreq = allWords.reduce((s, w) => s + freqOf(w), 0);
        el.drawerFreqTotal.textContent = allWords.length > 0 ? ' · 累计出现 ' + totalFreq + ' 次' : '';

        if (words.length === 0) {
            el.wordListContainer.innerHTML = '<div class="empty-state">' +
                (keyword ? '没有匹配「' + escapeHtml(keyword) + '」的单词' : '还没有收藏词语<br>进入精翻，双击单词或词组即可收藏') +
                '</div>';
            return;
        }

        const html = words.map(w => {
            const exam = state.exams.find(e => e.exam_id === w.examId);
            const examLabel = exam ? (exam.year + ' ' + exam.subject) : '';
            const key = normalizeWord(w.word);
            const count = state.freq ? (state.freq.total.get(key) || 0) : 0;
            const ym = state.freq ? state.freq.perYear.get(key) : null;
            let freqTitle = '';
            if (ym) {
                const parts = Array.from(ym.entries())
                    .sort((a, b) => (b[0] < a[0] ? -1 : b[0] > a[0] ? 1 : b[1] - a[1]))
                    .map(([y, c]) => y + '×' + c);
                freqTitle = '各年份出现次数：' + parts.join('，');
            }
            const freqHtml = count > 0
                ? '<span class="word-freq" title="' + escapeHtml(freqTitle) + '">' + count + ' 次</span>'
                : '';
            return '<div class="word-list-item">' +
                '<div class="word-item-main"><span class="word-text">' + escapeHtml(w.word) + '</span>' + (w.kind === 'phrase' ? '<span class="precision-kind">词组</span>' : '') + (w.meaning ? '<div class="word-item-meaning">' + escapeHtml(w.meaning) + '</div>' : '') + '</div>' +
                '<div class="word-item-side">' +
                    (examLabel ? '<span class="word-meta">' + escapeHtml(examLabel) + '</span>' : '') +
                    freqHtml +
                    '<button class="word-remove" data-word="' + escapeHtml(w.word) + '" title="删除">' +
                    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>' +
                    '</button>' +
                '</div>' +
                '</div>';
        }).join('');
        el.wordListContainer.innerHTML = html;
    }

    // ==================== 一键复制 ====================
    function copyWords() {
        const words = Object.values(state.words).map(w => w.word);
        if (words.length === 0) {
            showToast('还没有收藏任何单词，无法复制', 'warn');
            return;
        }
        const content = words.join('\n') + '\n';
        const done = () => showToast('已复制 ' + words.length + ' 个单词', 'success');
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(content).then(done).catch(() => {
                fallbackCopyText(content, done);
            });
        } else {
            fallbackCopyText(content, done);
        }
    }

    function fallbackCopyText(text, onDone) {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        let ok = false;
        try {
            ok = document.execCommand('copy');
        } catch (e) {
            ok = false;
        } finally {
            document.body.removeChild(ta);
        }
        if (ok) onDone();
        else showToast('复制失败，请手动选择文本', 'error');
    }

    // ==================== 数据管理（导出 / 导入 / 扫码传递） ====================
    // 电脑端 ↔ 手机端整套数据迁移：收藏单词 + 背词进度 + 设置
    const BACKUP_APP = 'aseeker-english';
    const BACKUP_VERSION = 1;
    const SRS_KEY = 'aseeker_english_srs_v1';
    const SRS_LIMITS_KEY = 'aseeker_english_srs_limits_v1';
    const SRS_TTS_KEY = 'aseeker_english_srs_tts';

    // 本地预览联调：?api=http://127.0.0.1:3010 指向本地后端；生产同源为空
    function apiBase() {
        try {
            return (new URLSearchParams(location.search).get('api') || '').replace(/\/+$/, '');
        } catch (e) {
            return '';
        }
    }

    // 与 correction.js 相同的 Double-Submit：静态站生成并持久化 csrf cookie
    function csrfToken() {
        const m = document.cookie.match(/(?:^|;\s*)csrf=([^;]+)/);
        const token = m ? m[1] : (crypto.randomUUID ? crypto.randomUUID().replace(/-/g, '') : (Math.random().toString(36).slice(2) + Date.now().toString(36)));
        if (!m) document.cookie = 'csrf=' + token + '; path=/; max-age=' + (365 * 24 * 3600) + '; SameSite=Strict';
        return token;
    }

    function gatherBackup() {
        let srs = null;
        try { srs = localStorage.getItem(SRS_KEY) ? JSON.parse(localStorage.getItem(SRS_KEY)) : null; } catch (e) { srs = null; }
        return {
            app: BACKUP_APP,
            kind: 'backup',
            version: BACKUP_VERSION,
            exportedAt: new Date().toISOString(),
            data: {
                words: state.words,
                srs: srs,
                srsLimits: localStorage.getItem(SRS_LIMITS_KEY),
                dblMode: localStorage.getItem(DBL_MODE_KEY),
                tts: localStorage.getItem(SRS_TTS_KEY),
                precision: window.EnglishPrecision ? window.EnglishPrecision.exportData() : null
            }
        };
    }

    function exportBackup() {
        try {
            const payload = JSON.stringify(gatherBackup(), null, 2);
            const url = URL.createObjectURL(new Blob([payload], { type: 'application/json' }));
            const a = document.createElement('a');
            const d = new Date();
            const pad = (n) => String(n).padStart(2, '0');
            a.href = url;
            a.download = 'aseeker-english-backup-' + d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + '.json';
            document.body.appendChild(a);
            a.click();
            setTimeout(() => { URL.revokeObjectURL(url); a.remove(); }, 800);
            showToast('已导出数据文件，发到新设备后导入即可', 'success');
        } catch (err) {
            showToast('导出失败：' + (err && err.message ? err.message : err), 'error');
        }
    }

    /** 校验并写入备份对象；确认后重载。fromCode：导入成功后清理 URL 参数 */
    async function applyBackupData(obj, fromCode) {
        if (!obj || obj.app !== BACKUP_APP || obj.kind !== 'backup' || !obj.data || typeof obj.data !== 'object') {
            showToast('这不是英语站的备份数据', 'error');
            return false;
        }
        const words = obj.data.words && typeof obj.data.words === 'object' ? obj.data.words : null;
        const srs = obj.data.srs && typeof obj.data.srs === 'object' ? obj.data.srs : null;
        if (!words && !srs) {
            showToast('备份里没有可导入的数据', 'error');
            return false;
        }
        const wc = words ? Object.keys(words).length : 0;
        const sc = srs && srs.cards ? Object.keys(srs.cards).length : 0;
        const sentenceCount = obj.data.precision && Array.isArray(obj.data.precision.sentences) ? obj.data.precision.sentences.length : 0;
        const ok = confirm(
            '将把备份数据导入到本设备：\n\n· 收藏单词 ' + wc + ' 个\n· 背词进度 ' + sc + ' 张卡片\n· 长难句 ' + sentenceCount + ' 条（备份有此项时导入）\n· 设置（精翻 / 每日上限等）\n\n' +
            '导入会覆盖本设备的当前数据，继续？'
        );
        if (!ok) return false;
        try {
            if (words) localStorage.setItem(STORAGE_KEY_WORDS, JSON.stringify(words));
            if (srs) localStorage.setItem(SRS_KEY, JSON.stringify(srs));
            if (typeof obj.data.srsLimits === 'string') localStorage.setItem(SRS_LIMITS_KEY, obj.data.srsLimits);
            if (obj.data.dblMode === 'translate' || obj.data.dblMode === 'collect') localStorage.setItem(DBL_MODE_KEY, obj.data.dblMode);
            if (obj.data.tts === '1' || obj.data.tts === '0') localStorage.setItem(SRS_TTS_KEY, obj.data.tts);
            if (obj.data.precision && window.EnglishPrecision) window.EnglishPrecision.importData(obj.data.precision);
            if (fromCode) {
                try {
                    const u = new URL(location.href);
                    u.searchParams.delete('import');
                    history.replaceState(null, '', u.pathname + u.search + u.hash);
                } catch (e) { /* ignore */ }
            }
            sessionStorage.setItem('aseeker_backup_imported', '1');
            location.reload();
            return true;
        } catch (e) {
            showToast('导入写入失败：' + (e && e.message ? e.message : e), 'error');
            return false;
        }
    }

    async function importBackup(file) {
        if (!file) return;
        let obj = null;
        try {
            obj = JSON.parse(await file.text());
        } catch (e) {
            showToast('文件无法解析：不是有效的备份 JSON', 'error');
            return;
        }
        await applyBackupData(obj, false);
    }

    /** 扫一扫打开 ?import=<code>：拉取一次性备份并导入 */
    async function handleImportByUrl() {
        let code = null;
        try {
            code = new URLSearchParams(location.search).get('import');
        } catch (e) { /* ignore */ }
        if (!code || !/^[A-Za-z0-9_-]{6,16}$/.test(code)) return;
        try {
            const r = await fetch(apiBase() + '/biochem/api/backup/' + encodeURIComponent(code) + '/');
            const j = await r.json().catch(() => ({}));
            if (!r.ok || !j.ok || typeof j.data !== 'string') {
                showToast('链接已失效（可能已被使用，或超过 24 小时）', 'error');
                try {
                    const u = new URL(location.href);
                    u.searchParams.delete('import');
                    history.replaceState(null, '', u.pathname + u.search + u.hash);
                } catch (e) { /* ignore */ }
                return;
            }
            const obj = JSON.parse(j.data);
            await applyBackupData(obj, true);
        } catch (e) {
            showToast('导入失败：' + (e && e.message ? e.message : e), 'error');
        }
    }

    /** 扫码传递：备份上传到中转，生成二维码 URL */
    async function scanShare() {
        const btn = document.getElementById('scanShareBtn');
        const resultEl = document.getElementById('scanResult');
        const qrEl = document.getElementById('scanQr');
        try {
            if (btn) { btn.disabled = true; btn.textContent = '生成中…'; }
            if (qrEl) qrEl.innerHTML = '';
            const payload = JSON.stringify(gatherBackup());
            const r = await fetch(apiBase() + '/biochem/api/backup/', {
                method: 'POST',
                credentials: 'include',
                headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': csrfToken() },
                body: JSON.stringify({ data: payload })
            });
            const j = await r.json().catch(() => ({}));
            if (!r.ok || !j.ok || !j.url) throw new Error((j && j.error) || ('HTTP ' + r.status));
            if (qrEl && typeof qrcode === 'function') {
                const qr = qrcode(0, 'L');
                qr.addData(j.url);
                qr.make();
                qrEl.innerHTML = qr.createImgTag(6, 8);
            }
            if (qrEl) {
                const link = document.createElement('div');
                link.className = 'scan-link';
                const a = document.createElement('a');
                a.href = j.url;
                a.target = '_blank';
                a.rel = 'noopener';
                a.textContent = j.url;
                link.appendChild(a);
                qrEl.appendChild(link);
            }
            if (resultEl) resultEl.style.display = '';
            showToast('二维码已生成，手机扫一扫即可导入', 'success');
        } catch (err) {
            showToast('生成失败：' + (err && err.message ? err.message : err), 'error');
        } finally {
            if (btn) { btn.disabled = false; btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect><path d="M14 14h3v3h-3zM20 14h1M14 20h1M18 18h3v3h-3z"></path></svg><span>扫码传递（手机扫一扫即导入）</span>'; }
        }
    }

    // ==================== 真题渲染 ====================
    function renderClickableText(text) {
        if (!text) return '';
        text = text.replace(/[\u2018\u2019]/g, "'");
        const regex = /[A-Za-z][A-Za-z'-]*/g;
        let result = '';
        let lastIndex = 0;
        let m;
        while ((m = regex.exec(text)) !== null) {
            if (m.index > lastIndex) {
                result += escapeHtml(text.slice(lastIndex, m.index));
            }
            const token = m[0];
            if (token.length > 1) {
                const collected = isCollected(token) ? ' collected' : '';
                result += '<span class="word' + collected + '" data-word="' + escapeHtml(token) + '">' + escapeHtml(token) + '</span>';
            } else {
                result += escapeHtml(token);
            }
            lastIndex = regex.lastIndex;
        }
        if (lastIndex < text.length) {
            result += escapeHtml(text.slice(lastIndex));
        }
        return result;
    }

    // Part B 段落/选项段的字母标记：[A] / A. / B、 / A)（与 corpus.strip_option_prefix 同口径）。
    // 有标记 → 渲染成 .choice-letter badge + .choice-body（正文不含标记，划词文本=句库键）；
    // 没标记 → 当普通段落渲染。
    const CHOICE_MARK_RE = /^\s*(?:[\[（(]\s*([A-Ha-h])\s*[\]）)][.、．]?|([A-Ha-h])\s*[.、．)）])\s*([\s\S]*)$/;

    // 匹配题（英二 Part B）的数据把「左栏题干 | [答] 右栏选项」拼在一个段落里，
    // 标记落在**正文中部**；上面的 CHOICE_MARK_RE 只认开头，剥不掉，于是正文和译文里
    // 都留着字面「| [B]」/「| B.」（用户反馈 english_corrections #25 问的就是这个中括号）。
    // 全库真题数据里 '|' 一共只出现 30 次，全部是这种标记，所以可以放心地按 '|' 剥离。
    // 规则：[B] 形式 → 换成空格（题干与选项本就连成一句）；
    //       B. 形式 → 换成句号（题干是"人名"这类独立成分，选项是另一句）。
    // **句库里的键必须用同一条规则同步处理**，否则点词查不到。
    const MID_MARK_RE = /\s*\|\s*(?:[\[（(]\s*([A-Ha-h])\s*[\]）)]|([A-Ha-h]))\s*([.、．)）]?)\s*/g;
    function stripMidMark(s) {
        return String(s == null ? '' : s).replace(MID_MARK_RE, (m, br, bare, dot) => ((br || !dot) ? ' ' : '. ')).trim();
    }

    /** 完形 / Part C 正文分段。
     *
     *  数据里的 `\n\n` 不可靠：165 处里 9 处落在句子中间（源文本硬换行），而有的整篇
     *  只有 2 段（2010 英一 1537 字符 → 两堵 684/851 的墙；用户反馈 #59「为啥没分段落」）。
     *  规则：① 落在句子中间的换行并回上一段（判据：上一段没以句末标点收尾）；
     *        ② 过长的段落再按**真句末标点**切开——切点只在句号之后，绝不切进句子
     *           （句库是按句存的，切进句子就会查不到）。 */
    function passageParagraphs(raw) {
        const text = String(raw == null ? '' : raw);
        const joined = [];
        for (const chunk of text.split(/\n{2,}/)) {
            const t = chunk.replace(/\s+/g, ' ').trim();
            if (!t) continue;
            const prev = joined[joined.length - 1];
            if (prev && !/[.!?]["'\u201d\u2019)\]]*$/.test(prev)) joined[joined.length - 1] = prev + ' ' + t;
            else joined.push(t);
        }
        return joined.length ? joined : [text.trim()];
    }

    function renderChoiceParagraph(text) {
        const raw = stripMidMark(text);
        const m = raw.match(CHOICE_MARK_RE);
        if (!m) {
            return '<p class="paragraph-option">' + renderClickableText(raw) + '</p>';
        }
        const letter = (m[1] || m[2] || '').toUpperCase();
        const body = m[3] || '';
        return '<p class="paragraph-option choice">' +
            '<span class="choice-letter">' + escapeHtml(letter) + '</span>' +
            '<span class="choice-body">' + renderClickableText(body) + '</span></p>';
    }

    function renderOptionsObj(optionsObj) {
        let html = '<div class="options">';
        Object.keys(optionsObj).forEach(letter => {
            html += '<div class="option"><span class="option-letter">' + escapeHtml(letter) + '</span>' +
                renderClickableText(optionsObj[letter]) + '</div>';
        });
        html += '</div>';
        return html;
    }

    function renderOptionsInline(optionsObj) {
        let html = '';
        Object.keys(optionsObj).forEach(letter => {
            html += '<span class="option-inline"><span class="option-letter">' + escapeHtml(letter) + '</span>' +
                renderClickableText(optionsObj[letter]) + '</span>';
        });
        return html;
    }

    function renderQuestions(questions) {
        let html = '';
        (questions || []).forEach(q => {
            html += '<div class="question-block">';
            html += '<div class="question-text"><span class="question-num">' + escapeHtml(q.q_num) + '.</span>' +
                renderClickableText(q.question) + '</div>';
            if (q.options) {
                html += renderOptionsObj(q.options);
            }
            html += '</div>';
        });
        return html;
    }

    function renderExam(exam) {
        let html = '';

        html += '<div class="exam-title-block">' +
            '<h2>' + escapeHtml(exam.title || (exam.year + ' ' + exam.subject)) + '</h2>' +
            '<div class="exam-meta">' + escapeHtml(exam.year || '') + ' · ' + escapeHtml(exam.subject || '') +
            (exam.code ? ' · 科目代码 ' + escapeHtml(exam.code) : '') + '</div>' +
            '</div>';

        html += '<div class="hint-bar">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>' +
            '进入精翻后：单击查义 · 双击收藏 · 选中后翻译或右键收藏长难句' +
            '</div>';

        (exam.sections || []).forEach(section => {
            html += '<div class="section-block">';
            html += '<h3 class="section-title">' + escapeHtml(section.title || '') + '</h3>';

            if (section.directions) {
                html += '<div class="directions">' + renderClickableText(section.directions) + '</div>';
            }

            if (section.passage) {
                passageParagraphs(section.passage).forEach(p => {
                    html += '<p class="paragraph">' + renderClickableText(p) + '</p>';
                });
            }

            if (section.cloze_options) {
                html += '<div class="cloze-options">';
                html += '<h4 class="sub-title">完形填空选项</h4>';
                html += '<div class="cloze-grid">';
                Object.keys(section.cloze_options).forEach(num => {
                    const opts = section.cloze_options[num];
                    html += '<div class="cloze-item">' +
                        '<span class="cloze-q-num">' + escapeHtml(num) + '.</span>' +
                        '<span class="cloze-opts">' + renderOptionsInline(opts) + '</span>' +
                        '</div>';
                });
                html += '</div></div>';
            }

            if (section.parts) {
                section.parts.forEach(part => {
                    html += '<h4 class="part-title">' + escapeHtml(part.title || '') + '</h4>';

                    if (part.directions) {
                        html += '<div class="directions">' + renderClickableText(part.directions) + '</div>';
                    }

                    if (part.texts) {
                        part.texts.forEach(text => {
                            html += '<h5 class="text-title">' + escapeHtml(text.title || '') + '</h5>';
                            passageParagraphs((text.paragraphs || []).join('\n\n')).forEach(p => {
                                html += '<p class="paragraph">' + renderClickableText(p) + '</p>';
                            });
                            html += renderQuestions(text.questions);
                        });
                    }

                    if (part.paragraphs && /Part\s*B/i.test(part.title || '')) {
                        if (part.intro) {
                            html += '<p class="paragraph intro">' + renderClickableText(part.intro) + '</p>';
                        }
                        html += '<div class="paragraph-options">';
                        // Part B 段落（7 选 5 的 A–G 段、完型填句段）：数据里带 "[A] " 标记，
                        // 旧代码把它当正文渲染 → 用户看到 "[A] ..." 中括号（纠错 #25
                        // 「这块 为什么要有中括号」）。统一走 renderChoiceParagraph：
                        // 字母进 badge（划选/点选到的正文不含标记，与句库键一致），
                        // 译文里也不会再出现「[A] 保持谦逊」。
                        part.paragraphs.forEach(p => {
                            html += renderChoiceParagraph(p);
                        });
                        // Part B 的选择项（A–G 小标题）：同一套处理
                        (part.paragraph_options || []).forEach(opt => {
                            html += renderChoiceParagraph(opt);
                        });
                        html += '</div>';
                    }

                    if (part.passage && /Part\s*C/i.test(part.title || '')) {
                        passageParagraphs(part.passage).forEach(p => {
                            html += '<p class="paragraph">' + renderClickableText(p) + '</p>';
                        });
                    }
                });
            }

            html += '</div>';
        });

        el.examContent.innerHTML = html;
        if (window.EnglishPrecision) window.EnglishPrecision.onRendered(exam);
    }

    // ==================== 真题列表 ====================
    function loadGroupState() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_GROUPS);
            return raw ? JSON.parse(raw) : {};
        } catch (e) {
            return {};
        }
    }

    // ==================== 侧栏「使用提示」折叠 ====================
    // PC 端侧栏高度锁在 100vh-116px：提示卡若始终自然高度(≈533px)，
    // 会把上面的真题列表挤成 ~80px 的滚动条。所以 PC 默认收起提示，
    // 用户手动展开过就记住；移动端侧栏是静态流式布局，默认展开。
    let tipOpenPref = null;

    function loadTipOpen() {
        try {
            const v = localStorage.getItem(STORAGE_KEY_TIP_OPEN);
            if (v === '1') return true;
            if (v === '0') return false;
        } catch (e) { /* ignore */ }
        return null;
    }

    function saveTipOpen(open) {
        try {
            localStorage.setItem(STORAGE_KEY_TIP_OPEN, open ? '1' : '0');
        } catch (e) { /* ignore */ }
    }

    function applyTipOpen(open) {
        const section = $('#tipSection');
        if (!section) return;
        section.classList.toggle('open', !!open);
        const toggle = $('#tipToggle');
        if (toggle) {
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            toggle.setAttribute('title', open ? '收起使用提示' : '展开使用提示');
        }
        const body = $('#tipBody');
        if (body) body.setAttribute('aria-hidden', open ? 'false' : 'true');
    }

    /** 初始化折叠态；返回当前是否展开。 */
    function initTipCollapse() {
        tipOpenPref = loadTipOpen();
        // 兜底：提示头不存在（旧缓存页面）时全展开，别把内容藏死
        const toggle = $('#tipToggle');
        if (!toggle) {
            const section = $('#tipSection');
            if (section) section.classList.add('open');
            return true;
        }
        const isPC = window.matchMedia('(min-width: 961px)').matches;
        const open = tipOpenPref !== null ? tipOpenPref : !isPC;
        applyTipOpen(open);
        toggle.addEventListener('click', () => {
            const section = $('#tipSection');
            const next = !(section && section.classList.contains('open'));
            tipOpenPref = next;
            saveTipOpen(next);
            applyTipOpen(next);
        });
        return open;
    }

    // 窗口在 PC/移动之间跨越时重算（用户显式选择过就尊重选择）
    window.addEventListener('resize', () => {
        if (tipOpenPref !== null) return;
        applyTipOpen(!window.matchMedia('(min-width: 961px)').matches);
    });

    function saveGroupState() {
        try {
            localStorage.setItem(STORAGE_KEY_GROUPS, JSON.stringify(state.groupOpen || {}));
        } catch (e) {}
    }

    function renderExamList() {
        if (state.exams.length === 0) {
            el.examList.innerHTML = '<div class="empty-state">还没有真题</div>';
            return;
        }
        // 按科目分组：英语（一）/ 英语（二）优先，其余按字典序
        const groups = {};
        state.exams.forEach(exam => {
            const key = exam.subject || '其他真题';
            if (!groups[key]) groups[key] = [];
            groups[key].push(exam);
        });
        const preferred = ['英语（一）', '英语（二）'];
        const keys = Object.keys(groups).sort((a, b) => {
            const ia = preferred.indexOf(a);
            const ib = preferred.indexOf(b);
            return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
        });
        if (!state.groupOpen) state.groupOpen = loadGroupState();
        let html = '';
        keys.forEach(key => {
            const exams = groups[key];
            const open = state.groupOpen[key] === true;
            html += '<div class="exam-group' + (open ? '' : ' collapsed') + '" data-group="' + escapeHtml(key) + '">' +
                '<div class="exam-group-title" role="button" tabindex="0" title="' + (open ? '收起' : '展开') + '">' +
                '<span class="exam-group-toggle">' +
                '<span class="exam-group-arrow" aria-hidden="true"></span>' +
                '<span class="exam-group-name">' + escapeHtml(key) + '</span>' +
                '</span>' +
                '<span class="exam-group-count">' + exams.length + '套</span>' +
                '</div>';
            exams.forEach(exam => {
                const active = exam.exam_id === state.activeExamId ? ' active' : '';
                const builtin = exam.builtin ? '<span class="badge-builtin">内置</span>' : '';
                html += '<div class="exam-item' + active + '" data-exam-id="' + escapeHtml(exam.exam_id) + '">' +
                    '<div class="exam-item-main">' +
                    '<div class="exam-item-year">' + escapeHtml(exam.year) + '</div>' +
                    '<div class="exam-item-sub">' + (builtin || escapeHtml(exam.subject)) + '</div>' +
                    '</div>' +
                    (exam.builtin ? '' : '<button class="exam-del" data-exam-id="' + escapeHtml(exam.exam_id) + '" title="删除真题">' +
                        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>' +
                        '</button>') +
                    '</div>';
            });
            html += '</div>';
        });
        el.examList.innerHTML = html;
    }

    function selectExam(examId) {
        state.activeExamId = examId;
        saveActiveExamId();
        const exam = state.exams.find(e => e.exam_id === examId);
        if (exam) {
            renderExam(exam);
        } else {
            el.examContent.innerHTML = '<div class="empty-state">未找到真题</div>';
        }
        renderExamList();
    }

    function deleteExam(examId) {
        const exam = state.exams.find(e => e.exam_id === examId);
        if (!exam) return;
        if (exam.builtin) {
            showToast('内置真题不可删除', 'warn');
            return;
        }
            if (!confirm('确定删除「' + exam.year + ' ' + exam.subject + '」真题吗？\n（已收藏的单词不会被删除）')) return;
            state.exams = state.exams.filter(e => e.exam_id !== examId);
            saveExams();
            buildFrequencyIndex();
            if (state.activeExamId === examId) {
                const first = state.exams[0];
            if (first) {
                selectExam(first.exam_id);
            } else {
                state.activeExamId = null;
                el.examContent.innerHTML = '<div class="empty-state">还没有真题</div>';
            }
        }
        renderExamList();
        showToast('已删除真题', 'warn');
    }

    // ==================== 上传真题 ====================
    let mammothPromise = null;
    function loadMammoth() {
        if (typeof mammoth !== 'undefined') return Promise.resolve();
        if (!mammothPromise) {
            mammothPromise = new Promise(function (resolve, reject) {
                const s = document.createElement('script');
                s.src = 'js/mammoth.browser.min.js';
                s.onload = function () {
                    if (typeof mammoth === 'undefined') {
                        mammothPromise = null;
                        reject(new Error('解析库加载失败，请刷新后重试'));
                    } else {
                        resolve();
                    }
                };
                s.onerror = function () {
                    mammothPromise = null;
                    reject(new Error('解析库加载失败，请检查网络后重试'));
                };
                document.head.appendChild(s);
            });
        }
        return mammothPromise;
    }

    function openUploadModal() {
        el.uploadModal.classList.add('open');
        el.fileInput.value = '';
        el.uploadForm.style.display = 'none';
        el.uploadStatus.style.display = 'none';
        el.uploadStatus.textContent = '';
        el.uploadStatus.className = 'upload-status';
        el.uploadConfirm.disabled = true;
        state.pendingUpload = null;
        // 打开上传窗口时预加载解析库，选文件期间通常已就绪
        loadMammoth().catch(function () {});
    }

    function closeUploadModal() {
        el.uploadModal.classList.remove('open');
    }

    // 真题详解弹窗
    const MATERIALS_BASE = '/english-materials/';

    function formatSize(bytes) {
        if (bytes < 1024) return bytes + ' B';
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / 1024 / 1024).toFixed(1) + ' MB';
    }

    function buildMaterialsList() {
        if (!el.materialsList) return;
        if (el.materialsList.children.length > 0) return;
        fetch(MATERIALS_BASE + 'manifest.json?v=' + Date.now())
            .then(r => {
                if (!r.ok) throw new Error('HTTP ' + r.status);
                return r.json();
            })
            .then(files => {
                const yingyi = files.filter(f => f.name.includes('英一'));
                const yinger = files.filter(f => f.name.includes('英二'));
                const groups = [
                    { label: '英语一', items: yingyi },
                    { label: '英语二', items: yinger }
                ];
                el.materialsList.innerHTML = '';
                groups.forEach(g => {
                    if (!g.items.length) return;
                    const title = document.createElement('div');
                    title.className = 'materials-group-title';
                    title.textContent = g.label + '（' + g.items.length + ' 份）';
                    el.materialsList.appendChild(title);
                    g.items.forEach(file => {
                        const a = document.createElement('a');
                        a.className = 'material-item';
                        a.href = file.url || (MATERIALS_BASE + encodeURIComponent(file.name));
                        a.download = file.name;
                        a.target = '_blank';
                        a.innerHTML = '<div class="material-item-left">' +
                            '<span class="material-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></span>' +
                            '<span class="material-name">' + file.name.replace(/\.pdf$/i, '') + '</span>' +
                            '</div>' +
                            '<span class="material-size">' + formatSize(file.size) + '</span>' +
                            '<span class="material-dl"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></span>';
                        el.materialsList.appendChild(a);
                    });
                });
            })
            .catch(err => {
                el.materialsList.innerHTML = '<p style="text-align:center;color:var(--text-faint);padding:20px;">加载失败：' + (err.message || '未知错误') + '</p>';
            });
    }

    function openMaterialsModal() {
        el.materialsModal.classList.add('open');
        buildMaterialsList();
    }

    function closeMaterialsModal() {
        el.materialsModal.classList.remove('open');
    }

    // 交个朋友（微信二维码）
    function openFriendModal() {
        // 二维码 130 KB：HTML 里只放 data-src，真正打开弹窗时才赋值下载
        //（弹窗是 visibility:hidden、仍在视口里有盒子，所以 loading="lazy" 拦不住它）
        try {
            const qr = document.querySelector('#friendModal .friend-qr');
            if (qr && !qr.getAttribute('src') && qr.getAttribute('data-src')) {
                qr.setAttribute('src', qr.getAttribute('data-src'));
            }
        } catch (e) { /* ignore */ }
        if (el.friendModal) el.friendModal.classList.add('open');
    }

    function closeFriendModal() {
        if (el.friendModal) el.friendModal.classList.remove('open');
    }

    async function handleFile(file) {
        if (!file) return;
        const name = file.name.toLowerCase();
        if (!name.endsWith('.docx') && !name.endsWith('.doc')) {
            showUploadStatus('请上传 .docx 格式的文件', 'error');
            return;
        }
        showUploadStatus('正在加载解析库...', 'loading');
        try {
            await loadMammoth();
        } catch (err) {
            showUploadStatus(err.message || '解析库加载失败', 'error');
            return;
        }
        showUploadStatus('正在解析文档...', 'loading');

        const reader = new FileReader();
        reader.onload = function (e) {
            const arrayBuffer = e.target.result;
            if (typeof mammoth === 'undefined') {
                showUploadStatus('解析库未加载，请检查网络连接后重试', 'error');
                return;
            }
            mammoth.extractRawText({ arrayBuffer: arrayBuffer })
                .then(result => {
                    const text = result.value;
                    if (!text || text.trim().length === 0) {
                        showUploadStatus('文档内容为空', 'error');
                        return;
                    }
                    const yearMatch = file.name.match(/(20\d{2})/);
                    const guessedYear = yearMatch ? yearMatch[1] : '';
                    if (guessedYear && !el.uploadYear.value) {
                        el.uploadYear.value = guessedYear;
                    }
                    state.pendingUpload = { text: text, fileName: file.name };
                    el.uploadForm.style.display = 'block';
                    showUploadStatus('文档解析成功，共 ' + text.length + ' 字符。请填写年份和科目后确认。', 'success');
                    el.uploadConfirm.disabled = false;
                })
                .catch(err => {
                    showUploadStatus('解析失败：' + (err.message || err), 'error');
                });
        };
        reader.onerror = function () {
            showUploadStatus('文件读取失败', 'error');
        };
        reader.readAsArrayBuffer(file);
    }

    function showUploadStatus(msg, type) {
        el.uploadStatus.style.display = 'block';
        el.uploadStatus.textContent = msg;
        el.uploadStatus.className = 'upload-status ' + type;
    }

    function confirmUpload() {
        if (!state.pendingUpload) return;
        const year = (el.uploadYear.value || '').trim();
        const subject = el.uploadSubject.value;
        if (!year) {
            showToast('请填写年份', 'error');
            el.uploadYear.focus();
            return;
        }
        const examId = 'upload_' + year + '_' + subject + '_' + Date.now();
            const exam = parseUploadedText(state.pendingUpload.text, year, subject, examId);
            state.exams.push(exam);
            saveExams();
            buildFrequencyIndex();
            closeUploadModal();
            selectExam(examId);
        showToast('已添加 ' + year + ' ' + subject + ' 真题', 'success');
    }

    // ==================== OCR 修复 ====================
    function fixOcrErrors(text) {
        const fixes = [
            [/\[BJ\]/g, '[B]'],
            [/\[EJ\]/g, '[E]'],
            [/\[GJ\]/g, '[G]'],
            [/\[q\]/g, '[C]'],
            [/\[Cl/g, '[C]'],
            [/\[A\]ccording/g, 'According'],
            [/\[C\]onsumers/g, 'Consumers'],
            [/\[C\]ircumstances/g, 'Circumstances'],
            [/\[T\]oyota/g, 'Toyota'],
            [/\(lOpoints\)/g, '(10 points)'],
            [/\(lO points\)/g, '(10 points)'],
            [/ofreaders/g, 'of readers'],
            [/ofinfluentials/g, 'of influentials'],
            [/ofthis/g, 'of this'],
            [/ofjournalistic/g, 'of journalistic'],
            [/ofknowledge/g, 'of knowledge'],
            [/ofa /g, 'of a '],
            [/ofthe /g, 'of the '],
            [/ofrecordings/g, 'of recordings'],
            [/th an /g, 'than '],
            [/t rying/g, 'trying'],
            [/h appen/g, 'happen'],
            [/p arts/g, 'parts'],
            [/p arents/g, 'parents'],
            [/s ame/g, 'same'],
            [/th at/g, 'that'],
            [/w ant/g, 'want'],
            [/morn-and-pop/g, 'mom-and-pop'],
            [/Joumalistic/g, 'Journalistic'],
            [/modem/g, 'modern'],
            [/tum /g, 'turn '],
            [/Wilrzburg/g, 'Würzburg'],
            [/lQ_/g, '16'],
            [/function ing/g, 'functioning'],
            [/opposingtrends/g, 'opposing trends'],
            [/verybig/g, 'very big'],
            [/a  re /g, 'are '],
            [/5 1\./g, '51.'],
            [/微\s*信\s*公\s*众\s*号[：:][^\n]*/g, ''],
            [/全年资料免费分享/g, ''],
            [/神仙小土豆/g, ''],
            [/南山小[^\n]*/g, ''],
        ];
        let out = text;
        for (const [pat, rep] of fixes) { out = out.replace(pat, rep); }
        return out;
    }

    // 从一行文本中提取所有 [X] 选项标记和内容
    function extractOptionsFromLine(line) {
        const opts = [];
        const regex = /\[([A-G])\]\s*([^[]+)/g;
        let m;
        while ((m = regex.exec(line)) !== null) {
            opts.push({ letter: m[1], text: m[2].trim() });
        }
        return opts;
    }

    // 将上传的纯文本解析为真题结构（增强版）
    function parseUploadedText(rawText, year, subject, examId) {
        let text = fixOcrErrors(rawText);
        text = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
        let lines = text.split('\n').map(l => l.trim()).filter(l => l.length > 0);

        // 合并被错误断行的句子
        const merged = [];
        for (let i = 0; i < lines.length; i++) {
            let cur = lines[i];
            const isStructural = /^(Section\s+[IVX]+|Part\s*[A-C]|Text\s*\d+|Directions:?|Read\s+the\s+following)/i.test(cur);
            const isQuestion = /^\d{1,2}\.\s/.test(cur);
            const isOptionOnly = /^\[[A-G]\]\s/.test(cur) && !/^\d/.test(cur);
            while (i + 1 < lines.length) {
                const next = lines[i + 1];
                const nextIsStructural = /^(Section\s+[IVX]+|Part\s*[A-C]|Text\s*\d+|Directions:?)/i.test(next);
                const nextIsQuestion = /^\d{1,2}\.\s/.test(next);
                const nextIsOption = /^\[[A-G]\]\s/.test(next);
                const nextIsTranslation = /^\(\d{2}\)/.test(next);
                if (isStructural || isQuestion || isOptionOnly) break;
                if (nextIsStructural || nextIsQuestion || nextIsOption || nextIsTranslation) break;
                if (/[.?!":]\s*$/.test(cur)) break;
                if (/\s\d+\s*$/.test(cur)) break;
                cur = cur + ' ' + next;
                i++;
            }
            merged.push(cur);
        }
        lines = merged;

        const exam = {
            exam_id: examId, year: year, subject: subject,
            title: year + '年考研' + subject + '真题',
            sections: [], builtin: false
        };

        let currentSection = null;
        let currentPart = null;
        let currentText = null;
        let pendingDirections = null;
        let allQuestions = [];
        let pendingQuestion = null;

        function flushPendingQuestion() {
            if (pendingQuestion) { allQuestions.push(pendingQuestion); pendingQuestion = null; }
        }

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];

            if (/^Section\s+[IVX]+\b/i.test(line)) {
                flushPendingQuestion();
                currentSection = { section_id: 'sec_' + exam.sections.length, title: line, parts: [] };
                exam.sections.push(currentSection);
                currentPart = null; currentText = null;
                continue;
            }
            if (/^Part\s*[A-C]\b/i.test(line)) {
                flushPendingQuestion();
                if (!currentSection) {
                    currentSection = { section_id: 'sec_' + exam.sections.length, title: 'Section', parts: [] };
                    exam.sections.push(currentSection);
                }
                const title = line.replace(/\s+/g, ' ').replace('PartB', 'Part B').replace('PartC', 'Part C');
                currentPart = { part_id: 'part_' + (currentSection.parts.length + 1), title: title };
                currentSection.parts.push(currentPart);
                currentText = null;
                continue;
            }
            if (/^Text\s*\d+/i.test(line)) {
                flushPendingQuestion();
                if (currentPart) {
                    currentText = {
                        text_id: 'text_' + ((currentPart.texts ? currentPart.texts.length : 0) + 1),
                        title: line.replace(/\s+/g, ' ').trim(),
                        paragraphs: [], questions: []
                    };
                    if (!currentPart.texts) currentPart.texts = [];
                    currentPart.texts.push(currentText);
                }
                continue;
            }
            if (/^Directions:?\s*$/i.test(line)) {
                pendingDirections = currentPart ? 'part' : (currentSection ? 'section' : null);
                continue;
            }

            // 完形填空选项：1. [A] xxx [B] yyy ...
            const clozeMatch = line.match(/^(\d{1,2})\.\s*\[([A-D])\]\s*(.+)/);
            if (clozeMatch && currentSection && /Section\s*I\b/i.test(currentSection.title)) {
                flushPendingQuestion();
                if (!currentSection.cloze_options) currentSection.cloze_options = {};
                const qNum = clozeMatch[1];
                const opts = extractOptionsFromLine(line);
                currentSection.cloze_options[qNum] = {};
                opts.forEach(o => {
                    if (/[A-D]/.test(o.letter)) currentSection.cloze_options[qNum][o.letter] = o.text;
                });
                continue;
            }
            // 完形选项续行：[B] xxx [C] yyy [D] www
            if (/^\[[A-D]\]\s/.test(line) && currentSection && /Section\s*I\b/i.test(currentSection.title) && currentSection.cloze_options) {
                const qNums = Object.keys(currentSection.cloze_options);
                if (qNums.length > 0) {
                    const lastNum = qNums[qNums.length - 1];
                    const opts = extractOptionsFromLine(line);
                    opts.forEach(o => {
                        if (/[A-D]/.test(o.letter) && !currentSection.cloze_options[lastNum][o.letter]) {
                            currentSection.cloze_options[lastNum][o.letter] = o.text;
                        }
                    });
                    continue;
                }
            }

            // 阅读题题干：21. xxx 或 21.xxx
            const readingQMatch = line.match(/^(2[1-9]|3[0-9]|4[0-5])\.\s*(.+)/);
            if (readingQMatch) {
                flushPendingQuestion();
                const num = readingQMatch[1];
                const rest = readingQMatch[2];
                const inlineOpts = extractOptionsFromLine(rest);
                let questionText = rest;
                pendingQuestion = { q_num: num, question: '', options: {} };
                if (inlineOpts.length > 0) {
                    const firstBracket = rest.indexOf('[');
                    questionText = rest.substring(0, firstBracket).trim();
                    inlineOpts.forEach(o => {
                        if (/[A-D]/.test(o.letter)) pendingQuestion.options[o.letter] = o.text;
                    });
                }
                pendingQuestion.question = questionText;
                continue;
            }
            // 阅读题选项续行
            if (/^\[[A-D]\]\s/.test(line) && pendingQuestion) {
                const opts = extractOptionsFromLine(line);
                opts.forEach(o => {
                    if (/[A-D]/.test(o.letter) && !pendingQuestion.options[o.letter]) {
                        pendingQuestion.options[o.letter] = o.text;
                    }
                });
                continue;
            }

            // Part B 段落选项 [A] xxx
            if (/^\[[A-G]\]\s/.test(line) && currentPart && /Part\s*B/i.test(currentPart.title)) {
                flushPendingQuestion();
                if (!currentPart.paragraphs) currentPart.paragraphs = [];
                currentPart.paragraphs.push(line);
                continue;
            }

            // Part C 翻译句标记 (46) (47) ...
            if (/^\(\d{2}\)/.test(line) && currentPart && /Part\s*C/i.test(currentPart.title)) {
                flushPendingQuestion();
                if (!currentPart.passage) currentPart.passage = '';
                currentPart.passage += (currentPart.passage ? '\n\n' : '') + line;
                continue;
            }

            // Writing 题号：51. 52.
            const writingMatch = line.match(/^(5[1-2])\.\s*(.+)/);
            if (writingMatch && currentPart && /Part\s*[AB]/i.test(currentPart.title)) {
                flushPendingQuestion();
                currentPart.directions = (currentPart.directions ? currentPart.directions + ' ' : '') + line;
                continue;
            }

            // Directions 内容
            if (pendingDirections === 'part' && currentPart) {
                currentPart.directions = (currentPart.directions ? currentPart.directions + ' ' : '') + line;
                pendingDirections = null;
                continue;
            }
            if (pendingDirections === 'section' && currentSection) {
                currentSection.directions = (currentSection.directions ? currentSection.directions + ' ' : '') + line;
                pendingDirections = null;
                continue;
            }

            // 普通正文段落
            flushPendingQuestion();

            // Section I 完形文章
            if (currentSection && /Section\s*I\b/i.test(currentSection.title)) {
                if (!currentSection.passage) currentSection.passage = '';
                currentSection.passage += (currentSection.passage ? '\n\n' : '') + line;
                continue;
            }
            // Part C 翻译文章
            if (currentPart && /Part\s*C/i.test(currentPart.title)) {
                if (!currentPart.passage) currentPart.passage = '';
                currentPart.passage += (currentPart.passage ? '\n\n' : '') + line;
                continue;
            }
            // Text 段落
            if (currentText) { currentText.paragraphs.push(line); continue; }
            // Part 段落
            if (currentPart) {
                if (!currentPart.paragraphs) currentPart.paragraphs = [];
                currentPart.paragraphs.push(line);
                continue;
            }
            // Section 段落
            if (currentSection) {
                if (!currentSection.passage) currentSection.passage = '';
                currentSection.passage += (currentSection.passage ? '\n\n' : '') + line;
                continue;
            }
        }

        flushPendingQuestion();

        // 把散落的阅读题按题号分配给 Text
        if (allQuestions.length > 0) {
            let partA = null;
            for (const s of exam.sections) {
                if (s.parts) {
                    for (const p of s.parts) {
                        if (/Part\s*A/i.test(p.title)) { partA = p; break; }
                    }
                }
                if (partA) break;
            }
            if (partA) {
                if (!partA.texts) partA.texts = [];
                while (partA.texts.length < 4) {
                    partA.texts.push({
                        text_id: 'text_' + (partA.texts.length + 1),
                        title: 'Text ' + (partA.texts.length + 1),
                        paragraphs: [], questions: []
                    });
                }
                allQuestions.forEach(q => {
                    const n = parseInt(q.q_num, 10);
                    let idx = -1;
                    if (n >= 21 && n <= 25) idx = 0;
                    else if (n >= 26 && n <= 30) idx = 1;
                    else if (n >= 31 && n <= 35) idx = 2;
                    else if (n >= 36 && n <= 40) idx = 3;
                    if (idx >= 0 && partA.texts[idx]) partA.texts[idx].questions.push(q);
                });
            }
        }

        return exam;
    }

    // ==================== 事件绑定 ====================
    function bindEvents() {
        // 侧栏「使用提示」折叠（PC 默认收起，给真题列表让出高度）
        initTipCollapse();

        // 阅读区的单击、双击、选区和右键由 precision.js 统一处理。

        // 气泡按钮
        el.bubbleMore.addEventListener('click', () => {
            if (dictCurrentWord) openDictPanel(dictCurrentWord);
        });
        el.bubbleSpeak.addEventListener('click', () => {
            if (dictCurrentWord) speakWord(dictCurrentWord);
        });
        el.bubbleStar.addEventListener('click', () => {
            if (dictCurrentWord) toggleWord(dictCurrentWord);
        });
        el.bubbleCorrect.addEventListener('click', () => {
            if (dictCurrentWord && window.SrsCorrection) window.SrsCorrection.open(dictCurrentWord);
        });

        // 滚动/缩放时气泡脱离单词，自动关闭（气泡内部滚动除外）
        window.addEventListener('scroll', (e) => {
            if (!isBubbleOpen()) return;
            if (e.target && e.target.closest && e.target.closest('#dictBubble')) return;
            closeBubble();
        }, { passive: true, capture: true });
        window.addEventListener('resize', () => {
            if (isBubbleOpen()) closeBubble();
        });

        // 点击气泡外空白处关闭气泡
        document.addEventListener('click', (e) => {
            if (!isBubbleOpen()) return;
            if (e.target.closest('.dict-bubble') || e.target.closest('span.word')) return;
            closeBubble();
        });

        // 完整面板
        el.dictClose.addEventListener('click', closeDictPanel);
        el.dictBackdrop.addEventListener('click', closeDictPanel);
        el.dictSpeak.addEventListener('click', () => {
            if (dictCurrentWord) speakWord(dictCurrentWord);
        });
        el.dictStar.addEventListener('click', () => {
            if (dictCurrentWord) toggleWord(dictCurrentWord);
        });
        el.dictCorrect.addEventListener('click', () => {
            const word = dictCurrentWord || el.dictWord.textContent.trim();
            if (word && window.SrsCorrection) window.SrsCorrection.open(word);
        });
        el.dictSenses.addEventListener('click', (e) => {
            if (e.target.closest('[data-collapse]')) {
                el.dictPanel._showAll = !el.dictPanel._showAll;
                if (dictCurrentWord && dictLastEntry) {
                    renderDictPanel(dictCurrentWord, dictLastEntry);
                }
            }
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (el.dictPanel.classList.contains('show')) closeDictPanel();
                else closeBubble();
            }
        });

        // 移动端：下拉关闭
        let dragStartY = 0;
        let dragDy = 0;
        let dragging = false;
        el.dictHandle.addEventListener('touchstart', (e) => {
            dragStartY = e.touches[0].clientY;
            dragging = true;
            el.dictPanel.classList.add('dragging');
        }, { passive: true });
        el.dictHandle.addEventListener('touchmove', (e) => {
            if (!dragging) return;
            dragDy = Math.max(0, e.touches[0].clientY - dragStartY);
            el.dictPanel.style.transform = 'translateY(' + dragDy + 'px)';
        }, { passive: true });
        el.dictHandle.addEventListener('touchend', () => {
            if (!dragging) return;
            dragging = false;
            el.dictPanel.classList.remove('dragging');
            el.dictPanel.style.transform = '';
            if (dragDy > 80) closeDictPanel();
            dragDy = 0;
        });

        el.wordListBtn.addEventListener('click', openDrawer);
        el.drawerClose.addEventListener('click', closeDrawer);
        el.wordListDrawer.querySelector('.drawer-mask').addEventListener('click', closeDrawer);

        el.copyBtn.addEventListener('click', copyWords);
        if (el.copyBtn2) el.copyBtn2.addEventListener('click', copyWords);

        // 数据管理弹窗（顶部按钮）：导出 / 导入
        const backupModal = document.getElementById('backupModal');
        const backupManageBtn = document.getElementById('backupManageBtn');
        const backupCloseBtn = document.getElementById('backupClose');
        const backupExportBtn = document.getElementById('backupExportBtn');
        const backupImportBtn = document.getElementById('backupImportBtn');
        const backupFileInput = document.getElementById('backupFileInput');
        if (backupManageBtn && backupModal) {
            backupManageBtn.addEventListener('click', () => backupModal.classList.add('open'));
        }
        if (backupCloseBtn && backupModal) {
            backupCloseBtn.addEventListener('click', () => backupModal.classList.remove('open'));
            backupModal.addEventListener('click', (e) => {
                if (e.target === backupModal) backupModal.classList.remove('open');
            });
        }
        if (backupExportBtn) backupExportBtn.addEventListener('click', exportBackup);
        if (backupImportBtn && backupFileInput) {
            backupImportBtn.addEventListener('click', () => backupFileInput.click());
            backupFileInput.addEventListener('change', () => {
                const f = backupFileInput.files && backupFileInput.files[0];
                backupFileInput.value = '';
                importBackup(f);
            });
        }
        const scanShareBtn = document.getElementById('scanShareBtn');
        if (scanShareBtn) scanShareBtn.addEventListener('click', scanShare);

        el.clearAllBtn.addEventListener('click', clearAllWords);

        el.wordSearch.addEventListener('input', renderWordList);

        el.sortToggleBtn.addEventListener('click', () => {
            state.sortMode = state.sortMode === 'freq' ? 'time' : 'freq';
            const isFreq = state.sortMode === 'freq';
            el.sortToggleBtn.textContent = isFreq ? '按频率' : '按时间';
            el.sortToggleBtn.classList.toggle('active', isFreq);
            renderWordList();
        });

        el.wordListContainer.addEventListener('click', (e) => {
            const btn = e.target.closest('.word-remove');
            if (btn && btn.dataset.word) {
                removeWord(btn.dataset.word);
            }
        });

        // 单词背诵面板（SRS）入口按钮：不再在此直绑——
        // 由文件尾部的 document 捕获阶段委托统一处理（bindEvents 出错也拦得住）。

        el.examList.addEventListener('click', (e) => {
            const delBtn = e.target.closest('.exam-del');
            if (delBtn) {
                e.stopPropagation();
                deleteExam(delBtn.dataset.examId);
                return;
            }
            const groupTitle = e.target.closest('.exam-group-title');
            if (groupTitle) {
                const group = groupTitle.closest('.exam-group');
                const key = group ? group.dataset.group : null;
                if (key) {
                    if (!state.groupOpen) state.groupOpen = loadGroupState();
                    state.groupOpen[key] = !(state.groupOpen[key] === true);
                    saveGroupState();
                    group.classList.toggle('collapsed', state.groupOpen[key] !== true);
                    groupTitle.setAttribute('title', state.groupOpen[key] === true ? '收起' : '展开');
                }
                return;
            }
            const item = e.target.closest('.exam-item');
            if (item && item.dataset.examId) {
                selectExam(item.dataset.examId);
            }
        });

        // 真题详解
        el.materialsBtn.addEventListener('click', openMaterialsModal);
        el.materialsClose.addEventListener('click', closeMaterialsModal);
        el.materialsModal.addEventListener('click', (e) => {
            if (e.target === el.materialsModal) closeMaterialsModal();
        });

        // 交个朋友（微信二维码）——极简弹窗：× / 遮罩 / Esc 关闭
        el.friendBtn.addEventListener('click', openFriendModal);
        if (el.friendClose) el.friendClose.addEventListener('click', closeFriendModal);
        const friendMask = el.friendModal.querySelector('.modal-mask');
        if (friendMask) friendMask.addEventListener('click', closeFriendModal);

        // 双击模式开关（手机端标题旁）：收藏 ↔ 整句翻译
        if (el.dblModeBtn) {
            el.dblModeBtn.addEventListener('click', () => {
                dblMode = dblMode === 'collect' ? 'translate' : 'collect';
                saveDblMode(dblMode);
                applyDblModeUI();
                showToast(dblMode === 'translate' ? '已切换：单击单词 = 整句翻译' : '已切换：单击 = 收藏', 'warn');
            });
        }

        // 使用反馈
        el.feedbackBtn.addEventListener('click', openFeedback);
        el.feedbackClose.addEventListener('click', closeFeedback);
        // 按用户要求：反馈弹窗只能点「×」关闭，点击遮罩不关闭（防止误触丢失草稿）
        el.feedbackText.addEventListener('input', () => {
            el.feedbackCount.textContent = el.feedbackText.value.length;
        });
        el.feedbackSubmit.addEventListener('click', submitFeedback);

        // 专业课真题入口：已登录 → 学校/专业目录；未登录 → 门户首页
        const biochemNav = document.querySelector('.snav-link[href="/biochem/"]');
        if (biochemNav) {
            biochemNav.addEventListener('click', (e) => {
                e.preventDefault();
                fetch('/biochem/api/check/', { credentials: 'same-origin' })
                    .then((r) => {
                        const loggedIn =
                            r.ok &&
                            (r.headers.get('content-type') || '').indexOf('application/json') !== -1;
                        location.href = loggedIn ? '/biochem/schools/' : '/';
                    })
                    .catch(() => {
                        location.href = '/';
                    });
            });
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (el.uploadModal && el.uploadModal.classList.contains('open')) closeUploadModal();
                else if (el.friendModal && el.friendModal.classList.contains('open')) closeFriendModal();
                else if (el.wordListDrawer.classList.contains('open')) closeDrawer();
            }
        });
    }

    // ==================== 初始化 ====================
    async function init() {
        loadWords();
        loadExams();
        loadActiveExamId();
        updateWordCount();
        bindEvents();
        applyDblModeUI();
        // 过期页面自愈：手机浏览器常把标签页挂好几天，页面里跑的还是部署前的旧 JS，
        // 表现就是「服务端修了、用户还是旧行为」。这里比对版本串，不一致就自动刷新一次。
        guardStaleCode();
        // 回到前台时再查一次（用户往往是隔天切回来继续用）
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') guardStaleCode();
        });
        // 扫码传递：?import=<code> 打开时自动拉取并导入（异步，不阻塞加载）
        handleImportByUrl();

        // 导入备份后刷新：显示导入成功提示（sessionStorage 标记，刷新后消费）
        try {
            if (sessionStorage.getItem('aseeker_backup_imported') === '1') {
                sessionStorage.removeItem('aseeker_backup_imported');
                const wc = Object.keys(state.words || {}).length;
                showToast('✓ 已导入备份：' + wc + ' 个收藏单词', 'success');
            }
        } catch (e) { /* ignore */ }

        // ---- 产品调整：导出/复制合并为"复制单词"（移除"导出"txt 下载入口，保留复制）----
        document.querySelectorAll('#exportBtn2').forEach(function (b) {
            if (b) b.style.display = 'none';
        });

        // 并行加载所有内置真题（串行会放大 34 个请求的总耗时）
        await loadDataVersions();   // 真题 URL 也要带内容戳（改过文本立刻生效）
        const examsStamp = String(DATA_VERSIONS.exams || '');

        // 首屏要先画哪一套：深链 ?exam= → 上次打开 → 最新一套
        let wantExamId = '';
        try { wantExamId = new URLSearchParams(location.search).get('exam') || ''; } catch (e) { /* ignore */ }
        if (!wantExamId) wantExamId = state.activeExamId || '';
        if (!wantExamId) wantExamId = examIdFromPath(BUILTIN_EXAM_PATHS[BUILTIN_EXAM_PATHS.length - 1] || '');

        // 首屏/tail 共用的两件小事
        const applyDeepLinkExam = () => {
            try {
                const qExam = new URLSearchParams(location.search).get('exam');
                if (qExam && state.exams.some(function (e) { return e.exam_id === qExam; })) {
                    state.activeExamId = qExam;
                    saveActiveExamId();
                }
            } catch (e) { /* ignore */ }
        };
        const renderActiveExam = () => {
            if (state.activeExamId) {
                const exam = state.exams.find(e => e.exam_id === state.activeExamId);
                if (exam) { renderExam(exam); return; }
                state.activeExamId = null;
            }
            if (state.exams[0]) selectExam(state.exams[0].exam_id);
        };

        // —— ① 真题按内容戳复用 ——
        // 以前每次打开都无条件重下 34 套（1.05 MB），哪怕服务器上的真题一个字都没改。
        // 现在本地存的真题带着上次的 exams 戳：戳一致就直接用，**一个请求都不发**
        //（这也是静态资源能把 TTL 放到一年的前提：内容没变就不该产生流量）。
        if (examsStamp && examsStamp === storedExamsStamp() && builtinsComplete()) {
            state.exams.sort(sortExamsByYearDesc);
            buildFrequencyIndex();
            renderExamList();
            applyDeepLinkExam();
            renderActiveExam();
            return;
        }

        // —— ② 要重新取时，也不再让首屏等全部 34 套 ——
        // 一拿到"当前这一套"就先把首屏画出来，其余 33 套在后台继续；到齐后再补侧栏与词频。
        let loadedCount = 0;
        let updatedCount = 0;
        let painted = false;
        const mergeBuiltin = (builtin) => {
            const index = state.exams.findIndex(e => e.exam_id === builtin.exam_id);
            if (index === -1) { state.exams.push(builtin); loadedCount++; }
            else { state.exams[index] = builtin; updatedCount++; }   // 服务器版本为准，覆盖本地旧数据
        };
        const paintFirstPaint = () => {
            const wanted = state.exams.find(e => e.exam_id === wantExamId);
            if (wanted) {
                state.activeExamId = wanted.exam_id;
                saveActiveExamId();
                state.exams.sort(sortExamsByYearDesc);
                buildFrequencyIndex();
                renderExamList();
                renderExam(wanted);
            } else {
                renderExamList();
                renderActiveExam();
            }
        };

        const results = await Promise.all(
            BUILTIN_EXAM_PATHS.map(async (path) => {
                try {
                    const resp = await fetch(path + (path.indexOf('?') >= 0 ? '&' : '?')
                        + 'v=' + DATA_VERSIONS.exams);
                    if (!resp.ok) throw new Error('HTTP ' + resp.status);
                    const builtin = await resp.json();
                    builtin.builtin = true;
                    mergeBuiltin(builtin);
                    // 当前要展示的那一套一到 → 立刻画首屏，不等其余 33 套
                    if (!painted && builtin.exam_id === wantExamId) {
                        painted = true;
                        paintFirstPaint();
                    }
                    return { ok: true };
                } catch (e) {
                    console.error('加载内置真题失败：' + path, e);
                    return { ok: false };
                }
            })
        );
        const failedCount = results.filter(r => !r.ok).length;
        if (loadedCount > 0 || updatedCount > 0) {
            saveExams();
        }
        // 只有全部成功才记内容戳：否则下次会误以为本地这份是完整的
        if (failedCount === 0 && examsStamp) saveExamsStamp(examsStamp);
        // 按年份排序（新的在前）
        state.exams.sort(sortExamsByYearDesc);
        buildFrequencyIndex();
        if (failedCount === BUILTIN_EXAM_PATHS.length) {
            el.examContent.innerHTML = '<div class="empty-state">' +
                '内置真题加载失败<br><br>' +
                '可能原因：直接双击打开了 HTML 文件，浏览器限制了本地文件访问。<br><br>' +
                '请改用本地服务器打开（参见 README.md）。' +
                '</div>';
        }

        renderExamList();   // 侧栏补全

        // 首屏已经画过（第 ② 步）就不要重画正文：那会把用户正在读的位置顶回开头
        if (!painted) {
            applyDeepLinkExam();
            renderActiveExam();
        }
    }

    // Public bridge for the precision-reading UI; legacy learning data is preserved.
    window.EnglishApp = {
        state: () => state,
        normalizeWord,
        toast: showToast,
        lookup: async (word) => { await loadDict(); return lookupWord(word); },
        translate: (text) => lookupSentence(text, true),
        selectExam: (id) => { selectExam(id); return window.EnglishPrecision ? window.EnglishPrecision.whenRendered() : Promise.resolve(); },
        collect: (word, info, options = {}) => {
            const key = normalizeWord(word);
            if (!key) return;
            const previous = state.words[key];
            state.words[key] = Object.assign({}, previous || {}, info || {}, {
                word, addedAt: previous ? previous.addedAt : Date.now(), examId: state.activeExamId
            });
            saveWords(); updateWordCount(); renderWordList();
            document.querySelectorAll('#examContent [data-word]').forEach(span => {
                span.classList.toggle('collected', !!state.words[normalizeWord(span.dataset.word)]);
            });
            if (!options.silent) showToast(previous ? '已在生词本：' + word : '已收藏：' + word, 'success');
        },
        remove: removeWord
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    /* ==================== 整段翻译气泡 ====================
       选中一段文字（多词）后，弹出「复制 / 百度翻译 / 必应翻译」。
       纯前端 + 外链跳转：不经过服务器、不存储任何文本。
       ======================================================= */
    let translateBubble = null;
    let translateText = '';
    let translateZh = '';
    let translateSeq = 0;
    let sentenceBank = null;
    let sentenceBankState = 'idle';
    let sentenceBankPromise = null;

    function normalizeSentence(text) {
        return String(text || '')
            .replace(/[\u2018\u2019]/g, "'")
            .replace(/\s+/g, ' ')
            .replace(/^[\s"'\u201c\u201d\u2018\u2019]+|[\s"'\u201c\u201d\u2018\u2019]+$/g, '')
            .toLowerCase();
    }

    const SENT_ABBR = new Set([
        'mr', 'mrs', 'ms', 'dr', 'st', 'no', 'vs', 'etc', 'e.g', 'i.e',
        'cf', 'al', 'prof', 'inc', 'ltd', 'co', 'a.m', 'p.m', 'u.s',
        'u.k', 'fig', 'ref', 'vol', 'pp', 'jan', 'feb', 'mar', 'apr',
        'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec',
    ]);

    // 手动切句：避开 U.S. / e.g. 等缩写与小数点，兼容不支持 lookbehind 的老浏览器
    function splitSentencesManual(text) {
        const out = [];
        let cur = '';
        for (let i = 0; i < text.length; i++) {
            const ch = text[i];
            cur += ch;
            if (ch !== '.' && ch !== '!' && ch !== '?') continue;
            // 小数点（3.5）或缩写内部句点（e.g. / U.S.）不切
            const prev = text[i - 1] || '';
            const next = text[i + 1] || '';
            if (/[0-9]/.test(prev) && /[0-9]/.test(next)) continue;
            if (/[A-Za-z]/.test(next)) continue;
            let j = i;
            while (j < text.length && /[.!?]/.test(text[j])) j++;
            while (j < text.length && (text[j] === '"' || text[j] === "'" ||
                   text[j] === '\u201d' || text[j] === '\u2019')) j++;
            const wordBefore = (text.slice(0, i).match(/([A-Za-z.]+)$/) || ['', ''])[1].toLowerCase();
            const isAbbr = SENT_ABBR.has(wordBefore) || /^[a-z]\.$/.test(wordBefore);
            let k = j;
            while (k < text.length && /\s/.test(text[k])) k++;
            if (k >= text.length || /[A-Za-z0-9"\u201c(]/.test(text[k])) {
                if (!isAbbr) {
                    const s = cur.trim();
                    if (s) out.push(s);
                    cur = '';
                    i = k - 1;
                }
            }
        }
        if (cur.trim()) out.push(cur.trim());
        return out.filter((s) => s.length > 2);
    }

    async function sha256Hex20(text) {
        const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
        return Array.from(new Uint8Array(buf))
            .map((b) => b.toString(16).padStart(2, '0'))
            .join('')
            .slice(0, 20);
    }

    async function loadSentenceBank() {
        if (sentenceBank) return sentenceBank;
        if (sentenceBankState === 'loading') return sentenceBankPromise;
        sentenceBankState = 'loading';
        sentenceBankPromise = (async () => {
            try {
                // 句库 URL 带**内容戳**（部署时按文件 md5 生成），内容变了 URL 就变，
                // 不会出现「代码是新的、句库还是几个月前的缓存」——
                // 那正是「阅读选项点了全是暂未收录」的元凶。
                // 取法也从 force-cache（永不回源）改成 no-cache（带 ETag 回源校验，304 很便宜）。
                const v = await loadDataVersions();
                const r = await fetch('data/sentence_translations.json?v=' + v.bank, { cache: 'no-cache' });
                if (!r.ok) throw new Error('http ' + r.status);
                const data = await r.json();
                const map = {};
                for (const it of data.items || []) {
                    if (it && it.h && it.zh) map[it.h] = it;
                }
                sentenceBank = map;
                sentenceBankState = 'ready';
            } catch (err) {
                sentenceBank = null;
                sentenceBankState = 'error';
            }
            return sentenceBank;
        })();
        return sentenceBankPromise;
    }

    async function lookupSentence(text, exactOnly = false) {
        const norm = normalizeSentence(text);
        if (!norm || !/[a-z]/.test(norm)) return null;
        try {
            await loadSentenceBank();
            if (!sentenceBank) return null;
            const h = await sha256Hex20(norm);
            if (sentenceBank[h]) {
                return { en: sentenceBank[h].en, zh: sentenceBank[h].zh, mode: 'exact' };
            }
            if (exactOnly) return null;
            // 选中跨了多句：逐句匹配
            const clean = String(text || '').replace(/\s+/g, ' ').trim();
            const parts = splitSentencesManual(clean).filter((s) => s.length > 6);
            let splitPartial = null;
            if (parts.length > 1) {
                const rows = [];
                let complemented = false;
                for (const part of parts) {
                    const ph = await sha256Hex20(normalizeSentence(part));
                    let it = sentenceBank[ph];
                    if (!it && part.length >= 12) {
                        // 某句只划了一半：补全到所在完整句
                        let best = null;
                        for (const cand of Object.values(sentenceBank)) {
                            const en = normalizeSentence(cand.en);
                            if (en.includes(normalizeSentence(part)) && (!best || en.length < best.en.length)) {
                                best = cand;
                            }
                        }
                        if (best) {
                            it = best;
                            complemented = true;
                        }
                    }
                    if (it) rows.push(it);
                }
                if (rows.length === parts.length) {
                    const dd = dedupeRows(rows);
                    return {
                        rows: dd,
                        en: dd.map((r) => r.en).join(' '),
                        zh: dd.map((r) => r.zh).join('\n\n'),
                        mode: complemented ? 'multi-complemented' : 'multi',
                    };
                }
                if (rows.length > 0) {
                    const dd = dedupeRows(rows);
                    splitPartial = {
                        rows: dd,
                        en: dd.map((r) => r.en).join(' '),
                        zh: dd.map((r) => r.zh).join('\n\n'),
                    };
                }
            }
            // 无标点边界（从句子中间划起）：用句库贪心解析完整句序列
            const decomposed = decomposeByBank(clean);
            if (decomposed && decomposed.rows.length > 1 &&
                (!splitPartial || decomposed.rows.length > splitPartial.rows.length)) {
                const dd = dedupeRows(decomposed.rows);
                return {
                    rows: dd,
                    en: dd.map((r) => r.en).join(' '),
                    zh: dd.map((r) => r.zh).join('\n\n'),
                    mode: decomposed.complemented ? 'multi-complemented' : 'multi',
                };
            }
            if (splitPartial) {
                return { ...splitPartial, mode: 'multi-partial' };
            }
            // 没划完整句：把选中片段补全到所在整句
            if (norm.length >= 10) {
                let best = null;
                for (const it of Object.values(sentenceBank)) {
                    const en = normalizeSentence(it.en);
                    if (en.includes(norm) && (!best || en.length < best.en.length)) {
                        best = { en: it.en, zh: it.zh };
                    }
                }
                if (best) return { en: best.en, zh: best.zh, mode: 'partial' };
            }
            return null;
        } catch (err) {
            return null;
        }
    }

    /** 词条能不能当「一句完整的话」被贪心解析吃掉。
     *
     *  句库里混着 892 条（11%）1–3 词的碎片条目——"energy"→能源、"as well as"→以及、
     *  "experience"→经验。它们是从完形选项/短语收藏里带进来的，不是句子。
     *  贪心解析一旦把它们当句子吃掉，剩下的残片又会被 findContainingSentence()
     *  补全回**同一整句**，于是同一句译文在气泡里出现两次，中间夹着一堆
     *  「energy → 能源」这种碎片行（用户报的「重复的两段翻译」就是这么来的）。
     *  判据：结尾带句末标点 = 句子；否则只认 4 词以上的（标题式无句点整句）。 */
    function isSentenceEntry(en) {
        if (/[.!?]["'\u201d\u2019)\]]*$/.test(en)) return true;
        return en.split(' ').length >= 4;
    }

    /** 同一个词条在 rows 里只保留第一次出现——双保险，杜绝「同一段译文出现两遍」。 */
    function dedupeRows(rows) {
        const seen = new Set();
        const out = [];
        for (const r of rows) {
            const k = (r && r.h) || normalizeSentence(r && r.en);
            if (k) {
                if (seen.has(k)) continue;
                seen.add(k);
            }
            out.push(r);
        }
        return out;
    }

    function findContainingSentence(frag) {
        const nf = normalizeSentence(frag);
        if (!nf || nf.length < 12) return null;
        let best = null;
        for (const it of Object.values(sentenceBank)) {
            const en = normalizeSentence(it.en);
            if (en.includes(nf) && (!best || en.length < normalizeSentence(best.en).length)) {
                best = it;
            }
        }
        return best;
    }

    function decomposeByBank(clean) {
        const sel = normalizeSentence(clean);
        if (!sel) return null;
        const rows = [];
        let rest = sel;
        let complemented = false;
        while (rest.length > 0) {
            let best = null;
            for (const it of Object.values(sentenceBank)) {
                const en = normalizeSentence(it.en);
                if (!isSentenceEntry(en)) continue;   // 别把 "energy"/"as well as" 这类碎片当句子
                if (rest.startsWith(en) && (!best || en.length > normalizeSentence(best.en).length)) {
                    best = it;
                }
            }
            if (best) {
                rows.push(best);
                rest = rest.slice(normalizeSentence(best.en).length);
                continue;
            }
            // 当前位置不是句子开头：跳到下一处完整句，残片尝试补全
            let nextIdx = -1;
            let nextIt = null;
            for (const it of Object.values(sentenceBank)) {
                const en = normalizeSentence(it.en);
                if (!isSentenceEntry(en)) continue;
                const idx = rest.indexOf(en, 1);
                if (idx > 0 && (nextIdx === -1 || idx < nextIdx ||
                    (idx === nextIdx && en.length > normalizeSentence(nextIt.en).length))) {
                    nextIdx = idx;
                    nextIt = it;
                }
            }
            if (nextIdx > 0 && nextIt) {
                const frag = rest.slice(0, nextIdx);
                const fragIt = findContainingSentence(frag);
                if (fragIt) {
                    rows.push(fragIt);
                    complemented = true;
                }
                rest = rest.slice(nextIdx).replace(/^\s+/, '');
            } else {
                const fragIt = findContainingSentence(rest);
                if (fragIt) {
                    rows.push(fragIt);
                    complemented = true;
                }
                break;
            }
        }
        if (rows.length === 0) return null;
        return { rows, complemented };
    }

    function buildTranslateBubble() {
        if (translateBubble) return translateBubble;
        translateBubble = document.createElement('div');
        translateBubble.className = 'translate-bubble';
        translateBubble.innerHTML =
            '<div class="tb-title">整段翻译</div>' +
            '<div class="tb-result" style="display:none">' +
            '    <div class="tb-zh"></div>' +
            '    <div class="tb-meta">真题原文句 · 本地译文</div>' +
            '</div>' +
            '<div class="tb-miss" style="display:none">暂未收录这句（已支持历年真题阅读原文）</div>' +
            '<div class="tb-actions">' +
            '<button type="button" class="tb-btn tb-copy">复制</button>' +
            '<button type="button" class="tb-btn tb-copy-orig" style="display:none">复制原文</button>' +
            '<a class="tb-btn tb-link" href="#" target="_blank" rel="noopener">必应翻译</a>' +
            '<button type="button" class="tb-btn tb-close">收起</button>' +
            '</div>';
        translateBubble.addEventListener('click', (e) => {
            const closeBtn = e.target.closest('.tb-close');
            if (closeBtn) {
                closeTranslateBubble();
                return;
            }
            const origBtn = e.target.closest('.tb-copy-orig');
            if (origBtn && translateText) {
                copyTranslateText(origBtn, translateText);
                return;
            }
            const copyBtn = e.target.closest('.tb-copy');
            if (copyBtn && translateText) {
                copyTranslateText(copyBtn, translateZh || translateText);
                return;
            }
            const link = e.target.closest('.tb-link');
            if (link && translateText) {
                const url = link.href;
                // 纯鼠标设备：拦截后用 window.open 复用同一个翻译窗口；
                // 触屏设备（手机/平板/触屏笔记本）：走原生链接 target=_blank，
                // window.open 在移动端会被拦截/不可靠
                const isTouch = navigator.maxTouchPoints > 0 || ('ontouchstart' in window);
                if (!isTouch) {
                    e.preventDefault();
                    const w = window.open(url, 'aseeker-translate');
                    if (w) w.focus();
                    else if (url) window.location.href = url;
                }
            }
        });
        document.body.appendChild(translateBubble);
        return translateBubble;
    }

    function copyTranslateText(copyBtn, text) {
            const t = text || translateText;
            if (navigator.clipboard && window.isSecureContext) {
                navigator.clipboard.writeText(t).then(() => {
                    copyBtn.textContent = '已复制';
                    setTimeout(() => { copyBtn.textContent = '复制'; }, 1200);
                }).catch(() => {});
            } else {
                const ta = document.createElement('textarea');
                ta.value = t;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                document.body.appendChild(ta);
                ta.select();
                try { document.execCommand('copy'); } catch (err) { /* ignore */ }
                document.body.removeChild(ta);
                copyBtn.textContent = '已复制';
                setTimeout(() => { copyBtn.textContent = '复制'; }, 1200);
            }
    }

    function selectedTextForTranslate() {
        try {
            const sel = window.getSelection();
            if (!sel || sel.isCollapsed) return '';
            const text = (sel.toString() || '').trim();
            // 单次点击单词（无空格）交给词典逻辑，不弹翻译气泡
            if (!text || !/\s/.test(text)) return '';
            // 纯空白/符号不弹
            if (!/[A-Za-z\u4e00-\u9fa5]/.test(text)) return '';
            return text.slice(0, 3000);
        } catch (err) {
            return '';
        }
    }

    // 复制/翻译前规范化：换行、制表符、连续空格统一成单个空格
    function cleanTranslateText(raw) {
        return String(raw || '').replace(/\s+/g, ' ').trim();
    }

    function selectionRect() {
        try {
            const sel = window.getSelection();
            if (!sel || sel.rangeCount === 0) return null;
            const rect = sel.getRangeAt(0).getBoundingClientRect();
            if (rect && (rect.width > 0 || rect.height > 0)) return rect;
            if (sel.anchorNode && sel.anchorNode.parentElement) {
                return sel.anchorNode.parentElement.getBoundingClientRect();
            }
        } catch (err) { /* ignore */ }
        return null;
    }

    function positionTranslateBubble(bubble, anchorRect) {
        if (!bubble || bubble.style.display === 'none') return;
        let rect = anchorRect || selectionRect();
        // 触屏点词：优先用整句包围盒，且每次按 DOM 实时重算
        //（滚动 / 手机地址栏收起后依然准确，不会被顶到别处）
        if (translateLastSentence && translateLastSentence.para && translateLastSentence.para.isConnected) {
            rect = sentenceBox(translateLastSentence.para, translateLastSentence.text) || rect;
        }
        if (rect) {
            placeBubbleAvoiding(bubble, rect);
            return;
        }
        const bw = bubble.offsetWidth || 220;
        const bh = bubble.offsetHeight || 90;
        const x = Math.max(8, (window.innerWidth - bw) / 2);
        const y = Math.max(8, window.innerHeight - bh - 32);
        bubble.style.left = x + 'px';
        bubble.style.top = y + 'px';
    }

    function showTranslateBubble() {
        const text = selectedTextForTranslate();
        if (!text) { closeTranslateBubble(); return; }
        openTranslateByText(text, null);
    }

    /** 用指定文本打开句译气泡（命中本地句库内嵌显示；未命中提示+必应翻译）。
        anchorRect 为空时退回原生选区定位（桌面划词）。 */
    function openTranslateByText(text, anchorRect) {
        translateText = cleanTranslateText(text);
        if (!translateText) { closeTranslateBubble(); return; }
        // 记住锚点：视口变化（手机浏览器地址栏收起等）时只重定位，不关闭气泡
        translateLastAnchor = anchorRect || null;
        translateLastSentence = null;
        const bubble = buildTranslateBubble();
        // 关闭词典气泡，避免两个气泡叠一起
        try { closeBubble(); } catch (err) { /* ignore */ }
        const links = bubble.querySelectorAll('.tb-link');
        const resultEl = bubble.querySelector('.tb-result');
        const missEl = bubble.querySelector('.tb-miss');
        const zhEl = bubble.querySelector('.tb-zh');
        const copyBtn = bubble.querySelector('.tb-copy');
        const origBtn = bubble.querySelector('.tb-copy-orig');
        const seq = ++translateSeq;
        translateZh = '';
        resultEl.style.display = 'none';
        missEl.style.display = 'none';
        origBtn.style.display = 'none';
        copyBtn.style.display = '';
        copyBtn.textContent = '复制';
        links[0].textContent = '必应翻译';
        links[0].href = 'https://cn.bing.com/translator/?text=' + encodeURIComponent(translateText);
        // 查本地句译库：命中直接内嵌显示译文，不跳转
        lookupSentence(translateText).then((hit) => {
            if (seq !== translateSeq) return;
            if (!hit) {
                missEl.style.display = '';
            } else {
                translateZh = hit.zh;
                const metaEl = bubble.querySelector('.tb-meta');
                if (hit.mode === 'multi') metaEl.textContent = '真题原文 · 逐句译文';
                else if (hit.mode === 'multi-complemented') metaEl.textContent = '部分为半句补全 · 逐句译文';
                else if (hit.mode === 'multi-partial') metaEl.textContent = '部分句子已匹配 · 其余暂未收录';
                else if (hit.mode === 'partial') metaEl.textContent = '已补全到完整句 · 本地译文';
                else metaEl.textContent = '真题原文句 · 本地译文';
                zhEl.innerHTML = '';
                if (hit.rows) {
                    for (const row of hit.rows) {
                        const wrap = document.createElement('div');
                        wrap.className = 'tb-srow';
                        const enEl = document.createElement('div');
                        enEl.className = 'tb-sen';
                        enEl.textContent = row.en;
                        const zhRow = document.createElement('div');
                        zhRow.className = 'tb-szh';
                        zhRow.textContent = row.zh;
                        wrap.appendChild(enEl);
                        wrap.appendChild(zhRow);
                        zhEl.appendChild(wrap);
                    }
                } else {
                    zhEl.textContent = hit.zh;
                }
                resultEl.style.display = '';
                copyBtn.textContent = '复制译文';
                origBtn.style.display = '';
            }
            // 内容(命中/未命中)就绪后气泡高度会变化：用最终高度重新避让整句，
            // rAF + 下一帧兜底，避免加载态定位后内容撑高气泡压住原句
            requestAnimationFrame(() => positionTranslateBubble(bubble, anchorRect));
            setTimeout(() => positionTranslateBubble(bubble, anchorRect), 40);
        });
        bubble.style.display = 'block';
        positionTranslateBubble(bubble, anchorRect);
    }

    /** 点上的单词 span（翻译模式点单个单词时回落到词典气泡用）。
     *  完形填空选项、正文单词都渲染成 span.word，所以直接用命中测试取回即可。 */
    function wordSpanAtPoint(x, y) {
        try {
            const node = document.elementFromPoint(x, y);
            if (node && node.closest) {
                const span = node.closest('span.word');
                if (span && span.dataset.word) return span;
            }
        } catch (err) { /* ignore */ }
        return null;
    }

    /** 点是否落在**真的有字**的地方。
     *
     *  用户要求「点空处弹窗要消失」。只靠 `caretRangeFromPoint` 不行：点段落左侧
     *  页边（x≈10）浏览器照样把 caret 定位到该行行首，于是「点空白」变成了「点了第一句」，
     *  气泡不关反而换了一句。所以还要验证落点确实在某行的**文字行盒**里：
     *  取 caret 所在文本节点的所有行盒矩形，落点不在任何行盒内 = 没字 = 空白。
     *  badge（题号/选项字母，user-select:none 但属于可点目标）与 span.word 直接放行。 */
    function pointOnText(x, y) {
        try {
            const hit = document.elementFromPoint(x, y);
            if (hit && hit.closest && hit.closest('span.word, .option-letter, .choice-letter, .question-num')) {
                return true;
            }
            let range = null;
            if (document.caretRangeFromPoint) range = document.caretRangeFromPoint(x, y);
            else if (document.webkitCaretRangeFromPoint) range = document.webkitCaretRangeFromPoint(x, y);
            if (!range || !range.startContainer) return false;
            const node = range.startContainer;
            if (node.nodeType !== 3) return false;
            const probe = document.createRange();
            probe.selectNodeContents(node);
            for (const rc of probe.getClientRects()) {
                if (rc.width < 1 || rc.height < 1) continue;
                if (x >= rc.left - 1 && x <= rc.right + 1 && y >= rc.top - 1 && y <= rc.bottom + 1) {
                    return true;
                }
            }
            return false;
        } catch (err) {
            return false;
        }
    }

    /** 触屏点词句译：找到点击位置所在的整句，走句译气泡；并把该句原文涂上阴影高亮。
     *  返回 true = 确实弹了东西（句译或词典）；false = 点了空白，已把气泡收掉。 */
    function showSentenceBubbleAt(x, y) {
        // 点在没有文字的地方（页边、行外空隙、区块之间）→ 关掉气泡
        if (!pointOnText(x, y)) {
            closeTranslateBubble();
            closeBubble();
            return false;
        }
        const found = sentenceAtPoint(x, y);
        if (!found) {
            closeTranslateBubble();
            return false;
        }
        // 去掉**题号/选项字母**前缀（"21. " / "A. " / "[A] "），句库不含这些前缀。
        // 与 corpus.strip_option_prefix 同口径：只认带括号/点号/顿号的写法。
        // 渲染层 badge（题号、选项字母）已由 sentenceAtPoint 的 leadingBadgeLen()
        // 按 DOM 剔干净，这里**不再**用「裸单字母开头」去猜——那会把
        // "Any person can do it." 的 Any 当成选项字母 A 吃掉（→ "ny person…"）。
        const cleaned = found.text.replace(
            /^\s*(?:[\[（(]\s*[A-Ha-h]\s*[\]）)]|(?:\d{1,2}|[A-Ha-h])\s*[.、．)）])\s*/,
            ''
        );
        let text = cleanTranslateText(cleaned);
        // 注：早期这里有个「剥完不足 10 字就回退用带标记原文去查」的特例（"[G] Be humble"）。
        // 现在 Part B 段落/选项段的字母已经在**渲染层**做成 badge（renderChoiceParagraph），
        // 句库键也同步剥掉了标记 → DOM 文本与句库键一致，这个特例成了死代码，已删。
        if (!text) text = cleanTranslateText(found.text);
        if (!text || !/[A-Za-z]/.test(text)) {
            closeTranslateBubble();
            return false;
        }
        // 单词级（无空格、就是一个词，允许句点）一律走**词典气泡**：完形填空的选项
        // 就是这种（"Though" / "understandings"）。**不能用长度当判据**——
        // 旧阈值 12 会把 "understandings"(14)、"Approximately"(13) 漏到句译分支，
        // 句库里没有这个单词就弹「暂未收录」（用户反馈的正是这一类）。
        const singleWord = !/\s/.test(text) && /^[A-Za-z][A-Za-z'-]*\.?$/.test(text);
        if (singleWord) {
            const wSpan = wordSpanAtPoint(x, y);
            const w = (wSpan && wSpan.dataset.word) || text.replace(/[^A-Za-z'-]/g, '');
            if (wSpan && w && w.length > 1) {
                closeTranslateBubble();
                showBubble(w, wSpan);
                return true;
            }
            closeTranslateBubble();
            return false;
        }
        if (text.length > 1200) text = text.slice(0, 1200);
        // 以“整句包围盒”为锚：弹窗避开整句（上方优先，其次下方），不挡原句
        const box = sentenceBox(found.para, found.text);
        const anchor = box || { left: x - 80, width: 160, bottom: y + 8, top: y - 2 };
        openTranslateByText(text, anchor);
        // 记住整句引用：滚动/地址栏收起时按 DOM 实时重算，气泡始终避让该句
        translateLastSentence = { para: found.para, text: found.text };
        // 给被翻译的句子原文涂上阴影（划重点效果）
        highlightSentence(found.para, found.text);
        return true;
    }

    /** 翻译模式下由触摸点弹句译：先用抬手/取消时的点，失败再退回**按下的点**。
     *
     *  为什么需要这个兜底：`pointOnText` 是按**落点**判「有没有点到字」的，而手指
     *  抬起时常常已经漂出了那一行的行盒——实测（iPhone 13 视口，CDP 触摸）漂移
     *  13px 还正常、**14px 就出去了**。于是 touchend 拿到的是一个「点在空白上」的
     *  结论：收掉气泡 + 什么都不弹，同时 400ms 内把浏览器补发的 click 也吞掉。
     *  用户看到的就是「手指按在词上（:hover 有反馈），气泡不弹，点了等于没点」。
     *  用户点的是哪个词，由**按下的位置**表达，所以起点必须作为兜底。
     *  （再往外漂 16px+ 浏览器自己就会开始滚动且不再补发 click，那才是真拖拽。） */
    function showSentenceBubbleFrom(start, x, y) {
        if (showSentenceBubbleAt(x, y)) return true;
        if (start && (Math.abs(start.x - x) > 1 || Math.abs(start.y - y) > 1)) {
            return showSentenceBubbleAt(start.x, start.y);
        }
        return false;
    }

    // ==================== 句译高亮层 ====================
    let senRange = null;

    function ensureSenLayer() {
        let layer = document.getElementById('sen-highlight-layer');
        if (!layer) {
            layer = document.createElement('div');
            layer.id = 'sen-highlight-layer';
            layer.className = 'sen-highlight-layer';
            document.body.appendChild(layer);
        }
        return layer;
    }

    function updateSenHighlight() {
        const layer = document.getElementById('sen-highlight-layer');
        if (!layer) return;
        if (!senRange) { layer.innerHTML = ''; return; }
        try {
            layer.innerHTML = '';
            const rects = senRange.getClientRects();
            for (const r of rects) {
                if (r.width < 1 || r.height < 1) continue;
                const d = document.createElement('div');
                d.className = 'sen-rect';
                d.style.left = r.left + 'px';
                d.style.top = r.top + 'px';
                d.style.width = r.width + 'px';
                d.style.height = r.height + 'px';
                layer.appendChild(d);
            }
        } catch (e) { /* ignore */ }
    }

    function clearSentenceHighlight() {
        senRange = null;
        const layer = document.getElementById('sen-highlight-layer');
        if (layer) layer.innerHTML = '';
    }

    /** 高亮段落中某整句：按字符偏移定位文本节点区间，用矩形层涂阴影 */
    function highlightSentence(para, sentence) {
        clearSentenceHighlight();
        if (!para || !sentence) return;
        try {
            const full = para.textContent || '';
            const idx = full.indexOf(sentence);
            if (idx < 0) return;
            const range = document.createRange();
            let off = 0;
            let startNode = null, startOff = 0, endNode = null, endOff = 0;
            const walker = document.createTreeWalker(para, NodeFilter.SHOW_TEXT);
            let node = null;
            while ((node = walker.nextNode())) {
                const len = (node.textContent || '').length;
                if (startNode === null && off + len > idx) {
                    startNode = node;
                    startOff = idx - off;
                }
                if (endNode === null && off + len >= idx + sentence.length) {
                    endNode = node;
                    endOff = idx + sentence.length - off;
                    break;
                }
                off += len;
            }
            if (!startNode || !endNode) return;
            range.setStart(startNode, startOff);
            range.setEnd(endNode, endOff);
            ensureSenLayer();
            senRange = range;
            updateSenHighlight();
        } catch (e) { /* ignore */ }
    }

    window.addEventListener('scroll', () => {
        if (senRange) requestAnimationFrame(updateSenHighlight);
    }, { passive: true, capture: true });
    window.addEventListener('resize', () => {
        if (senRange) requestAnimationFrame(updateSenHighlight);
    });

    /** 文本块开头的「标记」长度：题号 / 选项字母是独立 badge 元素
     *  （.question-num / .option-letter / .choice-letter），它们的 textContent
     *  会与正文拼在一起（"21.Romans…" / "AIt is clear…" / "ASaving them…"）。
     *  用 DOM 精确量出长度后剔除，**不做正则猜测**——按「字母开头」猜会把
     *  "Any person can do it." 的 Any 吃掉。 */
    function leadingBadgeLen(para) {
        if (!para || !para.children) return 0;
        let n = 0;
        for (const child of para.children) {
            if (child.matches && child.matches('.question-num, .option-letter, .choice-letter')) {
                n += (child.textContent || '').length;
            } else {
                break; // 只剔开头的连续 badge，正文里出现的同类元素不动
            }
        }
        return n;
    }

    /** 由触摸点定位所在文本块（段落）与整句 */
    function sentenceAtPoint(x, y) {
        try {
            let range = null;
            if (document.caretRangeFromPoint) range = document.caretRangeFromPoint(x, y);
            else if (document.webkitCaretRangeFromPoint) range = document.webkitCaretRangeFromPoint(x, y);
            if (!range) return null;
            let el = null;
            if (range.startContainer && range.startContainer.nodeType === 3) {
                el = range.startContainer.parentElement;
            } else if (range.startContainer && range.startContainer.nodeType === 1) {
                el = range.startContainer;
            }
            if (!el) return null;
            // 定位「文本块容器」。**必须把题干/选项也算进来**：
            // 它们是 div（.question-text / .option / .choice-body），不在
            // p.paragraph|p.paragraph-option|p.intro 里，closest 会返回 null；
            // 而下面的兜底循环一旦从 span.word 起步，单字就满足
            // /[A-Za-z]{4,}/ && length<600 而把自己当成整块 →
            // 句子变成 "buried" → 被 showSentenceBubbleAt 的单词保护拦掉，
            // 表现为「翻译模式点题干/选项没反应」。
            const para = el.closest(
                'p.paragraph, p.paragraph-option, p.intro, ' +
                '.question-text, .option, .option-inline, .choice-body'
            ) || (function () {
                let node = el.parentElement;
                let hops = 0;
                while (node && node !== document.body && hops < 8) {
                    const tc = node.textContent || '';
                    // 跳过单字容器（span.word 及其同类），否则永远退不出单词
                    const isWordSpan = node.tagName === 'SPAN' &&
                        node.classList && node.classList.contains('word');
                    if (!isWordSpan && /[A-Za-z]{4,}/.test(tc) &&
                        tc.length >= 12 && tc.length < 600 && node.children.length <= 8) {
                        return node;
                    }
                    node = node.parentElement;
                    hops++;
                }
                return null;
            })();
            if (!para || !para.textContent) return null;
            // 剔除开头的题号/选项字母 badge 再切句：badge 是渲染层加的排版元素，
            // 不是正文（句库键里也没有）。否则 "21.Romans…" / "ASaving them…"
            // 切出来的句子与句库键对不上，表现为「点了没译文」。
            const badge = leadingBadgeLen(para);
            const full = para.textContent.slice(badge);
            let idx = full.length;
            if (range.startContainer && range.startContainer.nodeType === 3) {
                idx = 0;
                const walker = document.createTreeWalker(para, NodeFilter.SHOW_TEXT);
                let cur = null;
                let hit = false;
                while ((cur = walker.nextNode())) {
                    if (cur === range.startContainer) { idx += range.startOffset; hit = true; break; }
                    idx += (cur.textContent || '').length;
                }
                // walker 走的是含 badge 的原始坐标，换算到剔除后的坐标
                idx -= badge;
                if (idx < 0) idx = 0;
                if (idx > full.length) idx = full.length;
                if (!hit) idx = Math.min(range.startOffset, full.length);
            }
            const sentences = splitSentencesManual(full);
            let pos = 0;
            for (const s of sentences) {
                if (idx >= pos && idx <= pos + s.length) return { text: s, para: para };
                pos += s.length + 1;
            }
            return { text: full, para: para };
        } catch (err) {
            return null;
        }
    }

    function closeTranslateBubble() {
        if (translateBubble) translateBubble.style.display = 'none';
        translateText = '';
        translateZh = '';
        translateLastSentence = null;
        // 句译气泡关闭时同步清除句子高亮
        clearSentenceHighlight();
    }

    let translateSelectionTimer = null;
    // 最近一次单词点击时间戳（防延迟补发 mouseup/selectionchange 误关气泡）
    let lastWordTapAt = 0;
    let translateLastAnchor = null;
    // 触屏点词定位用的整句引用（para + 句文本），重定位时实时重算包围盒
    let translateLastSentence = null;
    function scheduleTranslateBubble() {
        // 触屏点击后浏览器会补发 mouseup / selectionchange（无选中）：
        // 此时不执行「无选中即关闭句译气泡」，否则刚点开的句译会一闪而过
        if (suppressClick || Date.now() - lastWordTapAt < 900) return;
        clearTimeout(translateSelectionTimer);
        translateSelectionTimer = setTimeout(showTranslateBubble, 30);
    }

    // 是否存在（正文内的）非空选区：用于决定悬停查词是否让位给划词/句译
    function hasTextSelection() {
        try {
            const sel = window.getSelection();
            if (!sel || sel.isCollapsed) return false;
            const root = document.querySelector('#examContent');
            return !!(root && sel.anchorNode && root.contains(sel.anchorNode));
        } catch (err) {
            return false;
        }
    }

    /* ==================== 自定义选区高亮层 ====================
       浏览器原生选区按字形渲染，空格没有字形所以高亮断档。
       这里用 Range.getClientRects() 的矩形（含空格）自绘高亮，
       让拖选/长按选中时空格处也有阴影，视觉连续。 */
    let selLayer = null;
    function ensureSelLayer() {
        if (selLayer) return selLayer;
        selLayer = document.createElement('div');
        selLayer.className = 'sel-highlight-layer';
        document.body.appendChild(selLayer);
        return selLayer;
    }

    function updateSelectionHighlight() {
        const layer = ensureSelLayer();
        layer.innerHTML = '';
        const root = document.querySelector('#examContent');
        if (!root) return;
        try {
            const sel = window.getSelection();
            if (!sel || sel.isCollapsed) return;
            if (!(sel.anchorNode && sel.focusNode &&
                  root.contains(sel.anchorNode) && root.contains(sel.focusNode))) return;
            const rects = sel.getRangeAt(0).getClientRects();
            for (const r of rects) {
                if (r.width < 1 || r.height < 1) continue;
                const d = document.createElement('div');
                d.className = 'sel-rect';
                d.style.left = r.left + 'px';
                d.style.top = r.top + 'px';
                d.style.width = r.width + 'px';
                d.style.height = r.height + 'px';
                layer.appendChild(d);
            }
        } catch (err) { /* ignore */ }
    }

    let selRaf = 0;
    function scheduleSelectionHighlight() {
        if (selRaf) return;
        selRaf = requestAnimationFrame(() => {
            selRaf = 0;
            updateSelectionHighlight();
        });
    }
    document.addEventListener('selectionchange', scheduleSelectionHighlight);
    window.addEventListener('scroll', scheduleSelectionHighlight, { passive: true, capture: true });
    window.addEventListener('resize', scheduleSelectionHighlight);
    // 兜底：点击空白 / 按 Esc 清空选区时，部分浏览器不触发 selectionchange，手动同步一次
    document.addEventListener('click', scheduleSelectionHighlight);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') scheduleSelectionHighlight();
    });

    window.addEventListener('scroll', () => {
        if (translateBubble && translateBubble.style.display !== 'none') {
            requestAnimationFrame(() => positionTranslateBubble(translateBubble));
        }
    }, { passive: true, capture: true });
    // 视口变化（手机地址栏收起/旋转等）：只重定位，不关闭句译气泡（否则点开即闪）
    window.addEventListener('resize', () => {
        if (translateBubble && translateBubble.style.display !== 'none') {
            requestAnimationFrame(() => positionTranslateBubble(translateBubble, translateLastAnchor));
        }
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeTranslateBubble();
    });
    document.addEventListener('click', (e) => {
        if (!translateBubble || translateBubble.style.display === 'none') return;
        if (e.target && e.target.closest && e.target.closest('.translate-bubble')) return;
        // 点单词（含触屏补发的 click）不关句译气泡——否则弹窗一闪而过
        if (e.target && e.target.closest && e.target.closest('span.word')) return;
        // 翻译模式下点题号/选项字母 badge（.question-num/.option-letter/.choice-letter）
        // 等**非 span.word** 区域同样会弹句译；这类位置浏览器补发的 click 不在上面的
        // 白名单里，会被当成「点空白」立刻关掉——表现为「点了没反应」。
        // 用与 touch 逻辑同一个 900ms 窗口兜底。
        if (dblMode === 'translate' && Date.now() - lastWordTapAt < 900) return;
        closeTranslateBubble();
    });
})();
