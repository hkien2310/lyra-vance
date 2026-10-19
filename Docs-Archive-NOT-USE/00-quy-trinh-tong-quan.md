# QUY TRÌNH LÀM KÊNH MỚI

> **Nguyên tắc:** Toàn bộ phân tích AI chỉ là tham khảo, không phải chân lý. Sản phẩm cuối cùng luôn phải qua tai người. Sản xuất lấy cảm hứng từ đối thủ, không copy 1:1.

---

## 📌 CHECKLIST BẮT BUỘC: LƯU GÌ & COPY GÌ QUA MỖI BƯỚC

| # | Bước | Thao tác cần làm | File / Dữ liệu bắt buộc lưu | Copy sang đâu? |
|---|------|------------------|-----------------------------|----------------|
| **1** | **Cào data** | Bấm extension YouTube Scraper | Bấm **"💾 Lưu file"** $\rightarrow$ lưu file `.md` về máy | Copy nội dung vào chat Gemini bước 2 |
| **2** | **Phân tích nhạc** | Gemini phân tích xong | Lưu bản phân tích | **Bắt buộc copy `Theme Brief`** sang Meta AI bước 3 |
| **3** | **Phân tích ảnh** | Meta AI phân tích xong | Giữ nguyên trong chat | Dùng luôn cho bước 5 (cùng khung chat) |
| **4** | **Sản xuất nhạc** | Gemini nhả prompt Suno | Copy `Style Prompt` + `Lyrics` vào Suno | **Tải file nhạc `.mp3` hoàn chỉnh** từ Suno về máy |
| **5** | **Sản xuất ảnh** | Meta AI vẽ ảnh (đợt 1, 2...) | 1. Tải các ảnh về máy<br>2. Lưu toàn bộ prompt vào file `image_prompts.txt` | Ném file `image_prompts.txt` sang bước 6 |
| **6** | **Tạo video** | AI xuất prompt video $\rightarrow$ Veo3 tạo clip | 1. Lưu file `video_prompts.txt`<br>2. Tải các clip video 8s về máy | Đưa video + file nhạc MP3 vào khâu Edit |
| **7** | **Dựng video** | Ráp clip vào nhạc theo beat | **Xuất file video MV hoàn chỉnh** | Sẵn sàng đăng YouTube |

---

## PHÂN TÍCH (hiểu đối thủ)

| # | Bước | Hành động | Tool | Tài liệu |
|---|------|-----------|------|----------|
| 1 | Cào data đối thủ | Mở video → bấm extension → lưu file `.md` | Extension `YouTube Scraper` | `youtube-scraper/` |
| 2 | Phân tích nhạc | Paste prompt → AI hỏi dữ liệu → phân tích | Gemini Web | `01-phan-tich-nhac.md` |
| 3 | Phân tích hình ảnh | Dán Theme Brief + ảnh ref → phân tích | Meta AI | `02-phan-tich-hinh-anh.md` |

---

## SẢN XUẤT (tạo mới, lấy cảm hứng từ phân tích)

```
3 tư liệu phân tích (tham khảo)
       ↓
  Nhạc (Suno) ───┐  (chạy song song)
  Ảnh (Meta AI) ─┤
       ↓         ↓
       Video 8s (Veo3 / Kling)
       ↓
       Edit ráp nhạc (CapCut / Premiere)
```

| # | Bước | Hành động | Tool | Tài liệu |
|---|------|-----------|------|----------|
| 4 | Tạo nhạc | Tiếp tục chat Gemini → sinh gói Suno | Suno | `03-san-xuat-nhac.md` |
| 5 | Tạo ảnh | Tiếp tục chat Meta AI → vẽ 5 ảnh + prompt | Meta AI / Midjourney | `04-san-xuat-hinh-anh.md` |
| 6 | Tạo video | Nhập ảnh + prompt chuyển động | Veo3 / Kling | `05-san-xuat-video.md` |
| 7 | Edit | Ráp 5 clip vào file MP3 theo beat | CapCut / Premiere | MV 4K hoàn chỉnh |

---

## Danh mục tài liệu

| File | Mô tả | Trạng thái |
|------|--------|------------|
| `youtube-scraper/` | Chrome extension cào SEO + comments (có nút xuất file `.md`) | ✅ |
| `01-phan-tich-nhac.md` | Phân tích nhạc (interactive, hỏi cảm nhận tự nhiên) | ✅ |
| `02-phan-tich-hinh-anh.md` | Phân tích hình ảnh (interactive, bóc tách chất siêu thực & người có hồn) | ✅ |
| `03-san-xuat-nhac.md` | Sản xuất nhạc (Suno Style Prompt 60-90 từ + Lyrics ~4 phút có hook) | ✅ |
| `04-san-xuat-hinh-anh.md` | Sản xuất ảnh (vẽ trực tiếp 5 ảnh chuẩn Toàn/Trung/Cận + xuất code prompt) | ✅ |
| `05-san-xuat-video.md` | Sản xuất video (công thức One-Take Veo3 + thư viện máy quay & vũ đạo) | ✅ |
