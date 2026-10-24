# 01 - Quy Tắc Phân Tích Nhạc & Nội Dung (Lyra Vance)

Tài liệu quy định quy trình vận hành **Bước 1**: AI đọc kết quả phân tích âm thanh bằng code (`audio_dsp.json`) + đọc dữ liệu `SEO & Top Comments` (`seo.md`) + nghe lại trực tiếp file âm thanh (`listen.mp3`) đã được tách sẵn từ **Bước 0** ([`00-xu-ly-vat-ly.md`](file:///Users/hoangkien/Youtube/lyra-vance/00-xu-ly-vat-ly.md)) để bóc tách cấu trúc âm thanh, nội dung lời và tâm lý thính giả. Kết quả lưu tại `projects/XX/phan-tich-nhac.md` làm dữ liệu nền tảng chuyển sang Bước 2 ([`02-san-xuat-nhac.md`](file:///Users/hoangkien/Youtube/lyra-vance/02-san-xuat-nhac.md)).

---

## 1. Quy Trình Đọc Đầu Vào (Từ Đầu Ra Của Bước 0)

Tại thư mục dữ liệu đã chạy xong Bước 0 (`projects/XX/doi-thu/` hoặc `doithu/<ten-kenh>/<ten-video>/raw/`), AI đọc trực tiếp 3 nguồn:
1. **Đọc phân tích âm thanh bằng code (`audio_dsp.json`):** Lấy chính xác các con số vật lý đã đo ở Bước 0 (`BPM`, `Half-time BPM`, `Beat Stability`, `Key & Scale`, `Crest Factor / Độ nén bản mix`, `Tỷ lệ năng lượng 6 dải tần số`, và `Energy Sections` tổng thể / từng bài).
2. **Đọc dữ liệu SEO & Bình luận khán giả (`seo.md`):** Lấy `TITLE`, `DESCRIPTION`, `HASHTAGS`, `HIDDEN TAGS`, `CHAPTERS` và toàn bộ `TOP COMMENTS`.
3. **Nghe lại trực tiếp file âm thanh (`listen.mp3`):** Nghe từ đầu đến cuối để xác thực nhạc cụ, màu giọng, vòng hòa thanh, cấu trúc câu hook và chép lời bài hát (kết hợp với ghi chú cảm nhận cá nhân của người dùng nếu có).

---

## 2. Cấu Trúc Phân Tích 3 Tầng (`projects/XX/phan-tich-nhac.md`)

Kết hợp số liệu từ `audio_dsp.json` với bằng chứng thính giác khi nghe `listen.mp3` và dữ liệu `seo.md`:

### Tầng 1: Âm Thanh & Kỹ Thuật (Sound & DSP)
- **Thể loại chính (Main Genre):** Xác định một thể loại âm nhạc cốt lõi.
- **Nhánh phụ và Giao thoa (Sub-genres & Fusion):** Từ 2 đến 4 nhánh âm nhạc phụ và cách chúng kết hợp với nhau.
- **Ảnh hưởng và Thời kỳ (Reference Era):** Thập niên, trào lưu hoặc dòng chảy âm nhạc được phản ánh qua cách phối khí.
- **Không khí và Cảm xúc (Mood & Atmosphere):** Từ 4 đến 6 tính từ đặc tả và 1 đến 2 câu mô tả trạng thái cảm xúc mà bản nhạc gợi lên.
- **Nhạc cụ và Thiết kế âm thanh (Instruments & Sound Design):** Liệt kê từng lớp nhạc cụ nghe được kèm theo vai trò (nền tảng, dẫn dắt, điểm xuyết, chuyển đoạn), đặc tính âm sắc, dải tần số (đối chiếu với `frequency_energy_pct` trong `audio_dsp.json`) và hiệu ứng biến thiên điện tử.
- **Giọng hát (Vocals):** Giới tính, chất giọng, kỹ thuật thanh nhạc, ngôn ngữ, vai trò trong bản phối, hiệu ứng xử lý âm thanh và sự thay đổi cảm xúc qua từng đoạn.
- **Nhịp độ và Tiết tấu (Tempo & Rhythm):** Chỉ số **BPM chính xác** từ `audio_dsp.json` (ghi rõ cả cảm giác nhịp thực tế nếu là half-time/double-time), số chỉ nhịp, độ ổn định nhịp (`beat_stability`), kiểu groove và đặc trưng tiết tấu.
- **Hòa thanh (Key & Harmony):** **Giọng (Key) và Âm giai (Scale/Mode)** từ `audio_dsp.json` kết hợp thẩm âm thực tế, cùng tính chất vòng hòa thanh.
- **Giai điệu và Motif (Melody & Motifs):** Đường nét giai điệu, cấu trúc câu hook chính, quãng âm và nhạc cụ/giọng hát đảm nhận giai điệu chủ đạo.
- **Cấu trúc bài nhạc (Song Structure):** Chia mốc thời gian (timestamp) chính xác cho từng phần (kết hợp `energy_sections` trong `audio_dsp.json` và điểm chuyển đoạn nghe được) kèm mô tả diễn biến âm thanh.
- **Đường cong năng lượng (Energy Arc):** Cách cường độ âm nhạc tích tụ, bùng nổ, lắng xuống và chuyển tiếp xuyên suốt bài.
- **Ghi chú Sản xuất và Mix (Production & Mix Notes):** Độ rộng không gian stereo, đặc tính reverb, dải động thực tế (`crest_factor_db` & `compression_character`), tỷ lệ Sub-bass/Bass/Mid/High và các hiệu ứng chuyển đoạn.

### Tầng 2: Nội Dung Ca Từ (Content)
- **Lời bài hát đầy đủ (Full Lyrics):** Chép lại toàn bộ lời bài hát nghe được từ bản thu `listen.mp3` (đánh dấu `[unclear]` tại các vị trí âm thanh mờ; nếu là nhạc không lời ghi rõ `Instrumental`).
- **Ngôn ngữ và Giọng văn (Language & Register):** Ngôn ngữ sử dụng và sắc thái biểu đạt của ca từ.
- **Chủ đề cốt lõi (Theme & Core Message):** Tóm tắt thông điệp chính trong một câu và làm rõ các tầng ý nghĩa cảm xúc bên dưới.
- **Mạch phát triển lời (Narrative Arc):** Cách nội dung ca từ tiến triển từ phần mở đầu đến phần kết thúc.
- **Hình ảnh ẩn dụ trong lời (Lyrical Metaphors):** Các hình ảnh văn học và phép ẩn dụ nổi bật được sử dụng trong câu chữ.
- **Sự đồng bộ giữa Lời và Nhạc (Lyrics-Music Alignment):** Cách các câu hát quan trọng ăn khớp với điểm rơi nhịp điệu và cao trào âm nhạc.

### Tầng 3: Tác Động Tâm Lý Thính Giả & Phản Hồi Thực Tế (Impact & Audience Proof)
- **Sức nặng của Hook (Hook Power):** Khoảnh khắc âm nhạc hoặc câu hát gây nhớ nhất và cơ chế tạo nên sự bắt tai đó.
- **Điểm chạm cảm xúc (Emotional Triggers):** Từ 2 đến 4 mốc thời gian cụ thể tạo phản ứng cảm xúc mạnh mẽ nhất cùng cơ chế âm nhạc đứng sau.
- **Phân tích Bình luận Khán giả (Audience Comments Insight):** *(Trích xuất từ phần `TOP COMMENTS` trong `seo.md`)* Khán giả thực tế đang khen ngợi, ám ảnh hay bàn tán nhiều nhất về yếu tố nào (giọng hát, nhịp trống, cảm giác thôi miên, câu hát chạm cảm xúc...)?
- **Yếu tố nghe lại (Replay Factor):** Những chi tiết âm thanh hoặc cảm xúc thúc đẩy người nghe bấm phát lại.
- **Dư âm cảm xúc (Target Feeling):** Một câu mô tả trạng thái cảm xúc đọng lại trong lòng người nghe khi bài nhạc kết thúc.

---

## 3. Tổng Hợp & Đối Chiếu SEO (Synthesis & SEO Cross-check)

- **Tóm tắt Chủ đề & Âm học (Theme & Sonic Brief):** Một đoạn văn ngắn (60 đến 90 từ) đúc kết chủ đề cốt lõi, mạch cảm xúc, thông số `BPM` + `Key` và công thức nhịp điệu để truyền thẳng sang Bước 2 ([`02-san-xuat-nhac.md`](file:///Users/hoangkien/Youtube/lyra-vance/02-san-xuat-nhac.md)).
- **Đối chiếu SEO Đối thủ (SEO & Genre Cross-check):**
  - So sánh kết quả phân tích âm học với `TITLE`, `DESCRIPTION`, `HASHTAGS`, `HIDDEN TAGS` trong `seo.md` để chuẩn hóa bộ từ khóa thể loại chính xác nhất.
  - Rút ra **Công thức SEO & Định vị (SEO Angle)** của video đối thủ (cách đặt tiêu đề, từ khóa ngách thu hút view) để tham khảo cho dự án.
