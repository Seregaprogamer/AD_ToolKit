---
aliases:
  - "read-only file system / no space left on device"
  - "read-only file system"
  - "no space left on device"
tags:
  - ошибка
  - docker
---

# read-only file system / no space left on device

## Что могло произойти

Запись в read-only rootfs, закончилось место или inode на хосте.

## Что проверить

`docker inspect -f '{{.HostConfig.ReadonlyRootfs}}' ID`, `df -h`, `df -i`, `docker system df`.

## Что изменить

Направь нужные записи в согласованный writable volume, либо освободи согласованные временные данные.

## Как проверить результат

Запись и повторное чтение тестовых данных проходят.

## Как откатить

Верни прежнее монтирование. Удаление томов/глобальный prune может уничтожить текущие данные.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
