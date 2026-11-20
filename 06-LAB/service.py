"""Учебный HTTP-сервис. Python 3.8+, только стандартная библиотека."""
import argparse
import json
import logging
import sqlite3
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(BaseHTTPRequestHandler):
    def reply(self, code, content):
        data = json.dumps(content, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def healthy(self):
        try:
            mode = self.server.mode.read_text().strip()
        except OSError:
            mode = "missing"
        if mode in ("ok", "bad-schema"):
            return mode
        self.reply(503, {"error": "maintenance", "mode": mode})
        return None

    def do_GET(self):
        mode = self.healthy()
        if not mode:
            return
        if self.path == "/health":
            self.reply(200, {"status": "ok"})
        elif self.path.startswith("/notes/"):
            key = self.path[len("/notes/"):]
            with sqlite3.connect(self.server.db) as db:
                row = db.execute("SELECT body FROM notes WHERE id=?", (key,)).fetchone()
            if row:
                field = "text" if mode == "ok" else "value"
                self.reply(200, {field: row[0]})
            else:
                self.reply(404, {"error": "unknown note"})
        else:
            self.reply(404, {"error": "unknown route"})

    def do_POST(self):
        if not self.healthy():
            return
        if self.path != "/notes":
            return self.reply(404, {"error": "unknown route"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 4096:
                raise ValueError()
            note = json.loads(self.rfile.read(length))
            if not isinstance(note, dict) or not isinstance(note.get("text"), str):
                raise ValueError()
        except (ValueError, UnicodeError):
            return self.reply(400, {"error": "expected short JSON object with text"})
        key = uuid.uuid4().hex
        with sqlite3.connect(self.server.db) as db:
            db.execute("INSERT INTO notes VALUES (?,?)", (key, note["text"]))
        self.reply(201, {"id": key})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--port", type=int, default=18765)
    parser.add_argument("--container", action="store_true", help="Listen on container interfaces")
    args = parser.parse_args()
    args.state.mkdir(parents=True, exist_ok=True)
    mode = args.state / "mode"
    try:
        with mode.open("x") as handle:
            handle.write("ok\n")
    except FileExistsError:
        pass
    db_file = args.state / "notes.sqlite"
    with sqlite3.connect(db_file) as db:
        db.execute("CREATE TABLE IF NOT EXISTS notes(id TEXT PRIMARY KEY, body TEXT NOT NULL)")
    bind = "0.0.0.0" if args.container else "127.0.0.1"
    with ThreadingHTTPServer((bind, args.port), Handler) as server:
        server.mode, server.db = mode, db_file
        logging.warning("Listening on %s:%d", bind, server.server_port)
        server.serve_forever()

if __name__ == "__main__":
    main()
