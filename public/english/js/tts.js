/* ============================================================
   单词发音（全局）
   优先：有道词典在线美音音频（手机上 speechSynthesis 经常无声）
   回退：浏览器内置 speechSynthesis（桌面端）
   用法：window.WordSpeak('word')
   ============================================================ */
(function () {
  'use strict';

  function synth(word) {
    try {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        var u = new SpeechSynthesisUtterance(word);
        u.lang = 'en-US';
        u.rate = 0.85;
        window.speechSynthesis.speak(u);
      }
    } catch (e) { /* 静默 */ }
  }

  window.WordSpeak = function (word) {
    var w = String(word == null ? '' : word).trim();
    if (!w) return;
    try {
      var a = new Audio('https://dict.youdao.com/dictvoice?audio=' + encodeURIComponent(w) + '&type=2');
      var p = a.play();
      if (p && p.catch) p.catch(function () { synth(w); });
    } catch (e) {
      synth(w);
    }
  };
})();
