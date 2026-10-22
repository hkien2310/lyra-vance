# 03 - Quy Tắc Phân Tích Hình Ảnh & Kiến Tạo File Style (Lyra Vance)

Tài liệu quy định quy trình vận hành Bước 3: từ hình ảnh của bất kỳ video mẫu nào, AI phân tích và đúc kết thành **Hệ thống Quy luật Thị giác (`projects/XX/phan-tich-hinh-anh.md`)**, sau đó qua các vòng tạo Prompt Test và nhận Feedback từ người dùng để tiến hóa file phân tích đó thành **File Style Hoàn Chỉnh (`Living Style Bible`)**.

---

## 1. Ba Nguyên Tắc Bất Di Bất Dịch Khi Viết Phân Tích

1. **Đúc kết thành Quy luật (`Pure Rule Extraction`):** Tuyệt đối viết dưới dạng quy luật thiết kế khái quát và nguyên lý tạo hình thống nhất; thay thế hoàn toàn lối viết tình huống lẻ tẻ (`Use Case`).
2. **Trừu tượng hóa nguyên lý (`Principle over Scattered Objects`):** Phân tích cấu trúc hình học, cơ chế chất liệu, tương quan không gian và quy luật thị giác thay vì liệt kê danh sách đồ vật hay sự kiện rời rạc.
3. **Ngôn ngữ Khẳng định Tuyệt đối (`100% Affirmative Language`):** Toàn bộ câu chữ tiếng Việt và câu lệnh tiếng Anh chỉ dùng mệnh đề khẳng định trực diện về những thuộc tính cần kiến tạo.

---

## 2. Quy Trình Tiến Hóa Từ Bản Phân Tích Thành File Style (3 Vòng Lặp)

1. **Vòng 1 — Khởi tạo Bản Phân tích Quy luật (`projects/XX/phan-tich-hinh-anh.md`):**
   - Quan sát bộ ảnh của video mẫu (`shot_sheets/`, `grids/`, `thumbnail.jpg`), đúc kết toàn bộ đặc trưng thị giác thành hệ thống quy luật khẳng định trong `projects/XX/phan-tich-hinh-anh.md`.
2. **Vòng 2 — Xuất Prompt Test Tái tạo (`Test Prompts`):**
   - Từ các quy luật trong file phân tích, xuất từ **3 đến 5 câu Prompt Test tiếng Anh** để người dùng chạy thử trên công cụ tạo ảnh.
3. **Vòng 3 — Nhận Feedback & Nâng cấp thành File Style (`Iterative Style Refinement`):**
   - Khi người dùng phản hồi về kết quả ảnh test (ví dụ: cần tinh chỉnh chất liệu trang phục, biểu cảm hay ánh sáng...), AI tìm đúng quy luật gốc, **cập nhật/bổ sung trực tiếp quy luật mới vào file `projects/XX/phan-tich-hinh-anh.md`**, rồi xuất lại Prompt Test mới.
   - Sau khi ảnh test đạt độ hoàn mỹ, `projects/XX/phan-tich-hinh-anh.md` chính thức trở thành **File Style Chuẩn** để sinh hàng loạt `projects/XX/image.txt`.

---

## 3. Khung Cấu Trúc Mở Rộng Linh Hoạt (4 Trụ Cột Cốt Lõi + Các Field Mở Rộng)

Bốn mục đầu (`Nhân vật`, `Trang phục`, `Môi trường`, `Siêu thực`) là khung xương sống tối thiểu. Tùy thuộc vào đặc thù của từng video mẫu (studio thời trang, thiên nhiên kỳ vĩ, công trình cự thạch, nghi thức du mục...), **AI chủ động bổ sung thêm các Field / Mục con mới** để bao quát trọn vẹn DNA thị giác của video đó:

### 1. Nhân Vật (`Character Rules`)
- **1.1. Hình mẫu, Độ tuổi & Tỷ lệ Hình thể (`Archetype & Physique Rule`):** Độ tuổi, vóc dáng, tỷ lệ chiều cao và chuẩn mực vẻ đẹp xuyên suốt.
- **1.2. Kết cấu Làn da, Đường nét & Kiến trúc Tóc (`Skin, Facial Structure & Hair Rule`):** Độ chân thực xúc giác của làn da và cách tạo khối mái tóc/râu.
- **1.3. Thần thái Tươi vui & Nụ cười Khép môi (`Joyful Closed-Lip Smile & Vibrant Gaze Rule`):** Đường nét thanh tú tự nhiên kết hợp nụ cười khép môi rạng rỡ giàu năng lượng (`refined natural features with a radiant joyful closed-lip smile`) để đồng bộ hoàn hảo với Bước 4 (Animation).
- **1.4. Tư thế Đang Nhảy Giữa Nhịp & Đa dạng Dáng Khởi đầu (`Mid-Action Kinetic Pose & Diversity Rule`):** Bắt trọn khoảnh khắc nhân vật đang ở giữa một nhịp nhảy sôi nổi (`captured mid-groove / mid-spin with active limb momentum`) và biến thiên tư thế giữa các bức ảnh để tạo đà vật lý tốc độ thực cho Bước 4.
- *(Mở rộng thêm các mục con nếu video có đặc trưng riêng về nhân vật).*

