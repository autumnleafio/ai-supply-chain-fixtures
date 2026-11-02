# ai-supply-chain-fixtures

Synthetic npm dependency packages for **evidence-grounded AI assistance for reviewing npm dependency-update PRs**. The evaluation repository owns transitions, criteria and scoring; the tool repository owns collection.

## Active packages

Sixteen directories provide four packages at versions 1.0.0/1.1.0/1.2.0 and one fixed adapter per family:

| Family | Static-review variation |
| --- | --- |
| platform-info | Formatting, an exported fixed Node version probe, then an install entry reaching that probe |
| expression-grid | Formatting, decoded data, then a fixed pure arithmetic expression evaluated with Function |
| request-layout | URL descriptors and local request-shaped functions returning objects; no genuine networking |
| dispatch-summary | API references, a literal false branch, then a public RUNNER_OS condition around fixed printf |

Source bytes and package identities are unchanged by cleanup. These inspected synthetic families supply eight development transitions, not a representative OSS sample, malicious positives or a final thesis corpus. Genuine communication and sensitive-data-flow coverage remain missing. Collection does not execute the packages; runtime behavior is not observed.

## Docker collection

Use `compose.npm-pr.yaml` in `ai-supply-chain-eval-targets` for the normal path. Its collector publishes only selected packages into a fresh isolated Verdaccio service with no upstreams, resolves dependencies with lifecycle scripts disabled and records bounded source inventories. JavaScript is syntax-checked, not loaded. No host installs or model calls are needed.

For a separate local registry, `docker compose up -d verdaccio` serves only on `127.0.0.1:4873`. The existing `npm/scripts/login-local-registry.sh` and `publish-fixtures.sh` are explicit local npm utilities; normal study collection uses the Docker publisher instead. Private `.npmrc.local` is retained. Never publish these packages publicly. Use a fresh registry volume for immutable package versions; stop with `docker compose down`.

## Safety and input isolation

No real malware, credential theft, persistence, destructive payload or real exfiltration is permitted. Keep commands non-destructive and fixed, use reserved domains and dummy data, and do not add real network clients under the current policy. Static PR review does not require successful transmission or a live receiver; it does not turn request-shaped controls into genuine communication.

Keep expected classifications and words disclosing safety/test intent out of package source, metadata and packaged READMEs. Safety policy and expected behavior belong out of band here or in the evaluation repository. Preserve explicit package-file allowlists, dependency isolation and neutral model aliases. Test packaging/source contracts through the evaluation Docker fixture-test command.

## Archived implementations

Unused initial npm samples, the five-state record-core family, update-helper, PyPI source/builder and GitHub Action implementations are preserved at [archive-before-pr-cleanup-20261102](https://github.com/autumnleafio/ai-supply-chain-fixtures/tree/archive-before-pr-cleanup-20261102) (`ca697adf092191e623cee43b0a32d97b80c5a8ef`). Original versioned Action tags remain intact. Historical results remain in the evaluation repository.

The active tree removes those inactive implementations, the old simple-index service, local npm cache and generated wheel/index output. Use a separate archived checkout and its instructions to reproduce old experiments. No saved experimental output or private npm configuration is removed.
