# AGENTS.md

Maintain documentation in English. Preserve frozen research artifacts/model responses in their original form.

This repository owns npm dependency implementations for the PR-review study. Evaluation transitions/criteria belong in `ai-supply-chain-eval-targets`; scanner code belongs in `ai-supply-chain-agent`.

## Safety and evidence

- No malware, credential theft, persistence, destructive behavior or real exfiltration. Use dummy data, reserved domains, fixed non-destructive commands and no real network clients under the current safety policy.
- Never publish to public registries or use historical Action specimens in production.
- Keep expected classifications/safety labels out of collected package source, metadata and packaged READMEs. Document safety and intended behavior only out of band.
- Existing request-shaped functions are local descriptors, not genuine communication. No live receiver/transmission is required for static review, and this does not relax safety policy.
- Source changes require reviewing evaluation source pins and freezing a new cohort; never change frozen expectations to fit model answers. Current synthetic families are development data, not malicious positives or representative OSS.

## Active structure and local workflow

- `npm/packages/`: sixteen current package directories, four families with three versions and one adapter each.
- `compose.yaml`, `verdaccio/config.yaml`: local-only registry, no upstream registry.
- `npm/scripts/`: explicit local-registry utilities; `.npmrc.local` is private and must be preserved.
- `tests/`: package/source contracts; parse source, never import or run fixture modules.

Prefer the evaluation repository's `compose.npm-pr.yaml` collector and fixture-test service. It selects packages explicitly and uses a fresh isolated registry. Publish/install with scripts disabled; only `node --check` for syntax. No host installs, virtual environments, public publication, or committed registry data, node_modules, tarballs/caches.

## Archive boundary

`archive-before-pr-cleanup-20261102` preserves removed initial npm samples, five-state record-core/update-helper families, PyPI builder/source and GitHub Action source with original instructions. Preserve all historical Action tags. Reproduce old experiments in a separate archived checkout using their pinned refs, not by reinstating old workflows in the active tree. Regenerable npm cache and wheel/index output may be removed; saved evidence/model answers and private configuration must be retained.
