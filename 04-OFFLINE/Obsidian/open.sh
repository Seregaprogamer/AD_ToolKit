#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
if command -v obsidian >/dev/null; then exec obsidian; fi
case $(uname -m) in
 x86_64) app=Obsidian-1.15.1.AppImage ;;
 aarch64|arm64) app=Obsidian-1.15.1-arm64.AppImage ;;
 *) echo 'Поддерживаются Linux amd64 и arm64.' >&2; exit 2;;
esac
if [[ ! -s "$app" ]]; then
    echo "Нужен $app. Пока есть интернет, выполни из корня комплекта: python3 04-OFFLINE/Obsidian/download.py" >&2
    exit 2
fi
if [[ -f "$app.sha256" ]]; then sha256sum -c -- "$app.sha256"; fi
if [[ ! -x "$app" ]]; then
    echo "Скопируй AppImage в домашнюю папку и выполни chmod +x для файла. На флешке может действовать noexec." >&2
    exit 2
fi
exec "./$app"
