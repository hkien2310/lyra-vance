# HƯỚNG DẪN ĐỌC & PHÂN TÍCH DỮ LIỆU GỐC (`raw/`) TRONG THƯ VIỆN ĐỐI THỦ (`doithu/`)

Tài liệu này là quy chuẩn dành cho AI và người sản xuất khi đọc thư mục `doithu/<ten-kenh>/<ten-video>/raw/` để tổng hợp thành bản báo cáo [`phan-tich.md`](file:///Users/hoangkien/Youtube/lyra-vance/doithu/surreal-ai/elderly-fashion-dance-we-are-the-late-light/phan-tich.md) và cập nhật vào mục lục trung tâm [`doithu/index.md`](file:///Users/hoangkien/Youtube/lyra-vance/doithu/index.md).

> **Nguyên tắc cốt lõi ("Tam Giác Kiểm Chứng"):**
> Mọi kết luận trong `phan-tich.md` được kiểm chứng chéo từ 3 nguồn trong `raw/`:
> 1. **Dữ liệu Kỹ thuật Cứng bằng Code (`audio_dsp.json`, `motion_metadata.json`, `seo_metadata.json`)** — cung cấp con số vật lý chính xác.
> 2. **Trực quan Đa phương thức của AI (`listen.mp3`, `thumbnail.jpg`, `shot_sheets/`, `grids/`)** — AI trực tiếp nghe nhạc và nhìn ảnh để nắm bắt cảm xúc, ca từ, màu giọng, chất liệu và chuyển động.
> 3. **Dữ liệu SEO & Phản hồi Khán giả (`seo.md`)** — đối chiếu ý đồ của chủ kênh với phản ứng thực tế từ Top 30–50 bình luận nhiều tim nhất.

---

## 1. Giải Thích Cấu Trúc Thư Mục `raw/` & Vai Trò Trong Phân Tích Chéo

Khi chạy lệnh `python3 common/ingest_doithu.py "<youtube_url>"`, hệ thống tự động sinh ra đầy đủ các file sau trong `doithu/<ten-kenh>/<ten-video>/raw/`:

| Tên file / Thư mục trong `raw/` | Nguồn tạo | Chức năng & Vai trò trong phân tích sâu |
| :--- | :--- | :--- |
| **`seo.md`** | `ingest_doithu.py` (`yt-dlp`) | Chứa Title, Tên kênh, Số Sub, Views, Likes, Ngày đăng, **Hidden Tags (Thẻ từ khóa ẩn)**, **Chapters (Mốc thời gian bài hát)**, toàn bộ Description, Hashtags và **Top 30–50 Comments nhiều tim nhất**. |
| **`seo_metadata.json`** | `ingest_doithu.py` | Dữ liệu JSON gốc của SEO & Chapters để các script âm thanh/hình ảnh đọc tự động. |
| **`thumbnail.jpg`** | `ingest_doithu.py` | Ảnh bìa gốc độ phân giải cao nhất (`maxresdefault`) -> Giải phẫu bố cục hình học, ngôn ngữ cơ thể, màu sắc tương phản và chất liệu mồi nhử thị giác (`Visual Hook`) tạo CTR cao. |
| **`video.mp4`** | `ingest_doithu.py` / `analyze_motion.py` | File video gốc tải về (`<=720p`) dùng làm nguồn tách nhạc và cắt khung hình. |
| **`listen.mp3`** | `analyze_audio.py` | File âm thanh nhẹ (`128kbps MP3`) -> **AI mở nghe trực tiếp** từ đầu đến cuối để phân tích nhạc lý, vòng hòa thanh, màu giọng, cách nhả chữ, lớp nhạc cụ và chép lời bài hát. |
| **`audio_dsp.json`** | `analyze_audio.py` (`librosa`) | Số đo vật lý bằng code: `BPM`, `Half-time BPM`, `Beat Stability`, `Key & Scale`, `Crest Factor (dB)`, phân bổ năng lượng `6 dải tần số (%)`, `Energy Sections`, và **thông số tách riêng cho từng bài hát (`tracks`)** theo Chapters. |
| **`motion_metadata.json`** | `analyze_motion.py` (`ffmpeg`) | Thống kê tổng số cảnh cắt (`total_shots`), thời lượng trung bình mỗi cảnh (`avg_shot_duration_sec`), danh sách timestamp từng shot. |
| **`shot_sheets/shots_*.jpg`** | `analyze_motion.py` | **Lưới ảnh tĩnh 3x3 chuẩn HD (`1280x720`/ô, tổng `3840x2160` 4K)**: Chụp chính giữa từng cảnh cắt từ đầu đến cuối video -> **AI mở xem toàn bộ các tấm `shots_*.jpg`** để lập danh mục 100% các nhóm chất liệu, phom dáng trang phục, đạo cụ và ánh sáng. |
| **`grids/grid_*.jpg`** | `analyze_motion.py` | **Lưới chuyển động 6x10 tốc độ cao (`4 FPS` — mỗi ô cách nhau `0.25 giây`, 15 giây/tấm)**: Bao phủ 100% thời lượng video -> Dùng để **soi chuyển động cơ thể, độ bay của vải, nhịp dựng theo khuông nhạc và góc máy**. |

---

## 2. Quy Trình Giải Phẫu 5 Chiều Cực Chi Tiết (Từ `raw/` -> `phan-tich.md`)

### CHIỀU 1: THEME, IDEA, TRIẾT LÝ THẨM MỸ & TÂM LÝ HỌC KHÁN GIẢ
*Đọc kết hợp `raw/seo.md` (Description + Top Comments) + `raw/thumbnail.jpg` + Nghe thông điệp trong `raw/listen.mp3`.*

AI phân tích rõ 4 lớp:
1. **Chủ đề Tư tưởng & Nghịch lý Trung tâm (`Core Theme & Central Tension`):**
   - Video đặt ra cuộc đối thoại hay sự đảo chiều định kiến nào? (Ví dụ: Định kiến *"tuổi già là phai tàn, sống bằng hoài niệm quá khứ"* vs Tuyên ngôn *"tuổi già là ánh sáng muộn rực rỡ nhất, sống trọn ở hiện tại"*).
2. **Triết lý Chuyển hóa Thẩm mỹ (`Aesthetic Sublimation`):**
   - Cách video biến những yếu tố đời thường hoặc dấu vết tuổi tác (nếp nhăn, tóc bạc, bước chân chậm) thành nghệ thuật cao cấp.
3. **Giải phẫu Tâm lý Khán giả từ Bình luận (`Audience Psychology from Top Comments`):**
   - Đối chiếu `Views` với `Subscribers` và tỷ lệ `Likes / Views`.
   - Phân loại các nhóm bình luận có lượt tim cao nhất: Khán giả ở độ tuổi nào? Nỗi đau hay khát khao thầm kín nào của họ được video chạm trúng? Câu chữ hay hình ảnh nào được họ trích dẫn lại nhiều nhất?
4. **Nghệ thuật Dựng Thumbnail (`Thumbnail Semiotics`):**
   - Phân tích bố cục hình học (tam giác, vòm, đối xứng), tương tác ánh mắt/bàn tay, bảng màu và lý do tại sao chất liệu trên Thumbnail thu hút lượt bấm vào.

---

### CHIỀU 2: NHẠC LÝ, HÒA THANH, PHỐI KHÍ & KIẾN TRÚC ÂM THANH (MUSICOLOGY & ARRANGEMENT)
*Đọc `raw/audio_dsp.json` (tổng thể & từng bài trong `tracks`) + Đọc `CHAPTERS` trong `raw/seo.md` + Nghe kỹ `raw/listen.mp3`.*

AI kết hợp "Code + Đôi Tai" để giải nghĩa bản chất âm nhạc học:
1. **Kiểm tra cấu trúc đơn bài hay đa bài (`Single vs Multi-Track`):**
   - Nhìn mục `tracks` trong `audio_dsp.json` và `CHAPTERS` trong `seo.md` để phân tích từng bài hát riêng biệt kèm bảng tổng hợp.
2. **Nhịp điệu học & Cảm giác Nhịp (`Tempo, Meter & Groove Pocket`):**
   - Đối chiếu `bpm` và `half_time_bpm` trong `audio_dsp.json` với cảm giác thực tế khi nghe `listen.mp3`: Giải thích cơ chế **Dual-Feel (Nhịp kép)** (ví dụ: trống Kick/Bass đánh nhịp 4/4 ở `112 BPM` tạo lực bước đi, câu hát và hợp âm trải dài theo nhịp Half-time `56 BPM` tạo sự khoan thai, đĩnh đạc).
   - Phân tích **Đảo phách (`Syncopation`) & Pocket**: Nhạc cụ gõ nào rơi vào phách mạnh (`downbeat`), nhạc cụ nào đánh lơi vào phách nhẹ (`off-beat`) tạo độ nảy (`bounce/swing`).
3. **Nhạc lý Hòa thanh & Thang âm (`Harmony, Tonality & Modal Color`):**
   - Giải thích màu sắc của `Key & Scale` (`Dorian`, `Aeolian`, `Natural Minor`, `Major`).
   - Phân tích **Vòng hòa âm (`Chord Progression`) & Kỹ thuật giữ nốt nền (`Pedal Point / Drone Bass`)**: Ở Verse hòa âm giữ tĩnh trên bậc `i` như thế nào để tạo tính nghi lễ thôi miên; khi lên Chorus, hòa âm mở sang bậc Trưởng (`VI - III - VII` hoặc `Parallel/Relative Major lift`) ra sao để nâng cảm xúc lên cao trào kiêu hãnh.
4. **Giải phẫu Bản Mix & Phổ Tần Số (`Spectral Balance & Dynamic Staging`):**
   - Từ bảng 6 dải tần số và `crest_factor_db` (`<11 dB` nén chặt; `11–15 dB` cân bằng nảy; `>15 dB` độ thở động học rộng), giải thích ý đồ kỹ thuật phòng thu: Tại sao dải trầm (`Sub-bass + Bass`) được đẩy lên mức `55%–88%`? Khoảng trống ở dải `Low-Mid` giúp giọng hát sạch ra sao? Việc làm dịu dải `High (>6kHz)` dưới `2%` tác động thế nào đến thính giác của khán giả lớn tuổi?
5. **Kiến trúc Phối khí & Thiết kế Giọng hát theo Thời gian (`Arrangement & Vocal Architecture`):**
   - Bóc tách từng lớp nhạc cụ (`Layering`) từ `Intro` -> `Pre-Groove` -> `Verse` -> `Pre-Chorus` -> `Chorus` -> `Post-Chorus Hook` -> `Bridge` -> `Outro`.
   - Phân tích chi tiết **Vocal Production**: Cách dùng `Close-mic Spoken Word` (khoảng cách mic, tiếng thở, độ vang), màu giọng chính (`timbre`, độ khàn `raspy`, `vibrato`, cách luyến láy), và cách dàn dựng bè hợp xướng (`Call-and-Response`, `Anthem Choir`, `Rhythmic Chants`).
   - Viết sẵn **`Suno Style Prompt` mẫu (60–90 từ tiếng Anh)** chuẩn xác cho từng bài.

---

### CHIỀU 3: THI PHÁP CA TỪ, CÁCH DÙNG TỪ & CẤU TRÚC LỜI BÀI HÁT (LYRICISM, DICTION & RHETORIC)
*Nghe `raw/listen.mp3` + Đọc `Description/Comments` trong `raw/seo.md`.*

Phân tích lời bài hát ở cấp độ nhà biên kịch và nhạc sĩ viết lời chuyên nghiệp:
1. **Toàn văn Lời bài hát & Mốc thời gian (`Full Verbatim Lyrics & Structural Map`):**
   - Chép lại đầy đủ 100% lời thoại (`Spoken Word`) và lời hát (`Sung Lyrics`) của tất cả các bài trong video kèm timestamp chính xác (`mm:ss`).
2. **Thủ pháp Tu từ & Cấu trúc Câu (`Rhetorical Devices & Framing`):**
   - **Thủ pháp Đối sánh (`Antithesis / Contrast Framing`):** Chỉ rõ các cặp câu đặt 2 khái niệm trái ngược cạnh nhau để định nghĩa lại giá trị sống (VD: *Mirror calls a wrinkle* vs *Spotlight calls design*).
   - **Thủ pháp Điệp cấu trúc (`Anaphora & Tricolon`):** Cách lặp lại cụm từ tạo nhịp điệu găm vào tâm trí người nghe.
3. **Giải phẫu Trường Từ vựng (`Lexical Fields & Sensory Diction`):**
   - Liệt kê và phân nhóm các từ khóa giàu tính hình ảnh (`Visual & Tactile Verbs/Nouns`) mà bài hát sử dụng:
     - *Trường từ vựng Ánh sáng & Nhiệt độ:* (`soft gold`, `halos`, `spotlight`, `spark in a glass`, `soft flame`, `late light`...)
     - *Trường từ vựng Cắt may, Vải vóc & Chuyển động cơ thể:* (`fabric`, `seams`, `hem`, `crease`, `turn of the wrist`, `look over the shoulder`, `worn a thousand stories in my skin`...) -> Chỉ ra cách lời bài hát mô tả trực tiếp chuyển động của trang phục trên màn hình.
4. **Nhịp điệu Ngôn từ & Gieo vần (`Prosody, Cadence & Rhyme Scheme`):**
   - Phân tích độ dài câu, cách đặt từ trọng âm rơi đúng vào phách trống mạnh (`downbeat`), cách mở nguyên âm cuối câu và cách gieo vần (`AABB`, `ABAB`, `internal rhyme`).

---

### CHIỀU 4: CHẤT LIỆU HỌC, CẤU TRÚC CẮT MAY & DANH MỤC TẠO HÌNH TOÀN DIỆN (`shot_sheets/`)
*Mở xem trực tiếp toàn bộ 100% các tấm `raw/shot_sheets/shots_*.jpg`.*

Soi kỹ từng tấm `shots_*.jpg` để bóc tách:
1. **Ngôn ngữ Không gian, Ánh sáng & Bảng màu (`Spatial Design, Lighting & Color Theory`):**
   - Phân tích tỷ lệ % các loại phông nền, hướng đánh sáng (`Rim light`, `Top-down spotlight`, `Diffused cyclorama light`), và bảng màu chủ đạo.
2. **Giải phẫu Nhân vật & Ngôn ngữ Cơ thể (`Casting, Styling & Embodied Presence`):**
   - Độ tuổi, sắc tộc, kiểu tóc/râu, chi tiết đôi bàn chân trần (`barefoot grounding`), thần thái gương mặt và tỷ lệ xoay vòng đội hình (`Solo` <-> `Duo` <-> `Trio` <-> `Ensemble`).
3. **Từ điển Giải phẫu Chất liệu & Hệ thống Trang phục Siêu thực (`Comprehensive Material & Silhouette Taxonomy`):**
   - Chia toàn bộ các cảnh trong `shot_sheets/` thành các Hệ Chất liệu & Cấu trúc Tạo hình cụ thể:
     - **Bản chất Vật liệu & Bề mặt xúc giác (`Tactile Surface`):** Sợi nấm, sợi cọ raffia, dây mây uốn 3D, giấy xếp origami, vải denim ghép boro, nham thạch phát sáng, gương vỡ mosaic, vảy quả thông, đồng chạm khắc, v.v.
     - **Cấu trúc Phom dáng (`Silhouette & Architectural Volume`):** Cổ áo đĩa mặt trời (`cartwheel/saucer ruff`), tay áo cánh vỏ sò chần bông, chân váy lồng đèn đa giác, cầu vai cổng vòm chạm đất, mũ chóp xoắn ốc...
     - **Cơ chế Bất thường Siêu thực (`Surreal Anomaly Mechanism`):** Trang phục biến thành dãy núi trên sàn, đầm mọc ra những ngôi nhà gỗ thu nhỏ, chim giấy bay khỏi gấu váy, đạo cụ khóa Sol bằng len...
     - **Từ vựng Prompt Tiếng Anh chuẩn xác (`Exact English Prompt Vocabulary`)** cho từng chất liệu để copy dùng ngay.
4. **Bảng Kiểm kê Chi tiết theo từng tấm `shot_sheets` (`Shot-by-Shot / Sheet-by-Sheet Visual Inventory`):**
   - Liệt kê từ `shots_01` đến tấm cuối cùng để tra cứu chính xác từng cảnh.

---

### CHIỀU 5: CHUYỂN ĐỘNG, NHỊP DỰNG & CHIẾN LƯỢC SEO ĐÓNG GÓI
*Đọc `raw/motion_metadata.json` + Xem `raw/grids/grid_*.jpg` + Đọc `raw/seo.md`.*

1. **Giải phẫu Nhịp dựng & Âm nhạc (`Musical Editing & Beat-Sync Pacing`):**
   - Tính toán mối liên hệ giữa `avg_shot_duration_sec` và `BPM` (ví dụ: mỗi cảnh cắt kéo dài đúng 2–3 khuông nhạc 4/4) và cách dựng thay đổi theo năng lượng bài hát.
2. **Động học Cơ thể & Vật lý Chất liệu (`Kinesiology & Fabric Physics`):**
   - Phân tích tỷ lệ góc máy (`Locked Static` vs `Single-Axis Push/Pull/Pan`) và các nhóm động tác giúp khoe trọn chất liệu trên mô hình tạo video.
3. **Chiến lược SEO, Từ khóa Ẩn & Nghệ thuật Viết Description (`SEO & Copywriting Formula`):**
   - Công thức đặt Title, toàn bộ danh sách `Hidden Tags`, `Hashtags`, và cấu trúc viết Description kiểu tâm sự cá nhân (`Human-led Storytelling`) kích thích bình luận.

---

## 3. Quy Tắc Cập Nhật Bảng Mục Lục [`doithu/index.md`](file:///Users/hoangkien/Youtube/lyra-vance/doithu/index.md)

Sau khi tạo xong `phan-tich.md` cho bất kỳ video nào, cập nhật 1 dòng vào bảng trong [`doithu/index.md`](file:///Users/hoangkien/Youtube/lyra-vance/doithu/index.md) gồm: Tên kênh & Tên video, Views / Likes, Thời lượng & Số bài hát, `BPM` & `Key` chuẩn, Dòng nhạc & Vocal Hook, Concept Hình ảnh & Yếu tố Siêu thực cốt lõi, cùng đường dẫn tới `phan-tich.md` và `raw/`.
