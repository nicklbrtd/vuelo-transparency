# Frequently asked questions

English · [Русский](../ru/faq.md)

Last reviewed: 2026-09-28<br>
Status: Current

### Is Vuelo open source?

No. Vuelo's application source code and backend implementation are currently private. This repository publishes public privacy, security, and transparency documentation only. See [source status](source-status.md).

### Why is the client source not public?

Vuelo is in active development. The project is publishing clear documentation about current privacy behavior and limitations without publishing the application source or its internal structure. No date or commitment to open the full application is being made.

### Does Vuelo use the Signal Protocol?

The current one-to-one message code path uses the official LibSignalClient bindings for Signal Protocol primitives. Vuelo implements its own application, transport, and storage integration. Production deployment and runtime behavior remain in validation, and no independent audit has been completed.

### Can Vuelo read my messages?

The current one-to-one E2EE code path sends ciphertext to delivery infrastructure. This repository does not make that promise for group or channel messages, legacy history, or all media. See [known limitations](known-limitations.md).

### Can the server see who I talk to?

The delivery service processes account/device routing and conversation membership. E2EE protects content in the covered path; it does not hide all metadata.

### Are group chats protected the same way?

No. Group and channel flows are not covered by the current one-to-one E2EE transport.

### Are attachments encrypted?

The outgoing one-to-one voice-message path is connected to attachment encryption. Complete coverage for all media types, previews, and legacy paths has not been established.

### What happens when a device is revoked?

The app has device approval and revocation features. This public review has not established complete cryptographic revocation behavior for every E2EE session or pending message.

### Are backups end-to-end encrypted?

No end-to-end encrypted backup flow was found in the reviewed code. Do not assume one exists.

### Has Vuelo been independently audited?

No. No independent third-party security audit has been completed yet.
