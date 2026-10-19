# 04 — SẢN XUẤT HÌNH ẢNH (Meta AI / Midjourney / Flux)

> Dùng cho: Tiếp tục ngay trong đoạn chat vừa phân tích ảnh trên Meta AI.  
> Cách dùng: Gõ câu lệnh dưới đây để Meta AI vẽ từng đợt 5 ảnh + gom prompt để lưu file.

---

## 1. Câu lệnh đợt 1 (Dán tiếp vào chat sau khi phân tích):

```
Dựa trên những gì vừa phân tích ở trên, hãy tạo bộ đúng 5 concept ảnh siêu thực mới (tỉ lệ 16:9) để dựng MV. Vẽ trực tiếp ảnh cho từng concept trong chat:

1. NGUYÊN TẮC CỨNG (GIỮ NGUYÊN XUYÊN SUỐT):
- [Style & Color]: Kế thừa trọn vẹn bảng màu, phong cách siêu thực, texture chất liệu từ phân tích.
- [Subject DNA]: Người đẹp có hồn, vóc dáng thanh thoát cao ráo, thần thái cuốn hút (tuyệt đối không vẽ người vô hồn như ma nơ canh).
- [Lighting & Mood]: Giữ đúng kiểu ánh sáng đặc trưng và không khí ma mị, thôi miên.
- [Visual Anchor (Điểm neo)]: Tự đề xuất màu sắc hoặc chi tiết đặc trưng xuyên suốt theo vibe bài hát (để mở, không ép cứng).
- [Technical]: photorealistic, 8k texture, --ar 16:9.

2. NGUYÊN TẮC ĐỘNG (BIẾN THIÊN ĐỂ EDIT DỰNG VIDEO KHÔNG NHÀM CHÁN):
- Phân bổ 5 cảnh đa dạng (chủ yếu là Toàn và Trung để nhảy, xen kẽ Cận):
  + 1 cảnh Toàn (Wide): không gian rộng, bối cảnh siêu thực bao quát
  + 3 cảnh Trung chuyển động (Medium): vũ đạo, xoay người, tà áo bay, chuyển động sống động
  + 1 cảnh Cận (Close-up) hoặc Siêu cận: đặc tả ánh mắt thần thái, chi tiết mặt nạ/trang sức độc lạ
- [Specific action]: Mỗi cảnh một hành động cụ thể, tương tác với không gian/đạo cụ, không đứng đơ một chỗ.
- [Camera movement]: Luôn có hint chuyển động máy (slow pan, orbital drift, push in, slow-motion...) để làm tiền đề đưa ảnh vào Veo3/Kling tạo clip 8 giây.

3. ĐỊNH DẠNG TRẢ VỀ:
- Với mỗi cảnh:
  + Mô tả ý tưởng & yếu tố siêu thực bằng tiếng Việt: [Cỡ cảnh + Góc máy] — [Hành động]
  + VẼ TRỰC TIẾP ẢNH TRONG CHAT
  + In dòng Prompt tiếng Anh ngay dưới ảnh theo công thức:
    `[Shot size + Angle], [Subject + appearance + action], [Setting + surreal elements], [Lighting & Mood], [Style & Color], [Camera movement hint], [Technical: photorealistic, 8k, --ar 16:9]`
- Cuối cùng: 1 code block gom toàn bộ 5 prompt tiếng Anh để copy lưu vào file image_prompts.txt.
```

---

## 2. Câu lệnh gen thêm các đợt tiếp theo (Đợt 2, Đợt 3...):

Khi cần thêm ảnh để dựng bài dài (10–15 ảnh), chỉ cần gõ lệnh ngắn:

```
Tiếp tục tạo 5 ảnh tiếp theo thật đa dạng (tuân thủ nghiêm ngặt toàn bộ rules cũ ở trên, đổi mới hoàn toàn góc máy, hành động và concept, tuyệt đối không lặp lại các ảnh đã tạo). Cuối phản hồi nhớ gom 5 prompt tiếng Anh vào 1 code block để tôi copy lưu file.
```

---

## Ghi Chú Sử Dụng

1. **Meta AI vẽ trực tiếp 5 ảnh** mỗi lần (giữ 5 ảnh để không bị lỗi timeout).
2. **LƯU TOÀN BỘ PROMPT VÀO 1 FILE:** Mỗi lần gen 5 ảnh xong, copy code block prompt dán gom vào 1 file text (ví dụ `image_prompts.txt`). File này sẽ được ném thẳng sang bước `05` để AI tự sinh kịch bản video.
