# Evaluation Summary

## IFEval benchmark: Compliance Engine × small models

Benchmark: IFEval (instruction-following evaluation), 50 samples × 3 seeds.

### Results — Qwen2.5-1.5B-Q4

| Repair mode | Pass rate | Std dev | Notes |
|---|---|---|---|
| `direct` | ~38% | — | No repair |
| `prompt_retry` | 46.0% | ±2.0pp | Single retry with rephrased prompt |
| `full_pcl` | **54.7%** | **±1.2pp** | Full compliance-conditioned repair loop |

**Delta: +8.7pp** (full_pcl vs prompt_retry), with 40% lower variance.

### Results — Llama-3.2-1B

| Repair mode | Pass rate | Std dev |
|---|---|---|
| `prompt_retry` | ~42% | ±4.8pp |
| `full_pcl` | ~42% | **±0.9pp** |

On Llama-3.2-1B, full_pcl ties on mean but achieves 5× lower variance — more
predictable compliance without mean improvement. This is consistent with the
hypothesis that PCL acts as a variance stabilizer for weaker models.

### Reproduce

```bash
git clone https://github.com/WasmAgent/wasmagent-js
cd wasmagent-js
bun packages/compliance/benchmarks/ifeval/run.ts --limit=50 --seed=42
```

Full methodology: [wasmagent-js/packages/compliance/benchmarks/ifeval/](https://github.com/WasmAgent/wasmagent-js/tree/main/packages/compliance/benchmarks/ifeval)

### Claim binding

| Claim | Status |
|---|---|
| CLAIM-TTP-001: full_pcl +8.7pp over prompt_retry on Qwen2.5-1.5B-Q4 | Verified |
