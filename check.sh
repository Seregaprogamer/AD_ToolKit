#!/usr/bin/env bash
set -u
cd -- "$(dirname -- "$0")"
echo "Платформа: $(uname -sm); $(getconf GNU_LIBC_VERSION 2>/dev/null || echo 'glibc неизвестна')"
for tool in bash sha256sum grep find tar ss ip curl jq rg docker journalctl python3 dpkg-deb; do
    if found=$(command -v "$tool"); then printf 'OK       %-12s %s\n' "$tool" "$found"
    else printf 'НЕТ      %s\n' "$tool"; fi
done
if command -v python3 >/dev/null; then python3 -c 'import sqlite3, http.server; print("Лаборатория: модули SQLite и HTTP доступны")' || echo 'НЕТ: стандартные модули тренировки'; fi
if command -v docker >/dev/null; then
    docker compose version || echo 'НЕТ: плагин Compose v2'
    timeout 4 docker info -f '{{.OSType}}/{{.Architecture}}' || echo 'Docker Engine недоступен в текущем контексте'
    docker context show
fi
echo 'Отсутствие отдельной утилиты не мешает открыть START_HERE.md.'
