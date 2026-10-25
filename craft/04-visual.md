Quy tắc chỉnh sửa tài liệu này:
Không liệt kê lẻ tẻ sự vật sự kiện.
Không dùng phủ định.
Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

# 04 - Quy Tắc Thiết Kế Thế Giới Thị Giác & Chuyển Động (`Planimetric Stop-Motion Tiny World`)

> **Chức năng tài liệu (`File Role & Scope`):** Tài liệu gốc tại `craft/` quy định phương pháp chuyển hóa kịch bản từng dự án thành hệ thống nhân vật, bối cảnh thế giới thu nhỏ và xuất tệp câu lệnh `image.txt` / `video.txt` theo đúng quy luật tại [style/STYLE-BIBLE.md](file:///Users/hoangkien/Youtube/lyra-vance/style/STYLE-BIBLE.md).

## 1. Đầu Vào (`Input`)
- **Tài liệu bắt buộc đọc kèm:**
  1. [craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md) — Hệ quy chiếu thế giới thu nhỏ và định vị toàn kênh.
  2. [style/STYLE-BIBLE.md](file:///Users/hoangkien/Youtube/lyra-vance/style/STYLE-BIBLE.md) — Bộ quy luật gốc về 3 nhóm cư dân, tỷ lệ giải phẫu, bề mặt da theo độ tuổi, chất liệu sợi và dàn cảnh 2.5D.
  3. `projects/<STT>/idea.md` — Bản thiết kế tổ hợp `Sự kiện x Nỗi niềm` và mạch tự sự của dự án.
  4. `projects/<STT>/nhac.md` — Bản thiết kế nhịp điệu, âm thanh định danh và lời bài hát của dự án.

---

## 2. Quy Luật Chuyển Hóa Kịch Bản Thành Thị Giác (`Visual Translation Rules`)

### 2.1. Quy Luật Tuyển Chọn & Tạo Hình Ba Nhóm Cư Dân
- Lựa chọn tự do các cư dân đóng vai chính và vai phụ cho từng bài hát từ 3 nhóm của thế giới thu nhỏ (**Con người**, **Dạng người**, **Sinh vật khác**) sao cho cộng hưởng sâu sắc nhất với cảm giác chủ đạo trong `projects/<STT>/idea.md`.
- Áp dụng tỷ lệ đầu và thân lớn trên đôi chân que mảnh (`ultra-thin stick legs`) cho nhóm Con người và Dạng người, giữ hình thái tự nhiên cho nhóm Sinh vật khác; đồng thời sử dụng làn da đất sét tự nhiên theo độ tuổi (mịn màng ở người trẻ, có nét nhăn nhẹ ở người già), đôi mắt cầu 3D có lòng trắng (`huge wide-set soulful round cartoon eyes`), mái tóc sợi đầy đủ và trang phục/phụ kiện linh hoạt theo ngữ cảnh.

### 2.2. Quy Luật Kiến Tạo Không Gian Thị Trấn Kỳ Lạ Định Danh (`Strange Town Staging`)
- Thể hiện trực quan đặc điểm kỳ lạ gọi tên được của thị trấn ngay trên cả mặt phẳng tiền cảnh lẫn lớp phông nền hậu cảnh trong mọi phân cảnh của dự án.
- Duy trì bố cục ngang tầm mắt nhân vật (`medium full shot at eye-level`), phân tách rõ mặt phẳng đường phố/tiền cảnh sắc nét nơi cư dân sinh hoạt với phông nền thị trấn tranh vẽ mờ (`soft blurry painterly townscape background`) mang bầu khí quyển đồng điệu với tâm trạng bài hát.

### 2.3. Quy Luật Chuyển Động Stop-Motion Vi Mô
- Thiết kế chuyển động cho từng cảnh dựa trên những cử chỉ tinh tế của nhân vật (chớp đôi mắt tròn, nghiêng đầu, đung đưa đôi chân que, bước đi hoặc thao tác với đạo cụ nhỏ) kết hợp cùng sự lay động tự nhiên của sợi vải, mái tóc, khói ấm, sương mù và thời tiết theo nhịp điệu âm nhạc.

---

## 3. Quy Tắc Thực Thi Đầu Ra (`Output Execution Rules`)

### 3.1. Hồ Sơ Quy Chuẩn Thị Giác Dự Án (`projects/<STT>/visual.md`)
- Xác định rõ danh sách cư dân xuất hiện trong bài (thuộc nhóm Con người, Dạng người hay Sinh vật khác), hệ thống vật thể khổng lồ làm sân khấu tiền cảnh, phông nền hậu cảnh và bảng phân cảnh theo 3 hồi của bài hát trước khi xuất tệp câu lệnh.

### 3.2. Tệp Câu Lệnh Sinh Ảnh Hàng Loạt (`projects/<STT>/image.txt`)
- Mỗi câu lệnh tiếng Anh nằm trọn vẹn trên một dòng đơn duy nhất và tuân thủ nghiêm ngặt cấu trúc câu lệnh chuẩn tại [style/STYLE-BIBLE.md](file:///Users/hoangkien/Youtube/lyra-vance/style/STYLE-BIBLE.md) với phần hậu tố cố định: `Stylized stop-motion animation film still, matte clay, soft felt, and coarse yarn textures, flat planimetric staging against a soft blurry painterly ... background, moody fairytale atmosphere --ar 16:9`.

### 3.3. Tệp Câu Lệnh Chuyển Động Video (`projects/<STT>/video.txt`)
- Mỗi câu lệnh chuyển động tiếng Anh nằm trọn vẹn trên một dòng đơn duy nhất tương ứng 1:1 với từng dòng trong `image.txt`.

---

## 4. Template Output Bắt Buộc Cho `projects/<STT>/visual.md`

```markdown
# THIẾT KẾ THẾ GIỚI THỊ GIÁC — PROJECT <STT>

> **Chức năng tài liệu (`File Role & Scope`):** Hồ sơ thiết kế cư dân, bối cảnh thế giới thu nhỏ và bảng phân cảnh cho **Project <STT>** theo chuẩn `style/STYLE-BIBLE.md`, làm cơ sở trực tiếp để xuất `projects/<STT>/image.txt` và `projects/<STT>/video.txt`.

## 1. Dàn Cư Dân Của Dự Án (`Project Cast`)
- **Cư dân trung tâm (`Lead Figure`):** [Thuộc nhóm Con người / Dạng người / Sinh vật khác — Cụm từ khóa tiếng Anh khóa tạo hình]
- **Các cư dân đồng hành (`Supporting Figures`):** [Cụm từ khóa tiếng Anh cho các cư dân xuất hiện cùng trong bài]

## 2. Không Gian Thế Giới Thu Nhỏ & Bảng Màu (`Tiny World Stage & Palette`)
- **Vật thể tiền cảnh (`Foreground Giant Objects & Props`):** [Các vật thể lớn làm sân khấu và đạo cụ qua từng chặng]
- **Phông nền tranh vẽ mờ (`Painterly Backdrops`):** [Không gian hậu cảnh và thời tiết tương ứng]

## 3. Bảng Phân Cảnh Khớp Nhạc (`Storyboard Mapping`)
- **Hồi 1 (Khởi phát sự kiện):** [Danh sách các cảnh mở đầu]
- **Hồi 2 (Triển khai cảm giác):** [Danh sách các cảnh phát triển và cao trào]
- **Hồi 3 (Lắng đọng & Kết):** [Danh sách các cảnh khép lại câu chuyện]
```
