# 群星计划 · Constellation

首页保留原创云海晨光场景；课程区与个人博客采用 **Material for MkDocs** 成熟主题。线上只提供阅读，编辑器仅在本机运行，不进入 GitHub Pages 部署产物，也不上传编辑器源码到仓库的当前版本。

- 首页：https://panda-china666.github.io/constellation-project/
- 课程区：https://panda-china666.github.io/constellation-project/zh/courses/
- 个人博客：https://panda-china666.github.io/constellation-project/zh/blog/
- 英文课程：https://panda-china666.github.io/constellation-project/en/courses/

## 本地编辑

使用本次提供的完整 ZIP，保留 `.local-editor` 文件夹。双击 **start-editor.cmd**，打开本地创作工作室。当前电脑的依赖已装入项目 `.venv`；在新电脑首次运行会安装 requirements.txt，需要 Python 3.10+ 和网络。

左侧是可折叠的课程树。选中 T1，再点“添加子课程”，即可建立 T1 下的子课程；选中这个子课程再点同一按钮，还可以继续往下建立。每一级都可以有中英文正文与下级内容，未设置固定层数上限。

“课程设置 → 上级课程”可以移动节点及其整棵子树；不能移动到自己或自己的后代下面。箭头调整同级顺序。“移入回收站”保留整棵子树与正文，回收站可以恢复。左侧“栏目”管理顶层研究方向。

“＋ 随笔”新建博客文章。中英文分别编辑，日期、发布状态、分类在设置中管理。Markdown、LaTeX、实时预览、导出与双语独立标题均保留。

工作室有两种保存：编辑时自动缓存本机草稿；点击“保存本机”会真正写入 content 文件夹并构建网站。草稿与标为草稿的节点的全部子节点不进入发布产物。请定期导出备份。发布状态为“公开发布”后，可在本地工作室点击“发布到网站”，填写仅限此仓库的 GitHub 凭证，提交目录和公开内容；凭证不写入项目或浏览器存储。

也可以双击 **open-vscode.cmd**，或点本地工作室的“打开 VS Code”，用已安装的 VS Code 编辑 Markdown 文件。GitHub Desktop 也可以提交本地修改。

## 课程结构

`content/catalog.json` 是树形目录。每个节点有唯一 id、可为空的 parentId、中英文标题、分类、日期、发布状态与类型。正文仍为 `content/节点ID.zh.md` 和 `.en.md`，移动课程不会改变正文文件名。

当前整理为 10 门主课程、85 个专题与 T1 概率论下的 4 个章节。专题内容是原课程大纲拆分后的学习提纲，**不是已经写完的完整讲义**。每个节点均可继续补充和细分。博客保留为空，等待作者发布自己的文章。

生成后的路径包含层级，例如：

`/zh/courses/t1/t1-m1/t1-conditional/`

对应：T1 → 概率论基础 → 条件期望。网站侧栏可以逐层展开，正文右侧有页内目录，支持搜索、明暗模式、移动端导航和英文版本。

## 构建与部署

运行 `.venv/Scripts/python.exe build.py`。构建器依据目录树生成 MkDocs Markdown 与导航，再生成 dist/zh 与 dist/en。推送 main 后 GitHub Actions 安装固定版本依赖并自动发布。

- `.generated/`：临时生成的文档与配置，不进入 Git。
- `.local-editor/`：本地管理器及其依赖，已被 Git 忽略；仅完整 ZIP 中提供。
- `.venv/`：本地 Python 环境，不进入 Git 或交付 ZIP。
- `dist/`：静态阅读站点；不包含工作室、管理接口或编辑器依赖。
- `build.py`：树形校验、双语导航与站点构建。
- `theme.css`：成熟主题的小幅配色与排版定制。
- `vendor/mathjax.js`：自托管公式渲染器。

从 GitHub 直接克隆会获得阅读站点源码；本地可视化管理器请使用完整项目 ZIP。此前已发布的旧工作室地址会返回 404，网站导航不再显示编辑入口。

## 采用的开源项目

- Material for MkDocs：https://github.com/squidfunk/mkdocs-material ，MIT 许可证。课程导航、排版、搜索、移动端和博客引擎均来自真实主题。
- CS 自学指南参考配置：https://raw.githubusercontent.com/PKUFlyingPig/cs-self-learning/master/mkdocs.yml 。参考其以 Material 承载分层学习内容的方式，未复制其课程正文。
- 本地管理器继续使用 CodeMirror、marked、DOMPurify、MathJax、fflate，许可证随 `.local-editor/vendor` 保存。

首页美术为此前生成的原创场景，生成记录随交付文件提供。
