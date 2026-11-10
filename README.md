# ai-supply-chain-fixtures

Synthetic npm dependency packages for **evidence-grounded AI assistance for reviewing npm dependency-update PRs**. The evaluation repository owns transitions, criteria and scoring; the tool repository owns collection.

## Active packages

Twenty-four directories provide six packages at versions 1.0.0/1.1.0/1.2.0 and one fixed adapter per family:

| Family | Static-review variation |
| --- | --- |
| platform-info | Formatting, an exported fixed Node version probe, then an install entry reaching that probe |
| expression-grid | Formatting, decoded data, then a fixed pure arithmetic expression evaluated with Function |
| request-layout | URL descriptors and local request-shaped functions returning objects; no genuine networking |
| dispatch-summary | API references, a literal false branch, then a public RUNNER_OS condition around fixed printf |
| delivery-status | An unchanged genuine node:http helper to fixed 127.0.0.1:48153/status, then a new install entry reaching it |
| session-report | Ordinary formatting preserving authorization redaction, then fixed dummy authorization data entering the existing console output |

The original sixteen package directories remain unchanged. Eight additional directories supply two new families with matched normal updates. Together they supply twelve development transitions. Genuine HTTP call/entry and dummy authorization-to-output mechanisms are now represented, with fixed loopback/dummy-value limits. They remain inspected synthetic development data, not a representative OSS sample, malicious positives or a final human-approved thesis corpus. Collection does not execute the packages; runtime behavior is not observed.

## Docker collection

Use `compose.npm-pr.yaml` in `ai-supply-chain-eval-targets` for the normal path. Its collector publishes only selected packages into a fresh isolated Verdaccio service with no upstreams, resolves dependencies with lifecycle scripts disabled and records bounded source inventories. JavaScript is syntax-checked, not loaded. No host installs or model calls are needed.

For a separate local registry, `docker compose up -d verdaccio` serves only on `127.0.0.1:4873`. The existing `npm/scripts/login-local-registry.sh` and `publish-fixtures.sh` are explicit local npm utilities; normal study collection uses the Docker publisher instead. Private `.npmrc.local` is retained. Never publish these packages publicly. Use a fresh registry volume for immutable package versions; stop with `docker compose down`.

## Safety and input isolation

No real malware, credential theft, persistence, destructive payload or real exfiltration is permitted. Keep commands non-destructive and fixed, use reserved domains and dummy data, and permit a real client only in the bounded delivery-status family: node:http, literal 127.0.0.1:48153/status, a fixed POST body, a 250 ms timeout, no external destination, no secret/environment/file input and no destination/body overrides. Do not execute that path in tests or collection. Static PR review does not require successful transmission or a live receiver; it does not turn request-shaped controls into genuine communication.

Keep expected classifications and words disclosing safety/test intent out of package source, metadata and packaged READMEs. Safety policy and expected behavior belong out of band here or in the evaluation repository. Preserve explicit package-file allowlists, dependency isolation and neutral model aliases. Test packaging/source contracts through the evaluation Docker fixture-test command.

## Archived implementations

Unused initial npm samples, the five-state record-core family, update-helper, PyPI source/builder and GitHub Action implementations are preserved at [archive-before-pr-cleanup-20261102](https://github.com/autumnleafio/ai-supply-chain-fixtures/tree/archive-before-pr-cleanup-20261102) (`ca697adf092191e623cee43b0a32d97b80c5a8ef`). Original versioned Action tags remain intact. Historical results remain in the evaluation repository.

The active tree removes those inactive implementations, the old simple-index service, local npm cache and generated wheel/index output. Use a separate archived checkout and its instructions to reproduce old experiments. No saved experimental output or private npm configuration is removed.

## Coverage extension (2026-11-10)

Each added family uses versions 1.0.0 -> 1.1.0 for a normal formatting update and 1.1.0 -> 1.2.0 for the review-oriented change. The communication helper is byte-identical in all three versions; the new behavior opportunity is the added postinstall entry, not a newly invented request call. The data family changes one field from "[redacted]" to session.authorization while preserving the same console sink and fixed demo-access-value source. Source-derived expectations and missing observation relationships are recorded in the evaluation repository's v3 cohort; no model answers informed selection.
