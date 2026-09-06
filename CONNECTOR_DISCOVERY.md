# Manhattan Associates WMS Connector — Connector Discovery

**Category:** C46. Warehouse & 3PL Logistics Management  
**Vendor:** Manhattan Associates WMS  
**Official Website:** https://www.manh.com

## 1. Официальный API
- **Базовый URL API:** `https://<tenant-manh-host>/api`
- **Поддерживаемая модель авторизации:** OAuth 2.0 Client Credentials Grant

## 2. Архитектура сущностей
- Ключевые ресурсы платформы Manhattan Associates WMS:
  - склады и зоны хранения (/facilities)
  - инвентарь/остатки (/inventory)
  - заказы на отгрузку (/orders)
  - поставки (/shipments)

## 3. Требования к отказоустойчивости и безопасности
- Соблюдение вендорных лимитов запросов (Rate Limiting) с экспоненциальной задержкой.
- Строгая валидация Pydantic-схем на входе и выходе каждого запроса.
- Тестовая точка проверки подключения: `GET /api/facilities`.
