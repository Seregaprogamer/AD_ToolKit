---
aliases:
  - "Python venv и Pygments · открыть код офлайн"
tags:
  - ad
  - защита
---

# Python venv и Pygments · открыть код офлайн

Создать локальную среду без изменения системного Python и подсветить исходник сервиса.

**Версия.** Pygments 2.19.1 в приложенном wheel, Python ≥ 3.8.

**Зависимости и совместимость.** Python 3, venv, pip, wheel без дополнительных обязательных runtime-зависимостей.

**Офлайн-установка.** См. 04-OFFLINE/README.md. В pip используй --no-index.

## Команды и проверка

```text
python3 --version
"$HOME/ad-tools-venv/bin/pygmentize" -V
"$HOME/ad-tools-venv/bin/pygmentize" -l c -f terminal 01-SERVICE/modecheck.c
```

В подсвеченном исходнике найди обработку maintenance и сверь код возврата с запуском modecheck.

**Частая ошибка.** При externally-managed-environment команда запущена системным pip. Вызывай python из своего venv.

[Официальная документация](https://pygments.org/docs/cmdline/)

[[START_HERE|На главную]]
