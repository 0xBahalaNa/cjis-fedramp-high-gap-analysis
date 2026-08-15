# CJIS v6.1 to FedRAMP High (NIST 800-53 Rev 5) - Gap Report

Generated from `data/cjis-overlay.json`. CJIS Security Policy v6.1 has been the default audit baseline since 2026-04-01.

## Summary

- **Total deltas:** 25
- **Implementation-Level Deltas:** 13
- **Control-Level Gaps:** 12

## Implementation-Level Deltas

| Control | Category | Title |
|---------|----------|-------|
| PS-3 | Personnel | CJIS v6.1 Delta — Personnel Screening |
| PS-6 | Personnel | CJIS v6.1 Delta — Access Agreements |
| IA-2 | Authentication | CJIS v6.1 Delta — Identification and Authentication |
| IA-5 | Authentication | CJIS v6.1 Delta — Authenticator Management |
| MP-6 | Media Protection | CJIS v6.1 Delta — Media Sanitization |
| SC-12 | Encryption | CJIS v6.1 Delta — Cryptographic Key Management |
| SC-13 | Encryption | CJIS v6.1 Delta — Cryptographic Protection |
| SC-28 | Encryption | CJIS v6.1 Delta — Protection of Information at Rest |
| AU-6 | Audit | CJIS v6.1 Delta — Audit Record Review |
| AC-2 | Access Control | CJIS v6.1 Delta — Account Management |
| IR-6 | Incident Response | CJIS v6.1 Delta — Incident Reporting |
| PE-17 | Physical Environmental | CJIS v6.1 Delta — Alternate Work Site |
| AT-2 | Training | CJIS v6.1 Delta — Awareness Training |

## Control-Level Gaps

| Control | Category | Title |
|---------|----------|-------|
| SI-12.1 | Privacy Retention | CJIS v6.1 — Limit PII Elements |
| SI-12.2 | Privacy Retention | CJIS v6.1 — Minimize PII in Testing, Training, and Research |
| SI-12.3 | Privacy Retention | CJIS v6.1 — Information Disposal |
| AU-3.3 | PII Limitation | CJIS v6.1 — Limit PII Elements in Audit Records |
| PE-8.3 | PII Limitation | CJIS v6.1 — Limit PII Elements in Visitor Access Records |
| AC-3.14 | PII Limitation | CJIS v6.1 — Individual Access to PII |
| SC-7.24 | PII Limitation | CJIS v6.1 — PII Processing Rules at Boundaries |
| AT-3.5 | Training | CJIS v6.1 — Role-Based Training on Processing PII |
| IR-2.3 | Training | CJIS v6.1 — Breach Response Training |
| IR-8.1 | Incident Response Planning | CJIS v6.1 — IR Plan for Breaches |
| PL-9 | Planning | CJIS v6.1 — Central Management |
| SA-8.33 | Engineering | CJIS v6.1 — Minimization as Engineering Principle |

## Control-by-Control Detail

### Implementation-Level Deltas

#### Personnel

##### PS-3 - CJIS v6.1 Delta — Personnel Screening

**FedRAMP High Baseline Requirement**

Background investigation conducted for personnel requiring access to the information system, commensurate with the risk level of the position.

**CJIS v6.1 Delta**

Fingerprint-based background check through state and national (FBI) repositories required for ALL personnel with access to CJI, regardless of position risk level. No exceptions for contractors, vendor personnel, or cloud service provider staff with logical or physical access to unencrypted CJI.

**Implementation Guidance**

Establish fingerprint submission process with the state CSA (CJIS Systems Agency). Ensure all CSP personnel with access to unencrypted CJI complete fingerprint-based checks prior to access provisioning. Maintain records of background check completion and adjudication results. Re-screening is required when personnel change roles or at intervals defined by the CSA.

**Evidence Required**

Fingerprint submission records; background check adjudication results from state/FBI repositories; personnel roster cross-referenced with CJI access list; evidence of pre-access screening completion; re-screening schedule and completion records.

##### PS-6 - CJIS v6.1 Delta — Access Agreements

**FedRAMP High Baseline Requirement**

