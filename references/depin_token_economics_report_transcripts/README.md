# DePIN Token Economics Report Transcript Pack

This folder is for the 9-episode Fluence series:
`The DePIN Token Economics Report` (Tom Trowbridge).

Purpose:
- Keep this source separate from Onocoy-specific transcript evidence.
- Use transcripts as secondary evidence for claim discovery and hypothesis generation.
- Route thesis-critical claims to primary-source verification before final citation.

## Structure
- `raw/`: one raw transcript per episode.
- `transcript_manifest_template.tsv`: metadata tracker for ingestion and status.
- `transcript_manifest_2026-02-22.tsv`: collected 9-episode manifest from user transcript batch.
- `claim_ledger_template.csv`: claim-level extraction mapped to thesis chapters and DTSE parameters.
- `claim_ledger_2026-02-22.csv`: initial extracted claim ledger (verification pending).
- `dedup_decisions_2026-02-22.md`: canonicalization and duplicate-removal log.

## File naming convention
Use:
`YYYY-MM-DD_fluence_depin-token-economics-epXX_short-title-transcript.txt`

Example:
`2026-02-22_fluence_depin-token-economics-ep04-fiat-integration-transcript.txt`

## Transcript header format (inside each raw file)
At minimum, include:

```text
Title: ...
Series: The DePIN Token Economics Report
Episode: ...
Source: Fluence
Type: Video transcript
URL: ...
Duration: ...
Published: ...
Captured: ...
Captured by: ...
```

## Evidence policy
- Set Fluence transcript claims to `third_party_secondary` by default.
- Do not use transcript-only claims for final quantitative calibration.
- For hard claims (token supply, issuance, burn rates, adoption KPIs), add a primary-source follow-up:
  - protocol docs / whitepaper
  - on-chain contract/explorer evidence
  - timestamped dashboard exports

## Thesis alignment workflow
1. Ingest transcript into `raw/` and update manifest status.
2. Extract claims into `claim_ledger_template.csv`.
3. Map each claim to thesis chapter and DTSE parameter where relevant.
4. Add `% TODO-CITE:` tags in `.tex` while drafting.
5. Resolve tags with `REFERENCE_MAPPING.md` + verified primary sources.
