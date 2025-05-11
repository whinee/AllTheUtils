# Constants
app_id := `python -c 'from alltheutils.config import read_conf_file;print(read_conf_file("dev/conf/constants/main.yaml")["app_name"])'`
app_version := `sed 's/^[[:space:]]*//;s/[[:space:]]*$//' dev/version`
dev_docs := "dev/docs"
docs_api_root_dir := "docs/api"
docs_api_unreleased_dir := docs_api_root_dir + "/unreleased"

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

[private]
nio:
    @ python -m no_implicit_optional {{app_id}} tests; exit 0

[private]
ruff:
    @ python -m ruff check --fix {{app_id}} tests; exit 0

# Lint codebase
lint:
    @ just nio
    @ python -m black -q {{app_id}} tests
    @ just ruff

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

test:
    @ pytest --md-report --md-report-zeros empty --md-report-color never --md-report-output dev/docs/tests.md tests
    @ python dev/scripts/py/prepend_dev_docs_test_md.py

# Generate documentation
[unix]
docs:
    #!/usr/bin/env bash
    set -euo pipefail
    TMPDIR=$(mktemp -d)
    TARGET_DIR="{{docs_api_unreleased_dir}}"

    just lint

    pdoc --force --output-dir "$TMPDIR" --template-dir dev/tpl/pdoc3 {{app_id}} >/dev/null
    
    rm -rf "$TARGET_DIR"
    mkdir -p "$TARGET_DIR"
    cp -r "$TMPDIR/{{app_id}}"/* "$TARGET_DIR"
    rm -rf "$TMPDIR"

    erdantic alltheutils.cli.dataclasses.CommandSchema --dot | dot -Tpng -Gdpi=300 -o "{{dev_docs}}/cli/dataclasses.png"

    mkdir -p "$TARGET_DIR/dev"
    cp -r "{{dev_docs}}"/* "$TARGET_DIR/dev"

    echo "Docs generated in $TARGET_DIR"

[unix]
[confirm('Are you sure you want to bump the version? [y/N]')]
bump +args:
    #!/usr/bin/env bash
    set -euo pipefail

    just lint
    uv version --bump {{args}}
    uv version --short > dev/version
    just docs

    APP_VERSION=$(sed 's/^[[:space:]]*//;s/[[:space:]]*$//' dev/version)

    DOCS_SOURCE_DIR="{{docs_api_unreleased_dir}}"
    DOCS_TARGET_DIR="{{docs_api_root_dir}}/$APP_VERSION"

    rm -rf "$DOCS_TARGET_DIR"
    mkdir -p "$DOCS_TARGET_DIR"
    cp -r "$DOCS_SOURCE_DIR"/* "$DOCS_TARGET_DIR"

    echo "Docs generated in $DOCS_TARGET_DIR"
