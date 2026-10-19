// YouTube Video Scraper Content Script

function getCleanText(el) {
  return el ? el.innerText.trim() : '';
}

async function scrapeMetadata() {
  // Title
  let title = '';
  const titleEl = document.querySelector('h1.ytd-watch-metadata yt-formatted-string') ||
                  document.querySelector('h1.ytd-watch-metadata') ||
                  document.querySelector('#title h1 yt-formatted-string');
  if (titleEl) {
    title = titleEl.innerText.trim();
  }
  if (!title) {
    title = document.querySelector('meta[name="title"]')?.content ||
            document.title.replace(/ - YouTube$/, '').trim();
  }

  // Channel Name & Subs
  let channel = '';
  const channelEl = document.querySelector('#owner ytd-channel-name #text a') ||
                    document.querySelector('#owner #channel-name a') ||
                    document.querySelector('ytd-watch-metadata #channel-name a');
  if (channelEl) {
    channel = channelEl.innerText.trim();
  }
  if (!channel) {
    channel = document.querySelector('link[itemprop="name"]')?.getAttribute('content') || '';
  }

  let subs = '';
  const subEl = document.querySelector('#owner-sub-count') ||
                document.querySelector('yt-formatted-string#owner-sub-count');
  if (subEl) {
    subs = subEl.innerText.trim();
  }

  // Views & Date
  let views = '';
  let date = '';
  const infoSpans = document.querySelectorAll('#info-container #info span, ytd-watch-info-text #info span');
  if (infoSpans.length >= 1) {
    views = infoSpans[0].innerText.trim();
  }
  if (infoSpans.length >= 3) {
    date = infoSpans[2].innerText.trim();
  } else if (infoSpans.length === 2) {
    date = infoSpans[1].innerText.trim();
  }

  if (!views) {
    const metaViews = document.querySelector('meta[itemprop="interactionCount"]')?.getAttribute('content');
    if (metaViews) {
      views = Number(metaViews).toLocaleString() + ' views';
    }
  }

  if (!date) {
    const metaDate = document.querySelector('meta[itemprop="datePublished"]')?.getAttribute('content') ||
                     document.querySelector('meta[itemprop="uploadDate"]')?.getAttribute('content');
    if (metaDate) {
      date = metaDate;
    }
  }

  // Likes
  let likes = '';
  const likeBtn = document.querySelector('like-button-view-model button') ||
                  document.querySelector('segmented-like-dislike-button-view-model button') ||
                  document.querySelector('#top-level-buttons-computed segmented-like-dislike-button-view-model button');
  if (likeBtn) {
    const spanText = likeBtn.innerText.trim();
    const aria = likeBtn.getAttribute('aria-label') || '';
    if (spanText && spanText !== '' && !spanText.toLowerCase().includes('like')) {
      likes = spanText;
    } else if (aria) {
      const match = aria.match(/[\d,.]+/);
      if (match) likes = match[0];
    }
  }
  if (!likes) likes = '0';

  // Description — expand inline expander if collapsed, then read from DOM
  let description = '';
  const expander = document.querySelector('ytd-watch-metadata ytd-text-inline-expander#description-inline-expander') ||
                   document.querySelector('#description-inline-expander');
  if (expander) {
    const expandBtn = expander.querySelector('tp-yt-paper-button#expand, #expand');
    if (expandBtn && !expandBtn.hasAttribute('hidden') && expandBtn.offsetParent !== null) {
      try {
        expandBtn.click();
        await new Promise(r => setTimeout(r, 250));
      } catch (e) {}
    }

    const descSelectors = [
      '#expanded yt-attributed-string',
      '#expanded yt-formatted-string',
      '#expanded',
      '#attributed-snippet-text',
      '#snippet-text'
    ];
    for (const sel of descSelectors) {
      const el = expander.querySelector(sel);
      if (el) {
        const txt = (el.innerText || el.textContent || '').trim();
        if (txt) {
          description = txt;
          break;
        }
      }
    }
  }

  if (!description) {
    const fallbackEl = document.querySelector('#bottom-row #description-inner ytd-text-inline-expander') ||
                       document.querySelector('meta[name="description"]');
    if (fallbackEl) {
      description = (fallbackEl.content || fallbackEl.innerText || '').replace(/\.\.\.more\s*$/i, '').replace(/Show less\s*$/i, '').trim();
    }
  }

  // Hashtags
  const hashtagSet = new Set();
  const hashtagLinks = document.querySelectorAll('ytd-watch-metadata a[href*="/hashtag/"], a[href*="/hashtag/"]');
  hashtagLinks.forEach(a => {
    const tag = (a.innerText || a.textContent || '').trim();
    if (tag.startsWith('#')) hashtagSet.add(tag);
  });
  const matches = description.match(/#[^\s#]+/g);
  if (matches) {
    matches.forEach(tag => hashtagSet.add(tag));
  }

  const hashtags = Array.from(hashtagSet);

  return {
    title,
    channel,
    subs,
    views,
    likes,
    date,
    description,
    hashtags
  };
}

async function scrapeComments(onProgress, maxComments = 30) {
  onProgress('Đang tìm vùng bình luận...');
  const commentsElem = document.querySelector('ytd-comments#comments, #comments');
  if (!commentsElem) {
    return { status: 'disabled', comments: [] };
  }

  // Scroll down towards comments to trigger YouTube lazy load
  commentsElem.scrollIntoView({ behavior: 'smooth', block: 'center' });
  await new Promise(r => setTimeout(r, 1200));

  // Check if disabled
  const disabledElem = commentsElem.querySelector('#message');
  if (disabledElem && disabledElem.offsetParent !== null) {
    const text = disabledElem.innerText.trim();
    if (text.toLowerCase().includes('turned off') || text.toLowerCase().includes('tắt')) {
      return { status: 'disabled', message: text, comments: [] };
    }
  }

  let lastCount = 0;
  let stagnantRounds = 0;
  const maxRounds = 20;

  for (let round = 0; round < maxRounds; round++) {
    const threads = document.querySelectorAll('ytd-comment-thread-renderer');
    const currentCount = threads.length;
    onProgress(`Đang tải comments... (${Math.min(currentCount, maxComments)}/${maxComments})`);

    if (currentCount >= maxComments) {
      break;
    }

    if (currentCount === lastCount) {
      stagnantRounds++;
      if (stagnantRounds >= 4) {
        break;
      }
    } else {
      stagnantRounds = 0;
      lastCount = currentCount;
    }

    // Scroll further down to trigger lazy loading of comments
    window.scrollBy({ top: 1200, behavior: 'smooth' });
    await new Promise(r => setTimeout(r, 900));
  }

  // Scroll back to top
  window.scrollTo({ top: 0, behavior: 'smooth' });

  const threads = Array.from(document.querySelectorAll('ytd-comment-thread-renderer')).slice(0, maxComments);
  const parsedComments = [];

  for (const thread of threads) {
    // Check pinned badge
    const pinnedBadge = thread.querySelector('ytd-pinned-comment-badge-renderer, #pinned-comment-badge');
    const isPinned = pinnedBadge && pinnedBadge.offsetParent !== null;

    // Expand comment if it has "Read more"
    const moreBtn = thread.querySelector('#more-button, #expander #more');
    if (moreBtn && moreBtn.offsetParent !== null && !moreBtn.hidden) {
      try {
        moreBtn.click();
      } catch (e) {}
    }

    // Author
    const authorEl = thread.querySelector('#author-text');
    const author = authorEl ? authorEl.innerText.trim() : 'Anonymous';

    // Comment text
    const contentEl = thread.querySelector('#content-text');
    const text = contentEl ? contentEl.innerText.trim() : '';

    // Likes
    const voteEl = thread.querySelector('#vote-count-middle');
    let voteCount = voteEl ? voteEl.innerText.trim() : '0';
    if (!voteCount) voteCount = '0';

    parsedComments.push({
      author,
      text,
      likes: voteCount,
      isPinned
    });
  }

  return { status: 'ok', comments: parsedComments };
}

function formatOutput(meta, commentResult) {
  const lines = [];
  lines.push('=== YOUTUBE VIDEO DATA ===\n');
  lines.push(`TITLE: ${meta.title || 'N/A'}`);
  lines.push(`CHANNEL: ${meta.channel || 'N/A'}${meta.subs ? ` (${meta.subs})` : ''}`);
  lines.push(`VIEWS: ${meta.views || 'N/A'}`);
  lines.push(`LIKES: ${meta.likes || 'N/A'}`);
  lines.push(`UPLOADED: ${meta.date || 'N/A'}`);
  lines.push('\n--- DESCRIPTION ---');
  lines.push(meta.description || '(Không có mô tả)');
  lines.push('\n--- HASHTAGS ---');
  if (meta.hashtags && meta.hashtags.length > 0) {
    lines.push(meta.hashtags.join(' '));
  } else {
    lines.push('(Không có hashtags)');
  }
  lines.push(`\n--- TOP COMMENTS (${commentResult.comments.length}) ---`);
  if (commentResult.status === 'disabled') {
    lines.push('[Comments disabled / Tính năng bình luận bị tắt]');
  } else if (commentResult.comments.length === 0) {
    lines.push('(Không có bình luận nào)');
  } else {
    commentResult.comments.forEach((c, idx) => {
      const pinPrefix = c.isPinned ? '[PINNED] ' : '';
      lines.push(`${idx + 1}. ${pinPrefix}${c.author} (❤️ ${c.likes}) — ${c.text}`);
    });
  }

  return lines.join('\n');
}

// Runtime message listener
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'PING') {
    sendResponse({ status: 'PONG' });
    return false;
  }

  if (request.action === 'SCRAPE_VIDEO') {
    (async () => {
      try {
        const meta = await scrapeMetadata();
        const comments = await scrapeComments((msg) => {
          chrome.runtime.sendMessage({ action: 'SCRAPE_PROGRESS', message: msg }).catch(() => {});
        }, 30);
        const text = formatOutput(meta, comments);
        sendResponse({
          success: true,
          text,
          commentsCount: comments.comments.length,
          title: meta.title
        });
      } catch (err) {
        sendResponse({
          success: false,
          error: err.message || 'Lỗi khi cào dữ liệu'
        });
      }
    })();
    return true; // Keep asynchronous channel open
  }
});
