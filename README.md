# AICTE APAAR Student Verification & Sanctioned Intake Portal

An interactive regulatory compliance prototype for AICTE-approved technical institutions, built around the 12-digit **APAAR / Academic Bank of Credits (ABC)** identifier ecosystem.

## Core Capabilities Demonstrated
- **12-Digit APAAR Format & Sandbox ABC Verification:** Validates 12-digit numeric identifiers, catches missing mandatory roster fields, and routes anomalies to an interactive Exception Queue.
- **UGC 2022 Concurrent Enrolment Classifier:** Distinguishes between exact duplicate submissions (rejected), allowed dual-degree combinations (Physical + ODL/Online, or two Physical programmes with non-overlapping timetables), and Ph.D. exclusions requiring human review.
- **Programme-Level Sanctioned Intake Monitoring:** Evaluates valid regular admissions against programme-level sanctioned caps for the active academic year while isolating supernumerary categories (`PMSSS`, `NRI`, `OCI`, `Foreign National`) and unresolved exception rows.
- **DPDP Act 2023 Section 6 Student Consent Lock:** Enables students to lock/unlock third-party credential verification access and logs blocked verification attempts.
- **Tamper-Evident SHA-256 Hash Chain:** Records statutory mutations (batch uploads, case adjudications, consent changes, credit transfers, and draft show-cause notices) in a verifiable SHA-256 hash-linked audit log.

- AICTE APAAR Student Verification & Sanctioned Intake Platform
1. Project Summary Description
The AICTE APAAR Student Verification & Sanctioned Intake Portal is a national-scale regulatory compliance and data management platform designed for AICTE-approved technical institutions, central regulators, and student citizens. Built around India’s Automated Permanent Academic Account Registry (APAAR) and the Academic Bank of Credits (ABC) ecosystem, the platform automates real-time verification, cross-institution duplicate detection, programme-level intake monitoring, and tamper-evident cryptographic auditing.

2. Background & Problem Statement
Higher and technical education in India historically suffered from fragmented, paper-based student tracking and isolated institutional databases. This fragmentation introduced critical systemic vulnerabilities:

  Duplicate Admissions & Ghost Students: Students simultaneously occupying seats across multiple colleges or universities without detection, artificially inflating enrolment numbers and draining state resources.

  Intake Cap Violations: Institutions admitting students beyond their AICTE-approved sanctioned intake capacities, leading to compromised educational standards and regulatory breaches.

  Credential Fraud & Verification Delays: Employers and background verification agencies relying on slow, manual processes to verify degree authenticity, leaving room for forged credentials.

  Data Privacy & Consent Gaps: A lack of granular student control over who accesses their academic lifecycle data, conflicting with modern data privacy mandates like the Digital Personal Data Protection (DPDP) Act, 2023.

3. Novelty & Key Innovations of the Solution
The platform introduces several architectural and algorithmic innovations to solve these national challenges:

  Automated UGC 2022 Concurrent Enrolment Engine: Unlike legacy systems that flag all repeated IDs as outright fraud, our rule engine parses dual-enrolment scenarios against official UGC guidelines—automatically separating exact duplicates (rejected), allowed dual-degree pathways (Physical + ODL/Online or non-overlapping physical classes), and Ph.D. exceptions requiring human review.

  Programme-Level Sanctioned Intake & What-If Simulator: Moves beyond blunt, college-wide headcount caps by evaluating admissions per individual discipline and academic year. It isolates supernumerary quotas (PMSSS, NRI, OCI, Foreign National) from regular intake counts and provides administrators with real-time capacity utilization analytics.

  Tamper-Evident SHA-256 Cryptographic Hash Chain: Implements an append-only, hash-linked audit ledger for all statutory mutations (batch uploads, case resolutions, consent toggles, and inter-university credit transfers). Any unauthorized modification to historical records invalidates subsequent cryptographic pointers, ensuring absolute accountability.

  DPDP-Compliant Student Consent Lock & Live Alerts: Empowers students with total ownership over their data via a consent lock mechanism. When locked, third-party verification requests are restricted, and automated alerts dispatch live sandbox notifications to the student's registered mobile device whenever their credentials are queried.

  Explainable Case Adjudication Desk: Provides regulators and institution admins with structured exception queues, automated provenance passports, and evidence trails to resolve flagged discrepancies transparently.

## Sandbox Scope & Architecture Note
This repository runs as a self-contained client-side sandbox (`localStorage` persistence + simulated ABC verification adapter) for rapid evaluation via the **Demo Control Bar**. Reference PostgreSQL DDL and FastAPI service blueprints are included in the System Blueprint view (`seed_data.py` and `src/data/seedData.ts`).

## Local Setup & Verification
```bash
npm install
npm run dev      # Launch interactive portal at http://localhost:3000
npm test         # Execute unit tests via tsx --test
npm run lint     # Run TypeScript strict type-checking
```
