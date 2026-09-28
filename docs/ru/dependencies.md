# Зависимости, важные для безопасности

[English](../en/dependencies.md) · Русский

Последняя проверка: 2026-09-28<br>
Статус: Актуально

Версии ниже проверены в текущем приватном репозитории: в файле блокировки и конфигурации зависимостей на 2026-09-28.

| Зависимость | Назначение | Версия | Источник |
|---|---|---|---|
| LibSignalClient | Связки Signal Protocol, используемые транспортом сообщений один на один. | 0.97.1 | [signalapp/libsignal](https://github.com/signalapp/libsignal) |
| SQLCipher.swift | Зашифрованное локальное хранилище протокола E2EE. | 4.16.0 | [sqlcipher/SQLCipher.swift](https://github.com/sqlcipher/SQLCipher.swift) |
| Apple CryptoKit | API AES-GCM, SHA-256 и P-256 для описанных функций. | Входит в Apple OS SDK | [Документация Apple](https://developer.apple.com/documentation/cryptokit) |
| Apple Security / Keychain Services | Локальное хранение учётных данных и отдельных приватных ключей, безопасные случайные байты. | Входит в Apple OS | [Документация Apple](https://developer.apple.com/documentation/security) |
| Apple LocalAuthentication | Необязательная локальная аутентификация приложения и подтверждение сопряжения устройств. | Входит в Apple OS | [Документация Apple](https://developer.apple.com/documentation/localauthentication) |

Это не полный перечень компонентов. Обычные UI- и сетевые пакеты не включены, если они напрямую не влияют на описанную границу защиты. Версии и лицензии зависимостей нужно повторно проверять для каждого публичного релиза.
