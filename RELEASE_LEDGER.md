# WasmAgent Release Ledger

Published milestones — items that have shipped and graduated off the
[roadmap](docs/roadmap.md). This ledger is the canonical record of completed
work; the [roadmap](docs/roadmap.md) tracks only what is **In progress** or
**Planned**.

Per-package release history (versions, dates, artifacts) lives in the
org-wide [`.github` repository](https://github.com/WasmAgent/.github)
(`releases/public-release-ledger.yml`). The entries below track milestone-level
graduation rather than individual version bumps.

## Published

- [x] Core agent runtime (`@wasmagent/core`)
- [x] QuickJS sandbox kernel (`@wasmagent/kernel-quickjs`)
- [x] Remote sandbox kernel (`@wasmagent/kernel-remote`)
- [x] AI SDK adapter (`@wasmagent/aisdk`)
- [x] Mastra sandbox adapter (`@wasmagent/mastra-sandbox`)
- [x] Compliance Engine alpha (`@wasmagent/compliance`) — IFEval × PCL pipeline
- [x] AEP / BudgetLedger / AEPEmitter (`@wasmagent/aep`)
- [x] OTel exporter + AEP span names (`@wasmagent/otel-exporter`)
- [x] MCP Firewall / Gateway / Policy / Attestation
- [x] AgentBOM, MCP Posture, and Trust Passport specifications — [agent-trust-infra](https://github.com/WasmAgent/agent-trust-infra) (PR #42: end-to-end chain visualization, runnable demo, README stitching)
- [x] Public claim registry — migrated to [.github](https://github.com/WasmAgent/.github)
