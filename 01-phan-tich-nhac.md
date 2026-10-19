# 01 - Quy Tắc Phân Tích Nhạc & SEO Đối Thủ (Lyra Vance - Local Workflow)

Tài liệu quy định quy trình vận hành Bước 1 tại Local: kết hợp đo đạc tín hiệu âm học bằng script (`common/analyze_audio.py`), nghe trực tiếp bằng Multimodal và mổ xẻ dữ liệu SEO/Comments đối thủ từ `projects/XX/doi-thu/`. Kết quả lưu tại `projects/XX/phan-tich-nhac.md` để làm dữ liệu nền tảng cho Bước 2 (`02-san-xuat-nhac.md`).

---

## 1. Quy Trình Đầu Vào & Thực Thi Tự Động (Local)

### Đầu vào tại `projects/XX/doi-thu/`
Người dùng chỉ cần bỏ vào thư mục `projects/XX/doi-thu/` (ví dụ `projects/01/doi-thu/`):
1. **File nhạc hoặc video đối thủ** (`.mp3`, `.wav`, `.m4a`, `.mp4`, `.mov`...).
2. **File SEO đối thủ** (`.md` hoặc `.txt` lưu từ extension `youtube-scraper`, chứa `TITLE`, `DESCRIPTION`, `HASHTAGS`, `TOP COMMENTS`).
3. *(Tùy chọn)* Ghi chú cảm nhận cá nhân kèm theo câu lệnh (ví dụ: *"Phân tích project 01, bài này đoạn bass giữa bài rất cuốn"*). Nếu người dùng không ghi kèm, tiến hành phân tích thẳng không hỏi lại từng bước.

### Các bước AI tự động thực thi
1. **Đo thông số kỹ thuật chuẩn (DSP):** Chạy lệnh:
   ```bash
   python3 common/analyze_audio.py projects/XX/doi-thu
   ```
   Lấy số liệu chính xác về: `BPM` (kèm half/double-time), `Key & Scale` (Krumhansl-Schmuckler chroma), `Crest Factor / Độ nén bản mix`, `Tỷ lệ năng lượng 6 dải tần số`, và `Các mốc phân đoạn năng lượng (Energy Sections)`. *(Nếu đầu vào là video hoặc file lớn >25MB, script tự động tách sẵn file `*_listen.mp3` nhẹ để AI nghe).*
2. **Nghe Multimodal & Đọc SEO:** Dùng `view_file` đọc trực tiếp file âm thanh (hoặc file `*_listen.mp3`) từ đầu đến cuối, đồng thời đọc file SEO đối thủ trong `projects/XX/doi-thu/`.
3. **Tổng hợp & Lưu kết quả:** Lập báo cáo theo Cấu trúc 3 Tầng bên dưới và lưu vào `projects/XX/phan-tich-nhac.md`.

---

## 2. Cấu Trúc Phân Tích 3 Tầng (`projects/XX/phan-tich-nhac.md`)

Kết hợp số liệu đo từ `common/analyze_audio.py` với bằng chứng thính giác thực tế khi nghe file âm thanh và dữ liệu từ người dùng/khán giả:

### Tầng 1: Âm Thanh & Kỹ Thuật (Sound & DSP)
- **Thể loại chính (Main Genre):** Xác định một thể loại âm nhạc cốt lõi.
- **Nhánh phụ và Giao thoa (Sub-genres & Fusion):** Từ 2 đến 4 nhánh âm nhạc phụ và cách chúng kết hợp với nhau.
- **Ảnh hưởng và Thời kỳ (Reference Era):** Thập niên, trào lưu hoặc dòng chảy âm nhạc được phản ánh qua cách phối khí.
- **Không khí và Cảm xúc (Mood & Atmosphere):** Từ 4 đến 6 tính từ đặc tả và 1 đến 2 câu mô tả trạng thái cảm xúc mà bản nhạc gợi lên.
- **Nhạc cụ và Thiết kế âm thanh (Instruments & Sound Design):** Liệt kê từng lớp nhạc cụ nghe được kèm theo vai trò (nền tảng, dẫn dắt, điểm xuyết, chuyển đoạn), đặc tính âm sắc, dải tần số (đối chiếu với `frequency_energy_pct` từ script) và hiệu ứng biến thiên điện tử.
- **Giọng hát (Vocals):** Giới tính, chất giọng, kỹ thuật thanh nhạc, ngôn ngữ, vai trò trong bản phối, hiệu ứng xử lý âm thanh và sự thay đổi cảm xúc qua từng đoạn.
- **Nhịp độ và Tiết tấu (Tempo & Rhythm):** Chỉ số **BPM chính xác** từ script (ghi rõ cả cảm giác nhịp thực tế nếu là half-time/double-time), số chỉ nhịp, độ ổn định nhịp (`beat_stability`), kiểu groove và đặc trưng tiết tấu.
- **Hòa thanh (Key & Harmony):** **Giọng (Key) và Âm giai (Scale/Mode) chính xác** từ script kết hợp thẩm âm thực tế, cùng tính chất vòng hòa thanh.
- **Giai điệu và Motif (Melody & Motifs):** Đường nét giai điệu, cấu trúc câu hook chính, quãng âm và nhạc cụ/giọng hát đảm nhận giai điệu chủ đạo.
- **Cấu trúc bài nhạc (Song Structure):** Chia mốc thời gian (timestamp) chính xác cho từng phần (kết hợp `energy_sections` từ script và điểm chuyển đoạn nghe được) kèm mô tả diễn biến âm thanh.
- **Đường cong năng lượng (Energy Arc):** Cách cường độ âm nhạc tích tụ, bùng nổ, lắng xuống và chuyển tiếp xuyên suốt bài.
- **Ghi chú Sản xuất và Mix (Production & Mix Notes):** Độ rộng không gian stereo, đặc tính reverb, dải động thực tế (`crest_factor_db` & `compression_character`), tỷ lệ Sub-bass/Bass/Mid/High và các hiệu ứng chuyển đoạn.

