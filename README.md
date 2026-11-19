# ChatGPT workspace settings response: unofficial reference

This repository documents the JSON keys and observed JSON types in **one** response saved on November 19, 2026 from:

```text
GET https://chatgpt.com/backend-api/accounts/{account_id}/settings
```

It is an unofficial, point-in-time observation. It is not an OpenAI API contract, a complete list of backend settings, or a description of every workspace or account. The response was supplied locally by the repository owner; the raw response is not included here.

## What is included

- [Browsable key reference](REFERENCE.md), grouped by top-level response section.
- [Machine-readable path and type catalogue](catalogue.json).
- [Illustrative sanitized response](example-response.json). It replaces every observed value with examples or explicit null/empty-collection placeholder strings; consult the catalogue for observed JSON types.
- [`tools/generate_catalogue.py`](tools/generate_catalogue.py), a standard-library Python script for regenerating the catalogue, reference, and illustrative example from a local response.

## Reading the reference

Paths use a JSONPath-like form: `$["section"]["field"]`; `[]` means an item of an array. Object properties whose names match the observed workspace role-ID form are normalized to `*` so the generated public material cannot disclose role IDs. This normalization applies to paths and example data; ordinary field names are preserved.

Types describe the values present in this one saved response. `null` means only that the observed value was null; it does not reveal the intended type. Likewise, an empty object or array shows only that the collection had no entries in this response. Array item paths describe the item shape seen when items were present.

The meaning label is one of:

- **Confirmed** — the broad meaning is supported by the linked official documentation; this does not confirm undocumented backend semantics.
- **Inferred from name** — a plausible reading of the identifier, not a verified product behavior.
- **Unknown** — the response name and available documentation do not establish what the field does.

A `false` value in a settings response does not prove that an administrator deliberately disabled a feature. Values can reflect defaults, eligibility, rollout state, inheritance, or other server logic. This reference intentionally does not publish any observed values.

## Scope and privacy

The catalogue contains paths and JSON value types only. The example uses clearly illustrative values and explicit placeholder strings for observed nulls and empty collections, and substitutes dynamic role keys. Its placeholder values may not have the observed JSON type; use `catalogue.json` for types. It excludes the source response's workspace/account identifiers, role IDs and membership data, names, emails, domains, tokens, organization-specific policy values, and actual settings values. The source file must remain outside this repository. Local response files are ignored by `.gitignore`.

Do not commit a raw response, even if it appears to contain only settings. Before publishing regenerated files, review the diff for identifiers and organization-specific data.

## Not local Codex configuration

These are server-side workspace/account response fields. They are distinct from local Codex client configuration such as `~/.codex/config.toml`, which controls behavior on a device or client. A server response key with a similar name is not thereby a supported `config.toml` key, and local configuration is not a substitute for workspace administration.

The observed response included `windows_computer_use`. The installed client on Windows checks this key. No equivalent Mac key has been verified; this repository makes no claim about one.

## Provenance and limitations

The provenance is the locally saved JSON response and its recorded observation date, November 19, 2026. The endpoint is an internal web backend endpoint and is not presented here as a supported public API. The observation is not a claim about defaults or admin intent. Null and empty values do not establish hidden schema types, and the absence of a key does not show that the setting is unsupported.

The reference links only to public official documentation that provides useful context for workspace settings, role-based access control, and client configuration. Those documents do not define this response's complete schema. Meaning labels are deliberately conservative.

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

The script overwrites `catalogue.json`, `REFERENCE.md`, and `example-response.json`. It does not upload or transmit the input. Inspect all generated diffs before committing.

This repository is an independent community reference and is not affiliated with or endorsed by OpenAI.
