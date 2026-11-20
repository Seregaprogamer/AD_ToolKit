---
aliases:
  - "Kali ARM64"
tags:
  - ad
  - установка
---

# Kali ARM64

Проверь `uname -m` → aarch64 и `dpkg --print-architecture` → arm64. Готовые CLI и образ с меткой amd64 собраны для другой архитектуры.

Сразу доступны заметки Obsidian, встроенный поиск по хранилищу, PCAP, колесо Pygments и сервис с чекером на системном Python. Используй [[06-LAB/README|тренировку без Docker]]. Для ELF-упражнения из корня выполни `cc -g -O0 01-SERVICE/modecheck.c -o "$HOME/modecheck-arm64"`. ARM64 понадобится свой компилятор.

Пакеты rg, curl, jq и Docker можно подготовить на ARM64 Kali [[04-OFFLINE/README|через локальный APT-репозиторий]]. Тест ARM64-исполнения в этой сборке не проводился.

[[START_HERE|На главную]]
