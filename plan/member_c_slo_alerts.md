# Kế hoạch chi tiết: Member C - SLO & Alerts

Thành viên C chịu trách nhiệm định nghĩa các chỉ số SLO (Service Level Objectives), viết quy tắc cảnh báo (Alert Rules) và chuẩn bị tài liệu xử lý sự cố (Runbooks).

---

## 🛠️ Các File Cần Chỉnh Sửa / Tham Chiếu

1.  [config/slo.yaml](file:///c:/AI_2026/project/Lab13-Observability/config/slo.yaml) - Định nghĩa mục tiêu dịch vụ (SLO targets).
2.  [config/alert_rules.yaml](file:///c:/AI_2026/project/Lab13-Observability/config/alert_rules.yaml) - Danh sách các luật cảnh báo tự động.
3.  [docs/alerts.md](file:///c:/AI_2026/project/Lab13-Observability/docs/alerts.md) - Runbook hướng dẫn ứng cứu sự cố khi cảnh báo được kích hoạt.

---

## 📋 Nhiệm Vụ Chi Tiết Theo Từng Bước

### Bước 1: Xem xét và cấu hình chỉ số mục tiêu SLO
Chỉnh sửa [config/slo.yaml](file:///c:/AI_2026/project/Lab13-Observability/config/slo.yaml):
*   [ ] Đảm bảo các chỉ số mục tiêu (Objectives) và đích hướng tới (Target %) được thống nhất:
    *   `latency_p95_ms`: Đích trễ 95% số request phải dưới **3000ms** (hoặc giá trị nhóm thảo luận thống nhất).
    *   `error_rate_pct`: Tỷ lệ lỗi dưới **2%**.
    *   `daily_cost_usd`: Chi phí hoạt động hàng ngày dưới **$2.5**.
    *   `quality_score_avg`: Điểm chất lượng trung bình của câu trả lời trên **0.75**.

### Bước 2: Thiết lập Quy tắc Cảnh báo (Alert Rules)
Chỉnh sửa [config/alert_rules.yaml](file:///c:/AI_2026/project/Lab13-Observability/config/alert_rules.yaml):
*   [ ] Khai báo/Kiểm tra các rule cảnh báo chính:
    1.  `high_latency_p95`: Trễ P95 > 5000ms trong 30 phút.
    2.  `high_error_rate`: Tỷ lệ lỗi > 5% trong 5 phút.
    3.  `cost_budget_spike`: Chi phí hàng giờ tăng gấp 2 lần baseline trong 15 phút.
*   [ ] Đảm bảo trường `runbook` trỏ chính xác đến dòng tương ứng của file [docs/alerts.md](file:///c:/AI_2026/project/Lab13-Observability/docs/alerts.md) (ví dụ: `docs/alerts.md#1-high-latency-p95`).

### Bước 3: Viết tài liệu Hướng dẫn Ứng cứu (Runbooks)
Chỉnh sửa [docs/alerts.md](file:///c:/AI_2026/project/Lab13-Observability/docs/alerts.md):
*   [ ] Định nghĩa các bước kiểm tra đầu tiên (First checks) cho từng cảnh báo để các kỹ sư on-call dễ dàng thực hiện:
    *   Ví dụ: check incident toggle `rag_slow` có bị bật không, đối chiếu chi phí tokens input/output, xem log của cụm LLM hoặc RAG.
*   [ ] Đưa ra các biện pháp giảm thiểu sự cố tạm thời (Mitigation):
    *   Ví dụ: Cắt ngắn query đầu vào, hạ size prompt, chuyển hướng sang model rẻ hơn, hoặc tắt tool bị lỗi.

---

## 🔍 Hướng Dẫn Tự Kiểm Tra (Self-Validation)

*   [ ] Kiểm tra các liên kết (anchors `#...`) trong file [config/alert_rules.yaml](file:///c:/AI_2026/project/Lab13-Observability/config/alert_rules.yaml) xem có nhảy đúng đến các mục tiêu trong [docs/alerts.md](file:///c:/AI_2026/project/Lab13-Observability/docs/alerts.md) không.
*   [ ] Chụp lại ảnh màn hình cấu hình Alert rules và đưa vào báo cáo nhóm để làm minh chứng đạt điểm phần Alert & SLO.
