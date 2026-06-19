"""PyPI update-helper module."""

import base64
import subprocess

PLACEHOLDER_URL = "https://example.invalid/pypi-update-helper/install.sh"
PLACEHOLDER_TOKEN_NAME = "UPDATE_HELPER_TOKEN"
ENCODED_MARKER = base64.b64encode(b"update helper marker").decode("ascii")


def describe() -> str:
    return "pypi update-helper 1.1.0"


def command_preview() -> str:
    command = f"echo would review {PLACEHOLDER_URL}"
    return subprocess.list2cmdline(["sh", "-c", command])
