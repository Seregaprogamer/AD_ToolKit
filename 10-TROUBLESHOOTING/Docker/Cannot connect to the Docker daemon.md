---
aliases:
  - "Cannot connect to the Docker daemon"
tags:
  - ошибка
  - docker
---

# Cannot connect to the Docker daemon

## Что могло произойти

Клиент смотрит в другой context, демон остановлен или недоступен сокет.

## Что проверить

`docker context show`, `docker context ls`, `systemctl is-active docker`, `journalctl -u docker -b -n 60 --no-pager`. Для rootless проверь `systemctl --user status docker`.

## Что изменить

Выбери правильный context только для команды через `docker --context ИМЯ info`. Если служба остановлена, выясни причину по журналу и запусти соответствующую службу на своей машине.

## Как проверить результат

`docker info` выводит секцию Server, видны прежние контейнеры.

## Как откатить

Верни прежний context, если переключал глобально. Не перезапускай весь движок ради одного сервиса.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