Signed rules of behavior and acceptable use agreements required before access to the information system.

**CJIS v6.1 Delta**

CJIS Security Addendum (CSA form) must be executed by all personnel with access to CJI. The Security Addendum is a binding agreement separate from standard rules of behavior that specifically addresses CJI handling, dissemination, and sanctions for misuse.

**Implementation Guidance**

Obtain the CJIS Security Addendum template from the state CSA. Integrate addendum signing into the onboarding workflow prior to CJI access provisioning. Maintain signed addendums on file. Ensure addendums are re-executed when terms change or at intervals required by the CSA.

**Evidence Required**

Signed CJIS Security Addendum for each individual with CJI access; addendum tracking log with execution dates; evidence addendum signing occurs before CJI access is granted; re-execution records when terms are updated.

#### Authentication

##### IA-2 - CJIS v6.1 Delta — Identification and Authentication

**FedRAMP High Baseline Requirement**

Multi-factor authentication required for access to the information system per FedRAMP High baseline.

**CJIS v6.1 Delta**

Advanced Authentication required for CJI access: AAL2 (per NIST SP 800-63-3) phishing-resistant multi-factor authentication. Must use two of: something you know, something you have, something you are. Advanced Authentication is mandatory when accessing CJI from outside a physically secure location or over any network.

**Implementation Guidance**

Deploy AAL2-compliant MFA for all CJI access paths. Phishing-resistant authenticators (FIDO2/WebAuthn, PIV/CAC, or hardware tokens) are preferred. Software OTP tokens meet AAL2 minimum but do not satisfy phishing-resistance. Ensure MFA is enforced at the application layer, not just the network perimeter. Document which authenticator types are used and their AAL level.

**Evidence Required**

MFA configuration screenshots/exports; authenticator type inventory and AAL classification; authentication policy documentation specifying CJIS Advanced Authentication requirements; logs demonstrating MFA enforcement for CJI access; network diagrams showing MFA enforcement points.

##### IA-5 - CJIS v6.1 Delta — Authenticator Management

**FedRAMP High Baseline Requirement**

Password complexity, rotation, and authenticator management per FedRAMP High baseline parameters.

**CJIS v6.1 Delta**

Prescriptive password requirements for CJI systems: minimum 8 characters; must include characters from at least three of four categories (uppercase, lowercase, numeric, special); maximum password lifetime of 90 days; cannot reuse last 10 passwords. These are floor requirements — the CJIS policy sets specific values rather than deferring to organization-defined parameters.

**Implementation Guidance**

Configure identity provider and directory services to enforce CJIS password parameters. Document password policy settings and map them to CJIS requirements. If using SSO, ensure the upstream IdP enforces CJIS-compliant password policy. Note: CJIS password requirements may conflict with NIST 800-63B guidance (which discourages periodic rotation) — CJIS requirements take precedence for CJI systems.

**Evidence Required**

Password policy configuration exports from IdP/directory; screenshots of complexity enforcement settings; password history and rotation settings; documentation mapping CJIS password requirements to implemented configuration.

#### Media Protection

##### MP-6 - CJIS v6.1 Delta — Media Sanitization

**FedRAMP High Baseline Requirement**

Media sanitized before disposal or reuse per FedRAMP High baseline using approved methods.

**CJIS v6.1 Delta**

Prescriptive sanitization procedures per media type for CJI. Physical destruction (shredding, incineration, degaussing to the point of destruction) required for media that cannot be sanitized to NIST 800-88 Purge level. Electronic media must be sanitized to Purge level minimum. Paper and microform containing CJI must be cross-cut shredded or incinerated. Sanitization must be witnessed or verified, with records maintained.

**Implementation Guidance**

Develop CJI-specific media sanitization procedures referencing NIST 800-88 guidelines. Create a media sanitization matrix mapping media types to approved sanitization methods. Implement verification procedures (witnessed destruction or sanitization verification testing). Maintain sanitization logs with media identifier, method used, date, and verifier.

**Evidence Required**

