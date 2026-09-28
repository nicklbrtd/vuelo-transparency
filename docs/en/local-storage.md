# Local storage

English · [Русский](../ru/local-storage.md)

Last reviewed: 2026-09-28<br>
Status: Current

## What is encrypted

The E2EE protocol store keeps Signal identity/session records, prekeys, E2EE message history, attachment state, and the durable outbox in an SQLCipher-backed database. The database master key is stored in Apple Keychain with device-only accessibility. The database directory and database file use iOS complete file protection in the current source.

Saved Messages uses a separate random AES-GCM key in Keychain with device-only accessibility. Session tokens are stored in Keychain.

## What this does not establish

SQLCipher is not the app's universal local database in the reviewed implementation. This review does not establish encryption at rest for every app cache, every legacy message, ordinary preferences, media preview, downloaded plaintext file, or backup. The app uses standard preferences for non-secret settings and other local state.

## When the device is unlocked

To display a message, the client must make its plaintext available to the app. An attacker controlling an unlocked device or the app process may access available content. iOS file protection and Keychain accessibility reduce some risks; they do not replace E2EE or an independent device-security assessment.

## Backups

No end-to-end encrypted backup and recovery flow was confirmed in the reviewed code. Do not assume that app data is recoverable across a new device or that any system backup is protected by Vuelo-held cryptographic guarantees.
