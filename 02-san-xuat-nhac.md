# 02 - Quy Tắc Sản Xuất Nhạc (Lyra Vance)

Tài liệu quy định quy trình vận hành Bước 2: chuyển hóa bản phân tích âm nhạc từ Bước 1 (`01-phan-tich-nhac.md`) hoặc ý tưởng chủ đề tự chọn thành gói sản xuất nhạc nhảy múa trên Suno/Udio. Kết quả được lưu vào `projects/XX/docs-nhac.md`.

---

## 1. Quy Trình Thu Thập Đầu Vào

Khi bắt đầu Bước 2 cho dự án `projects/XX`, tự động kiểm tra và đọc file `projects/XX/phan-tich-nhac.md` (từ Bước 1). Trường hợp bắt đầu mới không qua Bước 1, nhận đầu vào theo một trong hai hướng:
- **Hướng A:** File phân tích `projects/XX/phan-tich-nhac.md` từ Bước 1.
- **Hướng B:** Ý tưởng chủ đề hoặc nhịp điệu cốt lõi do người dùng cung cấp trực tiếp.

Sau khi đọc đầu vào, mặc định tạo **2 phương án bài hát** bám sát công thức âm học và tinh thần chủ đề từ Bước 1 để người dùng thoải mái chọn (trừ khi người dùng chỉ định số lượng khác).

---

## 2. Quy Tắc Tạo Gói Sản Xuất Suno/Udio

Xuất đầy đủ 3 thành phần dưới đây bằng tiếng Anh để đưa trực tiếp vào Suno/Udio:

### 1. Tên bài hát (Song Title)
Cụm từ tiếng Anh ngắn gọn (2 đến 5 từ), giàu nhịp điệu và thể hiện trực diện tinh thần bài hát.

### 2. Câu lệnh điều khiển âm thanh (Suno Style Prompt)
Một đoạn văn liền mạch (60 đến 90 từ) chỉ sử dụng các thuật ngữ âm học và sản xuất âm nhạc có tác dụng điều khiển trực tiếp bộ tạo âm thanh trên 4 trụ cột (kế thừa cơ chế âm học từ bài mẫu ở Bước 1):
- **Thể loại và Nhánh âm nhạc:** Nền tảng nhịp điệu thôi miên thúc đẩy chuyển động cơ thể và trình diễn thời trang (ví dụ: Hypnotic Indie Electronic, Dark Disco, Trip-Hop Groove, Melodic Deep House, Afro House, Avant-Pop Electronica...).
- **Lớp nhạc cụ và Tiết tấu:** Hệ thống trống/bộ gõ sắc nét, đường bass dẫn dắt rõ nhịp bước chân và lớp nhạc cụ/synth tạo không gian điện ảnh.
- **Cấu trúc Giọng hát:** Âm sắc giọng cuốn hút (tự sự lạnh lùng ma mị hoặc trầm ấm nội lực tùy mood bài), vị trí thu âm gần (close-mic presence) cùng các lớp bè nâng đỡ.
- **Không gian Mix và Thông số:** Độ dày dải trầm, độ sắc nét của nhịp gõ (transients), chỉ số BPM và giọng (Key) cụ thể.

### 3. Lời bài hát biểu diễn (Suno Performance Lyrics - Thời lượng ~4 phút)
Cấu trúc từ 32 đến 40 dòng lời kèm theo các thẻ chỉ dẫn cấu trúc và nhạc cụ nằm trong ngoặc vuông `[Section | chỉ dẫn tiết tấu và âm sắc]`, bao gồm các đoạn dạo nhịp điệu (`[Instrumental Groove]` / `[Percussion Break]` / `[Dance Drop]`) để phục vụ cảnh chuyển động và trình diễn trang phục.

**Quy tắc viết lời:**
1. Mỗi dòng là một câu hoàn chỉnh, trọn vẹn ý nghĩa.
2. Ưu tiên sử dụng các từ tiếng Anh đơn âm tiết hoặc hai âm tiết để giọng hát bám sát vào nhịp trống.
3. Xây dựng hình ảnh giàu tính thị giác, không gian siêu thực, chuyển động cơ thể và chiều sâu tâm lý theo chủ đề bài hát.
4. Duy trì xuyên suốt sắc thái cảm xúc cuốn hút, có hồn và thôi miên người nghe.
5. Thiết kế điệp khúc (Chorus) có câu hook ngắn gọn (1 đến 2 dòng), bắt tai và lặp lại gây nghiện ngay lập tức.

---

## 3. Tinh Chỉnh Sau Thử Nghiệm

Khi người dùng phản hồi kết quả nghe thử từ Suno, điều chỉnh chính xác các từ khóa âm học trong phần Style Prompt hoặc cấu trúc nhịp của lời bài hát, sau đó xuất lại trọn bộ gói kết quả hoàn chỉnh vào `projects/XX/docs-nhac.md`.
