# 00 - Bước Xử Lý Vật Lý Bằng Code (Không Cần AI)

Tài liệu quy định **Bước 0**: Toàn bộ khâu tải dữ liệu và đo đạc vật lý từ Link YouTube được thực hiện thuần bằng code Python (`common/`), không cần AI suy luận. Đầu ra của Bước 0 là gói dữ liệu thô hoàn chỉnh để cung cấp cho Bước 1 (Phân tích nhạc), Bước 3 (Làm `image.txt`) và Bước 4 (Làm `video.txt`).

---

## 1. Lệnh Thực Thi Duy Nhất Từ Link YouTube

### Chạy cho dự án cụ thể (`projects/XX/doi-thu/`):
```bash
python3 common/ingest_doithu.py "<youtube_url>" --out projects/XX/doi-thu
```

### Hoặc nạp vào kho đối thủ chung (`doithu/<ten-kenh>/<ten-video>/raw/`):
```bash
python3 common/ingest_doithu.py "<youtube_url>"
```

*(Nếu đã có sẵn video hoặc file âm thanh trong `projects/XX/doi-thu/`, có thể chạy lẻ từng tool: `python3 common/analyze_motion.py projects/XX/doi-thu` và `python3 common/analyze_audio.py projects/XX/doi-thu`).*

---

## 2. Các Tác Vụ Vật Lý Code Tự Động Chạy 100%

Khi chạy lệnh trên, hệ thống tự động thực hiện 4 việc:

1. **Tải Video, Thumbnail & Cào SEO + Comments (`yt-dlp`):**
   - Tải video gốc: `video.mp4` (`<=720p`).
   - Tải ảnh bìa gốc độ phân giải cao nhất: `thumbnail.jpg`.
   - Cào toàn bộ Metadata & Bình luận: `seo.md` và `seo_metadata.json` (gồm `TITLE`, `CHANNEL`, `SUBSCRIBERS`, `VIEWS`, `LIKES`, `HIDDEN TAGS`, `CHAPTERS`, `DESCRIPTION`, `HASHTAGS`, và `TOP 30–50 COMMENTS` nhiều tim nhất).
2. **Tách Âm Thanh & Phân Tích Âm Thanh Bằng Code ([`common/analyze_audio.py`](file:///Users/hoangkien/Youtube/lyra-vance/common/analyze_audio.py)):**
   - Tách file âm thanh nhẹ chuẩn `128kbps MP3`: `listen.mp3` (để Bước 1 nghe lại).
   - Đo thông số tín hiệu âm học DSP bằng `librosa` và lưu vào `audio_dsp.json`:
     - `BPM` & `Half-time BPM`, `Beat Stability`.
     - `Key & Scale` (Krumhansl-Schmuckler chroma profile).
     - `Crest Factor (dB)` & đặc tính nén bản mix (`Compression Character`).
     - Tỷ lệ phân bổ năng lượng `6 dải tần số (%)` (`Sub-bass`, `Bass`, `Low-mid`, `Mid`, `High-mid`, `High`).
     - Các mốc phân đoạn năng lượng (`Energy Sections`) tổng thể và tách riêng từng bài hát (`tracks`) theo Chapters.
3. **Phát Hiện Cảnh Cắt & Tách Lưới Ảnh Bằng Code ([`common/analyze_motion.py`](file:///Users/hoangkien/Youtube/lyra-vance/common/analyze_motion.py)):**
   - Phát hiện toàn bộ điểm chuyển cảnh (`shots`) và lưu thống kê vào `motion_metadata.json` (`total_shots`, `avg_shot_duration_sec`, timestamp từng cảnh).
   - Cắt bộ **lưới ảnh liên hoàn `4 FPS`** (`grids/grid_*.jpg` — mỗi ô cách nhau `0.25s`, lưới 6x10 phủ 100% video) phục vụ Bước 3 (`image.txt`) và Bước 4 (`video.txt`).
   - Cắt bộ **ảnh tĩnh từng cảnh 4K** (`shot_sheets/shots_*.jpg` — lưới 3x3 HD `1280x720`/ô chụp giữa mỗi shot).

---

## 3. Cây Thư Mục Đầu Ra Sau Bước 0

```text
projects/XX/doi-thu/ (hoặc doithu/<kenh>/<video>/raw/)
├── video.mp4                # Video gốc tải về
├── listen.mp3               # File nhạc nhẹ để Bước 1 nghe
├── thumbnail.jpg            # Ảnh bìa gốc
├── seo.md                   # Title, Description, Hidden Tags, Chapters, Top Comments
├── seo_metadata.json        # JSON metadata gốc
├── audio_dsp.json           # Kết quả phân tích âm thanh bằng code (BPM, Key, 6 dải tần, Sections)
├── motion_metadata.json     # Thống kê số cảnh cắt & thời lượng từng shot
├── grids/                   # Bộ lưới ảnh 4 FPS (0.25s/ô) dùng cho Bước 3 & Bước 4
│   └── grid_01_...jpg
└── shot_sheets/             # Bộ lưới ảnh 3x3 HD chụp từng shot
    └── shots_01_...jpg
```
