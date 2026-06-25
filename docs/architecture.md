# WasmAgent Architecture Overview

## System overview

```
┌─────────────────────────────────────────────────────┐
│                   Application / LLM                  │
└──────────────────────────┬──────────────────────────┘
                           │ tool call request
┌──────────────────────────▼──────────────────────────┐
│              GatewayMiddleware chain                 │
│  (composeMiddleware — mcp-gateway)                   │
│                                                      │
│  1. RequestIdentity extraction                       │
│  2. PolicyBundle.evaluate()  (mcp-policy)            │
│  3. CapabilityAttestation check (mcp-attestation)    │
│  4. isStateChangingTool() risk gate (mcp-firewall)   │
│  5. GatewayDecision: allow / deny / require_approval │
└──────────────────────────┬──────────────────────────┘
                           │ allowed
┌──────────────────────────▼──────────────────────────┐
│               AEPEmitter + BudgetLedger              │
│  (aep package)                                       │
│  - emits wasmagent.tool.invocation span              │
│  - charges BudgetLedger                              │
└──────────────────────────┬──────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────┐
│              Sandbox Kernel (tool execution)         │
│  kernel-quickjs  │  kernel-remote                   │
└──────────────────────────┬──────────────────────────┘
                           │ result
┌──────────────────────────▼──────────────────────────┐
│               AEPEmitter (result span)               │
│  - emits wasmagent.tool.result span                  │
│  - ComplianceVerifier runs if configured             │
└──────────────────────────┬──────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────┐
│               ComplianceEvalRecord                   │
│  canonical cross-repo data contract                  │
│  consumed by trace-pipeline → evomerge               │
└─────────────────────────────────────────────────────┘
```

## Package map

| Package | npm | Purpose |
|---|---|---|
| `@wasmagent/core` | stable | Agent runtime, ToolCallingAgent, KernelPool |
| `@wasmagent/kernel-quickjs` | stable | QuickJS sandbox |
| `@wasmagent/kernel-remote` | stable | Remote sandbox via runCommand |
| `@wasmagent/aep` | alpha→stable | AEPRecord, AEPEmitter, BudgetLedger |
| `@wasmagent/otel-exporter` | growth | OTel export, AEP_SPAN_NAMES |
| `@wasmagent/mcp-firewall` | growth | MCPGateway, isStateChangingTool, GatewayDecision |
| `@wasmagent/mcp-gateway` | growth | GatewayMiddleware, composeMiddleware, InMemoryAuditLogger |
| `@wasmagent/mcp-policy` | growth | PolicyBundle, PolicyBundleMetadata |
| `@wasmagent/mcp-attestation` | growth | CapabilityAttestation, AttestationRegistry |
| `@wasmagent/compliance` | alpha | ComplianceVerifier, IFEvalVerifier, RepairPlanner |
| `@wasmagent/aisdk` | growth | AI SDK adapter |
| `@wasmagent/mastra-sandbox` | growth | Mastra sandbox adapter |
| `@wasmagent/devtools` | growth | React DevTools for agent traces |
| `@wasmagent/evals-runner` | growth | Eval harness |

## Data flow: trace-to-training

```
agent run
  → AEPRecord (wasmagent-js)
  → ComplianceEvalRecord (wasmagent-js/compliance)
  → trace-pipeline ingestion
  → evomerge: SFT / DPO / router training
```
