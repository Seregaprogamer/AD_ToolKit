---
aliases:
  - "Ghidra · прочитать небольшой ELF"
tags:
  - ad
  - сервис
---

# Ghidra · прочитать небольшой ELF

Определить, где программа разбирает режим конфигурации, без её запуска.

**Версия.** 12.1.3 на странице Kali.

**Зависимости и совместимость.** GUI и JDK версии, указанной в Installation Guide выбранного релиза. Готовый ELF читается независимо от архитектуры хоста Ghidra.

**Офлайн-установка.** Заранее установи ghidra и JDK из одной ветки Kali или используй официальный релиз с его инструкцией.

## Команды и проверка

```text
file 04-OFFLINE/amd64/modecheck
readelf -h 04-OFFLINE/amd64/modecheck
ghidra
```

Создай локальный Non-Shared Project. Импортируй modecheck → CodeBrowser → Analyze. Найди check_mode в Symbol Tree, открой Decompiler и сопоставь ветви ready/maintenance с C-исходником. Проверь, откуда вызывается функция в main.

**Частая ошибка.** Если видны только инструкции, открой Window → Decompiler. При отказе старта проверь java -version и требования именно твоей версии.

[Официальная документация](https://github.com/NationalSecurityAgency/ghidra)

[[START_HERE|На главную]]
