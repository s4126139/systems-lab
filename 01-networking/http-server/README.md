# HTTP Server from Scratch

## Goal

Build a minimal HTTP/1.1 server directly on TCP sockets to understand how a
request travels from a network connection to an HTTP response.

## Scope

### Supported in Week 1

- TCP listener
- Minimal request-line parsing
- HTTP response serialization
- `/`, `/health`, and fallback routes

### Deliberately unsupported in Week 1

- POST
- File serving
- Concurrency
- Keep-alive
- TLS

## Architecture

```text
Client
  -> listening socket
  -> client socket
  -> request bytes
  -> request-line parsing
  -> route selection
  -> response bytes
```

## Project configuration

This component uses `pyproject.toml` as the central configuration file for
building, installing, discovering, and testing the Python package.

### Purpose of each table

| Table | Purpose |
|---|---|
| `[build-system]` | Selects the backend used to build and install the package |
| `[project]` | Stores project metadata and runtime dependencies |
| `[project.optional-dependencies]` | Stores dependencies needed only for testing |
| `[tool.setuptools]` | Tells setuptools that packages live under `src/` |
| `[tool.setuptools.packages.find]` | Controls package discovery |
| `[tool.pytest.ini_options]` | Configures pytest test discovery |

### Current configuration

```toml
# Build and install the package with setuptools.
[build-system]
requires = ["setuptools>=77"]
build-backend = "setuptools.build_meta"

# Project metadata.
[project]
name = "systems-lab-http-server"
version = "0.1.0"
description = "A minimal HTTP/1.1 server built directly on TCP sockets"
readme = "README.md"
requires-python = ">=3.11"

# The server uses only Python standard-library modules.
dependencies = []

# pytest is needed for testing, but not for running the server.
[project.optional-dependencies]
test = [
    "pytest>=8",
]

# Importable packages are stored under src/.
[tool.setuptools]
package-dir = {"" = "src"}

# Discover http_server and its future subpackages.
[tool.setuptools.packages.find]
where = ["src"]
include = ["http_server*"]
namespaces = false

# Discover tests only in the tests directory.
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra"
```

### Key lessons

- TOML keys belong to the most recent table header. Omitting `[project]` causes
  project metadata to be interpreted as part of `[build-system]`.
- The distribution name is `systems-lab-http-server`, while the Python import
  package is `http_server`.
- `setuptools` is a build dependency, not a server runtime dependency.
- `pytest` is optional because it is needed for testing but not for running the
  server.
- `socket` and `uuid` are part of the Python standard library, so they are not
  listed in `dependencies`.
- The `src` layout separates importable code from tests and project files.
- `src/http_server/__init__.py` is required because implicit namespace packages
  are disabled.
- File names should use exact casing; the configuration references
  `README.md`, not `Readme.md`.

### Install and verify

The following commands are for Git Bash on Windows:

```bash
python -m venv .venv
./.venv/Scripts/python.exe -m pip install --upgrade pip
./.venv/Scripts/python.exe -m pip install -e '.[test]'
```

`-e` installs the package in editable mode. `.[test]` installs the project in
the current directory together with the optional `test` dependencies.

Verify that setuptools discovered the package under `src/`:

```bash
./.venv/Scripts/python.exe -c \
  "import http_server; print(http_server.__file__)"
```

The printed path should end with:

```text
src/http_server/__init__.py
```

Verify pytest:

```bash
./.venv/Scripts/python.exe -m pytest --version
```

## Known limitations

- The HTTP server implementation is not complete yet.
- The current configuration covers only packaging and testing.
- Linting, formatting, coverage, and CI are intentionally excluded from Week 1.
