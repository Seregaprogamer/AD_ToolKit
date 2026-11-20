---
aliases:
  - "Тренировка в Docker Compose"
tags:
  - ad
  - docker
---

# Тренировка в Docker Compose

В комплекте готовый архив одного образа Linux/amd64 с Python, SQLite и сервисом заметок. Импорт использует локальные файлы. Docker CLI, работающий Engine и Compose v2 должны быть доступны на машине. Запускать в своей учебной среде.

```bash
bash load-docker.sh
cd 03-DOCKER
docker compose -p adusbnotes config -q
docker compose -p adusbnotes up -d --pull never --no-build
docker compose -p adusbnotes ps -a
docker compose -p adusbnotes logs --tail 40 notes
```

В примере проект везде называется adusbnotes. Перед первым стартом проверь, что это имя свободно на твоём хосте. Сервис опубликован только на loopback, данные в именованном томе. В образе нет оболочки sh. Python работает от UID 65532.

```bash
work=$(mktemp -d)
python3 ../06-LAB/checker.py "$work/receipt.json"
docker compose -p adusbnotes exec -T notes /usr/bin/python3.13 -c 'from pathlib import Path; Path("/data/mode").write_text("bad-schema\n")'
python3 ../06-LAB/checker.py "$work/receipt.json"
docker compose -p adusbnotes exec -T notes /usr/bin/python3.13 -c 'from pathlib import Path; Path("/data/mode").write_text("ok\n")'
python3 ../06-LAB/checker.py "$work/receipt.json"
docker compose -p adusbnotes stop
```

Для продолжения: `docker compose -p adusbnotes start`. Используй ту же квитанцию и имя проекта. При сбое проверь `docker context show`, `docker compose version`, `docker compose -p adusbnotes logs notes` и [[10-TROUBLESHOOTING/Docker|каталог ошибок]]. При отсутствии доступа к движку [[06-LAB/README|запуск без Docker]] даёт тот же сценарий.

**Образ и данные:** `docker image save` сохраняет образ и тег, но не содержимое томов и не bind mounts. Для переноса своего стенда нужны отдельно файл Compose, конфиги, долговечные данные и все образы совместимой архитектуры. [Docker image save](https://docs.docker.com/reference/cli/docker/image/save/)

[[START_HERE|На главную]]
