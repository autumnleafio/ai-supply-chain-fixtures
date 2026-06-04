#!/usr/bin/env sh
set -eu

REGISTRY_URL="${REGISTRY_URL:-http://localhost:4873}"
SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
PACKAGES_DIR="$SCRIPT_DIR/../packages"

export HOME="${NPM_HOME:-$REPO_ROOT/.npm-home}"
export NPM_CONFIG_USERCONFIG="${NPM_CONFIG_USERCONFIG:-$REPO_ROOT/.npmrc.local}"
mkdir -p "$HOME"

for package_dir in "$PACKAGES_DIR"/*; do
  [ -d "$package_dir" ] || continue
  echo "Publishing $(basename "$package_dir") to $REGISTRY_URL"
  npm publish "$package_dir" \
    --registry "$REGISTRY_URL" \
    --access public \
    --ignore-scripts
 done
