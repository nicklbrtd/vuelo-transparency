# Security status

English · [Русский](../ru/security-status.md)

Last reviewed: 2026-09-28<br>
Documentation revision: initial public source review<br>
Applies to: current development code reviewed on 2026-09-28; production deployment not verified.

Statuses describe code wiring found in the repository. They do not mean that an independent reviewer has verified the implementation.

| Area | Status | Current boundary |
|---|---|---|
| Authentication | Implemented · Not independently audited | Account authentication uses server-backed sessions. |
| Session storage | Implemented · Not independently audited | Session tokens are stored in Apple Keychain on the device. |
| One-to-one text E2EE | In validation · Not independently audited | Current source wires text and control events through LibSignalClient. Runtime and deployed-server behavior remain unverified. |
| Group and channel E2EE | Planned | Current message paths do not use the one-to-one E2EE transport. |
| Attachments | Partial · Not independently audited | Encryption is wired to outgoing voice messages in one-to-one chats. Full media coverage is not established. |
| Saved Messages | In validation · Not independently audited | A separate AES-GCM vault stores content as ciphertext on the server; its key is device-local. |
| Local message storage | Partial · Not independently audited | SQLCipher is used for the E2EE protocol store, messages and outbox. This does not establish encryption of all app data. |
| Device trust | Partial · Not independently audited | Device registration, approval and revocation flows exist. Complete E2EE device lifecycle and revocation guarantees are not established. |
| Key verification between people | Planned | No user-verifiable safety-number or key-transparency flow was confirmed in the reviewed code. |
| Backups | Planned | End-to-end encrypted backup flow was not found. |
| Remote push notifications | Planned | No current remote-push delivery path was confirmed in the reviewed client and migrations. |
| Independent audit | Not yet completed | No independent third-party audit has been completed. |

## Interpretation

“In validation” means the code path exists and is connected to a user-facing path, but production deployment or end-to-end behavior still needs confirmation. “Partial” means the mechanism covers only a subset of data or flows. “Planned” is a target, not a current feature.

Existing one-to-one legacy history is not retroactively made end-to-end encrypted by the newer transport. The server can retain legacy plaintext content. A successful E2EE send path does not prove every historic record, group, attachment, or device path has the same protection.

## Review scope

This is a static review of the current private source tree and checked-in dependency versions. It did not inspect production databases, live server configuration, released binaries, runtime traffic, or private audit results. It is not an independent security audit.
