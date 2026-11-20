---
aliases:
  - "Библиотеки Python для AD"
tags:
  - ad
  - справочник
---

# Библиотеки Python для AD

### Прочитать HTTP-ответ и проверить JSON

Для упражнения запусти сервис заметок по [[06-LAB/README|инструкции лаборатории]]. В другом терминале открой Python (`python3` в Linux или `py -3` в Windows). Пример использует стандартную библиотеку и работает без pip.

```python
import json
from urllib.request import urlopen

with urlopen("http://127.0.0.1:18765/health", timeout=3) as response:
    print(response.status, response.headers.get_content_type())
    data = json.load(response)

print(data.get("status"))
```

Ожидаемый вывод — `200 application/json`, затем `ok`. Число показывает результат HTTP-запроса, поле `status` — состояние по контракту приложения. При `HTTPError` у сервера есть HTTP-ответ: код доступен в `exc.code`, если поймать исключение как `exc`. При отказе в соединении проверь запущенный процесс и порт. Успешный ответ на `/health` ещё не проверяет сохранение записей. Это делает [[06-LAB/README|чекер заметок]].

**Если уже установлен requests**, тот же запрос короче. Библиотека ставится отдельно, в архиве её дистрибутива нет.

```python
import requests

r = requests.get("http://127.0.0.1:18765/health", timeout=(2, 3))
r.raise_for_status()
print(r.json()["status"])
```

### Разобрать байты без сети

Когда в спецификации протокола указано «первые два байта — длина сообщения, старший байт первым», используй `struct`. На учебном кадре ниже получишь `3 ABC`.

```python
import struct

frame = bytes.fromhex("00 03 41 42 43")
length = struct.unpack_from(">H", frame)[0]
body = frame[2:]
if len(body) != length:
    raise ValueError("Длина тела отличается от заголовка")
print(length, body.decode("ascii"))
```

Чтобы посмотреть пример с реальной структурой пакета, открой `01-SERVICE/read-pcap.py` и приложенный `health-demo.pcap`. [Справка requests](https://requests.readthedocs.io/en/latest/user/quickstart/) · [Форматы struct](https://docs.python.org/3/library/struct.html).

[[09-CHEATSHEETS/ROUND|Команды на один раунд]] · [[README|Все руководства]]
