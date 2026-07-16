"""Architect-agent repo integrity tests.

This repo is a documentation/agent-spec package (no runtime app). These tests
validate the contract a reviewer cares about: required docs exist, the README
defines the agent's purpose, and no placeholder test scaffold remains.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_required_docs_present():
    for rel in ["README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md", "LAUNCH.md"]:
        assert (REPO / rel).exists(), f"missing {rel}"


def test_readme_has_agent_sections():
    text = (REPO / "README.md").read_text(encoding="utf-8")
    for section in ["# Architect Agent", "## What It Does", "## Design Principles"]:
        assert section in text, f"README missing section: {section}"


def test_no_placeholder_test_left_behind():
    tests_dir = REPO / "tests"
    for f in tests_dir.glob("*.py"):
        if f.name == "__init__.py":
            continue
        assert "test_placeholder" not in f.name, f"placeholder test still present: {f.name}"
        body = f.read_text(encoding="utf-8")
        for line in body.splitlines():
            stripped = line.strip()
            if stripped == "assert True" or stripped.startswith("def test_placeholder"):
                assert False, f"placeholder assert found in {f.name}: {stripped}"
