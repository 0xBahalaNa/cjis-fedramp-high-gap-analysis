# CJIS v6.1 to FedRAMP High — Control-by-Control Delta Analysis

Source data: `data/cjis-overlay.json` (OSCAL overlay with structured delta capture)

## Gap Categories

The gap analysis distinguishes two categories of gaps between CJIS v6.1 and FedRAMP High:

1. **Implementation-level deltas** are controls present in both baselines where CJIS imposes stricter parameters, scope, or methodology. The baseline control exists in FedRAMP High; CJIS tightens it (for example, CJIS requires fingerprint-based background checks for PS-3 while FedRAMP leaves screening method to organizational discretion).
2. **Control-level gaps** are controls present in the CJIS v6.1 baseline but absent from FedRAMP High entirely. An agency running FedRAMP High must implement these from scratch to satisfy CJIS. These are concentrated in the NIST 800-53 Rev 5 privacy overlay, reflecting CJI's status as sensitive personal data.

Baseline comparison identifies 13 implementation-level deltas and 12 control-level gaps. The analysis below addresses both, grouped by category. See the "Methodology" section at the end of this document for how gap controls were verified against the published CJIS v6.1 source text.

### Implementation-Level Deltas (13 controls)

| Control | Family | Status |
|---------|--------|--------|
| PS-3 | Personnel Security | Complete |
| PS-6 | Personnel Security | Complete |
| IA-2 | Identification and Authentication | Complete |
| IA-5 | Identification and Authentication | Complete |
| SC-12 | Encryption | Complete |
| SC-13 | Encryption | Complete |
| SC-28 | Encryption | Complete |
| MP-6 | Media Protection | Complete |
| AU-6 | Audit and Accountability | Complete |
| AC-2 | Access Control | Complete |
| IR-6 | Incident Response | Complete |
| PE-17 | Physical and Environmental Protection | Complete |
| AT-2 | Awareness and Training | Complete |

### Control-Level Gaps (12 controls)

| Control | Family | Cluster | Status |
|---------|--------|---------|--------|
| SI-12.1 | System and Information Integrity | Privacy, Retention | Complete |
| SI-12.2 | System and Information Integrity | Privacy, Retention | Complete |
| SI-12.3 | System and Information Integrity | Privacy, Retention | Complete |
| AU-3.3 | Audit and Accountability | PII Limitation | Complete |
| PE-8.3 | Physical and Environmental Protection | PII Limitation | Complete |
| AC-3.14 | Access Control | PII Limitation | Complete |
| SC-7.24 | System and Communications Protection | PII Limitation | Complete |
| AT-3.5 | Awareness and Training | Training | Complete |
| IR-2.3 | Incident Response | Training | Complete |
| IR-8.1 | Incident Response | Incident Response Planning | Complete |
| PL-9 | Planning | Central Management | Complete |
| SA-8.33 | System and Services Acquisition | Engineering | Complete |

---

## Personnel Security

### PS-3 — Personnel Screening

**NIST 800-53 Rev 5 Control:** Screen individuals prior to authorizing access to the system; rescreen individuals in accordance with organization-defined conditions and frequency.

**CJIS v6.1 Reference:** Personnel Security (PS) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires background investigations for personnel with access to the information system, commensurate with the risk level of the assigned position. The baseline defers to organization-defined parameters for:

- **Rescreening conditions** — the organization defines what triggers rescreening (role change, time-based, etc.)
- **Rescreening frequency** — the organization defines how often rescreening occurs

FedRAMP does not prescribe the *type* of background check. A standard OPM-tier investigation or commercial background check satisfies the baseline, as long as it matches the position risk designation. This flexibility is where CJIS diverges.

#### CJIS v6.1 Delta

CJIS eliminates the flexibility in screening method and scope:

- **Fingerprint-based background check** required — not just any background investigation, but specifically a fingerprint submission processed through state and national (FBI) criminal history repositories.
- **All CJI access** — applies to every individual with access to unencrypted CJI, regardless of position risk level. There is no "low-risk position" exemption.
- **No role exceptions** — contractors, vendor personnel, and CSP staff with logical or physical access to unencrypted CJI must complete fingerprint-based checks. A CSP system administrator who can access the database where CJI is stored is in scope, even if they never query CJI directly.
- **Pre-access requirement** — the fingerprint check must be completed and adjudicated *before* access is provisioned, not concurrently.

**Why this matters:** A CSP operating under FedRAMP High may have completed standard background checks for all personnel. Those checks satisfy FedRAMP but do not satisfy CJIS unless they included fingerprint submission to state and FBI repositories. This is a process gap, not a policy gap — the CSP likely already has a screening program, but it needs to be augmented with the fingerprint-specific requirement.

#### Implementation Guidance

1. **Establish a fingerprint submission process** with the state CJIS Systems Agency (CSA). Each state has a CSA that coordinates fingerprint-based background checks. The CSP must work with the subscribing agency's CSA to set up the submission channel.
2. **Identify all in-scope personnel.** Map every individual (employee, contractor, subcontractor) with logical or physical access to systems that store, process, or transmit unencrypted CJI. Include system administrators, database administrators, and operations staff — not just application users.
3. **Integrate into onboarding.** Add fingerprint submission as a gate in the personnel onboarding workflow. CJI access must not be provisioned until the fingerprint check is completed and adjudicated favorably.
4. **Define rescreening triggers.** Work with the CSA to determine rescreening conditions — typically role changes, periodic intervals (often every 5 years), or when the CSA mandates it.
5. **Maintain records.** Track fingerprint submission dates, adjudication results, and the link between each individual and their CJI access authorization.

#### Evidence Required

An auditor will expect to see:

- **Fingerprint submission records** for each individual with CJI access, showing submission to state and FBI repositories
- **Background check adjudication results** confirming favorable determination prior to CJI access
- **Personnel roster cross-referenced with CJI access list** — demonstrating that every person with CJI access has a completed fingerprint check on file
- **Onboarding procedures** documenting the fingerprint check as a prerequisite for CJI access provisioning
- **Rescreening schedule** and completion records showing the organization tracks and executes rescreening

#### Key Considerations

- **Encryption safe harbor:** If CJI is encrypted with agency-managed keys and the CSP personnel cannot access the decryption keys, those personnel may be outside the fingerprint check scope. This is a common architecture strategy to reduce the population requiring fingerprint checks, but the encryption implementation must be defensible (see SC-12, SC-28).
- **Subcontractor chains:** If the CSP uses subcontractors (e.g., managed services, data center staff), the fingerprint requirement flows down. The CSP must ensure subcontractors complete fingerprint checks or are architecturally excluded from CJI access.
- **State-specific variations:** While CJIS v6.1 sets the floor, individual state CSAs may impose additional screening requirements. The CSP should confirm requirements with each state CSA it serves.
- **Timeline:** Fingerprint-based checks can take weeks to complete depending on the state. Plan for this lead time in hiring and onboarding processes.

---

### PS-6 — Access Agreements

**NIST 800-53 Rev 5 Control:** Develop and document access agreements for organizational systems; review and update access agreements at organization-defined frequency; verify that individuals sign appropriate access agreements prior to being granted access and re-sign when agreements are updated.

**CJIS v6.1 Reference:** Personnel Security (PS) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires signed access agreements before system access is granted. This includes:

- **Nondisclosure agreements** — protecting sensitive information
- **Acceptable use agreements** — defining permitted system use
- **Rules of behavior** — documenting user responsibilities and expected conduct

The baseline defers to the organization for:

- **Review/update frequency** — how often access agreements are reviewed and refreshed
- **Re-signing frequency** — how often users must re-sign to maintain access

Standard access agreements cover general system use, data handling, and security responsibilities. FedRAMP does not prescribe a specific agreement template for particular data types.

#### CJIS v6.1 Delta

CJIS requires a specific, additional agreement beyond standard access agreements:

- **CJIS Security Addendum** — a binding legal agreement that must be executed by every individual with access to CJI. This is a separate document from standard rules of behavior or acceptable use agreements.
- **CJI-specific content** — the Security Addendum specifically addresses CJI handling rules, dissemination restrictions, sanctions for misuse or unauthorized disclosure, and obligations that survive termination of access.
- **Pre-access gate** — the signed addendum is a prerequisite for CJI access, not something that can be completed after access is provisioned.
- **Binding on individuals, not just organizations** — the addendum is signed by each person, not covered by an organizational MOU. An MOU between the agency and CSP is also required, but does not replace individual addendums.

**Why this matters:** A CSP with a FedRAMP High ATO has access agreements, but they are generic to the system. The CJIS Security Addendum is a *specific document* with *specific content* about CJI. A CSP cannot substitute its standard rules of behavior for the CJIS Security Addendum — both are required.

#### Implementation Guidance

1. **Obtain the CJIS Security Addendum template** from the state CSA. The FBI CJIS Division publishes a standard template, but state CSAs may have modified versions. Use the version required by the subscribing agency's CSA.
2. **Integrate addendum signing into onboarding.** Add the CJIS Security Addendum as a required step alongside (not replacing) standard access agreements. The addendum must be signed before CJI access is provisioned.
3. **Maintain signed addendums on file.** Store executed addendums in a retrievable format, linked to the individual's access record. Both physical and electronic signatures are typically acceptable.
4. **Track re-execution requirements.** When the Security Addendum terms are updated (e.g., by the CSA or FBI CJIS Division), all personnel with CJI access must re-sign. Track addendum versions and re-execution dates.
5. **Include in separation procedures.** When an individual's CJI access is revoked, document the termination of the addendum obligation and retain the signed addendum per the CSA's records retention requirements.

#### Evidence Required

An auditor will expect to see:

- **Signed CJIS Security Addendum** for every individual with CJI access — one per person, not a collective agreement
- **Addendum tracking log** showing execution dates, addendum version, and the individual's name and role
- **Evidence of pre-access signing** — demonstrating the addendum was signed before CJI access was granted (compare signing date to access provisioning date)
- **Re-execution records** showing personnel re-signed when addendum terms were updated
- **Organizational MOU/MOA** between the agency and CSP covering CJIS responsibilities (separate from individual addendums)

#### Key Considerations

- **The addendum is not optional.** Even if the CSP has comprehensive rules of behavior that cover similar ground, the CJIS Security Addendum is a specific, named document that auditors will look for by name.
- **Contractor and subcontractor coverage.** The addendum requirement applies to all personnel with CJI access, including third-party contractors. The CSP must ensure its vendors execute addendums if their personnel access CJI.
- **Relationship to PS-3.** The Security Addendum and fingerprint-based background check (PS-3) are complementary — both must be completed before CJI access is granted. The addendum is the *legal agreement*; the fingerprint check is the *screening verification*.
- **Records retention.** Retain signed addendums for the duration required by the CSA. Some states require retention beyond the period of CJI access.

---

## Identification and Authentication

### IA-2 — Identification and Authentication (Organizational Users)

**NIST 800-53 Rev 5 Control:** Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.

**CJIS v6.1 Reference:** Identification and Authentication (IA) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires multi-factor authentication for all users through enhancements IA-2(1) (MFA for privileged accounts) and IA-2(2) (MFA for non-privileged accounts). The baseline requires:

- **Unique identification** — each user has a distinct identity, no shared accounts for accountability purposes
- **Multi-factor authentication** — two or more factors from: something you know, something you have, something you are
- **Network and local access** — MFA applies to both network (remote) and local access for privileged accounts

FedRAMP High does not prescribe a specific Authentication Assurance Level (AAL) from NIST SP 800-63-3, nor does it mandate phishing resistance. An organization using SMS-based OTP as a second factor satisfies the FedRAMP High baseline, even though SMS OTP is vulnerable to SIM-swapping and interception attacks.

#### CJIS v6.1 Delta

CJIS defines "Advanced Authentication" with specific requirements that narrow the acceptable MFA implementations:

- **AAL2 minimum** — per NIST SP 800-63-3, AAL2 requires multi-factor authentication using authenticators with proven possession through a cryptographic protocol or comparable mechanism. This eliminates some weaker MFA implementations that satisfy AAL1 but not AAL2.
- **Phishing-resistant authenticators preferred** — while AAL2 is the floor, CJIS guidance favors phishing-resistant methods (FIDO2/WebAuthn, PIV/CAC cards, hardware security keys). Software OTP tokens (TOTP apps) meet AAL2 but are not phishing-resistant.
- **Mandatory trigger conditions** — Advanced Authentication is required when accessing CJI from outside a physically secure location (defined by the agency) or when accessing CJI over any network. This means remote access to CJI always requires Advanced Authentication.
- **Two distinct factors required** — must use two of the three categories: something you know (password/PIN), something you have (token/smart card/phone), something you are (biometric). Two factors from the same category do not satisfy the requirement.

**Why this matters:** A CSP using basic MFA (e.g., password + SMS OTP) satisfies FedRAMP High but may not satisfy CJIS Advanced Authentication. The distinction is the assurance level — CJIS requires AAL2, which demands that the authenticator prove possession through a cryptographic protocol. SMS OTP does not meet AAL2 because the phone number is not a cryptographic authenticator. Organizations must evaluate their current MFA stack against NIST SP 800-63-3 AAL2 requirements, not just confirm that "MFA is enabled."

#### NIST SP 800-63-3 AAL Levels (Reference)

Understanding the AAL hierarchy is essential for evaluating whether current MFA satisfies CJIS:

- **AAL1** — single-factor or multi-factor, no cryptographic proof of possession required. Password-only or password + SMS OTP can satisfy AAL1.
- **AAL2** — multi-factor required, with at least one factor providing cryptographic proof of authenticator possession. Examples: TOTP app + password, hardware OTP token + password, smart card + PIN. *This is the CJIS floor.*
- **AAL3** — hardware-based cryptographic authenticator required, verifier impersonation resistance mandatory. Examples: PIV/CAC + PIN, FIDO2 hardware key + PIN. This exceeds CJIS requirements but is the strongest option.

#### Implementation Guidance

1. **Inventory current MFA implementations.** Map each CJI access path to the authenticator types in use. Classify each against NIST SP 800-63-3 AAL levels. Any path using SMS OTP, email codes, or voice callbacks as the second factor likely falls below AAL2.
2. **Deploy AAL2-compliant authenticators.** TOTP apps (Authy, Google Authenticator, Microsoft Authenticator) meet AAL2 minimum. For stronger posture, deploy FIDO2/WebAuthn hardware keys or PIV/CAC cards, which meet AAL3 and provide phishing resistance.
3. **Enforce MFA at the application layer.** MFA must be enforced at the point of CJI access, not just at the network perimeter. If a user authenticates with MFA to a VPN but then accesses the CJI application with only a password, the Advanced Authentication requirement is not satisfied for the CJI access.
4. **Document authenticator classifications.** Maintain a record mapping each authenticator type to its AAL level, with references to NIST SP 800-63-3. This documentation is critical during audits.
5. **Address the physically secure location exception.** Work with the subscribing agency to define which locations qualify as "physically secure" for CJIS purposes. Users at physically secure locations accessing CJI over local networks may have different authentication requirements — but this exception must be formally documented and approved by the agency.

#### Evidence Required

An auditor will expect to see:

- **MFA configuration exports** from the identity provider showing enforcement for all CJI access paths
- **Authenticator type inventory** classified by AAL level per NIST SP 800-63-3
- **Authentication policy documentation** specifying CJIS Advanced Authentication requirements and which authenticator types are approved
- **Authentication logs** demonstrating MFA enforcement for CJI access events
- **Network diagrams** showing MFA enforcement points relative to CJI data flows
- **Physically secure location documentation** if the exception is claimed, including agency approval

#### Key Considerations

- **SMS OTP is the most common gap.** Many organizations implemented SMS-based MFA to satisfy FedRAMP. For CJIS, SMS does not meet AAL2. This is often the single highest-effort remediation item in the IA-2 delta.
- **SSO complicates the picture.** If users authenticate via SSO, the AAL level is determined by the IdP's authentication flow, not the downstream application. Verify the IdP enforces AAL2 for sessions that will access CJI.
- **Conditional access policies.** Consider using conditional access to require stronger authenticators (AAL3/phishing-resistant) for CJI access while allowing AAL2 for non-CJI systems. This reduces friction while exceeding CJIS minimums for the most sensitive access.
- **Grace period for migration.** If migrating from SMS OTP to AAL2-compliant authenticators, coordinate with the CSA on timeline expectations. An in-progress migration with a documented plan and deadline is better than no plan.

---

### IA-5 — Authenticator Management

**NIST 800-53 Rev 5 Control:** Manage system authenticators by verifying identity during initial distribution, establishing initial authenticator content, ensuring sufficient strength, implementing administrative procedures, changing defaults, and protecting authenticator content from unauthorized disclosure and modification.

**CJIS v6.1 Reference:** Identification and Authentication (IA) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires authenticator management with organization-defined parameters for:

- **Refresh/change period** — the organization defines the time period for changing or refreshing authenticators by type
- **Change-triggering events** — the organization defines events that require authenticator changes (compromise, personnel change, etc.)

For password-based authenticators specifically, FedRAMP High enhancement IA-5(1) requires password complexity and rotation, but the specific values (minimum length, composition rules, rotation period, history depth) are left to the organization. FedRAMP provides guidance through its parameter requirements but does not dictate exact values for all parameters.

#### CJIS v6.1 Delta

CJIS replaces the org-defined flexibility with prescriptive password parameters:

- **Minimum 8 characters** — this is a floor, not a recommendation. Passwords shorter than 8 characters are non-compliant regardless of complexity.
- **Complexity: 3 of 4 categories** — passwords must include characters from at least three of: uppercase letters, lowercase letters, numeric digits, special characters. This is more prescriptive than "enforce complexity" — it defines exactly what complexity means.
- **90-day maximum lifetime** — passwords must be changed at least every 90 days. This is a hard ceiling — the organization cannot set a longer rotation period for CJI systems.
- **10-password history** — users cannot reuse any of their last 10 passwords. This prevents trivial rotation patterns (Password1 → Password2 → Password1).

**Why this matters — the 800-63B tension:** NIST SP 800-63B (Digital Identity Guidelines, 2017) explicitly *discourages* periodic password rotation, recommending instead that passwords be changed only when there is evidence of compromise. The reasoning is sound — forced rotation leads to weaker passwords (users increment a number, add a symbol) and does not measurably improve security when combined with breach detection.

