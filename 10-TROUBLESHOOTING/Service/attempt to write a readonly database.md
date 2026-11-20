---
aliases:
  - "attempt to write a readonly database / PermissionError"
  - "attempt to write a readonly database"
  - "PermissionError"
tags:
  - ошибка
  - сервис
---

# attempt to write a readonly database / PermissionError

## Что могло произойти

UID сервиса не может писать файл БД или соседний журнал в каталоге.

## Что проверить

`docker inspect -f '{{.Config.User}} {{json .Mounts}}' ID`, `ls -ldn КАТАЛОГ`, `ls -ln ФАЙЛ`.

## Что изменить

На тренировке поправь доступ только к каталогу данных нужного UID. Сначала проверь, что переподключён исходный том.

## Как проверить результат

Создание тестовой записи и повторное чтение проходят.

## Как откатить

Верни прежние UID, режим и mount по снимку.

[[02-DEFENSE/CHECKER|Руководство по теме]] · [[10-TROUBLESHOOTING/Service|Другие симптомы]]

[[START_HERE|На главную]]
