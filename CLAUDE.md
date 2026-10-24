Quy tắc chỉnh sửa tài liệu này:
Không liệt kê lẻ tẻ sự vật sự kiện.
Không dùng phủ định.
Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

# CLAUDE.md - Quy Trình Vận Hành Tổng Thể (Lyra Vance)

> **Chức năng tài liệu (`File Role & Scope`):** Tài liệu điều phối trung tâm của toàn bộ hệ thống, phân định ranh giới bất khả xâm phạm giữa **Thư Mục Quy Chuẩn Gốc Toàn Kênh (`craft/` — chỉ đọc khi vận hành video)** và **Thư Mục Thực Thi Từng Dự Án (`projects/<STT>/` — nơi duy nhất được phép ghi và chỉnh sửa khi làm video)**.

## 1. Quy Tắc Bất Biến Về Bảo Toàn Tài Liệu Gốc (`Read-Only Master Docs Rule`)
- **Nhóm Tài liệu Gốc Toàn Kênh tại `craft/` ([craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md), [craft/02-idea.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/02-idea.md), [craft/03-san-xuat-nhac.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/03-san-xuat-nhac.md), [craft/04-visual.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/04-visual.md)):** Đóng vai trò bộ luật gốc chỉ đọc (`Read-Only`) và được giữ nguyên trạng tuyệt đối dưới mọi hình thức trong suốt quá trình vận hành sản xuất bất kỳ video nào.
- **Nhóm Tài liệu Thực thi Dự án tại `projects/<STT>/` (`projects/<STT>/idea.md`, `projects/<STT>/nhac.md`, `projects/<STT>/visual.md`):** Là khu vực duy nhất được phép tạo mới, ghi chép, phân tích và chỉnh sửa toàn bộ ý tưởng, âm nhạc, thế giới thị giác và câu lệnh của từng dự án video cụ thể.
- Luôn đọc [craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md) đầu tiên trước mọi bước thực thi để đồng bộ linh hồn và chuẩn mực thẩm mỹ toàn kênh.

## 2. Luồng Vận Hành Các Bước
1. **Nền tảng bắt buộc (`Chỉ đọc từ craft/`):** Đọc [craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md) — Hệ quy chiếu định vị khán giả, cảm xúc và định dạng nghệ thuật toàn kênh.
2. **Bước Kiến tạo Idea & Thế giới (`Đọc craft/02` $\rightarrow$ `Ghi projects/<STT>/idea.md`):** Đọc quy tắc tại [craft/02-idea.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/02-idea.md) để xuất bản thiết kế thế giới siêu thực riêng của dự án tại `projects/<STT>/idea.md`.
3. **Bước Sản xuất Âm nhạc (`Đọc craft/03` $\rightarrow$ `Ghi projects/<STT>/nhac.md`):** Đọc quy tắc tại [craft/03-san-xuat-nhac.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/03-san-xuat-nhac.md) và `projects/<STT>/idea.md` để xuất bản thiết kế âm nhạc và ca từ tại `projects/<STT>/nhac.md`.
4. **Bước Thiết kế Thế giới Thị giác (`Đọc craft/04` $\rightarrow$ `Ghi projects/<STT>/visual.md`):** Đọc quy tắc tại [craft/04-visual.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/04-visual.md), kết hợp `projects/<STT>/idea.md` và `projects/<STT>/nhac.md` để xuất bộ quy chuẩn thị giác riêng của dự án tại `projects/<STT>/visual.md`.
