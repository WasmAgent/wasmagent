#!/usr/bin/env python3
"""Generate the WasmAgent public project table from the repository manifest.

The project table in ``README.md`` is derived from the canonical repository
manifest (``repos.yml``). Only repositories with ``public_product: true`` are
surfaced; internal tooling such as ``claude-bot`` and ``wasmagent-ops`` is
omitted. This keeps the README table in lock-step with the public WasmAgent org
profile and prevents the table from silently drifting out of sync.

Usage::

    scripts/generate_project_table.py --check README.md
        Verify the README project table matches repos.yml. Exits non-zero and
        prints a diff on drift.

    scripts/generate_project_table.py --write README.md
        Rewrite the README project table to match repos.yml.

The managed table in README.md is delimited by the markers
``<!-- BEGIN PROJECT TABLE -->`` / ``<!-- END PROJECT TABLE -->``.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - dependency declared in CI
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "repos.yml"
README = ROOT / "README.md"

BEGIN_MARKER = "<!-- BEGIN PROJECT TABLE -->"
END_MARKER = "<!-- END PROJECT TABLE -->"

# Repositories that must never be surfaced as public products, regardless of the
# manifest. This is a defence-in-depth guard against accidental reclassification.
FORBIDDEN_PUBLIC = ("claude-bot", "wasmagent-ops")

# Matches the managed block, markers inclusive (DOTALL so newlines are covered).
_BLOCK_RE = re.compile(
    re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
)


def load_repositories(manifest_path: Path = MANIFEST) -> list[dict]:
    """Return the full repository list from the manifest."""
    with manifest_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return list(data.get("repositories", []))


def public_repositories(manifest_path: Path = MANIFEST) -> list[dict]:
    """Return only repositories that should appear in the public table."""
    repos = load_repositories(manifest_path)
    surfaced = [r for r in repos if r.get("public_product") is True]
    names = {r["name"] for r in surfaced}
    for forbidden in FORBIDDEN_PUBLIC:
        if forbidden in names:
            raise ValueError(
                f"{forbidden!r} is classified as a public product in "
                f"{manifest_path.name}; it is internal tooling and must set "
                f"public_product: false"
            )
    return surfaced


def render_table(repos: list[dict]) -> str:
    """Render the markdown table (header + rows) for the given repositories."""
    lines = ["| Repository | Purpose |", "|---|---|"]
    for repo in repos:
        name = repo["name"]
        url = repo.get("url") or f"https://github.com/WasmAgent/{name}"
        purpose = str(repo.get("purpose", "")).strip().replace("\n", " ")
        lines.append(f"| [{name}]({url}) | {purpose} |")
    return "\n".join(lines)


def expected_block(repos: list[dict]) -> str:
    """Return the full managed block (markers inclusive) for README.md."""
    return f"{BEGIN_MARKER}\n\n{render_table(repos)}\n\n{END_MARKER}"


def current_block(text: str) -> str | None:
    """Return the existing managed block (markers inclusive), or None."""
    match = _BLOCK_RE.search(text)
    return match.group(0) if match else None


def cmd_check(readme_path: Path) -> int:
    """Verify README.md's table matches the manifest. Returns shell exit code."""
    try:
        repos = public_repositories()
    except ValueError as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 1

    text = readme_path.read_text(encoding="utf-8")
    existing = current_block(text)
    if existing is None:
        sys.stderr.write(
            f"error: managed table markers not found in {readme_path.name} "
            f"(expected `{BEGIN_MARKER}` ... `{END_MARKER}`)\n"
        )
        return 1

    expected = expected_block(repos)
    if existing != expected:
        sys.stderr.write(
            f"error: README project table is out of sync with "
            f"{MANIFEST.relative_to(ROOT)}\n"
        )
        diff = difflib.unified_diff(
            existing.splitlines(keepends=True),
            expected.splitlines(keepends=True),
            fromfile=f"{readme_path.name} (current)",
            tofile=f"{readme_path.name} (expected)",
            n=1,
        )
        sys.stderr.writelines(diff)
        sys.stderr.write(
            "\nFix with: python3 scripts/generate_project_table.py --write "
            "README.md\n"
        )
        return 1
    return 0


def cmd_write(readme_path: Path) -> int:
    """Regenerate the managed table in README.md. Returns shell exit code."""
    repos = public_repositories()
    block = expected_block(repos)
    text = readme_path.read_text(encoding="utf-8")
    if current_block(text) is not None:
        new_text = _BLOCK_RE.sub(lambda _: block, text)
    else:
        # Insert the managed block right after the "## Repositories" heading.
        heading = "## Repositories"
        if heading not in text:
            sys.stderr.write(
                f"error: could not find `{heading}` heading in {readme_path.name} "
                f"and no managed markers are present\n"
            )
            return 1
        new_text = text.replace(
            heading, f"{heading}\n\n{block}", 1
        )
    readme_path.write_text(new_text, encoding="utf-8")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate the WasmAgent public project table from repos.yml.",
    )
    parser.add_argument(
        "readme",
        nargs="?",
        type=Path,
        default=README,
        help="Path to README.md (default: %(default)s)",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check",
        action="store_true",
        help="verify the README table matches repos.yml",
    )
    mode.add_argument(
        "--write",
        action="store_true",
        help="rewrite the README table to match repos.yml",
    )
    args = parser.parse_args(argv)

    if not args.readme.exists():
        sys.stderr.write(f"error: {args.readme} does not exist\n")
        return 2

    if args.check:
        return cmd_check(args.readme)
    return cmd_write(args.readme)


if __name__ == "__main__":
    sys.exit(main())
