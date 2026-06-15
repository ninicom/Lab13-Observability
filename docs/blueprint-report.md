# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Đặng Tiến Quyền - 2A202600896
- [REPO_URL]: https://github.com/ninicom/Lab13-Observability
- [MEMBERS]:
  - Member A: Đặng Tiến Quyền (MSV: 2A202600896) | Role: Logging & PII
  - Member B: Đặng Tiến Quyền (MSV: 2A202600896) | Role: Tracing & Enrichment
  - Member C: Đặng Tiến Quyền (MSV: 2A202600896) | Role: SLO & Alerts
  - Member D: Đặng Tiến Quyền (MSV: 2A202600896) | Role: Load Test & Dashboard
  - Member E: Đặng Tiến Quyền (MSV: 2A202600896) | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 20
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: assets/correlation_id.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: assets/pii_redaction.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: assets/trace_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: One interesting trace shows the `run` method span encompassing both RAG retrieval and LLM generation. When `rag_slow` is enabled, the retrieve span takes exactly 2500ms, proving that the latency bottleneck lies in the retrieval tool, not the LLM.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: assets/dashboard_6_panels.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 2651ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.0369 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: assets/alert_rules.png
- [SAMPLE_RUNBOOK_LINK]: alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: P95 latency increased dramatically from ~150ms to 2651ms on the server-side. Under concurrent request load (concurrency = 5), client-side round-trip latencies spiked up to 13280ms due to queuing bottlenecks in the application server.
- [ROOT_CAUSE_PROVED_BY]: The Langfuse trace waterfall showed that the `retrieve` helper function span took 2500ms, while the LLM generation span remained constant at ~150ms. The active incident state was verified via the `/health` endpoint as `"rag_slow": true`.
- [FIX_ACTION]: Disabled the active scenario by running `python scripts/inject_incident.py --scenario rag_slow --disable` or making a POST request to `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Implement a query-timeout limit (e.g., 1000ms) on vector database retrieval, and fallback to a default prompt or cache when the retrieval latency budget is breached.

---

## 5. Individual Contributions & Evidence

### [MEMBER_A_NAME]: Đặng Tiến Quyền
- [TASKS_COMPLETED]: Completed CorrelationIdMiddleware, added Passport and Address VN regex patterns, and registered PII scrub processor.
- [EVIDENCE_LINK]: [app/middleware.py](../app/middleware.py), [app/pii.py](../app/pii.py)

### [MEMBER_B_NAME]: Đặng Tiến Quyền
- [TASKS_COMPLETED]: Integrated Langfuse SDK v3 observe decorator, created LangfuseContextWrapper to map trace and observation calls dynamically, and enriched API log context.
- [EVIDENCE_LINK]: [app/tracing.py](../app/tracing.py), [app/agent.py](../app/agent.py), [app/main.py](../app/main.py)

### [MEMBER_C_NAME]: Đặng Tiến Quyền
- [TASKS_COMPLETED]: Configured SLO targets (Latency, Error Rate, cost budget), verified alert rules condition match, and completed incident response runbooks.
- [EVIDENCE_LINK]: [config/alert_rules.yaml](../config/alert_rules.yaml), [docs/alerts.md](alerts.md)

### [MEMBER_D_NAME]: Đặng Tiến Quyền
- [TASKS_COMPLETED]: Conducted load test with concurrency 5, injected incidents (rag_slow, tool_fail, cost_spike) to simulate failures, and verified metric collections.
- [EVIDENCE_LINK]: [scripts/load_test.py](../scripts/load_test.py), [scripts/inject_incident.py](../scripts/inject_incident.py)

### [MEMBER_E_NAME]: Đặng Tiến Quyền
- [TASKS_COMPLETED]: Created dashboard panels layout, added the Alerting Rules & Runbooks panel to dashboard, monitored SLO status, and prepared the final report.
- [EVIDENCE_LINK]: [app/dashboard.html](../app/dashboard.html), [docs/blueprint-template.md](blueprint-template.md)

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: Implemented `AuditFileProcessor` in `app/logging_config.py` to intercept security, startup, and control logs (e.g. incident enabling/disabling) and write them to a dedicated log file at `data/audit.jsonl` separate from transaction logs. Verified audit entries are recorded successfully.
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
