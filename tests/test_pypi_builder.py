from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "pypi" / "scripts" / "build-simple-index.py"
)


def load_builder():
    spec = importlib.util.spec_from_file_location("pypi_fixture_builder", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReproduciblePyPIBuilderTest(unittest.TestCase):
    def test_repeated_builds_are_byte_identical(self):
        builder = load_builder()
        temp_root = Path(tempfile.mkdtemp())
        builder.PUBLIC_DIR = temp_root / "public"
        builder.WHEELHOUSE_DIR = builder.PUBLIC_DIR / "packages"
        builder.SIMPLE_DIR = builder.PUBLIC_DIR / "simple"

        builder.main()
        first_hashes = file_hashes(builder.PUBLIC_DIR)
        builder.main()
        second_hashes = file_hashes(builder.PUBLIC_DIR)

        self.assertEqual(first_hashes, second_hashes)

        for wheel_path in sorted(builder.WHEELHOUSE_DIR.glob("*.whl")):
            with zipfile.ZipFile(wheel_path) as archive:
                for info in archive.infolist():
                    self.assertEqual(info.date_time, builder.ZIP_TIMESTAMP)
                    self.assertEqual(info.create_system, 3)
                    self.assertEqual(info.external_attr, builder.ZIP_FILE_MODE)
                    self.assertEqual(info.compress_type, zipfile.ZIP_STORED)


def file_hashes(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


if __name__ == "__main__":
    unittest.main()
