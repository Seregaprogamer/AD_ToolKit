---
aliases:
  - "Obsidian на Kali и Windows"
  - "Как установить Obsidian"
  - "Как открыть хранилище"
tags:
  - ad
  - установка
---

# Obsidian на Kali и Windows

## Сегодня · положить приложение на флешку

Официальный Linux AppImage скачивается один раз. После загрузки перенеси **всю распакованную папку AD-TOOLKIT** на флешку, включая скрытую папку .obsidian. В исходном tar.gz лежит загрузчик. Сам AppImage появится рядом с ним после загрузки; уже скачанный архив при этом не изменится.

В Kali открой терминал в AD-TOOLKIT. На ноутбуке с Intel/AMD выполни:

```bash
bash setup.sh obsidian --arch amd64
bash 04-OFFLINE/Obsidian/open.sh
```

На ARM выбери `--arch arm64`. Если тип выданного ноутбука неизвестен, `--arch both` сохранит оба файла. Загрузчику нужен Python 3.8+ и интернет. Он сверяет размер и SHA-256 из официального релиза. Повторный запуск проверяет скачанный файл.

**Если готовишь флешку в Windows:** в PowerShell в папке AD-TOOLKIT введи `py -3 .\04-OFFLINE\Obsidian\download.py --arch amd64`. Без Python просто скачай [AppImage для Intel/AMD](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.15.1/Obsidian-1.15.1.AppImage) или [AppImage для ARM64](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.15.1/Obsidian-1.15.1-arm64.AppImage) и сохрани файл с исходным именем в 04-OFFLINE/Obsidian. Сам Linux AppImage запускается на Kali. Если хочешь читать заметки уже на Windows, на [странице загрузки](https://obsidian.md/download) выбери Windows → Universal, установи Obsidian и открой ту же папку.

## Перед выездом · проверить без сети

1. На Kali скопируй всю распакованную папку вместе с AppImage на локальный диск. Для ручной загрузки на Intel/AMD из корня выполни `chmod u+x 04-OFFLINE/Obsidian/Obsidian-1.15.1.AppImage`; на ARM укажи имя с суффиксом -arm64.
2. Запусти `bash 04-OFFLINE/Obsidian/open.sh`. Он открывает системный Obsidian, если тот установлен, иначе запускает локальный AppImage. Если флешка смонтирована с noexec, скопируй файл в домашнюю папку, выставь право запуска и запусти его оттуда. При сообщении о FUSE заранее проверь поддержку AppImage на своей Kali. Для amd64 доступен и официальный [Deb-пакет](https://github.com/obsidianmd/obsidian-releases/releases/download/v1.15.1/obsidian_1.15.1_amd64.deb); устанавливай его заранее, пока APT может получить зависимости.
3. В стартовом окне нажми **Open folder as vault → Open** и укажи папку AD-TOOLKIT, внутри которой лежит START_HERE.md. Если открыт другой vault, открой меню выбора хранилищ и выбери **Manage vaults**. Для сохранения рабочих заметок папка должна быть доступна для записи.
4. Выключи интернет, закрой и снова открой Obsidian, перейди на START_HERE, найди ошибку через Ctrl+Shift+F. Для этого хранилища достаточно встроенных функций Obsidian.

После редактирования заметок полная проверка оригинального набора может показать изменения. Для проверки только программ и скриптов выполни `bash verify.sh --tools`.

## Как пользоваться во время раунда

| Что нужно | Действие |
|---|---|
| Открыть заметку по названию или псевдониму | Ctrl+O → набери «Первые 5 минут» или «Connection refused» → Enter |
| Найти сообщение в тексте | Ctrl+Shift+F → введи `tag:#ошибка "Connection refused"` |
| Посмотреть все ошибки Docker | Ctrl+Shift+F → `tag:#ошибка tag:#docker` |
| Найти строку на текущей странице | Ctrl+F |
| Перейти к связанному шагу | Нажми ссылку в режиме чтения или Ctrl+щелчок в редакторе |
| Записать результат проверки | Открой журнал сервиса, создай копию для текущего раунда и заполни время, изменение, проверку и способ возврата |

[Официальная установка](https://obsidian.md/help/install) · [Открытие папки](https://obsidian.md/help/vault) · [Поиск в Obsidian](https://obsidian.md/help/plugins/search)

[[START_HERE|На главную]]
