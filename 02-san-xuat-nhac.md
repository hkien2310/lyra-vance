# 02 - Quy Tắc Sản Xuất Nhạc (Lyra Vance)

Tài liệu quy định Bước 2: chuyển hóa Phần A (Âm thanh & SEO) từ `projects/XX/phan-tich.md` thành gói sản xuất nhạc trên Suno/Udio. Người dùng dùng gói này để tạo nhạc và chốt bản nhạc ưng ý lưu vào `projects/XX/docs-nhac.md`.

---

## 1. Quy Trình Thực Thi

1. Đọc Phần A trong `projects/XX/phan-tich.md` (hoặc nhận yêu cầu chủ đề trực tiếp từ người dùng).
2. Đề xuất **2 phương án bài hát** bám sát công thức âm học (`BPM`, `Key`, nhạc cụ, giọng hát và mood cảm xúc) của bài mẫu để người dùng đem vào Suno/Udio test thử.
3. Khi người dùng chọn và chốt bản nhạc (hoặc yêu cầu tinh chỉnh lời/style), cập nhật bản chốt cuối cùng vào `projects/XX/docs-nhac.md`.

---

## 2. Cấu Trúc Gói Sản Xuất Suno/Udio

Xuất đầy đủ 3 thành phần bằng tiếng Anh:

### 1. Tên bài hát (`Song Title`)
Cụm từ tiếng Anh ngắn gọn (2 đến 5 từ), giàu cảm xúc và đúng tinh thần video.

### 2. Câu lệnh điều khiển âm thanh (`Suno Style Prompt`)
Đoạn văn liền mạch (60 đến 90 từ) sử dụng các thuật ngữ âm học cụ thể trên 4 trụ cột kế thừa từ bài mẫu:
- **Thể loại & Nhánh âm nhạc:** Đúng dòng nhạc của video mẫu (Soulful Pop, Nostalgic Folk-Pop, Gentle Cinematic Indie, Ageless Groove, Deep Melodic House, Vintage Ballroom...).
- **Lớp nhạc cụ & Tiết tấu:** Nhạc cụ chủ đạo, tiếng trống/bộ gõ và đường bass rõ nét.
- **Giọng hát (`Vocals`):** Giới tính, màu giọng (ấm áp từng trải, sâu lắng tự sự hoặc rạng rỡ nội lực), vị trí thu âm gần (`close-mic presence`).
- **Không gian Mix & Thông số:** Độ ấm bản mix, độ rộng stereo, chỉ số `BPM` và `Key` cụ thể.

### 3. Lời bài hát biểu diễn (`Suno Performance Lyrics`)
Cấu trúc từ 32 đến 40 dòng lời kèm các thẻ chỉ dẫn `[Intro]`, `[Verse]`, `[Chorus]`, `[Instrumental Break]`, `[Bridge]`, `[Outro]`:
1. Mỗi dòng là một câu hoàn chỉnh, từ ngữ tự nhiên, dễ hát bám nhịp.
2. Giàu hình ảnh thị giác và cảm xúc đồng điệu với chủ đề video.
3. Điệp khúc (`Chorus`) có câu Hook ngắn gọn, dễ nhớ và chạm cảm xúc ngay lập tức.
