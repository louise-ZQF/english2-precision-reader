/* Static-host adapter. Study data and feedback stay in this browser. */
(function () {
  'use strict';
  if (!window.EnglishHosting || window.EnglishHosting.mode !== 'static') return;
  const nativeFetch = window.fetch.bind(window);
  const base = window.EnglishHosting.base || '';
  const reply = (data, status) => new Response(JSON.stringify(data), { status: status || 200, headers: { 'Content-Type': 'application/json' } });
  window.fetch = async function (input, options) {
    const raw = typeof input === 'string' ? input : input.url;
    const url = new URL(raw, location.href);
    const path = base && url.pathname.startsWith(base + '/') ? url.pathname.slice(base.length) : url.pathname;
    if (url.origin !== location.origin || !path.startsWith('/biochem/api/')) return nativeFetch(input, options);
    if (path === '/biochem/api/check/') return reply({ ok: false }, 401);
    if (path.startsWith('/biochem/api/backup/')) return reply({ ok: false, error: '网页版请使用数据文件导出和导入，不提供扫码中转。' }, 501);
    const stores = { '/biochem/api/feedback/': 'english2_local_feedback_v1', '/biochem/api/english-correction/': 'english2_local_corrections_v1' };
    const key = stores[path];
    if (!key) return reply({ ok: false, error: '网页版没有此服务' }, 404);
    try {
      const body = JSON.parse(options && options.body || '{}');
      const rows = JSON.parse(localStorage.getItem(key) || '[]');
      rows.push({ ...body, createdAt: new Date().toISOString() });
      localStorage.setItem(key, JSON.stringify(rows));
      return reply({ ok: true, local: true });
    } catch (_) { return reply({ ok: false, error: '浏览器保存失败，请先导出数据。' }, 507); }
  };
  function adapt() {
    const share = document.getElementById('scanShareBtn');
    if (share) share.hidden = true;
    const result = document.getElementById('scanResult');
    if (result) { result.hidden = true; result.style.display = 'none'; }
    const modal = document.getElementById('backupModal');
    if (modal) {
      modal.querySelectorAll('p').forEach(p => {
        if (p.textContent.includes('24 小时') || p.textContent.includes('扫描二维码')) p.textContent = '网页版使用导出文件备份与迁移，收藏和练习记录保存在当前浏览器。';
      });
    }
    const friend = document.getElementById('friendBtn');
    if (friend) friend.hidden = true;
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', adapt); else adapt();
})();
