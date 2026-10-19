// YouTube Scraper Popup Script

document.addEventListener('DOMContentLoaded', async () => {
  const statusBadge = document.getElementById('statusBadge');
  const scrapeBtn = document.getElementById('scrapeBtn');
  const progressBox = document.getElementById('progressBox');
  const resultBox = document.getElementById('resultBox');
  const preview = document.getElementById('preview');
  const copyAgainBtn = document.getElementById('copyAgainBtn');
  const saveFileBtn = document.getElementById('saveFileBtn');

  let activeTab = null;
  let scrapedText = '';
  let videoTitle = '';

  // Listen for progress updates from content script
  chrome.runtime.onMessage.addListener((message) => {
    if (message.action === 'SCRAPE_PROGRESS' && progressBox) {
      progressBox.style.display = 'block';
      progressBox.textContent = message.message;
    }
  });

  try {
    const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tabs || tabs.length === 0) {
      statusBadge.className = 'status-badge error';
      statusBadge.textContent = '❌ Không tìm thấy tab hoạt động.';
      return;
    }

    activeTab = tabs[0];
    const url = activeTab.url || '';

    const isYouTubeVideo = url.includes('youtube.com/watch') || url.includes('youtube.com/shorts/');

    if (isYouTubeVideo) {
      statusBadge.className = 'status-badge success';
      statusBadge.textContent = '🎬 Đã kết nối trang video YouTube. Sẵn sàng cào.';
      scrapeBtn.disabled = false;
    } else {
      statusBadge.className = 'status-badge error';
      statusBadge.textContent = '⚠️ Mở một trang video YouTube (watch) rồi mở lại extension.';
      scrapeBtn.disabled = true;
    }
  } catch (err) {
    statusBadge.className = 'status-badge error';
    statusBadge.textContent = 'Lỗi kiểm tra tab: ' + err.message;
  }

  // Ensure content script is alive
  async function ensureContentScript(tabId) {
    try {
      const res = await chrome.tabs.sendMessage(tabId, { action: 'PING' });
      if (res && res.status === 'PONG') return true;
    } catch (e) {
      // Content script not loaded yet, inject it manually
      await chrome.scripting.executeScript({
        target: { tabId },
        files: ['content.js']
      });
      await new Promise(r => setTimeout(r, 200));
    }
    return true;
  }

  scrapeBtn.addEventListener('click', async () => {
    if (!activeTab) return;

    scrapeBtn.disabled = true;
    scrapeBtn.textContent = '⏳ Đang cào dữ liệu...';
    resultBox.style.display = 'none';
    progressBox.style.display = 'block';
    progressBox.textContent = 'Đang khởi động cào...';

    try {
      await ensureContentScript(activeTab.id);

      // Step 1: Get full untruncated description from page's JS context (world: MAIN)
      let description = '';
      try {
        const descResult = await chrome.scripting.executeScript({
          target: { tabId: activeTab.id },
          world: 'MAIN',
          func: () => {
            try {
              const currentVid = new URLSearchParams(window.location.search).get('v');

              // 1. Best & always live on SPA navigation: #movie_player.getPlayerResponse()
              const player = document.getElementById('movie_player');
              if (player && typeof player.getPlayerResponse === 'function') {
                const pr = player.getPlayerResponse();
                if (pr?.videoDetails?.shortDescription) {
                  return pr.videoDetails.shortDescription;
                }
              }

              // 2. Polymer live component data on ytd-watch-flexy / ytd-watch-metadata / expander
              const flexy = document.querySelector('ytd-watch-flexy');
              const flexyDesc = flexy?.playerData?.videoDetails?.shortDescription ||
                                flexy?.__data?.playerData?.videoDetails?.shortDescription;
              if (flexyDesc) return flexyDesc;

              const expander = document.querySelector('ytd-text-inline-expander#description-inline-expander');
              const expDesc = expander?.data?.attributedDescription?.content ||
                              expander?.__data?.data?.attributedDescription?.content ||
                              expander?.attributedDescription?.content;
              if (expDesc) return expDesc;

              // 3. ytInitialPlayerResponse (only if videoId matches current URL)
              if (window.ytInitialPlayerResponse?.videoDetails) {
                const vd = window.ytInitialPlayerResponse.videoDetails;
                if (!currentVid || vd.videoId === currentVid) {
                  if (vd.shortDescription) return vd.shortDescription;
                }
              }

              // 4. DOM fallback inside #description-inline-expander (click expand if collapsed)
              if (expander) {
                const expandBtn = expander.querySelector('tp-yt-paper-button#expand, #expand');
                if (expandBtn && !expandBtn.hasAttribute('hidden')) {
                  try { expandBtn.click(); } catch (e) {}
                }
                const expandedEl = expander.querySelector('#expanded yt-attributed-string, #attributed-snippet-text, #snippet-text');
                if (expandedEl) {
                  const text = (expandedEl.innerText || expandedEl.textContent || '').trim();
                  if (text) return text;
                }
              }
            } catch (e) {}
            return '';
          }
        });
        if (descResult && descResult[0] && descResult[0].result) {
          description = descResult[0].result;
        }
      } catch (e) {
        console.warn('Failed to get description via MAIN world:', e);
      }

      // Step 2: Get everything else from content script
      const response = await chrome.tabs.sendMessage(activeTab.id, { action: 'SCRAPE_VIDEO' });

      if (response && response.success) {
        // Inject the clean description into the output if MAIN world got a fuller one
        if (description && description.trim().length > 0) {
          scrapedText = response.text.replace(
            /--- DESCRIPTION ---\n[\s\S]*?(?=\n--- HASHTAGS ---)/,
            '--- DESCRIPTION ---\n' + description.trim() + '\n'
          );
          const descTags = description.match(/#[^\s#]+/g);
          if (descTags && descTags.length > 0) {
            scrapedText = scrapedText.replace(
              /--- HASHTAGS ---\n([^\n]*)/,
              (_, existing) => {
                const current = existing.includes('Không có') ? [] : existing.trim().split(/\s+/).filter(Boolean);
                const merged = Array.from(new Set([...current, ...descTags]));
                return '--- HASHTAGS ---\n' + (merged.length ? merged.join(' ') : '(Không có hashtags)');
              }
            );
          }
        } else {
          scrapedText = response.text;
        }

        // Extract title for filename
        const titleMatch = scrapedText.match(/TITLE:\s*(.+)/);
        videoTitle = titleMatch ? titleMatch[1].trim() : 'youtube-data';

        // Copy to clipboard
        try {
          await navigator.clipboard.writeText(scrapedText);
        } catch (clipErr) {
          console.warn('Clipboard write via navigator failed, trying fallback', clipErr);
        }

        progressBox.style.display = 'none';
        resultBox.style.display = 'block';
        preview.value = scrapedText;

        statusBadge.className = 'status-badge success';
        statusBadge.textContent = `✅ Đã cào & copy (${response.commentsCount} comments)!`;

        scrapeBtn.disabled = false;
        scrapeBtn.textContent = '🔄 Cào lại';
      } else {
        throw new Error(response ? response.error : 'Không nhận được dữ liệu.');
      }
    } catch (err) {
      progressBox.style.display = 'none';
      statusBadge.className = 'status-badge error';
      statusBadge.textContent = 'Lỗi: ' + (err.message || 'Không thể cào dữ liệu');
      scrapeBtn.disabled = false;
      scrapeBtn.textContent = '📋 Cào & Copy';
    }
  });

  copyAgainBtn.addEventListener('click', async () => {
    if (!scrapedText) return;
    try {
      await navigator.clipboard.writeText(scrapedText);
      const originalText = copyAgainBtn.textContent;
      copyAgainBtn.textContent = '✅ Đã copy!';
      setTimeout(() => {
        copyAgainBtn.textContent = originalText;
      }, 1500);
    } catch (err) {
      alert('Không thể copy vào clipboard: ' + err.message);
    }
  });

  saveFileBtn.addEventListener('click', () => {
    if (!scrapedText) return;
    const safeName = videoTitle
      .replace(/[^a-zA-Z0-9\u00C0-\u024F\u1E00-\u1EFF\s-]/g, '')
      .replace(/\s+/g, '-')
      .substring(0, 80) || 'youtube-data';
    const blob = new Blob([scrapedText], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = safeName + '.md';
    a.click();
    URL.revokeObjectURL(url);
    const originalText = saveFileBtn.textContent;
    saveFileBtn.textContent = '✅ Đã lưu!';
    setTimeout(() => {
      saveFileBtn.textContent = originalText;
    }, 1500);
  });
});
