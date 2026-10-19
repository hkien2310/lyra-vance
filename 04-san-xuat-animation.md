# 04 - Quy trình sản xuất `video.txt` trực tiếp từ lưới 4 FPS

Tài liệu này quy định cách tạo danh sách prompt chuyển động (`projects/XX/video.txt`) bằng cách đọc trực tiếp quỹ đạo cử động từ bộ lưới ảnh `4 FPS` (`projects/XX/doi-thu/grids/grid_*.jpg`) mà không cần qua file phân tích trung gian.

## 1. Tinh thần cốt lõi của chuyển động

Mọi chuyển động phải toát lên vẻ sang trọng, lịch lãm, điềm tĩnh và uyển chuyển liên tục như bậc thầy luyện nội công, khí công kết hợp vũ đạo cổ điển và sải bước thời trang cao cấp (`noble, aristocratic, fluid internal martial-qigong mastery and flowing classical grace`).

Các trường phái hạt nhân sử dụng trong prompt:
1. **Xoay thiền định và Bát Quái xoay trục (`Meditative Sufi Whirling & Baguazhang Circle-Spin`):** Xoay tròn 360 độ tĩnh tại, trục lưng thẳng, lực ly tâm nâng tà áo và lớp lót trong bung thành đĩa tròn đồng tâm.
2. **Thái Cực Quyền Võ Đang và Kình lực rút tơ (`Wudang Taijiquan, Tai Chi Cloud Hands & Qigong Silk-Reeling`):** Chuyển động dẫn khí mềm mại từ đan điền lên bả vai, vẽ các vòng tròn âm dương liên hoàn không dứt.
3. **Múa Thủy Tụ và Thân pháp cổ điển (`Imperial Shuixiu Water-Sleeve & Dunhuang Shen-Yun Classical Dance`):** Phóng, thu và lượn sóng hai ống tay áo rộng mềm như nước chảy mây trôi.
4. **Múa đương đại phương Đông (`Cloud-Gate Oriental Contemporary Flow`):** Hạ trọng tâm trầm mặc, uốn sóng cột sống mượt mà và nghiêng mở thân trên đầy kiểm soát.
5. **Sải bước sàn diễn quý tộc và Tĩnh tọa khí công (`Aristocratic Haute Couture Runway Glide & Meditative Seated Qigong`):** Bước đi khoan thai thẳng lưng làm tà áo dài lướt sóng phía sau, hoặc ngồi tĩnh tọa điều tức và xoay nhẹ cổ tay.

Cấm các từ khóa gây giật cục, hỗn loạn hoặc phá hoại cấu trúc (`hip-hop popping`, `street house jumping`, `frantic waacking`, `violent whipping`, `chaotic splashing`, `submerged`, `broken`, `damaged`).

## 2. Cách đọc Grid 4 FPS để viết `video.txt`

Nhìn chuỗi ô ảnh liên tiếp của từng cảnh trên `grid_01` đến `grid_N` để lấy đúng 3 thông tin thực tế:
1. **Cử động của nhân vật:** Nhân vật đứng xoay tròn, múa tay tại chỗ, bước đi ngang khung hình, ngồi tĩnh tọa hay phối hợp 2 người đối xứng.
2. **Biến đổi của đạo cụ và hậu cảnh:** Đèn lồng/trụ đồng giữ nguyên ánh sáng hay chuyển từ trạng thái tắt sang bừng sáng giữa cảnh (`dormant-to-ignited transition`); xe hơi đỗ tĩnh hay lướt chậm ngang qua hậu cảnh.
3. **Quỹ đạo máy quay:** Máy đứng tĩnh đối xứng (`static symmetrical wide frame`), đẩy chậm vào trung cảnh (`slow meditative dolly push-in`), lùi chậm mở rộng không gian (`slow dolly pull-out`), hay trượt ngang song song (`smooth lateral tracking glide`).

## 3. Quy tắc viết câu prompt trong `video.txt`

1. **Ẩn chi tiết màu sắc và thiết kế trang phục cụ thể (`Image-Agnostic Reference`):**
   - Dùng danh từ khái quát (`the subject` hoặc `both subjects`, `their monumental oversized coat and voluminous sleeves`, `the heavy floor-length train`, `the colossal background monoliths`, `the warm architectural lanterns`) để mỗi dòng trong `video.txt` ghép khớp với mọi ảnh tĩnh trong `image.txt`.
2. **Cấu trúc chuỗi 3 pha liên hoàn (`3-Phase Flowing Progression`):**
   - **Pha 1 (Khởi thế tụ khí):** Mở rộng hai vai, cuộn cổ tay dẫn khí từ đan điền với phong thái ung dung.
   - **Pha 2 (Triển khai thân pháp):** Thực hiện chuỗi vòng tròn Thái Cực Vân Thủ, phóng tay áo Thủy Tụ, hoặc xoay thân 360 độ êm ái.
   - **Pha 3 (Mở rộng khí trường và quán tính vải):** Mở hết biên độ cánh tay và tà áo tạo sóng lụa đồng tâm, đồng bộ với hiệu ứng ánh sáng ấm hoặc chuyển động êm của hậu cảnh.
3. **Công thức 1 dòng (`Single-Line Format`):**
   ```text
   [Quỹ đạo máy quay] + [Trường phái luyện công/vũ đạo + Chuỗi 3 pha liên hoàn] + [Vật lý tà áo và ống tay áo] + [Chuyển động ánh sáng/đạo cụ hậu cảnh an toàn]
   ```