Media sanitization policy and procedures specific to CJI; sanitization matrix by media type; sanitization/destruction logs with dates, methods, and witness signatures; certificates of destruction from third-party destruction vendors; NIST 800-88 Purge verification records.

#### Encryption

##### SC-12 - CJIS v6.1 Delta — Cryptographic Key Management

**FedRAMP High Baseline Requirement**

Cryptographic key management using FIPS-validated cryptographic modules per FedRAMP High baseline.

**CJIS v6.1 Delta**

Agency must manage encryption keys for CJI. The law enforcement agency (not the CSP) must retain control over key creation, distribution, storage, rotation, and revocation. FIPS 140-2 or FIPS 140-3 validated cryptographic modules are required. The agency must have the ability to immediately revoke the CSP's access to CJI by revoking or rotating keys.

**Implementation Guidance**

Implement customer-managed keys (CMK) in the CSP's key management service (e.g., AWS KMS with customer-managed CMKs). Ensure the agency has sole administrative access to key policies. Document key lifecycle procedures including creation, rotation schedule, and emergency revocation. Ensure FIPS 140-2/3 validation certificates are available for all cryptographic modules in the key management chain.

**Evidence Required**

Key management policy documenting agency key control; KMS configuration showing customer-managed keys; key policy documents showing agency-only administrative access; FIPS 140-2/3 validation certificates for cryptographic modules; key rotation schedules and logs; emergency key revocation procedures and test results.

##### SC-13 - CJIS v6.1 Delta — Cryptographic Protection

**FedRAMP High Baseline Requirement**

FIPS-validated cryptography required for information protection per FedRAMP High baseline.

**CJIS v6.1 Delta**

Minimum cryptographic strength requirements for CJI: 128-bit symmetric key length (AES-128 or higher) and 2048-bit asymmetric key length (RSA-2048 or equivalent ECC). All cryptographic modules must be FIPS 140-2 or FIPS 140-3 validated. These are floor requirements — the CJIS policy mandates specific minimum key lengths rather than deferring to organization-defined parameters.

**Implementation Guidance**

Audit all encryption configurations for CJI data paths (at rest, in transit, in use) to verify minimum key lengths. Document FIPS validation status of each cryptographic module. Ensure TLS configurations use FIPS-approved cipher suites with adequate key lengths. Verify that key generation processes produce keys meeting minimum length requirements.

**Evidence Required**

Inventory of cryptographic implementations protecting CJI with key lengths documented; FIPS 140-2/3 validation certificates for each module; TLS/SSL configuration showing cipher suites and key lengths; encryption configuration for data-at-rest showing algorithm and key length.

##### SC-28 - CJIS v6.1 Delta — Protection of Information at Rest

**FedRAMP High Baseline Requirement**

Encryption at rest required for protection of information stored on the system per FedRAMP High baseline.

**CJIS v6.1 Delta**

Agency-managed customer master key (CMK) required for all CJI at rest. The agency (not the CSP) must control the encryption key used to protect stored CJI. The agency must retain the ability to revoke the CSP's access to CJI at any time by revoking or rotating the CMK. CSP-managed default encryption keys are insufficient — agency key control is mandatory.

**Implementation Guidance**

Configure all storage services containing CJI to use agency-managed CMKs (e.g., AWS KMS CMK with agency-controlled key policy, not aws/s3 default keys). Ensure key policies restrict administrative actions to agency IAM principals. Implement key rotation per agency policy. Test key revocation procedures to verify CJI becomes inaccessible when the CMK is disabled or deleted.

**Evidence Required**

Storage service encryption configuration showing CMK ARN/ID; KMS key policy showing agency-only administrative access; inventory of all storage locations containing CJI mapped to their encryption keys; key rotation configuration and logs; key revocation test results demonstrating CJI inaccessibility.

#### Audit

##### AU-6 - CJIS v6.1 Delta — Audit Record Review

**FedRAMP High Baseline Requirement**

Review and analysis of audit records per organization-defined frequency for indications of inappropriate or unusual activity per FedRAMP High baseline.

**CJIS v6.1 Delta**

