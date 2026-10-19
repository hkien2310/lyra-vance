# 03 - Quy trình sản xuất `image.txt` trực tiếp từ lưới 4 FPS

Tài liệu này quy định cách tạo `projects/XX/image.txt` trực tiếp từ bộ lưới ảnh `4 FPS` của video đối thủ mà không cần viết các file phân tích trung gian. Mọi quy tắc thẩm mỹ và an toàn nền tảng của kênh tuân theo [STYLE_lyra_vance_haute_surreal.md](file:///Users/hoangkien/Youtube/lyra-vance/STYLE_lyra_vance_haute_surreal.md).

## Bước 1: Tạo bộ lưới ảnh 4 FPS toàn video

Chạy công cụ trích xuất lưới ảnh liên hoàn 4 khung hình/giây (`4 FPS`, mỗi ô cách nhau `0.25s`) phủ toàn bộ thời lượng video đối thủ:

```bash
python3 common/analyze_motion.py projects/XX/doi-thu
```

Sau khi chạy xong, mở xem tuần tự toàn bộ các tấm lưới `grid_01` đến `grid_N` trong `projects/XX/doi-thu/grids/`.

## Bước 2: Viết Phần 1 của `image.txt` (Sao chép 1:1 từng cảnh gốc)

Quét tuần tự từ `grid_01` đến `grid_N` để xác định từng cảnh cắt (`Shot`) từ đầu đến cuối video (thường từ 35 đến 42 cảnh cho một video dài 3.5 phút). Với mỗi cảnh gốc, viết 1 dòng prompt trong `image.txt` theo quy tắc:

1. **Giữ nguyên bố cục tối giản của cảnh gốc (`1 Shot = 1 Bối cảnh nguyên bản`):**
   - Cảnh gốc có đúng loại đạo cụ, mặt sàn và ánh sáng nào thì chỉ mô tả đúng những yếu tố đó.
   - Không đem đạo cụ của cảnh khác (xe hơi, rèm lụa, bàn thờ, người đứng sau) nhồi thêm vào cảnh đang viết.
2. **Bám sát trang phục và trạng thái đèn của cảnh gốc:**
   - Mô tả đúng phom dáng, cổ áo, chất liệu vải thô/bóng, màu sắc lớp ngoài và lớp lót bên trong của nhân vật trong cảnh đó.
   - Ghi rõ trạng thái đạo cụ trong cảnh: đang ở trạng thái tĩnh tối (`dormant matte/metallic state`) hay đang bừng sáng qua khe lưới/gân đèn (`ignited warm-amber lattice/rib glow`).
3. **Áp dụng diện mạo nhân vật thích ứng và chuẩn an toàn của kênh:**
   - Bám sát thần thái, phong cách tạo hình, kiểu tóc và sắc thái cảm xúc của nhân vật trong cảnh gốc (mô tả thành người mẫu điện ảnh độc lập).
   - Ghi rõ giới tính (`female model` hoặc `male model`). Mẫu nam chỉ mặc áo choàng/trang phục nam phối quần ống rộng và bốt đế bằng, không mặc váy đầm hoặc giày cao gót.
   - Đảm bảo tính toàn vẹn cấu trúc cho mọi đạo cụ và phương tiện theo [STYLE_lyra_vance_haute_surreal.md](file:///Users/hoangkien/Youtube/lyra-vance/STYLE_lyra_vance_haute_surreal.md).

## Bước 3: Viết Phần 2 của `image.txt` (Mở rộng bằng hoán đổi chéo sạch)

Khi cần số lượng ảnh lớn hơn số cảnh gốc của video (ví dụ nâng từ 38 cảnh gốc lên 70 dòng), viết tiếp các dòng còn lại bằng 3 phép biến đổi đơn lẻ trên nền các cảnh đã có ở Phần 1. Tuyệt đối không cộng dồn đạo cụ của nhiều phòng vào chung một ảnh:

1. **Hoán đổi Trang phục và Phòng (`Outfit-to-Room Swap`):**
   - Lấy nguyên bộ trang phục (màu sắc, chất liệu, phụ kiện) của Cảnh A đặt vào nguyên căn phòng tối giản của Cảnh B.
2. **Đổi cự ly máy và trạng thái ánh sáng (`Framing & Luminance Shift`):**
   - Giữ nguyên căn phòng và đạo cụ của một cảnh gốc, đổi góc máy từ toàn cảnh (`wide full-body shot`) sang trung cận góc thấp (`medium-wide low-angle shot`), hoặc đổi đạo cụ từ trạng thái tắt đèn sang bật sáng ấm.
3. **Đổi đội hình hoặc giới tính nhân vật (`Subject & Pose Swap`):**
   - Giữ nguyên căn phòng tối giản của một cảnh gốc, đổi từ 1 mẫu nữ đứng sang 1 mẫu nam (mặc quần ống rộng) hoặc cặp đôi 2 nhân vật đứng/ngồi đối xứng theo thế luyện công.
