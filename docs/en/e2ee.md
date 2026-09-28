# End-to-end encryption

English · [Русский](../ru/e2ee.md)

Last reviewed: 2026-09-28<br>
Status: Current

One-to-one messaging status: In validation · Not independently audited.

## What E2EE means here

End-to-end encryption (E2EE) means that message content is encrypted on the sender's device and decrypted on a recipient device. A delivery service can route ciphertext without needing the plaintext. This description applies only to flows that actually use the E2EE transport.

## Current one-to-one code path

The current source connects one-to-one text and control events to the official LibSignalClient bindings for Signal Protocol primitives. The sending device obtains public prekey material, establishes or advances a session, encrypts the event, and submits an encrypted envelope. The receiving path fetches an envelope, decrypts it locally, and stores the result in the E2EE local store.

The code also provisions signed prekeys, one-time prekeys, and Kyber prekey material through LibSignalClient. This statement describes code integration; it does not claim an independently verified post-quantum guarantee or confirm production server configuration.

Vuelo uses LibSignalClient for protocol primitives while implementing its own application, transport, and storage integration. Vuelo does not claim to use the exact same complete security architecture as Signal.

## Sessions and keys

Signal identity and session records, prekeys, and E2EE message history are kept in an SQLCipher-backed local store whose master key is stored in Keychain. Separate device-signing and device-agreement keys use Apple CryptoKit and are stored using Secure Enclave when available, with a Keychain-backed software fallback. These are distinct key roles; the device registry keys are not a user-facing verification of Signal identity keys.

The reviewed code did not establish a user-facing safety-number comparison or key-transparency workflow. Users should not infer that seeing an E2EE status indicator means they independently verified a contact's identity key.

## Saved Messages

Status: In validation · Not independently audited.

Saved Messages uses a separate owner-only vault, not a Signal session with oneself. The client encrypts vault events with AES-GCM and stores the corresponding key in Keychain with device-only accessibility. The reviewed flow does not establish recovery or synchronization of this key across devices.

## Attachments

Status: Partial · Not independently audited.

The attachment cipher uses chunked AES-GCM with authenticated metadata. The current one-to-one outgoing voice-message path is wired through this encryption and upload flow. This does not prove that every attachment type, thumbnail, preview, or legacy media path is encrypted.

## What E2EE does not hide

E2EE does not automatically hide account identifiers, sender and recipient routing, conversation membership, event ordering, timestamps, network addresses, or ciphertext size. The delivery service must process some routing metadata. See [data and metadata](data-and-metadata.md).

## Current limits

- Group and channel conversations are not covered by this one-to-one E2EE implementation.
- Legacy one-to-one history can remain server-side in plaintext.
- Device revocation and multi-device protections have not been established for all E2EE flows.
- Production deployment and end-to-end runtime behavior have not been verified in this documentation review.
- The implementation has not received an independent third-party audit.

For protocol background, see the [Signal Double Ratchet specification](https://signal.org/docs/specifications/doubleratchet/) and [PQXDH specification](https://signal.org/docs/specifications/pqxdh/). Those specifications are not an audit of Vuelo.
