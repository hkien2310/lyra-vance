# BẢN RAW 1A (Sáng 16/10 - Bản Gốc Thời Trang Người Già)

# 03 - Quy Tắc Hình Ảnh & Sản Xuất Video (Lyra Vance)

Tài liệu quy định chuẩn thị giác và quy trình vận hành Bước 3: chuyển hóa bài nhạc từ Bước 2 (`02-san-xuat-nhac.md`) thành bộ 50 đến 80 kịch bản hình ảnh và chuyển động nhảy múa (`visual.md` và `prompts.json`).

---

## 1. Quy Tắc Thị Giác Cốt Lõi

1. **Nguyên lý Bức tranh sống (Sự liền mạch giữa Tường và Váy):** Hậu cảnh và trang phục hoạt động như một tác phẩm hội họa duy nhất. Đặt nhân vật trước một bức tường triển lãm có bề mặt chất liệu rõ nét (tranh sơn dầu trát bay dày, tường vữa phong hóa dát kim loại, tranh thủy mặc khổ lớn, phù điêu đá chạm khắc nguyên khối) hoặc sân khấu tối có luồng sáng điêu khắc. Thiết kế trang phục sao cho mảng màu, đai eo, dải chuyển sắc (ombré) hoặc cấu trúc bề mặt vải nối tiếp trực tiếp các đường nét, vệt cọ và tầng màu của bức tường phía sau.
2. **Kỹ thuật Haute Couture vi mô và Phom dáng tôn hình thể:** Xây dựng trang phục trên phom dáng thời trang cao cấp thanh thoát (thân trên ôm gọn hoặc xếp nếp tinh tế, định hình rõ vòng eo, chân váy hoặc áo choàng dài rủ mềm mại). Tạo điểm nhấn siêu thực bằng cấu trúc bề mặt vi mô có độ chuyển động cao: hàng ngàn nếp gấp nhỏ (micro-pleats), các lớp cánh lụa mỏng xếp chồng, tua rua sợi tơ tự nhiên, chuỗi đá thô/ngọc trai, hoặc hiệu ứng chuyển màu hội họa liền mạch trên vải.
3. **Bảng màu Hội họa và Điểm neo Xanh đặc trưng:** Sử dụng hệ màu khoáng vật và sơn dầu trầm sang trọng (trắng thạch cao, đen than, cam đất nung, vàng thổ, hồng tro, nâu đất), kết hợp sắc Xanh đặc trưng của kênh (`Slate-Blue`, `Prussian Blue`, `Cerulean` trầm, `Deep Indigo`) làm điểm kết nối xuyên suốt giữa bức tường nền và trang phục.
4. **Người mẫu cao tuổi quý phái và Vũ đạo đương đại:** Nhân vật là những người mẫu cao tuổi (65 đến 75 tuổi) có vóc dáng mảnh mai, thẳng lưng, mái tóc bạc trắng tự nhiên, gương mặt mộc thanh tú với nụ cười rạng rỡ bình yên, đi chân trần và thực hiện các chuyển động múa đương đại uyển chuyển trên mặt sàn đá phẳng.
5. **Ánh sáng Phòng trưng bày:** Sử dụng ánh sáng tự nhiên chiếu xiên dịu nhẹ hoặc luồng sáng sân khấu ấm áp lướt qua bề mặt tường và tà vải, làm nổi bật độ nổi 3D của chất liệu hội họa trên tường và độ rủ mềm của lụa.

---

## 2. Quy Trình Vận Hành (2 Giai Đoạn)

### Giai đoạn 1: Brainstorm Phân Khu Triển Lãm (Dừng chờ duyệt)
Đọc cấu trúc bài nhạc và chủ đề từ Bước 2 (`projects/XX/docs-nhac.md`). Đề xuất **4 đến 5 Phân Khu Triển Lãm (Exhibition Zones)** tương ứng với các trường đoạn âm nhạc (Intro/Verse, Chorus, Bridge, Drop, Outro). Ở mỗi phân khu, xác định rõ:
- Chất liệu bề mặt và bố cục của bức tường nghệ thuật phía sau.
- Phom dáng Haute Couture và kỹ thuật chất liệu vi mô trên trang phục nối liền với bức tường đó.
- Bảng màu hội họa chủ đạo và vị trí đặt sắc Xanh đặc trưng.

