---
aliases:
  - "Could not resolve host / DNS resolution failed / Temporary failure in name resolution"
  - "Could not resolve host"
  - "DNS resolution failed"
  - "Temporary failure in name resolution"
tags:
  - ошибка
  - сеть
---

# Could not resolve host / DNS resolution failed / Temporary failure in name resolution

## Что могло произойти

Ошибка DNS или внутреннее имя Compose запрошено с ноутбука.

## Что проверить

`getent ahosts ИМЯ`, `cat /etc/resolv.conf`; повтори в том же сетевом пространстве, где работает клиент.

## Что изменить

Для межсервисной связи укажи имя сервиса в общей Docker-сети. Для внешнего имени проверь DNS текущего профиля.

## Как проверить результат

Имя разрешается в ожидаемый адрес, запрос доходит до сервиса.

## Как откатить

Верни прежний DNS-профиль; публичный DNS может не знать игровых имён.

[[02-DEFENSE/NETWORK-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Network|Другие симптомы]]

[[START_HERE|На главную]]
