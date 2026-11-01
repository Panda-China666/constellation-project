from pathlib import Path
import json,re,shutil,subprocess,sys
import yaml
from datetime import date
ROOT=Path(__file__).resolve().parent
BASE='https://panda-china666.github.io/constellation-project/'

def validate_catalog(c):
 if not isinstance(c.get('posts'),list) or not isinstance(c.get('categories'),list):raise ValueError('Invalid catalog')
 cats={g['id'] for g in c['categories']};nodes={}
 for p in c['posts']:
  if not re.fullmatch('[a-z0-9-]+',p['id']) or p['id'] in nodes:raise ValueError('Duplicate or invalid node ID')
  if p['category'] not in cats:raise ValueError('Unknown category')
  nodes[p['id']]=p
 for p in c['posts']:
  seen={p['id']};parent=p.get('parentId')
  if p['category']=='journal' and parent:raise ValueError('Blog posts cannot have course parents')
  while parent:
   if parent not in nodes:raise ValueError('Missing parent')
   if parent in seen:raise ValueError('Course hierarchy contains a cycle')
   seen.add(parent);ancestor=nodes[parent]
   if ancestor['category']!=p['category']:raise ValueError('Parent category mismatch')
   parent=ancestor.get('parentId')
 return nodes

def public_nodes(c):
 nodes=validate_catalog(c)
 def visible(p):
  while p:
   if not p.get('published',True) or p.get('trashed'):return False
   p=nodes.get(p.get('parentId'))
  return True
 return [p for p in c['posts'] if visible(p)]

def course_path(p,nodes):
 ids=[p['id']];parent=p.get('parentId')
 while parent:ids.insert(0,parent);parent=nodes[parent].get('parentId')
 return 'courses/'+'/'.join(ids)+'/index.md'

