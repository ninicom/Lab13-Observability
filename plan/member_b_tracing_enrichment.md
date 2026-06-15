# Kế hoạch chi tiết: Member B - Tracing & Enrichment

Thành viên B chịu trách nhiệm theo dõi vết luồng xử lý (Distributed Tracing) qua Langfuse và làm giàu thông tin nhật ký (Log Enrichment).

---

## 🛠️ Các File Cần Chỉnh Sửa

1.  [app/main.py](file:///c:/AI_2026/project/Lab13-Observability/app/main.py) - Endpoint chính của FastAPI.
2.  [app/agent.py](file:///c:/AI_2026/project/Lab13-Observability/app/agent.py) - Logic xử lý của AI Agent.
3.  [.env](file:///c:/AI_2026/project/Lab13-Observability/.env) - File cấu hình môi trường.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Thiết lập cấu hình Langfuse (.env)
*   [ ] Đăng nhập vào trang quản lý Langfuse (hoặc local Langfuse instance).
*   [ ] Lấy các khoá API cần thiết và điền vào file `.env`:
    ```env
    LANGFUSE_PUBLIC_KEY=pk-lf-...
    LANGFUSE_SECRET_KEY=sk-lf-...
    LANGFUSE_HOST=https://cloud.langfuse.com # Hoặc URL host tự dựng
    ```

### Bước 2: Làm giàu Log (Log Enrichment)
Chỉnh sửa endpoint `/chat` trong [app/main.py](file:///c:/AI_2026/project/Lab13-Observability/app/main.py):
*   [ ] Tìm block `TODO: Enrich logs with request context`.
*   [ ] Sử dụng hàm `bind_contextvars(...)` để liên kết thông tin ngữ cảnh vào log của request hiện tại, bao gồm:
    *   `user_id_hash`: Sử dụng hàm `hash_user_id(body.user_id)` để băm mã định danh người dùng (tránh rò rỉ PII).
    *   `session_id`: `body.session_id`
    *   `feature`: `body.feature`
    *   `model`: dòng model đang chạy (đọc từ thuộc tính của agent hoặc body).
    *   `env`: Đọc từ biến môi trường `os.getenv("APP_ENV", "dev")`.

### Bước 3: Theo vết Agent qua Langfuse Tracing
Chỉnh sửa hàm `run(...)` trong [app/agent.py](file:///c:/AI_2026/project/Lab13-Observability/app/agent.py):
*   [ ] Đảm bảo hàm `run` có sử dụng decorator `@observe()`.
*   [ ] **Cập nhật Trace hiện tại (Trace Update):**
    *   Sử dụng `langfuse_context.update_current_trace` để truyền các tham số:
        *   `user_id`: Sử dụng `hash_user_id(user_id)`.
        *   `session_id`: `session_id`
        *   `tags`: Mảng chứa các thẻ: `["lab", feature, self.model]`.
*   [ ] **Cập nhật Quan sát (Observation / Span Details):**
    *   Sử dụng `langfuse_context.update_current_observation` để cập nhật:
        *   `metadata`: Chứa số lượng tài liệu đã truy vấn (`doc_count=len(docs)`) và tóm tắt câu hỏi (`query_preview=summarize_text(message)`).
        *   `usage_details`: Ghi nhận lượng token thực tế (`input=response.usage.input_tokens`, `output=response.usage.output_tokens`).

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

Sau khi hoàn thành:
1. Chạy server FastAPI và gửi tối thiểu **10 requests** thử nghiệm (bằng Postman hoặc chạy load test).
2. Kiểm tra trên dashboard Langfuse xem:
   *   Có đủ 10 traces xuất hiện không?
   *   Các Trace có hiển thị đầy đủ tags, user_id đã băm và metadata liên quan không?
3. Chạy lệnh:
   ```powershell
   python scripts/validate_logs.py
   ```
   *   **Mục tiêu đạt được:** `+ [PASSED] Log enrichment`