Trình bày ngắn gọn phương án 4 đến 5 phân khu và dừng lại chờ người dùng duyệt hoặc tinh chỉnh, đồng thời chốt tổng số lượng cảnh cần sinh (từ 50 đến 80 cảnh, chia theo từng phân khu).

### Giai đoạn 2: Sản Xuất Hàng Loạt (50 đến 80 Prompts)
Sau khi người dùng duyệt phương án Brainstorm, tiến hành sinh danh sách kịch bản chi tiết theo từng phân khu. Lưu bản mô tả tổng quan vào `projects/XX/visual.md` và xuất dữ liệu máy đọc vào `projects/XX/prompts.json` theo đúng cấu trúc JSON dưới đây.

---

## 3. Cấu Trúc Dữ Liệu Đầu Ra (`prompts.json`)

Các trường điều khiển tạo ảnh (`image_prompt`) và tạo chuyển động video (`video_motion_prompt`) được xuất bằng tiếng Anh chuẩn xác để đưa trực tiếp vào công cụ sinh ảnh/video:

```json
[
  {
    "scene_id": "zone1_01",
    "zone_theme": "<Tên phân khu triển lãm>",
    "aspect_ratio": "16:9",
    "camera": "Wide 16:9 full-body gallery framing, eye-level, f/2.8 shallow depth of field",
    "subject": "<Mô tả người mẫu cao tuổi (65-75 tuổi) dáng mảnh mai quý phái, tóc bạc tự nhiên, gương mặt thanh tú cười rạng rỡ, chân trần>",
    "dance_action": "<Chuyển động múa đương đại uyển chuyển làm bung mở cấu trúc vải>",
    "couture_attire": "<Phom đầm/trang phục Haute Couture tôn dáng + kỹ thuật bề mặt vi mô (micro-pleats, lớp cánh lụa, tua rua, chuyển sắc ombré) bằng chất liệu cao cấp>",
    "environment": "<Bức tường hội họa bề mặt nổi khổ lớn hoặc phù điêu nguyên khối trên mặt sàn phòng trưng bày phẳng mịn>",
    "canvas_continuity_and_blue": "<Sự liền mạch thị giác giữa vệt màu/kết cấu tường với trang phục + vị trí cài sắc Xanh đặc trưng>",
    "lighting": "Soft directional gallery daylight grazing across the textured wall and flowing silk fabric",
    "image_prompt": "<Đoạn văn tiếng Anh hoàn chỉnh ghép toàn bộ các trường trên để tạo ảnh tĩnh 16:9>",
    "video_motion_prompt": "<Câu lệnh tiếng Anh mô tả chuyển động One-Take: bước múa chân trần nhịp nhàng, chuyển động vật lý mềm mại của hàng ngàn lớp vải/sợi và góc máy vững chãi>"
  }
]
```


---

# BẢN RAW 1B (Trưa 16/10 - Bản Tinh Chỉnh 5 Quy Luật Người Già Haute Couture)

# 03 - Quy Tắc Hình Ảnh & Sản Xuất Video (Lyra Vance)

Tài liệu quy định khung nguyên lý **Surrealist Haute Couture** và quy trình vận hành Bước 3: chuyển hóa bài nhạc từ Bước 2 (`02-san-xuat-nhac.md`) thành bộ 50 đến 80 kịch bản hình ảnh và chuyển động nhảy múa (`visual.md` và `prompts.json`).

---

## 1. 5 Quy Luật Thiết Kế Trang Phục & Không Gian Cốt Lõi

