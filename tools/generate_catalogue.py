#!/usr/bin/env python3
"""Generate reviewed, value-free documentation from an external local JSON file."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "tools" / "field_notes.json").read_text(encoding="utf-8"))
NOTES = REGISTRY["entries"]
DYNAMIC_MAPS = set(REGISTRY["dynamic_maps"])


def kind(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    raise ValueError("Unsupported JSON value")


def child_path(parent: str, key: str) -> str:
    # All members of these maps are identifiers, regardless of their spelling.
    safe_key = "*" if parent in DYNAMIC_MAPS else key
    path = parent + "[" + json.dumps(safe_key, ensure_ascii=False) + "]"
    if path not in NOTES:
        # Never echo unreviewed keys, even in error messages.
        raise ValueError("Unreviewed object path: no output written. Review new field names privately and update tools/field_notes.json before regenerating.")
    return path


def walk(value: Any, path: str = "$") -> list[dict[str, str]]:
    if path not in NOTES:
        raise ValueError("Unreviewed array item path: no output written.")
    rows = [{"path": path, "type": kind(value)}]
    if isinstance(value, dict):
        for key, child in value.items():
            rows.extend(walk(child, child_path(path, key)))
    elif isinstance(value, list):
        for child in value:
            rows.extend(walk(child, path + "[]"))
    return rows


def illustrative(value: Any, path: str = "$") -> Any:
    """Replace every value; preserve all distinct observed array item shapes."""
    if value is None:
        return "<illustrative null placeholder>"
    if isinstance(value, bool):
        return True
    if isinstance(value, int):
        return 1
    if isinstance(value, float):
        return 1.0
    if isinstance(value, str):
        return "<illustrative>"
    if isinstance(value, list):
        if not value:
            return "<illustrative empty-array placeholder>"
        unique = {}
        for item in value:
            example = illustrative(item, path + "[]")
            unique[json.dumps(example, sort_keys=True)] = example
        return [unique[key] for key in sorted(unique)]
    if isinstance(value, dict):
        if not value:
            return "<illustrative empty-object placeholder>"
        out = {}
        for key, child in value.items():
            target = child_path(path, key)
            safe_key = "*" if path in DYNAMIC_MAPS else key
            example = illustrative(child, target)
            if safe_key in out and out[safe_key] != example:
                raise ValueError("Dynamic map has incompatible example shapes; no output written. Review privately before extending the example format.")
            out[safe_key] = example
        return out
    raise ValueError("Unsupported JSON value")


def section(path: str) -> str:
    return "(root)" if path == "$" else json.JSONDecoder().raw_decode(path[2:])[0]


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def sources_text(note: dict) -> str:
    items = []
    for source in note["sources"]:
        if "url" in source:
            items.append(f"[{source['label']}]({source['url']}) (product context; key mapping unverified)")
        else:
            items.append(source["label"])
    return "; ".join(items) or "No supporting public source located."


def render_reference(rows: list[dict[str, str]], observed_on: str) -> str:
    sections = sorted({section(row["path"]) for row in rows if row["path"] != "$"})
    lines = [
        "# Observed key reference", "",
        f"One response observed on {observed_on}; no observed values are published. See [scope and evidence rules](README.md).", "",
        "`[]` represents observed array item shapes. `*` replaces every identifier in reviewed role maps, including built-in role keys. Multiple identifiers and repeated items collapse to distinct path/type pairs. Null and empty collections establish no hidden schema types.", "",
        "Official links provide product context, not confirmation of an internal JSON key. All backend mappings below remain inferred or unknown except the explicitly attributed Windows client observation supplied by the source author.", "",
        "## Contents", "",
    ]
    lines += [f"- [{name}](#{name})" for name in sections]
    lines += [""]
    for name in sections:
        lines += [f"## {name}", "", "| Full JSON path | Observed type | Meaning | Status | Evidence / context |", "|---|---|---|---|---|"]
        for row in rows:
            if section(row["path"]) != name:
                continue
            note = NOTES[row["path"]]
            cells = [f"`{row['path']}`", f"`{row['type']}`", note["meaning"], note["status"], sources_text(note)]
            lines.append("| " + " | ".join(map(escape_cell, cells)) + " |")
        lines.append("")
    return "\n".join(lines)


def generate(data: Any, observed_on: str) -> dict[str, str]:
    try:
        if date.fromisoformat(observed_on).isoformat() != observed_on:
            raise ValueError("Noncanonical date")
    except ValueError:
        raise ValueError("Invalid observation date; use YYYY-MM-DD. No output written.") from None
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object at the response root")
    raw_rows = walk(data)
    rows = [dict(path=p, type=t) for p, t in sorted({(r["path"], r["type"]) for r in raw_rows})]
    catalogue = {
        "title": "Unofficial ChatGPT workspace settings response catalogue",
        "observed_on": observed_on,
        "source_endpoint": "GET https://chatgpt.com/backend-api/accounts/{account_id}/settings",
        "scope_note": "One response only; no observed values. Null and empty collections do not establish hidden types.",
        "path_convention": "JSONPath-like brackets; [] aggregates observed array item shapes; * redacts every key in reviewed dynamic role maps.",
        "entries": [dict(row, **NOTES[row["path"]]) for row in rows],
    }
    example = {
        "notice": "ILLUSTRATIVE ONLY. Scalar values are synthetic and may coincidentally match a source value. Nulls and empty collections use explicit placeholder strings; consult catalogue.json for observed types. Dynamic role keys and duplicate item shapes are collapsed.",
        "response": illustrative(data),
    }
    # Build everything before writing so rejected input cannot partially refresh outputs.
    return {
        "catalogue.json": json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n",
        "REFERENCE.md": render_reference(rows, observed_on),
        "example-response.json": json.dumps(example, indent=2, ensure_ascii=False) + "\n",
    }


def unique_object(pairs: list[tuple[str, Any]]) -> dict:
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("Duplicate JSON object key; no output written.")
        obj[key] = value
    return obj


def reject_constant(_: str) -> None:
    raise ValueError("Nonstandard JSON numeric constant; no output written.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON response outside this repository")
    parser.add_argument("--observed-on", required=True, help="observation date (YYYY-MM-DD)")
    args = parser.parse_args()
    try:
        if args.input.resolve().is_relative_to(ROOT):
            raise ValueError("Keep local input JSON outside the repository; no output written.")
        data = json.loads(args.input.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object, parse_constant=reject_constant)
        outputs = generate(data, args.observed_on)
    except (OSError, ValueError) as error:
        # OS/decoder diagnostics may contain private paths or input snippets.
        message = str(error) if type(error) is ValueError else "Could not read valid local JSON; no output written."
        raise SystemExit(message) from None
    for name, content in outputs.items():
        (ROOT / name).write_text(content, encoding="utf-8")
    print("Generated catalogue, reference, and illustrative example from reviewed paths.")


if __name__ == "__main__":
    main()
