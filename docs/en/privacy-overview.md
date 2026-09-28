# Privacy overview

English · [Русский](../ru/privacy-overview.md)

Last reviewed: 2026-09-28<br>
Status: Current<br>
Applies to: current development code reviewed on 2026-09-28; production deployment and end-to-end runtime have not been verified.

## What Vuelo aims to protect

Vuelo is developing private messaging. The current code routes one-to-one text conversations through a Signal Protocol transport using LibSignalClient. This code path is wired into the current send and receive flow, but its production deployment and complete runtime behavior have not been independently confirmed. See [security status](security-status.md).

## What is protected today

- Authenticated sessions are stored locally in Apple Keychain.
- One-to-one message code encrypts message and control-event content on the sending device before it is submitted to delivery infrastructure.
- The corresponding received content is decrypted on the recipient device and written to an SQLCipher-backed store used for this E2EE path.
- Saved Messages has a separate AES-GCM encrypted vault with a device-local Keychain key.
- The outgoing voice-message path in one-to-one chats uses an attachment-encryption flow. This does not establish encryption coverage for every media type or chat kind.

These are source-code findings, not an independent audit or proof that every production service is configured as expected.

## What is not currently covered

- Group and channel message flows are not covered by the current one-to-one E2EE transport.
- Existing legacy messages remain on the legacy server-backed path and may be plaintext.
- E2EE attachment coverage is partial; do not assume every file, image, video, preview, or voice message is encrypted.
- Complete local encryption of every Vuelo data store has not been established.
- End-to-end encrypted backups and multi-device Signal session transfer have not been established.
- No independent third-party security audit has been completed.

## Where plaintext exists

Plaintext necessarily exists briefly in memory on a sending or receiving device while a person composes or reads a message. The E2EE message history and protocol state are stored in the SQLCipher-backed local store. Other app data and legacy message paths are not covered by that statement. A compromised unlocked device can expose content available to that device.

## What the server can see

For current E2EE one-to-one delivery, the server receives ciphertext and routing information required to deliver it. The service also handles account and device identifiers, conversation membership, event timing and ordering, and profile information required by current product features. Network services can observe connection metadata such as IP address. Public documentation does not claim that all such metadata is retained or hidden.

For group and legacy paths, the current code does not provide the same E2EE content boundary. Details are in [data and metadata](data-and-metadata.md).

## Security direction

The target is to expand verified end-to-end protection, minimize metadata, and make security claims match observable behavior. Goals are not current guarantees. Each area is tracked separately in the [security status](security-status.md) and [known limitations](known-limitations.md).
