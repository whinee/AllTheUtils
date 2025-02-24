# Constants

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

[private]
nio:
    @ python -m no_implicit_optional alltheutils tests; exit 0

[private]
ruff:
    @ python -m ruff check --fix alltheutils tests; exit 0

# Set up development environment
[unix]
bootstrap:
    #!/usr/bin/env bash
    rm -rf poetry.lock
    poetry install --with dev

# Lint codebase
lint:
    @ just nio
    @ python -m black -q alltheutils tests
    @ just ruff