However, CJIS v6.1 requires 90-day rotation. For CJI systems, **CJIS requirements take precedence over 800-63B guidance.** This is not a contradiction in the framework — CJIS is a policy overlay with specific operational requirements for CJI, while 800-63B is a guideline. When they conflict, the more restrictive policy wins for the data type it governs. An auditor will not accept "we follow 800-63B instead" as a justification for skipping 90-day rotation on CJI systems.

#### Implementation Guidance

1. **Configure the identity provider** to enforce CJIS password parameters. Set minimum length to 8, require 3 of 4 character categories, enforce 90-day maximum age, and set password history to 10. These settings must be applied to all accounts that access CJI.
2. **Verify SSO/federated IdP compliance.** If CJI access flows through SSO, the upstream IdP must enforce CJIS password policy. A downstream application cannot compensate for a weak upstream password policy.
3. **Document the 800-63B deviation.** Since CJIS password requirements conflict with 800-63B guidance, document this explicitly: "CJI systems enforce 90-day password rotation per CJIS Security Policy v6.1 Section 5.6, which takes precedence over NIST SP 800-63B rotation guidance for systems processing CJI." This preempts questions about why your password policy appears to contradict NIST guidance.
4. **Scope the policy to CJI systems.** Non-CJI systems can follow 800-63B guidance (no forced rotation). Apply CJIS password parameters only to systems and accounts that access CJI. This reduces user friction on non-CJI systems while maintaining compliance.
5. **Monitor for weak rotation patterns.** Even with history enforcement, users may rotate through predictable patterns (Summer2026!, Fall2026!, Winter2027!). Consider implementing password similarity checks or a deny-list of common patterns if the IdP supports it.

#### Evidence Required

An auditor will expect to see:

- **Password policy configuration exports** from the IdP or directory service showing all four CJIS parameters (8-char minimum, 3-of-4 complexity, 90-day max age, 10-password history)
- **Scope documentation** showing which systems/accounts are subject to CJIS password policy
- **IdP configuration screenshots** demonstrating enforcement (not just documentation — actual system settings)
- **Documentation mapping** CJIS password requirements to implemented configuration, line by line
- **800-63B deviation justification** documenting why periodic rotation is enforced despite 800-63B guidance

#### Key Considerations

- **MFA does not replace password policy.** Even with AAL2 MFA (IA-2), CJIS still requires compliant password parameters. MFA and password policy are independent requirements — satisfying one does not exempt the other.
- **Service accounts and API keys.** Clarify with the CSA whether service accounts that access CJI must follow the same password parameters. Service accounts typically use long-lived secrets or certificates, not user-interactive passwords. The 90-day rotation may apply differently to these.
- **Password manager compatibility.** Organizations should encourage (or require) password managers to help users generate and manage complex passwords that change every 90 days. This mitigates the weak-rotation-pattern problem.
- **Future CJIS updates.** CJIS v6.1 aligned with 800-53 Rev 5 but retained legacy password parameters from earlier versions. Future CJIS updates may reconcile with 800-63B guidance. Until then, enforce the current requirements.

---

## Encryption

Encryption is the most technically consequential delta between CJIS v6.1 and FedRAMP High. FedRAMP High requires encryption with FIPS-validated modules but allows the CSP to manage encryption keys. CJIS fundamentally changes the key management model: the law enforcement agency — not the CSP — must retain control over encryption keys for CJI. This has direct architectural implications for AWS KMS, storage service configuration, and cross-account access patterns.

These three controls are tightly coupled:
- **SC-12** governs *who manages the keys* and the key lifecycle
- **SC-13** governs *what algorithms and key strengths* are acceptable
- **SC-28** applies both to *data at rest*, requiring agency-managed keys for stored CJI

### SC-12 — Cryptographic Key Establishment and Management

**NIST 800-53 Rev 5 Control:** Establish and manage cryptographic keys when cryptography is employed within the system in accordance with organization-defined key management requirements.

**CJIS v6.1 Reference:** System and Communications Protection (SC) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires cryptographic key management using FIPS-validated cryptographic modules. The baseline defers to organization-defined parameters for:

- **Key management requirements** — the organization defines requirements for key generation, distribution, storage, access, and destruction
- **Key lifecycle management** — the organization determines rotation schedules, revocation procedures, and key recovery mechanisms

Critically, FedRAMP High does not prescribe *who* manages the keys. A CSP using AWS-managed keys (e.g., `aws/s3`, `aws/ebs` default KMS keys) satisfies the FedRAMP baseline. The CSP manages the key lifecycle, the keys live in the CSP's infrastructure, and the customer trusts the CSP to handle key management properly. This is the standard shared responsibility model for encryption — the CSP provides the service, the customer uses it.

#### CJIS v6.1 Delta

CJIS breaks the standard shared responsibility model for key management:

- **Agency must manage encryption keys** — the law enforcement agency, not the CSP, must retain control over key creation, distribution, storage, rotation, and revocation for keys protecting CJI. This is not a suggestion — it is a mandatory requirement that changes the fundamental trust model.
- **Agency retains revocation authority** — the agency must have the ability to immediately revoke the CSP's access to CJI by revoking or rotating encryption keys. If the agency cannot unilaterally cut off access, the key management model does not satisfy CJIS.
- **FIPS 140-2 or FIPS 140-3 validated modules** — all cryptographic modules in the key management chain must be FIPS validated. This aligns with FedRAMP but is explicitly stated in CJIS to ensure no gaps in the validation chain (e.g., a key wrapping layer that uses a non-validated module).
- **Key lifecycle documentation** — the agency must have documented procedures for key creation, rotation, revocation, and destruction. These procedures must be agency-controlled, not just inherited from the CSP's default key management.

**Why this matters:** A CSP with a FedRAMP High ATO is already using FIPS-validated encryption, but the keys are CSP-managed. Moving to agency-managed keys requires architectural changes — different KMS key types, different key policies, different IAM trust relationships. This is not a policy update; it is an infrastructure change that affects every service that encrypts CJI.

#### Implementation Guidance — AWS KMS Architecture

1. **Use customer-managed CMKs (not AWS-managed keys).** In AWS KMS, this means creating keys of type `CUSTOMER_MANAGED_CMK`, not using the default `aws/s3`, `aws/ebs`, or `aws/rds` service keys. Customer-managed CMKs allow the key policy to be configured with agency-specific access controls.
2. **Configure key policies to restrict administrative access to agency IAM principals.** The KMS key policy is the primary access control. The `kms:*` administrative permissions must be granted only to IAM roles or users controlled by the agency — not to the CSP's account. This is the mechanism that gives the agency revocation authority.
3. **Implement cross-account key sharing if the CSP operates in a separate AWS account.** The agency creates the CMK in their account and grants the CSP's account `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey`, and `kms:ReEncrypt` permissions via the key policy. The agency retains `kms:*` (full administrative control). To revoke access, the agency removes the CSP's account from the key policy or disables the key.
4. **Document the key lifecycle.** Create procedures for: key creation (who initiates, who approves), key rotation (automatic annual rotation via KMS, or manual rotation with a defined schedule), emergency key revocation (steps to disable or delete the CMK, expected impact on CJI availability), and key destruction (KMS scheduled deletion with a 7-30 day waiting period).
5. **Verify FIPS 140-2/3 validation.** AWS KMS uses FIPS 140-2 Level 2 validated HSMs (certificate numbers are published in AWS documentation). Document the certificate numbers and validation status. If using CloudHSM for additional control, it provides FIPS 140-2 Level 3 validated modules.
6. **Test revocation.** Periodically test the agency's ability to revoke CSP access by temporarily removing permissions from the key policy and verifying that CJI becomes inaccessible to CSP services. This test validates the revocation procedure and confirms no backdoor access paths exist.

#### Evidence Required

An auditor will expect to see:

- **Key management policy** documenting agency key control responsibilities, not delegated to the CSP
- **KMS configuration exports** showing customer-managed CMKs (not AWS-managed default keys) for all CJI-related services
- **Key policy documents** showing agency IAM principals have administrative access and the CSP has only usage permissions
- **FIPS 140-2/3 validation certificates** for all cryptographic modules in the key management chain (AWS KMS HSM certificates)
- **Key rotation configuration** showing automatic or scheduled rotation with documented procedures
- **Emergency key revocation procedures** and test results demonstrating the agency can immediately cut off CSP access to CJI
- **Cross-account architecture diagram** (if applicable) showing key ownership in the agency's account and usage grants to the CSP's account

#### Key Considerations

- **AWS-managed keys vs. customer-managed CMKs.** This is the single most important distinction. AWS-managed keys (the default when you enable encryption on S3, EBS, RDS, etc.) are created and managed by AWS in your account but you cannot modify their key policies. Customer-managed CMKs give you full control over the key policy — this is what CJIS requires. Migrating from AWS-managed to customer-managed CMKs may require re-encrypting existing data.
- **CloudHSM as an alternative.** For agencies requiring FIPS 140-2 Level 3 (instead of Level 2), AWS CloudHSM provides dedicated HSMs. CloudHSM keys are managed entirely by the agency and never leave the HSM in plaintext. This exceeds CJIS requirements but adds operational complexity and cost.
- **Key policy vs. IAM policy.** In AWS KMS, the key policy is the authoritative access control. An IAM policy alone cannot grant access to a CMK if the key policy does not allow it. Agencies should rely on key policies (not just IAM policies) to enforce access controls — this ensures that even a compromised IAM administrator cannot access the CMK without key policy changes.
- **Relationship to SC-28.** SC-12 governs *who manages the keys*; SC-28 governs *where those keys are applied* (data at rest). An agency cannot satisfy SC-28 without first satisfying SC-12 — you cannot have agency-managed encryption at rest without agency-managed keys.
- **Multi-region considerations.** If CJI is replicated across AWS regions, the CMK must be replicated or separate CMKs must be created in each region. AWS KMS multi-Region keys can simplify this, but each replica must have the same agency-controlled key policy.

---

### SC-13 — Cryptographic Protection

**NIST 800-53 Rev 5 Control:** Determine the cryptographic uses required for the system; implement the required types of cryptography for each specified use.

**CJIS v6.1 Reference:** System and Communications Protection (SC) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires FIPS-validated cryptography for information protection. The baseline defers to organization-defined parameters for:

- **Cryptographic uses** — the organization determines which data flows and storage locations require cryptographic protection
- **Types of cryptography** — the organization selects the specific algorithms and key lengths, as long as they are FIPS-validated

FedRAMP High does not prescribe minimum key lengths. An organization using AES-128 or AES-256 both satisfy the baseline, as long as the implementation uses a FIPS-validated module. Similarly, RSA-2048 and RSA-4096 are both acceptable. The baseline focuses on *validation status*, not *cryptographic strength* beyond what FIPS validation requires.

#### CJIS v6.1 Delta

CJIS adds prescriptive minimum key lengths on top of the FIPS validation requirement:

- **128-bit minimum symmetric key length** — AES-128 is the floor. AES-192 and AES-256 exceed the requirement. Any symmetric cipher below 128-bit is non-compliant for CJI, regardless of FIPS validation status.
- **2048-bit minimum asymmetric key length** — RSA-2048 is the floor. RSA-3072 and RSA-4096 exceed the requirement. For elliptic curve cryptography (ECC), the equivalent strength is approximately 224-bit ECC (NIST P-224 or higher), though NIST P-256 and P-384 are more commonly deployed.
- **FIPS 140-2 or FIPS 140-3 validated modules** — same as FedRAMP, but CJIS explicitly states this to close any ambiguity. Every cryptographic operation protecting CJI (encryption, decryption, hashing, signing, key exchange) must use a FIPS-validated module.
- **Applies to all CJI data states** — these minimums apply to CJI at rest, in transit, and in use. TLS configurations, disk encryption, database encryption, and any other cryptographic protection for CJI must meet these floors.

**Why this matters:** Most modern AWS services default to AES-256 for symmetric encryption and support RSA-2048+ for asymmetric operations, so the key length minimums are usually satisfied by default configurations. The real risk is in edge cases: legacy TLS configurations that include weaker cipher suites, custom application-layer encryption that uses shorter keys, or third-party integrations that negotiate down to weaker algorithms. The audit obligation is to *prove* compliance across all CJI data paths, not just assume it.

#### Implementation Guidance

1. **Audit all encryption configurations across CJI data paths.** Inventory every service and component that encrypts CJI — storage (S3, EBS, RDS, DynamoDB), transit (TLS, VPN, API gateways), and application-layer encryption. Document the algorithm and key length for each.
2. **Verify TLS configurations.** Ensure TLS configurations enforce FIPS-approved cipher suites with adequate key lengths. In AWS, this means using security policies that exclude weak ciphers. For ALB/NLB, use TLS security policies that enforce TLS 1.2+ with AES-128-GCM or AES-256-GCM cipher suites. Disable any cipher suite using keys below 128-bit or algorithms not on the FIPS-approved list.
3. **Check storage encryption defaults.** AWS KMS defaults to AES-256 for symmetric CMKs. S3 SSE-KMS, EBS encryption, and RDS encryption all use AES-256 when configured with KMS CMKs. Verify this by checking the key spec on each CMK (`SYMMETRIC_DEFAULT` = AES-256-GCM in AWS KMS).
4. **Review asymmetric key usage.** If using asymmetric keys for signing, key exchange, or certificate-based authentication, verify RSA-2048 minimum. For ECC, verify NIST P-256 or higher. Check TLS certificates, SSH keys, and any application-level digital signatures.
5. **Document FIPS validation chain.** For each cryptographic module, record the CMVP certificate number, validation level, and the specific operations it covers. AWS publishes certificate numbers for KMS, CloudHSM, and other services in their FIPS compliance documentation.
6. **Establish a cipher suite policy.** Create a documented list of approved cipher suites for CJI systems. Reference NIST SP 800-52 (TLS guidelines) for recommended cipher suites. Block any configuration change that introduces a cipher suite below the minimums.

#### Evidence Required

An auditor will expect to see:

- **Cryptographic inventory** mapping every CJI data path (at rest, in transit) to the algorithm and key length in use
- **FIPS 140-2/3 validation certificates** for each cryptographic module, with CMVP certificate numbers
- **TLS configuration exports** showing cipher suites, protocol versions, and key lengths for all endpoints handling CJI
- **KMS key specifications** showing symmetric key algorithm (AES-256) and any asymmetric key specs (RSA-2048+)
- **Cipher suite policy document** listing approved algorithms and minimum key lengths for CJI systems
- **Configuration scan results** from tools like SSL Labs, `nmap --script ssl-enum-ciphers`, or AWS Config rules showing no weak ciphers in use

#### Key Considerations

- **AES-256 is the practical default.** AWS KMS symmetric keys are AES-256-GCM. S3, EBS, RDS, and DynamoDB encryption all use AES-256 when configured with KMS. The 128-bit floor is unlikely to be a problem in AWS-native services — the risk is in custom or third-party components.
- **TLS is where gaps hide.** While storage encryption is typically AES-256, TLS configurations can inadvertently include weaker cipher suites from older security policies. Audit all load balancers, API gateways, and CloudFront distributions for cipher suite compliance.
- **ECC equivalence.** CJIS specifies 2048-bit asymmetric minimum, which is RSA-specific. For ECC, use NIST-recommended equivalent strength: P-256 (128-bit security level) meets the minimum, P-384 (192-bit) exceeds it. Document the equivalence rationale.
- **Relationship to SC-12 and SC-28.** SC-13 defines the *strength* of the cryptography; SC-12 defines *who manages* it; SC-28 defines *where it applies* for data at rest. All three must be satisfied together — using AES-256 (SC-13) with a CSP-managed key (fails SC-12) for data at rest (SC-28) would not satisfy CJIS.
- **Crypto agility.** As NIST post-quantum cryptography standards mature, agencies should plan for algorithm migration. CJIS v6.1 does not yet require post-quantum algorithms, but awareness of the transition timeline is a forward-looking consideration.

---

### SC-28 — Protection of Information at Rest

**NIST 800-53 Rev 5 Control:** Protect the confidentiality and integrity of information at rest.

**CJIS v6.1 Reference:** System and Communications Protection (SC) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires encryption at rest for information stored on the system. The baseline requires protection of both confidentiality and integrity, with the organization defining:

- **Information requiring protection** — the organization determines which data at rest requires cryptographic protection
- **Protection mechanisms** — the organization selects the specific encryption method (e.g., full-disk encryption, database-level encryption, object-level encryption)

FedRAMP High is satisfied by enabling encryption on storage services using any FIPS-validated method. AWS-managed default encryption (e.g., S3 default encryption with `aws/s3` KMS key, EBS encryption with `aws/ebs` KMS key) satisfies the FedRAMP baseline. The key management is transparent to the customer — AWS creates, rotates, and manages the keys.

#### CJIS v6.1 Delta

CJIS adds a specific key ownership requirement that changes the entire encryption-at-rest architecture:

- **Agency-managed CMK required** — all CJI at rest must be encrypted with a customer master key controlled by the law enforcement agency. CSP-managed default encryption keys (AWS-managed keys like `aws/s3`, `aws/ebs`) are **insufficient** — they do not give the agency control over the key.
- **Agency retains key revocation authority** — the agency must be able to immediately render CJI inaccessible by disabling or deleting the CMK. This is the "kill switch" requirement — if the agency-CSP relationship ends or a breach occurs, the agency must be able to unilaterally cut off access to CJI by acting on the encryption key.
- **Applies to all storage locations** — every location where CJI is stored must use the agency-managed CMK. This includes primary databases, backups, replicas, caches, logs containing CJI, temporary files, and any other persistent storage. A single S3 bucket using the default `aws/s3` key while others use the agency CMK creates a compliance gap.
- **Encryption is not optional for CJI at rest** — unlike FedRAMP, which allows the organization to determine which data requires encryption at rest, CJIS mandates encryption for all CJI at rest with no exceptions.

**Why this matters:** This is the control that makes the PS-3 encryption safe harbor work. If CJI is encrypted at rest with agency-managed keys and the CSP cannot access those keys, CSP personnel may be outside the scope of fingerprint-based background checks (PS-3). But this only works if the encryption implementation is airtight — agency-managed keys, no CSP access to key administrative operations, and verifiable key revocation capability. SC-28 is where the rubber meets the road for the agency-managed encryption architecture.

#### Implementation Guidance — AWS Storage Services

