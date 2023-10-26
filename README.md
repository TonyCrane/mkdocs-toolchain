# mkdocs-toolchain

> My personal mkdocs toolchain, only for personal use.

我个人使用的 mkdocs 工具链，仅供个人使用、学习参考。

## 原创插件
自己写着玩的，可能有 bug，不过欢迎使用！

- [TonyCrane/mkdocs-changelog-plugin](https://github.com/TonyCrane/mkdocs-changelog-plugin)
- [TonyCrane/mkdocs-heti-plugin](https://github.com/TonyCrane/mkdocs-heti-plugin)
- [TonyCrane/mkdocs-statistics-plugin](https://github.com/TonyCrane/mkdocs-statistics-plugin)

未单独发布插件：

- mkdocs-linkbackward-plugin: 为了链接兼容性创建跳转页面
- mkdocs-tikzautomata-plugin: 在 markdown 中直接编写 tikz 并嵌入 svg，修改自 [FrightenedFoxCN/mkdocs-mathenv-plugin](https://github.com/FrightenedFoxCN/mkdocs-mathenv-plugin/)
- mkdocs-toc-plugin: 从页面内嵌 yml 生成 toc（带字数统计/更新时间）

## 各包原始 commit sha

- mkdocs: [`3e0949a332ee2d4e3b0256869a9c448b03ea944d`](https://github.com/mkdocs/mkdocs/commit/3e0949a332ee2d4e3b0256869a9c448b03ea944d) ~~(old: [`730da08158b05374c4230f9785dd7f5068801fe3`](https://github.com/mkdocs/mkdocs/tree/730da08158b05374c4230f9785dd7f5068801fe3))~~
- mkdocs-encryptcontent-plugin: [`c28e4ce359cc3e69e097db8eba3fb77ab683b40d`](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin/tree/c28e4ce359cc3e69e097db8eba3fb77ab683b40d)
- mkdocs-git-revision-date-localized-plugin: [`9cfce40942c83dd15834fb879caa4171a426ecdd`](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/tree/9cfce40942c83dd15834fb879caa4171a426ecdd)
- mkdocs-rss-plugin: [`89e9cfa8262e9b40f571d554a75a2e9929264efc`](https://github.com/Guts/mkdocs-rss-plugin/commit/89e9cfa8262e9b40f571d554a75a2e9929264efc) ~~(old: [`07975d6f4c27759d3bc7845427ac05fe49afd9c1`](https://github.com/Guts/mkdocs-rss-plugin/tree/07975d6f4c27759d3bc7845427ac05fe49afd9c1))~~
- mkdocs-material: 不在此 repo 中，直接使用 8.1.4 版本（mkdocs-material-extensions 1.1）
- mkdocs-glightbox: 不在此 repo 中，直接使用 0.3.4 版本

## 各包做的修改
### mkdocs

23.10.25 更新 mkdocs 后以下所有 patch 都在 [`2e21a9`](https://github.com/TonyCrane/mkdocs-toolchain/commit/2e21a9b26d2549104ce894b8c95611b53e3297ef) 中。

- 更新了 logger，使用 RichHandler 美化（[`324ef3`](https://github.com/TonyCrane/mkdocs-toolchain/commit/324ef3652d2a5df3fe1b769113236f4d72cd6e22)）
- ~~不警告 todo.md 文件没包含在 nav 中 ⚠️ 个人限定（[`324ef3`](https://github.com/TonyCrane/mkdocs-toolchain/commit/324ef3652d2a5df3fe1b769113236f4d72cd6e22)）~~（官方 `not_in_nav` 实现）
- ~~不要求对 html 文件的引用包含在文件树中 ⚠️ 个人限定（[`324ef3`](https://github.com/TonyCrane/mkdocs-toolchain/commit/324ef3652d2a5df3fe1b769113236f4d72cd6e22)）~~（官方 `validation` 可实现忽略）
- 为文档构建的三个过程（渲染、构建、拷贝静态文件）增加进度条（[`6c8c36`](https://github.com/TonyCrane/mkdocs-toolchain/commit/6c8c36302fdae95c621d8ffd0e3e6ef9581e58d6)）
- serve 模式下不监控 .DS_Store 文件（[`0cbebe`](https://github.com/TonyCrane/mkdocs-toolchain/commit/0cbebe95b5b7baff25c6c646bda7be63f790d2c4)）
- 为 gh-deploy 增加 --skip-build 选项，用于跳过构建过程（[`610185`](https://github.com/TonyCrane/mkdocs-toolchain/commit/6101855cf70270d44f0a0427055ccd8e9e36d4a4)）
- ~~serve 模式下监控主题 overrides 文件夹 ⚠️ 硬编码（[`47ba34`](https://github.com/TonyCrane/mkdocs-toolchain/commit/47ba3450ff7547999a78dae925217c614d8aa00f)）~~（官方 `--watch-theme` flag 实现）

### mkdocs-encryptcontent-plugin
- 将一些 info 级别的无关紧要 log 降低为 debug 级别（[`751ff1`](https://github.com/TonyCrane/mkdocs-toolchain/commit/751ff15bfa549141b518059b260802c082b4a6f1)）
- 从加密页面中获取 summary、placeholder、encryption_info_message，而不是全部使用全局（[`59211c`](https://github.com/TonyCrane/mkdocs-toolchain/commit/59211cd433a9f4c88bf7e21a9c62c5e96a10d754)）

### mkdocs-git-revision-date-localized-plugin
- 在 serve 模式下自动关闭插件，加速预览（[`d90259`](https://github.com/TonyCrane/mkdocs-toolchain/commit/d902594c21d40b617ab203a531e1bbb83fd676b7)）

### mkdocs-rss-plugin
- 在 serve 模式下自动关闭插件，加速预览（[`ef7f45`](https://github.com/TonyCrane/mkdocs-toolchain/commit/ef7f45953d3b5d50e1eff282dc2ad37be014aa97)）
- 规范地使用 logger（[`ef7f45`](https://github.com/TonyCrane/mkdocs-toolchain/commit/ef7f45953d3b5d50e1eff282dc2ad37be014aa97)）