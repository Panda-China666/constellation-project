"""Build the separate Quartz notebook from the same local editor content."""
from pathlib import Path
from html import escape
from datetime import date
import os, re, shutil, subprocess
import yaml

def build_notes(root, published, out, theme=None):
    theme = theme or root / 'notes-theme'
    node = shutil.which('node')
    npm = shutil.which('npm.cmd' if os.name == 'nt' else 'npm')
    if not node or not npm:
        raise RuntimeError('The notebook requires Node.js 22+ and npm. Install Node.js, then save again.')
    if int(subprocess.check_output([node, '--version'], text=True).strip().lstrip('v').split('.')[0]) < 22:
        raise RuntimeError('The notebook requires Node.js 22+.')
    if not (theme / 'node_modules/esbuild/package.json').exists():
        subprocess.run([npm, 'ci', '--no-audit', '--no-fund'], cwd=theme, check=True)
    notes = sorted((p for p in published if p['category'] == 'journal'), key=lambda p: (p['date'], p['id']), reverse=True)
    for lang in ('zh', 'en'):
        zh = lang == 'zh'
        key = 'titleZh' if zh else 'titleEn'
        docs = root / '.generated' / ('notes-' + lang)
        if docs.exists():
            assert docs.resolve().parent == (root / '.generated').resolve()
            shutil.rmtree(docs)
        docs.mkdir(parents=True)
        title = '我的随笔' if zh else 'Field notes'
        intro = '一些随手记下的问题、观察与想法。' if zh else 'Questions, observations, and thoughts along the way.'
        index = '<p class="notebook-kicker">THE CONSTELLATION NOTEBOOK</p>\n\n'
        index += '<p class="notebook-intro">' + intro + '</p>\n\n'
        if not notes:
            index += '<div class="notebook-empty"><span class="empty-number">PAGE 001</span><h2>' + ('这一页，留给下一个想法。' if zh else 'A page for the next thought.') + '</h2><p>' + ('还没有公开的随笔。' if zh else 'No public notes yet.') + '</p></div>\n'
        previous_year = None
        for p in notes:
            raw = (root / f"content/{p['id']}.{lang}.md").read_text(encoding='utf-8-sig')
            meta = {'title': p[key], 'date': date.fromisoformat(p['date']), 'tags': p.get('tags', []), 'note': True}
            folder = docs / p['id']
            folder.mkdir()
            (folder / 'index.md').write_text('---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n' + raw, encoding='utf-8')
            year = p['date'][:4]
            if year != previous_year:
                index += f'\n## {year}\n\n'
                previous_year = year
            excerpt = raw.split('<!-- more -->')[0]
            excerpt = re.sub(r'```[\s\S]*?```|\$\$[\s\S]*?\$\$|<[^>]*>', '', excerpt)
            excerpt = re.sub(r'!\[.*?\]\(.*?\)', '', excerpt)
            excerpt = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', excerpt)
            excerpt = re.sub(r'[#*_`>\[\]]', '', excerpt)
            excerpt = ' '.join(excerpt.split())
            excerpt = excerpt[:140] + ('…' if len(excerpt) > 140 else '')
            tags = ' · '.join('#' + t for t in p.get('tags', []))
            index += f'<a class="note-entry" href="{p["id"]}/"><time datetime="{p["date"]}">{p["date"]}</time><strong>{escape(p[key])}</strong><span class="note-summary">{escape(excerpt)}</span><span class="note-tags">{escape(tags)}</span></a>\n\n'
        index += '<p class="notebook-count">' + (f'{len(notes):02d} 篇记录 · 持续生长的笔记本' if zh else f'{len(notes):02d} notes · An evolving notebook') + '</p>\n'
        (docs / 'index.md').write_text('---\n' + yaml.safe_dump({'title': title, 'description': intro, 'enableToc': False}, allow_unicode=True) + '---\n\n' + index, encoding='utf-8')
        env = dict(os.environ, NOTES_LANG=lang)
        subprocess.run([node, 'quartz/bootstrap-cli.mjs', 'build', '-d', docs.as_posix(), '-o', (out / lang / 'blog').as_posix(), '--concurrency=1'], cwd=theme, env=env, check=True)
    print(f'Built bilingual Quartz notebook: {len(notes)} published notes.')