1. **Create a dedicated CMK for CJI encryption.** In the agency's AWS account (or in a dedicated key management account), create a customer-managed symmetric CMK. Set the key policy to grant administrative access (`kms:*`) only to agency IAM principals. Grant the CSP's account or roles only usage permissions (`kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey`, `kms:DescribeKey`).
2. **Configure S3 bucket encryption.** For S3 buckets containing CJI, set the default encryption to use the agency-managed CMK (SSE-KMS with the CMK ARN). Apply a bucket policy that denies `s3:PutObject` without the `x-amz-server-side-encryption-aws-kms-key-id` header matching the CMK ARN. This prevents objects from being uploaded with the wrong key.
3. **Configure EBS volume encryption.** For EC2 instances processing CJI, enable EBS encryption using the agency-managed CMK. Set the default EBS encryption key in the account to the agency CMK. Existing volumes encrypted with AWS-managed keys must be re-encrypted — create a snapshot, copy the snapshot with the new CMK, and create a new volume from the re-encrypted snapshot.
4. **Configure RDS encryption.** RDS instances storing CJI must be encrypted with the agency-managed CMK. RDS encryption is set at instance creation and cannot be changed — if an existing instance uses the wrong key, the migration path is: snapshot → copy snapshot with agency CMK → restore to new instance from re-encrypted snapshot.
5. **Configure DynamoDB encryption.** For DynamoDB tables containing CJI, set encryption to use the agency-managed CMK (not the default `AWS_OWNED_CMK` or `AWS_MANAGED_CMK`).
6. **Address backup encryption.** AWS Backup, S3 replication, RDS automated backups, and EBS snapshots must all use the agency-managed CMK. Verify that backup configurations inherit the source encryption key or are explicitly configured to use the agency CMK.
7. **Inventory all CJI storage locations.** Create and maintain a complete inventory of every storage location containing CJI, mapped to the encryption key protecting it. Include primary storage, backups, replicas, logs, and caches. This inventory is critical for audit evidence and for verifying that no CJI exists outside the agency-managed CMK's protection.

#### Evidence Required

An auditor will expect to see:

- **Storage encryption configuration** for every service containing CJI, showing the agency-managed CMK ARN/ID (not AWS-managed key ARNs)
- **KMS key policy** showing agency-only administrative access and CSP limited to usage permissions
- **CJI storage inventory** mapping every storage location to its encryption key — demonstrating complete coverage
- **Key rotation configuration and logs** showing the CMK is rotated per agency policy
- **Key revocation test results** demonstrating that disabling the CMK renders CJI inaccessible across all storage locations
- **Bucket/volume/instance encryption configuration exports** from AWS CLI or Config showing encryption settings for each resource
- **Backup encryption verification** showing backups, snapshots, and replicas use the agency-managed CMK

#### Key Considerations

- **Migration from AWS-managed to customer-managed CMKs.** This is often the highest-effort item. S3 objects can be re-encrypted in place using S3 Batch Operations with a copy operation specifying the new CMK. EBS volumes and RDS instances require snapshot-copy-restore workflows. Plan for downtime and data validation during migration.
- **The encryption safe harbor for PS-3.** SC-28 with agency-managed keys is the foundation of the encryption safe harbor referenced in PS-3 (Personnel Screening). If CSP personnel cannot access the CMK, they cannot decrypt CJI, and they may be outside the scope of fingerprint-based background checks. But this only holds if the key policy is airtight — any administrative access by CSP IAM principals undermines the safe harbor.
- **Cost implications.** Customer-managed CMKs in AWS KMS cost $1/month per key plus per-request charges. CloudHSM (if used for FIPS 140-2 Level 3) costs significantly more (~$1.50/hour per HSM). The cost is modest relative to the compliance benefit, but should be budgeted.
- **Logging and monitoring.** Enable CloudTrail logging for all KMS API calls related to the CJI CMK. Monitor for unexpected `kms:DisableKey`, `kms:ScheduleKeyDeletion`, or key policy changes. Alarm on any CMK administrative action not initiated by an authorized agency principal.
- **Relationship to SC-12.** SC-28 cannot be satisfied without SC-12. The agency-managed CMK requirement (SC-28) depends on agency key management (SC-12). These controls must be implemented together — you cannot have agency-managed encryption at rest without agency-managed key lifecycle procedures.

---

## Media Protection

### MP-6 — Media Sanitization

**NIST 800-53 Rev 5 Control:** Sanitize organization-defined system media prior to disposal, release out of organizational control, or release for reuse using organization-defined sanitization techniques and procedures; employ sanitization mechanisms with the strength and integrity commensurate with the security category or classification of the information.

**CJIS v6.1 Reference:** Media Protection (MP) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires media sanitization before disposal or reuse, but defers heavily to organization-defined parameters for:

- **System media scope** — the organization defines which media types are subject to sanitization before disposal, release, or reuse
- **Sanitization techniques and procedures** — the organization selects the sanitization methods, as long as the strength is commensurate with the security category of the information

FedRAMP High requires sanitization that is proportional to the data classification, and it references NIST SP 800-88 (Guidelines for Media Sanitization) as guidance. However, the baseline does not mandate specific sanitization methods per media type. An organization could clear, purge, or destroy media — the choice is left to the organization based on their risk assessment and the information's sensitivity. There is no explicit requirement for witnessed destruction or per-event sanitization records beyond what the organization defines in its own procedures.

#### CJIS v6.1 Delta

CJIS replaces the organizational flexibility with prescriptive sanitization requirements tied to media type:

- **NIST 800-88 Purge level minimum for electronic media** — electronic media containing CJI must be sanitized to at least the Purge level as defined in NIST SP 800-88. Purge renders data recovery infeasible using state-of-the-art laboratory techniques. Clear level (which protects against simple non-invasive recovery) is insufficient for CJI. This means standard "quick format" or single-pass overwrite may not satisfy the requirement — the method must achieve Purge-level assurance.
- **Physical destruction when Purge is not achievable** — media that cannot be reliably sanitized to Purge level must be physically destroyed. Approved destruction methods include shredding, incineration, and degaussing to the point of destruction (for magnetic media). This applies to damaged media, media with firmware-level storage (SSDs with wear-leveling that cannot guarantee complete overwrite), and any media where Purge-level sanitization cannot be verified.
- **Paper and microform: cross-cut shred or incinerate** — paper documents and microform (microfiche, microfilm) containing CJI must be cross-cut shredded or incinerated. Strip-cut shredding is insufficient — cross-cut produces particles small enough to prevent reconstruction. The shred size should align with NSA/CSS EPL-listed shredder specifications for classified material handling (typically 1mm x 5mm or smaller), though CJIS does not mandate a specific particle size.
- **Witnessed or verified sanitization** — sanitization events must be witnessed by an authorized individual or verified through testing. "Verified" means the sanitization result is confirmed (e.g., attempting data recovery on a sanitized drive to confirm data is irrecoverable). This is more rigorous than FedRAMP's general requirement, which does not mandate per-event witnessing.
- **Sanitization records** — each sanitization event must be documented with: media identifier (serial number, asset tag), media type, sanitization method used, date of sanitization, and identity of the person who performed and witnessed/verified the sanitization. These records must be retained per the organization's records retention policy.

**Why this matters:** A CSP operating under FedRAMP High likely has a media sanitization procedure, but it may rely on the CSP's own risk assessment to determine methods per media type. CJIS removes that discretion for CJI media — the methods are prescribed, destruction is mandatory in specific cases, and every event must be documented. For CSPs using cloud-only infrastructure (no physical media they control), the primary impact is on the agency side and on any hybrid components. For CSPs managing physical infrastructure, this affects hardware lifecycle management, decommissioning procedures, and vendor relationships for destruction services.

#### Implementation Guidance

1. **Create a CJI media sanitization matrix.** Map each media type to the approved sanitization method:

   | Media Type | Sanitization Method | Standard |
   |------------|-------------------|----------|
   | HDD (magnetic) | Purge (secure erase / cryptographic erase) or physical destruction (degauss + shred) | NIST 800-88 Purge |
   | SSD / Flash | Cryptographic erase (if supported with verification) or physical destruction (shred/incinerate) | NIST 800-88 Purge |
   | Magnetic tape | Degauss to point of destruction or incinerate | NIST 800-88 Destroy |
   | Optical media (CD/DVD) | Physical destruction (shred/incinerate) | NIST 800-88 Destroy |
   | Paper documents | Cross-cut shred or incinerate | CJIS v6.1 §5.8 |
   | Microform | Cross-cut shred or incinerate | CJIS v6.1 §5.8 |
   | Mobile devices | Cryptographic erase + factory reset (if verified) or physical destruction | NIST 800-88 Purge |

2. **Implement witnessed destruction procedures.** Designate authorized witnesses for sanitization events. For in-house sanitization, the witness must be present during the process. For third-party destruction vendors, require certificates of destruction that include media serial numbers, destruction method, date, and witness signatures.
3. **Establish a sanitization log.** Create a standardized log template capturing: media identifier, media type, data classification (CJI), sanitization method, date/time, operator name, witness/verifier name, and verification result (pass/fail). Retain logs per the agency's records retention requirements.
4. **Address SSD sanitization challenges.** SSDs with wear-leveling algorithms may retain data in overprovisioned cells even after a standard wipe. For SSDs containing CJI, cryptographic erase (where the encryption key is destroyed, rendering all data irrecoverable) is the preferred Purge method. If the SSD does not support verified cryptographic erase, physical destruction is required. Document the SSD manufacturer's sanitization capabilities and verification methods.
5. **Contract requirements for third-party destruction.** If using a third-party media destruction vendor, the contract must require: NIST 800-88 compliance, certificates of destruction per media item, chain-of-custody documentation during transport, and the right to audit the vendor's destruction process. The vendor's employees who handle CJI media may be subject to CJIS personnel requirements (PS-3, PS-6) if they have access to unencrypted CJI during the destruction process.
6. **Cloud-specific considerations.** For CJI stored entirely in AWS, the CSP (AWS) handles physical media sanitization under their shared responsibility model. AWS publishes media sanitization procedures in their SOC 2 reports and follows NIST 800-88 guidelines. The agency should obtain AWS's media sanitization attestation and verify it meets CJIS Purge/Destroy requirements. For any agency-controlled media (laptops, removable drives, backup tapes), the agency is directly responsible for CJIS-compliant sanitization.

#### Evidence Required

An auditor will expect to see:

- **Media sanitization policy** specific to CJI, referencing NIST 800-88 and CJIS v6.1 requirements
- **Sanitization matrix** mapping media types to approved methods (as described above)
- **Sanitization logs** with media identifiers, methods, dates, and witness signatures for each event
- **Certificates of destruction** from third-party destruction vendors, per media item
- **Verification records** showing sanitization effectiveness was confirmed (e.g., recovery attempt results)
- **Third-party vendor contracts** with NIST 800-88 compliance requirements and audit rights
- **CSP media sanitization attestation** (for cloud-hosted CJI) — AWS SOC 2 or equivalent documentation showing media sanitization procedures meet NIST 800-88 Purge/Destroy levels

#### Key Considerations

- **Cloud vs. on-premises distinction.** For fully cloud-hosted CJI, the physical media sanitization responsibility falls primarily on the CSP (AWS). The agency's responsibility shifts to: (1) obtaining the CSP's sanitization attestation, (2) verifying the attestation meets CJIS requirements, and (3) sanitizing any agency-controlled endpoints or removable media. This does not eliminate the requirement — it shifts where it applies.
- **SSD overprovisioning is the biggest technical risk.** Standard overwrite methods that work on HDDs do not guarantee complete data removal on SSDs due to wear-leveling and overprovisioned NAND cells. Cryptographic erase (ATA Secure Erase Enhanced or NVMe Format with crypto erase) is the only reliable Purge method for SSDs. If the SSD does not support verified cryptographic erase, physical destruction is the only compliant option.
- **Degaussing does not work on SSDs.** Degaussing is effective only on magnetic media (HDDs, tapes). SSDs use NAND flash storage, which is not affected by magnetic fields. An organization that includes "degaussing" as a sanitization method for all media types has a gap — SSDs must be handled separately.
- **Chain of custody for off-site destruction.** If media is transported to a destruction facility, document the chain of custody from the point of removal to the point of destruction. Any gap in the chain creates a period where CJI media is unaccounted for — this is an audit finding.
- **Relationship to SC-28 (encryption safe harbor).** If CJI at rest is encrypted with agency-managed keys (SC-28), cryptographic erase becomes a stronger sanitization option — destroying the encryption key renders the data irrecoverable regardless of whether the physical media is sanitized. This is another benefit of the agency-managed key architecture. However, cryptographic erase alone may not satisfy CJIS if the agency or CSA requires physical destruction for certain media types — confirm with the CSA.

---

## Audit and Accountability

### AU-6 — Audit Record Review, Analysis, and Reporting

**NIST 800-53 Rev 5 Control:** Review and analyze system audit records for indications of inappropriate or unusual activity and the potential impact of the inappropriate or unusual activity; report findings to designated personnel or roles; and adjust the level of audit record review, analysis, and reporting when there is a change in risk.

**CJIS v6.1 Reference:** Audit and Accountability (AU) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires review and analysis of audit records at an organization-defined frequency. The baseline defers to organization-defined parameters for:

- **Review frequency** (au-06_odp.01) — the organization defines how often audit records are reviewed and analyzed. FedRAMP High typically sets this to "at least weekly," but the specific cadence and scope are left to the organization's discretion.
- **Types of inappropriate or unusual activity** (au-06_odp.02) — the organization defines what constitutes suspicious activity worth reviewing (failed logins, privilege escalation attempts, after-hours access, etc.)
- **Reporting recipients** (au-06_odp.03) — the organization defines who receives the findings from audit record reviews

FedRAMP High does not prescribe which specific events must be included in each review cycle, nor does it mandate a minimum retention period for audit logs beyond compliance with applicable records management requirements (typically NARA schedules). The organization determines the scope and depth of each review based on its own risk assessment.

#### CJIS v6.1 Delta

CJIS narrows the flexibility in two areas: review cadence and log retention.

- **Weekly audit log review for CJI events** — CJIS mandates weekly review of audit logs related to CJI access and transactions. This is prescriptive, not organization-defined. While FedRAMP High often sets a similar "at least weekly" cadence, CJIS specifically scopes the weekly review to CJI-related events: access to CJI, modification of CJI records, deletion of CJI, queries against CJI databases, and export or dissemination of CJI. The review cannot be a general-purpose log scan that incidentally covers CJI — it must explicitly target CJI event categories.
- **1-year minimum retention for CJI audit logs** — audit logs related to CJI access and transactions must be retained for a minimum of 1 year. FedRAMP defers to NARA records schedules, which may specify different retention periods depending on the record type and system. CJIS sets a floor of 1 year regardless of what NARA schedules would otherwise require. For CJI-related logs, whichever retention period is longer (NARA or CJIS) applies.
- **Prescriptive event scope** — the types of events that must be reviewed are defined by CJIS, not left to the organization. At minimum, the review must cover: successful and failed authentication attempts to CJI systems, CJI record access (read/query), CJI record modification (create/update/delete), CJI export or dissemination, privilege changes for CJI-authorized accounts, and administrative actions on CJI systems.

**Why this matters:** A CSP operating under FedRAMP High likely has a weekly log review process, but it may be scoped to infrastructure-level events (firewall logs, system alerts, vulnerability scan results). CJIS requires the review to explicitly cover application-layer CJI access events, which may not be captured by infrastructure-focused SIEM rules. The gap is often not in the review process itself but in the event coverage: are CJI access queries, record modifications, and dissemination events being logged, ingested into the SIEM, and included in the weekly review? The 1-year retention requirement may also exceed what the organization currently retains for application-level logs.

#### Implementation Guidance

1. **Define CJI audit event categories.** Create a documented list of event types that constitute "CJI-related audit events" for your environment. At minimum, include: authentication to CJI systems (success and failure), CJI record access/query, CJI record create/update/delete, CJI export or download, privilege changes on CJI-authorized accounts, and administrative actions on CJI infrastructure. Map each event category to the specific log source that captures it (application logs, database audit logs, CloudTrail, etc.).
2. **Configure application-layer audit logging.** Infrastructure-level logging (CloudTrail, VPC Flow Logs) captures API calls and network traffic but does not capture application-level CJI access. Ensure the application that manages CJI generates audit logs for record-level access events. For database-hosted CJI, enable database audit logging (e.g., RDS audit logs, DynamoDB Streams, or Aurora activity streams) to capture queries against CJI tables.
3. **Implement weekly review workflow.** Configure the SIEM or log management platform to generate a weekly CJI audit review report. The report should aggregate CJI-related events by category, flag anomalies (unusual access volumes, after-hours access, access by accounts not on the CJI-authorized roster, failed authentication spikes), and require reviewer sign-off. Assign a specific individual or team responsible for the weekly review, with a backup reviewer for coverage.

   **AWS Implementation:** Use CloudWatch Logs Insights or Athena queries against CloudTrail logs in S3 to generate weekly CJI event summaries. Create saved queries for each CJI event category. Use Amazon Security Lake or a third-party SIEM (Splunk, Elastic) to centralize application-level and infrastructure-level logs into a single review workflow. Schedule weekly CloudWatch alarms or EventBridge rules to trigger review report generation.

4. **Set log retention to 1 year minimum.** Configure log storage retention to meet the 1-year floor. For CloudWatch Logs, set the retention period to at least 365 days on all log groups containing CJI audit events. For logs stored in S3 (CloudTrail, application logs), configure S3 Lifecycle rules to retain objects for at least 1 year before transitioning to archival storage (Glacier) or deletion. If using a SIEM, verify the SIEM's hot/warm/cold storage tiers retain CJI logs for at least 1 year in a searchable state.
5. **Document escalation procedures.** Define what happens when the weekly review identifies an anomaly. Establish escalation paths: reviewer identifies anomaly, notifies the CJIS Systems Officer (CSO) and the incident response team, initiates investigation, and documents resolution. The escalation procedure should integrate with the CJIS incident reporting chain (IR-6) for events that constitute a security incident.
6. **Integrate AU-6 with AC-2.** The weekly audit review should cross-reference CJI access events against the current CJI-authorized user roster (AC-2). Any CJI access by an account not on the authorized roster is an immediate escalation. This creates a continuous assurance loop: AU-6 detects who accessed CJI, AC-2 verifies who should have accessed CJI.

#### Evidence Required

An auditor will expect to see:

