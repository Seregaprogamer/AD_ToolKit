---
aliases:
  - "No space left on device / disk quota exceeded"
  - "No space left on device"
  - "disk quota exceeded"
tags:
  - ошибка
  - linux
---

# No space left on device / disk quota exceeded

## Что могло произойти

Исчерпаны байты, inode или квота пользователя.

## Что проверить

`df -h .`, `df -i .`, `du -h --max-depth=1 . | sort -h`, при наличии `quota -s`.

## Что изменить

Перенеси свои воспроизводимые артефакты на свободный носитель после проверки копии; сохрани логи ошибки.

## Как проверить результат

Проверь свободное место и запись одного временного файла.

## Как откатить

Верни перемещённые файлы при необходимости. Игровую БД оставь на месте.

[[04-OFFLINE/README|Руководство по теме]] · [[10-TROUBLESHOOTING/Linux|Другие симптомы]]

[[START_HERE|На главную]]
