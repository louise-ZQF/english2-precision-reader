#!/usr/bin/env python3
"""Local companion server for the preserved English application.

The browser-facing API shapes are reconstructed from the public client.
No request is forwarded to the author's private backend.
"""
import argparse
import hashlib
import json
import mimetypes
import os
import re
import secrets
import sqlite3
import time
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / 'public'
STATE = ROOT / '.local-data'
APP_ID = 'aseeker-english-local'
MAX_BODY = 12 * 1024 * 1024


def connection():
    c = sqlite3.connect(STATE / 'local.sqlite3', timeout=10)
    c.row_factory = sqlite3.Row
    return c


def init_database():
    STATE.mkdir(exist_ok=True, mode=0o700)
    with connection() as c:
        c.executescript('''
          CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY, created_at INTEGER, content TEXT NOT NULL);
          CREATE TABLE IF NOT EXISTS corrections (
            id INTEGER PRIMARY KEY, created_at INTEGER, word TEXT NOT NULL,
            kind TEXT NOT NULL, content TEXT, note TEXT);
          CREATE TABLE IF NOT EXISTS backups (
            code TEXT PRIMARY KEY, data TEXT NOT NULL, expires INTEGER NOT NULL);
        ''')


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**mimetypes.types_map, '.js': 'application/javascript', '.json': 'application/json', '.woff2': 'font/woff2'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC), **kwargs)

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'same-origin')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def send_json(self, obj, status=200):
        payload = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        path = urllib.parse.urlsplit(self.path).path
        if path in {'/', '/about/'}:
            self.send_response(302)
            self.send_header('Location', '/english/')
            self.end_headers()
            return
        if path == '/local-api/health':
            return self.send_json({'ok': True, 'app': APP_ID, 'mode': 'local', 'version': 1})
        if path == '/biochem/api/check/':
            return self.send_json({'loggedIn': False, 'ok': True, 'authenticated': False})
        match = re.fullmatch(r'/biochem/api/backup/([A-Za-z0-9_-]{6,16})/', path)
        if match:
            with connection() as c:
                c.execute('BEGIN IMMEDIATE')
                row = c.execute('SELECT data, expires FROM backups WHERE code=?', (match[1],)).fetchone()
                if not row or row['expires'] <= int(time.time()):
                    return self.send_json({'ok': False, 'error': '链接已失效'}, 410)
                c.execute('DELETE FROM backups WHERE code=?', (match[1],))
            return self.send_json({'ok': True, 'data': row['data']})
        if path.startswith('/biochem/') or path.startswith('/login/') or path.startswith('/cellbio/'):
            self.send_response(302)
            self.send_header('Location', 'https://study.aseeker.bio' + self.path)
            self.end_headers()
            return
        # Prevent SimpleHTTPRequestHandler from exposing directory contents.
        target = Path(self.translate_path(path))
        if target.is_dir() and not (target / 'index.html').exists():
            self.send_error(404)
            return
        return super().do_GET()

    def do_POST(self):
        path = urllib.parse.urlsplit(self.path).path
        allowed = {'/biochem/api/backup/', '/biochem/api/feedback/', '/biochem/api/english-correction/', '/biochem/api/device/register-visitor/'}
        if path not in allowed:
            return self.send_json({'ok': False, 'error': '本地版没有此接口'}, 404)
        origin = self.headers.get('Origin')
        expected = 'http://' + self.headers.get('Host', '')
        if origin and origin != expected:
            return self.send_json({'ok': False, 'error': '不接受跨站请求'}, 403)
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length <= 0 or length > MAX_BODY:
                return self.send_json({'ok': False, 'error': '数据大小不合适'}, 413)
            obj = json.loads(self.rfile.read(length))
            if not isinstance(obj, dict):
                raise ValueError('请求必须为 JSON 对象')
        except (ValueError, UnicodeDecodeError):
            return self.send_json({'ok': False, 'error': 'JSON 格式错误'}, 400)
        now = int(time.time())
        if path.endswith('/register-visitor/'):
            return self.send_json({'ok': True})
        if path.endswith('/feedback/'):
            text = str(obj.get('content', '')).strip()
            if not text or len(text) > 1000:
                return self.send_json({'ok': False, 'error': '反馈需要 1—1000 个字'}, 400)
            with connection() as c:
                row = c.execute('INSERT INTO feedback(created_at, content) VALUES(?, ?)', (now, text))
                identifier = row.lastrowid
            return self.send_json({'ok': True, 'id': identifier, 'local': True})
        if path.endswith('/english-correction/'):
            word = str(obj.get('word', '')).strip()
            kind = str(obj.get('kind', 'other'))
            content = str(obj.get('content', '')).strip()
            note = str(obj.get('note', '')).strip()
            if not word or len(word) > 160 or kind not in {'meaning', 'phonetic', 'example', 'other'} or max(len(content), len(note)) > 10000:
                return self.send_json({'ok': False, 'error': '纠错内容不合适'}, 400)
            with connection() as c:
                row = c.execute('INSERT INTO corrections(created_at, word, kind, content, note) VALUES(?, ?, ?, ?, ?)', (now, word, kind, content, note))
                identifier = row.lastrowid
            return self.send_json({'ok': True, 'id': identifier, 'local': True})
        if path.endswith('/backup/'):
            payload = obj.get('data')
            try:
                if not isinstance(payload, str):
                    raise ValueError()
                backup = json.loads(payload)
                if backup.get('app') != 'aseeker-english' or backup.get('kind') != 'backup' or not isinstance(backup.get('data'), dict):
                    raise ValueError()
            except (ValueError, AttributeError):
                return self.send_json({'ok': False, 'error': '备份格式不正确'}, 400)
            code = secrets.token_urlsafe(9)
            with connection() as c:
                c.execute('DELETE FROM backups WHERE expires < ?', (now,))
                c.execute('INSERT INTO backups(code, data, expires) VALUES(?, ?, ?)', (code, payload, now + 86400))
            url = expected + '/english/?import=' + code
            return self.send_json({'ok': True, 'code': code, 'url': url, 'expiresAt': now + 86400})

    def log_message(self, fmt, *args):
        if args and len(args) > 1 and str(args[1]) not in {'200', '304'}:
            super().log_message(fmt, *args)


def main():
    parser = argparse.ArgumentParser(description='考研英语本地版')
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--open', action='store_true', help='启动后在默认浏览器打开')
    args = parser.parse_args()
    init_database()
    # Reuse the existing local app when the desktop launcher is double-clicked again.
    import urllib.request
    if args.open:
        try:
            with urllib.request.urlopen(f'http://127.0.0.1:{args.port}/local-api/health', timeout=1) as r:
                active = json.load(r)
            if active.get('app') == APP_ID:
                import webbrowser
                webbrowser.open(f'http://127.0.0.1:{args.port}/english/')
                return
        except Exception:
            pass
    for port in range(args.port, args.port + 20):
        try:
            server = ThreadingHTTPServer((args.host, port), Handler)
            break
        except OSError:
            if port == args.port + 19:
                raise
    url = f'http://127.0.0.1:{port}/english/'
    print(f'考研英语本地版已启动：{url}\n关闭此终端或按 Ctrl+C 可停止。', flush=True)
    if args.open:
        import webbrowser
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
