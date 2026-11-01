# 群星计划 · Constellation

原创云海与浮岛首页，极简研究笔记阅读界面。为个人知识、研究课程、日常随笔而建。静态发布到 GitHub Pages，编辑器只在本地运行。

## 立即开始

1. 解压项目后，双击 `start-editor.cmd`（当前电脑已有 Python 3.10）。
2. 浏览器会打开 http://127.0.0.1:4173/admin.html 。网站首页是 http://127.0.0.1:4173/ 。
3. 左侧选择文章，分别编辑中文和 English；支持 Markdown、表格、代码块、`$x^2$`、`$$E=mc^2$$`、`\(...\)`、`\[...\]`。
4. 点击“预览当前语言”查看排版和公式；点击“保存并生成网站”，或 Ctrl+S。保存是真实写入本地文件，不是浏览器临时存储。
5. “管理目录”可修改栏目名称与说明、新建栏目、调整栏目顺序；文章用上移/下移调整顺序。
6. 新文章默认为草稿。准备公开时改成“公开发布”，再保存。随笔按日期从新到旧展示。

关闭命令窗口即停止编辑器；再次双击即可继续。修改前建议备份或使用 Git 版本历史。编辑器不提供自动保存，请留意未保存提示。

## GitHub 发布（仓库名：constellation-project）

项目仓库：https://github.com/Panda-China666/constellation-project

网站：https://panda-china666.github.io/constellation-project/

发布状态请查看仓库 Actions。此前在聊天中暴露的密钥应在本次发布完成后撤销，网站运行不依赖该密钥。

可用 GitHub Desktop 克隆上述仓库，或将本地项目接入同一远端。请确保 `index.html`、`build.py`、`content`、`.github` 在仓库根目录，不要把包含本项目的外层目录作为根目录。

仓库 Settings → Pages → Build and deployment → Source 选择 **GitHub Actions**。推送 main 分支后，随项目提供的工作流会生成 `dist` 并部署。首次设置后可在 Actions 手动运行 Deploy Constellation。

所有站内资源采用相对路径，兼容 GitHub Pages 仓库子路径。

GitHub 官方部署说明：https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

日常更新：本地编辑器保存 → GitHub Desktop 查看修改并提交 → Push origin → Actions 自动发布。不需要把任何 GitHub 密钥放进网站。

## 内容与双语

- 10 门课程，5 条研究主轴，另设“我的随笔”。
- 中文课程从你提供的原始资料导入；原文件另保存在 `content/source.md` 供核对，不进入发布产物。
- 英文课程是从原材料整理的技术主题纲要摘要，**不是完整逐段译文**，正文中有明确说明。可在本地编辑器逐步扩充。
- 开篇随笔是一篇明确标注的可替换示例。
- 原始材料中论文年份、前沿成果与引用未逐项核查，保留为个人学习规划，不应视为已验证的学术参考文献。

## 文件结构

- `content/catalog.json`：目录、文章元数据、发布状态与顺序。
- `content/文章ID.zh.md` / `文章ID.en.md`：两种语言的 Markdown 正文。
- `index.html` / `style.css` / `app.js`：网站源码、原创矢量风景和浏览器交互。
- `admin.html` / `admin.js` / `editor.py`：本地双语编辑器。
- `build.py`：零第三方 Python 依赖的静态构建。
- `.github/workflows/pages.yml`：GitHub Pages 自动部署。
- `dist/`：生成的公开站点，排除编辑器、草稿及原始资料备份。

## 构建与依赖

运行 `python build.py`。本地服务为 Python 标准库，不需要 npm、数据库或云端后台。

Markdown 使用 marked 15.0.12，经 DOMPurify 3.2.6 过滤；公式使用 MathJax 3.2.2。它们目前从 jsDelivr CDN 加载，字体从 Google Fonts 加载，因此完整排版与公式预览需要联网。字体不可用时使用本地字体；Markdown 库不可用时以安全的原始文本显示。后续可将这些依赖下载到仓库改为自托管，获得更好的离线体验。

网站采用响应式布局并尊重减少动画偏好，但本次环境的浏览器不能访问本地预览服务，尚未完成桌面和手机的视觉与交互实测。已通过 Python 构建、JavaScript 语法检查与发布内容一致性检查。上线前请在本机浏览器确认页面、语言切换、保存及公式预览。

## 设计方向

以温柔的青蓝天空、暖白色光、云海、浮岛与小小旅人为首页意象。原创 SVG 与 CSS 绘制，未使用《光·遇》游戏素材。阅读区域使用低饱和纸白、细线和留白。
