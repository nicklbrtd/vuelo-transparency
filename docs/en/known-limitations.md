# Known limitations

English · [Русский](../ru/known-limitations.md)

Last reviewed: 2026-09-28<br>
Status: Current

This page describes user-relevant limits, not instructions for exploiting a vulnerability.

| Limitation | Area | Status | Confidentiality impact |
|---|---|---|---|
| Group and channel conversations are not covered by the current one-to-one E2EE transport. | Messaging | Current limitation; group E2EE is planned. | Their current server-backed message path does not have the one-to-one content guarantee. |
| Existing legacy one-to-one history may remain server-side in plaintext. | Message history | Current limitation | Historical content is not retroactively encrypted by the new transport. |
| Attachment encryption coverage is partial; the current one-to-one voice-message path is wired, while complete coverage for every media type is not established. | Media | Partial / in validation | Do not assume every uploaded media object is ciphertext. |
| Complete SQLCipher coverage of all local app data has not been established. | Local storage | Partial | Other caches, preferences, legacy data, or plaintext media files may have different protections. |
| User-verifiable contact-key checking and key transparency were not confirmed. | Identity | Not established | Users cannot rely on this repository to claim independent key verification. |
| Complete multi-device E2EE and device-revocation guarantees were not established. | Devices | Partial / in validation | Do not assume every device lifecycle edge case is covered. |
| End-to-end encrypted backup and recovery were not found. | Backups | Planned | No recovery or cross-device backup confidentiality claim is made. |
| Production migration/configuration and complete runtime E2EE behavior were not checked in this review. | Deployment | In validation | Source wiring does not prove a live environment is configured identically. |
| No independent third-party security audit has been completed. | Assurance | Not yet completed | No external audit assurance is claimed. |
| Remote push delivery and notification payload handling were not confirmed. | Notifications | Not established | No privacy guarantee about remote notification payloads is made. |

Known limitations are revisited when a relevant user-visible flow or backend contract changes.
