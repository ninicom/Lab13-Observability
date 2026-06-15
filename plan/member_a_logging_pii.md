# Kế hoạch chi tiết: Member A - Logging & PII

Thành viên A chịu trách nhiệm cấu trúc hóa nhật ký (Structured Logging) và bảo vệ dữ liệu nhạy cảm (PII Redaction) của hệ thống.

---

## 🛠️ Các File Cần Chỉnh Sửa

1.  [app/middleware.py](file:///c:/AI_2026/project/Lab13-Observability/app/middleware.py) - Middleware quản lý Correlation ID.
2.  [app/pii.py](file:///c:/AI_2026/project/Lab13-Observability/app/pii.py) - Bộ lọc thông tin nhạy cảm.
3.  [app/logging_config.py](file:///c:/AI_2026/project/Lab13-Observability/app/logging_config.py) - Cấu hình Structlog.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Middleware & Correlation ID
Chỉnh sửa class `CorrelationIdMiddleware` trong [app/middleware.py](file:///c:/AI_2026/project/Lab13-Observability/app/middleware.py):
*   [ ] **Giải phóng Contextvars:** Gọi `clear_contextvars()` ở đầu hàm `dispatch` để đảm bảo không rò rỉ dữ liệu log từ request trước sang request sau.
*   [ ] **Xử lý Request ID:**
    *   Kiểm tra xem request gửi lên có header `x-request-id` chưa.
    *   Nếu chưa có, sinh mới một chuỗi ngẫu nhiên có format: `req-<8-char-hex>` (ví dụ: `req-a3f29b1c`). Bạn có thể dùng `uuid.uuid4().hex[:8]`.
*   [ ] **Binding Context:** Gọi `bind_contextvars(correlation_id=correlation_id)` để structlog tự động chèn ID này vào mọi dòng log của request hiện tại.
*   [ ] **Cập nhật Response Headers:** Trả về `x-request-id` và tính toán thời gian xử lý (`x-response-time-ms`) đưa vào headers của response trả về cho client.

### Bước 2: Nhận diện PII nhạy cảm (PII Patterns)
Chỉnh sửa dictionary `PII_PATTERNS` trong [app/pii.py](file:///c:/AI_2026/project/Lab13-Observability/app/pii.py):
*   [ ] **Thêm regex cho Hộ chiếu (Passport):** Bổ sung mẫu regex để phát hiện số hộ chiếu phổ thông Việt Nam (ví dụ: bắt đầu bằng 1 chữ cái in hoa tiếp theo là 7 chữ số).
*   [ ] **Thêm regex cho Địa chỉ/Từ khóa Việt Nam:** Định nghĩa các từ khóa nhạy cảm thường xuất hiện trong địa chỉ (ví dụ: `Đường`, `Phường`, `Quận`, `Thành phố`, `Street`, `District`, `City`).

### Bước 3: Đăng ký PII Processor vào Structlog Pipeline
Chỉnh sửa hàm `configure_logging()` trong [app/logging_config.py](file:///c:/AI_2026/project/Lab13-Observability/app/logging_config.py):
*   [ ] Đăng ký hàm `scrub_event` vào danh sách `processors` của Structlog (ngay sau dòng `structlog.processors.TimeStamper(...)`) để tự động lọc sạch thông tin nhạy cảm trước khi ghi log ra file.

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

Sau khi hoàn thành code, chạy script kiểm tra:
```powershell
python scripts/validate_logs.py
```
*   **Mục tiêu đạt được:** 
    *   `+ [PASSED] Basic JSON schema`
    *   `+ [PASSED] Correlation ID propagation`
    *   `+ [PASSED] PII scrubbing`
