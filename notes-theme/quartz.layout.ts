import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import NotebookNav from "./quartz/components/NotebookNav"
const zh = process.env.NOTES_LANG !== "en"
const isNote = (page: any) => page.fileData.frontmatter?.note === true
const left = [
  Component.PageTitle(), Component.MobileOnly(Component.Spacer()),
  Component.Flex({ components: [
    { Component: Component.Search(), grow: true },
    { Component: Component.Darkmode() }, { Component: Component.ReaderMode() },
  ] }),
  NotebookNav(),
  Component.Explorer({ title: zh ? "笔记目录" : "Notebook", folderDefaultState: "open" }),
]
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(), header: [], afterBody: [],
  footer: Component.Footer({ links: { "群星计划 · Constellation": "/constellation-project/" } }),
}
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({ component: Component.Breadcrumbs({ rootName: zh ? "笔记本" : "Notebook" }), condition: isNote }),
    Component.ArticleTitle(),
    Component.ConditionalRender({ component: Component.ContentMeta(), condition: isNote }),
    Component.TagList(),
  ],
  left,
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    Component.ConditionalRender({ component: Component.Backlinks(), condition: isNote }),
    Component.RecentNotes({ title: zh ? "最近的记录" : "Recent notes", limit: 5, filter: f => f.frontmatter?.note === true }),
  ],
}
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs({ rootName: zh ? "笔记本" : "Notebook" }), Component.ArticleTitle()],
  left, right: [],
}
