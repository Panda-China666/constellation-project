# Constellation Notebook

Vendored Quartz **v4.5.2**, upstream commit `4923affa7722dfc751f1074348e6dad214fe0c08`.
Upstream: https://github.com/jackyzha0/quartz — MIT license in `LICENSE.txt`.

The parent `build_notes.py` generates temporary bilingual Markdown from the shared
local-editor catalog, then invokes this engine with `NOTES_LANG=zh` or `en`.
Run the parent `build.py` instead of Quartz's sync/create commands.

Customizations:

- Quartz configuration/layout: paper and ink palette, no analytics or graph,
  system fonts, build-time MathJax SVG, native search, tags and backlinks.
- `NotebookNav.tsx`, `custom.scss`: site navigation, language routes, notebook styling.
- `processors/parse.ts`: normalize Windows separators before generating URL slugs.
- `emitters/contentPage.tsx`: render editor-owned `note: true` directory indexes as
  notes. FolderPage disabled so it cannot replace them with folder listings.
- Head/Favicon: Constellation icon and social preview.

Generated content, dependency installs and caches are ignored by the parent Git repository.