Weekly audit log review required for CJI-related events. Minimum 1-year retention period for audit logs related to CJI access and transactions. The review frequency and retention period are prescriptive — CJIS does not defer to organization-defined parameters for CJI audit logs.

**Implementation Guidance**

Configure SIEM or log management to generate weekly review reports for CJI-related audit events. Define CJI audit events (access, modification, deletion, query, export of CJI). Set log retention to minimum 1 year for CJI-related logs. Assign personnel responsible for weekly review and document the review process. Establish escalation procedures for anomalous findings.

**Evidence Required**

Weekly audit review reports with reviewer signature/acknowledgment; log retention configuration showing 1-year minimum; SIEM rules or queries used for CJI audit review; sample review reports demonstrating review completeness; escalation records for identified anomalies.

#### Access Control

##### AC-2 - CJIS v6.1 Delta — Account Management

**FedRAMP High Baseline Requirement**

Account lifecycle management including creation, modification, disabling, and removal per FedRAMP High baseline.

**CJIS v6.1 Delta**

Quarterly access reviews required for all users authorized to access CJI. Reviews must verify continued need-to-know and appropriate privilege levels. Accounts for personnel who no longer require CJI access must be disabled immediately upon determination, not at the next review cycle.

**Implementation Guidance**

Implement quarterly user access review process for CJI-authorized accounts. Generate access review reports from the identity provider listing all accounts with CJI access, their roles, and last access date. Require manager/data owner certification of continued need. Integrate with HR/personnel processes to trigger immediate access revocation upon role change or separation.

**Evidence Required**

Quarterly access review reports with reviewer certification; CJI-authorized user roster with roles and justification; evidence of access revocation for personnel no longer requiring CJI access; access review policy documenting quarterly cadence; IAM configuration showing review-triggered account actions.

#### Incident Response

##### IR-6 - CJIS v6.1 Delta — Incident Reporting

**FedRAMP High Baseline Requirement**

Incident reporting to US-CERT and organization-defined authorities per FedRAMP High baseline.

**CJIS v6.1 Delta**

Security incidents involving CJI must be reported to the state CSA-designated recipient (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6, page 171) in addition to standard FedRAMP reporting channels. Reporting must occur within timeframes established by the state CSA. The state CSA selects one or more recipients from {CSO, SIB Chief, Interface Agency Official}; the CSP's obligation is satisfied by reaching the designated recipient(s) for each affected state. Onward escalation to the FBI CJIS Division is the state CSA's responsibility, not the CSP's.

**Implementation Guidance**

Update incident response plan to include the CJIS-specific reporting chain per CJIS v6.1 IR-6 (page 171). For each state served, document which IR-6 recipient role(s) the state CSA has designated (CSO, SIB Chief, or Interface Agency Official) and maintain primary, backup, and after-hours contact information for each. Define what constitutes a CJI security incident (unauthorized access, loss, or disclosure of CJI). Establish reporting templates that satisfy both FedRAMP (US-CERT) and CJIS (state CSA-designated recipient) requirements. Conduct tabletop exercises including CJIS reporting procedures.

**Evidence Required**

Incident response plan with CJIS reporting procedures identifying each state CSA's designated IR-6 recipient(s) (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 page 171); state CSA-designated recipient contact information documented and verified for each state served; incident reporting templates; evidence of tabletop exercises including CJIS reporting chain; sample incident reports demonstrating dual reporting (US-CERT and CJIS).

#### Physical Environmental

##### PE-17 - CJIS v6.1 Delta — Alternate Work Site

**FedRAMP High Baseline Requirement**

Alternate work sites authorized with security controls equivalent to primary site per FedRAMP High baseline.

**CJIS v6.1 Delta**

Remote CJI access locations must implement specific controls: Advanced Authentication is mandatory (cannot rely on physical location security); encrypted VPN or equivalent secure connection required; personally owned devices must meet agency security configuration standards; CJI must not be stored on personally owned devices unless encrypted with agency-managed keys and approved by the CSA.

**Implementation Guidance**

Define approved remote access methods for CJI (VPN configuration, VDI, etc.). Ensure Advanced Authentication is enforced regardless of location. Establish BYOD policy for CJI access if applicable, including required device security configurations. Implement endpoint compliance checks before granting remote CJI access. Document approved alternate work sites and their security controls.

