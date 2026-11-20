#!/usr/bin/env bash
# Применяет подготовленный локальный репозиторий только по явному согласию.
set -euo pipefail
[[ $# == 1 ]] || { echo 'Укажи путь к готовому локальному репозиторию.'; exit 2; }
repo=$(realpath -- "$1")
[[ "$repo" =~ ^/[a-zA-Z0-9._/-]+$ ]] || { echo 'Скопируй репозиторий в путь без пробелов, например /var/tmp/ad-repo.'; exit 2; }
cd -- "$repo"
sha256sum -c --quiet --strict SHA256SUMS
[[ $(cat architecture.txt) == "$(dpkg --print-architecture)" ]] || { echo 'Другая архитектура.'; exit 2; }
mapfile -t pkgs < requested.txt
for p in "${pkgs[@]}"; do [[ "$p" =~ ^[a-z0-9][a-z0-9.+-]+$ ]] || exit 2; done
[[ $EUID == 0 ]] || { echo 'Для системной установки нужны права администратора.'; exit 2; }
work=$(mktemp -d)
trap 'rm -rf -- "$work"' EXIT
chmod 755 "$work"
mkdir -p "$work/lists/partial" "$work/archives/partial"
printf 'deb [trusted=yes] file:%s ./\n' "$repo" > "$work/sources.list"
opt=(-o "Dir::Etc::sourcelist=$work/sources.list" -o Dir::Etc::sourceparts=- -o "Dir::State::lists=$work/lists" -o "Dir::Cache::archives=$work/archives" -o Acquire::Languages=none)
apt-get "${opt[@]}" update
apt-get "${opt[@]}" -s --no-remove --no-install-recommends install "${pkgs[@]}"
read -rp 'Применить именно этот план? Введи ДА: ' reply
[[ "$reply" == ДА ]] || { echo 'Отменено'; exit 0; }
apt-get "${opt[@]}" --no-remove --no-install-recommends install "${pkgs[@]}"
