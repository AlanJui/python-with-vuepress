module.exports = {
  title: "Manjaro KDE 開發環境建置指引",
  description: "如何在 Manjaro KDE 電腦建置開發環境",
  base: "/python-with-vuepress/",
  themeConfig: {
    nav: [
      { text: "專案文件", link: "/" },
      { text: "作業流程", link: "/D01/" },
      { text: "應用工具", link: "/D02/" },
      { text: "專業知識", link: "/D03/" },
      { text: "教育訓練", link: "/D04/" },
    ],
    sidebar: ["/", "/D01/", "/D02/", "/D03/", "/D04/"],
  },
  markdown: {
    lineNumbers: true,
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@uml": "./diagrams/out",
        "@picts": "./.vuepress/public/assets/img",
      },
    },
  },
};
