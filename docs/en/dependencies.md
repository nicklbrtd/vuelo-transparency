# Security-relevant dependencies

English · [Русский](../ru/dependencies.md)

Last reviewed: 2026-09-28<br>
Status: Current

Versions below were checked in the current private repository's dependency lock/configuration on 2026-09-28.

| Dependency | Used for | Version | Upstream |
|---|---|---|---|
| LibSignalClient | Signal Protocol bindings used by the one-to-one message transport. | 0.97.1 | [signalapp/libsignal](https://github.com/signalapp/libsignal) |
| SQLCipher.swift | Encrypted local E2EE protocol/message store. | 4.16.0 | [sqlcipher/SQLCipher.swift](https://github.com/sqlcipher/SQLCipher.swift) |
| Apple CryptoKit | AES-GCM, SHA-256, and P-256 APIs used by named features. | Provided by the Apple OS SDK | [Apple documentation](https://developer.apple.com/documentation/cryptokit) |
| Apple Security / Keychain Services | Local credential and selected private-key storage, plus secure random bytes. | Provided by the Apple OS | [Apple documentation](https://developer.apple.com/documentation/security) |
| Apple LocalAuthentication | Optional local app authentication and device-pairing approval. | Provided by the Apple OS | [Apple documentation](https://developer.apple.com/documentation/localauthentication) |

This list is not a complete software bill of materials. It excludes ordinary UI and networking packages unless they directly affect the described security boundary. Dependency versions and licensing must be reviewed again for each public release.
