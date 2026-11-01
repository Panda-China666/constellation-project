import { QuartzComponent, QuartzComponentConstructor } from "./types"

export default (() => {
  const NotebookNav: QuartzComponent = ({ cfg, fileData, allFiles }) => {
    const zh = cfg.locale === "zh-CN"
    const base = "/constellation-project/"
    const lang = zh ? "zh" : "en"
    const other = zh ? "en" : "zh"
    const slug = fileData.slug === "index" ? "" : fileData.slug?.replace(/\/index$/, "/")
    const count = allFiles.filter(f => f.frontmatter?.note === true).length
    return <div class="notebook-nav">
      <div class="notebook-label">CONSTELLATION / NOTEBOOK</div>
      <nav aria-label={zh ? "网站导航" : "Site navigation"}>
        <a href={base}>{zh ? "首页" : "Home"}<span>↗</span></a>
        <a href={`${base}${lang}/courses/`}>{zh ? "课程区" : "Courses"}<span>↗</span></a>
        <a class="selected" href={`${base}${lang}/blog/`}>{zh ? "我的随笔" : "Field notes"}<span>{String(count).padStart(2, "0")}</span></a>
      </nav>
      <a class="language-link" href={`${base}${other}/blog/${slug}`}>{zh ? "English" : "简体中文"} ↗</a>
    </div>
  }
  return NotebookNav
}) satisfies QuartzComponentConstructor
