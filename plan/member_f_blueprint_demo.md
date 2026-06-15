# Kế hoạch chi tiết: Member F - Blueprint & Demo

Thành viên F chịu trách nhiệm tổng hợp báo cáo (Blueprint Template), điều phối dữ liệu minh chứng của nhóm và dẫn dắt buổi Demo trực tiếp với giảng viên.

*(Lưu ý: Nếu nhóm 5 người, vai trò này sẽ do Member E thực hiện và chịu trách nhiệm chính)*

---

## 🛠️ Các File / Thư Mục Cần Làm Việc

1.  [docs/blueprint-template.md](file:///c:/AI_2026/project/Lab13-Observability/docs/blueprint-template.md) - Báo cáo nộp bài của nhóm.
2.  [docs/grading-evidence.md](file:///c:/AI_2026/project/Lab13-Observability/docs/grading-evidence.md) - Bằng chứng kỹ thuật của nhóm.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Quản lý và tổng hợp Báo cáo Blueprint
Cập nhật file [docs/blueprint-template.md](file:///c:/AI_2026/project/Lab13-Observability/docs/blueprint-template.md):
*   [ ] **Phần 1: Metadata nhóm:** Điền tên nhóm (`[GROUP_NAME]`), đường dẫn Git Repository (`[REPO_URL]`), và họ tên đầy đủ của từng thành viên tương ứng với các vai trò.
*   [ ] **Phần 2: Kết quả tự động:** Điền điểm số validate logs cuối cùng (`[VALIDATE_LOGS_FINAL_SCORE]`), tổng số trace đếm được trên Langfuse (`[TOTAL_TRACES_COUNT]`), và xác nhận số vụ rò rỉ dữ liệu PII (`[PII_LEAKS_FOUND]`).
*   [ ] **Phần 3: Minh chứng kỹ thuật:** Nhúng link ảnh chụp màn hình do Member E chuẩn bị vào báo cáo. Giải thích luồng Trace dạng thác nước (Trace Waterfall).
*   [ ] **Phần 5: Báo cáo cá nhân:** Yêu cầu mỗi thành viên viết phần mô tả công việc tự hoàn thành và đính kèm link commit/PR làm minh chứng đóng góp code.

### Bước 2: Viết báo cáo Phân tích Sự cố (Incident Response)
Sau khi nhóm hoàn thành việc gỡ lỗi sự cố ở Phase 4, Member F hoàn thiện Phần 4 trong báo cáo:
*   [ ] Xác định chính xác tên tình huống lỗi (`[SCENARIO_NAME]`).
*   [ ] Liệt kê các triệu chứng quan sát được qua Dashboard / Metrics (`[SYMPTOMS_OBSERVED]`).
*   [ ] Chỉ ra nguyên nhân gốc rễ cụ thể (`[ROOT_CAUSE_PROVED_BY]`) bằng cách dẫn chứng Trace ID bị lỗi hoặc dòng Log lỗi cụ thể.
*   [ ] Trình bày giải pháp sửa chữa tạm thời (`[FIX_ACTION]`) và đề xuất phương án phòng ngừa dài hạn (`[PREVENTIVE_MEASURE]`).

### Bước 3: Lên kịch bản Demo trực tiếp (Live Demo)
*   [ ] Thiết kế kịch bản Demo mượt mà diễn ra trong 5-10 phút.
*   [ ] Phân công luồng demo cho các thành viên trong nhóm trình bày phần việc của mình.
*   *Gợi ý kịch bản Demo:*
    1.  Khởi động ứng dụng, gửi request bình thường -> Cho giảng viên thấy Log JSON có đầy đủ context và correlation ID, Trace Langfuse hiển thị real-time.
    2.  Tiến hành kích hoạt incident (bằng script test của Member D) -> Dashboard hiện thị biểu đồ nhảy vọt (Latency/Error/Cost) -> Alerts nhảy trạng thái kích hoạt.
    3.  Dùng Runbook để hướng dẫn kiểm tra -> tìm đúng Trace ID lỗi -> Chỉ ra nguyên nhân -> Khắc phục sự cố.

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

*   [ ] Chuẩn bị và thảo luận trước các câu hỏi vấn đáp có thể gặp từ phía giảng viên khi demo (về regex, middleware, correlation ID, cách tính percentile p95, cách hoạt động của Langfuse).
*   [ ] Đảm bảo không thay đổi hoặc xoá bỏ các thẻ đánh dấu dạng `[TEMPLATE_TAGS]` trong file báo cáo để công cụ chấm điểm tự động có thể parse được kết quả.
