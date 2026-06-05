#!/usr/bin/env python3
from __future__ import annotations

import base64
import csv
import hashlib
import json
import posixpath
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES_DIR = ROOT / "packages"
PUBLIC_DIR = ROOT / "public"
WHEELHOUSE_DIR = PUBLIC_DIR / "packages"
SIMPLE_DIR = PUBLIC_DIR / "simple"


def main() -> None:
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    WHEELHOUSE_DIR.mkdir(parents=True)
    SIMPLE_DIR.mkdir(parents=True)

    wheels: list[tuple[str, Path, str]] = []
    for fixture_path in sorted(PACKAGES_DIR.glob("*/fixture.json")):
        package_dir = fixture_path.parent
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        wheel_path = build_wheel(package_dir, fixture)
        digest = hashlib.sha256(wheel_path.read_bytes()).hexdigest()
        wheels.append((normalize_name(fixture["distribution"]), wheel_path, digest))

    for normalized_name, wheel_path, digest in wheels:
        project_dir = SIMPLE_DIR / normalized_name
        project_dir.mkdir(parents=True)
        relative_href = posixpath.relpath(
            f"/packages/{wheel_path.name}",
            f"/simple/{normalized_name}/",
        )
        (project_dir / "index.html").write_text(
            "<!doctype html>\n"
            f"<html><body><a href=\"{relative_href}#sha256={digest}\">{wheel_path.name}</a></body></html>\n",
            encoding="utf-8",
        )

    links = "\n".join(
        f'<a href="{name}/">{name}</a><br>' for name, _wheel_path, _digest in wheels
    )
    (SIMPLE_DIR / "index.html").write_text(
        f"<!doctype html>\n<html><body>{links}</body></html>\n",
        encoding="utf-8",
    )


def build_wheel(package_dir: Path, fixture: dict[str, str]) -> Path:
    distribution = fixture["distribution"]
    version = fixture["version"]
    module = fixture["module"]
    normalized_distribution = normalize_distribution(distribution)
    dist_info = f"{normalized_distribution}-{version}.dist-info"
    wheel_name = f"{normalized_distribution}-{version}-py3-none-any.whl"
    wheel_path = WHEELHOUSE_DIR / wheel_name

    entries: dict[str, bytes] = {
        f"{module}.py": (package_dir / "module.py").read_bytes(),
        f"{dist_info}/METADATA": metadata(fixture).encode("utf-8"),
        f"{dist_info}/WHEEL": wheel_metadata().encode("utf-8"),
    }
    record_path = f"{dist_info}/RECORD"
    entries[record_path] = record(entries, record_path).encode("utf-8")

    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, content in entries.items():
            archive.writestr(path, content)
    return wheel_path


def metadata(fixture: dict[str, str]) -> str:
    return (
        "Metadata-Version: 2.1\n"
        f"Name: {fixture['distribution']}\n"
        f"Version: {fixture['version']}\n"
        f"Summary: {fixture['summary']}\n"
        "License: UNLICENSED\n"
        "Classifier: Private :: Do Not Upload\n"
        "Project-URL: Research Fixture, https://github.com/autumnleafio/ai-supply-chain-fixtures\n"
        "\n"
        f"{fixture['description']}\n"
    )


def wheel_metadata() -> str:
    return (
        "Wheel-Version: 1.0\n"
        "Generator: ai-supply-chain-fixtures manual wheel builder\n"
        "Root-Is-Purelib: true\n"
        "Tag: py3-none-any\n"
    )


def record(entries: dict[str, bytes], record_path: str) -> str:
    rows: list[list[str]] = []
    for path, content in sorted(entries.items()):
        if path == record_path:
            continue
        digest = base64.urlsafe_b64encode(hashlib.sha256(content).digest()).rstrip(b"=").decode("ascii")
        rows.append([path, f"sha256={digest}", str(len(content))])
    rows.append([record_path, "", ""])

    output = []
    for row in rows:
        output.append(",".join(csv_escape(value) for value in row))
    return "\n".join(output) + "\n"


def csv_escape(value: str) -> str:
    from io import StringIO

    buffer = StringIO()
    writer = csv.writer(buffer, lineterminator="")
    writer.writerow([value])
    return buffer.getvalue()


def normalize_name(name: str) -> str:
    return name.lower().replace("_", "-").replace(".", "-")


def normalize_distribution(name: str) -> str:
    return name.replace("-", "_").replace(".", "_")


if __name__ == "__main__":
    main()
