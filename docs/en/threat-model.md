# Threat model

English · [Русский](../ru/threat-model.md)

Last reviewed: 2026-09-28<br>
Status: Current

This public model describes broad security boundaries. It intentionally omits internal service maps, database schema, and operational details.

| Threat | What Vuelo attempts to protect | Current status and limits |
|---|---|---|
| Network observer | Message content while it travels between devices and delivery infrastructure. | One-to-one E2EE code is wired in the current source; deployment and runtime validation remain open. Connection metadata is not hidden by E2EE. |
| Stolen server data | One-to-one E2EE message content and Saved Messages vault content. | Ciphertext is used by these paths. Legacy messages, group messages and uncovered media may remain readable server-side. |
| Compromised backend or operator | E2EE content in protected one-to-one flows. | The server receives ciphertext on the wired E2EE path. Metadata and legacy plaintext remain outside that guarantee. |
| Stolen locked device | Secrets and content protected by iOS device security and app-level controls. | Keychain and file protection are used for specific E2EE material. This does not prove every app file is encrypted or inaccessible. |
| Compromised unlocked device | Limit exposure where possible. | No client-side E2EE can protect plaintext displayed or processed on a fully compromised unlocked endpoint. |
| Malicious or revoked device | Prevent unauthorized devices from receiving future protected content. | Device approval and revocation code exists, but complete E2EE revocation behavior is not established. |
| Account takeover | Reduce unauthorized access through authenticated sessions and device controls. | Authentication and device controls exist; resistance to every takeover scenario has not been independently assessed. |
| Metadata analysis | Minimize exposure beyond what delivery requires. | Account, routing, membership, timing, ordering, network and size metadata may be observable. No anonymity claim is made. |
| Malicious application build | Make the distributed client match reviewed code. | Source is private and reproducible-build verification is not currently offered. A malicious client could access plaintext on the endpoint. |

## Out of scope

This document does not claim protection against compromised operating systems, coercion, screenshots, recipient copying, traffic analysis, or plaintext already present in legacy flows. It is not a formal cryptographic proof or audit report.