- **Weekly audit review reports** with reviewer signature or acknowledgment, covering all CJI event categories
- **CJI audit event category definition** documenting which events are in scope for the weekly review
- **Log retention configuration** showing 1-year minimum for all CJI-related log sources (CloudWatch Logs retention settings, S3 Lifecycle policies, SIEM retention configuration)
- **SIEM rules or queries** used for the CJI audit review, demonstrating coverage of all required event categories
- **Sample review reports** demonstrating completeness (all event categories covered, anomalies flagged, reviewer acknowledgment)
- **Escalation records** showing how anomalous findings were handled, investigated, and resolved
- **Log source inventory** mapping each CJI event category to its log source, demonstrating that all CJI access paths are captured

#### Key Considerations

- **Application-layer logging is the gap.** Most FedRAMP-authorized CSPs have strong infrastructure logging (CloudTrail, VPC Flow Logs, GuardDuty). The gap is typically at the application layer: does the application log who queried which CJI records, who exported data, who modified records? If the application treats CJI as opaque data and only the database logs queries, ensure database audit logging is enabled and feeding into the SIEM.
- **"Weekly" means every 7 days, not "sometime this week."** Establish a consistent review day and document it. If a review is missed due to personnel absence, the backup reviewer must complete it. An auditor will check for gaps in the weekly review cadence, and a missing week is a finding.
- **Retention cost planning.** A year of application-level audit logs can be significant in volume, especially for high-traffic CJI systems. Plan storage costs accordingly. Use tiered storage (S3 Intelligent-Tiering or Glacier after 90 days) to manage cost while maintaining the 1-year retention requirement. Logs must remain searchable for the review process, so purely archival storage (Glacier Deep Archive) may not satisfy the requirement if logs need to be recalled for investigation.
- **Relationship to AU-6 and AC-2 feedback loop.** AU-6 weekly reviews should flag any CJI access by accounts that are not on the current AC-2 authorized roster. Conversely, AC-2 quarterly reviews should use AU-6 data (last access date, access frequency) to inform need-to-know determinations. If an account has not accessed CJI in 90 days, the quarterly reviewer should question whether continued access is justified.
- **FedRAMP continuous monitoring overlap.** FedRAMP continuous monitoring (ConMon) already requires ongoing log review. The CJIS delta is not a new process but a tighter scope and cadence for CJI events within the existing ConMon program. Frame it as a CJI-specific layer on top of ConMon, not a separate program.

---

## Access Control

### AC-2 — Account Management

**NIST 800-53 Rev 5 Control:** Define and document account types; assign account managers; specify authorized users, group and role membership, and access authorizations for each account; review accounts for compliance with account management requirements at an organization-defined frequency; and align account management processes with personnel termination and transfer processes.

**CJIS v6.1 Reference:** Access Control (AC) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires comprehensive account lifecycle management, but defers to organization-defined parameters for several key elements:

- **Account review frequency** (ac-02_odp.10) — the organization defines how often accounts are reviewed for compliance with account management requirements. FedRAMP High typically sets this to "at least annually."
- **Notification timelines** — the organization defines the time periods for notifying account managers when accounts are no longer required (ac-02_odp.06), when users are terminated or transferred (ac-02_odp.07), and when system usage or need-to-know changes (ac-02_odp.08).
- **Account creation prerequisites** — the organization defines the prerequisites and criteria for group and role membership (ac-02_odp.01) and the personnel who must approve account creation (ac-02_odp.03).

FedRAMP High satisfies the account management baseline with annual access reviews, organization-defined notification timelines, and standard account lifecycle procedures. The baseline focuses on the *existence* of account management processes rather than prescribing specific cadences for CJI or other data-type-specific reviews.

#### CJIS v6.1 Delta

CJIS tightens the review cadence and adds immediate-action requirements for CJI-authorized accounts:

- **Quarterly access reviews** — accounts authorized to access CJI must be reviewed every 90 days, not annually. Each review must verify: (1) the individual still has a legitimate need-to-know for CJI access, (2) the individual's privilege level remains appropriate for their current role, and (3) all prerequisite requirements remain current (fingerprint-based background check per PS-3, signed CJIS Security Addendum per PS-6, security awareness training per AT-2). A quarterly review that only checks "is this account still active?" is insufficient. The review must validate the full chain of CJI access authorization.
- **Immediate revocation upon determination** — when it is determined that an individual no longer requires CJI access (role change, transfer, separation, need-to-know expiration), access must be revoked immediately. "Immediately" means as soon as the determination is made, not at the next quarterly review cycle or at the end of a grace period. The quarterly review is the backstop that catches anything the real-time revocation process missed. It is not a substitute for prompt action when access should be revoked.
- **Need-to-know validation** — each CJI access authorization must be tied to a specific, documented need-to-know. Generic justifications ("user needs system access for their job") are insufficient. The need-to-know must reference the individual's role, the specific CJI data sets they require, and the business function that requires CJI access. This is more granular than FedRAMP's general "valid access authorization" requirement.
- **Prerequisite chain validation** — CJI access authorization depends on other CJIS controls being satisfied. During each quarterly review, the reviewer must verify that the individual's fingerprint-based background check (PS-3) is current, their CJIS Security Addendum (PS-6) is on file and current, and their CJIS security awareness training (AT-2) is not expired. If any prerequisite is out of compliance, CJI access must be suspended until the prerequisite is remediated. This creates a dependency chain that annual reviews do not enforce with the same rigor.

**Why this matters:** This is where IGA (Identity Governance and Administration) meets law enforcement data protection. A CSP with an annual access review process meets FedRAMP but leaves a 12-month window where stale or inappropriate CJI access persists undetected. In a law enforcement context, that window is unacceptable: personnel transfer between departments, officers are placed on administrative leave, contractor engagements end, and interagency agreements expire. Quarterly reviews with immediate revocation shrink the maximum exposure window to 90 days (for cases the real-time process misses) rather than 365 days.

#### Implementation Guidance

1. **Establish the CJI-authorized user roster.** Maintain a definitive list of all accounts authorized to access CJI, including: individual name, account identifier, role, assigned privilege level, need-to-know justification, date of last PS-3 background check, date of last PS-6 Security Addendum execution, and date of last AT-2 CJIS security awareness training. This roster is the single source of truth for CJI access authorization and the primary input for quarterly reviews.

   **AWS Implementation:** Use AWS IAM Identity Center (SSO) to manage CJI-authorized users in a dedicated permission set or group. Tag IAM roles and policies associated with CJI access with a `cji-authorized: true` tag. Use IAM Access Analyzer to identify which principals can reach CJI resources (S3 buckets, RDS instances, DynamoDB tables). Generate the roster by querying IAM Identity Center group membership cross-referenced with IAM Access Analyzer findings.

2. **Build the quarterly review workflow.** Create a structured review process that runs every 90 days:
   - **Generate the review report.** Pull the current CJI-authorized roster with each user's role, last access date (from AU-6 audit logs), background check status (PS-3), Security Addendum status (PS-6), and training status (AT-2).
   - **Assign reviewers.** Each account should be reviewed by the user's manager or the data owner responsible for the CJI data set the user accesses. Reviewers must not review their own access.
   - **Certify or revoke.** For each account, the reviewer must certify continued need-to-know and appropriate privilege level, or flag the account for revocation. Certifications must include a specific justification, not a blanket approval.
   - **Execute revocation.** Accounts flagged for revocation must be disabled within the review cycle. Track revocation completion as part of the review record.
   - **Document results.** The completed review report, with certifications and revocations, must be retained as audit evidence.

3. **Integrate real-time revocation triggers.** Connect CJI access revocation to HR and personnel processes so that access is revoked immediately upon:
   - Employee termination or resignation
   - Role change to a position that does not require CJI access
   - Placement on administrative leave (depending on agency policy)
   - Expiration of contractor engagement or interagency agreement
   - Failure to complete required PS-3 rescreening, PS-6 re-execution, or AT-2 training renewal

   **AWS Implementation:** Use SCIM provisioning between the HR system (or IdP) and IAM Identity Center for automated deprovisioning. Configure Lambda functions triggered by EventBridge rules to monitor for group membership changes and log deprovisioning events. For immediate revocation, disabling the user in IAM Identity Center terminates active sessions and blocks new authentication.

4. **Cross-reference with AU-6 audit data.** Use CJI access log data from the weekly AU-6 reviews to inform quarterly AC-2 reviews. Specifically: identify accounts that have not accessed CJI in the past 90 days (candidates for access removal under least privilege), identify accounts with unusual access patterns (potential indicator of compromised credentials or misuse), and verify that all CJI access events in the audit logs were performed by accounts on the authorized roster.
5. **Document the need-to-know justification standard.** Define what constitutes a valid need-to-know justification for CJI access in your environment. Example structure: "[Role] requires access to [specific CJI data set] to perform [specific business function]." Example: "Case analyst requires access to NCIC query results to perform background investigations for sworn officer applicants." Prohibit generic justifications that do not reference a specific data set or business function.

#### Evidence Required

An auditor will expect to see:

- **Quarterly access review reports** with reviewer certifications for each CJI-authorized account, completed every 90 days
- **CJI-authorized user roster** with roles, privilege levels, and need-to-know justifications for each account
- **Prerequisite compliance records** cross-referencing each CJI-authorized user with their PS-3 background check status, PS-6 Security Addendum status, and AT-2 training status
- **Access revocation records** showing accounts removed during or between quarterly reviews, with dates and reasons
- **Evidence of immediate revocation** for personnel separations, role changes, or prerequisite expirations (timestamps showing revocation within hours, not days or weeks)
- **Access review policy** documenting the quarterly cadence, reviewer assignment, certification requirements, and revocation procedures
- **IAM configuration** showing CJI access groups, permission sets, and the mechanism for enforcing access revocation (IAM Identity Center group removal, policy detachment, etc.)

#### Key Considerations

- **Quarterly reviews are the backstop, not the primary control.** The real-time revocation process (integrated with HR, provisioning/deprovisioning workflows) is the primary control. Quarterly reviews catch what the real-time process missed: role changes that were not communicated, contractor engagements that expired without notification, training that lapsed without triggering deprovisioning. If the quarterly review is catching a high volume of stale accounts, the real-time process needs improvement.
- **Prerequisite chain creates cascading revocations.** If a user's PS-3 background check expires and rescreening is not completed in time, their CJI access must be suspended regardless of their role or need-to-know. This means the quarterly review must check not just "does this person still need access?" but also "are all their prerequisites still current?" A lapsed training certificate (AT-2) or overdue background check (PS-3) is an access revocation trigger, even if the person's job function has not changed.
- **Separation of review duties.** Users must not certify their own CJI access. Managers reviewing their direct reports is standard practice, but consider whether a second-level review (data owner or CJIS Systems Officer) is warranted for privileged accounts (database administrators, system administrators with access to unencrypted CJI). This mirrors the dual-approval patterns common in IGA platforms.
- **Automation reduces review burden.** Manual quarterly reviews for a large user population (hundreds of officers across multiple agencies) become unsustainable. Automate the report generation, prerequisite compliance checking, and last-access-date calculation. Reserve human judgment for the certification decision itself: "Does this person still need this level of CJI access?"
- **Relationship to PS-3 and PS-6.** AC-2 quarterly reviews enforce the ongoing validity of PS-3 (personnel screening) and PS-6 (access agreements). A person who was properly screened and signed the Security Addendum at onboarding may fall out of compliance if rescreening is overdue or the addendum terms have changed. AC-2 is the recurring checkpoint that verifies the entire access authorization chain remains intact.
- **Relationship to AU-6.** AC-2 and AU-6 form a feedback loop. AU-6 weekly reviews detect who is actually accessing CJI. AC-2 quarterly reviews verify who is authorized to access CJI. Discrepancies between the two (access by unauthorized accounts, or authorized accounts with no access activity) are findings that require investigation. Implementing these controls together produces stronger assurance than either control alone.

---

## Incident Response

### IR-6 — Incident Reporting

**NIST 800-53 Rev 5 Control:** Require personnel to report suspected incidents to the organizational incident response capability within an organization-defined time period; and report incident information to organization-defined authorities.

**CJIS v6.1 Reference:** Incident Response (IR) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires incident reporting with two organization-defined parameters:

- **Reporting timeframe** (ir-06_odp.01) — the organization defines how quickly personnel must report suspected incidents to the internal incident response capability. FedRAMP High typically sets this at "immediately" for confirmed incidents and within specified hours for suspected incidents.
- **External reporting authorities** (ir-06_odp.02) — the organization defines who receives the incident information. For FedRAMP, the primary external authority is US-CERT (now part of CISA, the Cybersecurity and Infrastructure Security Agency). FedRAMP requires reporting to US-CERT/CISA within timeframes tied to the incident severity (US-CERT classifies incidents by functional impact and information impact, with reporting windows ranging from 1 hour for Level 1 incidents to 24 hours for lower-severity events).

FedRAMP incident reporting is oriented toward cyber threat intelligence and federal incident coordination. The reporting content focuses on technical details: indicators of compromise, tactics/techniques/procedures (TTPs), affected systems, attack vectors. The purpose is to enable US-CERT/CISA to warn other federal entities and coordinate a federal response.

#### CJIS v6.1 Delta

CJIS adds a parallel reporting chain for incidents involving CJI. The delta is in the authorities parameter (ir-06_odp.02), which must be expanded to include law enforcement-specific reporting channels:

- **Additional reporting to CJIS Systems Officer (CSO)** — each state's CJIS Systems Agency (CSA) designates a CSO who serves as the point of contact for CJIS incident reporting. Incidents involving CJI must be reported to the CSO of the state whose agencies' CJI was affected. The CSO is a law enforcement coordination role, not a general cybersecurity role. Note the acronym collision: CJIS Systems Officer (CSO) is different from Chief Security Officer (CSO) — in a CJIS context, CSO always refers to the CJIS Systems Officer.
- **Additional reporting to SIB Chief or Interface Agency Official** — depending on the state CSA's designation under CJIS v6.1 IR-6 (page 171), incidents must be reported to the State Identification Bureau (SIB) Chief or to a designated Interface Agency Official in addition to (or instead of) the CSO. The state CSA selects one or more recipients from this set. The FBI CJIS Division publishes the policy and is the federal authority responsible for CJIS oversight, but is not itself a designated incident-reporting recipient under IR-6 — any onward escalation to the FBI is the state CSA's responsibility, not the CSP's.
- **State-designated recipient set** — under CJIS v6.1 IR-6 (page 171), the recipients of incident reports are CSO, SIB Chief, or Interface Agency Official, as designated by each state CSA. The CSP's reporting obligation is satisfied by reaching the designated recipient(s) for each affected state. For a CSP serving multiple state agencies, this means tracking the designated recipient(s) per state CSA, which may differ between states.
- **State-defined reporting timeframes** — unlike US-CERT's standardized severity tiers with specific reporting windows, CJIS defers the reporting timeframe to the state CSA. Common timeframes range from immediate (within 1 hour for high-severity) to within 24 hours for lower-severity incidents. The CSP must confirm the specific timeframe with each state CSA it serves, and the most restrictive timeframe applies when a single incident affects multiple states.
- **Expanded incident content** — CJIS incident reports must include information beyond the standard cyber incident report: which specific CJI data sets were affected (NCIC, III, CHRI, fingerprint data, etc.), whether the compromised data relates to active investigations, whether officer or source safety is impacted, and the number of records affected. This content is more operationally sensitive than typical FedRAMP reports.

**Why this matters:** The CJIS reporting chain exists because US-CERT/CISA does not have law enforcement operational equities. When CJI is compromised, the impact is not just a cybersecurity incident — it may affect active investigations, undercover operations, protected witnesses, informants, victims (including minors), and suspect records. These are real people whose safety and ongoing legal proceedings may depend on the confidentiality of that data. The state CSA-designated recipient (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6) has the law enforcement context to assess those operational impacts and coordinate downstream notifications to affected agencies, officers, and individuals. A CSP that reports only to US-CERT and skips CJIS reporting has satisfied FedRAMP but failed CJIS — and the consequence is loss of CJIS authorization, which ends the CSP's ability to serve law enforcement customers.

#### Implementation Guidance

1. **Update the Incident Response Plan to include the CJIS reporting chain.** Document the full reporting flow for CJI-related incidents:
   - **Internal detection and triage** — how the incident is identified and classified as CJI-related.
   - **Internal reporting** — who on the incident response team is notified, and within what timeframe.
   - **Customer (agency) notification** — the CSP notifies the affected state and local agencies whose CJI was involved.
   - **State CSA-designated recipient notification** — the CSP or the affected local agency reports to the state CSA-designated recipient (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6, page 171) within the state-defined timeframe. Onward escalation within the state CSA (including any FBI CJIS Division notification) is the state CSA's responsibility.
   - **US-CERT/CISA notification** — standard FedRAMP reporting continues in parallel with CJIS reporting.
2. **Maintain current CSO contact information.** For each state the CSP serves, maintain the current contact information for the state CSA and CSO, including primary and backup contacts, phone numbers, email addresses, and after-hours contact procedures. CSO personnel change — verify contacts annually and after known CSA staffing changes.
3. **Document each state CSA's designated IR-6 recipient(s).** For each state the CSP serves, document which IR-6 recipient role(s) the state CSA has designated under CJIS v6.1 IR-6 (page 171): CSO, SIB Chief, or Interface Agency Official. A state CSA may designate one or more. Include role-by-role contact information in the IRP (primary, backup, and after-hours) for each designated recipient.
4. **Define what constitutes a CJI security incident.** A CJI security incident includes: unauthorized access to CJI (logical or physical), loss or theft of media containing CJI, unauthorized disclosure of CJI (internal or external), compromise of systems that store or process CJI (even if CJI exfiltration cannot be confirmed), and compromise of authentication credentials for CJI-authorized accounts. Document these triggers in the IRP so the response team can quickly classify an incident as CJI-related.
5. **Build incident report templates that satisfy both frameworks.** Create standardized incident report templates for CJI incidents that capture all information required by both FedRAMP (US-CERT classification, TTPs, IOCs) and CJIS (affected CJI data sets, operational impact, affected agencies, record counts). A single template with dual-purpose sections reduces the risk of omitting required content under time pressure.
6. **Conduct tabletop exercises that include CJIS reporting.** Test the CJIS reporting chain in tabletop exercises at least annually. Scenarios should include: CJI exfiltration, compromised CJI-authorized credentials, ransomware affecting CJI systems, and insider threat scenarios involving CJI access. Measure reporting timeliness to each state's designated recipient(s) (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6) as specific tabletop objectives. Document exercise results and any gaps identified.
7. **Establish communication channels for incident reporting.** Identify the communication channels for reaching each state CSA's designated recipient(s) during an incident: phone, encrypted email, secure portal. Verify these channels work during off-hours, since incidents often occur outside business hours. Test the channels periodically.

