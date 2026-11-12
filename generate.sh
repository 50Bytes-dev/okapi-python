#!/bin/bash
# Regenerates okapi_python from the gateway's schema, ../okapi/static/api/spec.yml.
set -euo pipefail
source .venv/bin/activate

SPEC=../okapi/static/api/spec.yml
# Hand-written modules of the package: kept across a regeneration.
KEEP=(webhooks.py)

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for f in "${KEEP[@]}"; do
    if [ -f "./okapi_python/$f" ]; then cp "./okapi_python/$f" "$work/$f"; fi
done

openapi-python-client generate --custom-template-path=./templates --path "$SPEC" --overwrite --meta uv --output-path generated
rm -rf ./okapi_python
mv ./generated/okapi_client ./okapi_python
rm -rf ./generated

for f in "${KEEP[@]}"; do
    if [ -f "$work/$f" ]; then cp "$work/$f" "./okapi_python/$f"; fi
done
