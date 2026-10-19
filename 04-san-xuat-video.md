# 04 - Quy Tắc Sản Xuất Chuyển Động Video (`video.txt`)

Tài liệu quy định Bước 4: Trao đổi về cách chuyển động (Animate) cho bộ ảnh đã có $\rightarrow$ Viết vài prompt motion test để thử nghiệm $\rightarrow$ Khi ưng ý mới mở rộng sản xuất hàng loạt ra `projects/XX/video.txt`.

---

## 1. Quy Trình 3 Nhịp (Tương Tự Bước Làm Ảnh)

### Nhịp 1: Trao Đổi Về Chuyển Động (Animate)
1. AI đối chiếu **Phần C (Phân tích Chuyển động của video gốc)** trong `projects/XX/phan-tich.md` với danh sách cảnh trong `projects/XX/image.txt`.
2. Tóm tắt ngắn gọn đề xuất chuyển động cho người dùng và hỏi:
   - *"Với bộ ảnh này, mình sẽ dùng các kiểu chuyển động [nhảy múa nhịp nhàng / đi dạo khoan thai / ngồi tĩnh đón gió / tương tác cặp đôi...] và góc máy [tĩnh / đẩy chậm...] như video gốc. Bạn muốn giữ nguyên hay điều chỉnh nhịp độ ở đâu không?"*

### Nhịp 2: Viết 3–5 Prompt Motion Test
- Sau khi thống nhất kiểu chuyển động, AI viết **3 đến 5 câu Prompt Motion tiếng Anh** tương ứng với các bức ảnh test để người dùng đưa vào tool tạo video chạy thử.
- **Dừng lại** chờ người dùng kiểm tra kết quả video test:
  - Nếu chuyển động bị nhanh quá, bị méo tay chân hay lem vải, AI điều chỉnh lại động từ chuyển động cho êm và gọn hơn.

### Nhịp 3: Mở Rộng Sản Xuất Hàng Loạt (`projects/XX/video.txt`)
- Khi người dùng xác nhận **ưng kết quả Motion Test**:
  - AI viết toàn bộ danh sách câu lệnh chuyển động khớp 1:1 với từng dòng trong `projects/XX/image.txt` (hoặc viết theo dạng tổng quát dùng chung tùy theo yêu cầu ghép tool của người dùng).
  - Xuất kết quả sạch (mỗi dòng 1 prompt, không đánh số đầu dòng) vào `projects/XX/video.txt`.

---

## 2. Nguyên Tắc Viết Prompt Chuyển Động Mượt & Ít Lỗi AI

1. **Chuyển động Đúng Bản Chất Cảnh:**
   - Cảnh kể chuyện / ngắm cảnh: Chuyển động vi mô tinh tế (nhân vật mỉm cười, chớp mắt, lật trang sách, nghiêng đầu, gió thổi tà áo và tóc bạc, nắng chiều lung linh).
   - Cảnh hành trình / dạo bước: Bước đi khoan thai chậm rãi, dắt thú cưng đi bộ nhịp nhàng, máy quay trượt êm.
   - Cảnh vũ đạo / thời trang: Chuyển động nhảy múa vui tươi, xoay người hoặc mở tay có kiểm soát để tà vải lượn sóng mềm mại mà không làm biến dạng cơ thể.
2. **Cấu trúc 1 dòng gọn rõ:**
   ```text
   [Chuyển động máy quay êm ái (Static frame / Slow push-in / Smooth tracking)] + [Hành động có kiểm soát của nhân vật] + [Vật lý tự nhiên của trang phục, gió, ánh sáng và vật thể xung quanh, zero morphing]
   ```
