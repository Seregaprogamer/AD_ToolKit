---
aliases:
  - "Could not get lock / dpkg frontend lock"
  - "Could not get lock"
  - "dpkg frontend lock"
tags:
  - ошибка
  - linux
---

# Could not get lock / dpkg frontend lock

## Что могло произойти

Другой APT/dpkg ещё работает или установка прервана.

## Что проверить

`ps -ef | grep -E '[a]pt|[d]pkg'`, `dpkg --audit`.

## Что изменить

Дождись действующей операции. После её завершения посмотри аудит и на собственной машине заверши прерванную настройку `sudo dpkg --configure -a`, если аудит этого требует.

## Как проверить результат

`dpkg --audit` пуст, пакет доступен.

## Как откатить

Не удаляй lock работающего процесса. Восстановление прежних версий требует сохранённых пакетов/снимка.

[[04-OFFLINE/README|Руководство по теме]] · [[10-TROUBLESHOOTING/Linux|Другие симптомы]]

[[START_HERE|На главную]]
