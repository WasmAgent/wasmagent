# AgentBOM & MCP Posture — API/SDK interfaces

The canonical, code-level definitions of the **AgentBOM**, **MCP Posture**, and
**Trust Passport** specifications live in the
[WasmAgent/agent-trust-infra](https://github.com/WasmAgent/agent-trust-infra)
repository, which is the source of truth for the MCP / Trust / Attestation
domain. This page is the WasmAgent-side index that points tooling and
downstream issues (for example `wasmagent#40`) at those interfaces so they can
link to a stable canonical location rather than to prose alone.

## What agent-trust-infra provides

For each of the AgentBOM, MCP Posture, and Trust Passport specs,
agent-trust-infra owns:

- the normative **specification** document,
- the **validators** — the code-level interface that consumers integrate
  against, and
- the **trust artifacts** schema.

These are the surfaces WasmAgent relies on for trust and attestation, and that
the MCP Firewall / Gateway / Policy / Attestation packages interoperate with.

## Status

Per the WasmAgent [release ledger](../RELEASE_LEDGER.md), the AgentBOM, MCP
Posture, and Trust Passport specifications, validators, and trust artifacts are
recorded as shipped via
[agent-trust-infra PR #48](https://github.com/WasmAgent/agent-trust-infra/pull/48)
(end-to-end chain visualization, runnable demo, README stitching), and the
corresponding npm publishes have shipped.

agent-trust-infra remains the authoritative source for the current API surface,
schema versions, and stability classification. Consult its README and published
packages for the binding contract before integrating.
