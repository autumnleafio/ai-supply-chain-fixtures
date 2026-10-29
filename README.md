# ai-supply-chain-fixtures

Safe fixture packages for the MSc research prototype `ai-supply-chain-agent`.

Original project theme:

**Can AI Security Agents Achieve Defensive Advantage Against Software Supply Chain Attacks?**

Current thesis working scope: evidence-grounded pre-adoption review of npm dependencies, with extraction and output-verification effects. The evaluation repository owns the current protocol. These fixtures are non-harmful materials for controlled review, not evidence of an observed compromise or autonomous-agent advantage.

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
- Keep safety controls in this repository-level documentation and review policy.

### Evaluation-input isolation

Do not embed ground-truth labels such as `safe`, `benign`, `inert`, `fixture`, `test`, or `research-only` in package source, lifecycle scripts, package metadata, wheel metadata, GitHub Action metadata, action source, or packaged README files when those files can become scanner or model input.

Evaluated artifacts should look like ordinary dependency artifacts and expose only observable behavior. Safety is enforced by implementation: use reserved domains, avoid network clients and destructive operations, make command examples side-effect free, and keep collection non-executing. Repository-level documentation and agent instructions remain the out-of-band safety record.

After changing a fixture, search the publishable/packageable files for explanatory safety labels and verify that the intended detection signals remain without disclosing the expected assessment.

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
The wheel builder fixes ZIP timestamps, permissions, entry ordering, and uses
uncompressed ZIP entries so unchanged fixture inputs produce byte-identical
wheels without depending on zlib output.

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

- `@ai-supply-chain-fixtures/minimal-helper`: minimal control package
- `@ai-supply-chain-fixtures/lifecycle-helper`: safe package with an npm lifecycle script
- `@ai-supply-chain-fixtures/obfuscated-helper`: safe package with obfuscation-like lifecycle code
- `@ai-supply-chain-fixtures/update-helper`: versioned safe package used to model benign `1.0.0` to suspicious-looking `1.1.0` update scenarios

These packages are intentionally synthetic. They are designed to produce evidence for scanners without executing harmful behavior.

### npm dependency-chain pilot

`@ai-supply-chain-fixtures/record-adapter@1.0.0` depends on
`@ai-supply-chain-fixtures/record-core@^1.0.0` and delegates record formatting to
it. The evaluation application pins each indirect core version with npm overrides.
The six package directories contain only explicit package files; no packaged
README or explanatory classification labels are included. Existing model-facing
blinding must remove the fixture scope, package names, and repeated tarball names.

Core versions preserve the ordinary formatting function while varying context:

- `1.0.0`: initial record formatter.
- `1.1.0`: trims the formatted value.
- `1.2.0`: same formatter plus a `postinstall` script that prints the Node
  version using `execFile(process.execPath, ["--version"])`.
- `1.3.0`: same formatter plus `postinstall` with base64 decoding, `RUNNER_OS`
  access, a reserved-domain string, and a fixed `printf record-format` command.
- `1.4.0`: same formatter and the same helper function as `1.3.0`, with its
  invocation and lifecycle declaration removed.

No helper transmits data or accesses credentials. Collector validation disables
lifecycle scripts; JavaScript is syntax-checked, not imported or executed.
The default npm collector reads lifecycle source for `1.2.0` and `1.3.0`, but
omits ordinary entry sources and the unreferenced helper in `1.4.0`. The explicit
`--collect-npm-source` condition additionally captures all entry sources and that
helper in this five-state pilot, with bounded inventory/coverage records. It
does not establish helper reachability or runtime execution. These are
coverage/calibration cases, not malware labels. Expectations live in the
existing evaluation repository's `EVALUATION_EXPECTATIONS.md`.

Run the isolated Docker validation from `ai-supply-chain-eval-targets` using
`compose.npm-chain.yaml`; it publishes only these six packages into a temporary,
non-public Verdaccio service and makes no model requests. Use a fresh Compose
project/volume for each run because npm versions are immutable once published.

### GitHub Actions Fixtures

- `github-actions/indirect-action`: JavaScript action used to model indirect GitHub Actions supply chain dependency risk
- `github-actions/update-action`: versioned action used with `@update-action-v1`, `@update-action-v2`, and `@update-action-v3` refs to model external action update scenarios

This action is referenced from evaluation workflows with `uses: autumnleafio/ai-supply-chain-fixtures/github-actions/indirect-action@main`. The repository safety policy applies, and the action must not be used in production.

### GitHub Actions Update Fixtures

Use `github-actions/update-action@update-action-v1` as the baseline action. `@update-action-v2` preserves the earlier URL-only calibration state, while `@update-action-v3` adds uninvoked source paths containing `fetch()`, environment access, base64 decoding, and `childProcess.exec()`. This keeps the action path stable and changes only the Git ref. The evaluation scanner reads these refs as archives and does not execute the action. These refs must not be used in production workflows.

### PyPI Fixtures

- `ai-supply-chain-pypi-minimal-helper`: minimal control wheel
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
