# AICTE APAAR Student Verification & Sanctioned Intake Portal

An interactive regulatory compliance prototype for AICTE-approved technical institutions, built around the 12-digit **APAAR / Academic Bank of Credits (ABC)** identifier ecosystem.

## Core Capabilities Demonstrated
- **12-Digit APAAR Format & Sandbox ABC Verification:** Validates 12-digit numeric identifiers, catches missing mandatory roster fields, and routes anomalies to an interactive Exception Queue.
- **UGC 2022 Concurrent Enrolment Classifier:** Distinguishes between exact duplicate submissions (rejected), allowed dual-degree combinations (Physical + ODL/Online, or two Physical programmes with non-overlapping timetables), and Ph.D. exclusions requiring human review.
- **Programme-Level Sanctioned Intake Monitoring:** Evaluates valid regular admissions against programme-level sanctioned caps for the active academic year while isolating supernumerary categories (`PMSSS`, `NRI`, `OCI`, `Foreign National`) and unresolved exception rows.
- **DPDP Act 2023 Section 6 Student Consent Lock:** Enables students to lock/unlock third-party credential verification access and logs blocked verification attempts.
- **Tamper-Evident SHA-256 Hash Chain:** Records statutory mutations (batch uploads, case adjudications, consent changes, credit transfers, and draft show-cause notices) in a verifiable SHA-256 hash-linked audit log.

## Sandbox Scope & Architecture Note
This repository runs as a self-contained client-side sandbox (`localStorage` persistence + simulated ABC verification adapter) for rapid evaluation via the **Demo Control Bar**. Reference PostgreSQL DDL and FastAPI service blueprints are included in the System Blueprint view (`seed_data.py` and `src/data/seedData.ts`).

## Local Setup & Verification
```bash
npm install
npm run dev      # Launch interactive portal at http://localhost:3000
npm test         # Execute unit tests via tsx --test
npm run lint     # Run TypeScript strict type-checking
```
