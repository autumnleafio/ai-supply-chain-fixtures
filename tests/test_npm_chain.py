from pathlib import Path
import json
import re
import unittest


PACKAGES = Path(__file__).resolve().parents[1] / "npm/packages"
SCOPE = "@ai-supply-chain-fixtures/"


class NpmChainPackageTests(unittest.TestCase):
    def test_versions_and_dependency_contract_are_fixed(self):
        adapter = json.loads((PACKAGES / "record-adapter/package.json").read_text())
        self.assertEqual(adapter["version"], "1.0.0")
        self.assertEqual(adapter["dependencies"], {SCOPE + "record-core": "^1.0.0"})
        for minor in range(5):
            package = json.loads((PACKAGES / f"record-core-1.{minor}.0/package.json").read_text())
            self.assertEqual(package["name"], SCOPE + "record-core")
            self.assertEqual(package["version"], f"1.{minor}.0")
            self.assertNotIn("dependencies", package)
            self.assertEqual("postinstall" in package.get("scripts", {}), minor in (2, 3))

    def test_matched_states_preserve_normal_function_and_helper(self):
        sources = [(PACKAGES / f"record-core-1.{minor}.0/index.js").read_text()
                   for minor in range(1, 5)]
        self.assertTrue(all(source == sources[0] for source in sources))
        active = (PACKAGES / "record-core-1.3.0/postinstall.js").read_text()
        uninvoked = (PACKAGES / "record-core-1.4.0/postinstall.js").read_text()
        self.assertEqual(active, uninvoked + "\ninitialize();\n")
        self.assertNotIn("postinstall", json.loads(
            (PACKAGES / "record-core-1.4.0/package.json").read_text()).get("scripts", {}))

    def test_packaging_excludes_ground_truth_and_network_clients(self):
        directories = [PACKAGES / "record-adapter"] + [
            PACKAGES / f"record-core-1.{minor}.0" for minor in range(5)]
        labels = re.compile(r"\b(?:safe|benign|inert|fixture|test|research-only)\b", re.I)
        for directory in directories:
            package = json.loads((directory / "package.json").read_text())
            self.assertNotIn("README.md", package["files"])
            for filename in package["files"]:
                source = (directory / filename).read_text()
                self.assertIsNone(labels.search(source), directory.name)
                self.assertNotRegex(source, r"\bfetch\s*\(|\bhttps?\.(?:request|get)\s*\(")
                self.assertNotRegex(source, r"process\.env\.(?:TOKEN|SECRET|PASSWORD)")
            metadata = json.dumps({k: v for k, v in package.items() if k != "name"})
            self.assertIsNone(labels.search(metadata), directory.name)


if __name__ == "__main__":
    unittest.main()
