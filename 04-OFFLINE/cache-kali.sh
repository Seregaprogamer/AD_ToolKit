#!/usr/bin/env bash
# Запустить на Kali с интернетом. Собирается локальный репозиторий для той же ветки и архитектуры.
set -euo pipefail
[[ $# -ge 2 ]] || { echo 'Пример: bash cache-kali.sh /путь/к/новой-папке tshark docker.io docker-compose'; exit 2; }
for cmd in apt-get dpkg-scanpackages dpkg dpkg-deb sha256sum gzip realpath; do command -v "$cmd" >/dev/null || { echo "Нужен $cmd"; exit 2; }; done
dest=$(realpath -m -- "$1"); shift
for p in "$@"; do [[ "$p" =~ ^[a-z0-9][a-z0-9.+-]+$ ]] || { echo "Недопустимое имя пакета: $p"; exit 2; }; done
[[ ! -e "$dest" ]] || { echo 'Выбери новую папку для репозитория.'; exit 2; }
mkdir -p "$dest"
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
touch "$work/status"
# Пустой статус dpkg нужен, чтобы включить зависимости, уже установленные на машине подготовки.
LC_ALL=C apt-get -s -o Debug::NoLocking=1 -o Dir::State::status="$work/status" \
    --no-install-recommends install "$@" > "$work/plan"
# С пустым статусом строки Inst содержат имя и версию всех выбранных пакетов.
awk '/^Inst / {v=$3; sub(/^\(/,"",v); print $2 "=" v}' "$work/plan" > "$work/versions"
mapfile -t versions < "$work/versions"
(( ${#versions[@]} )) || { echo 'APT не выбрал пакеты.'; exit 1; }
cd -- "$dest"
apt-get download "${versions[@]}"
shopt -s nullglob
debs=(*.deb)
(( ${#debs[@]} )) || { echo 'APT не оставил пакетов. Проверь настройки кэша.'; exit 1; }
dpkg-scanpackages . /dev/null > Packages
gzip -c Packages > Packages.gz
printf '%s\n' "$@" > requested.txt
dpkg --print-architecture > architecture.txt
sha256sum -- *.deb Packages Packages.gz requested.txt architecture.txt > SHA256SUMS
sha256sum --check --quiet SHA256SUMS
echo "Готово: ${#debs[@]} пакетов в $dest"
