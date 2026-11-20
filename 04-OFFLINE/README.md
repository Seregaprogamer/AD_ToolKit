---
aliases:
  - "Что можно установить без интернета"
tags:
  - ad
  - установка
---

# Что можно установить без интернета

| Вложение | Платформа | Способ |
|---|---|---|
| ad-usb-tools_1.0-1_amd64.deb | Linux x86-64. curl и jq требуют системную glibc ≥ 2.39 и sh. rg — статический ELF | Из корня `bash setup.sh`. Он проверяет хеши и распаковывает пакет в домашнюю папку |
| pygments-2.19.1-py3-none-any.whl | Python ≥ 3.8, amd64/arm64. Для CLI нужен pip в venv | Установка ниже; пригодится для просмотра исходников |
| notes-amd64.tar | Docker Engine Linux/amd64 | `bash load-docker.sh`, см. [[03-DOCKER/README\|Compose]] |
| modecheck | Linux/amd64 с glibc | Запуск напрямую или сборка из [исходника](../01-SERVICE/modecheck.c) |
| Сервис заметок и checker | Python 3.8+ c sqlite3, стандартная библиотека | [[06-LAB/README\|Практикум]], без установки |

Пакет ad-usb-tools собран для этого архива. Внутри приватные каталоги opt/ad-usb-tools/bin, lib и libexec, лицензии, готовые двоичные файлы curl 8.14.1, jq 1.7 и ripgrep 15.2.0. curl/jq запускаются через обёртки с локальными библиотеками. Системные glibc, корневые сертификаты для HTTPS и обычные настройки DNS берутся с машины. Не переноси библиотеки в /lib, PATH меняется только для выбранного терминала. Для статического rg на более старой системе извлеки пакет в **новую** папку: `dir=$(mktemp -d "$HOME/ad-rg.XXXXXXXX")`, затем `dpkg-deb -x 04-OFFLINE/amd64/*.deb "$dir"` и `"$dir/opt/ad-usb-tools/bin/rg" --version`.

### Obsidian

[[04-OFFLINE/Obsidian/README|Скачивание, запуск и открытие папки]].

### Pygments без сети

```bash
python3 -m venv "$HOME/ad-tools-venv"
"$HOME/ad-tools-venv/bin/python" -m pip install --no-index --no-deps 04-OFFLINE/all/*.whl
"$HOME/ad-tools-venv/bin/pygmentize" -l python -f terminal 06-LAB/service.py
```

Выбери свежее имя окружения, если каталог уже существует. В Kali компонент python3-venv может потребовать предварительной установки. Полный Pygments нужен только для подсветки.

### Заранее собрать пакеты Kali и зависимости

Используй Kali той же ветки, снимка и архитектуры, что и целевая машина. Готовые пакеты Docker Engine, Compose, tshark, и графических программ в архиве отсутствуют. Команды ниже нужны только для расширения комплекта. Обнови подписанные индексы Kali через `sudo apt update`. Скрипту нужен dpkg-scanpackages из dpkg-dev. Сверь доступные названия и версии:

```bash
dpkg --print-architecture
apt-cache policy docker.io docker-compose docker-compose-v2 tshark
apt-cache depends docker.io
```

Выбери пакет, который в этой ветке поставляет `docker compose version`. Для примера с обычными утилитами:

```bash
bash 04-OFFLINE/cache-kali.sh "$HOME/ad-kali-cache" tshark iproute2 python3-venv
```

Новая папка будет содержать .deb, транзитивные зависимости по решению APT с пустым статусом dpkg, список запрошенных пакетов, индекс и контрольные суммы. Инструмент не включает Recommends. Репозиторий может быть крупнее фактически необходимого на конкретной установленной системе. Для другого профиля используй новую папку. Запиши версию ОС, дату индексов и своего списка пакетов. При обрыве папка без готового SHA256SUMS считается незавершённой.

Скопируй готовую папку на целевую машину, по возможности в доступный для чтения каталог без пробелов. Проверь целостность и прочитай предлагаемый план:

```bash
sudo bash 04-OFFLINE/install-cache.sh /var/tmp/ad-kali-cache
```

Скрипт использует только локальный file-репозиторий для этой операции, отдельные индексы и кэш, сверяет хеши, симулирует установку и спрашивает подтверждение. Запускай его только для собственного доверенного кэша: свой SHA256SUMS защищает от случайных повреждений. При конфликте версий или предложении нежелательных обновлений отмени установку. Проверь на копии целевой системы в авиарежиме. **NOT TESTED** для реального репозитория Kali в этой сборке.

[Пакетные источники Kali](https://www.kali.org/docs/general-use/kali-apt-sources/) · [Docker на Kali](https://www.kali.org/docs/containers/installing-docker-on-kali/) · [APT](https://manpages.debian.org/trixie/apt/apt-get.8.en.html)

Полный список приватных библиотек и минимальных версий ABI есть в [[04-OFFLINE/amd64/DEPENDENCIES|ведомости сборки]].

[[START_HERE|На главную]]
