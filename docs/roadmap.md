# WasmAgent Roadmap

This roadmap tracks work that is **In progress** or **Planned**. Shipped
milestones are recorded in the org-wide
[release ledger](https://github.com/WasmAgent/.github) maintained in `.github`
(`releases/public-release-ledger.yml`).

## Complete

- [x] AgentBOM, MCP Posture & Trust Passport specifications, validators, and trust artifacts — shipped in [agent-trust-infra](https://github.com/WasmAgent/agent-trust-infra) (PR #48); see the [API/SDK interface reference](agent-trust-infra-specs.md) and the [release ledger](../RELEASE_LEDGER.md).
- [x] Public trace-pipeline launch — shipped; see the release ledger.
- [x] Cloudflare Workers Agent demo (bscode) — shipped; see the release ledger.

## In progress

<!-- The MCP / Trust / Attestation specifications and validators are owned by
     the WasmAgent/agent-trust-infra repository
     (https://github.com/WasmAgent/agent-trust-infra), which is the source of
     truth for those domains; the corresponding npm publishes already shipped —
     see the release ledger. These items were removed from "In progress" to
     avoid orphaned duplicates of already-shipped milestones. -->

## Planned

- [ ] Trace-to-training public methodology doc
- [ ] IFEval benchmark reproducibility package
- [ ] Compliance Engine stable release
