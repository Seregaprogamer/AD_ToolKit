---
aliases:
  - "Unit not found / failed / start request repeated too quickly"
  - "Unit not found"
  - "failed"
  - "start request repeated too quickly"
tags:
  - ошибка
  - linux
---

# Unit not found / failed / start request repeated too quickly

## Что могло произойти

Неверное имя юнита, пакет отсутствует или служба аварийно завершается.

## Что проверить

`systemctl status ИМЯ --no-pager`, `systemctl cat ИМЯ`, `journalctl -u ИМЯ -b -n 100 --no-pager`.

## Что изменить

Устрани первую ошибку запуска. После исправления сброс лимита `systemctl reset-failed ИМЯ` применим к своему юниту.

## Как проверить результат

`systemctl is-active ИМЯ` и реальный запрос.

## Как откатить

Верни прежний unit/drop-in; после изменения unit вызови `systemctl daemon-reload`.

[[04-OFFLINE/README|Руководство по теме]] · [[10-TROUBLESHOOTING/Linux|Другие симптомы]]

[[START_HERE|На главную]]
