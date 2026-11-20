#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
bash verify.sh --tools
case "${1:-tools}" in
  obsidian)
    command -v python3 >/dev/null || { echo 'Нужен Python 3.8+ или скачай AppImage по ссылке в инструкции.' >&2; exit 2; }
    shift
    exec python3 04-OFFLINE/Obsidian/download.py "$@"
    ;;
  tools) ;;
  *) echo 'Использование: bash setup.sh [tools | obsidian [--arch amd64|arm64|both]]' >&2; exit 2 ;;
esac
if [[ $(uname -m) != x86_64 ]]; then echo 'Готовый пакет CLI предназначен для amd64. На ARM открой 04-OFFLINE/arm64/README.md.'; exit 2; fi
for cmd in dpkg-deb sha256sum sort getconf mktemp; do command -v "$cmd" >/dev/null || { echo "Нужен $cmd" >&2; exit 2; }; done
glibc=$(getconf GNU_LIBC_VERSION | cut -d' ' -f2)
if [[ $(printf '%s\n' 2.39 "$glibc" | sort -V | head -1) != 2.39 ]]; then echo 'Для curl/jq этой сборки нужна glibc >= 2.39. Можно отдельно извлечь статический rg (см. 04-OFFLINE/README.md).'; exit 2; fi
pkg=04-OFFLINE/amd64/ad-usb-tools_1.0-1_amd64.deb
hash=$(sha256sum "$pkg" | cut -d' ' -f1)
base="$HOME/.local/share/ad-usb-tools"
target="$base/$hash"
if [[ ! -e "$target" ]]; then
    mkdir -p -- "$base"
    temp=$(mktemp -d "$base/.stage.XXXXXXXX")
    trap 'rm -rf -- "$temp"' EXIT
    dpkg-deb -x "$pkg" "$temp"
    "$temp/opt/ad-usb-tools/bin/curl" --version >/dev/null
    "$temp/opt/ad-usb-tools/bin/jq" -ne '1 == 1' >/dev/null
    "$temp/opt/ad-usb-tools/bin/rg" --version >/dev/null
    # Параллельный запуск может опубликовать тот же пакет первым.
    mv -Tn -- "$temp" "$target"
fi
bin="$target/opt/ad-usb-tools/bin"
[[ -x "$bin/rg" && -x "$bin/jq" && -x "$bin/curl" ]] || { echo 'Каталог установки неполон. Извлеки пакет в новую папку.' >&2; exit 1; }
printf 'Готово. Только для текущего терминала выполни:\nexport PATH=%q:"$PATH"\n' "$bin"
