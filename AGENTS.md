# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Role

This repository contains safe fixture packages and GitHub Action fixtures for software supply chain security research.

It is not the scanner repository and not the evaluation target repository.

## Safety Rules

All fixtures must be safe and inert.

- Do not add real malware, credential theft, destructive payloads, persistence, or real exfiltration.
- Use placeholder domains such as `example.invalid`.
- Suspicious-looking code must be clearly synthetic and non-harmful.
- Do not publish fixture packages to public npm or PyPI registries.
- Do not use GitHub Action fixtures in production workflows.

## Evaluation-Input Isolation

Keep ground-truth safety labels out of files that can be packaged, published, downloaded, or collected as scanner evidence.

- Do not put words such as `safe`, `benign`, `inert`, `fixture`, `test`, or `research-only` in package/action source, lifecycle scripts, package metadata, wheel metadata, action metadata, or packaged README files when they reveal the expected assessment.
- Document safety and expected behavior in repository-level `README.md`, `AGENTS.md`, or other out-of-band review documentation.
- Enforce safety through implementation choices: reserved domains, no real network/exfiltration behavior, no destructive operations, and non-executing evidence collection.
- Preserve the intended observable risk signals without explanatory comments that tell scanners or models how to classify them.

## Local Environment Rules

Prefer Docker-based local fixture workflows.

- Use Verdaccio through `compose.yaml` for npm registry simulation.
- Use the local PEP 503 simple index under `pypi/public/` for PyPI fixture wheels.
- Do not install global npm or Python packages on the host unless explicitly requested.
- Do not commit generated registry storage, generated package indexes, package tarballs, wheels, or `node_modules/`.
- Keep generated PyPI wheels byte-for-byte reproducible. Use fixed archive timestamps, permissions, entry ordering, and uncompressed entries so repeated builds of unchanged fixture inputs produce the same SHA256 without depending on zlib output.

## Repository Structure

- `compose.yaml`: local fixture services for Verdaccio and PyPI simple index
- `verdaccio/config.yaml`: Verdaccio configuration
- `npm/packages/`: npm fixture packages
- `npm/scripts/publish-fixtures.sh`: publishes npm fixtures to the local registry
- `pypi/packages/`: PyPI fixture source definitions
- `pypi/scripts/build-simple-index.py`: builds local PyPI wheel fixtures and simple index output
- `github-actions/`: GitHub Action fixtures referenced by evaluation workflows
- `tests/`: fixture build reproducibility tests

## Development Commands

Run fixture tests with:

```bash
PYTHONPYCACHEPREFIX=/tmp/python-cache python3 -m unittest discover -s tests
```

## Research Design

The evaluation target repository should depend on these fixtures through local registries or external GitHub Action references. This keeps dependency source code outside the target repository while preserving reproducible, safe supply chain scenarios.

Current fixture categories:

- npm packages resolved from local Verdaccio, including versioned update-trigger fixtures
- PyPI wheels resolved from a local simple index, including versioned update-trigger fixtures
- GitHub Actions referenced with `uses: autumnleafio/ai-supply-chain-fixtures/...@ref`, including versioned update-trigger fixtures
