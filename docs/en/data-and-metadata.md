# Data and metadata

English · [Русский](../ru/data-and-metadata.md)

Last reviewed: 2026-09-28<br>
Status: Current

The table describes current code paths reviewed in the private source tree. “Not established” means this review did not confirm a complete flow or deployment behavior.

| Data | Device | Server or delivery service | Protection and current status |
|---|---|---|---|
| One-to-one message content | Plaintext while composing and reading; E2EE history in encrypted local store. | Ciphertext for the current E2EE path; older legacy records may be plaintext. | In validation · Not independently audited. |
| Group and channel message content | Available to participating clients. | Current message flow can store plaintext. | Not covered by current E2EE transport. |
| Attachments | Plaintext may exist in source/destination files during handling. | Encrypted upload is wired for one-to-one outgoing voice messages; other media coverage is not established. | Partial. |
| Reactions, edits, deletes and receipts | Processed on device. | Current one-to-one control events are carried through the E2EE envelope path; legacy/group paths differ. | In validation. |
| Account identifier and authentication state | Session token in Keychain. | Account/session service processes identifiers and authentication requests. | Server-side account data is not E2EE. |
| Public Vuelo ID, username and profile information | Cached/displayed by the client. | Profile and directory features require server-side profile data. | Not E2EE. |
| Device public key material and trust state | Private device key material is held on device; public material is registered remotely. | Public key and device-routing data are processed for device registration and delivery. | Partial; no claim that this is key transparency. |
| Conversation membership and routing IDs | Used by the client. | Required by the service to authorize and route messages. | Metadata; not hidden by message E2EE. |
| Event timestamps, sequence and ciphertext size | Visible as part of message handling. | Delivery infrastructure handles ordering/timing and ciphertext payload size. | Metadata; minimization and retention are not established here. |
| IP and network connection metadata | Network stack may expose it to the service. | A service receiving a connection can observe connection metadata. | Retention and third-party processing were not verified. |
| Push notification routing token | No current remote-push path was confirmed in reviewed code. | Not established. | No claim about collection or payload privacy. |
| Local database and preferences | E2EE data is in SQLCipher-backed storage; preferences also exist in ordinary app storage. | Not applicable. | Partial; not all local app data is covered by SQLCipher. |
| Session and private keys | Sensitive session and selected private key material is held in Keychain. | Private keys are not intended to be sent to the service. | Code review confirms specific stores, not every secret lifecycle. |
| Backups | No E2EE backup flow was confirmed. | Not established. | Planned in the internal target architecture; not a current guarantee. |

## Metadata E2EE does not automatically hide

Even when message text is encrypted, delivery may require account and device identifiers, conversation membership, event ordering and time, and a ciphertext object or envelope. Network providers may observe connection-level information. Encryption of content is not anonymity, and this repository does not claim otherwise.

## Retention

This source review did not verify production retention periods, server logs, backups, analytics pipelines, or third-party provider retention. Vuelo will document those separately once verified.
