from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parent

def build():
    out=ROOT/'dist';out.mkdir(exist_ok=True)
    for name in ('index.html','style.css','app.js'):
        shutil.copy2(ROOT/name,out/name)
    dest=out/'content';dest.mkdir(exist_ok=True)
    catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8-sig'))
    catalog['posts']=[p for p in catalog['posts'] if p.get('published',True)]
    for old in dest.glob('*'): old.unlink()
    for p in catalog['posts']:
        for lang in ('zh','en'):
            f=ROOT/'content'/f"{p['id']}.{lang}.md"
            shutil.copy2(f,dest/f.name)
    (dest/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
    (out/'.nojekyll').touch()
    print(f"Built {len(catalog['posts'])} published entries into {out}")
if __name__=='__main__': build()
