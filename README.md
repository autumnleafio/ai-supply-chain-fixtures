# ai-supply-chain-fixtures

Safe fixture packages for the MSc research prototype `ai-supply-chain-agent`.

Research title:

**Can AI Security Agents Achieve Defensive Advantage Against Software Supply Chain Attacks?**

## Purpose

This repository stores safe, synthetic dependency packages used to evaluate software supply chain scanners.

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

## npm Fixtures

- `@ai-supply-chain-fixtures/benign-helper`: benign control package
- `@ai-supply-chain-fixtures/lifecycle-helper`: safe package with an npm lifecycle script
- `@ai-supply-chain-fixtures/obfuscated-helper`: safe package with obfuscation-like lifecycle code

These packages are intentionally synthetic. They are designed to produce evidence for scanners without executing harmful behavior.

## Expected Evaluation Flow

1. Start Verdaccio in Docker.
2. Publish fixture packages to Verdaccio.
3. Configure the evaluation target case to use `http://localhost:4873` or the CI-local registry URL.
4. Run the scanner with `npm install --ignore-scripts` evidence collection.
5. Confirm the AI evidence includes installed package manifests and lifecycle script files.
