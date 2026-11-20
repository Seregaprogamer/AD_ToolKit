"""Тренировка целиком на случайном loopback-порту и в новой временной папке."""
from contextlib import contextmanager
from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent

@contextmanager
def server(state):
    log = state / "session.log"
    with log.open("w") as out:
        process = subprocess.Popen([sys.executable, str(HERE / "service.py"),
                                    "--state", str(state), "--port", "0"],
                                   stdout=out, stderr=out)
        try:
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline:
                match = re.search(r"Listening on 127\.0\.0\.1:(\d+)", log.read_text())
                if match:
                    yield match.group(1)
                    return
                if process.poll() is not None:
                    raise RuntimeError(log.read_text())
                time.sleep(0.04)
            raise RuntimeError("Тайм-аут запуска")
        finally:
            process.terminate()
            process.wait(timeout=5)

def check(state, port, expected_text, expected_code=0):
    run = subprocess.run([sys.executable, str(HERE / "checker.py"), str(state / "receipt"),
                          "--port", port], capture_output=True, text=True, timeout=8)
    if run.returncode != expected_code or expected_text not in run.stdout + run.stderr:
        raise RuntimeError(run.stdout + run.stderr)
    print("OK:", expected_text)

def main():
    with tempfile.TemporaryDirectory(prefix="ad-notes-test-") as temp:
        state = Path(temp)
        with server(state) as port:
            check(state, port, "создание")
            check(state, port, "старая запись сохранилась")
            (state / "mode").write_text("bad-schema")
            check(state, port, "поле text", 1)
            (state / "mode").write_text("maintenance")
            check(state, port, "503", 1)
            (state / "mode").write_text("ok")
            check(state, port, "старая запись сохранилась")
        with server(state) as port:
            check(state, port, "старая запись сохранилась")
        print("OK: откат и чтение после перезапуска")

if __name__ == "__main__":
    main()
