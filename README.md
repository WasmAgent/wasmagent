# WasmAgent

**Auditable, policy-enforced AI agent runtime for Cloudflare Workers and beyond.**

This is the public project home for WasmAgent — roadmap and project index.
The public media, release, and claim ledgers have been consolidated in the
org-wide [`.github` repository](https://github.com/WasmAgent/.github).

![WasmAgent product matrix](https://raw.githubusercontent.com/WasmAgent/.github/main/profile/assets/product-matrix.svg)

Source: canonical media hub in the org-wide [`.github` repository](https://github.com/WasmAgent/.github) (`profile/assets/product-matrix.svg`).

## Repositories

<!-- BEGIN PROJECT TABLE -->

| Repository | Purpose |
|---|---|
| [wasmagent-js](https://github.com/WasmAgent/wasmagent-js) | Core JS/TS runtime and MCP server |
| [agent-trust-infra](https://github.com/WasmAgent/agent-trust-infra) | MCP / Trust / Attestation specifications, validators, and trust artifacts (AgentBOM, MCP Posture, Trust Passport) |
| [bscode](https://github.com/WasmAgent/bscode) | Cloudflare Workers benchmark & demo workload |
| [trace-pipeline](https://github.com/WasmAgent/trace-pipeline) | Trace ingestion, audit, and claim/eval pipeline |
| [open-agent-audit](https://github.com/WasmAgent/open-agent-audit) | Open evidence format and Cloudflare-native audit toolkit |
| [fresharena](https://github.com/WasmAgent/fresharena) | Sister project — agent evaluation arena |
| [.github](https://github.com/WasmAgent/.github) | Org-wide public ledgers (media, releases, claims) |
| [wasmagent](https://github.com/WasmAgent/wasmagent) | Project home, roadmap, and repository index (this repository) |

<!-- END PROJECT TABLE -->

Repository classification (public products vs. internal tooling) is available as
machine-readable metadata in [`repos.yml`](repos.yml); see
[docs/repository-manifest.md](docs/repository-manifest.md) for the schema. The
project-table generator ([`scripts/generate_project_table.py`](scripts/generate_project_table.py))
derives the table above from this manifest, omitting internal tools such as
`claude-bot` and `wasmagent-ops`, and CI verifies the two never drift apart.

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

## Shipped work

Shipped milestones are tracked in the consolidated [release ledger](RELEASE_LEDGER.md).
AgentBOM, MCP Posture, and Trust Passport have graduated off the roadmap and are
recorded there as shipped/closed agent-trust-infra deliverables. For the
code-level API/SDK interfaces, see the
[agent-trust-infra API/SDK reference](docs/agent-trust-infra-specs.md).

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for **In progress** and **Planned** work.
Shipped milestones are recorded in the [release ledger](RELEASE_LEDGER.md).
