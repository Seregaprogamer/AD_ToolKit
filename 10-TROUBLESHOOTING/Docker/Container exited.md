---
aliases:
  - "Container exited / Restarting"
  - "Container exited"
  - "Restarting"
tags:
  - ошибка
  - docker
---

# Container exited / Restarting

## Что могло произойти

Ошибка entrypoint, обязательной переменной, подключения к БД или штатный выход одноразового процесса.

## Что проверить

`docker compose ps -a`, `docker compose logs --tail 100 APP`, `docker inspect -f '{{json .State}}' ID`. Проверь ExitCode, Error и OOMKilled.

## Что изменить

Исправь первую ошибку запуска. Для одноразового инициализатора проверь, ожидается ли exit 0.

## Как проверить результат

Процесс остаётся запущен, счётчик RestartCount стабилен и проходит штатная операция.

## Как откатить

Верни предыдущие параметры или образ одного APP, сохранив том.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
