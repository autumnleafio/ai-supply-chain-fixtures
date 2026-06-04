#!/usr/bin/env sh
set -eu

export REGISTRY_URL="${REGISTRY_URL:-http://localhost:4873}"
export NPM_USER="${NPM_USER:-fixture-user}"
export NPM_PASSWORD="${NPM_PASSWORD:-fixture-password}"
export NPM_EMAIL="${NPM_EMAIL:-fixture@example.invalid}"
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"

export HOME="${NPM_HOME:-$REPO_ROOT/.npm-home}"
export NPM_CONFIG_USERCONFIG="${NPM_CONFIG_USERCONFIG:-$REPO_ROOT/.npmrc.local}"
mkdir -p "$HOME"

python3 - <<'PY'
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

registry_url = os.environ["REGISTRY_URL"].rstrip("/")
user = os.environ["NPM_USER"]
password = os.environ["NPM_PASSWORD"]
email = os.environ["NPM_EMAIL"]
userconfig = Path(os.environ["NPM_CONFIG_USERCONFIG"])

payload = {
    "name": user,
    "password": password,
    "email": email,
    "type": "user",
    "roles": [],
}
endpoint = f"{registry_url}/-/user/org.couchdb.user:{urllib.parse.quote(user, safe='')}"
request = urllib.request.Request(
    endpoint,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PUT",
)
with urllib.request.urlopen(request, timeout=30) as response:
    body = json.loads(response.read().decode("utf-8"))

token = body.get("token")
if not token:
    raise SystemExit(f"Verdaccio did not return an auth token: {body}")

parsed = urllib.parse.urlparse(registry_url)
auth_key = f"//{parsed.netloc}{parsed.path.rstrip('/')}/:_authToken"
userconfig.write_text(
    "registry={registry}/\n"
    "@ai-supply-chain-fixtures:registry={registry}/\n"
    "{auth_key}={token}\n".format(registry=registry_url, auth_key=auth_key, token=token),
    encoding="utf-8",
)
print(f"Wrote npm auth config to {userconfig}")
PY
