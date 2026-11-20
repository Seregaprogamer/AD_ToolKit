---
aliases:
  - "permission denied while trying to connect to the Docker daemon socket"
tags:
  - ошибка
  - docker
---

# permission denied while trying to connect to the Docker daemon socket

## Что могло произойти

Сокет другого пользователя или не хватает прав.

## Что проверить

`id`, `ls -l /var/run/docker.sock`, `docker context ls`. Для rootless сопоставь сокет с `$XDG_RUNTIME_DIR`.

## Что изменить

Выбери свой rootless context или используй согласованный административный доступ.

## Как проверить результат

`docker info` от нужного пользователя успешно.

## Как откатить

Верни прежний context. Изменение режима сокета на 666 не требуется.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
