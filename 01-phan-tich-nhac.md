# 01 - Quy Tắc Phân Tích Toàn Diện Từ Link YouTube (Âm Thanh + Hình Ảnh + Chuyển Động)

Tài liệu quy định Bước 1: Người dùng chỉ cần **ném link YouTube** (hoặc bỏ file vào `projects/XX/doi-thu/`), AI tự động tải video, đo thông số âm thanh, cắt lưới hình ảnh và phân tích trọn gói cả **Nhạc – Hình ảnh – Chuyển động** vào `projects/XX/phan-tich.md`.

---

## 1. Đầu Vào & Thực Thi Tự Động

### Đầu vào từ Người dùng
- Người dùng gửi **Link YouTube + Nội dung SEO của đối thủ** (copy 1-click từ extension `youtube-scraper` rồi dán thẳng vào chat, hoặc lưu file vào `projects/XX/doi-thu/`).

### Các bước AI tự động chạy 100%
1. **Lưu dữ liệu SEO & Tải video + Cắt lưới hình ảnh (`4 FPS`):**
   - Nếu người dùng dán nội dung SEO + Link YouTube trực tiếp vào chat, AI tự động tạo thư mục `projects/XX/doi-thu/` và lưu vào `projects/XX/doi-thu/seo.md`.
   - Chạy lệnh:
     ```bash
     python3 common/analyze_motion.py projects/XX/doi-thu
     ```
   - Script tự động đọc link YouTube từ `seo.md`, tải `competitor_video.mp4`, phát hiện toàn bộ điểm cắt cảnh (`shots`) và xuất bộ lưới ảnh `projects/XX/doi-thu/grids/grid_*.jpg` bao phủ 100% video.
2. **Đo thông số kỹ thuật Âm thanh (DSP):**
   - Chạy tiếp lệnh:
     ```bash
     python3 common/analyze_audio.py projects/XX/doi-thu
     ```
   - Lấy chính xác: `BPM`, `Key & Scale`, `Crest Factor`, `Tỷ lệ 6 dải tần số`, `Energy Sections` và file `*_listen.mp3`.
3. **Nghe Nhạc + Xem Lưới Ảnh (`grids/`) + Đọc SEO:**
   - Dùng `view_file` nghe trực tiếp file `*_listen.mp3`, xem các tấm lưới ảnh trong `projects/XX/doi-thu/grids/` và đọc dữ liệu SEO/Top Comments trong `projects/XX/doi-thu/seo.md`.
4. **Xuất Báo Cáo Tổng Hợp (`projects/XX/phan-tich.md`):**
   - Lưu toàn bộ kết quả phân tích 3 phần (Âm thanh & SEO, Hình ảnh, Chuyển động) vào `projects/XX/phan-tich.md`.

---

## 2. Cấu Trúc Báo Cáo `projects/XX/phan-tich.md`

### Phần A: Phân Tích Âm Thanh & SEO (Phục vụ Bước 2 làm nhạc)
- **Thể loại chính, Nhánh phụ & Thời kỳ tham chiếu:** Xác định dòng nhạc cốt lõi và cảm hứng thập niên.
- **Thông số Kỹ thuật (DSP):** `BPM` (kèm cảm giác nhịp thực tế), `Key & Scale`, độ nén bản mix, tỷ lệ năng lượng các dải tần.
- **Nhạc cụ, Giọng hát & Hòa thanh:** Lớp nhạc cụ dẫn dắt, chất giọng (nam/nữ, màu giọng, cách xử lý), vòng hòa thanh và câu Hook chính.
- **Cấu trúc bài nhạc & Lời bài hát (Lyrics):** Chia mốc thời gian từng đoạn (Intro, Verse, Chorus, Bridge, Outro), chép lại lời bài hát và chủ đề cốt lõi.
- **Insight Khán giả & Công thức SEO:** Khán giả khen gì nhất trong bình luận? Cách đặt Title/Keywords hút view của video gốc là gì?
- **Tóm tắt Sonic Brief (60–90 từ):** Đúc kết công thức âm thanh để truyền thẳng sang Bước 2 (`02-san-xuat-nhac.md`).

### Phần B: Phân Tích Hình Ảnh & Thế Giới Thị Giác (Phục vụ Bước 3 làm ảnh)
- **Thể loại hình ảnh của video gốc:** Video gốc thuộc dạng nào? (Thời trang nhảy múa / Kể chuyện bình yên / Thế giới cổ tích thu nhỏ / Ngắm cảnh hoài niệm...).
- **Nhân vật & Tạo hình:** Độ tuổi, giới tính, biểu cảm gương mặt, kiểu tóc, phụ kiện và số lượng nhân vật trong các cảnh.
- **Trang phục & Chất liệu:** Phom dáng, chất liệu vải, màu sắc và các chi tiết thiết kế nổi bật.
- **Bối cảnh, Ánh sáng & Bảng màu:** Không gian diễn ra ở đâu (trong phòng, ngoài thiên nhiên, thị trấn...)? Ánh sáng và bảng màu chủ đạo là gì?
- **Yếu tố Siêu thực / Điểm chạm Thẩm mỹ:** Video gốc dùng chi tiết siêu thực hay nghệ thuật gì để làm khung hình đẹp và thu hút người xem?
- **Danh sách các nhóm cảnh chính:** Tóm tắt các nhóm bối cảnh/ý tưởng xuất hiện dọc theo video.

### Phần C: Phân Tích Chuyển Động & Nhịp Cắt Cảnh (Phục vụ Bước 4 làm video)
- **Nhịp độ cắt cảnh (Pacing):** Tổng số cảnh (`shots`), thời lượng trung bình mỗi cảnh.
- **Bản chất chuyển động của Nhân vật:** Nhân vật trong video gốc cử động như thế nào? (Đứng/ngồi tĩnh tại, đi bộ chậm, làm việc đời thường, tương tác cặp đôi, hay nhảy múa theo nhịp?).
- **Chuyển động của Vật thể / Môi trường:** Gió thổi tà áo, hoa lá đung đưa, sóng biển, phương tiện di chuyển hay ánh sáng thay đổi ra sao?
- **Chuyển động Máy quay (Camera Motion):** Máy đứng tĩnh (`static`), đẩy chậm (`slow push-in`), kéo ra (`pull-out`) hay trượt ngang (`tracking`)?
