# WasmAgent

**Auditable, policy-enforced AI agent runtime for Cloudflare Workers and beyond.**

This is the public project home for WasmAgent — roadmap and project index.
The public media, release, and claim ledgers have been consolidated in the
org-wide [`.github` repository](https://github.com/WasmAgent/.github).

![WasmAgent product matrix](assets/product-matrix.webp)

## Repositories

| Repository | Purpose |
|---|---|
| [wasmagent-js](https://github.com/WasmAgent/wasmagent-js) | Core JS/TS runtime and MCP server |
| [agent-trust-infra](https://github.com/WasmAgent/agent-trust-infra) | MCP / Trust / Attestation specifications, validators, and trust artifacts (AgentBOM, MCP Posture, Trust Passport) |
| [bscode](https://github.com/WasmAgent/bscode) | Cloudflare Workers benchmark & demo workload |
| [trace-pipeline](https://github.com/WasmAgent/trace-pipeline) | Trace ingestion, audit, claim/eval pipeline |
| [open-agent-audit](https://github.com/WasmAgent/open-agent-audit) | Open evidence format and Cloudflare-native audit toolkit |
| [fresharena](https://github.com/WasmAgent/fresharena) | Sister project — agent evaluation arena |
| [.github](https://github.com/WasmAgent/.github) | Org-wide public ledgers (media, releases, claims) |
| [wasmagent](https://github.com/WasmAgent/wasmagent) | This repo — project home, roadmap |

## Key concepts

- **Agent Execution Proof (AEP)** — every tool call produces a structured, hash-linked audit record
- **MCP Trust Pack** — policy enforcement and capability attestation for MCP servers
- **Compliance Engine** — runtime instruction-following evaluation + repair pipeline
- **Trace-to-Training** — agent runs become structured training data via `ComplianceEvalRecord`

## Public ledgers

The public media, claims, and release ledgers live in the org-wide
[`.github` repository](https://github.com/WasmAgent/.github):

- **Media ledger** (`media/posts.yml`) — published articles and their claim bindings
- **Claims registry** (`claims/public-claims.yml`) — verified public claims with evidence links
- **Release ledger** (`releases/public-release-ledger.yml`) — release history

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for **In progress** and **Planned** work.
Shipped milestones are recorded in the [release ledger](RELEASE_LEDGER.md).
