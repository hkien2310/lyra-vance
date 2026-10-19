# BẢN RAW 2A (12/10 - Bản Ngắn Gọn 4 Khối: GLOBAL / CHARACTER / ENVIRONMENT / OBJECTS - Chó Khổng Lồ)

# STYLE: Lyra Vance

Thời trang là chính, siêu thực là phụ bổ trợ.

---

> [!IMPORTANT] Quy Tắc Chỉnh Sửa Style (Bắt Buộc)
> * **[Ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) (Lazy Senior Dev Mode):** Giữ file ngắn nhất có thể. Không tự ý đẻ thêm mục hoặc trường mới. Thêm quy tắc mới chỉ gạch đầu dòng vào đúng 4 khối (`GLOBAL`, `CHARACTER`, `ENVIRONMENT`, `OBJECTS`). Xóa từ thừa, chỉ giữ quy tắc thực thi được.
> * **[Humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md):** Giữ đúng ý gốc của tác giả, không tự bịa thêm thuật ngữ hoa mỹ, không văn phong lý thuyết AI.

---

## 1. GLOBAL (Thế Giới & Thẩm Mỹ Chung)

* **Cảm giác cốt lõi:** Sang trọng, thư giãn.
* **Màu sắc:** 
  * Chủ đạo: Xanh da trời.
  * Điểm nhấn: Cam.
  * Sắc thái chung: Lạnh, trầm.
* **Ánh sáng:** Ánh sáng mềm, giống như trình diễn runway.
* **Tính chất vật lý:** Tuyệt đối không sử dụng hiệu ứng lơ lửng.
* **Định vị siêu thực:** Siêu thực chỉ đưa vào chủ yếu ở **Trang phục** và **OBJECTS**, tiêu chí bắt buộc là phải tinh tế, tự nhiên, tuyệt đối không lố lăng dị hợm.

---

## 2. CHARACTER (Nhân Vật & Trang Phục)

### Nhân vật (Main)
* **Vóc dáng:** Người thật, dáng cao, gầy tựa người mẫu.
* **Khuôn mặt & Da:** Da trắng sứ, hồng hào, mặt đầy đặn không bị hóp.
* **Đối tượng:** Nam nữ, già trẻ đủ cả, ngoại hình đẹp.

### Trang phục (Main)
* **Trường phái nghệ thuật:** Kết hợp những trường phái nghệ thuật có thực, dễ gọi tên (ví dụ: retro 1970s). Có thể dùng siêu thực gộp 2 trường phái vào nhau theo tỉ lệ chính - phụ rõ ràng.
* **Phom dáng & Đường nét:** Cắt may không đối xứng, ưu tiên các đường cong uốn lượn mềm mại. Dáng dài (dài lố một chút cũng được). Tổng thể trang phục đẹp nhưng hơi "lố" nghệ thuật một chút để tạo độ cuốn hút. Không được trơn nhẵn thẳng tuột.
* **Biến tấu siêu thực:** Có thể dùng một chút siêu thực hoặc không để thay đổi một phần nhỏ kiểu dáng, nhưng giữ nguyên chất liệu vải thực tế. Xử lý tinh tế, không lố lăng làm mất chất thời trang.
* **Chất liệu:** Gắn liền với chủ đề video. Không thích sự bóng.
* **Màu sắc:** Không bao giờ đơn sắc.
* **Quy tắc cấm:** Nam không mặc váy.
* **Cách tiếp cận:** Chọn cảm xúc của trang phục trước cho toàn bộ video, sau đó mới biến tấu chi tiết.

### Phụ kiện
* Tối đa 1–2 phụ kiện chính để tạo sức hút và điểm nhấn, không nhồi nhét lên cơ thể.

---

## 3. ENVIRONMENT (Môi Trường)

Chọn 1 trong 2 dạng bối cảnh:
* **Thoáng:** Không gian rộng mở vô hạn.
* **Kín:** Bối cảnh kết thúc ngay phía sau nhân vật như một bức tường để tôn nhân vật lên. Không nhìn thấy góc phòng hay góc cạnh của phòng; phân định rõ nền và tường/sàn (không lộ đường viền góc cạnh) để tạo cảm giác không gian rộng.

---

## 4. OBJECTS (Vật Thể & Kiến Trúc Phụ)