1. **Quy luật Toàn Khối Đồng Nhất (*100% Total Garment Sculpture — Cấm "Đồ Thường Gắn Phụ Kiện"*):**
   - **Cấm tuyệt đối:** Không bao giờ mô tả nhân vật mặc một bộ quần áo bình thường (như áo sơ mi, áo vest trơn, quần tây trơn, đồ bó cơ bản) rồi mới "gắn thêm" tà vải, cánh hay dây ruy-băng vào vai/lưng. Cấm xé lẻ vải thành các dải dây rời hay tua rua vụn (`NO loose ribbons, NO tacked-on capes over plain suits, NO plain base clothing`).
   - **Bắt buộc:** **100% diện tích trang phục từ cổ, vai, thân áo, tay áo xuống đến tận ống quần/chân váy đều phải được tạo tác từ cùng một cấu trúc chất liệu siêu thực duy nhất.** Dù là đầm nữ hay trang phục quần của nam, toàn bộ bộ đồ là một tác phẩm điêu khắc vải nguyên khối (chỉ chiết gọn ở vòng eo hoặc cổ chân để tôn dáng thanh thoát, nhưng bề mặt chất liệu phải phủ kín 100% trang phục).
2. **Quy luật Bức Tranh Sống (*Living Canvas — Tường và Trang phục là Một Tác Phẩm*):**
   - Hậu cảnh không bao giờ là bức tường phòng trống trơn vô hồn. Phía sau nhân vật luôn là **một bức tường triển lãm nghệ thuật khổ lớn tràn khung hình** (bức tranh sơn dầu trát bay dày *impasto*, bức tường tranh thủy mặc/khoáng vật chia tầng ngang, bức phù điêu chạm nổi, hoặc tường kiến trúc có các ô cửa màu/khối hình học lớn).
   - **Sự tiếp nối trực tiếp:** Bảng màu, tầng chuyển sắc (*ombré*), dải màu ngang hoặc kết cấu bề mặt của bức tường phía sau **chảy trực tiếp vào toàn bộ thân áo và quần/váy của nhân vật** (như thể nhân vật vừa bước ra từ chính bức tranh tường đó).
3. **Quy luật Siêu Thực Duyên Dáng (*Poetic Surrealism & Hình Học Mềm*):**
   - **Giả kim Chất liệu & Đột biến Tỷ lệ:** Chuyển hóa các bề mặt hội họa và tự nhiên (nhát cọ sơn dầu dày, cánh hoa lụa xếp lớp, vân sóng nước, sợi nấm/san hô mềm, vảy xà cừ, gấm dập nổi) thành cấu trúc trang phục có **tỷ lệ phóng đại duyên dáng** (như vòng cổ xếp ly tròn đồng tâm đóng khung gương mặt, cầu vai/tay áo phồng điêu khắc, chân váy hoặc quần ống phồng xếp tầng sóng lượn).
   - **100% Đường cong mềm (*Zero Sharp Edges*):** Cấm các nếp gấp giấy nhọn cứng (origami) hay góc vuông thô kệch. Mọi đường xếp ly và tầng vải đều uốn cong mềm mại, uyển chuyển theo từng bước múa.
4. **Quy luật Bố Cục Chính Diện & Đường Chân Tường Nằm Ngang (*Front-Parallel Tableau*):**
   - Máy quay luôn đặt **chính diện 90 độ, ngang tầm mắt (*eye-level, straight-on front-parallel*)**, vuông góc tuyệt đối với bức tường nghệ thuật phía sau.
   - Giao tuyến giữa bức tường và mặt sàn luôn là **một đường thẳng nằm ngang tuyệt đối (*strictly horizontal floor-to-wall line*)** chạy ngang qua phần dưới khung hình, không bao giờ quay góc chéo làm xiên đường chân tường.
