#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
command -v sha256sum >/dev/null || { echo 'Нужен sha256sum (coreutils)' >&2; exit 2; }
case "${1:-}" in
  "") manifest=SHA256SUMS ;;
  --tools) manifest=SHA256-TOOLS ;;
  *) echo 'Использование: bash verify.sh [--tools]' >&2; exit 2 ;;
esac
sha256sum --quiet --strict --check "$manifest"
echo 'OK: все файлы контрольного списка совпали.'
