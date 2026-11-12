#!/bin/bash
# Regenerates okapi_python from the gateway's schema, ../okapi/static/api/spec.yml.
set -euo pipefail
source .venv/bin/activate

SPEC=../okapi/static/api/spec.yml
# Hand-written modules of the package: kept across a regeneration.
KEEP=(webhooks.py)

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

# Each event (LoginUpdatedEvent, ...) is allOf EventEnvelope and its own `type` (a const) and `data`. The generator
# cannot merge the envelope's `type: string` with a const (it drops the event), and of two `data` objects it keeps
# the envelope's empty one. Both events narrow the envelope, so dropping the `type` keyword of the envelope's `type`
# and `data` changes no accepted body and lets each event keep its own.
python - "$SPEC" "$work/spec.json" <<'EOF'
import json
import sys

from ruamel.yaml import YAML

spec = YAML(typ="safe").load(open(sys.argv[1]))
envelope = spec["components"]["schemas"]["EventEnvelope"]["properties"]
for name in ("type", "data"):
    envelope[name].pop("type", None)
json.dump(spec, open(sys.argv[2], "w"))
EOF

for f in "${KEEP[@]}"; do
    if [ -f "./okapi_python/$f" ]; then cp "./okapi_python/$f" "$work/$f"; fi
done

openapi-python-client generate --custom-template-path=./templates --path "$work/spec.json" --overwrite --meta uv --output-path generated
rm -rf ./okapi_python
mv ./generated/okapi_client ./okapi_python
rm -rf ./generated

for f in "${KEEP[@]}"; do
    if [ -f "$work/$f" ]; then cp "$work/$f" "./okapi_python/$f"; fi
done
