Quy tắc chỉnh sửa tài liệu này:
Không liệt kê lẻ tẻ sự vật sự kiện.
Không dùng phủ định.
Tuyệt đối không viết Use Case mà phải đúc kết thành Rule.

# 03 - Quy Tắc Sản Xuất Âm Nhạc & Kỹ Thuật Suno

> **Chức năng tài liệu (`File Role & Scope`):** Tài liệu quy định bộ kỹ thuật âm học thuần túy (cấu trúc nhạc hai lớp, âm thanh định danh độc bản, kỹ thuật nhả chữ và cú pháp Suno) **cấp độ toàn kênh**, trong khi để AI tự do quyết định thể loại và cảm xúc âm nhạc theo từng câu chuyện. Toàn bộ lời bài hát và prompt nhạc cụ thể của từng video được xuất riêng vào `projects/<STT>/nhac.md`.

## 1. Đầu Vào (`Input`)
- **Tài liệu bắt buộc đọc kèm:** [craft/01-dinh-vi-kenh.md](file:///Users/hoangkien/Youtube/lyra-vance/craft/01-dinh-vi-kenh.md) và `projects/<STT>/idea.md`.
- **Cơ chế vận hành:** AI tự do chọn thể loại, điệu thức, nhịp độ và sắc thái cảm xúc phù hợp nhất với `projects/<STT>/idea.md`, sau đó áp dụng bộ kỹ thuật âm học dưới đây để đảm bảo chất lượng bản phối trên Suno.

---

## 2. Quy Luật Kỹ Thuật Âm Học & Cú Pháp Suno (`Core Technical Rules`)

### 2.1. Kỹ Thuật Kết Cấu Nhạc Hai Lớp (`Two-Layer Texture Rule`)
- Thiết kế bản phối luôn vận hành đồng thời hai tầng âm thanh tách biệt để vừa có nhịp chuyển động vừa có chiều sâu không gian:
  - **Lớp giữ nhịp nền bên dưới (`Rhythmic Foundation Layer`):** Duy trì mạch chuyển động ổn định và rõ phách để nâng đỡ bước chân hoặc cử chỉ của nhân vật trên hình.
  - **Lớp giai điệu ngân dài bên trên (`Sustained Legato Layer`):** Sử dụng các nhạc cụ kéo dây, hơi hoặc âm thanh ngân liền hơi (`sustained legato`) cùng giọng hát lướt chậm ở tầng trên để tạo độ quyện và chiều sâu cảm xúc.

### 2.2. Kỹ Thuật Âm Thanh Định Danh Độc Bản (`Signature Sonic Identity Rule`)
- Chuyển hóa chất liệu vật lý hoặc chuyển động đặc trưng của bối cảnh trung tâm trong `projects/<STT>/idea.md` thành một âm sắc nhạc cụ định danh duy nhất xuyên suốt bản phối.
- Kết hợp nhạc cụ định danh này với một tuyến ngân giai điệu bằng giọng người (`Humming / Vocalise`) đóng vai trò đối đáp cuối câu hát hoặc dẫn dắt đoạn dạo, ăn khớp trực tiếp với các từ gợi âm thanh trong lời bài hát.

### 2.3. Kỹ Thuật Cú Pháp `Style Prompt` Bốn Mệnh Đề & `Exclude` (`Four-Clause Suno Syntax Rule`)
- Trình bày `Style Prompt` bằng tiếng Anh súc tích, tách thành bốn mệnh đề ngăn cách bằng dấu chấm phẩy (`;`) đúng chuẩn bộ đọc của Suno để khóa riêng vai trò của từng tầng âm thanh:
  - **Mệnh đề 1 (Thể loại, Nhịp đàn dẫn dắt, BPM & Điệu thức):** Đặt thể loại và sắc thái do AI chọn ngay đầu câu cùng nhạc cụ giữ nhịp, tốc độ BPM và điệu thức.
  - **Mệnh đề 2 (Kết cấu Hai Lớp & Nhạc cụ Độc bản):** Đặc tả rõ lớp nhạc cụ giữ nhịp bên dưới, lớp nhạc cụ ngân dài liền hơi bên trên và nhạc cụ định danh độc bản của bài.
  - **Mệnh đề 3 (Không gian âm học & Động lực học):** Đặc tả không gian thu âm ấm áp, đoạn nhạc dạo độc tấu (`instrumental solo`), độ nở ở điệp khúc cuối (`final chorus swell`) và điểm lắng rút nhạc cụ về tối giản ở cuối bài.
  - **Mệnh đề 4 (Màu giọng & Kỹ thuật nhả chữ):** Đặc tả màu giọng thu sát mic giàu hơi thở và lối hát nhả chữ liền hơi thong thả (`unhurried smooth legato delivery`).
- Thiết lập trường `Exclude` ghi ngắn gọn các tần số hoặc yếu tố âm thanh đối nghịch cần lọc khỏi bản phối, cách nhau bằng dấu phẩy.

### 2.4. Kỹ Thuật Viết Lời Neo Thực Thể & Âm Vận Mượt (`Grounded Lyric & Prosody Rule`)
- Neo các khái niệm cảm xúc và thời gian vào những thực thể, vật dụng hoặc góc không gian cụ thể kèm giới từ định vị; giữ ngôn từ tự nhiên như lời kể chuyện và đọng ý ở câu chốt khổ hoặc câu `Hook` trung tâm ngắn gọn của điệp khúc.
- Giữ mỗi dòng hát gọn vừa một hơi thở tự nhiên (trọn một mệnh đề hoặc chia hai vế cân xứng qua dấu phẩy), sử dụng cấu trúc câu song hành và ưu tiên các từ kết câu giàu nguyên âm mở hoặc phụ âm vang mềm để Suno phát âm tròn chữ; viết toàn bộ chữ số dưới dạng chữ cái tiếng Anh.
- Đặt thẻ điều phối `[...]` tiếng Anh ngắn gọn ở đầu mỗi phân đoạn (`Intro`, `Verse`, `Chorus`, `Instrumental Solo`, `Bridge`, `Outro`) ghi rõ tên đoạn, nhạc cụ dẫn dắt, giọng hát và sắc thái động lực học; đặt toàn bộ tiếng ngân và lời bè thực tế vào trong dấu ngoặc đơn `(...)`.

---

## 3. Đầu Ra (`Output`)
- **Đường dẫn lưu trữ:** `projects/<STT>/nhac.md`.
- **Template Output bắt buộc:**

```markdown
# SẢN XUẤT ÂM NHẠC — PROJECT <STT>

> **Chức năng tài liệu (`File Role & Scope`):** Hồ sơ thiết kế kỹ thuật âm nhạc hai lớp, âm thanh định danh độc bản, `Style Prompt`, `Exclude` và `Lyrics` hoàn chỉnh dành riêng cho **Project <STT>**, làm đầu vào nhịp điệu/ngôn từ cho `projects/<STT>/visual.md`.

## 1. Thiết Kế Kỹ Thuật Âm Học (`Technical Audio Blueprint`)
- **Thể loại & Nhịp độ tự chọn (`Selected Genre, BPM & Key`):** [Phương án thể loại, nhịp độ và điệu thức do AI tự chọn theo idea.md]
- **Kết cấu Nhạc Hai Lớp (`Two-Layer Architecture`):** [Lớp giữ nhịp nền bên dưới + Lớp giai điệu ngân dài bên trên]
- **Âm thanh Định danh Độc bản (`Signature Sonic Identity`):** [Nhạc cụ đặc trưng hóa thân từ chất liệu thế giới + Tuyến ngân giọng người đối đáp]

---

## 2. Cấu Hình Suno (`Suno Input`)

### Title
[Tên bài hát tiếng Anh ngắn gọn, đồng bộ với câu Hook]

### Style Prompt
```text
[Mệnh đề 1: Genre, Mood, Lead Groove Instrument, BPM, Key]; [Mệnh đề 2: Rhythmic foundation layer + Sustained legato layer + Signature sonic instrument]; [Mệnh đề 3: Acoustic space, instrumental solo, final chorus swell, stripped-back outro]; [Mệnh đề 4: Close-mic vocal tone, unhurried smooth legato delivery]
```

### Exclude
```text
[Các yếu tố âm thanh cần lọc bỏ, cách nhau bằng dấu phẩy]
```

### Lyrics
```text
[Toàn bộ lời bài hát kèm thẻ cấu trúc [Metatags] và phần ngân (Vocalise)]
```
```
