#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
bash verify.sh --tools
command -v docker >/dev/null || { echo 'Сначала нужен Docker Engine и CLI. Без Docker работает 06-LAB/service.py.' >&2; exit 2; }
arch=$(docker info -f '{{.OSType}}/{{.Architecture}}')
case "$arch" in linux/x86_64|linux/amd64) ;; *) echo "Образ для linux/amd64; сервер сообщил $arch" >&2; exit 2;; esac
tag='ad-usb/notes:1.0-amd64'
expected=$(cat 03-DOCKER/image-id.txt)
if current=$(docker image inspect -f '{{.Id}}' "$tag" 2>/dev/null); then
    [[ "$current" == "$expected" ]] || { echo "Тег $tag уже занят другим образом. Импорт остановлен." >&2; exit 1; }
    echo 'Этот образ уже загружен.'; exit 0
fi
docker image load --input 03-DOCKER/notes-amd64.tar
[[ $(docker image inspect -f '{{.Id}}' "$tag") == "$expected" ]]
echo "Готово: $tag"
