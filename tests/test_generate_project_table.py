"""Tests for the WasmAgent public project-table generator.

Stdlib-only (``unittest``) so no extra dependencies are required. Run with::

    python3 -m unittest discover -s tests
    # or
    python3 tests/test_generate_project_table.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Make the generator importable regardless of the current working directory.
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import generate_project_table as gpt  # noqa: E402


def _write_manifest(text: str) -> Path:
    """Write ``text`` to a temporary manifest file and return its path."""
    handle = tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False, encoding="utf-8"
    )
    handle.write(text)
    handle.flush()
    handle.close()
    return Path(handle.name)


PUBLIC = """\
schema_version: 1
repositories:
  - name: wasmagent-js
    url: https://github.com/WasmAgent/wasmagent-js
    category: public-product
    public_product: true
    purpose: Core JS/TS runtime and MCP server
"""


class PublicRepositoriesTests(unittest.TestCase):
    def test_surfaces_public_products(self):
        path = _write_manifest(PUBLIC)
        surfaced = gpt.public_repositories(path)
        self.assertEqual([r["name"] for r in surfaced], ["wasmagent-js"])

    def test_excludes_internal_tool_with_public_product_false(self):
        """An internal-tool repo with public_product: false is omitted."""
        path = _write_manifest(
            PUBLIC
            + """\
  - name: wasmagent-ops
    url: https://github.com/WasmAgent/wasmagent-ops
    category: internal-tool
    public_product: false
    purpose: Internal operations and automation tooling
"""
        )
        surfaced = gpt.public_repositories(path)
        self.assertEqual([r["name"] for r in surfaced], ["wasmagent-js"])

    def test_rejects_internal_tool_misflagged_as_public(self):
        """A category=internal-tool repo with public_product: true is a hard
        error (category-based defence-in-depth, wasmagent#53)."""
        path = _write_manifest(
            PUBLIC
            + """\
  - name: wasmagent-ops
    url: https://github.com/WasmAgent/wasmagent-ops
    category: internal-tool
    public_product: true
    purpose: Internal operations and automation tooling
"""
        )
        with self.assertRaises(ValueError) as ctx:
            gpt.public_repositories(path)
        self.assertIn("internal-tool", str(ctx.exception))
        self.assertIn("wasmagent-ops", str(ctx.exception))

    def test_rejects_unknown_internal_tool_misflagged_as_public(self):
        """The category guard is self-maintaining: an internal tool that is
        NOT in FORBIDDEN_PUBLIC is still rejected by its category."""
        path = _write_manifest(
            PUBLIC
            + """\
  - name: some-future-ops-bot
    url: https://github.com/WasmAgent/some-future-ops-bot
    category: internal-tool
    public_product: true
    purpose: Another internal tool
"""
        )
        with self.assertRaises(ValueError):
            gpt.public_repositories(path)

    def test_rejects_forbidden_public_name_even_without_category(self):
        """FORBIDDEN_PUBLIC is a name-based backstop independent of category."""
        path = _write_manifest(
            PUBLIC
            + """\
  - name: claude-bot
    url: https://github.com/WasmAgent/claude-bot
    category: public-product
    public_product: true
    purpose: Should not be surfaced
"""
        )
        with self.assertRaises(ValueError) as ctx:
            gpt.public_repositories(path)
        self.assertIn("claude-bot", str(ctx.exception))


class RenderTableTests(unittest.TestCase):
    def test_render_excludes_internal_tools(self):
        repos = gpt.public_repositories(
            _write_manifest(
                PUBLIC
                + """\
  - name: wasmagent-ops
    url: https://github.com/WasmAgent/wasmagent-ops
    category: internal-tool
    public_product: false
    purpose: Internal operations and automation tooling
"""
            )
        )
        table = gpt.render_table(repos)
        self.assertIn("wasmagent-js", table)
        self.assertNotIn("wasmagent-ops", table)


if __name__ == "__main__":
    unittest.main()
