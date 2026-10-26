/* ============================================================
   单词背诵面板（SRS）——极简版
   对外：window.SrsPanel = { open, close, isOpen }
   依赖：srs-engine.js（全局 SrsEngine）、localStorage 词表 kyc_words_v1
   ============================================================ */
(function () {
  'use strict';

  // 词典 URL 必须带**内容戳**（部署时按文件 md5 生成）。
  // 这里以前写死 `data/dict.json?v=4`：换了词典、前端还在请求那个老 URL，
  // 于是手机继续吃 CDN 里旧那份（app.js 早就改成读 version.json 了）。
  // version.json 本身是 no-store，很小，读一次就够。
  var DICT_URL = 'data/dict.json';
  var dictUrlResolved = null;
  function resolveDictUrl() {
    if (dictUrlResolved) return Promise.resolve(dictUrlResolved);
    return fetch('data/version.json', { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (v) {
        dictUrlResolved = 'data/dict.json?v=' + ((v && v.dict) || '0');
        return dictUrlResolved;
      })
      .catch(function () { return DICT_URL; });
  }
  var STYLE = [
    '.srs-overlay{position:fixed;inset:0;z-index:2147483000;background:rgba(16,24,22,.45);display:flex;align-items:center;justify-content:center;padding:0;}',
    '.srs-panel{position:relative;width:100%;max-width:480px;background:#fff;display:flex;flex-direction:column;height:100%;max-height:100vh;box-shadow:0 24px 60px rgba(0,0,0,.22);}',
    '@media(min-width:560px){.srs-panel{height:auto;max-height:88vh;border-radius:20px;margin:24px;overflow:hidden;}}',
    // 头部：一行 = 计数 + 发音 + 纠错 + 菜单
    '.srs-head{flex:0 0 auto;display:flex;align-items:center;justify-content:space-between;gap:8px;padding:12px 16px;border-bottom:1px solid #eef2f0;}',
    '.srs-count{font-size:13px;font-weight:600;color:#7a8b86;letter-spacing:.5px;}',
    '.srs-head-btns{display:flex;align-items:center;gap:2px;}',
    '.srs-hbtn{width:34px;height:34px;border:none;background:transparent;border-radius:9px;color:#4c6b63;display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0;}',
    '.srs-hbtn:hover{background:#f0f5f3;color:#1f5d4a;}',
    '.srs-hbtn svg{width:19px;height:19px;}',
    '.srs-hbtn.srs-off{color:#b9c6c1;}',
    // 主体
    '.srs-body{flex:1 1 auto;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:28px 24px;}',
    '.srs-word{font-size:38px;font-weight:700;color:#17211e;text-align:center;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;letter-spacing:-.5px;line-height:1.1;word-break:break-word;cursor:pointer;}',
    '.srs-phon{font-size:15px;color:#7a8b86;text-align:center;margin-top:8px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}',
    '.srs-top-hint{text-align:center;margin-top:26px;color:#a3b1ac;font-size:14px;}',
    '.srs-flip-btn{display:block;margin:26px auto 0;padding:11px 22px;border:none;border-radius:999px;background:#f0f5f3;color:#1f5d4a;font-size:15px;font-weight:600;cursor:pointer;}',
    '.srs-flip-btn:hover{background:#e2ede8;}',
    '.srs-senses{margin-top:24px;background:#f7faf8;border:1px solid #e6efec;border-radius:14px;padding:16px 18px;}',
    '.srs-sense{display:flex;gap:10px;padding:6px 0;font-size:15px;line-height:1.55;color:#22302d;}',
    '.srs-sense + .srs-sense{border-top:1px dashed #e2ebe8;}',
    '.srs-sense-pos{flex:0 0 auto;min-width:20px;color:#1f5d4a;font-weight:700;}',
    '.srs-missing{color:#a3b1ac;text-align:center;padding:14px 0;font-size:14px;}',
    // 底部：三档大按钮
    '.srs-foot{flex:0 0 auto;padding:12px 16px calc(14px + env(safe-area-inset-bottom));border-top:1px solid #eef2f0;}',
    '.srs-rate{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;}',
    '.srs-rate-btn{border:none;border-radius:14px;padding:15px 0;font-size:16px;font-weight:600;cursor:pointer;color:#fff;transition:transform .08s ease,filter .08s ease;}',
    '.srs-rate-btn:active{transform:scale(.97);}',
    '.srs-rate-forgot{background:#b4552f;}',
    '.srs-rate-fuzzy{background:#c99a45;}',
    '.srs-rate-known{background:#1f5d4a;}',
    '.srs-rate-label{display:block;}',
    '.srs-interval{display:block;font-size:11px;font-weight:400;opacity:.85;margin-top:2px;}',
    // 菜单
    '.srs-menu{position:absolute;top:52px;right:12px;min-width:180px;background:#fff;border:1px solid #e6efec;border-radius:14px;box-shadow:0 12px 30px rgba(0,0,0,.14);padding:6px;z-index:2;}',
    '.srs-menu-item{display:flex;align-items:center;gap:8px;width:100%;border:none;background:none;text-align:left;padding:10px 12px;border-radius:9px;font-size:14px;color:#2b3a36;cursor:pointer;}',
    '.srs-menu-item:hover{background:#f0f5f3;}',
    '.srs-menu-item.srs-danger{color:#b4552f;}',
    '.srs-menu-title{font-size:11px;color:#9caca7;padding:8px 12px 4px;letter-spacing:.4px;}',
    '.srs-menu-paused{margin:2px 8px 6px;padding:6px 4px;border-top:1px dashed #e6efec;max-height:160px;overflow:auto;}',
    '.srs-paused-row{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:7px 8px;border-radius:8px;font-size:13px;color:#2b3a36;}',
    '.srs-paused-row:hover{background:#f7faf8;}',
    '.srs-paused-word{font-weight:600;}',
    '.srs-paused-act{font-size:12px;color:#1f5d4a;cursor:pointer;background:none;border:none;padding:0 6px;}',
    '.srs-paused-act.srs-danger{color:#b4552f;}',
    // 空态/完成态
    '.srs-empty,.srs-done{text-align:center;padding:34px 8px;}',
    '.srs-empty{color:#7a8b86;font-size:15px;line-height:1.7;}',
    '.srs-empty strong{display:block;margin-bottom:6px;font-size:17px;color:#17211e;}',
    '.srs-done-count{font-size:26px;font-weight:700;color:#1f5d4a;margin-bottom:8px;}',
    '.srs-done-stats{font-size:15px;color:#3b4a46;margin-bottom:8px;}',
    '.srs-done-remain{font-size:13px;color:#8a9b95;margin-bottom:12px;}',
    '.srs-done-limit{font-size:13px;color:#3b4a46;margin-bottom:5px;}',
    '.srs-done-limit input{width:58px;padding:5px 7px;border:1px solid #d7e2dd;border-radius:8px;font-size:13px;margin:0 4px;}',
    '.srs-done-limit-hint{display:block;font-size:12px;color:#9caca7;margin-bottom:16px;}',
    '.srs-primary{display:inline-flex;align-items:center;justify-content:center;min-width:120px;padding:11px 20px;border:none;border-radius:999px;background:#1f5d4a;color:#fff;font-size:15px;font-weight:600;cursor:pointer;margin:0 6px;}',
    '.srs-primary:hover{background:#174a3a;}',
    '.srs-ghost{display:inline-flex;align-items:center;justify-content:center;min-width:96px;padding:11px 18px;border:1px solid #d7e2dd;border-radius:999px;background:#fff;color:#33504a;font-size:14px;cursor:pointer;margin:0 6px;}',
    '.srs-ghost:hover{background:#f0f5f3;}',
    // 可访问 + 克制动效
    '.srs-panel button:focus-visible{outline:2px solid #1f5d4a;outline-offset:2px;}',
    '@media(prefers-reduced-motion:reduce){.srs-rate-btn{transition:none;}}'
  ].join('\n');

  // ==================== 状态 ====================
  var overlay = null;
  var dictCache = null;
  var dictPending = null;
  var ttsEnabled = localStorage.getItem('aseeker_english_srs_tts') !== '0';
  var keydownHandler = null;
  var menuOpen = false;

  var session = {
    phase: 'idle',
    wordsMap: {},
    data: null,
    study: [],
    index: 0,
    flipped: false,
    counts: { known: 0, fuzzy: 0, forgot: 0 },
    /** 今日待新学（剩余；毕业/跳过/暂停/删除递减） */
    remainNew: 0,
    /** 今日待复习（剩余；毕业/跳过/暂停/删除递减） */
    remainReview: 0,
    newRemaining: 0,
    reviewRemaining: 0
  };

  function loadLimits() {
    try {
      var raw = JSON.parse(localStorage.getItem('aseeker_english_srs_limits_v1') || 'null');
      if (raw && typeof raw.newPerDay === 'number' && typeof raw.reviewPerDay === 'number') {
        return { newPerDay: Math.max(0, Math.min(200, raw.newPerDay)), reviewPerDay: Math.max(0, Math.min(200, raw.reviewPerDay)) };
      }
    } catch (e) {}
    return { newPerDay: 20, reviewPerDay: 50 };
  }
  function saveLimits(l) {
    try { localStorage.setItem('aseeker_english_srs_limits_v1', JSON.stringify(l)); } catch (e) {}
  }

  // ==================== 工具 ====================
  function normalizeWord(w) { return String(w).toLowerCase().replace(/[^a-z'\s-]/g, '').replace(/\s+/g, ' ').trim(); }
  function escapeHtml(s) {
    if (s == null) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function posLabel(p) {
    var map = { n: '名', v: '动', vt: '动', vi: '动', a: '形', ad: '副', adv: '副', prep: '介', conj: '连', pron: '代', num: '数', art: '冠' };
    return map[p] || p || '';
  }
  function formatInterval(dueMs, nowMs) {
    var diff = dueMs - nowMs;
    if (diff <= 0) return '现在';
    var min = Math.round(diff / 60000);
    if (min < 60) return min + ' 分钟';
    var hr = Math.round(diff / 3600000);
    if (hr < 24) return hr + ' 小时';
    return Math.round(diff / 86400000) + ' 天后';
  }

  var SPEAKER_ON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a9 9 0 0 1 0 14"/></svg>';
  var SPEAKER_OFF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4z"/><line x1="16" y1="9" x2="22" y2="15"/><line x1="22" y1="9" x2="16" y2="15"/></svg>';
  var DOTS = '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="5" cy="12" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="19" cy="12" r="1.6"/></svg>';
  var XICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';
  var PENCIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h4L19.5 8.5l-4-4L4 16v4z"/><path d="M13.5 6.5l4 4"/></svg>';

  // ==================== 词库 ====================
  function loadDict() {
    if (dictCache) return Promise.resolve(dictCache);
    if (dictPending) return dictPending;
    dictPending = resolveDictUrl()
      .then(function (u) { return fetch(u); })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (d) { dictCache = d; dictPending = null; return d; })
      .catch(function (e) { dictPending = null; throw e; });
    return dictPending;
  }
  function lookupDict(word) {
    if (window.EnglishPrecision) { var study = window.EnglishPrecision.studyEntry(word); if (study) return study; }
    if (!dictCache) return null;
    var dict = dictCache.dict || {};
    var key = normalizeWord(word);
    if (dict[key]) return dict[key];
    var stems = [];
    if (key.endsWith('ies')) stems.push(key.slice(0, -3) + 'y');
    if (key.endsWith('ing')) stems.push(key.slice(0, -3), key.slice(0, -3) + 'e');
    if (key.endsWith('ed')) stems.push(key.slice(0, -2), key.slice(0, -1));
    if (key.endsWith('es')) stems.push(key.slice(0, -2), key.slice(0, -1));
    if (key.endsWith('s')) stems.push(key.slice(0, -1));
    for (var i = 0; i < stems.length; i++) { if (stems[i] && stems[i] !== key && dict[stems[i]]) return dict[stems[i]]; }
    return null;
  }

  // ==================== TTS ====================
  function speak(word) {
    if (!ttsEnabled) return;
    // 优先在线音频（手机 speechSynthesis 常无声），全局 WordSpeak 自带回退
    if (window.WordSpeak) { window.WordSpeak(word); return; }
    if (!('speechSynthesis' in window)) return;
    try { window.speechSynthesis.cancel(); } catch (e) {}
    var u = new SpeechSynthesisUtterance(word);
    u.lang = 'en-US';
    u.rate = 0.85;
    window.speechSynthesis.speak(u);
  }
  function toggleTts() { ttsEnabled = !ttsEnabled; localStorage.setItem('aseeker_english_srs_tts', ttsEnabled ? '1' : '0'); }

  // ==================== 存储 ====================
  function loadWords() {
    try { return JSON.parse(localStorage.getItem('kyc_words_v1') || '{}'); } catch (e) { return {}; }
  }

  // ==================== 会话 ====================
  function buildSession() {
    menuOpen = false;
    session.wordsMap = loadWords();
    var keys = Object.keys(session.wordsMap);
    session.data = SrsEngine.loadEnglishSrs(localStorage);
    session.data.cards = SrsEngine.ensureWordCards(session.data.cards, keys, new Date());
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    var domain = {};
    for (var i = 0; i < keys.length; i++) { domain[keys[i]] = SrsEngine.wordCardState(session.data.cards[keys[i]]); }
    var plan = SrsEngine.planQueue(Object.keys(domain).map(function (k) { return domain[k]; }), new Date(), loadLimits());
    // 重新映射 key + 分桶（新学/复习）
    var items = plan.newCards.concat(plan.due).map(function (c) {
      var k = Object.keys(domain).find(function (x) { return domain[x] === c; });
      return { key: k, card: c, bucket: plan.newCards.indexOf(c) >= 0 ? 'new' : 'review' };
    });
    session.study = items;
    session.index = 0;
    session.flipped = false;
    session.counts = { known: 0, fuzzy: 0, forgot: 0 };
    session.remainNew = plan.newCards.length;
    session.remainReview = plan.due.length;
    session.newRemaining = plan.newRemaining;
    session.reviewRemaining = plan.reviewRemaining;

    if (keys.length === 0) { session.phase = 'empty'; }
    else if (items.length === 0) { session.phase = 'done'; }
    else { session.phase = 'study'; }
    render();
  }

  function currentEntry() { return session.study[session.index]; }
  function displayWord(key) { var w = session.wordsMap[key]; return w ? (w.word || key) : key; }

  // ==================== 渲染 ====================
  function render() {
    if (!overlay) return;
    // 清除残留菜单（任何动作后菜单 DOM 都要同步消失——之前这个 bug 会留下"关不掉"的菜单）；
    // 菜单打开期间的普通重渲染（如词典加载完成）不能把它关掉
    if (!menuOpen) {
      var stale = overlay.querySelector('.srs-menu');
      if (stale) stale.remove();
    }
    var body = overlay.querySelector('.srs-body');
    var foot = overlay.querySelector('.srs-foot');
    var head = overlay.querySelector('.srs-head');
    renderHead(head);
    if (session.phase === 'error') { renderError(body); foot.innerHTML = ''; return; }
    if (session.phase === 'empty') { renderEmpty(body); foot.innerHTML = ''; return; }
    if (session.phase === 'done') { renderDone(body); foot.innerHTML = ''; return; }
    renderCard(body, foot);
    // 注意：这里不再把 menuOpen 置 false——词典后台加载等普通重渲染不能关闭菜单；
    // 菜单只由动作（评分/跳过/暂停/删除/点空白）关闭（对应函数先置 false 再 render）。
  }

  function renderError(body) {
    body.innerHTML = '<div class="srs-empty"><strong>加载出错了</strong>' +
      escapeHtml(session.error || '未知错误') +
      '<div style="margin-top:10px"><button class="srs-primary" data-act="close">关闭</button></div></div>';
  }

  function renderHead(head) {
    var text = session.phase === 'study' || session.phase === 'done'
      ? '今日待新学 ' + session.remainNew + ' 张 · 待复习 ' + session.remainReview + ' 张'
      : '';
    head.innerHTML =
      '<span class="srs-count">' + text + '</span>' +
      '<div class="srs-head-btns">' +
      '<button class="srs-hbtn' + (ttsEnabled ? '' : ' srs-off') + '" data-act="tts" title="发音开关">' + (ttsEnabled ? SPEAKER_ON : SPEAKER_OFF) + '</button>' +
      (session.phase === 'study' ? '<button class="srs-hbtn" data-act="correct" title="纠错这个词">' + PENCIL + '</button>' : '') +
      (session.phase === 'study' ? '<button class="srs-hbtn" data-act="menu" title="更多">' + DOTS + '</button>' : '') +
      '<button class="srs-hbtn" data-act="close" title="关闭">' + XICON + '</button>' +
      '</div>';
  }

  function renderEmpty(body) {
    body.innerHTML = '<div class="srs-empty"><strong>生词本还没有收藏的单词</strong>去真题里点一点英文单词，就能开始背了。</div>';
  }

  function renderDone(body) {
    var c = session.counts;
    var lim = loadLimits();
    var remain = session.newRemaining + session.reviewRemaining;
    body.innerHTML = '<div class="srs-done">' +
      '<p class="srs-done-count">今日复习完成</p>' +
      '<p class="srs-done-stats">认识 <b>' + c.known + '</b> · 模糊 <b>' + c.fuzzy + '</b> · 忘记 <b>' + c.forgot + '</b></p>' +
      '<p class="srs-done-remain">新词剩余 ' + session.newRemaining + ' · 复习剩余 ' + session.reviewRemaining +
        (remain > 0 ? '（调大每日学习量可继续）' : '') + '</p>' +
      '<div class="srs-done-limit">每日学习量：新词 <input type="number" min="0" max="200" value="' + lim.newPerDay + '" data-lim="new" /> · ' +
      '复习 <input type="number" min="0" max="200" value="' + lim.reviewPerDay + '" data-lim="rev" /></div>' +
      '<span class="srs-done-limit-hint">改完自动重排</span>' +
      '<button class="srs-primary" data-act="done">完成</button>' +
      '</div>';
    bindLimitInputs(body);
  }

  function renderCard(body, foot) {
    var entry = currentEntry();
    if (!entry) { session.phase = 'done'; renderDone(body); return; }
    var key = entry.key;
    var word = displayWord(key);
    var dict = lookupDict(key);
    var ph = dict && dict.ph ? dict.ph : '';

    // 未翻面：单词不绑定发音（点了整卡翻面，翻面时自动发音）；
    // 已翻面：点单词重新发音
    var html = '<div class="srs-word"' + (session.flipped ? ' data-act="speak"' : '') + '>' + escapeHtml(word) + '</div>';
    html += (ph ? '<div class="srs-phon">' + escapeHtml(ph) + '</div>' : '');

    if (!session.flipped) {
      html += '<div class="srs-top-hint">回想一下意思</div>' +
        '<button class="srs-flip-btn" data-act="flip">' + (!dictCache && dictPending ? '释义加载中…' : '显示释义') + '</button>';
      if (!dict && !dictPending) html += '<div class="srs-missing">（这个词暂无释义）</div>';
    } else {
      if (dict && dict.s && dict.s.length) {
        html += '<div class="srs-senses">' + dict.s.slice(0, 3).map(function (s) {
          return '<div class="srs-sense"><span class="srs-sense-pos">' + escapeHtml(posLabel(s.p)) + '</span><span>' + escapeHtml(s.t) + '</span></div>';
        }).join('') + '</div>';
      }
      if (dict && dict._partial) html += '<div class="srs-missing">释义参考：' + escapeHtml(dict._partial) + '</div>';
      if (!dict && !dictPending) html += '<div class="srs-missing">（这个词暂无释义）</div>';
    }
    body.innerHTML = html;

    // 底部：三档（墨墨格式）
    //  当天首见   → 小字 = 按下后"下次见到在第几天"（长期规划天数；认识 = 墨墨官方 5 天后）；
    //  当天非首见 → 小字 = 按下去后的「今日进度 %」；按下去即毕业（100%）= 模型 X 天后。
    if (session.flipped) {
      var now = new Date();
      var dayFresh = SrsEngine.isDayFresh(entry.card, now);
      var name = ['forgot', 'fuzzy', 'known'];
      var label = ['忘记', '模糊', '认识'];
      var cls = ['srs-rate-forgot', 'srs-rate-fuzzy', 'srs-rate-known'];
      var row = '';
      for (var i = 0; i < 3; i++) {
        var sub;
        if (dayFresh) {
          var d = SrsEngine.FRESH_PLAN_DAYS[name[i]];
          sub = d + ' 天后';
        } else {
          var level = SrsEngine.projectLevel(entry.card, name[i], now);
          sub = level >= 5
            ? formatInterval(SrsEngine.previewDue(entry.card, name[i], now), now.getTime())
            : '今日进度' + SrsEngine.todayLevelPercent(level) + '%';
        }
        row += '<button class="srs-rate-btn ' + cls[i] + '" data-act="rate" data-rating="' + name[i] + '">' +
          '<span class="srs-rate-label">' + label[i] + '</span>' +
          '<span class="srs-interval">' + sub + '</span>' +
          '</button>';
      }
      var hint = '';
      if ((entry.card.againStreak || 0) >= 3) {
        hint = '<div style="text-align:center;margin-top:10px;font-size:12px;color:#8a9b95">已多次忘记 · <button style="color:#1f5d4a;background:none;border:none;cursor:pointer;padding:0" data-act="tomorrow">今天先到这，明天再见 →</button></div>';
      }
      foot.innerHTML = '<div class="srs-rate">' + row + '</div>' + hint;
    } else {
      foot.innerHTML = '<div class="srs-top-hint" style="margin:0;font-size:12px;color:#9caca7">点击卡片显示释义 · 选择忘记/模糊/认识</div>';
    }
  }

  // ==================== 菜单 ====================
  /** 每日学习量输入（菜单与完成屏共用）：改完保存并重排队列 */
  function bindLimitInputs(scope) {
    var inputs = scope.querySelectorAll('input[data-lim]');
    inputs.forEach(function (inp) {
      inp.addEventListener('change', function () {
        var l = loadLimits();
        if (inp.getAttribute('data-lim') === 'new') l.newPerDay = Math.max(0, Math.min(200, Number(inp.value) || 0));
        else l.reviewPerDay = Math.max(0, Math.min(200, Number(inp.value) || 0));
        saveLimits(l);
        buildSession();
      });
    });
  }
  function renderMenu() {
    var old = overlay.querySelector('.srs-menu');
    if (old) old.remove();
    if (!menuOpen) return;
    var paused = Object.keys(session.data.cards).filter(function (k) { return session.data.cards[k].leeched && !session.data.cards[k].deleted; });
    var menu = document.createElement('div');
    menu.className = 'srs-menu';
    var lim = loadLimits();
    var rows = '<div class="srs-menu-title">每日学习量</div>' +
      '<div class="srs-menu-paused" style="border:none;margin:2px 4px 6px;padding:4px">' +
      '新词 <input type="number" min="0" max="200" value="' + lim.newPerDay + '" style="width:56px;padding:4px 6px;border:1px solid #d7e2dd;border-radius:8px;font-size:13px" data-lim="new" />' +
      ' 复习 <input type="number" min="0" max="200" value="' + lim.reviewPerDay + '" style="width:56px;padding:4px 6px;border:1px solid #d7e2dd;border-radius:8px;font-size:13px" data-lim="rev" />' +
      '</div>' +
      '<button class="srs-menu-item" data-act="skip">今天跳过这张卡</button>' +
      '<button class="srs-menu-item" data-act="pause">暂停这张卡</button>' +
      '<button class="srs-menu-item srs-danger" data-act="del">删除这张卡</button>';
    if (paused.length) {
      rows += '<div class="srs-menu-title">已暂停 ' + paused.length + ' 张</div>' +
        '<div class="srs-menu-paused">' + paused.map(function (k) {
          return '<div class="srs-paused-row"><span class="srs-paused-word">#' + escapeHtml(displayWord(k)) + '</span>' +
            '<button class="srs-paused-act" data-act="restore" data-key="' + escapeHtml(k) + '">恢复</button>' +
            '<button class="srs-paused-act srs-danger" data-act="delP" data-key="' + escapeHtml(k) + '">删</button></div>';
        }).join('') + '</div>';
    }
    menu.innerHTML = rows;
    overlay.querySelector('.srs-panel').appendChild(menu);
    // 限额输入：change（回车/失焦）即生效并重排
    bindLimitInputs(menu);
  }

  // ==================== 动作 ====================
  /** 今日剩余计数递减（新学/复习各自独立） */
  function settleRemaining(bucket) {
    if (bucket === 'new') session.remainNew = Math.max(0, session.remainNew - 1);
    else session.remainReview = Math.max(0, session.remainReview - 1);
  }
  function flip() { if (!session.flipped) { session.flipped = true; speak(displayWord(currentEntry().key)); } render(); }
  function rate(rating) {
    if (session.phase !== 'study' || !session.flipped) return;
    menuOpen = false;
    var entry = currentEntry();
    if (!entry) return;
    var now = new Date();
    var next = SrsEngine.gradeCard(entry.card, rating, now);
    session.data.cards[entry.key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    session.counts[rating] += 1;
    // 掌握度满 5（100%）= 毕业（今天离队，N/M +1）；
    // 未毕业 → 扩展检索式隔词重插（第 1 次隔 3 张，每多一次当天评分 +1，难词再 +1/+2，封顶 8）
    if (next.todayLevel >= 5) {
      settleRemaining(entry.bucket);
    } else {
      var pos = SrsEngine.sessionReinsertPos(session.index, session.study.length, next.todayReps, next.card.difficulty);
      session.study.splice(pos, 0, { key: entry.key, card: next, bucket: entry.bucket });
    }
    session.index += 1;
    session.flipped = false;
    if (session.index >= session.study.length) session.phase = 'done';
    render();
  }
  function skip() {
    if (session.phase !== 'study') return;
    menuOpen = false;
    var entry = currentEntry();
    if (!entry) return;
    var next = SrsEngine.skipCard(entry.card, new Date());
    session.data.cards[entry.key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    session.index += 1; session.flipped = false;
    settleRemaining(entry.bucket);
    if (session.index >= session.study.length) session.phase = 'done';
    render();
  }
  function tomorrowCard() { skip(); }
  function pauseCurrent() {
    if (session.phase !== 'study') return;
    menuOpen = false;
    var entry = currentEntry();
    if (!entry) return;
    var next = SrsEngine.pauseCard(entry.card, new Date());
    session.data.cards[entry.key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    session.index += 1; session.flipped = false;
    settleRemaining(entry.bucket);
    if (session.index >= session.study.length) session.phase = 'done';
    render();
  }
  function delCurrent() {
    if (session.phase !== 'study') return;
    menuOpen = false;
    var entry = currentEntry();
    if (!entry) return;
    var word = displayWord(entry.key);
    if (!window.confirm('删除「' + word + '」的背诵记录？不会取消收藏。')) return;
    var next = SrsEngine.deleteCard(entry.card, new Date());
    session.data.cards[entry.key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    session.study.splice(session.index, 1);
    settleRemaining(entry.bucket);
    if (session.index >= session.study.length) session.phase = 'done';
    render();
  }
  function restore(key) {
    var wire = session.data.cards[key];
    if (!wire) return;
    var next = SrsEngine.unleashCard(SrsEngine.wordCardState(wire), new Date());
    session.data.cards[key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    buildSession();
  }
  function delPaused(key) {
    var wire = session.data.cards[key];
    if (!wire) return;
    if (!window.confirm('删除「' + displayWord(key) + '」的背诵记录？')) return;
    var next = SrsEngine.deleteCard(SrsEngine.wordCardState(wire), new Date());
    session.data.cards[key] = SrsEngine.wordCardWire(next);
    SrsEngine.saveEnglishSrs(localStorage, session.data);
    buildSession();
  }

  // ==================== DOM 构建 / 事件 ====================
  function buildOverlay() {
    // 样式注入（一次性）：重写面板时曾丢过这一步——面板会"已打开但不可见"
    if (!document.getElementById('srs-panel-style')) {
      var st = document.createElement('style');
      st.id = 'srs-panel-style';
      st.textContent = STYLE;
      document.head.appendChild(st);
    }
    overlay = document.createElement('div');
    overlay.className = 'srs-overlay';
    overlay.innerHTML =
      '<div class="srs-panel">' +
      '<div class="srs-head"></div>' +
      '<div class="srs-body"></div>' +
      '<div class="srs-foot"></div>' +
      '</div>';
    document.body.appendChild(overlay);
    overlay.addEventListener('click', function (e) {
      var actBtn = e.target.closest('[data-act]');
      if (actBtn) {
        var act = actBtn.getAttribute('data-act');
        if (act === 'close') { close(); return; }
        if (act === 'menu') { menuOpen = !menuOpen; renderMenu(); return; }
        if (act === 'tts') { toggleTts(); render(); return; }
        if (act === 'flip') { flip(); return; }
        if (act === 'speak') { speak(displayWord(currentEntry().key)); return; }
        if (act === 'rate') { rate(actBtn.getAttribute('data-rating')); return; }
        if (act === 'skip') { skip(); return; }
        if (act === 'pause') { pauseCurrent(); return; }
        if (act === 'correct') {
          var ce = currentEntry();
          if (ce && window.SrsCorrection) window.SrsCorrection.open(ce.key, displayWord(ce.key));
          return;
        }
        if (act === 'del') { delCurrent(); return; }
        if (act === 'restore') { restore(actBtn.getAttribute('data-key')); return; }
        if (act === 'delP') { delPaused(actBtn.getAttribute('data-key')); return; }
        if (act === 'tomorrow') { tomorrowCard(); return; }
        if (act === 'done') { close(); return; }
        return;
      }
      // 点在菜单内部（输入框等）不关闭菜单
      if (e.target.closest('.srs-menu')) return;
      // 点空白关闭菜单
      if (menuOpen) { menuOpen = false; renderMenu(); return; }
      // 点卡片白色区域直接翻面显示释义（手机没键盘，空格键不可用）
      if (session.phase === 'study' && !session.flipped && e.target.closest('.srs-body')) { flip(); return; }
    });
    keydownHandler = function (e) {
      var tag = (document.activeElement && document.activeElement.tagName) || '';
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
      // 纠错弹窗（z-index 更高、叠在面板之上）打开时：键盘事件归它，别把 1/2/3 打到下面的卡上
      if (document.activeElement && document.activeElement.closest && document.activeElement.closest('#scr-overlay')) return;
      if (e.key === 'Escape') { close(); return; }
      if (session.phase !== 'study') return;
      if (e.key === ' ') { e.preventDefault(); flip(); return; }
      if (e.key === '1') rate('forgot');
      else if (e.key === '2') rate('fuzzy');
      else if (e.key === '3') rate('known');
    };
    window.addEventListener('keydown', keydownHandler);
  }

  function open() {
    if (!window.SrsEngine) { alert('页面未加载完整，请刷新后重试'); return; }
    if (overlay) { close(); }
    buildOverlay();
    // 锁背景滚动（与释义面板行为一致；关闭时恢复）
    document.body.style.overflow = 'hidden';
    // 先渲染会话（不等待 4.9MB 词典——否则手机上会先白屏几秒，看起来像"没反应"）
    try { buildSession(); }
    catch (e) {
      session.phase = 'error';
      session.error = (e && e.message) ? e.message : String(e);
      if (window.console && console.error) console.error('[srs-panel] buildSession failed:', e);
      render();
    }
    // 词典后台加载，就绪后重渲染一次
    loadDict().then(function () { if (overlay) render(); })
      .catch(function () { dictPending = null; if (overlay) render(); });
  }
  function close() {
    if (!overlay) return;
    if (keydownHandler) { window.removeEventListener('keydown', keydownHandler); keydownHandler = null; }
    overlay.remove(); overlay = null; menuOpen = false;
    document.body.style.overflow = '';
    if (session.phase === 'study' && session.data) SrsEngine.saveEnglishSrs(localStorage, session.data);
  }
  function isOpen() { return !!overlay; }

  window.SrsPanel = { open: open, close: close, isOpen: isOpen };
})();
