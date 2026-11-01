from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import json,re,os,webbrowser
from build import build
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/api/catalog':
            data=(ROOT/'content/catalog.json').read_bytes();self.send_response(200);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        else: super().do_GET()
    def do_POST(self):
        if self.headers.get('Origin') not in (f'http://127.0.0.1:{self.server.server_port}',f'http://localhost:{self.server.server_port}') or self.headers.get('Content-Type')!='application/json': self.send_error(403);return
        try:
            length=int(self.headers.get('Content-Length',0))
            if length>4_000_000: raise ValueError('Request too large')
            d=json.loads(self.rfile.read(length)); content=ROOT/'content'
            if self.path=='/api/save':
                catalog=d['catalog'];ids=set()
                cats=[g['id'] for g in catalog['categories']]
                if len(cats)!=len(set(cats)): raise ValueError('Duplicate category IDs')
                for g in catalog['categories']:
                    if not re.fullmatch('[a-z0-9-]+',g['id']): raise ValueError('Invalid category ID')
                for p in catalog['posts']:
                    if not re.fullmatch('[a-z0-9-]+',p['id']) or p['id'] in ids: raise ValueError('Invalid or duplicate article ID')
                    if p['category'] not in cats: raise ValueError('Unknown category')
                    ids.add(p['id'])
                for p in d.get('documents',[]):
                    if p['id'] not in ids: raise ValueError('Unknown article')
                    for lang in ('zh','en'):
                        target=content/f"{p['id']}.{lang}.md";temp=target.with_suffix('.tmp');temp.write_text(p[lang],encoding='utf-8');temp.replace(target)
                target=content/'catalog.json';temp=target.with_suffix('.tmp');temp.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8');temp.replace(target)
                build()
            else: self.send_error(404);return
            self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(b'{"ok":true}')
        except Exception as e:
            self.send_response(400);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(json.dumps({'error':str(e)}).encode())
if __name__=='__main__':
    print('Website: http://127.0.0.1:4173  |  Editor: http://127.0.0.1:4173/admin.html',flush=True)
    webbrowser.open('http://127.0.0.1:4173/admin.html')
    ThreadingHTTPServer(('127.0.0.1',4173),Handler).serve_forever()
