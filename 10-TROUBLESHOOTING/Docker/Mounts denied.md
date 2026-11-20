---
aliases:
  - "Mounts denied / not a directory / пустой volume"
  - "Mounts denied"
  - "not a directory"
  - "пустой volume"
tags:
  - ошибка
  - docker
---

# Mounts denied / not a directory / пустой volume

## Что могло произойти

Перепутаны файл и каталог, путь хоста или имя проекта.

## Что проверить

`docker inspect -f '{{json .Mounts}}' ID`. Сверь Source и Destination с `ls -ld -- ПУТЬ`. На удалённом Docker путь относится к серверу.

## Что изменить

Укажи существующий источник правильного типа. Для БД сначала найди том с предыдущими данными.

## Как проверить результат

Проверь прежний ID и чтение нужного файла внутри процесса.

## Как откатить

Верни исходное монтирование; оставь оба тома до проверки.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