### Tầng 2: Nội Dung Ca Từ (Content)
- **Lời bài hát đầy đủ (Full Lyrics):** Chép lại toàn bộ lời bài hát nghe được từ bản thu (đánh dấu `[unclear]` tại các vị trí âm thanh mờ; nếu là nhạc không lời ghi rõ `Instrumental`).
- **Ngôn ngữ và Giọng văn (Language & Register):** Ngôn ngữ sử dụng và sắc thái biểu đạt của ca từ.
- **Chủ đề cốt lõi (Theme & Core Message):** Tóm tắt thông điệp chính trong một câu và làm rõ các tầng ý nghĩa cảm xúc bên dưới.
- **Mạch phát triển lời (Narrative Arc):** Cách nội dung ca từ tiến triển từ phần mở đầu đến phần kết thúc.
- **Hình ảnh ẩn dụ trong lời (Lyrical Metaphors):** Các hình ảnh văn học và phép ẩn dụ nổi bật được sử dụng trong câu chữ.
- **Sự đồng bộ giữa Lời và Nhạc (Lyrics-Music Alignment):** Cách các câu hát quan trọng ăn khớp với điểm rơi nhịp điệu và cao trào âm nhạc.

### Tầng 3: Tác Động Tâm Lý Thính Giả & Phản Hồi Thực Tế (Impact & Audience Proof)
- **Sức nặng của Hook (Hook Power):** Khoảnh khắc âm nhạc hoặc câu hát gây nhớ nhất và cơ chế tạo nên sự bắt tai đó.
- **Điểm chạm cảm xúc (Emotional Triggers):** Từ 2 đến 4 mốc thời gian cụ thể tạo phản ứng cảm xúc mạnh mẽ nhất cùng cơ chế âm nhạc đứng sau.
- **Phân tích Bình luận Khán giả (Audience Comments Insight):** *(Trích xuất từ phần `TOP COMMENTS` trong file SEO đối thủ)* Khán giả thực tế đang khen ngợi, ám ảnh hay bàn tán nhiều nhất về yếu tố nào (giọng hát, nhịp trống, cảm giác thôi miên, trang phục/vũ đạo ăn khớp nhạc...)?
- **Yếu tố nghe lại (Replay Factor):** Những chi tiết âm thanh hoặc cảm xúc thúc đẩy người nghe bấm phát lại.
- **Dư âm cảm xúc (Target Feeling):** Một câu mô tả trạng thái cảm xúc đọng lại trong lòng người nghe khi bài nhạc kết thúc.

---

## 3. Tổng Hợp & Đối Chiếu SEO (Synthesis & SEO Cross-check)

- **Tóm tắt Chủ đề & Âm học (Theme & Sonic Brief):** Một đoạn văn ngắn (60 đến 90 từ) đúc kết chủ đề cốt lõi, mạch cảm xúc, thông số `BPM` + `Key` và công thức nhịp điệu để truyền thẳng sang Bước 2 (`02-san-xuat-nhac.md`).
- **Đối chiếu SEO Đối thủ (SEO & Genre Cross-check):**
  - So sánh kết quả phân tích âm học với `TITLE`, `DESCRIPTION`, `HASHTAGS` của đối thủ để chuẩn hóa bộ từ khóa thể loại chính xác nhất.
  - Rút ra **Công thức SEO & Định vị (SEO Angle)** của video đối thủ (cách đặt tiêu đề, từ khóa ngách thu hút view) để tham khảo cho dự án.
