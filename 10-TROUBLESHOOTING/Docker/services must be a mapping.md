---
aliases:
  - "services must be a mapping / validating compose / variable is not set"
  - "services must be a mapping"
  - "validating compose"
  - "variable is not set"
tags:
  - ошибка
  - docker
---

# services must be a mapping / validating compose / variable is not set

## Что могло произойти

Отступы YAML, неверный тип, не тот env-файл или каталог.

## Что проверить

`pwd`, `docker compose version`, `docker compose -f compose.yaml config -q`. Сверь имена переменных с примером без публикации секретов.

## Что изменить

Восстанови правильный тип и отступ или передай нужный `--env-file`.

## Как проверить результат

Валидация завершается с кодом 0, затем проходит запуск.

## Как откатить

Сравни с копией `diff -u`, верни только изменённый файл.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