def build():
 c=json.loads((ROOT/'content/catalog.json').read_text(encoding='utf-8-sig'));published=public_nodes(c);nodes={p['id']:p for p in published};out=ROOT/'dist';out.mkdir(exist_ok=True)
 # Remove obsolete public editor and old SPA payloads. Never copy local tool sources.
 for name in ('studio.html','studio.css','studio.js','admin.html','admin.js','app.js','markdown.js','math-config.js'):
  target=out/name
  if target.is_file():target.unlink()
 for name in ('content','vendor'):
  target=out/name
  if target.exists():
   # These are generated directories within this project's dist only.
   assert target.resolve().parent==out.resolve();shutil.rmtree(target)
 for name in ('index.html','style.css','landing.js'):shutil.copy2(ROOT/name,out/name)
 shutil.copytree(ROOT/'assets',out/'assets',dirs_exist_ok=True)
 generated=ROOT/'.generated';generated.mkdir(exist_ok=True)
 children=lambda id:[p for p in published if p.get('parentId')==id and p['category']!='journal']
 for lang in ('zh','en'):
  title='群星计划' if lang=='zh' else 'Constellation';courses='课程区' if lang=='zh' else 'Courses';blog='我的随笔' if lang=='zh' else 'Field notes';overview='课程概览' if lang=='zh' else 'Overview';key='titleZh' if lang=='zh' else 'titleEn'
  docs=generated/('docs-'+lang)
  if docs.exists():assert docs.resolve().parent==generated.resolve();shutil.rmtree(docs)
  docs.mkdir();(docs/'courses').mkdir();
  (docs/'theme.css').write_bytes((ROOT/'theme.css').read_bytes())
  (docs/'mathjax-config.js').write_bytes((ROOT/'mathjax-config.js').read_bytes())
  (docs/'mathjax.js').write_bytes((ROOT/'vendor/mathjax.js').read_bytes())
  (docs/'index.md').write_text(f'# {title}\n\n'+('人工智能课程与研究笔记。' if lang=='zh' else 'Artificial intelligence courses and research notes.')+f'\n\n[**{courses} →**](courses/index.md) · [**{blog} →**]({BASE}{lang}/blog/)\n',encoding='utf-8')
  def nav_node(p):
   path=course_path(p,nodes);kids=children(p['id']);label=(p['code']+' · ' if p.get('kind')=='course' else '')+p[key]
   if kids:return {label:[{overview:path}]+[nav_node(k) for k in kids]}
   return {label:path}
  course_nav=[{('全部课程' if lang=='zh' else 'All courses'):'courses/index.md'}]
  index='# '+courses+'\n\n'+('系统学习人工智能的理论、模型、系统与决策。选择一门课程，展开左侧目录即可逐层阅读。' if lang=='zh' else 'Study the theory, models, systems and decision-making foundations of AI. Select a course and explore its nested curriculum.')+'\n\n'
  for group in c['categories']:
   if group['id']=='journal':continue
   roots=[p for p in published if p['category']==group['id'] and not p.get('parentId')]
   if not roots:continue
   course_nav.append({group[lang]:[nav_node(p) for p in roots]})
   index+='## '+group[lang]+'\n\n<div class="grid cards" markdown>\n\n'
   for p in roots:
    path=course_path(p,nodes).removeprefix('courses/');count=len(children(p['id']))
    index+=f'-   **{p["code"]}** · **[{p[key]}]({path})**\n\n    '+(f'{count} 个子课程 · 14 周' if lang=='zh' else f'{count} modules · 14 weeks')+'\n\n'
   index+='</div>\n\n'
  (docs/'courses/index.md').write_text(index,encoding='utf-8')
  for p in published:
   text=(ROOT/f"content/{p['id']}.{lang}.md").read_text(encoding='utf-8-sig')
   if p['category']=='journal':continue
   path=docs/course_path(p,nodes);path.parent.mkdir(parents=True,exist_ok=True)
   heading=(p['code']+' · ' if p.get('kind')=='course' else '')+p[key]
   content='# '+heading+'\n\n'+text+'\n'
   kids=children(p['id'])
   if kids:
    content+='\n## '+('子课程' if lang=='zh' else 'Subcourses')+'\n\n'
    for kid in kids:content+=f'- [{kid[key]}]({kid["id"]}/index.md)\n'
   path.write_text(content,encoding='utf-8')
  intro=('记录学习过程中的问题、日常与独立思考。' if lang=='zh' else 'Questions, observations and independent thinking along the way.')
  config={'site_name':title,'site_url':BASE+lang+'/','site_description':intro,'docs_dir':str(docs),'site_dir':str(out/lang),'theme':{'name':'material','language':lang,'font':False,'features':['navigation.tabs','navigation.tabs.sticky','navigation.indexes','navigation.sections','navigation.top','navigation.footer','toc.follow','search.highlight','search.suggest','content.code.copy'],'palette':[{'scheme':'default','primary':'custom','accent':'teal','toggle':{'icon':'material/weather-night','name':'切换深色模式' if lang=='zh' else 'Dark mode'}},{'scheme':'slate','primary':'custom','accent':'teal','toggle':{'icon':'material/weather-sunny','name':'切换浅色模式' if lang=='zh' else 'Light mode'}}]},'nav':[{'首页' if lang=='zh' else 'Home':BASE},{courses:course_nav},{blog:BASE+lang+'/blog/'}],'plugins':[{'search':{'lang':['en','zh'] if lang=='zh' else ['en']}}],'markdown_extensions':['admonition','attr_list','md_in_html','footnotes','tables',{'toc':{'permalink':True}},'pymdownx.details',{'pymdownx.superfences':{}},{'pymdownx.arithmatex':{'generic':True}}],'extra_css':['theme.css'],'extra_javascript':['mathjax-config.js','mathjax.js'],'extra':{'alternate':[{'name':'简体中文','link':BASE+'zh/courses/','lang':'zh'},{'name':'English','link':BASE+'en/courses/','lang':'en'}]},'copyright':'群星计划 · Constellation'}
  conf=generated/f'mkdocs-{lang}.yml';conf.write_text(yaml.safe_dump(config,allow_unicode=True,sort_keys=False),encoding='utf-8')
  subprocess.run([sys.executable,'-m','mkdocs','build','--config-file',str(conf)],cwd=ROOT,check=True)
 from build_notes import build_notes
 build_notes(ROOT,published,out)
 (out/'.nojekyll').touch()
 # Machine-readable route map is public content only, not an editing API.
 routes={p['id']:{l:BASE+l+'/'+course_path(p,nodes).removesuffix('index.md') for l in ('zh','en')} for p in published if p['category']!='journal'}
 (out/'routes.json').write_text(json.dumps(routes,ensure_ascii=False),encoding='utf-8')
 print(f'Built Material courses and Quartz notebook: {len(published)} content nodes. Editor excluded.')
if __name__=='__main__':build()