**AWS Implementation Note:** AWS Shared Responsibility means AWS handles security incidents affecting the underlying infrastructure (hypervisor, physical hardware, AWS service planes), while the customer (the CJIS-subject CSP) handles incidents at the application and data layer. AWS reports infrastructure incidents to the customer through AWS Security Hub, AWS GuardDuty, and AWS Support cases. The CSP is responsible for classifying whether an AWS-reported infrastructure incident has CJI impact and for initiating the CJIS reporting chain accordingly. Configure AWS GuardDuty, CloudTrail alerts, and Security Hub findings to route to the incident response team with clear tagging for CJI-containing resources (e.g., resource tags like `contains-cji: true`) so the response team can quickly determine whether an alert triggers CJIS reporting.

#### Evidence Required

An auditor will expect to see:

- **Incident Response Plan** with explicit CJIS reporting procedures, identifying each state CSA's designated recipient(s) (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6, page 171)
- **State CSA-designated recipient contact information** for each state the CSP serves, with primary, backup, and after-hours contacts documented and verified for each designated role (CSO, SIB Chief, and/or Interface Agency Official as designated)
- **CJI security incident definition** documenting what triggers CJIS reporting
- **Incident report templates** covering both FedRAMP and CJIS required content
- **Tabletop exercise records** demonstrating testing of the CJIS reporting chain, with exercise scenarios, participants, and lessons learned
- **Sample incident reports** (redacted) demonstrating dual reporting (US-CERT and CJIS) for past incidents, or training/exercise reports if no real incidents have occurred
- **State CSA recipient contact verification records** showing annual or periodic verification of designated-recipient contact information for each state served

#### Key Considerations

- **Acronym disambiguation.** In a CJIS context, "CSO" means CJIS Systems Officer. In general information security, "CSO" often means Chief Security Officer. Documentation, training materials, and incident procedures must use "CJIS Systems Officer (CSO)" on first mention and in any context where the distinction could be confused. A mis-directed incident report to the Chief Security Officer when it should have gone to the CJIS Systems Officer is a reporting failure.
- **Multi-state coordination complexity.** A CSP serving agencies in multiple states must maintain relationships with multiple CSOs. A single incident affecting data from agencies in California, Texas, and New York requires notification to three different CSOs, each with potentially different reporting timeframes and content requirements. The incident response team should have a playbook that maps customer agencies to their state CSA/CSO so the notification chain is not improvised during an incident.
- **Timing pressure is real.** State-defined reporting timeframes can be tight (1 hour for high-severity in some states). The internal triage process — from detection to classification as CJI-related to CSO notification — must be fast enough to meet the shortest applicable timeframe. If internal processes take 4 hours to triage and classify an incident, but the state requires CSO notification within 1 hour, the CSP is structurally unable to comply. Measure internal triage time in tabletop exercises.
- **Content sensitivity of CJIS reports.** CJIS incident reports may contain more operationally sensitive information than FedRAMP reports: identities of informants or undercover officers, specifics of active investigations, or details about protected witnesses. Ensure the communication channel to the CSO is encrypted and that the report content is handled with appropriate sensitivity. Do not transmit sensitive operational content through unsecured email or ticketing systems.
- **Coordination with the affected agencies.** The local or state law enforcement agencies whose CJI was affected have their own incident response obligations and stakeholder notifications (to victims, witnesses, involved officers). The CSP's incident reporting to the CSO is the trigger for the agency's downstream actions — which means the CSP's report must contain enough operational detail for the agency to act. Coordinate with major customer agencies in advance to understand what information they need in an incident notification.
- **Loss of CJIS authorization as a business risk.** Failure to report a CJI incident through CJIS channels, or delayed reporting that exceeds the state-defined timeframe, can result in a CJIS audit finding. Severe or repeated findings can lead to loss of CJIS authorization — the CSP can no longer serve law enforcement customers. For a CSP whose primary market is public safety, this is an existential business risk, not just a compliance gap.
- **Relationship to AU-6 and AC-2.** IR-6 often triggers from detections made during AU-6 weekly reviews (unauthorized CJI access, anomalous access patterns) or AC-2 quarterly reviews (accounts with CJI access that should have been revoked). The incident response team should have direct input channels from the AU-6 review process and the AC-2 review process, so findings from those controls escalate into IR-6 when warranted.
- **FedRAMP continuous monitoring integration.** FedRAMP requires continuous monitoring (ConMon) with incident reporting built in. The CJIS delta layers on top of the existing ConMon program — it adds reporting destinations, not a parallel program. Frame CJIS incident reporting as an enhancement to ConMon, not a separate compliance workstream.

---

## Physical and Environmental Protection

### PE-17 — Alternate Work Site

**NIST 800-53 Rev 5 Control:** Determine and document the alternate work sites allowed for use by employees; employ organization-defined controls at alternate work sites; assess the effectiveness of controls at alternate work sites; and provide a means for employees to communicate with information security and privacy personnel in case of incidents.

**CJIS v6.1 Reference:** Physical and Environmental Protection (PE) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires organizations to define and control alternate work sites. The baseline defers to organization-defined parameters for:

- **Allowed alternate work sites** (pe-17_odp.01) — the organization defines which alternate work sites are authorized for use (government facilities, employee residences, customer sites, etc.)
- **Controls at alternate work sites** (pe-17_odp.02) — the organization defines which security controls must be employed at alternate work sites

FedRAMP High is satisfied by documenting the types of alternate work sites allowed and the controls applied at those sites. The controls are left to the organization's discretion based on its risk assessment. For a typical FedRAMP-authorized cloud service, this often means: VPN required for remote access, endpoint protection on managed devices, and organizational policy prohibiting CJI storage on unmanaged devices. The baseline does not prescribe specific authentication strengths, specific VPN configurations, or specific BYOD restrictions.

#### CJIS v6.1 Delta

CJIS replaces the organizational discretion with specific prescriptive controls for remote CJI access. The delta recognizes that physical location security — which provides a layer of protection in a police station — cannot be assumed at alternate work sites:

- **Advanced Authentication is mandatory** — Advanced Authentication (AAL2-compliant MFA per IA-2) is required for all remote CJI access, regardless of the alternate work site's perceived security. This is not an organization-defined choice. Physical location security (being inside a secure facility) cannot be used as a compensating control to lower authentication requirements when CJI is accessed remotely. The reasoning: at an alternate work site, there is no guarantee of who else has physical access to the device or the workspace.
- **Encrypted VPN or equivalent secure connection required** — all network traffic carrying CJI to/from an alternate work site must be protected by an encrypted VPN or equivalent (VDI, zero-trust network access with equivalent cryptographic controls). Public networks (coffee shop WiFi, cellular data, hotel networks) cannot be trusted to carry CJI in clear text. The VPN or equivalent must use FIPS-validated cryptography (per SC-13).
- **BYOD (personally owned devices) restrictions** — personal devices used for CJI access must meet agency-defined security configuration standards. This typically includes: full-disk encryption, current endpoint protection, managed patch level, automatic screen lock, and remote wipe capability. Personal devices that do not meet the standard cannot be used for CJI access.
- **Restrictions on CJI storage on personally owned devices** — CJI must not be stored on personally owned devices unless the storage is encrypted with agency-managed keys AND the storage has been explicitly approved by the state CSA. The default is: do not store CJI on personal devices. Exceptions require both technical controls (agency-managed encryption) and administrative approval (CSA sign-off).
- **Physical environment considerations** — the alternate work site itself must provide reasonable protection against shoulder surfing, unauthorized viewing of CJI on screens, and physical access by non-authorized persons. This translates to practical requirements: screen privacy filters in public areas, session lock when unattended, not leaving devices unattended in vehicles, and not conducting CJI work in environments where conversation can be overheard.

**Why this matters:** A CSP operating under FedRAMP High may satisfy PE-17 by documenting remote access via VPN and organizational BYOD policy. CJIS requires the specific controls to be named and enforced: the MFA must be AAL2 phishing-resistant, the VPN must use FIPS-validated crypto, BYOD must meet agency standards, and CJI storage on personal devices is prohibited absent CSA approval. The delta is especially relevant because law enforcement has access patterns that generic FedRAMP users don't: sworn officers access CJI from patrol vehicles during traffic stops, from crime scenes, from homes during on-call shifts, and from emergency situations. These access patterns fall under "alternate work site" and must meet CJIS controls regardless of how brief or urgent the access is.

#### Implementation Guidance

1. **Document the approved alternate work site categories.** Define the types of alternate work sites authorized for CJI access: employee residences (for telework or on-call), law enforcement vehicles (for mobile field operations), government facilities other than the primary site, customer/agency sites during visits, and any other categories relevant to the CSP's operations. For each category, document the specific controls applied.
2. **Enforce AAL2 Advanced Authentication for all remote access.** Configure the identity provider to require AAL2-compliant MFA (phishing-resistant: FIDO2/WebAuthn, PIV/CAC, or hardware tokens) for authentication when the access originates from outside the primary site. Note: this should be enforced at the application layer, not just the VPN layer — a user who authenticates to the VPN with MFA but then uses a password-only session to the CJI application has not satisfied AAL2 at the point of CJI access.
3. **Deploy encrypted VPN infrastructure.** Implement a VPN solution using FIPS 140-2/3 validated cryptography. Document the VPN cipher suite configuration, authentication mechanism, and session timeout settings. If using an alternative to traditional VPN (VDI, zero-trust network access, cloud-delivered secure web gateway), document equivalent cryptographic controls. Verify the solution prevents split-tunneling for CJI traffic — all CJI access must be routed through the encrypted tunnel.

   **AWS Implementation:** For AWS-hosted CJI systems, consider AWS Client VPN with FIPS endpoints and AWS-managed certificates, or AWS Verified Access for zero-trust application access. For applications in private subnets, require access via PrivateLink or VPC endpoints to prevent internet-exposed CJI data paths. Configure the VPN/Verified Access with MFA integration (IAM Identity Center or external IdP with AAL2 enforcement).

4. **Establish BYOD policy with technical enforcement.** If BYOD is permitted for CJI access, define the security configuration requirements: full-disk encryption (FileVault on macOS, BitLocker on Windows, native encryption on mobile), current OS patch level, endpoint protection, automatic screen lock within defined timeout, and remote wipe capability through MDM enrollment. Enforce the policy technically through conditional access: devices that do not meet the standard cannot authenticate to CJI applications.

   **AWS Implementation:** Use AWS Verified Access with device trust signals from an MDM (Jamf, Intune, etc.) to enforce BYOD compliance at the access point. For applications, AWS IAM Identity Center can integrate with device trust signals through SAML assertions from the IdP.

5. **Prohibit CJI storage on personally owned devices by default.** Configure applications to prevent local data download or caching on personal devices. Where possible, use VDI or application streaming so CJI never leaves the server infrastructure. If CJI must be stored on a device (e.g., offline field operations), require agency-managed encryption and explicit CSA approval; document the approval chain and the technical implementation.
6. **Define physical environment guidelines.** Document the physical environment requirements for CJI access at alternate work sites: locked workspace when unattended, screen privacy considerations, no CJI conversation in public areas, devices not left unattended in vehicles. Include these in user training (ties to AT-2) and in the access authorization documentation.
7. **Provide incident communication channels.** Per the baseline requirement, provide employees with means to communicate security incidents while at alternate work sites. Document contact information for the CSP's incident response team, including after-hours contacts, and ensure this information is accessible from remote locations (not only on the internal network).

#### Evidence Required

An auditor will expect to see:

- **Alternate work site policy** documenting authorized site categories and the controls applied at each
- **Remote access architecture documentation** showing VPN/Verified Access configuration, MFA enforcement, and encryption specifications
- **BYOD policy** documenting required device security configurations and the enforcement mechanism
- **Conditional access configuration** showing device trust signals, MFA requirements, and access denial rules
- **VPN cipher suite exports** showing FIPS-validated cryptography in use
- **MFA enforcement configuration** showing AAL2 compliance at the application layer, not just network perimeter
- **CSA approval documentation** for any exceptions allowing CJI storage on personally owned devices
- **Incident communication contact information** accessible to remote personnel
- **User training records** covering physical environment guidelines for remote CJI access (overlaps with AT-2 evidence)

#### Key Considerations

- **Application-layer MFA is where implementations fail.** Many organizations enforce MFA at the VPN layer but allow password-only authentication to the application once the user is on the VPN network. This does not satisfy AAL2 for CJI access. The MFA must be enforced at the point of CJI access, which means the application itself or the IdP providing the application's authentication. An auditor will test this by authenticating to the VPN with MFA and then attempting to access the CJI application with password only — if it succeeds, this is a finding.
- **Mobile field operations create unique patterns.** Sworn officers accessing CJI from patrol vehicles during traffic stops need sub-second authentication for operational reasons. This is often implemented with hardware tokens (YubiKey, smart cards) rather than software MFA that requires typing a code. Document the authenticator types used in mobile field operations and verify they meet AAL2 phishing-resistance requirements.
- **Public safety exigent circumstances.** Some CJIS provisions allow for relaxed authentication in emergency situations (officer safety, imminent threat). These exceptions are narrow and documented in state CSA policy. They are not a general exemption — document any exigent access provisions explicitly and verify they are consistent with state CSA guidance.
- **BYOD is a hard policy choice.** The most defensible CJIS posture is: no BYOD for CJI access. All CJI access occurs on agency-issued devices with enforced configurations. BYOD is allowed in some environments but introduces significant complexity in compliance verification. If the CSP's model requires BYOD support (e.g., contractors using their own laptops), document the compensating controls thoroughly.
- **Split-tunneling is a common compliance gap.** A VPN that allows split-tunneling (CJI traffic through the VPN, other traffic direct) may expose the endpoint to threats from the direct-internet traffic while CJI traffic is on the VPN. Full-tunnel VPN or access that forces all traffic through inspected paths is more defensible.
- **Relationship to IA-2 and IA-5.** PE-17's Advanced Authentication requirement depends on IA-2 (Advanced Authentication) being implemented correctly. If IA-2 is not satisfied (e.g., authenticators are not AAL2, MFA is not phishing-resistant), PE-17 cannot be satisfied for remote access. These controls must be implemented together. Similarly, IA-5 (authenticator management) applies to the hardware tokens, certificates, and credentials used for remote CJI access.
- **Relationship to AT-2.** Remote CJI access training is a required component of CJIS security awareness training. Users accessing CJI from alternate work sites must be specifically trained on the physical environment guidelines, BYOD restrictions, and incident reporting procedures applicable to remote access. Document this overlap in training content.

---

## Awareness and Training

### AT-2 — Literacy Training and Awareness

**NIST 800-53 Rev 5 Control:** Provide security and privacy literacy training to system users as part of initial training for new users and at organization-defined frequency thereafter; update training content at organization-defined frequency; and incorporate lessons learned from security incidents into training content.

**CJIS v6.1 Reference:** Awareness and Training (AT) family

#### FedRAMP High Baseline Requirement

FedRAMP High requires security and privacy literacy training for all system users, including managers, senior executives, and contractors. The baseline defers to organization-defined parameters for:

- **Training frequency after initial training** (at-02_odp.01, at-02_odp.02) — FedRAMP typically sets this to "at least annually" for both security and privacy training.
- **Events triggering training** (at-02_odp.03, at-02_odp.04) — the organization defines events (system changes, new threats, policy updates) that trigger refresh training.
- **Awareness techniques** (at-02_odp.05) — the organization defines the techniques used to increase awareness (posters, logon banners, email advisories, phishing simulations).
- **Content update frequency and triggering events** (at-02_odp.06, at-02_odp.07) — the organization defines how often training content is refreshed and what events trigger content updates.

FedRAMP High is satisfied by providing annual security and privacy awareness training covering general topics (phishing, password hygiene, incident reporting, data handling). The baseline does not prescribe specific content topics beyond the general security/privacy scope, and it does not set a specific initial training deadline — initial training is required but the timeline is often "as part of onboarding" or similar.

#### CJIS v6.1 Delta

CJIS adds specific requirements around training timing and content, but — notably — the refresh *frequency* is actually less strict than FedRAMP:

