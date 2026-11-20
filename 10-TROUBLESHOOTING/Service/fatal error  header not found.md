---
aliases:
  - "fatal error: header not found / undefined reference / compilation failed"
  - "fatal error: header not found"
  - "undefined reference"
  - "compilation failed"
tags:
  - ошибка
  - сервис
---

# fatal error: header not found / undefined reference / compilation failed

## Что могло произойти

Нет заголовка, неверная версия библиотеки, порядок линковки или ABI.

## Что проверить

`cc --version`, `file ОБЪЕКТ`, первая ошибка сборки; для библиотек `pkg-config --cflags --libs ИМЯ`.

## Что изменить

Собери в отдельном каталоге с нужным -dev пакетом того же дистрибутива или верни готовую рабочую сборку.

## Как проверить результат

Запускается новый бинарник и проходит контрольный запрос.

## Как откатить

Переключись на сохранённый артефакт прежней версии.

[[02-DEFENSE/CHECKER|Руководство по теме]] · [[10-TROUBLESHOOTING/Service|Другие симптомы]]

[[START_HERE|На главную]]
