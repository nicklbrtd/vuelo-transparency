# Device security

English · [Русский](../ru/device-security.md)

Last reviewed: 2026-09-28<br>
Status: Current

## Device keys

The current client creates separate device signing and key-agreement keys with Apple CryptoKit. It prefers Secure Enclave-backed P-256 keys when available and falls back to private key material stored in Keychain. This applies to the device registry/pairing key role; it is not a claim that every Vuelo or Signal key is stored in Secure Enclave.

Signal identity and prekey material are handled separately through LibSignalClient and the SQLCipher-backed protocol store. Selected private Signal material uses device-only Keychain storage for the local database key.

## Device registration and approval

The source includes a device registry and a QR-based approval flow for additional devices. The registry can mark a device trusted or revoked. These product mechanisms do not, by themselves, establish that Signal session keys are synchronized to every device or that every recipient enforces revocation for every pending event.

## Local authentication

The app includes an optional local privacy-lock flow using Apple LocalAuthentication and a visual privacy shield when the app leaves the foreground. This is a local access/display control. It does not encrypt all app data and does not protect content on a fully compromised unlocked device.

## Limits

- No user-verifiable E2EE safety-number or key-transparency flow was confirmed.
- Multi-device Signal session transfer was not established.
- Complete revocation behavior for future E2EE delivery has not been independently validated.
- Secure Enclave is preferred for the separate device keys when available, with a software Keychain fallback.
