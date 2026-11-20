---
aliases:
  - "OOMKilled / exit code 137"
  - "OOMKilled"
  - "exit code 137"
tags:
  - ошибка
  - docker
---

# OOMKilled / exit code 137

## Что могло произойти

SIGKILL мог прийти от OOM либо извне.

## Что проверить

`docker inspect -f '{{.State.OOMKilled}} {{.State.ExitCode}}' ID`, `docker stats --no-stream`, `journalctl -k -b | grep -i oom`.

## Что изменить

При подтверждённом OOM снизь нагрузку или исправь лимит одного сервиса в пределах ресурсов хоста.

## Как проверить результат

Повтори сценарий и проверь память и новые события OOM.

## Как откатить

Верни исходный лимит, если изменение повредило другим сервисам.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