**Evidence Required**

Remote access policy specific to CJI; VPN configuration showing encryption and MFA enforcement; BYOD policy and device compliance requirements; endpoint compliance check configuration; list of approved alternate work sites with documented security controls.

#### Training

##### AT-2 - CJIS v6.1 Delta — Awareness Training

**FedRAMP High Baseline Requirement**

Security awareness training for all information system users annually per FedRAMP High baseline.

**CJIS v6.1 Delta**

CJIS Security Awareness Training required within 6 months of initial CJI access authorization. Biennial (every 2 years) refresher training required thereafter. Training content must cover CJIS-specific topics: CJI handling and dissemination rules, Security Addendum obligations, incident reporting requirements for CJI, and sanctions for policy violations.

**Implementation Guidance**

Develop or obtain CJIS-specific security awareness training content. Track training completion dates per individual with CJI access. Ensure new personnel complete training within 6 months of CJI access grant. Schedule biennial refresher training. Integrate training tracking with CJI access management — personnel with expired training should be flagged for access review.

**Evidence Required**

CJIS Security Awareness Training curriculum/content; training completion records per individual with dates; evidence of training within 6 months of initial CJI access; biennial refresher completion records; training tracking system configuration showing CJIS training requirements.

### Control-Level Gaps

#### Privacy Retention

##### SI-12.1 - CJIS v6.1 — Limit PII Elements

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP includes SI-12 base (information retention generally) but not the privacy enhancement SI-12.1 that requires active minimization of PII elements across the information lifecycle.

**CJIS v6.1 Delta**

Limit the PII elements processed during the CJI information lifecycle (creation, collection, use, processing, storage, maintenance, dissemination, disclosure, disposition) to an organization-defined list of elements. Elements not needed for operational purposes must be excluded from processing even if they are technically available from upstream APIs.

**Implementation Guidance**

Enumerate the CJI data elements the system processes at each lifecycle stage. Define and document the allowed-elements list in the SSP. Enforce minimization at ingest by filtering incoming payloads to strip unneeded elements before storage. Enforce at disclosure by returning only elements required for the disclosure context. Review the allowed-elements list annually or on system boundary changes. Include backups, DR copies, caches, and logs in the enforcement scope.

**Evidence Required**

CJI data element inventory per lifecycle stage; design/architecture documents showing where element filtering occurs; sample records or log extracts demonstrating excluded elements are not persisted; review records showing periodic re-evaluation of the allowed-elements list; documented organization-defined parameter value for si-12.01_odp.

##### SI-12.2 - CJIS v6.1 — Minimize PII in Testing, Training, and Research

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP addresses development safeguards (CM-4, SA-3) but does not require minimization of PII in non-production environments. Production data in test environments is a common anti-pattern not explicitly prohibited by FedRAMP.

**CJIS v6.1 Delta**

Apply defined techniques (de-identification, synthetic data, data masking, tokenization) to minimize the use of CJI and PII in research, testing, and training contexts. Real CJI in non-production environments is prohibited unless minimized by an explicit technique.

**Implementation Guidance**

Default to synthetic CJI in non-production environments. Build a reference synthetic dataset with realistic structure. Prohibit production CJI in dev/test by policy and technical enforcement (export restrictions, network segregation, approval gating). Mask direct identifiers when real data shape is required for testing. Use synthetic case scenarios for training rather than real case files. For research use, require IRB-equivalent review and de-identification.

**Evidence Required**

Synthetic dataset documentation; policy prohibiting production CJI in non-production environments; technical controls enforcing the policy (database export restrictions, network segregation, cross-environment transfer audit logs); training material samples showing synthetic data; research governance records including de-identification method documentation.

##### SI-12.3 - CJIS v6.1 — Information Disposal

**FedRAMP High Baseline Requirement**

Not included at the disposal-enhancement level in FedRAMP High baseline. FedRAMP includes MP-6 (media sanitization) for physical media and SC-28 (protection at rest) for storage encryption, but not the logical information disposal mandate that requires active erasure or cryptographic destruction at end of retention.