* **Bắt buộc siêu thực:** Đã là vật thể hoặc sinh vật khác thì bắt buộc phải mang tính siêu thực, nhưng phải tinh tế và tự nhiên (Ví dụ: chó khổng lồ hiền hòa, nhà mọc mắt hài hòa của chính ngôi nhà; không chắp vá dị hợm, không lố lăng).
* **Số lượng:** Nếu có nhiều vật thể thì chỉ cần duy nhất 1 vật thể mang tính siêu thực là đủ.

---

## 5. WORKFLOW (Quy Trình Tạo Cảnh Mới)

Mỗi video cần xác định rõ 4 bước:
1. Chủ đề là gì?
2. Bối cảnh là gì (Thoáng hay Kín)?
3. Trang phục theo chủ đề như thế nào, gọi tên trường phái trang phục là gì?
4. Yếu tố siêu thực sẽ nằm ở đâu và giúp nâng tầm khung hình lên như thế nào?

---

## 6. CẤU TRÚC JSON PROMPT ĐẦU RA (Output Schema)

Mỗi prompt sinh ảnh/video xuất ra một JSON Object 4 khối tương ứng:

```json
{
  "id": "scene_01",
  "GLOBAL": {
    "palette": "Muted sky blue primary with subtle orange accents, cool and moody tone",
    "lighting": "Soft runway-like fashion show lighting"
  },
  "CHARACTER": {
    "model": "Real model, tall and slender, porcelain radiant skin, elegant full face",
    "costume": "Long flowing artistic attire inspired by 1970s retro, non-glossy textured fabric matching theme, non-monochrome, subtle surreal silhouette twist",
    "accessories": "1-2 focal statement accessories, non-cluttered"
  },
  "ENVIRONMENT": {
    "type": "open_infinite | closed_seamless_wall",
    "description": "<mô tả bối cảnh thoáng vô hạn hoặc phòng kín không thấy góc tường>"
  },
  "OBJECTS": {
    "surreal_object": "<tối đa 1 sinh vật hoặc kiến trúc phụ mang biến dị siêu thực tự nhiên>"
  }
}
```


---

# BẢN RAW 2B (12/10 - Bản Mở Rộng Không Gian & Vật Thể Siêu Thực)

# STYLE: Lyra Vance

Thời trang là chính, siêu thực là phụ bổ trợ.

---

