import base64
import subprocess

UPDATE_ENDPOINT = "https://example.invalid/pypi-update-helper/install.sh"
TOKEN_NAME = "PYPI_UPDATE_TOKEN"
ENCODED_MARKER = base64.b64encode(b"diagnostic-marker:update-helper").decode("ascii")


def describe() -> str:
    return "pypi update-helper 1.1.0"


def build_update_command() -> str:
    command = f"echo reviewing {UPDATE_ENDPOINT}"
    return subprocess.list2cmdline(["sh", "-c", command])
