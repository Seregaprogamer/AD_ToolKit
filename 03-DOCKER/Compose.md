---
aliases:
  - "Docker Compose · управлять одним сервисом"
tags:
  - ad
  - docker
---

# Docker Compose · управлять одним сервисом

Проверить итоговый конфиг, журнал или статус одного проекта.

**Версия.** Упражнение рассчитано на Compose v2 с --pull never и pull_policy.

**Зависимости и совместимость.** Docker CLI с плагином Compose v2, Engine, compose.yaml, образ данной архитектуры.

**Офлайн-установка.** Проверь наличие командой docker compose version. Заранее подготовь пакет Compose из того же источника, что и Engine.

## Команды и проверка

```text
docker compose version
docker compose -f 03-DOCKER/compose.yaml -p adusbnotes config -q
docker compose -f 03-DOCKER/compose.yaml -p adusbnotes ps -a
docker compose -f 03-DOCKER/compose.yaml -p adusbnotes logs --tail 40 notes
```

Пройди упражнение с именем проекта adusbnotes. stop и start позволяют проверить сохранность прежней квитанции.

**Частая ошибка.** При no configuration file provided укажи -f или перейди в нужную папку. Ввод разных -p ведёт к разным именам ресурсов.

[Официальная документация](https://docs.docker.com/reference/cli/docker/compose/)

[[START_HERE|На главную]]