**CJIS v6.1 Delta**

Use defined techniques (logical erasure with verified overwrite, cryptographic erasure via key destruction, physical destruction) to dispose of, destroy, or erase CJI and CJI-bearing artifacts at the end of the retention period. Scope includes originals, copies, archived records, and system logs that may contain PII or CJI. Disposal must be scheduled and produce audit evidence.

**Implementation Guidance**

Define retention periods per CJI data class in the SSP. Select the disposal technique per class (logical erasure for active records, cryptographic erasure for cloud archives via KMS key destruction, physical destruction for end-of-life media). Automate disposal where possible (AWS S3 Lifecycle policies). Include logs, backups, DR copies, and caches in the disposal scope. Integrate legal-hold awareness so held records are not disposed on schedule. Produce disposal logs showing what was disposed, when, and by which technique.

**Evidence Required**

Retention schedule per CJI data class; disposal procedures per class; disposal logs (lifecycle policy run reports, secure-delete verification output, key-destruction records); cross-copy coverage documentation showing backups and log archives are in scope; media destruction certificates for physical disposal events; legal-hold workflow documentation.

#### PII Limitation

##### AU-3.3 - CJIS v6.1 — Limit PII Elements in Audit Records

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's AU-3 requires specific audit record content (timestamp, event type, source, outcome, identity) but does not impose PII minimization within audit records.

**CJIS v6.1 Delta**

Audit records must contain only the PII elements identified as necessary in the privacy risk assessment (RA-3). Intent is that log contents themselves do not become a secondary PII exposure. For CJI, typically log the action metadata (who, when, what object, from where) without embedding the full CJI payload.

**Implementation Guidance**

Conduct RA-3 privacy risk assessment to define permitted audit record elements. Log object identifiers (case ID, record ID) rather than object content. Sanitize at the logging layer so implicit logging (dumping full request/response objects) does not leak PII. Apply minimization to exported log copies (SIEM, central log platform). Reconcile with AU-6 implementation-level delta (1-year retention) so minimized logs still meet retention obligations.

**Evidence Required**

Privacy risk assessment output defining permitted audit record elements; audit record schema documenting the permitted element set; sample audit records showing permitted elements only; SIEM configuration demonstrating minimization in exported copies; logging library standards or code review documentation.

##### PE-8.3 - CJIS v6.1 — Limit PII Elements in Visitor Access Records

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's PE-8 requires visitor access records be maintained with defined content (name, purpose, escort, date/time) but does not require minimizing PII within those records.

**CJIS v6.1 Delta**

