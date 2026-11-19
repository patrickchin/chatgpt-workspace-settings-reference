"""Regression checks for privacy boundaries and recursive inventory behavior."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("generator", ROOT / "tools/generate_catalogue.py")
g = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(g)
DATE = "2026-11-19"


class PrivacyAndCoverageTests(unittest.TestCase):
    def test_every_role_map_redacts_arbitrary_identifier_formats(self):
        sentinels = [
            "person@example.invalid", "internal.example.invalid",
            "11111111-2222-3333-4444-555555555555", "role-v2-private-team",
            "private-token-like-key", 'private-key[\"nested\"]',
        ]
        for parent in g.DYNAMIC_MAPS:
            keys = []
            rest = parent[1:]
            while rest:
                key, end = json.JSONDecoder().raw_decode(rest[1:])
                keys.append(key)
                rest = rest[end + 2:]
            data = target = {}
            for key in keys:
                target[key] = {}
                target = target[key]
            target.update({key: "PRIVATE_POLICY_SENTINEL" for key in sentinels})
            output = "\n".join(g.generate(data, DATE).values())
            for sentinel in sentinels + ["PRIVATE_POLICY_SENTINEL"]:
                self.assertNotIn(sentinel, output)
            self.assertIn(parent + '["*"]', output)

    def test_unknown_paths_are_rejected_in_fixed_and_empty_containers(self):
        for data in [
            {"person@example.invalid": True},
            {"settings": {"person@example.invalid": "private"}},
            {"beta_settings": {"new_feature": True}},
            {"available_admin_preview_features": {"private-preview": []}},
            {"role_summaries": [{"private-metadata-key": 1}]},
        ]:
            with self.assertRaises(ValueError) as error:
                g.generate(data, DATE)
            self.assertNotIn("person@example.invalid", str(error.exception))

    def test_array_walk_and_example_include_later_item_fields(self):
        data = {"role_summaries": [{"id": "secret-a"}, {"name": "secret-b"}]}
        output = g.generate(data, DATE)
        entries = json.loads(output["catalogue.json"])["entries"]
        paths = {row["path"] for row in entries}
        self.assertIn('$["role_summaries"][]["id"]', paths)
        self.assertIn('$["role_summaries"][]["name"]', paths)
        example = json.loads(output["example-response.json"])["response"]
        self.assertEqual(len(example["role_summaries"]), 2)
        self.assertNotIn("secret-", "".join(output.values()))

    def test_mixed_array_types_and_null_type_are_observed(self):
        data = {"permissions": ["secret", None, 1, True]}
        entries = json.loads(g.generate(data, DATE)["catalogue.json"])["entries"]
        self.assertEqual({r["type"] for r in entries if r["path"] == '$["permissions"][]'}, {"string", "null", "integer", "boolean"})

    def test_dynamic_collision_with_different_shapes_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "incompatible"):
            g.generate({"beta_settings_dict": {"admin_preview_team_create": {"role-a": True, "role-b": "private"}}}, DATE)

    def test_context_links_cannot_confirm_backend_mapping(self):
        for note in g.NOTES.values():
            if note["status"] == "Confirmed":
                self.assertTrue(note["sources"])
                self.assertTrue(all(s["scope"] in {"author_report", "local_observation"} for s in note["sources"]))
        for path in ['$["beta_settings"]["canvas"]', '$["beta_settings"]["canvas_code_execution"]', '$["role_summaries"][]["assignment_sources"][]["principal_id"]']:
            self.assertEqual(g.NOTES[path]["status"], "Inferred from name")

    def test_generation_is_deterministic(self):
        a = {"permissions": ["secret-one", "secret-two"], "workspace_id": "secret-id"}
        b = {"workspace_id": "other-id", "permissions": ["other-permission"]}
        self.assertEqual(g.generate(a, DATE)["catalogue.json"], g.generate(b, DATE)["catalogue.json"])

    def test_date_must_be_explicit_canonical_iso_format(self):
        for value in ["20261119", "2026-99-99", "PRIVATE_DATE_SENTINEL"]:
            with self.assertRaises(ValueError) as error:
                g.generate({}, value)
            self.assertNotIn("PRIVATE_DATE_SENTINEL", str(error.exception))

    def test_cli_rejects_input_without_changing_outputs_or_echoing_secrets(self):
        names = ["catalogue.json", "REFERENCE.md", "example-response.json"]
        before = {name: (ROOT / name).read_bytes() for name in names}
        fixtures = [
            '{"private-person@example.invalid": true}',
            '{"workspace_id":"a","workspace_id":"b"}',
            '{"permissions": [NaN]}',
            '{"permissions": "PRIVATE_MALFORMED_SENTINEL"',
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            for content in fixtures:
                path.write_text(content, encoding="utf-8")
                result = subprocess.run([sys.executable, str(ROOT / "tools/generate_catalogue.py"), str(path), "--observed-on", DATE], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("private-person", result.stdout + result.stderr)
                self.assertNotIn("PRIVATE_MALFORMED_SENTINEL", result.stdout + result.stderr)
        self.assertEqual(before, {name: (ROOT / name).read_bytes() for name in names})

    def test_input_inside_repository_is_rejected(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools/generate_catalogue.py"), str(ROOT / "example-response.json"), "--observed-on", DATE], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("outside the repository", result.stderr)


if __name__ == "__main__":
    unittest.main()
