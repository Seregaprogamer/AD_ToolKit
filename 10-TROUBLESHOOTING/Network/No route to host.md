---
aliases:
  - "No route to host / Host unreachable / Network is unreachable"
  - "No route to host"
  - "Host unreachable"
  - "Network is unreachable"
tags:
  - ошибка
  - сеть
---

# No route to host / Host unreachable / Network is unreachable

## Что могло произойти

Нет подходящего маршрута, интерфейс отключён либо получено ICMP-сообщение недоступности.

## Что проверить

`ip -br addr`, `ip route`, `ip route get IP`, `ip neigh`.

## Что изменить

Используй профиль сети этапа и правильный адрес. Проверь согласованный шлюз.

## Как проверить результат

Ядро выбирает верный dev/src и соединение со своим портом проходит.

## Как откатить

Верни прежний профиль и маршрут.

[[02-DEFENSE/NETWORK-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Network|Другие симптомы]]

[[START_HERE|На главную]]
