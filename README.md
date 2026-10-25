# Lyra Vance — Minimalist Production System

> **Nguyên tắc vận hành:** Hệ thống sản xuất tinh gọn qua 4 bước tại `craft/` (`01` Định vị $\rightarrow$ `02` Idea $\rightarrow$ `03` Nhạc $\rightarrow$ `04` Visual) kết hợp thư viện phong cách tại `style/`.

---

## 1. Cấu Trúc Thư Mục Tối Giản

```text
lyra-vance/
├── README.md                              # Tổng quan hệ thống & luồng chạy dự án
├── craft/                                 # BỘ QUY TẮC VẬN HÀNH LÕI (4 BƯỚC)
│   ├── 01-dinh-vi-kenh.md                 # B1: Định vị kênh, Bản chất thế giới & Ngụ ngôn chủ thể kỳ lạ
│   ├── 02-idea.md                         # B2: Quy tắc xây dựng Idea (Ma trận: Sự kiện bất kỳ x Nỗi niềm nhỏ bé)
│   ├── 03-san-xuat-nhac.md                # B3: Kỹ thuật âm học 2 lớp, Âm thanh định danh độc bản & Cú pháp Suno 4 mệnh đề
│   └── 04-visual.md                       # B4: Quy tắc thiết kế thị giác & chuyển động (Planimetric Stop-Motion 2.5D)
├── style/                                 # THƯ VIỆN PHONG CÁCH THỊ GIÁC
│   └── STYLE-BIBLE.md                     # Cẩm nang chi tiết, Từ điển lắp ghép 5 mảnh & 12 mẫu nhân vật/sinh vật chuẩn
├── common/                                # Công cụ hỗ trợ phân tích vật lý (Audio DSP / Motion Grids)
├── doithu/                                # Thư viện dữ liệu & phân tích đối thủ tham khảo
└── projects/                              # THƯ MỤC SẢN XUẤT TỪNG VIDEO
    └── <STT>/                             # Ví dụ: 01, 02, 03...
        ├── idea.md                        # Đầu ra B2: Tổ hợp (Sự kiện x Nỗi niềm) & Đường cong tự sự 3 hồi
        ├── nhac.md                        # Đầu ra B3: Thiết kế âm học, Style Prompt (4 mệnh đề), Exclude & Lyrics
        ├── visual.md                      # Đầu ra B4: Dàn nhân vật, Sân khấu 2.5D & Bảng phân cảnh khớp nhạc
        ├── image.txt                      # Tệp câu lệnh sinh ảnh hàng loạt (1 dòng = 1 prompt hoàn chỉnh)
        └── video.txt                      # Tệp câu lệnh chuyển động I2V tương ứng 1:1 với image.txt
```

---

## 2. Quy Trình Sản Xuất 1 Video (`projects/<STT>/`)

1. **Bước 1 — Khởi tạo Idea (`idea.md`):**
   Đọc [craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md) và [craft/02-idea.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/02-idea.md) $\rightarrow$ Chốt tổ hợp `1 Sự kiện bất kỳ x 1 Nỗi niềm nhỏ bé` và xuất `projects/<STT>/idea.md`.
2. **Bước 2 — Sản xuất Nhạc (`nhac.md`):**
   Đọc [craft/03-san-xuat-nhac.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/03-san-xuat-nhac.md) và `projects/<STT>/idea.md` $\rightarrow$ AI tự chọn thể loại khớp cảm xúc, áp dụng kỹ thuật nhạc 2 lớp + âm thanh độc bản và xuất `projects/<STT>/nhac.md`.
3. **Bước 3 — Thiết kế Visual & Xuất Prompt (`visual.md`, `image.txt`, `video.txt`):**
   Đọc [craft/04-visual.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/04-visual.md) và [style/STYLE-BIBLE.md](file:///Users/hoangkien/Youtube/lyra-vance/style/STYLE-BIBLE.md) $\rightarrow$ Chốt dàn nhân vật, bối cảnh sân khấu 2.5D trong `projects/<STT>/visual.md`, sau đó xuất thẳng `projects/<STT>/image.txt` và `projects/<STT>/video.txt`.
