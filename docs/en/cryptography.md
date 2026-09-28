# Cryptography

English · [Русский](../ru/cryptography.md)

Last reviewed: 2026-09-28<br>
Status: Current

This list is limited to primitives and libraries confirmed in the current source. It describes use, not independent validation.

| Primitive or provider | Purpose | Current status |
|---|---|---|
| Signal Protocol via LibSignalClient | One-to-one message session establishment and message encryption/decryption, using the official bindings. | In validation · Not independently audited. |
| Signal signed prekeys and one-time prekeys | Public prekey bundle setup in the current one-to-one transport. | In validation. |
| Kyber prekey material through LibSignalClient | Included in the current prekey setup. This repository does not independently claim a particular post-quantum security guarantee. | In validation. |
| AES-GCM through Apple CryptoKit | Saved Messages vault and chunked attachment encryption. | Partial · Not independently audited. |
| SHA-256 through Apple CryptoKit | Ciphertext digest for encrypted attachment integrity checks. | Partial. |
| P-256 through Apple CryptoKit / Secure Enclave | Separate device signing and key-agreement identity, when available. | Partial. |
| Apple Keychain and Security framework | Local storage for selected session and key material; secure random bytes for the Saved Messages key. | Implemented for named uses. |
| Swift SystemRandomNumberGenerator | Nonce-prefix bytes for the attachment format. | Implemented in the attachment path; not independently audited. |

Vuelo does not reimplement Signal Protocol primitives. The app does have its own application-level transport and storage integration, plus separate authenticated-encryption formats for attachments and Saved Messages. Those formats have not received an independent third-party review.
