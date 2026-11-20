---
aliases:
  - "exec format error / no matching manifest"
  - "exec format error"
  - "no matching manifest"
tags:
  - ошибка
  - docker
---

# exec format error / no matching manifest

## Что могло произойти

Архитектура ELF/образа не совпадает с двигателем; у текстового entrypoint отсутствует shebang.

## Что проверить

`uname -m`, `docker info -f '{{.Architecture}}'`, `docker image inspect -f '{{.Os}}/{{.Architecture}}' ТЕГ`, `file СКРИПТ`.

## Что изменить

Возьми нативный образ. Для скрипта добавь правильный shebang и LF в рабочей копии.

## Как проверить результат

Образ запускается на нужной архитектуре, entrypoint выполняется.

## Как откатить

Верни прежний образ или скрипт.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
