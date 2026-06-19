"""Safe suspicious-looking PyPI update-helper fixture.

This fixture is intentionally inert. It contains suspicious-looking strings for
evidence extraction only; the scanner reads this file from a wheel archive and
does not import or execute it.
"""

import base64
import subprocess

PLACEHOLDER_URL = "https://example.invalid/pypi-update-helper/install.sh"
PLACEHOLDER_TOKEN_NAME = "PYPI_FIXTURE_TOKEN"
ENCODED_MARKER = base64.b64encode(b"safe research fixture only").decode("ascii")


def describe() -> str:
    return "safe research fixture: pypi update-helper 1.1.0 update scenario"


def inert_command_preview() -> str:
    command = f"echo safe research fixture only: would review {PLACEHOLDER_URL}"
    return subprocess.list2cmdline(["sh", "-c", command])