Visitor access records for facilities hosting CJI must contain only the PII elements identified in the privacy risk assessment as operationally necessary. Excess identifiers (SSN, DOB, full driver's license, photograph) must not be collected if not required for access control.

**Implementation Guidance**

Define permitted visitor record elements via RA-3. Configure visitor management systems (and paper sign-in forms) to collect only permitted elements. Align with retention and SI-12.3 disposal schedules. Communicate the collection rationale to visitors who ask.

**Evidence Required**

Privacy risk assessment output defining permitted visitor record elements; visitor management system configuration or sign-in form showing limited element set; sample visitor records demonstrating compliance; retention and disposal documentation for visitor logs.

##### AC-3.14 - CJIS v6.1 — Individual Access to PII

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP does not require a subject-access mechanism. U.S. subject access rights are sector-specific (Privacy Act, HIPAA, GLBA).

**CJIS v6.1 Delta**

Provide a mechanism enabling individuals to access their own PII elements as defined. NIST supplemental guidance recognizes law-enforcement records may be exempt from disclosure under Privacy Act (j)(2) or state analogues; the control operates as: provide the mechanism, apply statutory exemptions when responding.

**Implementation Guidance**

Define the access mechanism (forms, authentication, fees, SLA, redaction policy) coordinated with the state CSA. Authenticate requesters strongly (notarized request, in-person ID verification, or AAL2 electronic identity proofing per IA-2). Route to privacy official and legal counsel for adjudication. Respond with cited exemptions for withheld elements. Track request volume, response time, and approval breakdown.

**Evidence Required**

Documented access mechanism (forms, authentication, SLA, redaction policy); exemption register cataloguing applicable statutory exemptions; sample request records showing full workflow from intake through response; aggregate metrics for access requests received and resolved.

##### SC-7.24 - CJIS v6.1 — PII Processing Rules at Boundaries

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's SC-7 requires boundary protection (firewalls, DMZ) but not PII-specific processing rules with exception tracking.

**CJIS v6.1 Delta**

For systems processing CJI: define processing rules per PII element (what operations are allowed), monitor for permitted processing at external interfaces and internal boundaries, document each exception, and periodically review and remove stale exceptions.

**Implementation Guidance**

Define processing rules per CJI element class in the SSP (sc-07.24_odp parameter). Enforce at technical boundaries (API gateways, inter-tier controls) using policy-as-code where feasible (OPA/Rego, API gateway policies). Instrument boundaries with telemetry to record rule evaluations. Maintain an exception register with scope, compensating control, and expiration. Review exceptions on a defined cadence (typical quarterly) and close stale exceptions.

**Evidence Required**

Processing rules documentation per CJI element class; boundary configuration (API gateway policy, inter-tier enforcement rules); monitoring telemetry showing rule evaluations; exception register listing active exceptions with scope and expiration; exception review records showing closure of stale exceptions.

#### Training

##### AT-3.5 - CJIS v6.1 — Role-Based Training on Processing PII

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP requires AT-3 role-based security training and AT-2 awareness but not a specific role-based training obligation for PII processing and transparency controls.

**CJIS v6.1 Delta**

Provide initial and recurring role-based training on PII processing and transparency controls to organization-defined personnel and roles at organization-defined frequency. Distinct from AT-2 (broad CJIS awareness); AT-3.5 targets personnel whose duties include PII processing activities (privacy officer, CJIS Systems Officer, auditors, DBAs with CJI access, developers of CJI processing code).

**Implementation Guidance**

Define target roles (at-03.05_odp.01) and refresher frequency (at-03.05_odp.02). Build role-specific content covering the organization's authority to process CJI, applicable privacy notices, dissemination agreements, privacy impact assessments, and role-specific obligations. Integrate with existing AT-3 role-based security training by adding a privacy module. Track completion per role including role-entry gating where applicable. Coordinate with the state CSA for state-specific requirements.

**Evidence Required**

Defined role list (at-03.05_odp.01 value); defined refresher frequency (at-03.05_odp.02 value); role-specific training content covering PII processing and transparency controls; completion rosters per role with dates; integration documentation showing AT-3.5 relationship to AT-2 and AT-3.

##### IR-2.3 - CJIS v6.1 — Breach Response Training

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's IR-2 requires general IR training but does not require training specifically on breach identification and response where breach is narrowed to PII-involving incidents.

**CJIS v6.1 Delta**

Provide IR training specifically on breach identification, response, and reporting. Breach for PII purposes includes loss of control, compromise, unauthorized disclosure or acquisition, or authorized-user access for unauthorized purposes. Content covers breach recognition versus lesser incidents, reporting obligations and timeframes, tabletop exercises, and the organization's breach response workflow.

**Implementation Guidance**

Incorporate breach module into existing IR-2 training: breach definition, recognition, reporting channels (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6 page 171), time-sensitive obligations. Run breach-specific tabletop exercises including insider-misuse scenarios. Cover the authorized-user-unauthorized-purpose case explicitly. Connect training to IR-8.1 notice-determination process. Align cadence with existing IR training (annual typical).

**Evidence Required**

IR training curriculum documenting the breach module; tabletop exercise records from breach-specific simulations (scenario, participants, observations, improvement actions); completion rosters per IR team member; documentation showing IR-6 reporting channels are covered in training.

#### Incident Response Planning

##### IR-8.1 - CJIS v6.1 — IR Plan for Breaches

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's IR-8 requires a general Incident Response Plan but not the breach-specific process content required by IR-8.1.

**CJIS v6.1 Delta**

The IR Plan must include three breach-specific elements: (1) notice determination process for notifying individuals or other organizations; (2) harm assessment process evaluating harm to affected individuals and mitigation mechanisms; (3) identification of applicable privacy requirements (for CJI: CJIS v6.1 IR-6 and IR-8(1) per published policy pages 167-174, state breach notification statutes, Privacy Act exemptions).

**Implementation Guidance**

Write a breach-specific appendix or section of the IR Plan separate from general incident workflow. Define the notice determination decision tree (what data, to whom, likelihood of misuse, notification scope). Define the harm assessment framework for CJI-specific harms (public embarrassment, safety risk for witnesses/informants, judicial consequences for sealed records). Catalog applicable privacy requirements per breach type in a matrix. Rehearse via tabletop exercises and revise based on observed friction.

**Evidence Required**

IR Plan breach section or appendix with the three required elements; notice determination decision tree; harm assessment framework with examples applied to typical CJI breach scenarios; applicable privacy requirements matrix mapping breach types to statutes and CJIS Security Policy sections; tabletop exercise results; plan revision history showing updates from exercises or real incidents.

#### Planning

##### PL-9 - CJIS v6.1 — Central Management

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP accepts the concept of common controls and inheritance but does not mandate that specific controls be centrally managed.

**CJIS v6.1 Delta**

Centrally manage a defined set of security and privacy controls and related processes. Goal is organization-wide standardization: rather than each system team implementing AC-2, AT-2, AU-6, or SI-12.3 individually, the controls are managed centrally and inherited. For CJI, central management typically takes two shapes: CSP-side (CSP manages common controls and offers them as inherited controls to agency tenants) or agency-side (state CSA or central agency privacy program manages CJIS-specific controls across subordinate components).

**Implementation Guidance**

Define the centrally managed control set (pl-09_odp). Candidates from NIST supplemental: AC-2, AT-2/3, AU-3/6/7/11, CA-2/3/7, CM family, SI-2/3/4. Add CJIS-specific items: dissemination logging, Security Addendum administration, fingerprint check workflow. Document inheritance per control in the SSP. Build central management capability through tooling (IAM, LMS, SIEM, compliance platform) and organizational structure (privacy office, CSO, CJIS Systems Officer). Measure inheritance coverage across consuming systems.

**Evidence Required**

Defined centrally managed control set per pl-09_odp; inheritance documentation in the SSP per control; central management tooling evidence (IAM configuration, LMS records, SIEM deployment); organizational chart showing central management functions; coverage metrics showing which systems inherit which controls and any gaps.

#### Engineering

##### SA-8.33 - CJIS v6.1 — Minimization as Engineering Principle

**FedRAMP High Baseline Requirement**

Not included in FedRAMP High baseline. FedRAMP's SA-8 requires security engineering principles during development but not privacy minimization as a specific engineering principle. Privacy engineering is not part of the FedRAMP High SA-family baseline.

**CJIS v6.1 Delta**

Implement the privacy principle of minimization (process only PII directly relevant and necessary; retain only as long as necessary) via defined engineering processes. Engages at system design, acquisition, and development time, not only at operational runtime. Architectural counterpart to the runtime minimization controls SI-12.1, SI-12.2, SI-12.3, SC-7.24, SI-19, AU-3.3, PE-8.3.

**Implementation Guidance**

Adopt privacy-by-design in the SDLC. Require minimization analysis in every design document or acquisition spec touching CJI: what PII, why, how long, with what lifecycle controls. Define engineering processes (sa-08.33_odp): privacy design review, PII data flow analysis, PIA completion prior to design approval, architectural review board with privacy reviewer, acquisition gate verifying vendor minimization capability. Integrate with FedRAMP SA-8 and SA-15 processes. Tie to PIA as the artifact documenting minimization analysis.

**Evidence Required**

Defined engineering processes per sa-08.33_odp; privacy design review records for CJI-processing systems; PIA documentation covering minimization analysis; architectural review board minutes showing privacy reviewer participation; acquisition evidence showing vendor minimization capability was verified (contract language, demonstrations, test results).
