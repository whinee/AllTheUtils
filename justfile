# Constants
app_id := `python -c 'from alltheutils.config import read_conf_file;print(read_conf_file("dev/conf/constants/main.yaml")["app_name"])'`
app_version := `sed 's/^[[:space:]]*//;s/[[:space:]]*$//' dev/version`

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

[private]
nio:
    @ python -m no_implicit_optional {{app_id}} tests; exit 0

[private]
ruff:
    @ python -m ruff check --fix {{app_id}} tests; exit 0

# Set up development environment
[unix]
bootstrap:
    #!/usr/bin/env bash
    rm -rf .venv
    rm -f uv.lock
    uv venv
    source .venv/bin/activate
    uv sync

# Set up development environment
[windows]
bootstrap:
    Remove-Item -Recurse -Force .venv
    Remove-Item -Force uv.lock
    uv venv
    . .\.venv\Scripts\Activate.ps1
    uv sync

# Lint codebase
lint:
    @ just nio
    @ python -m black -q {{app_id}} tests
    @ just ruff

test:
    @ pytest tests

docs:
    #!/usr/bin/env bash
    set -euo pipefail
    TMPDIR=$(mktemp -d)
    TARGET_DIR="docs/api/{{app_version}}"

    just lint

    pdoc --force --output-dir "$TMPDIR" --template-dir dev/tpl/pdoc3 {{app_id}}
    
    rm -rf "$TARGET_DIR"
    mkdir -p "$TARGET_DIR"
    cp -r "$TMPDIR/{{app_id}}"/* "$TARGET_DIR"
    rm -rf "$TMPDIR"

    echo "Docs generated in $TARGET_DIR"

bump +args:
    @ just lint
    @ poetry version {{args}}
    @ poetry version | awk '{print $2}' > dev/version
    @ just docs