# ChatGPT workspace settings response: unofficial reference

This repository documents the JSON keys and observed JSON types in **one** response saved on November 19, 2026 from:

```text
GET https://chatgpt.com/backend-api/accounts/{account_id}/settings
```

It is an unofficial, point-in-time observation. It is not an OpenAI API contract, a complete list of backend settings, or a description of every workspace or account. The response was supplied locally by the repository owner; the raw response is not included here.

## What is included

- [Browsable key reference](REFERENCE.md), grouped by top-level response section.
- [Machine-readable catalogue](catalogue.json) with observed paths, types, curated meanings, and evidence labels.
- [Illustrative sanitized response](example-response.json). It replaces every observed value with examples or explicit null/empty-collection placeholder strings; consult the catalogue for observed JSON types.
- [`tools/generate_catalogue.py`](tools/generate_catalogue.py), a standard-library Python script for regenerating the catalogue, reference, and illustrative example from a local response.
- [`tools/field_notes.json`](tools/field_notes.json), the reviewed registry of public field paths, explanations, evidence, and dynamic role-map locations.

## Reading the reference

Paths use a JSONPath-like form: `$["section"]["field"]`; `[]` means an observed array item shape. Every property name inside a reviewed role-policy map is normalized to `*`, including built-in role keys. This protects identifiers regardless of their format. Multiple role keys and repeated array items collapse to distinct path/type pairs. Ordinary field names must appear at their exact reviewed location in the registry; an unreviewed path causes generation to stop before any output is written.

Types describe the values present in this one saved response. `null` means only that the observed value was null; it does not reveal the intended type. Likewise, an empty object or array shows only that the collection had no entries in this response. Array item paths describe the item shape seen when items were present.

The meaning label is one of:

- **Confirmed** — directly observed structure or an explicitly attributed client observation supplied by the source author. The Windows client check is an author report, not an independently reproduced result; client version and code evidence are not included.
- **Inferred from name** — a curated interpretation of the field in its parent context. Official product documentation can support the surrounding concept without verifying this internal key or its enforcement.
- **Unknown** — the response name and available documentation do not establish what the field does.

Public documentation links are labeled **product context; key mapping unverified**. Generic feature or RBAC documentation never promotes an internal field mapping to Confirmed. Source records in the catalogue distinguish `product_context`, `local_observation`, and `author_report` evidence. Opaque feature names remain unidentified. No original third-party source directly establishing these mappings was located during this review; no secondhand speculation is treated as confirmation. Sources were reviewed on November 19, 2026 and may change later.

A `false` value in a settings response does not prove that an administrator deliberately disabled a feature. Values can reflect defaults, eligibility, rollout state, inheritance, or other server logic. This reference intentionally does not publish any observed values.

## Scope and privacy

The catalogue contains reviewed field paths, types, explanations, and evidence, with no source scalar values. The example replaces strings with illustrative placeholders, numbers with synthetic numbers, booleans with a fixed synthetic value, and nulls/empty collections with explicit placeholder strings. Synthetic values can coincidentally match a source value; they do not report the workspace's actual selections. Placeholder strings may not have the observed JSON type; use `catalogue.json` for types. Actual workspace/account identifiers, role IDs, membership lists, names, emails, domains, tokens, organization instructions/URLs, policy selections, and revision markers are omitted. The source file must remain outside this repository; the CLI enforces this. Common local input filenames are also ignored by `.gitignore`.

Do not commit a raw response, even if it appears to contain only settings. Before publishing regenerated files, review the diff for identifiers and organization-specific data.

## Not local Codex configuration

These are server-side workspace/account response fields. They are distinct from local Codex client configuration such as `~/.codex/config.toml`, which controls behavior on a device or client. A server response key with a similar name is not thereby a supported `config.toml` key, and local configuration is not a substitute for workspace administration.

The observed response included `windows_computer_use`. The installed client on Windows checks this key. No equivalent Mac key has been verified; this repository makes no claim about one.

## Provenance and limitations

The provenance is the locally saved JSON response and its recorded observation date, November 19, 2026. The endpoint is an internal web backend endpoint and is not presented here as a supported public API. The observation is not a claim about defaults or admin intent. Null and empty values do not establish hidden schema types, and the absence of a key does not show that the setting is unsupported.

The reference links to official documentation for workspace controls and individual product features. Those documents do not define this response schema. Duration units, enum exhaustiveness, flag precedence, and effective permissions remain unverified unless explicitly stated otherwise.

## References

- [Managing workspace settings in ChatGPT Enterprise](https://help.openai.com/en/articles/8411955-managing-workspace-settings-in-chatgpt-enterprise) — official overview of workspace administration surfaces and controls.
- [Managing feature access with role-based access control in ChatGPT](https://help.openai.com/en/articles/11750701-managing-feature-access-with-role-based-access-control-in-chatgpt) — official explanation of workspace defaults, roles, and permission states.
- [Managing members, seat types, and roles in ChatGPT Business](https://help.openai.com/en/articles/8542216-managing-workspaces-people-and-access-in-chatgpt-business) — official overview of roles and workspace discovery.
- [Codex configuration reference](https://developers.openai.com/codex/config-reference/) — official reference for local Codex configuration, separate from server-side workspace settings.

## Regenerate from a local response

Keep the input outside the repository, then run:

```powershell
python tools/generate_catalogue.py "C:\path\to\workspace-settings.json" --observed-on 2026-11-19
```

Requires Python 3.10 or later; no third-party packages. The observation date is required explicitly to avoid accidentally dating a new response as the original snapshot.

The script overwrites `catalogue.json`, `REFERENCE.md`, and `example-response.json` only after validating every path and constructing all three artifacts. It rejects duplicate object keys and nonstandard JSON numeric constants. It does not upload or transmit the input. Unexpected paths are rejected without printing their potentially sensitive names. Dynamic role keys are never copied, even if they contain emails, domains, UUIDs, or a new identifier format.

For a new response shape, review new field names privately, then add only public schema names and curated notes to `tools/field_notes.json`. Do not add private dictionary keys to that registry. New dynamic maps need an explicit parent path and a wildcard child entry. A dynamic map with incompatible example shapes is rejected for private review. Review diffs before committing.

The catalogue examines every array item. The example preserves distinct sanitized item shapes but collapses duplicates and role-map members; it does not preserve membership counts or associations.

Run the sanitizer regression checks with:

```powershell
python -m unittest discover -s tests -v
```

This repository is an independent community reference and is not affiliated with or endorsed by OpenAI.
