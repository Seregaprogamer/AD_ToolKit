---
aliases:
  - "Docker Engine · состояние контейнера"
tags:
  - ad
  - docker
---

# Docker Engine · состояние контейнера

Отличить остановленный контейнер, OOM и проблему сети от ошибки самого приложения.

**Версия.** Версия локального движка определяется docker version, включая строку Server.

**Зависимости и совместимость.** CLI, демон, runtime и доступ к выбранному context. Групповой доступ к системному Docker даёт широкие полномочия на хосте.

**Офлайн-установка.** Пакет docker.io и зависимости из Kali. Готовый образ лаборатории импортируется отдельно.

## Команды и проверка

```text
docker version
docker context show
docker ps -a
docker stats --no-stream
docker inspect -f '{{json .State}}' ID
```

Выбери ID своего контейнера из docker ps -a, затем сопоставь ExitCode, OOMKilled и логи с HTTP-пробой.

**Частая ошибка.** При Cannot connect проверь и context, и службу. При пустом списке не торопись создавать заново: возможно, выбран другой движок.

[Официальная документация](https://docs.docker.com/reference/cli/docker/)

[[START_HERE|На главную]]
