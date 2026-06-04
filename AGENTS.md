# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Role

This repository contains safe fixture packages for software supply chain security research.

It is not the scanner repository and not the evaluation target repository.

## Safety Rules

All fixtures must be safe and inert.

- Do not add real malware, credential theft, destructive payloads, persistence, or real exfiltration.
- Use placeholder domains such as `example.invalid`.
- Suspicious-looking code must be clearly synthetic and non-harmful.
- Do not publish these packages to the public npm registry.

## Local Environment Rules

Prefer Docker-based local registry workflows.

- Use Verdaccio through `compose.yaml` for npm registry simulation.
- Do not install global npm packages on the host unless explicitly requested.
- Do not commit generated registry storage, package tarballs, or `node_modules/`.

## Repository Structure

- `compose.yaml`: local registry services
- `verdaccio/config.yaml`: Verdaccio configuration
- `npm/packages/`: npm fixture packages
- `npm/scripts/publish-fixtures.sh`: publishes fixtures to the local registry

## Research Design

The evaluation target repository should depend on these packages through a local registry. This keeps dependency source code outside the target repository while preserving reproducible, safe supply chain scenarios.
