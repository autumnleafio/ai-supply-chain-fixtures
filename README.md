# ai-supply-chain-fixtures

Safe fixture packages for the MSc research prototype `ai-supply-chain-agent`.

Research title:

**Can AI Security Agents Achieve Defensive Advantage Against Software Supply Chain Attacks?**

## Purpose

This repository stores safe, synthetic dependency packages and GitHub Action fixtures used to evaluate software supply chain scanners.

It is separate from:

- `ai-supply-chain-agent`: scanner/tool repository
- `ai-supply-chain-eval-targets`: evaluation target repository

The evaluation target repository should depend on packages published from this repository into a local registry. It should not vendor these package sources directly.

## Safety Policy

Fixtures must be safe and inert.

- Do not include real malware, credential theft code, destructive behavior, or real exfiltration.
- Use placeholder domains such as `example.invalid`.
- Use suspicious-looking but non-harmful behavior only for research evaluation.
- Clearly label every suspicious fixture as safe and synthetic.

## Local PyPI Simple Index

This repository also provides safe PyPI fixture wheels through a local PEP 503-style simple index.

Build the local simple index from fixture source files:

```bash
pypi/scripts/build-simple-index.py
```

Start the local PyPI index server:

```bash
docker compose up -d pypi-simple
```

The local simple index is available at:

```text
http://localhost:8080/simple
```

Scanner containers should use:

```text
http://host.docker.internal:8080/simple
```

The generated `pypi/public/` directory is local build output and is not committed.

## Local npm Registry

This repository uses Verdaccio as a Docker-based local npm registry.

Start Verdaccio:

```bash
docker compose up -d verdaccio
```

Create a local Verdaccio npm user using repository-local npm config, then publish all npm fixtures:

```bash
npm/scripts/login-local-registry.sh
npm/scripts/publish-fixtures.sh
```

The local registry is available at:

```text
http://localhost:4873
```

Stop the registry:

```bash
docker compose down
```

Remove local registry data:

```bash
docker compose down -v
```

## Fixture Packages

### npm Fixtures

- `@ai-supply-chain-fixtures/benign-helper`: benign control package
- `@ai-supply-chain-fixtures/lifecycle-helper`: safe package with an npm lifecycle script
- `@ai-supply-chain-fixtures/obfuscated-helper`: safe package with obfuscation-like lifecycle code
- `@ai-supply-chain-fixtures/update-helper`: versioned safe package used to model benign `1.0.0` to suspicious-looking `1.1.0` update scenarios

These packages are intentionally synthetic. They are designed to produce evidence for scanners without executing harmful behavior.

### GitHub Actions Fixtures

- `github-actions/indirect-action`: safe synthetic JavaScript action used to model indirect GitHub Actions supply chain dependency risk
- `github-actions/update-action`: versioned safe action used with `@update-action-v1` and `@update-action-v2` refs to model external action update scenarios

This action is referenced from evaluation workflows with `uses: autumnleafio/ai-supply-chain-fixtures/github-actions/indirect-action@main`. It is intentionally inert and should not be used in production.

### GitHub Actions Update Fixtures

Use `github-actions/update-action@update-action-v1` as the benign baseline action and `github-actions/update-action@update-action-v2` as the safe suspicious-looking update action. This keeps the action path stable and changes only the Git ref, matching a realistic external action version update. Both refs are static fixtures for archive-read evidence collection and must not be used in production workflows.

### PyPI Fixtures

- `ai-supply-chain-pypi-benign-helper`: benign control wheel
- `ai-supply-chain-pypi-import-helper`: safe import-time source fixture
- `ai-supply-chain-pypi-obfuscated-helper`: safe base64-like source fixture
- `ai-supply-chain-pypi-update-helper`: versioned safe wheel used to model benign `1.0.0` to suspicious-looking `1.1.0` update scenarios

These wheels are generated locally into `pypi/public/` and served through the local simple index.

## Expected Evaluation Flow

### npm Dependency Fixtures

1. Start Verdaccio in Docker.
2. Publish fixture packages to Verdaccio.
3. Configure the evaluation target case to use `http://localhost:4873` locally or `http://host.docker.internal:4873` from scanner containers.
4. Run the scanner with `npm install --ignore-scripts` evidence collection.
5. Confirm the AI evidence includes installed package manifests, dependency tree metadata, lifecycle script files, and update-triggered version differences where applicable.

### PyPI Dependency Fixtures

1. Build `pypi/public/` with `pypi/scripts/build-simple-index.py`.
2. Start the local PyPI simple index with `docker compose up -d pypi-simple`.
3. Configure the evaluation target case to use `http://host.docker.internal:8080/simple` from scanner containers.
4. Run the scanner with PyPI metadata collection enabled.
5. Confirm the AI evidence includes pip resolution metadata, downloaded wheel metadata/source files, and update-triggered version differences where applicable.
