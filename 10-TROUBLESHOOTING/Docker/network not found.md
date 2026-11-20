---
aliases:
  - "network not found / Name or service not known"
  - "network not found"
  - "Name or service not known"
tags:
  - ошибка
  - docker
---

# network not found / Name or service not known

## Что могло произойти

Сервисы в разных сетях, ошибка имени, подключение по localhost внутри контейнера.

## Что проверить

`docker network ls`, `docker inspect -f '{{json .NetworkSettings.Networks}}' ID`. Сравни сети приложения и БД. При наличии `getent` проверь имя из контейнера.

## Что изменить

В своём Compose присоедини сервисы к исходной общей сети и используй имя сервиса и внутренний порт.

## Как проверить результат

Штатный запрос из приложения доходит до БД.

## Как откатить

Верни прошлое имя сети и подключения. Не удаляй все Docker-сети.

[[03-DOCKER/DAEMON-DOWN|Руководство по теме]] · [[10-TROUBLESHOOTING/Docker|Другие симптомы]]

[[START_HERE|На главную]]