- **Initial CJIS Security Awareness Training within 6 months of CJI access** — personnel authorized for CJI access must complete CJIS-specific security awareness training within 6 months of the initial CJI access authorization. This is unusual in that training can occur *after* access is granted, not strictly before. The rationale: onboarding delays for fingerprint-based background checks (PS-3) can already take weeks; requiring CJIS-specific training completion before access would cascade delays in operationally critical roles. However, the 6-month window is a hard deadline — personnel who do not complete training within 6 months must have CJI access suspended until training is completed.
- **Biennial (every 2 years) refresher training** — after initial training, CJIS requires refresher training every 2 years. This is **less frequent** than FedRAMP's typical annual cadence. The CJIS delta here is not about frequency (CJIS is less strict) but about content: the biennial refresher must cover CJIS-specific topics, not just generic security awareness. An agency providing annual FedRAMP-style training does not automatically satisfy CJIS biennial requirements if the content does not include CJIS-specific material.
- **CJIS-specific content requirements** — the training content must explicitly cover:
  - **CJI handling and dissemination rules** — what constitutes CJI, how it may be used, who it may be shared with, and the rules around dissemination (including the 28 CFR Part 20 dissemination restrictions on criminal history record information).
  - **Security Addendum obligations** — the terms of the CJIS Security Addendum (PS-6), including personal accountability, sanctions for violations, and the individual's responsibilities under the addendum.
  - **Incident reporting requirements for CJI** — the CJIS incident reporting chain to the state CSA-designated recipient (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6, page 171) and the user's role in reporting suspected incidents.
  - **Sanctions for policy violations** — the consequences of CJIS policy violations, which can include termination, criminal prosecution, and loss of certification. CJIS violations are not just administrative — they can be federal crimes under 18 USC 2721 (Driver's Privacy Protection Act) or state-specific criminal statutes for misuse of criminal justice data.
- **Training tied to the access authorization chain** — CJIS security awareness training status must be tracked per individual with CJI access. Expired or never-completed training is grounds for access suspension. This creates a dependency: CJI access (AC-2) depends on current training (AT-2), just as it depends on current background check (PS-3) and signed Security Addendum (PS-6).

**Why this matters:** A CSP operating under FedRAMP High likely has annual security awareness training, but the content is almost certainly generic — phishing, password hygiene, reporting suspicious activity. CJIS training content must explicitly cover CJI handling rules, Security Addendum obligations, CJIS-specific incident reporting, and sanctions. The 6-month initial training deadline adds a tracking burden: personnel with CJI access must be monitored for training completion within 6 months of access grant, and non-compliance must trigger access suspension. The biennial refresh is easier than the FedRAMP annual cadence, but only if the content actually covers CJIS topics — generic annual training does not satisfy the requirement.

#### Implementation Guidance

1. **Develop or acquire CJIS-specific training content.** Create training content covering the four required topic areas (CJI handling, Security Addendum, incident reporting, sanctions). Content sources include: state CSA-provided training materials (some states publish or distribute CJIS training content), commercial CJIS training vendors, or in-house developed content based on the CJIS Security Policy v6.1 Awareness and Training (AT) family. Ensure content is updated when CJIS policy changes (content must reflect current v6.x requirements, not v5.x).
2. **Track training status per individual with CJI access.** Maintain a training tracking system that records, for each CJI-authorized user: date of initial CJIS training completion, date of most recent biennial refresh, training content version, and completion status. Integrate the tracking system with the CJI-authorized user roster (from AC-2 implementation guidance) so training status is part of the quarterly access review.
3. **Implement the 6-month initial training deadline.** Create an automated workflow that flags CJI-authorized users who have not completed initial CJIS training within 6 months of access grant. The workflow should: send reminder notifications at 3, 5, and 6 months after access grant; escalate to the user's manager and the CJIS Systems Officer if training is not completed by the 6-month deadline; and automatically suspend CJI access upon expiration.

   **AWS Implementation:** For personnel who manage CJI infrastructure in AWS, tag IAM users or Identity Center users with training completion metadata (e.g., `cjis-training-completed: 2026-04-15`). Use Lambda scheduled functions to query the tags and flag users approaching or exceeding the 6-month deadline. For access suspension automation, Lambda can remove users from the CJI access permission set in IAM Identity Center.

4. **Implement biennial refresher automation.** Configure the tracking system to generate refresher notifications 2 years after the last completed training (with reminders at 21, 23, and 24 months). The content of the refresher must cover CJIS-specific topics, not just generic security awareness. If the organization delivers annual security awareness training for FedRAMP compliance, document which annual sessions include CJIS-specific content and serve as the biennial CJIS refresher.
5. **Document content coverage mapping.** Create a mapping showing how the training content addresses each required CJIS topic area. This is audit evidence: the auditor will want to verify that the training actually covers CJI handling, Security Addendum, incident reporting, and sanctions — not just that training was completed.
6. **Integrate with AC-2 quarterly reviews.** The quarterly access review process (per AC-2) must include verification of training currency. Any CJI-authorized user with expired training (exceeding 2 years since last completion) or overdue initial training (exceeding 6 months since access grant) must be flagged for access suspension during the review.
7. **Address training for alternate work site scenarios.** Per PE-17, users accessing CJI from alternate work sites need specific guidance on physical environment considerations, BYOD restrictions, and incident reporting. Include these topics in the CJIS training content, or provide supplemental training for remote CJI access users.

#### Evidence Required

An auditor will expect to see:

- **CJIS Security Awareness Training curriculum or content** covering the four required topic areas (CJI handling, Security Addendum, incident reporting, sanctions)
- **Content coverage mapping** showing how the training addresses each required CJIS topic
- **Training completion records** per individual with CJI access, including initial completion date and refresher dates
- **Evidence of initial training within 6 months of CJI access** — access grant dates cross-referenced with training completion dates
- **Evidence of biennial refresher compliance** — refresh dates showing no gaps exceeding 2 years
- **Training tracking system configuration** showing the deadline enforcement (6-month initial, 2-year refresh) and notification workflows
- **Access suspension records** for personnel whose training lapsed and whose CJI access was suspended as a consequence
- **Training content update records** showing content is refreshed when CJIS policy changes (e.g., v5.x to v6.x transition)

#### Key Considerations

- **Biennial vs. annual cadence — a rare case where CJIS is less strict.** Most CJIS deltas tighten FedRAMP requirements. AT-2 is a rare case where CJIS is actually less strict on frequency (2 years vs. FedRAMP's 1 year). However, an annual FedRAMP training cycle does not automatically satisfy CJIS unless the content explicitly covers CJIS topics. The simplest implementation: provide annual security awareness training with CJIS-specific content included in every second year's session, ensuring CJIS content coverage at least every 2 years. Alternatively, provide a dedicated CJIS-specific training module annually, which exceeds the CJIS minimum and avoids the complexity of alternating content cycles.
- **The 6-month deadline is forgiving but operationally demanding.** Unlike PS-3 (fingerprint check, which must precede access) or PS-6 (Security Addendum, which must precede access), AT-2 training can occur after access is granted. This is a concession to operational reality — police departments cannot wait 6 months for a new officer to complete training before the officer can access NCIC. But the 6-month window must be tracked and enforced. An organization that grants CJI access and never tracks training completion has satisfied AC-2 (account management) but failed AT-2 (training).
- **Sanctions content has legal weight.** The sanctions topic in CJIS training is not generic "you could be fired" language. CJIS violations can constitute federal crimes (18 USC 2721 for criminal history data misuse) or state criminal offenses. Training content should accurately reflect this — misrepresenting sanctions as merely administrative is both a training gap and a legal risk for the organization.
- **The Security Addendum content is specific.** The CJIS Security Addendum (PS-6) contains specific personal commitments the signatory makes regarding CJI handling, confidentiality, and sanctions for violations. Training must cover the addendum content so signatories understand what they committed to, not just that they signed something during onboarding. This is where PS-6 (the signed addendum) and AT-2 (training on its content) intersect.
- **Integration with the prerequisite chain.** CJIS access authorization depends on four prerequisites being satisfied: PS-3 (background check), PS-6 (Security Addendum), IA-2 (Advanced Authentication enrolled), and AT-2 (training current). During AC-2 quarterly reviews, all four prerequisites must be verified. If any is out of compliance, access must be suspended until remediated. AT-2 is the most likely to lapse quietly because training has an expiration date and personnel may not be actively tracking it.
- **Role-specific training considerations.** CJIS training requirements apply to all personnel with CJI access, but the level of detail may vary by role. A sworn officer querying NCIC needs different emphasis than a database administrator with logical access to CJI at rest. Consider role-based training tracks within the CJIS training program, with shared core content on dissemination rules, Security Addendum, and sanctions, and role-specific content on handling CJI in the user's operational context.
- **Phishing simulation integration.** If the organization conducts phishing simulations as part of awareness techniques (at-02_odp.05), ensure the simulations include CJI-relevant scenarios (e.g., fake credentials prompts for CJI systems, fake communications purporting to be from the CJIS Systems Officer). Generic phishing simulations do not reflect the threat landscape for law enforcement users.
- **Content versioning.** CJIS Security Policy has evolved (v5.x to v6.x was a significant update with alignment to NIST 800-53 Rev 5). Training content must be versioned and updated when policy changes. An organization delivering 2026 training with 2022-era content has not satisfied the content update requirement (at-02_odp.06).

---

## Control-Level Gaps

This section documents controls present in the CJIS v6.1 baseline but absent from the FedRAMP High baseline. Unlike the implementation-level deltas above, where the control exists in both baselines and CJIS imposes stricter parameters, these are entirely new controls a FedRAMP High environment must implement to satisfy CJIS.

Control-level gap candidates were initially identified by OSCAL baseline comparison between the CJIS v6.1 baseline (302 controls in tooling output) and the FedRAMP High baseline (410 controls). Tooling flagged 15 CJIS-only candidates. Verification against the published CJIS Security Policy v6.0 document (FBI CJIS Division, 2024-12-27) confirmed 12 of these as present in the v6.0 control set; three tooling-flagged candidates (SI-18, SI-18.4, SI-19 from the NIST 800-53 Rev 5 privacy overlay) are not in the published v6.0 control set and are therefore excluded from the analysis. Re-verification against v6.1 (released June 25, 2026) confirms both findings: the 12 gap controls remain in the v6.1 List of Priorities, and v6.1 removed SI-18/SI-19 from the list entirely. The 12 verified gap controls cluster around NIST 800-53 Rev 5 privacy requirements that CJIS v6.1 did adopt and FedRAMP High does not include.

Documentation for each control (baseline text, CJIS relevance, implementation guidance, evidence required) is grouped by cluster:

- **Privacy, Retention** (SI-12.1, SI-12.2, SI-12.3): CJI retention limits, minimization in testing/training/research, disposal procedures.
- **PII Limitation** (AU-3.3, PE-8.3, AC-3.14, SC-7.24): Limiting PII elements in audit records, visitor access records, individual access enforcement, and boundary protection.
- **Training and Incident Response** (AT-3.5, IR-2.3, IR-8.1): Role-based training on PII/CJI processing, breach-specific IR training, breach response plan.
- **Planning and Engineering** (PL-9, SA-8.33): Central management of security and privacy controls, minimization as an engineering principle.

OSCAL data for each control is captured in `data/cjis-overlay.json` with the `gap-type` property set to `control-level-gap` (distinguishing them from implementation-level deltas, which carry `gap-type: implementation-delta`).

---

### SI-12.1 — Limit Personally Identifiable Information Elements

**NIST 800-53 Rev 5 Control:** Limit personally identifiable information being processed in the information life cycle to the following elements of personally identifiable information: [organization-defined elements of PII].

**CJIS v6.1 Reference:** Information Management privacy overlay; applies to CJI as a class of sensitive PII.

#### FedRAMP High Baseline Requirement

Not included at this enhancement level. FedRAMP High includes the SI-12 base control (information management and retention, satisfied via NARA records retention schedules and organizational procedures) but does not include the privacy enhancement SI-12.1. FedRAMP High addresses PII through access controls (AC family), security and privacy attributes (AC-16), and physical access (PE-2) rather than by imposing a lifecycle-wide PII minimization requirement.

#### CJIS v6.1 Requirement

Controls must actively limit the PII elements processed across the CJI information lifecycle (creation, collection, use, processing, storage, maintenance, dissemination, disclosure, disposition) to an organization-defined list. The requirement is data minimization: only process PII elements required for operational purposes; exclude elements not operationally needed even when they are technically available.

CJI qualifies as PII because it includes direct identifiers (name, date of birth, SSN, biometrics) and criminal history data tied to identifiable individuals. CJIS v6.1 imports SI-12.1 to apply the minimization principle to CJI.

#### Implementation Guidance

1. **Enumerate CJI data elements.** Distinguish mandatory operational elements (for example, the NCIC query payload fields needed for a hit/miss response) from optional elements that upstream APIs return by default (photos, address history, secondary identifiers in a bundle).
2. **Define the allowed-elements list.** Document which specific CJI data elements the system processes at each lifecycle stage. Capture this in the SSP and system design. Elements not on the list must not be stored or processed even if the upstream API returns them.
3. **Enforce at ingest.** Filter incoming CJI payloads at the API gateway or ingest layer to strip unneeded elements before storage. Display-layer filtering is not sufficient since persisted-but-not-shown elements are still "processed" within the meaning of SI-12.1.
4. **Enforce at disclosure.** When CJI is returned to users or downstream systems, include only the allowed elements for the disclosure context. A fingerprint-based identity verification response does not need to include a full criminal history unless the operational purpose requires it.
5. **Review the allowed-elements list.** Review annually or when system boundaries change. Operational needs shift as workflows and integrations evolve.

#### Evidence Required

- **CJI data element inventory** listing elements processed at each lifecycle stage.
- **Design/architecture documents** showing where element filtering occurs (API gateway, database ingest, dissemination layer).
- **Sample records** or log extracts demonstrating excluded elements are not persisted.
- **Review records** showing periodic re-evaluation of the allowed-elements list.
- **Risk assessment output** informing which elements are in-scope versus out-of-scope under SI-12.1's organization-defined parameter (si-12.01_odp).

#### Key Considerations

- **Bulk-return API design.** Many NCIC and state CJIS query APIs return bundled records in a single response. SI-12.1 compliance requires filtering the bundle to only the elements needed by the requesting workflow, not passing the bundle through wholesale.
- **PII-in-log is silent retention.** Application logs and audit logs often capture PII elements unintentionally. Apply the minimization principle to log contents. This interacts with AU-3.3 (limit PII elements in audit records), another control-level gap in this analysis.
- **Secondary copies.** Minimization scope includes backups, DR copies, caches, and ephemeral working data. A system can satisfy minimization in production and violate it in backup snapshots. Include all data copies in the enforcement scope.
- **Field-level encryption is not minimization.** Encrypting an element still counts as processing it. Encryption is a layered protection, not a substitute for minimization. Decide first whether the element is needed; if yes, then apply encryption (see SC-28 implementation-level delta).
- **Parameter definition required.** SI-12.1 has an organization-defined parameter (si-12.01_odp). Blank parameters are an audit finding. The CSP or agency must define the in-scope element set explicitly.

---

### SI-12.2 — Minimize Personally Identifiable Information in Testing, Training, and Research

**NIST 800-53 Rev 5 Control:** Use the following techniques to minimize the use of personally identifiable information for research, testing, or training: [organization-defined techniques].

**CJIS v6.1 Reference:** Information Management privacy overlay; applies to CJI in non-production contexts.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High includes general development safeguards (CM-4 security impact analysis, SA-3 system development life cycle) but does not require PII minimization in test, training, or research environments. Production data in test environments is a common anti-pattern that is not explicitly prohibited by FedRAMP alone.

#### CJIS v6.1 Requirement

Apply defined techniques to minimize PII use in non-production contexts (research, testing, training). The control recognizes that these contexts typically do not require real production PII to fulfill their purpose, and that using real PII in them multiplies exposure surface area (developer laptops, training rooms, research outputs, shared test environments).

Techniques in scope:
- **De-identification**: transforming records so the individual is no longer identifiable.
- **Synthetic data**: machine-generated records that mimic production structure without containing real values.
- **Data masking or tokenization**: replacing sensitive elements with placeholders while preserving format for shape-dependent testing.
- **Subset sampling with legal basis**: rare; requires explicit authorization and typically additional controls.

#### Implementation Guidance

1. **Default to synthetic CJI in non-production.** Build a reference synthetic dataset with realistic structure (names, DOB, case IDs) that test systems can use for integration testing, UAT, performance testing, and training.
2. **Prohibit production CJI in dev/test.** Policy plus technical enforcement: block export operations from production, require explicit approval gating, segregate network paths so production-to-non-production data flows are observable and restrictable.
3. **Mask when real data is unavoidable.** Certain performance tests require near-production volume or data distribution that synthetic generation cannot reproduce. In those cases, mask direct identifiers (name, SSN, fingerprint templates, photos) and the identifying link columns. Unmasked CJI in test is a finding regardless of intent.
4. **Train with scenarios, not case files.** CJIS system training should use synthetic case scenarios. Pulling a real historical case as training material (even an old closed case) is a minimization violation.
5. **Governance for research use.** If the CSP or agency conducts research on CJI workflows (effectiveness studies, usability testing), require IRB-equivalent review and de-identification before research use.

#### Evidence Required

- **Synthetic dataset documentation** describing the generation method and coverage of test scenarios.
- **Policy prohibiting production CJI in non-production environments.**
- **Technical controls** enforcing the policy (database export restrictions, network segregation, audit logs of cross-environment data transfers).
- **Training material samples** showing synthetic rather than real case data.
- **Research governance records** if applicable (IRB-equivalent review output, de-identification method documentation, research dataset retention records).

#### Key Considerations

- **Minimization is a technique selection, not a binary.** The control requires defining techniques; the CSP chooses which apply to which context. Synthetic-data-only is the strongest posture. Masking is weaker because re-identification may be possible with auxiliary information. Document the technique per context.
- **De-identification consistency.** When de-identification is selected as the technique, apply it consistently across datasets. SI-19 formalizes de-identification as a separate control in NIST 800-53 Rev 5 but is not in the CJIS v6.1 control set; CJIS treats de-identification as one of several SI-12.2 minimization techniques rather than an independent obligation.
- **Training environments are often overlooked.** Agencies running CJIS training often use a stripped-down copy of production. Stripped-down is not minimized unless direct identifiers are removed by an explicit technique.
- **CSP dev/test boundary.** If the CSP runs dev/test environments on behalf of agencies, the CSP inherits the SI-12.2 obligation. Ensure customer CJI does not flow into CSP dev/test and that vendor-side test data is synthetic or masked.

---

### SI-12.3 — Information Disposal

**NIST 800-53 Rev 5 Control:** Use the following techniques to dispose of, destroy, or erase information following the retention period: [organization-defined techniques].

**CJIS v6.1 Reference:** Information Management privacy overlay; disposal of CJI and CJI-bearing artifacts (logs, backups, archives).

#### FedRAMP High Baseline Requirement

Not included at the disposal-enhancement level. FedRAMP High includes MP-6 (media sanitization) for physical media disposal and SC-28 (protection of information at rest) for storage encryption. Neither imposes an explicit logical information disposal mandate — the active erasure or cryptographic destruction of information records when the retention period expires. FedRAMP's SI-12 base control treats retention generally without specifying how disposal executes at end-of-retention.

#### CJIS v6.1 Requirement

Use defined techniques to dispose of, destroy, or erase information at the end of the retention period. Scope includes originals, copies, archived records, and system logs that may contain PII or CJI. Disposal must be an active, scheduled, and evidentiable process rather than an informal "we delete when we clean up."

Typical disposal techniques:
- **Logical erasure** with verified overwrite (secure delete utilities, database TRUNCATE plus vacuum, file-system zero-fill).
- **Cryptographic erasure** (destruction of the encryption key rendering the ciphertext permanently unrecoverable; the practical disposal technique for cloud-hosted archives where physical destruction is impossible).
- **Physical destruction** for end-of-life media (satisfied by MP-6 implementation-level delta procedures).

#### Implementation Guidance

1. **Define retention periods per CJI data class.** Document retention for each CJI category (active-case records, closed-case archives, audit logs, incident records, backup copies). Without explicit periods, "end of retention" is undefined and disposal cannot be triggered on schedule.
2. **Select disposal technique per data class.** Logical erasure for active-system records, cryptographic erasure for cloud-hosted archives, physical destruction for end-of-life hardware. Document the mapping.
3. **Automate disposal where possible.** Scheduled disposal jobs (for example, AWS S3 Lifecycle policies that transition and then delete after N days) reduce the risk of retained-past-period records. Manual-only disposal scales poorly and frequently misses archive copies.
4. **Include logs, backups, caches.** Disposal applies to all copies of the record, including audit logs that captured CJI (intersects with AU-3.3), database replicas, backup snapshots, DR copies, and ephemeral caches. A record disposed in the primary database but preserved in a nightly backup is not disposed within SI-12.3's meaning.
5. **Produce disposal evidence.** Logs showing the disposal event (what was disposed, when, by which technique). Without evidence, disposal cannot be asserted at audit.

#### Evidence Required

- **Retention schedule** per CJI data class.
- **Disposal procedures** documenting the technique applied per class.
- **Disposal logs and reports** showing execution — lifecycle policy run reports, secure-delete verification output, key-destruction records for cryptographic erasure.
- **Cross-copy coverage evidence** — documentation that backups, DR copies, and log archives are included in the disposal scope and schedule, not excluded by omission.
- **Media destruction certificates** for physical disposal events (coordinates with MP-6).

#### Key Considerations

- **Cryptographic erasure in cloud environments.** Destroying an AWS KMS customer-managed CMK renders ciphertext in S3, EBS, or RDS permanently unrecoverable. This is often the only practical erasure mechanism for cloud-hosted archives where physical media destruction is not possible. Requires key hierarchy design (see SC-12 implementation-level delta) that supports targeted key destruction without collateral data loss.
- **Legal holds override disposal.** Records under litigation hold must not be disposed even when the retention period expires. Integrate legal-hold awareness into the disposal automation; a blind lifecycle policy that deletes on schedule regardless of hold status is non-compliant.
- **Log-retention tension.** AU-6 implementation-level delta requires 1-year minimum retention for CJI audit events; SI-12.3 requires disposal at retention end. The reconciliation: dispose at exactly 1 year plus any extension, not earlier (would violate AU-6) and not later (would violate SI-12.3 minimization principle).
- **Backup retention alignment.** Backup systems often retain for years for DR purposes. A 7-day retention on an active database plus a 2-year retention on its nightly backup is an inconsistency — the backup retains what the active system has disposed. Align backup retention with the disposal schedule or document the deliberate offset and its legal/operational basis.
- **Cloud provider snapshot copies.** Some cloud services retain snapshots or transit copies that the customer does not directly control (for example, AWS S3 versioning history, RDS automated backups). Understand the provider's data lifecycle and ensure provider disposal mechanisms align with SI-12.3, or contractually flow down the obligation to the provider.

---

### AU-3.3 — Limit Personally Identifiable Information Elements (Audit Records)

**NIST 800-53 Rev 5 Control:** Limit personally identifiable information contained in audit records to the following elements identified in the privacy risk assessment: [organization-defined elements].

**CJIS v6.1 Reference:** PII-in-log minimization; intersects with AU-6 (implementation-level delta requiring weekly review and 1-year retention).

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's AU-3 base control requires specific content in audit records (timestamp, event type, source, outcome, identity) but does not impose PII minimization within those records. FedRAMP audit records can therefore contain significant PII, bounded only by the AU-3 minimums and organizational practice.

#### CJIS v6.1 Requirement

Audit records must contain only the PII elements identified as necessary in the privacy risk assessment. The intent is that log contents themselves do not become a secondary privacy exposure. For CJI, audit logs typically need to record who queried what case, when, from where, and the action's outcome — not the full query response payload.

#### Implementation Guidance

1. **Conduct the privacy risk assessment for audit records.** RA-3 output defines which PII elements are permissible in logs. Typical permitted set: user identifier, action, object identifier (case ID, record ID), timestamp, source IP or host. Typical excluded set: full CJI payload, fingerprint template data, full criminal history return, photo data.
2. **Separate identity from content.** Log the object ID, not the object content. The audit log says "user X accessed record Y at time T"; the content of record Y is not stored inline in the log. If content is needed for investigation, reconstruct via the record ID against the primary data store.
3. **Sanitize at the logging layer.** Application code that writes audit records should construct log payloads from the permitted-elements list explicitly, not dump the full request/response object. Implicit logging (Python `logger.info(request)` with a full PII-bearing object) is a common source of leakage.
4. **Apply to aggregated and exported logs.** If audit data is exported to a SIEM or central logging platform, the minimization applies to those copies too. Masking or transformation before export is preferable to retroactive redaction.
5. **Reconcile with AU-6 retention.** CJIS requires 1-year minimum retention for CJI audit events. Minimized logs are still subject to this. The interplay: minimize content, preserve necessary elements, retain for the full period.

#### Evidence Required

- **Privacy risk assessment output** (RA-3) defining permitted audit record elements for AU-3.3 parameter (au-03.03_odp).
- **Audit record schema** documenting the permitted element set.
- **Sample audit records** showing permitted elements only; no full CJI payloads.
- **SIEM or central logging configuration** demonstrating minimization in exported copies.
- **Code review or logging library standards** showing sanitization at the logging boundary.

#### Key Considerations

- **Tension with thorough audit.** A responder investigating a suspicious access may want the full query payload, not just the object ID. Design the logging architecture to support just-in-time retrieval of the content via the object ID rather than preserving it inline. This preserves investigative capability without inflating the audit log's privacy risk.
- **Log volume and retention cost.** Paradoxically, minimization reduces storage costs and eases 1-year retention compliance (AU-6 implementation-level delta) since logs are smaller.
- **Propagation into SIEM.** If CJI-minimized logs feed a SIEM, the SIEM's privacy posture inherits the minimization. If the SIEM enriches with additional context (geolocation, user profile), those enrichments must not reintroduce excluded PII.

---

### PE-8.3 — Limit Personally Identifiable Information Elements (Visitor Access Records)

**NIST 800-53 Rev 5 Control:** Limit personally identifiable information contained in visitor access records to the following elements identified in the privacy risk assessment: [organization-defined elements].

**CJIS v6.1 Reference:** PII-in-visitor-log minimization; applies to facilities where CJI is stored or processed.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's PE-8 base control requires visitor access records to be maintained for a defined period, with defined content (name, purpose of visit, name of escort, date/time). FedRAMP does not require minimizing PII within those records beyond the baseline content.

#### CJIS v6.1 Requirement

Visitor access records for facilities hosting CJI must contain only the PII elements identified in the privacy risk assessment as operationally necessary. Excess identifiers (for example, SSN, DOB, full driver's license number) must not be collected or retained in visitor logs if they are not required for the access control purpose.

#### Implementation Guidance

1. **Define permitted visitor record elements via RA-3.** Typical permitted set: name, employer or agency affiliation, purpose of visit, escort, date/time of entry/exit. Typical excluded set: SSN, DOB, full driver's license number, photograph (unless operationally required for access control).
2. **Update visitor management system configuration.** Many commercial visitor management systems capture by default more than is needed. Configure the system to collect only the permitted elements.
3. **Physical logs (paper sign-in sheets) follow the same rule.** If the facility uses paper visitor logs, the form must not request excluded elements.
4. **Align with retention and disposal.** Visitor records are subject to retention schedules. When they reach end-of-retention, apply SI-12.3 disposal techniques. Visitor records are a small but real surface for PII retention drift.
5. **Communicate the collection rationale.** If visitors ask why specific elements are collected (or not collected), staff should be able to cite the privacy risk assessment rationale.

#### Evidence Required

- **Privacy risk assessment output** (RA-3) defining permitted visitor record elements for PE-8.3 parameter (pe-08.03_odp).
- **Visitor management system configuration** or sign-in form showing the limited element set.
- **Sample visitor records** demonstrating compliance.
- **Retention and disposal documentation** for visitor logs.

#### Key Considerations

- **Escort visits to data centers hosting CJI.** Many cloud-hosted CJIS deployments involve CSP-operated data centers that rarely if ever have agency personnel on-site as visitors. PE-8.3 applies nonetheless to whatever visitor logs exist (for example, CSP-side maintenance vendor visits, agency audit visits, inspectors). The CSP's visitor logging practice is in scope.
- **Agency-operated facilities (command centers, evidence rooms).** Agencies operating their own CJI-hosting facilities have a more direct PE-8.3 obligation. Visitor traffic is typically higher and the log scrutiny from CJIS auditors is more visible.
- **Badge-reader logs versus sign-in logs.** Electronic access logs from badge readers typically do not contain PII beyond badge ID, which is not typically considered PII unless linked to the cardholder directly. Those are usually out of PE-8.3 scope, but the linkage table (badge ID to cardholder) that can re-link is in scope for other controls (AC-2, AC-3).

---

### AC-3.14 — Individual Access

**NIST 800-53 Rev 5 Control:** Provide [organization-defined mechanisms] to enable individuals to have access to the following elements of their personally identifiable information: [organization-defined elements].

**CJIS v6.1 Reference:** Subject access to own PII; law-enforcement records exemption recognized in supplemental guidance.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High does not require a subject-access mechanism. U.S. subject access rights are sector-specific (Privacy Act for federal agency records, HIPAA for health, GLBA for financial) and FedRAMP does not generalize them.

#### CJIS v6.1 Requirement

Provide a mechanism enabling individuals to access the organization-defined elements of their own PII. For CJI specifically, the NIST supplemental guidance explicitly recognizes that law enforcement records may be exempt from disclosure under Privacy Act section (j)(2) or state analogues. The control therefore operates as: provide the mechanism; apply the statutory exemptions when responding.

AC-3.14 addresses the access side of subject rights (I want to see what you have about me). The correction and deletion side is handled by state expungement law and agency-specific processes rather than by a dedicated CJIS v6.1 control. Individuals typically exercise access first and pursue correction through the relevant state mechanism if inaccuracies are found.

#### Implementation Guidance

1. **Define the access mechanism.** Typically coordinated with the state CSA. Forms, authentication requirements, fees (if any), response SLAs, and redaction policy should be documented. Exemptions must be pre-catalogued so the response can cite them.
2. **Authenticate the requester.** Subject access requires strong identity verification — a requester is asking for another person's record if identity is not verified. Typical mechanisms: notarized request, in-person verification with government ID, or AAL2 electronic identity proofing (coordinates with IA-2 implementation-level delta which requires AAL2 for CJI access).
3. **Route to privacy and legal for adjudication.** Senior agency official for privacy, legal counsel, and often the CJIS Systems Officer review the request. The adjudication determines what is released, what is redacted, what is withheld under exemption.
4. **Respond with cited exemptions.** If elements are withheld, cite the exemption source (statute or regulation). A plain "no" without citation is non-compliant with typical Privacy Act practice.
5. **Track the requests.** Volume, response time, approval/partial-approval/denial breakdown; metrics feed privacy program reporting.

#### Evidence Required

- **Documented access mechanism** (forms, authentication requirements, fees, SLA, redaction policy).
- **Exemption register** cataloguing applicable statutory exemptions.
- **Sample request records** showing the full workflow (intake, authentication, adjudication, response with citations).
- **Aggregate metrics** for access requests received and resolved.

#### Key Considerations

- **Law-enforcement records exemption is broad, not absolute.** The Privacy Act (j)(2) exemption applies to maintained systems of records principally compiled for criminal law enforcement purposes. Not every CJI system qualifies; apply the exemption rigorously per statute, not reflexively.
- **Partial disclosure is common.** Rather than full denial, many responses release non-sensitive elements (for example, arrest date and disposition category) while withholding investigative narrative, informant identity, or other sensitive elements. Partial disclosure requires a more complex redaction workflow.
- **Identity proofing is the hard part.** Weak authentication at the request intake means someone can request another person's criminal history. Strong identity proofing is operationally burdensome but compliance-critical. Coordinate with IA-2 implementation-level delta's AAL2 guidance for online mechanisms.
- **Chilling effect to avoid.** An overly burdensome access mechanism may effectively deny the right in practice. Reasonable authentication should not be confused with insurmountable authentication. Courts have found pretextual denial via impossible process to violate subject-access rights.

---

### SC-7.24 — Personally Identifiable Information at Boundaries

**NIST 800-53 Rev 5 Control:** For systems that process personally identifiable information: apply the following processing rules to data elements of personally identifiable information: [organization-defined rules]; monitor for permitted processing at external interfaces and at key internal boundaries; document each processing exception; and review and remove exceptions that are no longer supported.

**CJIS v6.1 Reference:** Boundary-processing rules for CJI; enforcement and monitoring at system interfaces.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's SC-7 base control requires boundary protection (firewalls, DMZ architecture) but does not require PII-specific processing rules with exception tracking. FedRAMP's PII boundary posture is generic rather than PII-aware.

#### CJIS v6.1 Requirement

Systems processing CJI must:
- Define processing rules per CJI data element (what operations are allowed: read, write, dissemination to specific destinations, transformation, retention).
- Monitor for compliance at external interfaces (for example, API gateway for NCIC queries, state CJIS network interface) and at key internal boundaries (for example, between the CJIS application tier and a database tier, between primary and replica systems).
- Document exceptions where processing deviates from the rules.
- Periodically review the exception list and remove stale exceptions.

#### Implementation Guidance

1. **Define processing rules per CJI element class.** Example: "Driver's license numbers may be queried by dispatch; they must not be exported to non-dispatch systems; they must be masked in analytics outputs." Rules are organization-defined (sc-07.24_odp) and must be documented in the SSP.
2. **Enforce at technical boundaries.** API gateways should be configured with per-element policy. Inter-tier communication should enforce rules (for example, a dispatch tier may not send raw fingerprint data to an analytics tier). This often requires policy-as-code approaches (for example, OPA/Rego at API gateways) that the CSP or agency can demonstrate.
3. **Monitor at boundaries.** Instrument the boundary with telemetry that records processing attempts and rule evaluation outcomes. This becomes the evidence trail for audit.
4. **Exception workflow.** When a processing rule must be deviated from (for example, a short-lived integration with a new system), document the exception: what rule, what scope, what compensating control, what expiration date. Exceptions without expiration drift into permanent policy violations.
5. **Exception review cadence.** Organization-defined; typical quarterly review. Expired exceptions must be closed (either by aligning practice with the rule, extending the exception with justification, or ending the deviating practice).

#### Evidence Required

- **Processing rules documentation** per CJI element class (sc-07.24_odp parameter value).
- **Boundary configuration** (API gateway policy, inter-tier enforcement rules).
- **Monitoring telemetry** showing rule evaluation at boundaries.
- **Exception register** listing each active exception with scope, compensating control, and expiration.
- **Exception review records** documenting quarterly (or defined-frequency) reviews and closure of stale exceptions.

#### Key Considerations

- **Policy-as-code is the practical enforcement.** Ad-hoc "don't send PII across this boundary" is unenforceable at scale. OPA/Rego, API gateway policy engines, or service-mesh policy provide evaluable rules. This aligns with FedRAMP 20x compliance-as-code direction.
- **Monitor volume can be very high.** Every CJI query is potentially a boundary evaluation. Sampling or aggregate telemetry may be necessary; full per-request logging may be prohibitive. Design the monitoring plan to balance evidentiary value with operational cost.
- **Exception drift is the primary failure mode.** Exceptions created for good reasons become permanent in practice because no one reviews. The review cadence is the control's backstop. Without it, SC-7.24 becomes a policy that everyone exempts in practice.
- **Ties to SI-12.1 (limit PII elements).** SI-12.1 defines what elements are in-scope; SC-7.24 enforces processing rules on those elements at boundaries. The two controls compose: SI-12.1 is the minimization principle, SC-7.24 is the enforcement mechanism at system edges.

---

### AT-3.5 — Role-Based Training on Processing PII

**NIST 800-53 Rev 5 Control:** Provide [organization-defined personnel or roles] with initial and [organization-defined frequency] training in the employment and operation of personally identifiable information processing and transparency controls.

**CJIS v6.1 Reference:** Role-based PII processing training; distinct from general awareness training (AT-2 implementation-level delta).

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High requires AT-3 role-based training (security responsibilities tied to role) and general awareness training (AT-2) but does not impose a specific role-based training obligation for PII processing and transparency controls. FedRAMP's role-based training focuses on security, not privacy.

#### CJIS v6.1 Requirement

Provide initial and recurring role-based training to defined personnel and roles on PII processing and transparency controls. "Processing" includes the full lifecycle (creation, collection, use, storage, dissemination, disposition); "transparency controls" include the authority to process PII, privacy policies, system of records notices, privacy impact assessments, and information-sharing agreements.

Distinguish AT-3.5 from AT-2 (the existing implementation-level delta):
- **AT-2** = broad CJIS awareness training for everyone with CJI access (dissemination rules, sanctions, Security Addendum content).
- **AT-3.5** = role-based training for personnel whose duties include PII processing activities (privacy officer, CJIS Systems Officer, auditors, DPO-equivalent roles, data engineers working with CJI).

#### Implementation Guidance

1. **Define the target roles (at-03.05_odp.01).** Typical roles: senior agency official for privacy (or state equivalent), CJIS Systems Officer, privacy program staff, auditors, database administrators with CJI access, application developers working on CJI processing code. General CJI-query users are usually scoped to AT-2, not AT-3.5.
2. **Define the refresher frequency (at-03.05_odp.02).** Typical cadences: annual, biennial. The CSA may define state-specific frequency.
3. **Build role-specific training content.** Content should cover the CSP's or agency's authority to process CJI, applicable privacy notices, dissemination agreements, privacy impact assessments, and the role's specific obligations. Generic privacy training does not satisfy role-based training.
4. **Integrate with AT-3 role-based training.** Many CSPs/agencies already deliver role-based security training (AT-3). Add a privacy module so role-based training covers both dimensions.
5. **Track completion per role.** Rosters, completion dates, refresher schedules, and any role-entry gating (training required within N days of role assignment).

#### Evidence Required

- **Defined role list** (at-03.05_odp.01 parameter value).
- **Defined refresher frequency** (at-03.05_odp.02 parameter value).
- **Training content** specific to PII processing and transparency controls.
- **Completion rosters** per role with dates.
- **Integration documentation** showing how AT-3.5 fits with AT-2 (awareness) and AT-3 (role-based security).

#### Key Considerations

- **Distinct from AT-2.** AT-2 is "everybody learns CJIS awareness." AT-3.5 is "people whose job is PII processing get extra training on the processing-and-transparency controls." Do not collapse these into one training track; the audit expects both.
- **Privacy impact assessment literacy.** Personnel covered by AT-3.5 should be able to read and act on a privacy impact assessment relevant to their role. Training should include exposure to real PIAs, not just the concept.
- **Transparency controls for CJI are narrower than for general PII.** Many traditional transparency mechanisms (system of records notices, privacy notices on websites) are constrained or exempt for law enforcement records. Training should cover what transparency applies and what is carved out under Privacy Act (j)(2) and state analogues. Do not teach general-PII transparency practice as if it directly applies to CJI.
- **Coordinate with the state CSA.** The state CSA may have specific role-based training requirements beyond AT-3.5's floor. Confirm.

---

### IR-2.3 — Breach Response Training

**NIST 800-53 Rev 5 Control:** Provide incident response training on how to identify and respond to a breach, including the organization's process for reporting a breach.

**CJIS v6.1 Reference:** Breach-specific IR training; complements IR-6 implementation-level delta (reporting channels) and IR-8.1 (plan content).

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's IR-2 base requires general incident response training. FedRAMP does not require training specifically on breach identification and response, where "breach" is narrowed to PII-involving incidents.

#### CJIS v6.1 Requirement

Provide incident response training specifically on breach identification, response, and reporting. A breach for PII purposes is loss of control, compromise, unauthorized disclosure, unauthorized acquisition, or access by an unauthorized user — or authorized user acting outside authorized purposes. For CJIS, any incident that exposes or potentially exposes unencrypted CJI qualifies.

Training content covers: recognizing a breach versus a lesser incident, reporting obligations (who to notify, in what timeframe), tabletop exercises simulating breach scenarios, and the organization's breach response workflow.

#### Implementation Guidance

1. **Incorporate into existing IR training (IR-2 base).** Most CSPs/agencies already run IR training annually. Add a breach module covering breach definition, recognition, reporting channels (CSO, SIB Chief, or Interface Agency Official per CJIS v6.1 IR-6 page 171), and time-sensitive obligations.
2. **Run breach-specific tabletop exercises.** Scenario: an administrator's credentials are compromised and are observed to have queried CJI for non-case-related purposes. Walk the team through detection, containment, assessment of scope, notification triggering, and remediation.
3. **Cover the "authorized user, unauthorized purpose" case.** Many CJI breaches are insider misuse (looking up an ex-spouse, a public figure, a neighbor). Training must address this as a breach, not just external compromises.
4. **Cover reporting-to-individuals considerations.** When the breach affects identifiable individuals, the IR team must engage with the IR-8.1 notice-determination process. Training connects IR-2.3 to IR-8.1 operationally.
5. **Track and refresh.** IR training is typically annual; CJIS IR-2.3 should align with that cadence.

#### Evidence Required

- **IR training curriculum** documenting the breach module.
- **Tabletop exercise records** from breach-specific simulations (scenario, participants, observations, improvement actions).
- **Completion rosters** for IR-2.3 training per IR team member.
- **Integration with IR-6 implementation-level delta reporting channels** documented in training material.

#### Key Considerations

- **Insider misuse is the underrecognized breach class.** Law enforcement agencies have a long record of personnel running queries on family, romantic interests, public figures, or people involved in off-duty disputes. These are breaches. Training must frame them as such and connect to sanctions (Security Addendum commitments, 18 USC 2721 criminal liability where applicable).
- **The 72-hour reporting instinct.** Many staff associate privacy breach reporting with the GDPR 72-hour window. CJIS has its own reporting timeframes (typically faster for initial notification to the CSO). Training should cover the specific CJIS reporting clock, not a generic privacy-law clock.
- **Distinguish breach from incident.** Not every incident is a breach. A failed phishing attempt blocked by email filtering is an incident; a successful phishing attempt that did not expose PII may or may not be a breach depending on the data at risk. Training must cover the distinction so the team does not over-report or under-report.
- **Ties to IR-6.** CJIS v6.1 IR-6 (page 171) requires reporting to the CSO, SIB Chief, or Interface Agency Official. IR-2.3 training reinforces the reporting chain; staff should know who to call, at what number, within what timeframe, with what information.

---

### IR-8.1 — Incident Response Plan for Breaches

**NIST 800-53 Rev 5 Control:** Include the following in the Incident Response Plan for breaches involving personally identifiable information: a process to determine if notice to individuals or other organizations is needed; an assessment process to determine the extent of harm, embarrassment, inconvenience, or unfairness to affected individuals and any mechanisms to mitigate such harms; and identification of applicable privacy requirements.

**CJIS v6.1 Reference:** Breach-specific IR Plan content; operates alongside IR-6 (reporting channels) and IR-2.3 (training) to close the breach-response loop.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's IR-8 base requires an Incident Response Plan with general content (incident classes, roles, procedures, metrics). FedRAMP does not require the plan to include breach-specific process content per IR-8.1.

#### CJIS v6.1 Requirement

The IR Plan must include three specific breach-response elements:
1. **Notice determination process** — decide whether individuals, other organizations, or oversight bodies need to be notified; who makes the decision, using what criteria, within what timeframe.
2. **Harm assessment process** — evaluate harm (financial, reputational, safety) to affected individuals and identify mitigation mechanisms (credit monitoring, identity protection, corrective record action).
3. **Applicable privacy requirements identification** — catalog the privacy statutes, regulations, or policies that apply to a given breach type (for CJI: CJIS v6.1 IR-6 and IR-8(1), state breach notification statutes, Privacy Act exemptions, agency-specific requirements).

#### Implementation Guidance

1. **Write a breach-specific appendix or section of the IR Plan.** Separate from general incident response workflow. Breaches have distinct obligations (notification, harm assessment, regulator engagement) that the general IR workflow does not address adequately.
2. **Define the notice determination process.** Decision tree: what data was exposed, to whom, for how long, with what likelihood of misuse. Outcome: notify individuals? notify the CSO, SIB Chief, or Interface Agency Official (per CJIS v6.1 IR-6)? notify state attorney general (if state breach law applies)? notify media?
3. **Define the harm assessment process.** Inputs: nature of exposed data (criminal history, fingerprints, investigation details), affected population size and characteristics, exposure duration and visibility. Outputs: harm categorization (low/medium/high) and mitigation mechanism selection.
4. **Catalog applicable privacy requirements per breach type.** Matrix or table: breach type (for example, unauthorized access to criminal history by insider; CJI exposed externally via misconfigured storage; third-party contractor compromise) mapped to applicable statutes and CJIS Security Policy sections.
5. **Rehearse and revise.** The IR-8.1 content is aspirational until exercised. Run breach tabletop exercises using the plan; update based on friction observed.

#### Evidence Required

- **IR Plan breach section or appendix** with the three required elements.
- **Notice determination decision tree** or equivalent structured workflow.
- **Harm assessment framework** with examples showing application to typical CJI breach scenarios.
- **Applicable privacy requirements matrix** mapping breach types to statutes and CJIS Security Policy sections.
- **Tabletop exercise results** demonstrating the plan has been rehearsed.
- **Revision history** showing the plan has been updated based on exercise outcomes or real incidents.

#### Key Considerations

- **Notice-to-individuals is operationally heavy.** Determining who to notify requires knowing which individuals' CJI was exposed. If the audit log did not capture the specific records accessed during the breach (interacts with AU-3.3 and AU-6), the notice scope may be unknowable. The IR-8.1 plan must either assume worst-case (notify all plausibly affected) or rely on logging evidence (integration with AU-6 implementation-level delta).
- **Harm framing for CJI is non-standard.** Traditional breach harm framing (credit risk, identity theft) applies loosely to CJI. CJI-specific harms include public embarrassment (criminal history exposure), safety risk (witness/informant identity exposure), and judicial consequences (exposure of sealed records). Harm assessment should use CJI-specific categories, not generic PII categories.
- **State variance in breach notification law.** State breach notification statutes vary in trigger thresholds, notice content, regulator engagement, and timing. A CSP serving multiple states must cover the union of state obligations. The applicable-privacy-requirements matrix is more complex for multi-state CSPs than for single-state agencies.
- **CJIS v6.1 Incident Response (IR) family is the source.** The IR family in CJIS v6.1 (published policy pages 167-174) contains the breach reporting and plan content requirements. IR-6 defines the reporting chain (CSO, SIB Chief, or Interface Agency Official per v6.1 page 171) and IR-8(1) defines the breach-specific plan content. CJIS v6.1 reorganized from v5.9.x and no longer uses numbered "Section 5.X" policy areas for IR; map the IR Plan workflow to these specific v6.1 controls directly.
- **Interplay with IR-6 implementation-level delta.** IR-6 covers who is notified per CJIS v6.1 page 171 (CSO, SIB Chief, or Interface Agency Official). IR-8.1 covers the process the plan documents for breach response. The two controls are complementary; both should be explicitly mapped in the plan.

---

### PL-9 — Central Management

**NIST 800-53 Rev 5 Control:** Centrally manage [organization-defined security and privacy controls and related processes].

**CJIS v6.1 Reference:** Central management of selected CJI-relevant security and privacy controls; common-controls-as-a-service model.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High accepts the concept of common controls (inherited from the CSP) but does not mandate that specific controls be centrally managed. The CSP's SSP describes control inheritance; there is no FedRAMP obligation to centralize management of privacy controls specifically.

#### CJIS v6.1 Requirement

Centrally manage a defined set of security and privacy controls and related processes. The goal is organization-wide standardization: rather than each system team implementing AC-2 account management, AT-2 training, AU-6 audit review, or SI-12.3 disposal individually, the controls are managed centrally and inherited.

For CJI environments, central management typically takes one of two shapes:
- **CSP-side**: The CSP centrally manages common controls (training, screening, audit log aggregation, continuous monitoring) and offers them as inherited controls to agency tenants via the SSP.
- **Agency-side**: The state CSA or a central agency privacy program centrally manages CJIS-specific controls (background check process, Security Addendum administration, quarterly access reviews) across the agency's subordinate components.

#### Implementation Guidance

1. **Define the centrally managed control set (pl-09_odp).** Candidates explicitly listed in NIST supplemental guidance include AC-2, AT-2/3, AU-3/6/7/11, CA-2/3/7, CM family, SI-2/3/4. Add CJIS-specific items: dissemination logging, Security Addendum administration, fingerprint check workflow.
2. **Document inheritance in the SSP.** For each centrally managed control, the SSP must specify the managing entity (CSP or agency), the inheriting systems, the evidence produced centrally, and the responsibility split for hybrid controls.
3. **Build the central management capability.** This is often a combination of tooling (IAM system for AC-2, LMS for AT-2, SIEM for AU-6, central compliance tool for continuous monitoring) and organizational structure (privacy office, CSO office, CJIS Systems Officer).
4. **Operate at the authorizing boundary.** Central management supports the independence needed for assessment; if the same team implements and assesses, independence is in question. Central management, when coupled with independent assessment, supports ongoing authorization.
5. **Measure inheritance coverage.** Track which systems inherit which centrally managed controls. Gaps are implicit risk. Report coverage to leadership as a compliance metric.

#### Evidence Required

- **Defined centrally managed control set** (pl-09_odp parameter value).
- **Inheritance documentation** in the SSP per control.
- **Central management tooling evidence** (IAM system configuration, LMS records, SIEM deployment, continuous monitoring platform).
- **Organizational chart** showing the central management functions and reporting relationships.
- **Coverage metrics** showing which systems inherit which centrally managed controls and any gaps.

#### Key Considerations

- **This is FedRAMP 20x territory.** FedRAMP 20x KSIs favor centrally managed, continuously monitored controls over per-system attestations. PL-9 is the NIST 800-53 Rev 5 hook that CJIS v6.1 uses for the same outcome. A CSP investing in FedRAMP 20x readiness is directly positioning for CJIS PL-9 compliance.
- **CSP versus agency central management boundary.** In multi-tenant CJIS deployments, the CSP centrally manages infrastructure-level controls; the agency centrally manages agency-specific processes (Security Addendum, fingerprint submission, access reviews). The boundary is contractual and must be documented.
- **Audit efficiency.** Centrally managed controls are assessed once and inherited across all consuming systems, rather than assessed per system. This compresses audit cost and time. For agencies running multiple CJIS systems, central management is pragmatic.
- **Central-management failure mode: brittleness.** A single centrally managed training platform outage blocks access for all consuming systems. Central management trades independence for efficiency; redundancy and continuity planning must compensate.
- **Integration with continuous monitoring.** Central management and continuous monitoring compose well: centralize the controls, centralize the evidence collection, centralize the reporting. This is the pattern for KSI-driven FedRAMP 20x and for a mature CJIS compliance posture.

---

### SA-8.33 — Minimization as an Engineering Principle

**NIST 800-53 Rev 5 Control:** Implement the privacy principle of minimization using [organization-defined processes].

**CJIS v6.1 Reference:** Privacy minimization during system design and acquisition; applies before system build, not as a retrofit.

#### FedRAMP High Baseline Requirement

Not included. FedRAMP High's SA-8 base control requires security engineering principles during development but does not require minimization as a privacy-specific engineering principle. Privacy engineering is not part of the FedRAMP High SA-family baseline posture.

#### CJIS v6.1 Requirement

Implement the privacy principle of minimization — only process PII that is directly relevant and necessary, and only maintain it as long as necessary — via defined engineering processes. The control engages at system design, acquisition, and development time, not only at operational runtime.

This is the architectural counterpart to the runtime minimization controls (SI-12.1 limit PII elements, SI-12.2 minimize PII in testing/training/research, SI-12.3 disposal). SA-8.33 says: before you build or acquire a system, bake minimization into the design.

#### Implementation Guidance

1. **Adopt privacy-by-design in the SDLC.** Every system design document or acquisition spec that touches CJI must include a minimization analysis: what PII is required, why, how long, with what lifecycle controls. Without this analysis, the project should not proceed to build.
2. **Define the engineering processes (sa-08.33_odp).** Typical processes: privacy design review, PII data flow analysis, PIA completion prior to design approval, architectural review board with a privacy reviewer, acquisition gate requiring vendor-side minimization evidence.
3. **Integrate with FedRAMP SA-8 and SA-15 processes.** Most CSPs already run a security engineering review (SA-8); extend it to include privacy minimization as a named review criterion.
4. **Vendor and COTS acquisition.** Many CJIS systems include COTS components or vendor-supplied modules. The acquisition process must verify that vendors support minimization (can filter elements, respect retention settings, expose disposal APIs). Acquisition evidence is part of compliance.
5. **Tie to PIA (Privacy Impact Assessment).** A PIA is often the artifact documenting minimization analysis. PIAs should be mandatory for systems processing CJI and revisited during major changes.

#### Evidence Required

- **Defined engineering processes** (sa-08.33_odp parameter value).
- **Privacy design review records** for systems processing CJI.
- **PIA documentation** covering minimization analysis.
- **Architectural review board minutes** showing privacy reviewer participation.
- **Acquisition evidence** showing vendor minimization capability was verified (contract language, capability demonstrations, test results).

#### Key Considerations

- **Minimization is easier in design than in retrofit.** A system built to process every CJI element returned by NCIC is hard to retrofit to process only a subset. A system designed with element filtering at ingest is trivially compliant. SA-8.33 captures this architectural reality.
- **Ties the privacy cluster together.** SA-8.33 is the design-time hook for the runtime minimization controls: SI-12.1 (elements), SI-12.2 (testing/training/research), SI-12.3 (disposal), SC-7.24 (boundary processing), AU-3.3 (audit record elements), PE-8.3 (visitor record elements). SA-8.33 says: design for all of these from the start.
- **COTS vendor diligence.** Many police records management systems, dispatch platforms, and evidence management tools are COTS. If the vendor does not support element filtering, configurable retention, or disposal APIs, the acquisition is a compliance problem. Acquisition reviewers should include minimization capability as a scored criterion.
- **Interacts with FedRAMP 20x KSI metrics.** FedRAMP 20x emphasizes continuous, measurable controls. Minimization is measurable (element count processed per lifecycle stage, retention age distribution, disposal event frequency). SA-8.33 engineering processes should generate these metrics.
- **Public-safety mission tension.** Law enforcement often argues that more data is better for investigative effectiveness. SA-8.33 constrains that with the directly-relevant-and-necessary floor. Resolving the tension requires explicit design decisions, not gut-feel data hoarding. Training personnel on SA-8.33's minimization principle is part of the broader AT-3.5 role-based privacy training loop.

---

## Methodology

### Source of truth

The authoritative source for the CJIS v6.1 control set in this analysis is the published CJIS Security Policy v6.1 document (FBI CJIS Division, 2024-12-27). The control set is the list of controls referenced in the document's Section 5 (Policy and Implementation) Table of Contents.

Baseline-comparison tooling, including the usfed-compliance MCP `compare_baselines` output for `cjis-v6` vs `fedramp-high`, was used as a starting point to identify candidate implementation-level deltas and control-level gaps. Tooling output is not authoritative. When tooling output disagrees with the published document, the published document governs.

### Verification process

Each control candidate is verified by:

1. Confirming the control's presence in the CJIS v6.1 Section 5 ToC.
2. Confirming the control's baseline status in FedRAMP High (either present and differing in parameters — implementation-level delta — or absent — control-level gap).
3. Reading the control text in CJIS v6.1 to confirm the nature of the delta or gap matches the analysis.

### Known tooling-versus-document discrepancies discovered during build

During the initial build of this gap analysis, three controls (SI-18, SI-18.4, SI-19 from the NIST 800-53 Rev 5 privacy overlay) appeared in tooling output as CJIS-only baseline controls. Verification against the published v6.0 document found that these three are not in the v6.0 control set, and v6.1 removed them from the List of Priorities entirely. They are excluded from the analysis. The cluster "Privacy, Quality and De-identification" was therefore removed from the scope; the remaining privacy cluster is "Privacy, Retention" (SI-12.1, SI-12.2, SI-12.3).

This discrepancy is documented here as a methodology caution: future contributors should verify tooling claims against the published v6.x document before extending the analysis.

### Section references

CJIS v6.1 reorganized from v5.9.x. Prior versions used numbered Policy Areas ("Section 5.3 Incident Response", "Section 5.13 Mobile Devices"). Version 6.x organizes Section 5 by NIST 800-53 Rev 5 control family (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PS, RA, SA, SC, SI, SR) with Policy Area 1 (Information Exchange Agreements) and Policy Area 20 (Mobile Devices) as the only numbered Policy Areas retained. References in this analysis use control identifiers (e.g., IR-6, SI-12(1)) and cite page numbers from the published document rather than v5.9.x-style Section 5.X numbering.
