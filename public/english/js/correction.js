/* ============================================================
   单词纠错弹窗（英语站）——对外 window.SrsCorrection = { open }
   提交到 /biochem/api/english-correction/（同域名 xm 服务器收集）
   2026-10-15：按用户反馈（english_corrections #55）改——**不强制填正确答案**，
   只标出「这块有问题」也能提交（word + 问题类型本身就是有效信息）。
   ============================================================ */
(function () {
  'use strict';

  var STYLE = [
    '#scr-overlay{position:fixed;inset:0;z-index:2147483100;background:rgba(16,24,22,.45);display:flex;align-items:center;justify-content:center;padding:20px;}',
    '#scr-card{width:100%;max-width:400px;background:#fff;border-radius:18px;padding:20px;box-shadow:0 24px 60px rgba(0,0,0,.25);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}',
    '#scr-title{display:flex;align-items:center;justify-content:space-between;font-size:16px;font-weight:700;color:#17211e;}',
    '#scr-title button{background:none;border:none;color:#7a8b86;font-size:18px;cursor:pointer;padding:2px 6px;border-radius:8px;}',
    '#scr-word{margin-top:4px;font-size:13px;color:#7a8b86;}',
    '#scr-hint{margin-top:8px;font-size:12px;color:#5c7a72;background:#f4f8f6;border-radius:8px;padding:8px 10px;line-height:1.55;}',
    '#scr-card label{display:block;font-size:12px;color:#4c6b63;margin-top:12px;font-weight:600;}',
    '#scr-kind{width:100%;margin-top:6px;padding:9px 10px;border:1px solid #d7e2dd;border-radius:10px;font-size:14px;background:#fff;color:#17211e;}',
    '#scr-content,#scr-note{width:100%;margin-top:6px;padding:9px 10px;border:1px solid #d7e2dd;border-radius:10px;font-size:14px;color:#17211e;box-sizing:border-box;resize:vertical;}',
    '#scr-actions{display:flex;gap:10px;margin-top:16px;}',
    '#scr-actions button{flex:1;padding:10px 0;border:none;border-radius:999px;font-size:14px;font-weight:600;cursor:pointer;}',
    '#scr-submit{background:#1f5d4a;color:#fff;}',
    '#scr-cancel{background:#f0f5f3;color:#33504a;}',
    '#scr-status{margin-top:10px;font-size:13px;text-align:center;color:#33504a;}',
    '#scr-status.ok{color:#1f5d4a;}',
    '#scr-status.err{color:#b4552f;}'
  ].join('\n');

  function escapeHtml(s) {
    if (s == null) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  var overlay = null;
  var submitBtn = null;
  var statusEl = null;
  var contentType = null;
  var keydownH = null;

  function close() {
    if (!overlay) return;
    overlay.remove();
    overlay = null;
    submitBtn = null;
    statusEl = null;
    contentType = null;
    if (keydownH) { document.removeEventListener('keydown', keydownH); keydownH = null; }
  }

  function open(word, display) {
    if (overlay) close();
    if (!document.getElementById('scr-style')) {
      var st = document.createElement('style');
      st.id = 'scr-style';
      st.textContent = STYLE;
      document.head.appendChild(st);
    }
    overlay = document.createElement('div');
    overlay.id = 'scr-overlay';
    overlay.innerHTML =
      '<div id="scr-card">' +
      '<div id="scr-title"><span>纠错</span><button id="scr-x" title="关闭">×</button></div>' +
      '<div id="scr-word">' + escapeHtml(display || word) + (display && display !== word ? '（' + escapeHtml(word) + '）' : '') + '</div>' +
      '<div id="scr-hint">只标出问题就行 —— <b>不必填正确答案</b>，我会去查。</div>' +
      '<label>问题类型</label>' +
      '<select id="scr-kind">' +
      '<option value="meaning">释义不对/不全</option>' +
      '<option value="phonetic">音标错</option>' +
      '<option value="example">例句错</option>' +
      '<option value="other">其他（正文/排版/功能）</option>' +
      '</select>' +
      '<label>修正内容（可选）</label>' +
      '<textarea id="scr-content" rows="3" placeholder="知道正确答案就写上；不知道也没关系，留空即可"></textarea>' +
      '<label>补充说明（可选）</label>' +
      '<input id="scr-note" placeholder="比如：2024 英一 T2 第 3 段 / 这句读不通" />' +
      '<div id="scr-actions">' +
      '<button id="scr-submit">提交纠错</button>' +
      '<button id="scr-cancel">取消</button>' +
      '</div>' +
      '<div id="scr-status"></div>' +
      '</div>';
    document.body.appendChild(overlay);
    submitBtn = overlay.querySelector('#scr-submit');
    statusEl = overlay.querySelector('#scr-status');
    contentType = overlay.querySelector('#scr-kind');

    overlay.querySelector('#scr-x').addEventListener('click', close);
    overlay.querySelector('#scr-cancel').addEventListener('click', close);
    overlay.addEventListener('click', function (e) { if (e.target === overlay) close(); });
    // Escape 只关纠错弹窗（不穿透到背后的面板——面板的 keydown 已屏蔽 #scr-overlay）
    keydownH = function (e) { if (e.key === 'Escape') { e.preventDefault(); close(); } };
    document.addEventListener('keydown', keydownH, true);
    overlay.querySelector('#scr-content').focus();

    submitBtn.addEventListener('click', function () {
      var content = overlay.querySelector('#scr-content').value.trim();
      var note = overlay.querySelector('#scr-note').value.trim();
      // 用户反馈（english_corrections #55）：不该强制他填「正确答案」，
      // 只要能标出「这块有问题」就够了。所以 content / note 全空也允许提交。
      //
      // 但**服务端还有一道 `if(!content && !note) → 400 请填写修正内容`**，
      // 而它的源码不在仓库里（src/app/api/ 下没有 english-correction，只有编译产物），
      // 没法从根上放宽。于是：用户什么都不填时，替他补一句说明再发——
      // 他一个键都不用敲，服务端也过得去，管理员看到这行就知道要去查。
      if (!content && !note) note = '（用户只标了问题，未填释义）';
      submitBtn.disabled = true;
      submitBtn.textContent = '提交中…';
      // CSRF Double-Submit：静态站无后端会话，前端生成本站 csrf cookie 并随请求带回
      var m = document.cookie.match(/(?:^|;\s*)csrf=([^;]+)/);
      var token = m ? m[1] : (crypto.randomUUID ? crypto.randomUUID().replace(/-/g, '') : (Math.random().toString(36).slice(2) + Date.now().toString(36)));
      if (!m) document.cookie = 'csrf=' + token + '; path=/; max-age=' + (365 * 24 * 3600) + '; SameSite=Strict';
      fetch(location.origin + '/biochem/api/english-correction/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': token },
        body: JSON.stringify({ word: word, kind: contentType.value, content: content, note: note }),
      })
        .then(function (r) {
          return r.json()
            .catch(function () { return { error: 'HTTP ' + r.status }; })
            .then(function (j) { return { ok: r.ok, j: j, status: r.status }; });
        })
        .then(function (res) {
          if (res.ok && res.j && res.j.ok) {
            statusEl.textContent = '✓ 纠错已保存在本机';
            statusEl.className = 'ok';
            setTimeout(close, 1200);
          } else {
            throw new Error((res.j && res.j.error) || 'HTTP ' + res.status);
          }
        })
        .catch(function (e) {
          statusEl.textContent = '提交失败（' + (e && e.message ? e.message : '网络') + '）。请稍后再试。';
          statusEl.className = 'err';
          submitBtn.disabled = false;
          submitBtn.textContent = '提交纠错';
        });
    });
  }

  window.SrsCorrection = { open: open, isOpen: function () { return !!overlay; } };
})();
