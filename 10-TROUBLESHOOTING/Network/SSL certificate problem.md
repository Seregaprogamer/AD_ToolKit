---
aliases:
  - "SSL certificate problem / TLS handshake failed"
  - "SSL certificate problem"
  - "TLS handshake failed"
tags:
  - ошибка
  - сеть
---

# SSL certificate problem / TLS handshake failed

## Что могло произойти

Часы, имя, цепочка доверия, неверный порт или протокол.

## Что проверить

`date -Is`, `curl -v --max-time 5 URL`; проверь Subject Alternative Name, адрес и время действия.

## Что изменить

Используй правильное имя и выданный организаторами CA. Для отдельного вызова подходит `curl --cacert ФАЙЛ URL`.

## Как проверить результат

TLS проходит со штатной верификацией, HTTP выдаёт ожидаемый код.

## Как откатить

Убери локальный параметр CA или верни прежний доверенный конфиг.

[[02-DEFENSE/NETWORK-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Network|Другие симптомы]]

[[START_HERE|На главную]]
