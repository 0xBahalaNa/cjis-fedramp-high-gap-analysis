"""Generate a markdown gap report from the CJIS overlay OSCAL data.

Reads an OSCAL profile overlay (CJIS v6.1 on FedRAMP High) and produces a
control-by-control gap report in markdown, formatted for GRC engineers and
CJIS auditors.

Usage:
    python scripts/generate_gap_report.py
    python scripts/generate_gap_report.py --input data/cjis-overlay.json \
        --output output/gap-report.md
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "data" / "cjis-overlay.json"
DEFAULT_OUTPUT = REPO_ROOT / "output" / "gap-report.md"

EXPECTED_SUB_PARTS = (
    "baseline-requirement",
    "cjis-addition",
    "implementation-guidance",
    "evidence-required",
)

GAP_TYPE_LABELS = {
    "implementation-delta": "Implementation-Level Delta",
    "control-level-gap": "Control-Level Gap",
}


class OverlayError(Exception):
    """Raised when the OSCAL overlay is missing required structure."""


def load_overlay(path: Path) -> dict:
    """Load and minimally validate the CJIS overlay OSCAL file."""
    if not path.is_file():
        raise OverlayError(f"overlay file not found: {path}")

    try:
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise OverlayError(f"invalid JSON in {path}: {exc}") from exc

    profile = data.get("profile")
    if not isinstance(profile, dict):
        raise OverlayError(f"{path}: missing top-level 'profile' object")

    alters = profile.get("modify", {}).get("alters")
    if not alters:
        raise OverlayError(f"{path}: no controls found under 'profile.modify.alters'")

    return data


def extract_deltas(data: dict) -> list[dict]:
    """Flatten the OSCAL alters into a list of delta records.

    Each record has: control_id, title, gap_type, delta_category,
    baseline, addition, guidance, evidence.
    """
    deltas: list[dict] = []
    for alter in data["profile"]["modify"]["alters"]:
        control_id = alter.get("control-id", "")
        for add in alter.get("adds", []):
            for part in add.get("parts", []):
                if part.get("name") != "cjis-delta":
                    continue
                props = {p["name"]: p["value"] for p in part.get("props", [])}
                sub_parts = {sp["name"]: sp.get("prose", "") for sp in part.get("parts", [])}
                missing = [name for name in EXPECTED_SUB_PARTS if name not in sub_parts]
                if missing:
                    print(
                        f"warning: {control_id} missing sub-parts {missing}",
                        file=sys.stderr,
                    )
                deltas.append(
                    {
                        "control_id": control_id.upper(),
                        "title": part.get("title", "").strip(),
                        "gap_type": props.get("gap-type", ""),
                        "delta_category": props.get("delta-category", ""),
                        "baseline": sub_parts.get("baseline-requirement", "(missing)"),
                        "addition": sub_parts.get("cjis-addition", "(missing)"),
                        "guidance": sub_parts.get("implementation-guidance", "(missing)"),
                        "evidence": sub_parts.get("evidence-required", "(missing)"),
                    }
                )
    return deltas


def group_by(items: Iterable[dict], key: str) -> dict[str, list[dict]]:
    """Group dict items by a key while preserving first-seen order."""
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        grouped[item[key]].append(item)
    return grouped


def humanize_category(value: str) -> str:
    """Turn 'pii-limitation' into 'PII Limitation'."""
    words = []
    for token in value.split("-"):
        words.append("PII" if token.lower() == "pii" else token.capitalize())
    return " ".join(words)


def format_report(data: dict, deltas: list[dict]) -> str:
    """Render the full markdown report."""
    meta = data["profile"]["metadata"]
    meta_props = {p["name"]: p["value"] for p in meta.get("props", [])}
    cjis_version = meta_props.get("cjis-version", "?")
    effective_date = meta_props.get("cjis-effective-date", "?")
    baseline_ref = meta_props.get("baseline-reference", "?")

    by_gap_type = group_by(deltas, "gap_type")

    out: list[str] = []
    out.append(f"# CJIS v{cjis_version} to {baseline_ref} - Gap Report")
    out.append("")
    out.append(
        f"Generated from `{DEFAULT_INPUT.relative_to(REPO_ROOT)}`. "
        f"CJIS Security Policy v{cjis_version} has been the default audit baseline since {effective_date}."
    )
    out.append("")

    out.append("## Summary")
    out.append("")
    out.append(f"- **Total deltas:** {len(deltas)}")
    for gap_type, label in GAP_TYPE_LABELS.items():
        out.append(f"- **{label}s:** {len(by_gap_type.get(gap_type, []))}")
    out.append("")

    for gap_type, label in GAP_TYPE_LABELS.items():
        subset = by_gap_type.get(gap_type, [])
        if not subset:
            continue
        out.append(f"## {label}s")
        out.append("")
        out.append("| Control | Category | Title |")
        out.append("|---------|----------|-------|")
        for d in subset:
            out.append(
                f"| {d['control_id']} | {humanize_category(d['delta_category'])} "
                f"| {d['title']} |"
            )
        out.append("")

    out.append("## Control-by-Control Detail")
    out.append("")
    for gap_type, label in GAP_TYPE_LABELS.items():
        subset = by_gap_type.get(gap_type, [])
        if not subset:
            continue
        out.append(f"### {label}s")
        out.append("")
        by_category = group_by(subset, "delta_category")
        for category, items in by_category.items():
            out.append(f"#### {humanize_category(category)}")
            out.append("")
            for d in items:
                out.append(f"##### {d['control_id']} - {d['title']}")
                out.append("")
                out.append("**FedRAMP High Baseline Requirement**")
                out.append("")
                out.append(d["baseline"])
                out.append("")
                out.append("**CJIS v6.1 Delta**")
                out.append("")
                out.append(d["addition"])
                out.append("")
                out.append("**Implementation Guidance**")
                out.append("")
                out.append(d["guidance"])
                out.append("")
                out.append("**Evidence Required**")
                out.append("")
                out.append(d["evidence"])
                out.append("")

    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a markdown gap report from the CJIS v6.1 overlay OSCAL file."
        )
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"Path to CJIS overlay OSCAL JSON (default: {DEFAULT_INPUT.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path to output markdown file (default: {DEFAULT_OUTPUT.relative_to(REPO_ROOT)})",
    )
    args = parser.parse_args(argv)

    try:
        data = load_overlay(args.input)
    except OverlayError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    deltas = extract_deltas(data)
    if not deltas:
        print("error: no cjis-delta parts found in overlay", file=sys.stderr)
        return 1

    report = format_report(data, deltas)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Wrote {args.output} ({len(deltas)} controls)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
