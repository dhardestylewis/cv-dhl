# Tech Holding provenance audit

## Finding

The available evidence establishes that Tech Holding received an application on March 7, 2026 and later stated an intention to retain Daniel's resume in its talent database. It does not identify the uploaded file, résumé version, checksum, upload timestamp, or profile state. Do not name any document as Tech Holding's retained résumé without new direct evidence.

## Evidence chain

| Date | Source ID | Direct evidence | Proves | Does not prove |
| --- | --- | --- | --- | --- |
| 2026-03-07 | `gmail_techholding_application_receipt_19cca1b771f97069` | "Thanks for applying to Tech Holding. Your application has been received." | An application was received. | Submitted résumé, cover letter, or profile data. |
| 2026-04-23 | `gmail_techholding_retention_19dbc4e648a8faa5` | "I'd like to express our interest in retaining your resume within our talent database." | A recruiter stated intent to retain a résumé. | File identity, contents, or current availability. |
| 2026-10-15 | `linkedin_pdf_v10` | Historical export created at 17:42:44 EDT. | October profile text: Worldcastr, Summit through August 2025, SPC through September 2026. | Live profile or March application profile. |
| 2026-10-15 | `public_cv_dlewis_20251117_checked_20261015` | Current URL serves Homecastr November 2024-Present and Summit November 2023-Present. | Current public document text. | That it was served in March or retained by Tech Holding. |

## Claim comparison

| Topic | Earlier or public presentation | Later profile presentation | Audit treatment |
| --- | --- | --- | --- |
| UT Austin teaching | v01-v06: January-May 2018 and August-December 2020. Current public CV: January 2018-December 2020. | v07-v10: January 2018-December 2020. | Preserve both. Obtain course or department records before stating continuity as fact. |
| Homecastr | Current public CV: November 2024-Present. | v08-v09: September 2025-Present. v10: not listed. | Keep dates distinct. They may describe different milestones only if Daniel confirms definitions. |
| Summit Geospatial | Current public CV: November 2023-Present. | v08-v10: November 2023-August 2025. | Treat both as documented presentations. Do not invent an explanation. |
| Worldcastr | Current public CV: not listed. | v10: December 2025-Present. | October export is not evidence of the March application state. |

## Truthful reconciliation options

1. Verify UT Austin terms from a course or department record, then confirm the intended milestone definitions for Homecastr and Summit.
2. If a clarification is needed after verification, distinguish historical presentation from the verified record: "The archived profile export displays [exact date text]. The supporting record shows [verified fact]."
3. If the application record matters, request a candidate-portal export or submission receipt that identifies filename, upload time, and attachment metadata. Do not assert that a public CV or local file is the retained résumé.
4. Preserve `Present` only as quoted source text. It is not an inferred future end date.

## Account exposure checked

- Gmail connector-authenticated: daniel@summitgeospatial.com, danielhardestylewis@gmail.com, dl3645@columbia.edu, and daniel@worldcastr.com.
- Superhuman account listing: daniel@worldcastr.com only, marked primary.
- Tech Holding correspondence is accessible in the Worldcastr-connected Gmail account. Messages addressed to daniel@homecastr.com do not establish a separately connected Homecastr mailbox.

See `profile-claim-ledger-v1.json` for source IDs, exact text, evidence types, timestamp provenance, confidence, and explicit unknowns.
