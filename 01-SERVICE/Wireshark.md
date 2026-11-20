---
aliases:
  - "Wireshark и tshark · разобрать PCAP"
tags:
  - ad
  - сервис
---

# Wireshark и tshark · разобрать PCAP

Посмотреть последовательность TCP и отличить отказ приложения от сетевого тайм-аута. Вложенный дамп синтетический и содержит два HTTP-ответа.

**Версия.** 4.6.6 на странице Kali.

**Зависимости и совместимость.** Wireshark требует GUI; tshark работает в терминале, оба используют dissectors Wireshark. Для чтения файла не нужны права для live capture.

**Офлайн-установка.** Системные пакеты wireshark и/или tshark из кэша для своей Kali.

## Команды и проверка

```text
tshark --version
tshark -n -r 01-SERVICE/health-demo.pcap -d tcp.port==18765,http -Y http.response -T fields -e tcp.stream -e http.response.code
```

Открой health-demo.pcap через File → Open. Если HTTP не распознан, через Analyze → Decode As назначь TCP 18765 протокол HTTP. Фильтр http.response покажет ответы 200 и 503, Follow TCP Stream покажет тело.

**Частая ошибка.** Не путай capture filter с display filter. Параметр -Y отбирает кадры после разбора. -n отключает разрешение имён.

[Официальная документация](https://www.wireshark.org/docs/man-pages/tshark.html)

### Если Wireshark на ноутбуке отсутствует

Из корня выполни `python3 01-SERVICE/read-pcap.py 01-SERVICE/health-demo.pcap`. Увидишь две пары GET и ответа, сначала 200 OK, затем 503 Service Unavailable. Просмотрщик читает файл офлайн, поддерживает классический Ethernet/IPv4/TCP PCAP и стартовую строку HTTP в одном кадре. Для pcapng, IPv6, TLS и сборки потока используй Wireshark/tshark.

[[START_HERE|На главную]]
