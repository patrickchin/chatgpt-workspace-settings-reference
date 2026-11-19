#!/usr/bin/env python3
"""Generate a value-free key/type catalogue from a local workspace settings JSON.

Uses only the Python standard library. Does not transmit or copy the input values.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATE = "2026-11-19"
ROLE_KEY = re.compile(r"^role_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}~[0-9a-f]{20,}$", re.IGNORECASE)

SOURCES = {
    "workspace": "[OpenAI workspace settings overview](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise)",
    "rbac": "[OpenAI RBAC guide](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt)",
    "business": "[OpenAI Business roles and discovery](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business)",
}


def kind(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "unknown"


def quote_key(key: str) -> str:
    return json.dumps(key, ensure_ascii=False)


def normalized_key(key: str) -> str:
    return "*" if ROLE_KEY.match(key) else key


def walk(value: Any, path: str = "$", top: str | None = None) -> list[dict[str, str]]:
    rows = [{"path": path, "type": kind(value), "section": top or "(root)"}]
    if isinstance(value, dict):
        for key, child in value.items():
            display_key = normalized_key(key)
            section = top or display_key
            rows.extend(walk(child, f"{path}[{quote_key(display_key)}]", section))
    elif isinstance(value, list):
        for child in value:
            rows.extend(walk(child, f"{path}[]", top))
    return rows


def illustrative(value: Any) -> Any:
    """Replace values with examples; use explicit strings for null/empty values."""
    if value is None:
        return "<illustrative null placeholder>"
    if isinstance(value, bool):
        return True
    if isinstance(value, int) and not isinstance(value, bool):
        return 1
    if isinstance(value, float):
        return 1.0
    if isinstance(value, str):
        return "<illustrative>"
    if isinstance(value, list):
        if not value:
            return "<illustrative empty-array placeholder>"
        # One representative item per array keeps the example compact.
        return [illustrative(value[0])]
    if isinstance(value, dict):
        if not value:
            return "<illustrative empty-object placeholder>"
        out = {}
        for key, child in value.items():
            out[normalized_key(key)] = illustrative(child)
        return out
    return "<illustrative>"


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def meaning(row: dict[str, str]) -> tuple[str, str, str]:
    path = row["path"]
    context_path = path[:-2] if path.endswith("[]") else path
    leaf = context_path.rsplit("[", 1)[-1].rstrip("]")
    try:
        name = json.loads(leaf) if leaf != "" else "array item"
    except json.JSONDecodeError:
        name = "array item"
    name = str(name)
    low = name.lower()
    if path == "$":
        return "Top-level JSON response object.", "Confirmed", SOURCES["workspace"]
    if name == "permissions" or name == "role_summaries" or "assignment_sources" in path:
        return "Permission or role-related data; the response shape alone does not define the exact authorization semantics.", "Confirmed", SOURCES["rbac"]
    if name in {"workspace_id", "workspace_discoverable", "public_display_name", "use_workspace_name_for_discovery", "auto_accept_requests"}:
        return "Workspace identity or discovery-related field, based on the documented workspace controls.", "Confirmed", SOURCES["business"]
    if name == "config.toml":
        return "Local Codex configuration file reference; unrelated to this server response field.", "Confirmed", "[Codex configuration reference](https://developers.openai.com/codex/config-reference/)"
    if name in {"settings", "beta_settings", "beta_settings_str", "beta_settings_dict", "desktop_app_beta_policy", "available_admin_preview_features", "admin_preview_launch_settings", "admin_preview_launch_defaults", "admin_preview_matching", "model_permission_preferences"}:
        return f"Container or policy field named `{name}`; precise backend semantics are not documented here.", "Inferred from name", "—"
    if name in {"id", "name", "metadata", "principal_id", "principal_type", "revision", "mode", "configured", "kind", "instructions", "request_url", "gpt_share_setting", "chat_share_setting", "conversation_ttl", "access_token_max_ttl", "allowed_custom_actions_domains", "allowed_web_search_domains", "seat_type_credit_limits", "access_request", "default_seat_type", "plugin_incentive_campaigns", "public_display_name"}:
        return "The field name indicates the general data concept; its backend-specific effect is not established by this response.", "Inferred from name", "—"
    if "windows_computer_use" == name:
        return "Feature-availability flag checked by the installed Windows client, as observed by the source author; no Mac equivalent is verified.", "Confirmed", "—"
    if any(token in low for token in ("access", "enable", "allow", "disable", "sharing", "share", "plugin", "model", "connector", "codex", "workspace", "admin_preview", "retired", "launched", "eligible", "visible", "opt_out", "policy", "training", "history", "feedback", "suggestion", "trial", "scim", "switching", "referral", "profile", "search", "invite", "approval", "join", "seat", "incentive", "banner", "orbit", "work_mode", "local_enabled")):
        return f"Name suggests a {name.replace('_', ' ')} setting or feature flag; no specific server behavior is verified.", "Inferred from name", "—"
    return "No reliable meaning established from the field name or cited documentation.", "Unknown", "—"


def render_reference(rows: list[dict[str, str]], observed_on: str) -> str:
    by_section: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if row["path"] == "$":
            continue
        by_section.setdefault(row["section"], []).append(row)
    lines = [
        "# Observed key reference",
        "",
        f"One response observed on {observed_on}. This is an unofficial snapshot, not a complete schema or a statement of defaults. The original values are intentionally omitted.",
        "",
        "`[]` denotes a representative array item. `*` denotes a redacted role-like map key. `null` and empty collections reveal no underlying schema type beyond the observed JSON value.",
        "",
    ]
    for section, section_rows in by_section.items():
        lines += [f"## `{section}`", "", "| Full JSON path | Observed type | Meaning | Status | Source |", "|---|---|---|---|---|"]
        for row in section_rows:
            desc, status, source = meaning(row)
            lines.append("| " + " | ".join(escape_cell(x) for x in (f"`{row['path']}`", f"`{row['type']}`", desc, status, source)) + " |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="local JSON response (kept outside this repository)")
    parser.add_argument("--observed-on", default=DEFAULT_DATE, help="observation date in YYYY-MM-DD form")
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Expected a JSON object at the response root")

    raw_rows = walk(data)
    # Arrays may contain heterogeneous objects. Preserve every distinct observed
    # path/type pair while avoiding duplicate entries for repeated items.
    rows = list({(r["path"], r["type"], r["section"]): r for r in raw_rows}.values())
    rows.sort(key=lambda r: (r["section"], r["path"], r["type"]))
    catalogue = {
        "title": "Unofficial ChatGPT workspace settings response key/type catalogue",
        "observed_on": args.observed_on,
        "source_endpoint": "GET https://chatgpt.com/backend-api/accounts/{account_id}/settings",
        "scope_note": "One observed response only; no observed values are included. Null and empty collections do not establish hidden types.",
        "path_convention": "JSONPath-like bracket notation; [] means an array item; * normalizes role-like object keys to prevent identifier disclosure.",
        "entries": [{"path": r["path"], "type": r["type"]} for r in rows],
    }
    (ROOT / "catalogue.json").write_text(json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "REFERENCE.md").write_text(render_reference(rows, args.observed_on), encoding="utf-8")
    example = {
        "notice": "ILLUSTRATIVE EXAMPLE ONLY. No observed values are reproduced. Null and empty collections use placeholder strings; some example values therefore do not match the catalogue type. Role-ID map keys are redacted.",
        "response": illustrative(data),
    }
    (ROOT / "example-response.json").write_text(json.dumps(example, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} path/type entries to catalogue.json and REFERENCE.md; wrote example-response.json.")


if __name__ == "__main__":
    main()
