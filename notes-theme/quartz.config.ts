import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const zh = process.env.NOTES_LANG !== "en"
const config: QuartzConfig = {
  configuration: {
    pageTitle: zh ? "我的随笔" : "Field notes",
    pageTitleSuffix: zh ? " · 群星计划" : " · Constellation",
    enableSPA: false,
    enablePopovers: true,
    analytics: null,
    locale: zh ? "zh-CN" : "en-US",
    baseUrl: `panda-china666.github.io/constellation-project/${zh ? "zh" : "en"}/blog`,
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "local",
      cdnCaching: false,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#f8f6f0",
          lightgray: "#e4dfd4",
          gray: "#a8a297",
          darkgray: "#514e46",
          dark: "#292c28",
          secondary: "#496453",
          tertiary: "#899d85",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#20221f",
          lightgray: "#393c35",
          gray: "#85897f",
          darkgray: "#d2d1c9",
          dark: "#f0eee5",
          secondary: "#a7c09e",
          tertiary: "#899d85",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "mathjax" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time

    ],
  },
}

export default config
