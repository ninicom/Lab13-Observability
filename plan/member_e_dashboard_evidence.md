# Kế hoạch chi tiết: Member E - Dashboard & Evidence

Thành viên E chịu trách nhiệm xây dựng bảng điều khiển giám sát (Dashboard) từ các metrics và thu thập đầy đủ các ảnh chụp minh chứng (Evidence Collection) để phục vụ cho việc chấm điểm.

*(Lưu ý: Nếu nhóm 5 người, vai trò này sẽ do Member D hoặc Member E thực hiện và chuẩn bị tài liệu báo cáo)*

---

## 🛠️ Các File / Thư Mục Cần Làm Việc

1.  [docs/dashboard-spec.md](file:///c:/AI_2026/project/Lab13-Observability/docs/dashboard-spec.md) - Đặc tả yêu cầu của Dashboard.
2.  [docs/grading-evidence.md](file:///c:/AI_2026/project/Lab13-Observability/docs/grading-evidence.md) - Hướng dẫn thu thập minh chứng chấm điểm.
3.  Endpoint `/metrics` của FastAPI app.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Nghiên cứu cấu trúc dữ liệu `/metrics`
*   [ ] Khởi chạy ứng dụng FastAPI và truy cập vào địa chỉ `http://localhost:8000/metrics`.
*   [ ] Đảm bảo dữ liệu trả về có đủ các trường: `traffic`, `latency_p50`, `latency_p95`, `latency_p99`, `avg_cost_usd`, `total_cost_usd`, `tokens_in_total`, `tokens_out_total`, `error_breakdown`, `quality_avg`.

### Bước 2: Thiết kế Dashboard (6 Panels)
Thiết lập Dashboard dựa trên công cụ nhóm chọn (Grafana, Datadog, Kibana, Prometheus hoặc công cụ custom dashboard) kết nối tới endpoint `/metrics`:
*   [ ] **Cấu hình 6 Panel bắt buộc:**
    1.  **Latency (P50/P95/P99):** Vẽ biểu đồ đường trễ xử lý (đơn vị: ms).
    2.  **Traffic:** Số lượng yêu cầu (Request count / QPS).
    3.  **Error Rate:** Tỷ lệ lỗi kèm phân tích loại lỗi (lỗi LLM, Schema, RAG).
    4.  **Cost over Time:** Biểu đồ chi phí tích luỹ hoặc trung bình.
    5.  **Tokens Usage:** Lượng Token đầu vào (In) và đầu ra (Out).
    6.  **Quality average:** Điểm chất lượng trung bình của hệ thống.
*   [ ] **Đáp ứng tiêu chuẩn chất lượng:**
    *   [ ] Khoảng thời gian mặc định (Time range) = 1 giờ.
    *   [ ] Tốc độ tự động làm mới (Auto refresh) mỗi 15-30 giây.
    *   [ ] Có đường hiển thị ngưỡng cảnh báo/SLO rõ ràng (ví dụ: vạch ngang màu đỏ ở mức trễ 3000ms).
    *   [ ] Các đơn vị đo lường (ms, USD, count) được ghi nhãn rõ ràng.

### Bước 3: Thu thập minh chứng (Grading Evidence)
Tiến hành chụp ảnh màn hình và cập nhật đường dẫn ảnh vào file [docs/grading-evidence.md](file:///c:/AI_2026/project/Lab13-Observability/docs/grading-evidence.md):
*   [ ] **Bắt buộc:**
    *   [ ] Danh sách trace Langfuse có ít nhất 10 traces hoạt động.
    *   [ ] Chi tiết 1 trace dạng Waterfall biểu thị rõ các Span (RAG vs LLM).
    *   [ ] Logs dạng JSON trong file `logs.jsonl` cho thấy trường `correlation_id` hợp lệ.
    *   [ ] Log dòng chứa thông tin nhạy cảm đã bị che ẩn bởi tiền tố `[REDACTED_...]`.
    *   [ ] Dashboard hoàn chỉnh với đủ 6 panels.
    *   [ ] Giao diện cấu hình quy tắc cảnh báo (Alert rules) kèm link runbook hoạt động.

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

*   [ ] Đảm bảo tất cả các tệp hình ảnh lưu trữ dưới định dạng phổ biến (PNG/JPG) trong thư mục chỉ định và liên kết hình ảnh trong markdown hoạt động bình thường (không bị lỗi đường dẫn).
