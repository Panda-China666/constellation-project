from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parent
FILES=('index.html','style.css','app.js','math-config.js','markdown.js','studio.html','studio.css','studio.js','admin.html')
def build():
 out=ROOT/'dist';out.mkdir(exist_ok=True)
 for name in FILES:shutil.copy2(ROOT/name,out/name)
 for name in ('assets','vendor'):shutil.copytree(ROOT/name,out/name,dirs_exist_ok=True)
 dest=out/'content';dest.mkdir(exist_ok=True)
 catalog=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8-sig'))
 catalog['posts']=[p for p in catalog['posts'] if p.get('published',True)]
 for old in dest.glob('*.md'):old.unlink()
 for p in catalog['posts']:
  for lang in ('zh','en'):
   f=ROOT/'content'/f"{p['id']}.{lang}.md";shutil.copy2(f,dest/f.name)
 (dest/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
 (out/'.nojekyll').touch()
 print(f"Built {len(catalog['posts'])} published entries, writing studio and self-hosted assets into {out}")
if __name__=='__main__':build()
