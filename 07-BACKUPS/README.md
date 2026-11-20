---
aliases:
  - "Сохранить конфиг и откатить одно изменение"
tags:
  - ad
  - восстановление
---

# Сохранить конфиг и откатить одно изменение

## Конфигурация

В каталоге своего сервиса укажи реальное имя Compose-файла. Каталог ниже создаётся с уникальным именем и закрытыми правами.

```bash
umask 077
snapshot=$(mktemp -d "$HOME/ad-before.XXXXXXXX")
cp -a -- compose.yaml "$snapshot/"
sha256sum "$snapshot/compose.yaml"
docker compose ps -a > "$snapshot/containers.txt"
docker compose images > "$snapshot/images.txt"
```

Запиши `docker inspect -f '{{.Image}}' ID_КОНТЕЙНЕРА` для работающего контейнера. Для исходников полезны `git status --short` и `git diff -- файл`; незакоммиченные и новые файлы копируй отдельно. Перед применением проверь `docker compose config -q`. Проверка синтаксиса YAML не выполняет приложение.

**Откат конфига:** `diff -u "$snapshot/compose.yaml" compose.yaml`. Если diff содержит только твою правку, сохрани текущий файл отдельно, затем верни копию и снова выполни проверку конфига. `docker compose up -d --no-deps --no-build --pull never ИМЯ` пересоздаст нужный сервис, если изменился конфиг. Изменение переменных окружения через обычный restart не применяется. Сначала убедись в наличии образа и подключении прежнего тома.

## Рабочие данные

Для SQLite в учебной лаборатории используй online backup, включая записи, уже подтверждённые в WAL. Запусти из терминала тренировки с переменной `LAB` и существующей базой. Получится новая копия в отдельной папке.

```bash
dest=$(mktemp -d "$HOME/ad-db.XXXXXXXX")
python3 - "$LAB/notes.sqlite" "$dest/notes.sqlite" <<'PY'
import pathlib, sqlite3, sys
src = pathlib.Path(sys.argv[1]).resolve()
with sqlite3.connect(src.as_uri() + "?mode=ro", uri=True) as live:
    with sqlite3.connect(sys.argv[2]) as copy:
        live.backup(copy)
        print("integrity:", copy.execute("PRAGMA integrity_check").fetchone()[0])
        print("notes:", copy.execute("SELECT count(*) FROM notes").fetchone()[0])
PY
```

Проверь копию запуском второго экземпляра на другом порту и чтением ранее записанного ID. Для PostgreSQL используй согласованный логический дамп штатным `pg_dump` и пробное восстановление в **другую** БД. Простой tar активной директории БД может захватить файлы в разные моменты. Полное восстановление старой БД на игровом сервере требует решения команды о потере последующих записей.

[[START_HERE|На главную]]
