# Title: Dassault Systèmes DELMIA Apriso Code Injection (CWE-94) — Active Exploitation

**CVE ID:** CVE-2025-6204

## Quick Summary
An Improper Control of Generation of Code (Code Injection) vulnerability in Dassault Systèmes DELMIA Apriso affects releases from 2020 through 2025 and can allow arbitrary code execution.
The issue is listed in CISA’s Known Exploited Vulnerabilities (KEV) catalog with active exploitation noted; vendor CVSS v3.1 rates it **High (8.0)** with network vector and changed scope.

## Severity
**High** — CVSS 3.1 base score **8.0** (AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H)

## Confidence
**High** — corroborated by vendor advisory and CISA KEV entry.

## Exploitation Status
Active exploitation (CISA KEV).
ExploitDB: No results found.

## Search Commands
`searchsploit DELMIA Apriso code injection`
`searchsploit "Dassault Systèmes CVE-2025-6204 injection exploit"`

## Recommended Next Steps
* Identify and inventory all DELMIA Apriso instances; confirm if they fall within affected ranges (Release 2020 Golden–SP4; 2021 Golden–SP3; 2022 Golden–SP3; 2023 Golden–SP3; 2024 Golden–SP1; 2025 Golden–SP1).
* Apply vendor mitigations/updates per advisory immediately; follow **BOD 22-01** guidance for cloud deployments and prioritize remediation by **2025-11-18**.
* Restrict exposure (limit network access, enforce least privilege), and monitor for signs of compromise (e.g., unexpected code execution, unusual persistence, or crypto-miner activity).
* If mitigations/patches are unavailable, consider temporary service disablement or discontinuation until a fix is in place.

## Sources
* [https://www.3ds.com/trust-center/security/security-advisories/cve-2025-6204](https://www.3ds.com/trust-center/security/security-advisories/cve-2025-6204)
* [https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-6204](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-6204)
* [https://nvd.nist.gov/vuln/detail/CVE-2025-6204](https://nvd.nist.gov/vuln/detail/CVE-2025-6204)

**Written by:** Reporter Agent
