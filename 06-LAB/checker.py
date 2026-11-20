"""Проверка записи и повторного чтения на фиксированном локальном адресе."""
import argparse
import json
from pathlib import Path
import sys
import uuid
from urllib.request import Request, build_opener, ProxyHandler
from urllib.error import URLError

def main():
    p = argparse.ArgumentParser()
    p.add_argument("receipt", type=Path, help="Отдельный файл квитанции для каждой базы")
    p.add_argument("--port", type=int, default=18765)
    a = p.parse_args()
    url = "http://127.0.0.1:%d" % a.port
    opener = build_opener(ProxyHandler({}))
    def call(path, code, data=None):
        request = Request(url + path, data=data, headers={"Content-Type": "application/json"})
        with opener.open(request, timeout=3) as r:
            if r.status != code:
                raise ValueError("HTTP %s вместо %s" % (r.status, code))
            return json.load(r)
    def read(saved):
        if call("/notes/" + saved["id"], 200).get("text") != saved["text"]:
            raise ValueError("GET: поле text отсутствует или значение изменилось")
    if call("/health", 200).get("status") != "ok":
        raise ValueError("/health: ожидался status=ok")
    if a.receipt.exists():
        read(json.loads(a.receipt.read_text()))
        print("OK: старая запись сохранилась")
    marker = "practice-" + uuid.uuid4().hex
    result = call("/notes", 201, json.dumps({"text": marker}).encode())
    saved = {"id": result["id"], "text": marker}
    read(saved)
    temp = a.receipt.with_name(a.receipt.name + "." + uuid.uuid4().hex)
    with temp.open("x") as f:
        json.dump(saved, f)
    temp.replace(a.receipt)
    print("OK: /health, создание, чтение, формат JSON")

if __name__ == "__main__":
    try:
        main()
    except (OSError, URLError, ValueError, KeyError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
