# Title and CVE ID

Broadcom VMware Aria Operations and VMware Tools Privilege Defined with Unsafe Actions Vulnerability — CVE-2025-41244

---

## Severity

- CVSS v3.1 Base Score: 7.8
- Base Severity: HIGH
- Vector String: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H

## Vulnerability Description

VMware Aria Operations and VMware Tools contain a local privilege escalation vulnerability. A malicious local actor with non-administrative privileges who has access to a VM with VMware Tools installed and managed by Aria Operations with SDMP enabled may exploit this vulnerability to escalate privileges to root on the same VM.

(Description sourced from MITRE/NVD and vendor advisory references.)

## Affected Products / Versions

Reported affected vendor: VMware

- VCF operations — versions: 9.0.x (status: affected; versions less than 9.0.1.0 are affected)
- VMware Tools — versions: 13.x.x.x (affected; less than 13.0.5.0) and 12.5.x (affected; less than 12.5.4)
- VMware Aria Operations — versions: 8.18.x (affected; less than 8.18.5)
- VMware Cloud Foundation — versions: 5.x, 4.x (affected; less than 8.18.5)
- VMware Telco Cloud Platform — versions: 5.x, 4.x (affected; less than 8.18.5)
- VMware Telco Cloud Infrastructure — versions: 3.x, 2.x (affected; less than 8.18.5)

(Version and product details taken from MITRE CNA affected list.)

## ExploitDB Search Results

Search queries used:

- Query: "CVE-2025-41244"
  - Result: No public exploits found (Exploits: No Results; Shellcodes: No Results)

- Query: "Broadcom VMware Aria Operations and VMware Tools Privilege Defined with Unsafe Actions Vulnerability"
  - Result: No public exploits found (Exploits: No Results; Shellcodes: No Results)

- Query: "Broadcom VMware Aria Tools Privilege Unsafe Actions"
  - Result: No public exploits found (Exploits: No Results; Shellcodes: No Results)

Summary: ExploitDB (searchsploit) returned no public exploit or shellcode entries for the queries above.

## Exploitation Status

- CISA KEV dateAdded: 2025-10-30
- Known ransomware campaign use: Unknown

Additional enrichment (CISA ADP): noted as "Exploitation: active" under ADP SSVC options in MITRE ADP metrics (see MITRE ADP references).

## Recommended Actions

Required action:
- Apply mitigations per vendor instructions, follow applicable BOD 22-01 guidance for cloud services, or discontinue use of the product if mitigations are unavailable.

Additional practical remediation steps:

1. Prioritize and apply vendor-supplied updates/patches for affected VMware Tools and Aria Operations versions as soon as available.
2. If immediate patching is not possible, disable or restrict SDMP management for VMs where practical, or limit which VMs are managed via Aria Operations to reduce exposure.
3. Enforce least-privilege on VM local accounts, restrict local login access, and audit/monitor privileged escalation attempts and sudo/authorization logs on affected systems.
4. Isolate or segment affected VMs where feasible, and implement compensating controls such as host-based intrusion detection, enhanced logging/alerting, and rapid incident response playbooks.

## Sources (unique URLs and news titles)

Extracted URLs:

- http://support.broadcom.com/group/ecx/support-content-view/-/support-content/Security%20Advisories/VMSA-2025-0015--VMware-Aria-Operations-and-VMware-Tools-updates-address-multiple-vulnerabilities--CVE-2025-41244-CVE-2025-41245--CVE-2025-41246-/36149
- https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149
- https://nvd.nist.gov/vuln/detail/CVE-2025-41244
- https://blog.nviso.eu/2025/09/29/you-name-it-vmware-elevates-it-cve-2025-41244/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-41244

Google News Articles:

- https:\/\/www.bleepingcomputer.com\/news\/security\/cisa-orders-feds-to-patch-vmware-tools-flaw-exploited-since-october-2024\/amp\/
- https:\/\/socprime.com\/blog\/cve-2025-41244-zero-day-vulnerability\/
- https:\/\/thehackernews.com\/2025\/09\/urgent-china-linked-hackers-exploit-new.html

## Relevant Tags

- Privilege Escalation
- Unsafe Actions
- Local Privilege Escalation
- CWE-267

---
Written by: Reporter Agent
--------------------------------------------------------------------------------