---
aliases:
  - "port is already allocated / address already in use"
  - "port is already allocated"
  - "address already in use"
tags:
  - ошибка
  - docker
---

# port is already allocated / address already in use

## Что могло произойти

Параллельный стенд или хост-процесс уже занял порт.

## Что проверить

`ss -lntp`, `docker ps --format '{{.Names}} {{.Ports}}'`. Проверь порт слева в Compose.

## Что изменить

Для своей тренировки выбери свободный порт хоста; поправь клиента. На игре сохрани объявленный организаторами порт, устранив согласованный дубликат.

## Как проверить результат

Повтори запрос с точки доступа клиента.

## Как откатить

Верни прежнюю привязку и URL при снятии конфликта.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
