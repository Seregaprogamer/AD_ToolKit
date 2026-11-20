---
aliases:
  - "Unable to locate package / unmet dependencies / GLIBC_x.y not found"
  - "Unable to locate package"
  - "unmet dependencies"
  - "GLIBC_x.y not found"
tags:
  - ошибка
  - linux
---

# Unable to locate package / unmet dependencies / GLIBC_x.y not found

## Что могло произойти

Другой релиз/архитектура, неполный кэш, несовместимый ABI.

## Что проверить

`dpkg --print-architecture`, `getconf GNU_LIBC_VERSION`, `apt-cache policy ИМЯ`, `dpkg-deb -I ФАЙЛ.deb`, `apt-get -s --no-remove install ИМЯ`.

## Что изменить

Выбери пакет и зависимости целевой ветки. Для jq/curl комплекта нужна glibc ≥ 2.39. Для rg доступен статический файл.

## Как проверить результат

Проверь версию и минимальную полезную операцию.

## Как откатить

Верни системный PATH или убери приватный каталог из него; не заменяй libc системы вручную.

[[04-OFFLINE/README|Руководство по теме]] · [[10-TROUBLESHOOTING/Linux|Другие симптомы]]

[[START_HERE|На главную]]
