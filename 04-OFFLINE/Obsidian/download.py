"""Save an official Linux Obsidian AppImage next to this file for offline use."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import tempfile
from urllib.error import URLError
from urllib.request import Request, urlopen

VERSION = "1.15.1"
REPO = "obsidianmd/obsidian-releases"
FILES = {"amd64": f"Obsidian-{VERSION}.AppImage", "arm64": f"Obsidian-{VERSION}-arm64.AppImage"}
TARGET = Path(__file__).resolve().parent

def fetch(url):
    return urlopen(Request(url, headers={"User-Agent": "AD-Toolkit-Offline-Setup/1.0"}), timeout=60)

def file_hash(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()

def download(arch):
    name = FILES[arch]
    direct = f"https://github.com/{REPO}/releases/download/v{VERSION}/{name}"
    with fetch(f"https://api.github.com/repos/{REPO}/releases/tags/v{VERSION}") as response:
        release = json.load(response)
    asset = next((a for a in release["assets"] if a["name"] == name), None)
    if not asset or asset.get("browser_download_url") != direct:
        raise ValueError("Файл отсутствует в официальном релизе")
    digest = asset.get("digest") or ""
    if not digest.startswith("sha256:") or len(digest) != 71:
        raise ValueError("GitHub не вернул SHA-256 для этого файла. Используй ручную загрузку из инструкции.")
    expected = digest.split(":")[1]
    path = TARGET / name
    if path.exists():
        if file_hash(path) != expected:
            raise ValueError(f"Хеш существующего {path.name} не совпал. Перемести его и попробуй снова.")
    else:
        print("Скачиваю", name, flush=True)
        with tempfile.NamedTemporaryFile(dir=TARGET, delete=False, suffix=".part") as temp:
            temp_path = Path(temp.name)
        try:
            with fetch(direct) as response, temp_path.open("wb") as output:
                while block := response.read(1024 * 1024):
                    output.write(block)
            if temp_path.stat().st_size != asset["size"] or file_hash(temp_path) != expected:
                raise ValueError("Размер или SHA-256 загрузки не совпали")
            temp_path.replace(path)
        finally:
            if temp_path.exists():
                temp_path.unlink()
    if os.name == "posix":
        path.chmod(path.stat().st_mode | 0o100)
    (TARGET / (name + ".sha256")).write_bytes(f"{expected}  {name}\n".encode("ascii"))
    print("Готово:", path, flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arch", choices=("amd64", "arm64", "both"), help="архитектура целевой Kali")
    args = parser.parse_args()
    arch = args.arch or {"x86_64":"amd64","amd64":"amd64","aarch64":"arm64","arm64":"arm64"}.get(platform.machine().lower())
    if not arch:
        parser.error("укажи --arch amd64 или --arch arm64")
    try:
        for chosen in (FILES if arch == "both" else [arch]):
            download(chosen)
    except (ValueError, OSError, KeyError, URLError) as error:
        sys.exit(f"Загрузка не завершена: {error}\nОфициальный источник: https://obsidian.md/download")
