---
aliases:
  - "journalctl · первая ошибка запуска"
tags:
  - ad
  - защита
---

# journalctl · первая ошибка запуска

Просмотреть записи конкретной системной службы за нужный интервал времени.

**Версия.** Локальная версия journalctl --version.

**Зависимости и совместимость.** systemd-journald, доступ к записям текущей системы. В контейнере этот журнал может отсутствовать.

**Офлайн-установка.** На Kali с systemd входит в системное окружение; логи контейнеров доступны также через Docker.

## Команды и проверка

```text
journalctl --version
journalctl -u docker -b --since "10 min ago" --no-pager
systemctl status docker --no-pager
```

Найди момент, когда демон прекратил работу, и прочитай события непосредственно перед ним. Для отдельного APP посмотри docker compose logs.

**Частая ошибка.** Пустой результат может означать другой boot (-b), неправильный unit, rootless-службу или нехватку прав.

[Официальная документация](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)

[[START_HERE|На главную]]
