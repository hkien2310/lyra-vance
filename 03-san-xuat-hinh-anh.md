# 03 - Quy Tắc Sản Xuất Hình Ảnh (`image.txt`)

Tài liệu quy định Bước 3: Trao đổi về phần hình ảnh dựa trên phân tích video gốc $\rightarrow$ Viết vài prompt test để thử nghiệm $\rightarrow$ Khi ưng ý mới mở rộng sản xuất hàng loạt ra `projects/XX/image.txt`.

---

## 1. Quy Trình 3 Nhịp (Không Tự Ý Đẻ Hàng Loạt Khi Chưa Test)

### Nhịp 1: Trao Đổi & Bổ Sung Nhận Diện Hình Ảnh
1. AI đọc lại **Phần B (Phân tích Hình ảnh)** trong `projects/XX/phan-tich.md` và tóm tắt ngắn gọn cho người dùng:
   - Nhân vật, trang phục, bối cảnh, bảng màu và chi tiết siêu thực mà AI đã nhận diện được từ video gốc.
2. **Hỏi ý kiến người dùng:**
   - *"Ngoài những điểm AI nhận ra ở trên, bạn có thấy chi tiết nào đắt giá trong video gốc mà AI bỏ sót, hoặc muốn biến tấu / thêm chút siêu thực làm đẹp nào không?"*
3. Ghi nhận bổ sung của người dùng để chốt **Công thức Hình ảnh (Visual Formula)** cho dự án.

### Nhịp 2: Viết 3–5 Prompt Test
- Dựa trên Công thức Hình ảnh vừa chốt, AI viết **3 đến 5 câu Prompt Test tiếng Anh** đại diện cho các góc cảnh/ý tưởng chính của video.
- **Dừng lại** để người dùng đem 3–5 câu này đi tạo ảnh thử.
- Nếu ảnh test chưa ưng ở điểm nào (màu sắc, ánh sáng, phom quần áo, độ tuổi, độ siêu thực...), tinh chỉnh lại cấu trúc câu prompt cho đến khi ra ảnh đẹp chuẩn ý.

### Nhịp 3: Mở Rộng Sản Xuất Hàng Loạt (`projects/XX/image.txt`)
- Khi người dùng xác nhận **ưng kết quả Prompt Test** và chốt số lượng ảnh cần làm (ví dụ: 50, 60 hay 80 ảnh):
  - AI nhân bản theo đúng cấu trúc câu Prompt Test đã thành công, phát triển đa dạng các cảnh bám sát tinh thần video gốc và mạch bài nhạc (không tự bịa ra quy tắc chia phòng cứng nhắc).
  - Lưu toàn bộ danh sách câu lệnh tiếng Anh (mỗi dòng 1 prompt sạch, không đánh số đầu dòng) vào `projects/XX/image.txt`.

---

## 2. Nguyên Tắc Viết Prompt Ảnh Chuẩn [STYLE_lyra_vance_haute_surreal.md](file:///Users/hoangkien/Youtube/lyra-vance/STYLE_lyra_vance_haute_surreal.md)

- **1 Dòng = 1 Cảnh Tĩnh Sắc Nét:** Luôn giữ tỷ lệ `16:9`, không nhòe chuyển động (`zero motion blur`), chủ thể tách lớp rõ khỏi hậu cảnh, đứng/ngồi vững chãi (`100% grounded`).
- **Tôn Vẻ Đẹp Bằng Chút Siêu Thực Tinh Tế:** Cài cắm vừa đủ yếu tố siêu thực thơ mộng (trên chất liệu trang phục, vật thể hoặc không gian) đúng như đã thống nhất ở Nhịp 1–2.
- **Chuẩn Giới Tính & Thần Thái:** Ghi rõ giới tính và độ tuổi nhân vật, biểu cảm gương mặt có hồn, trang phục nam chuẩn lịch lãm (không mặc váy).
