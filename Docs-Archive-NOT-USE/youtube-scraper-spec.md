# YouTube Competitor Scraper — Spec & Plan

## Mục đích

Extension Chrome cào data từ **1 video YouTube** đang xem. Output là 1 block text sạch, copy 1 click, paste thẳng vào AI phân tích.

## Phạm vi

- **Chỉ hoạt động trên trang xem video** (`youtube.com/watch?v=...`)
- Không hoạt động ở trang chủ, search, channel, playlist
- 1 video = 1 lần cào = 1 output

---

## Data cần cào

### 1. Video Metadata (SEO)

| Field | Nguồn trên trang | Bắt buộc |
|-------|-------------------|----------|
| Title | `<title>` hoặc `h1.ytd-watch-metadata` | ✅ |
| View count | `ytd-video-view-count-renderer` | ✅ |
| Like count | Like button `segmented-like-dislike-button-view-model` | ✅ |
| Upload date | `ytd-video-primary-info-renderer .date` | ✅ |
| Description (full) | `ytd-text-inline-expander` (phải expand trước) | ✅ |
| Hashtags | Các link `a[href*="/hashtag/"]` trong description | ✅ |
| Channel name | `ytd-channel-name` | ✅ |
| Subscriber count | `#owner-sub-count` | ✅ |

### 2. Comments

| Field | Chi tiết |
|-------|----------|
| Số lượng | Top **30 comments** (sorted by Top, mặc định YouTube) |
| Mỗi comment | Username + nội dung + số likes |
| Pinned comment | Nếu có, đánh dấu [PINNED] |
| Reply | Không cào reply, chỉ comment gốc |

**Lưu ý:** Comments load lazy (scroll để load thêm). Extension cần auto-scroll đủ để load ít nhất 30 comments trước khi cào.

---

## Output Format

```
=== YOUTUBE VIDEO DATA ===

TITLE: [title]
CHANNEL: [channel name] ([subscriber count])
VIEWS: [view count]
LIKES: [like count]  
UPLOADED: [date]

--- DESCRIPTION ---
[full description text]

--- HASHTAGS ---
[#tag1] [#tag2] [#tag3] ...

--- TOP COMMENTS (30) ---
1. [username] (❤️ [likes]) — [comment text]
2. [username] (❤️ [likes]) — [comment text]
...
[PINNED] [username] (❤️ [likes]) — [comment text]
```

Plain text, không markdown, không HTML — để paste thẳng vào bất kỳ AI nào.

---

## UI

### Popup (click icon extension)

- **Trạng thái:** "Đang ở trang video" hoặc "Không phải trang video"
- **Nút duy nhất:** `📋 Cào & Copy` 
- **Progress:** "Đang scroll load comments... (15/30)"
- **Khi xong:** "✅ Đã copy! Paste vào AI."
- Không có settings. Không có options page. 1 nút.

### Khi không ở trang video

- Popup hiện: "Mở một video YouTube rồi bấm lại"
- Nút bị disable

---

## Luồng hoạt động

```
User mở video YouTube
       ↓
Click icon extension
       ↓
Popup hiện → User click "Cào & Copy"
       ↓
Content script chạy:
  1. Đọc metadata (title, views, likes, date, description, hashtags, channel)
  2. Scroll xuống vùng comments
  3. Auto-scroll để load 30 comments (mỗi lần scroll chờ 1-2s cho lazy load)
  4. Đọc 30 comments (username + text + likes + pinned status)
  5. Format thành plain text
  6. Copy vào clipboard
       ↓
Popup hiện "✅ Đã copy!"
       ↓
User paste vào Gemini / Meta AI / bất kỳ đâu
```

---

## Kỹ thuật

| Thành phần | Công nghệ |
|-----------|-----------|
| Manifest | Manifest V3 |
| Content script | Chạy trên `*://www.youtube.com/watch*` |
| Popup | HTML + JS đơn giản |
| Clipboard | `navigator.clipboard.writeText()` |
| Scroll comments | `window.scrollTo()` + `MutationObserver` chờ DOM load |
| Permissions | `activeTab`, `clipboardWrite` |

### Cấu trúc file

```
youtube-scraper/
├── manifest.json
├── popup.html
├── popup.js
├── content.js
└── icons/
    ├── icon16.png
    ├── icon48.png
    └── icon128.png
```

**5 files chính, không thư viện ngoài, không framework.**

---

## Edge Cases

| Case | Xử lý |
|------|--------|
| Video tắt comments | Cào metadata, ghi "Comments disabled" |
| Comments < 30 | Cào bao nhiêu có bấy nhiêu |
| Description rất dài | Lấy full, không cắt |
| Video live/premiere | Cào như video thường, comments có thể khác format |
| Không có hashtag | Ghi "Không có hashtags" |
| YouTube đổi DOM | Selectors cần cập nhật — ghi chú selectors ở 1 chỗ dễ sửa |

---

## Plan (thứ tự build)

### Phase 1 — Metadata only (30 phút)
1. Tạo manifest.json + popup cơ bản
2. Content script đọc title, channel, views, likes, date, description, hashtags
3. Format + copy clipboard
4. Test trên 3 video khác nhau

### Phase 2 — Comments (1-2 giờ)
5. Auto-scroll vùng comments
6. Chờ lazy load bằng MutationObserver
7. Đọc top 30 comments (username, text, likes, pinned)
8. Gộp vào output format
9. Test trên video có nhiều comments / ít comments / tắt comments

### Phase 3 — Polish (30 phút)
10. Loading state trong popup
11. Error handling (không phải trang video, timeout scroll)
12. Icon đẹp hơn
13. Test cuối

**Tổng: ~3-4 giờ cho MVP hoạt động.**

---

## Không làm (YAGNI)

- ❌ Không cào replies
- ❌ Không cào video liên quan
- ❌ Không lưu history
- ❌ Không export file
- ❌ Không phân tích sentiment
- ❌ Không settings/options
- ❌ Không hoạt động trên nhiều video cùng lúc
- ❌ Không dùng YouTube API (đọc DOM thẳng, không cần API key)
