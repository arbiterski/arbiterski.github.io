(() => {
  const button = document.getElementById('language');
  const query = new URLSearchParams(location.search).get('lang');
  let stored;
  try { stored = localStorage.getItem('research-language'); } catch (_) {}
  let language = query === 'en' || query === 'zh' ? query : stored || 'zh';
  function render() {
    document.documentElement.lang = language === 'zh' ? 'zh-Hant' : 'en';
    document.querySelectorAll('[data-zh][data-en]').forEach(element => {
      element.textContent = element.dataset[language];
    });
    button.textContent = language === 'zh' ? 'English' : '中文';
    button.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : '切換中文');
    const title = document.querySelector('h1');
    if (title) document.title = `${title.textContent.replace(/\n/g, ' ')} | Ming-Chin Lin Research`;
    // Keep the language in local links so shared URLs also retain it.
    document.querySelectorAll('a[href]').forEach(link => {
      const url = new URL(link.getAttribute('href'), location.href);
      if (url.origin === location.origin && url.pathname.includes('/research') && !/\.(svg|png)$/.test(url.pathname)) {
        url.searchParams.set('lang', language);
        link.href = url.href;
      }
    });
  }
  button.addEventListener('click', () => {
    language = language === 'zh' ? 'en' : 'zh';
    try { localStorage.setItem('research-language', language); } catch (_) {}
    const url = new URL(location.href);
    url.searchParams.set('lang', language);
    history.replaceState(null, '', url);
    render();
  });
  document.querySelector('.print').addEventListener('click', () => window.print());
  render();
})();