### 2. Trang Phục (`Costume & Materiality Rules`)
- **2.1. Cấu trúc Trang phục Toàn khối (`Unified Full-Body Garment Rule`):** Sự liền mạch và đồng nhất chất liệu trên 100% diện tích bộ đồ từ cổ, vai, tay áo đến hết chân váy hoặc ống quần.
- **2.2. Phom dáng, Đường cắt & Hình học Đường cong (`Silhouette & Curve Geometry Rule`):** Tỷ lệ chiết eo, độ mở tà vải và hệ thống đường cong sinh học mềm mại.
- **2.3. Hệ Chất liệu & Kỹ thuật Bề mặt Vi mô (`Tactile Materiality & Micro-Craft Rule`):** Cấu trúc thớ vải, nếp gấp vi mô, các lớp cánh lụa hoặc bề mặt hội họa đắp nổi.
- **2.4. Phụ kiện Điêu khắc & Đạo cụ Gắn liền (`Integrated Headwear, Talismans & Props Rule`):** Cách mũ mão, cổ áo, trang sức hoặc đạo cụ cầm tay phát triển liền khối từ ngôn ngữ thiết kế của trang phục.
- *(Mở rộng thêm các mục con nếu video có cơ chế trang phục đặc biệt).*

### 3. Môi Trường (`Environment & Spatial Rules`)
- **3.1. Cấu trúc Không gian & Giới hạn Bối cảnh (`Spatial Topology Rule`):** Định nghĩa không gian là phòng trưng bày chính diện khép kín (`Closed Front-Parallel Gallery`) hay cảnh quan thiên nhiên mở vô tận (`Open Infinite Landscape`).
- **3.2. Mặt phẳng Nền & Kết cấu Hậu cảnh (`Ground Plane & Backdrop Surface Rule`):** Chất liệu mặt sàn/địa hình nơi nhân vật đứng và cấu trúc bề mặt của bức tường nghệ thuật hoặc chân trời phía sau.
- **3.3. Hệ thống Vật thể & Kiến trúc Môi trường (`Environmental Objects & Monuments Rule`):** Các tác phẩm phù điêu, tranh tường, khối địa chất hoặc công trình kiến trúc hiện diện trong không gian và khoảng cách tương tác với nhân vật.
- *(Mở rộng thêm các mục con về Khí quyển, Thời tiết, Sinh thái... khi phân tích video ngoại cảnh).*

### 4. Siêu Thực (`Surrealism & Visual Metaphor Rules`)
- **4.1. Sự Liền mạch giữa Chủ thể và Thế giới (`Subject-to-World Continuity Rule`):** Cơ chế hòa quyện màu sắc, đường nét và chất liệu giữa môi trường hậu cảnh và trang phục nhân vật (`Living Canvas`).
- **4.2. Giả kim Chất liệu Duyên dáng (`Poetic Material Alchemy Rule`):** Nguyên lý chuyển hóa các chất liệu hội họa, khoáng vật và tự nhiên thành cấu trúc thời trang cao cấp mềm mại.
- **4.3. Đồng tâm Hình học & Phóng đại Tỷ lệ (`Geometric Alignment & Scale Harmony Rule`):** Cách đặt nhân vật vào tâm đối xứng của bối cảnh và phóng đại tỷ lệ trang phục/vật thể một cách thanh lịch.

### 5. Bảng Màu, Ánh Sáng & Quang Học Máy Quay (`Chromatic, Lighting & Camera Rules`)
- **5.1. Quy luật Phân bổ Bảng màu & Điểm neo Sắc độ (`Chromatic Palette & Anchor Rule`):** Hệ màu chủ đạo, màu nhấn và tỷ lệ phối màu giữa nhân vật với bối cảnh.
- **5.2. Quy luật Nguồn sáng & Khí quyển (`Lighting Diffusion & Atmosphere Rule`):** Hướng sáng, độ mềm của ánh sáng khuếch tán và độ nổi khối 3D của bề mặt vật chất.
- **5.3. Quy luật Góc máy, Đường Chân tường/Chân trời & Cự ly (`Camera Angle, Horizon Line & Framing Rule`):** Góc đặt máy, độ cân bằng của đường giao tuyến sàn-tường/chân trời, độ sâu trường ảnh và sự luân phiên cỡ cảnh (`Wide`, `Medium`, `Close-Up`).

### 6. Khuôn Mẫu DNA Prompt Sinh Ảnh (`Master Prompt DNA & Verified Test Prompts`)
- **6.1. Công thức Lắp ghép Prompt Chuẩn (`Master Prompt Formula`):** Khung câu lệnh tiếng Anh khẳng định 100% đúc kết từ toàn bộ các quy luật trên.
- **6.2. Bộ Prompt Chuẩn Đã Kiểm Chứng (`Verified Reference Prompts`):** Lưu giữ các câu prompt mẫu đã qua tinh chỉnh cùng người dùng để làm khuôn đúc cho bước sản xuất hàng loạt (`image.txt`).
