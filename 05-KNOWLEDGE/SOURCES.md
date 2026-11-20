---
aliases:
  - "Источники и версии"
tags:
  - ad
  - раунд
---

# Источники и версии

Дата подготовки — 19 ноября 2026 года. Числа в карточках инструментов обозначают либо фактическую вложенную версию, либо значение на странице Kali/релиза. Для Kali Rolling решающее значение имеет версия-кандидат в индексах конкретной машины.

| Тема | Первичный источник | Что сверять |
|---|---|---|
| Финал | [Страница турнира](https://dovuz.innopolis.university/innoctfjunior) · [Регламент](https://start.innopolis.university/upload/sprint.editor/13e/5u2cn8845uwj1eaxyq03d6un9t0tbcwl.pdf) | П. 7.3 про оборудование, п. 7.6 про инфраструктуру, раздел 8 про AI |
| ForcAD | [README](https://github.com/pomo-mondreganto/ForcAD) · [релизы](https://github.com/pomo-mondreganto/ForcAD/releases) | Стабильный тег, актуальные для него требования и конфиги |
| Контейнеры | [Kali Docker](https://www.kali.org/docs/containers/installing-docker-on-kali/) · [команды Compose](https://docs.docker.com/reference/cli/docker/compose/) · [image save](https://docs.docker.com/reference/cli/docker/image/save/) | Разница между установкой движка, импортом образа и данными томов |
| APT | [Источники Kali](https://www.kali.org/docs/general-use/kali-apt-sources/) · [apt-get](https://manpages.debian.org/trixie/apt/apt-get.8.en.html) | Ветка, архитектура и согласованное решение зависимостей |
| HTTP и протоколы | [curl](https://curl.se/docs/manpage.html) · [Nmap/Ncat](https://www.kali.org/tools/nmap/) · [Wireshark](https://www.kali.org/tools/wireshark/) · [Burp](https://www.kali.org/tools/burpsuite/) | Поведение клиента, разбор файла, версии инструментов |
| Код и данные | [GDB](https://www.kali.org/tools/gdb/) · [Ghidra](https://www.kali.org/tools/ghidra/) · [jq](https://jqlang.org/manual/) · [SQLite в Python](https://docs.python.org/3/library/sqlite3.html) | Версии, ABI, проверка JSON, резервное копирование |
| Поиск и просмотр | [ripgrep](https://github.com/BurntSushi/ripgrep) · [Pygments](https://pygments.org/docs/) · [CyberChef](https://github.com/gchq/CyberChef/releases) | Релизы и штатная документация |

Вложенные утилиты взяты из среды сборки Debian amd64, упакованы в отдельный локальный .deb с приватными библиотеками. Это не пакет, выпущенный Kali. Полные лицензии компонентов curl и jq находятся внутри него в opt/ad-usb-tools/licenses. Pygments поставляется со своим wheel и метаданными. Лицензии runtime учебного образа лежат в /usr/share/doc/ad-lab внутри слоя.

[[START_HERE|На главную]]