> [!IMPORTANT] Quy Tắc Chỉnh Sửa Style (Bắt Buộc)
> * **[Ponytail](file:///Users/hoangkien/.gemini/config/skills/ponytail/SKILL.md) (Lazy Senior Dev Mode):** Giữ file ngắn nhất có thể. Xóa từ thừa, chỉ giữ quy tắc thực thi được.
> * **[Humanizer](file:///Users/hoangkien/Youtube/coslient-free/.agents/skills/humanizer/SKILL.md):** Giữ đúng ý gốc của tác giả, không tự bịa thêm thuật ngữ hoa mỹ, không văn phong lý thuyết AI.

---

## 1. GLOBAL (Thế Giới & Thẩm Mỹ Chung Toàn Kênh)

* **Cảm giác cốt lõi:** Sang trọng, thư giãn, điện ảnh Haute Couture.
* **Màu sắc thương hiệu (Bất biến toàn kênh):** 
  * Chủ đạo: Xanh phong hóa tự nhiên (chiếm 75–80% diện tích: xanh đá phiến slate, xanh chàm indigo, xanh khói dusty blue, xanh cerulean bạc màu). Tránh tuyệt đối màu xanh bệt trơn lì như đồ thể thao.
  * Điểm nhấn: Cam đất mộc (chiếm 10–15%: cam đất son terracotta, hổ phách amber, da thuộc cognac, đồng thau cổ antique brass).
  * Sắc thái chung: Lạnh, trầm, phong hóa tự nhiên (weathered earthy cinematic tones).
* **Ánh sáng:** 
  * Ánh sáng tự nhiên, mềm mại, chan hòa như sàn diễn runway ban ngày hoặc chiều tà điện ảnh.
  * Cho phép tài nguyên tự nhiên của vùng đất (khoáng thạch, thực vật...) phát ánh sáng ấm áp hữu cơ dịu nhẹ (*soft warm organic luminescence*).
  * **Tuyệt đối không dùng ánh sáng kịch tính hoặc sci-fi** (không spotlight gắt, không tia sáng neon, không sci-fi aura ma thuật kỹ xảo).
* **Tính chất vật lý:** Tuyệt đối không sử dụng hiệu ứng lơ lửng vô lý (100% grounded).
* **Tỉ lệ khung hình (Aspect Ratio):** Mặc định 16:9.
* **Định vị siêu thực:** Thể hiện rõ nét ở **Trang phục** và **OBJECTS (Địa chất tự nhiên & Đạo cụ nghi thức)**: đập vào mắt ngay sự bất thường độc đáo nhưng xử lý tinh tế, tự nhiên, không lố lăng dị hợm.

---

## 2. CHARACTER & TIÊU CHUẨN THIẾT KẾ COUTURE (Brand Wardrobe DNA)

### Nhân vật (Main)
* **Vóc dáng:** Người thật, dáng cao, thanh mảnh chuẩn người mẫu thời trang.
* **Khuôn mặt & Thần thái:** Đường nét khuôn mặt thanh tú góc cạnh, da sáng khỏe khoắn tự nhiên, thần thái đĩnh đạc cuốn hút, tự tại.

### Tiêu Chuẩn Trang Phục Toàn Kênh ("Oách & Cùng Một Loại")
* **Phong cách cốt lõi: Artisanal Nomadic Haute Couture** (Thời trang du mục thủ công vương giả — cảm hứng *Dune kết hợp Dries Van Noten / Etro / Zimmermann*). Toàn bộ trang phục tuân thủ **3 tiêu chuẩn**:

1. **Chiều sâu xúc giác & Hoa văn thủ công (Tactile Richness & Artisanal Weave):**
   * Tuyệt đối không dùng các mảng vải đơn sắc trơn phẳng lì hoặc bóng bẩy.
   * Ưu tiên bề mặt gấm thêu hoa văn cổ chìm (*tapestry, brocade, jacquard*), vải dệt thô mộc (*bouclé, slub, raw silk, heavyweight wool*), da thuộc phong hóa (*distressed leather*), và chi tiết viền thủ công (*frayed fringes, braided cords*).
2. **Cấu trúc lớp lang phóng khoáng & Độ rủ tự nhiên (Haute Layering & Flowing Drapes):**
   * Trang phục phối nhiều lớp dã hành thanh lịch: áo khoác ngoài (duster coats, cloaks, capes), lớp lót bay nhẹ, tà áo buông rủ tự nhiên tạo chiều sâu thị giác khi chuyển động.
   * Phom dáng tự do, phóng khoáng, thời thượng — không gò bó ép phải uốn lượn hay cong vòng cung.
3. **Phụ kiện mang tính nghi thức & hành trình (Ritual & Functional Talismans):**
   * Trang sức hộ mệnh thủ công (*talismans*), phụ kiện kim loại mờ hoặc da mộc, thiết kế tinh tế hài hòa với trang phục, phục vụ câu chuyện lữ hành, không rườm rà che lấp phom dáng.

* **Quy tắc cấm:** 
  * Nam không mặc váy. Không dùng chất liệu bóng (satin, nylon, nhựa). Không mặc đồ bình dân casual.
  * **Tuyệt đối cấm thiết kế hoạt hình / siêu nhân:** Không làm cầu vai nhọn dựng (sharp pagoda shoulders), không làm cổ áo nhọn dựng ngược cứng đơ, không dùng màu xanh - cam bệt chói chang như áo siêu nhân.
  * **Tuyệt đối không dùng chuyển động mạnh hay biên độ quá lớn (tránh làm dị tật chi thể và méo mó trang phục).** Tuyệt đối không bị nhòe chuyển động (zero motion blur) — hình ảnh phải sắc nét rõ nét từng chi tiết.

---

## 3. NGUYÊN TẮC HOẠT ĐỘNG CHUNG (The Shared Activity Principle)

> [!IMPORTANT]
> **Nhân vật không phải ma nơ canh đứng tạo dáng vô hồn.**
> Trong mỗi video, toàn bộ nhân vật luôn **tham gia vào một hoạt động hoặc nghi thức chung (The Shared Activity / Ritual)** gắn liền với bối cảnh và tài nguyên của vùng đất đó (được xác định cụ thể ở Bước 3 của mỗi video).

* **Bố cục đoàn người & Tương tác có hồn:**
  * Các nhân vật gắn kết với nhau và với vùng đất thông qua Hoạt động chung của video đó.
  * Hành động tự nhiên, có chủ đích, thể hiện sự tương tác trân trọng với môi trường hoặc đồng hành cùng nhau.
* **Biên độ chuyển động & Độ sắc nét (Subtle Movement & Crisp Focus):**
  * **Tuyệt đối không dùng chuyển động mạnh hay biên độ quá lớn:** Khi tạo ảnh, cấm các hành động chạy nhảy, sải bước quá rộng, vặn xoắn cơ thể, hoặc tà áo bay cuồng nộ. Chuyển động mạnh sẽ khiến AI làm dị tật tay chân, vỡ phom dáng Haute Couture và mất vẻ sang trọng.
  * **Chuyển động tinh tế, đĩnh đạc (Poised, controlled posture):** Tư thế đứng kiêu hãnh ngắm chân trời, dừng chân một nhịp khoan thai khi bước đi, thao tác nhẹ nhàng, gió thoảng lay nhẹ gấu áo.
  * **Không bị nhòe chuyển động:** Hình ảnh sắc nét, rõ ràng từng chi tiết (*zero motion blur / sharp editorial clarity*).

---

## 4. ENVIRONMENT & OBJECTS (Không Gian & Vật Thể)

### Môi trường (Environment)
* **Thoáng:** Không gian rộng mở vô hạn.
  * **Quy tắc xuyên suốt (Bắt buộc):** Luôn có một **Object siêu thực môi trường** hoặc **tính chất môi trường tương đối xuyên suốt** toàn video để định hình nhận diện thế giới.
* **Kín:** Bối cảnh kết thúc ngay phía sau nhân vật như một bức tường liền mạch để tôn vinh trang phục (không lộ góc phòng, phân định rõ nền và tường).

### Vật thể (Objects) — Phân định tương tác
Được chia làm 2 loại rõ rệt:
1. **OBJECT Môi trường (Environmental Object — Ưu tiên hàng đầu):**
   * Cấu tạo địa chất hoặc hệ sinh vật mang tính siêu thực thuộc về tự nhiên của vùng đất.
2. **OBJECT Nhân tạo / Đạo cụ hoạt động (Artificial / Ritual Objects):**
   * Vật dụng phục vụ trực tiếp cho **Hoạt động chung** của nhân vật trong video đó (chế tác thủ công, mộc mạc, tỷ lệ vừa vặn) hoặc công trình cự thạch đứng xa xa ở hậu cảnh.

> [!IMPORTANT] Quy Tắc Tương Tác Vật Lý & Cử Chỉ Tay
> * **Không chạm vào công trình cự thạch lớn:** Nhân vật tuyệt đối không leo trèo, không vịn hay thao tác vào các công trình kiến trúc cự thạch lớn ở hậu cảnh.
> * **Đạo cụ cầm tay phải linh hoạt, có chủ đích:** Tương tác tự nhiên với tài nguyên hoặc công cụ của hoạt động đó. Tuyệt đối không lặp lại một loại đạo cụ qua nhiều cảnh (tránh rập khuôn như ai cũng cầm gậy, ai cũng cầm túi).
> * **Chủ động định hình cử chỉ tay (Active Hand Posing):** Khi nhân vật không cầm đạo cụ, luôn mô tả rõ tư thế tay (buông tự nhiên hai bên hông chuẩn dáng runway, chắp sau lưng, đặt ở thắt lưng...) để AI không tự ý vẽ thêm vật thể thừa.

---

## 5. DIVERSITY (Quy Tắc Đa Dạng)

* **Kỹ thuật máy & Khung hình:**
  * Cỡ cảnh luân phiên: Toàn (Wide - bao quát không gian & địa chất), Trung (Medium - bắt trọn nhịp bước, tà áo và tư thế), Cận (Close-up - thần thái khuôn mặt, ánh mắt, chi tiết phụ kiện/trang sức talismans).
  * Góc máy: Ngang tầm mắt (Eye-level), Góc thấp (Low-angle tôn vóc dáng), Góc nghiêng 3/4, Góc nhìn từ sau lưng (Back-facing contemplative).
  * Bố cục: Đối xứng trung tâm, quy tắc 1/3, chừa khoảng trống âm lớn (negative space), hình ảnh phản chiếu trên mặt nước/mặt băng.
  * Chuyển động máy: Push-in chậm, tracking ngang hông, orbital drift vòng quanh nhân vật, slow-motion.
* **Nhân vật & Số lượng:**
  * Đa dạng độ tuổi & giới tính: Nam, nữ, người trẻ thanh tú, người cao niên tóc bạc quý phái.
  * Số lượng thay đổi linh hoạt: 1 người đơn độc, cặp đôi tương tác nhịp nhàng, hoặc nhóm nhỏ cùng thực hiện hoạt động.
* **Bắt buộc đa dạng trang phục:** Dù chung hoạt động và chung DNA bảng màu, mỗi cá nhân sở hữu phom dáng, đường cắt, lớp áo khoác và phụ kiện riêng biệt (tuyệt đối không mặc đồng phục).

---

## 6. WORKFLOW PHÂN TÍCH TỪNG VIDEO (Universal 5-Step Process)

Trước khi viết bất kỳ prompt nào cho một video mới, bắt buộc phân tích tuần tự 5 bước:

1. **Bối cảnh & Thế giới (The World):** Vùng đất này là gì? Địa hình, khí hậu, vật liệu địa chất siêu thực đặc trưng của môi trường.
2. **Họ là ai? (The Cast):** Chốt đúng 1 câu định danh bản thể của đoàn người trong thế giới này.
3. **HOẠT ĐỘNG CHUNG LÀ GÌ? (The Shared Activity / Ritual):**
   * Họ đến đây để làm gì? Nghi thức gì, công việc gì, sinh hoạt gì gắn kết họ với vùng đất?
   * *Hoạt động này là linh hồn quyết định cử chỉ của nhân vật và đạo cụ họ cầm trên tay.*
4. **Thiết kế trang phục phục vụ hoạt động đó:**
   * Chọn trường phái thiết kế và chất liệu xúc giác phù hợp với khí hậu vùng đất.
   * Thiết kế các phom dáng đa dạng riêng biệt cho từng nhân vật trên nền DNA thương hiệu (Xanh da trời 75–80% + Cam 10–15%, nhiều lớp, phụ kiện talismans).
5. **Hệ thống Vật thể & Đạo cụ:**
   * Vật thể siêu thực tự nhiên của môi trường.
   * Đạo cụ/công cụ phục vụ trực tiếp cho hoạt động chung (không chạm vào công trình cự thạch lớn).

---

## 7. CẤU TRÚC JSON PROMPT ĐẦU RA (Output Schema)

Mỗi prompt sinh ảnh/video xuất ra một JSON Object 4 khối tương ứng:

```json
{
  "id": "scene_01",
  "type": "generate_image",
  "GLOBAL": {
    "aspect_ratio": "16:9",
    "camera": "Wide shot, low angle, slow push-in, centered composition",
    "palette": "Muted weathered cerulean/slate primary (75-80%) with warm terracotta/amber accents (10-15%), cinematic earthy tone",
    "lighting": "Soft natural daylight or cinematic twilight, diffused ambient fill, allowing gentle warm organic luminescence from natural crystal specimens, zero harsh neon"
  },
  "CHARACTER": {
    "model": "Real model (diverse age/gender, individual fashion persona), tall and slender, sculpted high-fashion features, healthy natural skin tone",
    "action": "Diverse high-fashion posture, graceful stride, or sacred ritual engaged in the shared activity, captured with zero motion blur / crisp freeze-frame clarity, strictly no physical contact with large monuments",
    "costume": "Artisanal Nomadic Haute Couture ensemble: multi-layered textured fabrics (tapestry brocade, jacquard, or weathered leather), elegant flowing silhouette, weathered cerulean/slate primary with terracotta accents, strictly no cartoonish or superhero tropes",
    "accessories": "Storytelling accessories: layered talisman necklaces, functional leather pouches/satchels, artisanal headwear, non-cluttered"
  },
  "ENVIRONMENT": {
    "type": "open_infinite | closed_seamless_wall",
    "description": "<mô tả bối cảnh thoáng vô hạn hoặc phòng kín không thấy góc tường theo chủ đề video>"
  },
  "OBJECTS": {
    "environmental_object": "<vật thể địa chất hoặc sinh vật siêu thực thuộc về tự nhiên môi trường, xuyên suốt hoặc cục bộ>",
    "artificial_object": "<công cụ / đạo cụ phục vụ hoạt động của nhân vật, hoặc công trình cự thạch đứng độc lập ở hậu cảnh>"
  }
}
```

