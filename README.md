# mkdocs-toolchain

> My personal mkdocs toolchain, only for personal use.

我个人使用的 mkdocs 工具链，仅供个人使用、学习参考。

## 原创插件
自己写着玩的，可能有 bug，不过欢迎使用！

- [TonyCrane/mkdocs-changelog-plugin](https://github.com/TonyCrane/mkdocs-changelog-plugin)
- [TonyCrane/mkdocs-heti-plugin](https://github.com/TonyCrane/mkdocs-heti-plugin)
- [TonyCrane/mkdocs-statistics-plugin](https://github.com/TonyCrane/mkdocs-statistics-plugin)

其他额外功能见 [TonyCrane/note](https://github.com/TonyCrane/note) 中的 `hooks/` 文件夹。

## 各包原始 commit sha

- mkdocs: [`1.6.1`](https://github.com/mkdocs/mkdocs/tree/1.6.1) ~~(old: [`730da08`](https://github.com/mkdocs/mkdocs/tree/730da08158b05374c4230f9785dd7f5068801fe3) -> [`3e0949a`](https://github.com/mkdocs/mkdocs/commit/3e0949a332ee2d4e3b0256869a9c448b03ea944d))~~
- mkdocs-encryptcontent-plugin: [`c28e4ce359cc3e69e097db8eba3fb77ab683b40d`](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin/tree/c28e4ce359cc3e69e097db8eba3fb77ab683b40d)
- mkdocs-rss-plugin: [`1.17.3`](https://github.com/Guts/mkdocs-rss-plugin/tree/1.17.3) ~~(old: [`07975d6`](https://github.com/Guts/mkdocs-rss-plugin/tree/07975d6f4c27759d3bc7845427ac05fe49afd9c1) -> [`89e9cfa`](https://github.com/Guts/mkdocs-rss-plugin/commit/89e9cfa8262e9b40f571d554a75a2e9929264efc))~~
- mkdocs-git-revision-date-localized-plugin: [`v1.4.7`](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/tree/v1.4.7)

其他依赖见 [TonyCrane/note](https://github.com/TonyCrane/note) 中的 `requirements.txt`。

## 各包做的修改
### mkdocs

- 更新了 logger，使用 RichHandler 美化（[`e541b1e`](https://github.com/TonyCrane/mkdocs-toolchain/commit/e541b1efd1f5e60d7018833e0ae8f2bdc0deb436)）
- 为文档构建的三个过程（渲染、构建、拷贝静态文件）增加进度条（[`e541b1e`](https://github.com/TonyCrane/mkdocs-toolchain/commit/e541b1efd1f5e60d7018833e0ae8f2bdc0deb436)）
- serve 模式下不监控 .DS_Store 文件（[`e541b1e`](https://github.com/TonyCrane/mkdocs-toolchain/commit/e541b1efd1f5e60d7018833e0ae8f2bdc0deb436)）
- 为 gh-deploy 增加 --skip-build 选项，用于跳过构建过程（[`e541b1e`](https://github.com/TonyCrane/mkdocs-toolchain/commit/e541b1efd1f5e60d7018833e0ae8f2bdc0deb436)）

### mkdocs-encryptcontent-plugin
- 将一些 info 级别的无关紧要 log 降低为 debug 级别（[`751ff15`](https://github.com/TonyCrane/mkdocs-toolchain/commit/751ff15bfa549141b518059b260802c082b4a6f1)）
- 从加密页面中获取 summary、placeholder、encryption_info_message，而不是全部使用全局（[`59211cd`](https://github.com/TonyCrane/mkdocs-toolchain/commit/59211cd433a9f4c88bf7e21a9c62c5e96a10d754)）

### mkdocs-rss-plugin
- 规范地使用 logger（[`841e240`](https://github.com/TonyCrane/mkdocs-toolchain/commit/841e24029fe2edc7fdb753ee2defb1eef31e0e17)）
