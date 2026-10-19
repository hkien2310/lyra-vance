# 05 — SẢN XUẤT VIDEO (Prompt Chuyển Động Veo3 / Kling)

> Dùng cho: Gemini Web hoặc Claude  
> Đầu vào: Upload file `image_prompts.txt` (hoặc dán danh sách toàn bộ prompt ảnh đã tạo ở bước 04)  
> Đầu ra: Xuất thẳng thành file kịch bản chuyển động video hoàn chỉnh (mỗi ảnh thành 1 shot 8s cho Veo3/Kling)

---

## 🎯 CÔNG THỨC CHUYỂN ĐỘNG VEO3 (Zero-Stutter One-Take)

Veo3 ghét nhất là chia mốc giây nhân tạo (`0-3s`, `3-6s` làm video bị giật/ngáo). Veo3 cần **một câu lệnh chuyển động liền mạch, một cú máy duy nhất (One-Take)**:

```
[Lệnh & Góc máy điện ảnh] + [Chuyển động cơ thể / Vũ đạo theo nhịp] + [Hiệu ứng vải vóc & Môi trường trôi dạt] + [cinematic slow motion, 24fps, highly coherent motion]
```

---

## 🤖 CÂU LỆNH KÍCH HOẠT (Dán vào chat kèm upload file prompt ảnh):

```
Bạn là đạo diễn hình ảnh và chuyên gia tạo prompt chuyển động video hàng đầu cho Veo3 / Kling.

Tôi đính kèm danh sách/file toàn bộ prompt ảnh đã tạo ở bước trước (mỗi prompt tương ứng một bức ảnh đã được gen). Hãy chuyển đổi toàn bộ danh sách này thành một BẢN KỊCH BẢN CHUYỂN ĐỘNG VIDEO VEO3 HOÀN CHỈNH:

NGUYÊN TẮC ĐẠO DIỄN BẮT BUỘC:

1. ĐA DẠNG HÓA TỘT CÙNG (KHÔNG GIỚI HẠN GÓC MÁY):
- Không dùng lại cùng một kiểu máy quay cho các cảnh cạnh nhau.
- Tự do khai thác toàn bộ kho tàng góc máy điện ảnh không giới hạn:
  + Từ các góc êm ái kinh điển: slow push-in, gentle pull-back, lateral tracking trượt ngang, 360 orbital drift lượn quanh chủ thể...
  + Đến các góc máy độc lạ, táo bạo: góc siêu thấp quét sát đất luồn qua chân/tà áo (through-the-legs low sweep), cú máy bổ nhào từ trên đỉnh đầu xuống (overhead dive), lướt sượt qua vai kiểu FPV, góc nghiêng chao đảo Dutch angle, hay lia máy cực nhanh whip pan để chuyển cảnh.

2. CHUYỂN ĐỘNG CƠ THỂ & VŨ ĐẠO SỐNG ĐỘNG:
- Dựa vào nội dung bức ảnh, chỉ đạo chuyển động cơ thể phù hợp nhịp nhạc (xoay người bung tà áo, uốn lượn sống lưng, dậm chân theo nhịp bass, hoặc cận cảnh ánh mắt liếc nhìn sắc lẹm).

3. ĐỒNG BỘ NĂNG LƯỢNG ĐỂ DỰNG MV:
- Ghi chú rõ cảnh nào là "Nhịp êm (Mellow)" để dựng đoạn dạo đầu/hát êm, cảnh nào là "Bùng nổ (Drop / Climax)" để editor ráp vào đoạn điệp khúc.

ĐỊNH DẠNG ĐẦU RA:
- Với mỗi shot:
  Shot [#] — [Cỡ cảnh & Góc máy] — [Ghi chú đạo diễn: dùng cho đoạn êm hay đoạn drop]
  Video Motion Prompt: `[Prompt tiếng Anh chuẩn công thức One-Take để ném vào Veo3]`
- Cuối cùng: 1 code block gom toàn bộ các Video Motion Prompts theo thứ tự để tôi lưu thẳng thành file video_prompts.txt.
```

---

## Ghi Chú Sử Dụng

1. **Chuẩn bị:** Mở file `image_prompts.txt` (chứa toàn bộ 5, 10 hoặc 15 prompt ảnh đã gen ở bước 04).
2. **Kích hoạt:** Mở Gemini/Claude $\rightarrow$ Dán câu lệnh trên $\rightarrow$ Đính kèm file hoặc dán danh sách prompt ảnh vào.
3. **Kết quả:** AI xuất ra toàn bộ kịch bản chuyển động video $\rightarrow$ Copy code block lưu thành `video_prompts.txt`.
4. **Render:** Mở Veo3/Kling $\rightarrow$ Kéo ảnh 1 vào + dán prompt video 1 $\rightarrow$ Bấm tạo $\rightarrow$ Lặp lại cho các ảnh tiếp theo.
5. **Thành phẩm:** Đủ bộ clip 8 giây đa dạng góc máy, editor chỉ việc ném vào CapCut/Premiere ghép vào file nhạc MP3 là xong MV!
