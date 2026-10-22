# Lyra Vance — AI Art & Music Video Workflow

> **Nguyên tắc vận hành:** Tách riêng **Bước 0 (Xử lý vật lý thuần bằng code)** khỏi 4 bước AI làm việc (`01` Phân tích nhạc $\rightarrow$ `02` Sản xuất nhạc $\rightarrow$ `03` Phân tích hình ảnh & Tạo File Style Hình ảnh $\rightarrow$ `04` Phân tích Animation & Tạo File Style Chuyển động).

---

## 1. Cấu Trúc Thư Mục & Công Cụ

```text
lyra-vance/
├── README.md                              # Tổng quan hệ thống (file này)
├── 00-xu-ly-vat-ly.md                     # B0 (Code thuần): Tải video, tách nhạc, tách ảnh grid 4 FPS & đo DSP bằng code
├── 01-phan-tich-nhac.md                   # B1: AI nghe lại âm thanh + đọc SEO/Comment + đọc DSP -> phan-tich-nhac.md
├── 02-san-xuat-nhac.md                    # B2: Sản xuất & Remake nhạc trên Suno/Udio -> docs-nhac.md
├── 03-phan-tich-hinh-anh.md               # B3: Phân tích quy luật Hình ảnh -> Test Prompt & Feedback -> Style Bible (phan-tich-hinh-anh.md) & image.txt
├── 04-phan-tich-animation.md              # B4: Phân tích quy luật Animation -> Test Motion & Feedback -> Motion Style Bible (phan-tich-animation.md) & video.txt
├── common/                                # BỘ TOOL CHẠY BƯỚC 0
│   ├── ingest_doithu.py                   # Lệnh tổng Bước 0: Từ link YouTube -> tải video, SEO/Comments, tách nhạc, đo DSP & cắt lưới 4 FPS
│   ├── analyze_audio.py                   # Tách listen.mp3 & phân tích âm thanh bằng code (audio_dsp.json)
│   └── analyze_motion.py                  # Phát hiện cảnh cắt & xuất lưới ảnh 4 FPS (grids/) + shot_sheets/
├── doithu/                                # Thư viện 46 video đối thủ đã chạy sẵn Bước 0
│   └── INDEX.md                           # Bảng mục lục tra cứu 46 video đối thủ
└── projects/
    └── XX/                                # Thư mục từng dự án (01, 02, 03...)
        ├── doi-thu/                       # Đầu ra Bước 0 (video.mp4, listen.mp3, seo.md, audio_dsp.json, grids/, shot_sheets/)
        ├── phan-tich-nhac.md              # Đầu ra Bước 1 (Báo cáo phân tích Nhạc & SEO 3 Tầng)
        ├── docs-nhac.md                   # Đầu ra Bước 2 (Gói Suno Style + Lyrics đã chốt)
        ├── phan-tich-hinh-anh.md          # Đầu ra Bước 3 (Hệ Quy luật Hình ảnh & Living Style Bible)
        ├── phan-tich-animation.md         # Đầu ra Bước 4 (Hệ Quy luật Animation & Living Motion Style Bible)
        ├── image.txt                      # Danh sách prompt ảnh tĩnh sinh từ phan-tich-hinh-anh.md
        └── video.txt                      # Danh sách prompt chuyển động sinh từ phan-tich-animation.md
```
