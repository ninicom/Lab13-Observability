# Kế hoạch chi tiết: Member D - Load Test & Incidents

Thành viên D chịu trách nhiệm chạy thử tải (Load Testing), giả lập sự cố (Incident Injection) để đánh giá khả năng chịu đựng và giám sát của hệ thống.

*(Lưu ý: Nếu nhóm 5 người, Member D sẽ kiêm nhiệm cả phần Dashboard của Member E)*

---

## 🛠️ Các File / Thư Mục Cần Làm Việc

1.  [scripts/load_test.py](file:///c:/AI_2026/project/Lab13-Observability/scripts/load_test.py) - Script sinh traffic.
2.  [scripts/inject_incident.py](file:///c:/AI_2026/project/Lab13-Observability/scripts/inject_incident.py) - Script kích hoạt sự cố.
3.  [app/incidents.py](file:///c:/AI_2026/project/Lab13-Observability/app/incidents.py) - Logic điều khiển trạng thái sự cố.
4.  [data/sample_queries.jsonl](file:///c:/AI_2026/project/Lab13-Observability/data/sample_queries.jsonl) - Dữ liệu câu hỏi mẫu dùng để test.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Chuẩn bị dữ liệu và chạy Load Test
*   [ ] Xem lại file [data/sample_queries.jsonl](file:///c:/AI_2026/project/Lab13-Observability/data/sample_queries.jsonl) để hiểu cấu trúc dữ liệu gửi lên.
*   [ ] Chạy thử nghiệm load test cơ bản:
    ```powershell
    python scripts/load_test.py
    ```
*   [ ] Chạy thử nghiệm load test đồng thời (Concurrency):
    ```powershell
    python scripts/load_test.py --concurrency 5
    ```
*   [ ] Xác nhận rằng các yêu cầu được gửi thành công và sinh ra file logs [data/logs.jsonl](file:///c:/AI_2026/project/Lab13-Observability/data/logs.jsonl).

### Bước 2: Giả lập sự cố trực tiếp (Incident Injection)
Để kiểm tra tính nhạy bén của hệ thống cảnh báo và dashboard, tiến hành bật/tắt các sự cố:
*   [ ] **Bật sự cố RAG phản hồi chậm:**
    ```powershell
    python scripts/inject_incident.py --scenario rag_slow
    ```
    (Sau khi bật, chạy lại `load_test.py` để ghi nhận sự tăng vọt về Latency).
*   [ ] **Bật sự cố chi phí tăng vọt (Cost Spike):**
    ```powershell
    python scripts/inject_incident.py --scenario cost_spike
    ```
    (Chạy lại `load_test.py` để sinh ra các request tiêu tốn chi phí tokens).
*   [ ] **Tắt sự cố sau khi hoàn thành phân tích:**
    ```powershell
    python scripts/inject_incident.py --scenario rag_slow --disable
    ```
    hoặc gọi qua endpoint `/incidents/rag_slow/disable`.

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

*   [ ] Kiểm tra endpoint `/health` của API để xác thực trạng thái bật/tắt của các incident:
    ```json
    {
      "ok": true,
      "tracing_enabled": true,
      "incidents": {
        "rag_slow": true,
        "cost_spike": false
      }
    }
    ```
*   [ ] Đảm bảo phối hợp với Member E (hoặc tự làm nếu nhóm 5 người) chụp ảnh biểu đồ Latency/Cost thay đổi trước và sau khi kích hoạt incident làm bằng chứng cho phần Báo cáo.