5. **Quy luật Ánh Sáng Tự Nhiên / Khuếch Tán Mềm & Nhân Vật Cao Tuổi Quý Phái:**
   - **Ánh sáng:** Chỉ sử dụng ánh sáng tự nhiên ban ngày (*soft natural daylight*) hoặc ánh sáng phòng trưng bày khuếch tán mềm (*soft diffused gallery light*). Cấm ánh sáng kịch tính sân khấu và cấm mọi hiệu ứng trang phục tự phát sáng.
   - **Nhân vật (65–75 tuổi — Solo Nữ, Solo Nam, Cặp đôi, Nhóm):** Dáng mảnh mai thanh thoát, tóc/râu bạc trắng tự nhiên, gương mặt rạng rỡ bình yên, đi chân trần (hoặc giày/kính nghệ thuật đồng bộ màu trang phục), luôn lộ rõ cổ, cổ tay và bàn chân.
   - **Bảng màu & Điểm neo Xanh:** Sử dụng bảng màu khoáng vật/sơn dầu sang trọng; cài cắm tinh tế sắc Xanh đặc trưng (`Slate-Blue`, `Prussian Blue`, `Cobalt`, `Cerulean` trầm, `Deep Indigo`) kết nối giữa bức tường nghệ thuật và trang phục.

---

## 2. Quy Trình Vận Hành (2 Giai Đoạn)

### Giai đoạn 1: Brainstorm Phân Khu Triển Lãm (Dừng chờ duyệt)
Đọc cấu trúc bài nhạc từ Bước 2 (`projects/XX/docs-nhac.md`). Đề xuất **4 đến 5 Phân Khu Triển Lãm (Exhibition Zones)** tương ứng với các trường đoạn âm nhạc. Ở mỗi phân khu, xác định rõ:
- **Bức tường Nghệ thuật Chính diện:** Mô tả rõ tác phẩm hội họa/phù điêu/kiến trúc trên bức tường phẳng phía sau (tránh tường trống).
- **Thiết kế Trang phục Toàn khối (100% Sculptural Garment):** Cách chất liệu và mảng màu của bức tường hóa thành **toàn bộ trang phục** (từ thân áo, cổ/vai đến quần/váy — không dùng đồ trơn gắn phụ kiện) cho Nam, Nữ, Cặp đôi hoặc Nhóm.
- **Bảng màu & Điểm neo Xanh** dưới ánh sáng tự nhiên/khuếch tán mềm.

Trình bày phương án và **dừng lại chờ người dùng duyệt** trước khi sang Giai đoạn 2.

### Giai đoạn 2: Sản Xuất Hàng Loạt (50 đến 80 Prompts)
Sau khi người dùng duyệt, xuất bản mô tả tổng quan vào `projects/XX/visual.md` và xuất dữ liệu máy đọc vào `projects/XX/prompts.json`:

```json
[
  {
    "scene_id": "zone1_01",
    "zone": "Zone 1 - <Tên phân khu>",
    "cast": "<Solo Female | Solo Male | Duo | Ensemble>",
    "concept_vi": "<1 câu tóm tắt: Nhân vật + Trang phục điêu khắc toàn khối (100% chất liệu siêu thực mềm mại từ áo đến quần/váy, không đồ thường gắn phụ kiện) nối liền với Bức tường nghệ thuật chính diện>",
    "image_prompt": "<Full English prompt: [Strictly straight-on front-parallel 16:9 full-body gallery framing, eye-level, perpendicular to the flat background wall with a clean level horizontal floor-to-wall line, f/2.8], [65-75yo slender graceful model(s), natural silver hair, radiant serene smile, barefoot, fluid contemporary dance pose], [100% full-body sculptural Haute Couture garment where the ENTIRE outfit (bodice, sleeves, and flowing wide-leg trousers or skirt) is crafted from a single unified surreal textile/painterly structure with soft biomorphic curves and zero plain everyday clothing or tacked-on ribbons], [Monumental front-facing painted mural wall, bas-relief, or colored architectural doorway wall whose colors, horizontal bands, and textures flow directly into the garment], [Soft natural daylight or even diffused gallery lighting], photorealistic editorial art film, 8k>",
    "video_motion_prompt": "<One-Take English motion prompt: [Locked straight-on front-parallel camera keeping the horizontal floor-wall line completely level] + [Controlled fluid contemporary dance movement] + [The entire sculptural Haute Couture garment undulating and billowing as one cohesive, weighty fabric structure in harmony with the painted wall behind], soft natural lighting, zero morphing>"
  }
]
```

