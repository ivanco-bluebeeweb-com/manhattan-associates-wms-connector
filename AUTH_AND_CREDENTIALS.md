# Manhattan Associates WMS Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** OAuth 2.0 Client Credentials Grant
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /api/facilities`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
