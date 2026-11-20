---
aliases:
  - "Connection timed out / Operation timed out"
  - "Connection timed out"
  - "Operation timed out"
tags:
  - ошибка
  - сеть
---

# Connection timed out / Operation timed out

## Что могло произойти

Нет ответа на соединение или задержался уже принятый запрос.

## Что проверить

`ip route get IP`, `curl -so /dev/null -w '%{time_connect} %{time_starttransfer} %{time_total}\n' --connect-timeout 2 --max-time 5 URL`. Проверь наличие запроса в журнале.

## Что изменить

Если соединения нет, исправь маршрут/разрешённое сетевое правило. Если соединение быстрое, ищи задержку сервиса или БД.

## Как проверить результат

Штатный запрос укладывается в тайм-аут чекера.

## Как откатить

Верни ровно изменённое правило или конфиг; не отключай весь firewall.

[[02-DEFENSE/NETWORK-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Network|Другие симптомы]]

[[START_HERE|На главную]]
