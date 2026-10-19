# Lyra Vance — AI Art & Music Video Workflow

> **Định vị kênh:** Kênh MV **AI Art & Siêu Thực Thơ Mộng (`Cinematic AI Art, Ageless Style & Gentle Surrealism`)** hướng tới khán giả trung niên và cao tuổi. Kết hợp âm nhạc cuốn hút với thế giới thị giác giàu cảm xúc và một chút siêu thực làm tăng vẻ đẹp ở chất lượng `8K Photorealistic Editorial`.

---

## 1. Cấu Trúc Thư Mục

```text
lyra-vance/
├── README.md                          # Tổng quan quy trình làm việc (file này)
├── STYLE_lyra_vance_haute_surreal.md  # Định vị gốc, tinh thần siêu thực & quy tắc an toàn toàn kênh
├── 01-phan-tich-nhac.md               # B1: Tự động phân tích Nhạc + Hình ảnh + Chuyển động từ link YouTube
├── 02-san-xuat-nhac.md                # B2: Tạo gói Suno/Udio & chốt bản nhạc
├── 03-san-xuat-hinh-anh.md            # B3: Trao đổi hình ảnh -> Test prompt -> Xuất hàng loạt image.txt
├── 04-san-xuat-video.md               # B4: Trao đổi animate -> Test motion -> Xuất hàng loạt video.txt
├── common/
│   ├── analyze_motion.py              # Tự tải video YouTube, phát hiện cảnh cắt & xuất lưới ảnh 4 FPS
│   └── analyze_audio.py               # Đo BPM, Key, dải tần DSP & tách file nghe *_listen.mp3
├── youtube-scraper/                   # Chrome Extension quét SEO & Top Comments của đối thủ
└── projects/
    └── XX/                            # Thư mục từng dự án (01, 02, 03...)
        ├── doi-thu/                   # Chứa link/file SEO đối thủ, video tải về & thư mục grids/
        ├── phan-tich.md               # Báo cáo phân tích tổng hợp (Âm thanh + Hình ảnh + Chuyển động)
        ├── docs-nhac.md               # Gói Suno Style + Lyrics đã chốt
        ├── image.txt                  # Danh sách prompt tạo ảnh tĩnh hàng loạt (mỗi dòng 1 cảnh)
        └── video.txt                  # Danh sách prompt chuyển động hàng loạt (mỗi dòng 1 cảnh)
```

---

## 2. Quy Trình Sản Xuất 4 Bước (Áp Dụng Mọi Video)

### Bước 1: Phân Tích Toàn Diện Từ Link YouTube + SEO Đối Thủ ([01-phan-tich-nhac.md](file:///Users/hoangkien/Youtube/lyra-vance/01-phan-tich-nhac.md))
* **User:** Gửi **Link YouTube + Nội dung SEO của đối thủ** (dùng extension `youtube-scraper` bấm `📋 Cào & Copy` rồi dán thẳng vào chat, hoặc bỏ file vào `projects/XX/doi-thu/`).
* **AI tự động thực thi 100%:**
  1. Lưu nội dung SEO & Link vào `projects/XX/doi-thu/seo.md`.
  2. Chạy `python3 common/analyze_motion.py projects/XX/doi-thu` để tự tải video, tách cảnh và xuất lưới ảnh `grids/grid_*.jpg`.
  3. Chạy `python3 common/analyze_audio.py projects/XX/doi-thu` để đo `BPM`, `Key`, năng lượng dải tần và tách file `*_listen.mp3`.
  4. Nghe nhạc + xem toàn bộ lưới ảnh `grids/` + đọc SEO/Top Comments của đối thủ.
  5. Xuất báo cáo 3 mảng (**Phần A: Âm thanh & SEO**, **Phần B: Hình ảnh & Siêu thực**, **Phần C: Chuyển động & Nhịp cắt cảnh**) vào `projects/XX/phan-tich.md`.

### Bước 2: Sản Xuất & Chốt Nhạc ([02-san-xuat-nhac.md](file:///Users/hoangkien/Youtube/lyra-vance/02-san-xuat-nhac.md))
* **AI:** Dựa vào Phần A của `phan-tich.md`, viết **2 phương án** (`Song Title`, `Suno Style Prompt`, `Lyrics`, kèm gợi ý `YouTube Title / SEO` theo công thức đối thủ).
* **User:** Chạy nhạc trên Suno/Udio, chọn bản ưng ý nhất $\rightarrow$ AI lưu bản chốt vào `projects/XX/docs-nhac.md`.

### Bước 3: Thảo Luận Hình Ảnh $\rightarrow$ Test Prompt $\rightarrow$ Sản Xuất Hàng Loạt ([03-san-xuat-hinh-anh.md](file:///Users/hoangkien/Youtube/lyra-vance/03-san-xuat-hinh-anh.md))
1. **Trao đổi:** AI tóm tắt những gì nhận diện được từ Phần B (nhân vật, trang phục, bối cảnh, chất liệu, chi tiết siêu thực của video gốc) và hỏi User có nhận ra thêm chi tiết nào hoặc muốn biến tấu thêm chút siêu thực làm đẹp nào không.
2. **Test Prompt (3–5 câu):** AI viết 3–5 câu prompt tiếng Anh đại diện để User đem đi tạo ảnh thử. Tinh chỉnh đến khi ra ảnh đúng ý.
3. **Mở rộng hàng loạt (`image.txt`):** Khi User duyệt ảnh test và chốt số lượng (50–80 cảnh), AI mới nhân bản theo đúng công thức đã test và xuất ra `projects/XX/image.txt` (không chia phòng cứng nhắc).

### Bước 4: Thảo Luận Animate $\rightarrow$ Test Motion $\rightarrow$ Sản Xuất Hàng Loạt ([04-san-xuat-video.md](file:///Users/hoangkien/Youtube/lyra-vance/04-san-xuat-video.md))
1. **Trao đổi:** AI đối chiếu Phần C (chuyển động của video gốc) với bộ ảnh vừa chốt để thống nhất kiểu chuyển động (nhảy múa, đi dạo, đọc sách, ngắm cảnh, tương tác cặp đôi...) và góc máy.
2. **Test Motion (3–5 câu):** AI viết 3–5 câu prompt chuyển động khớp với bộ ảnh test để User chạy thử video trước.
3. **Mở rộng hàng loạt (`video.txt`):** Khi User xác nhận chuyển động mượt và không lỗi, AI xuất toàn bộ danh sách ra `projects/XX/video.txt`.

---

## 3. Lệnh Nhanh Cho User Khi Làm Việc Với AI

* **Bắt đầu dự án mới:** `"Làm Bước 1 cho project 01"` + Dán (`Cmd+V`) nội dung vừa copy từ `youtube-scraper` (chứa sẵn Link YouTube + SEO + Comments).
* **Sang Bước 2:** `"Làm nhạc Bước 2 cho project 01"`
* **Sang Bước 3:** `"Sang Bước 3 làm ảnh cho project 01"` $\rightarrow$ *(Test 3–5 câu)* $\rightarrow$ `"Ảnh test ổn rồi, xuất 60 câu vào image.txt"`
* **Sang Bước 4:** `"Sang Bước 4 làm animate cho project 01"` $\rightarrow$ *(Test 3–5 câu)* $\rightarrow$ `"Video test ổn rồi, xuất toàn bộ vào video.txt"`
