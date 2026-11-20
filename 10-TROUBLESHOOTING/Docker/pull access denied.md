---
aliases:
  - "pull access denied / manifest unknown / image not found"
  - "pull access denied"
  - "manifest unknown"
  - "image not found"
tags:
  - ошибка
  - docker
---

# pull access denied / manifest unknown / image not found

## Что могло произойти

Тег отсутствует локально, неверен registry/тег, либо нужен доступ к приватному источнику.

## Что проверить

`docker image ls --digests`, `docker compose config --images`, `docker context show`.

## Что изменить

Загрузи сохранённый образ для той же архитектуры и тега. Для упражнений подходит load-docker.sh.

## Как проверить результат

`docker image inspect ТЕГ` и запуск с `--pull never`.

## Как откатить

Верни предыдущий тег, сохрани образы обеих версий.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
