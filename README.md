<div align="center">

English · [Русский](README.ru.md)

# Vuelo Security & Transparency

**Privacy should be understandable, not merely promised.**

![App source: Private](https://img.shields.io/badge/App%20source-Private-4057a5?style=flat-square)
![Transparency docs: Public](https://img.shields.io/badge/Transparency%20docs-Public-16836b?style=flat-square)
![Security status: Active development](https://img.shields.io/badge/Security%20status-Active%20development-c58b24?style=flat-square)
![Independent audit: Not completed](https://img.shields.io/badge/Independent%20audit-Not%20completed-777777?style=flat-square)

</div>

Vuelo Security & Transparency is the public place to understand what Vuelo currently protects, what remains limited, and how those statements were checked. It documents the product's privacy boundaries without publishing the app's source code or internal design.

| Privacy | Encryption | Transparency |
|---|---|---|
| What information Vuelo handles | Which conversation paths use E2EE | What is implemented, partial, or planned |

> [!IMPORTANT]
> Vuelo is currently in active development. A code path is not the same as an independent security audit or confirmation of production deployment. Read the status and limitations before relying on a privacy claim.

## Source code status

Vuelo itself is currently **closed-source**. This repository contains public privacy, security, and transparency documentation only. It is not an open-source application repository or a public copy of the Vuelo source repository. See [Source status](SOURCE_STATUS.md).

## Security at a glance

| Area | Status | Notes |
|---|---|---|
| Authentication and session storage | Implemented · Not independently audited | Session tokens are stored in Apple Keychain. |
| One-to-one text E2EE | In validation · Not independently audited | Current source wires the user message path through LibSignalClient; production and runtime validation remain open. |
| Group and channel E2EE | Planned | Not covered by the current one-to-one transport. |
| Attachments | Partial · Not independently audited | Outgoing one-to-one voice messages use an encrypted upload path; complete media coverage is not established. |
| Saved Messages | In validation · Not independently audited | A separate encrypted vault uses a device-local key. |
| Local message storage | Partial · Not independently audited | SQLCipher protects the E2EE store, not every local app data path. |
| Device trust | Partial · Not independently audited | Registration, approval, and revocation flows exist; complete E2EE lifecycle guarantees are not established. |
| Independent audit | Not yet completed | No third-party security audit has been completed. |

## What the server can see

For the current one-to-one E2EE path, delivery infrastructure receives ciphertext and the routing metadata needed to deliver it. Account and profile information, conversation membership, device identifiers, event timing and ordering, ciphertext size, and connection metadata may also be visible. E2EE does not hide all metadata.

## What the server should not see

The current one-to-one E2EE message path does not require the server to read message content. This is a code-path statement, not a blanket promise about group chats, channels, legacy history, every attachment, or every production system. Those boundaries are documented in [Data and metadata](docs/en/data-and-metadata.md).

## Encryption

The current one-to-one message flow uses the official LibSignalClient bindings for Signal Protocol primitives while Vuelo provides its own app, transport, and storage integration. Saved Messages and the covered outgoing voice path use separate AES-GCM encryption. Details and limits: [E2EE](docs/en/e2ee.md) · [Cryptography](docs/en/cryptography.md).

## Transparency principles

- Document observed behavior, not intentions.
- Distinguish implemented paths from partial work and plans.
- State meaningful limitations and legacy paths.
- Update both languages when the code or claims change.
- Never describe unaudited code as independently verified.

## Documentation

| Topic | Documentation |
|---|---|
| Privacy at a glance | [Privacy overview](docs/en/privacy-overview.md) |
| Current implementation | [Security status](docs/en/security-status.md) |
| How encryption works | [End-to-end encryption](docs/en/e2ee.md) · [Cryptography](docs/en/cryptography.md) |
| Server visibility | [Data and metadata](docs/en/data-and-metadata.md) · [Server role](docs/en/server-role.md) |
| Devices and local data | [Device security](docs/en/device-security.md) · [Local storage](docs/en/local-storage.md) |
| Risks and limits | [Threat model](docs/en/threat-model.md) · [Known limitations](docs/en/known-limitations.md) |
| Dependencies and reviews | [Dependencies](docs/en/dependencies.md) · [Audits](docs/en/audits.md) |
| Questions and source status | [FAQ](docs/en/faq.md) · [Source status](SOURCE_STATUS.md) |
| Report a vulnerability | [Security reporting](SECURITY.md) |

## Security reports

Please do not post vulnerability details in a public issue. Use GitHub private vulnerability reporting when it is enabled for this repository. See [SECURITY.md](SECURITY.md).
