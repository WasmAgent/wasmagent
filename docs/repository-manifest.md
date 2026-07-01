# Repository manifest

WasmAgent ships a machine-readable manifest that classifies every repository in
the organization as a **public product** or **internal tool**. It is the
canonical metadata source consumed by the project-table generator
([`scripts/generate_project_table.py`](../scripts/generate_project_table.py),
[wasmagent#48](https://github.com/WasmAgent/wasmagent/issues/48)) and other org
tooling to decide which repositories to surface publicly.

- Manifest: [`repos.yml`](../repos.yml)
- Schema version: `1`

## Schema

Each entry in `repositories[]` exposes the following fields.

| Field | Type | Description |
|---|---|---|
| `name` | string | Repository name without the owner prefix. |
| `url` | string | Canonical GitHub URL. |
| `category` | enum | `public-product`, `infrastructure`, `project-home`, or `internal-tool`. |
| `public_product` | boolean | `true` when the repo should be surfaced as a public product/table row; `false` for internal tooling. |
| `purpose` | string | Short human-readable description. |

## Filtering rule

To reproduce the public project table, include only repositories where
`public_product == true`:

```python
import yaml

with open("repos.yml") as f:
    manifest = yaml.safe_load(f)

public_products = [r for r in manifest["repositories"] if r["public_product"]]
```

Internal tools such as `claude-bot` and `wasmagent-ops` set
`public_product: false` and are therefore omitted from the public table.

## Categories

| Category | Meaning |
|---|---|
| `public-product` | A shipped product or library consumed by users. |
| `infrastructure` | Org-wide infrastructure (for example, the `.github` ledgers). |
| `project-home` | The org project home and index repository. |
| `internal-tool` | Internal operations and automation tooling — not a public product. |

## Adding a repository

1. Append a new entry to `repositories[]` in [`repos.yml`](../repos.yml).
2. Set `category` and `public_product` to reflect whether the repository is a
   public product or an internal tool.
3. The project-table generator picks up the change automatically on the next
   build; no Markdown table edits are required.
