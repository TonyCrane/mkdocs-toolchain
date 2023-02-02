# mkdocs-toolchain

My personal mkdocs toolchain, only for personal use.

## Original commit sha

- mkdocs: [`730da08158b05374c4230f9785dd7f5068801fe3`](https://github.com/mkdocs/mkdocs/tree/730da08158b05374c4230f9785dd7f5068801fe3)
- mkdocs-encryptcontent-plugin: [`c28e4ce359cc3e69e097db8eba3fb77ab683b40d`](https://github.com/CoinK0in/mkdocs-encryptcontent-plugin/tree/c28e4ce359cc3e69e097db8eba3fb77ab683b40d)
- mkdocs-git-revision-date-localized-plugin: [`9cfce40942c83dd15834fb879caa4171a426ecdd`](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin/tree/9cfce40942c83dd15834fb879caa4171a426ecdd)
- mkdocs-rss-plugin: [`07975d6f4c27759d3bc7845427ac05fe49afd9c1`](https://github.com/Guts/mkdocs-rss-plugin/tree/07975d6f4c27759d3bc7845427ac05fe49afd9c1)
- mkdocs-material: just using version 8.1.4
- mkdocs-glightbox: just using version 0.3.1

## Changes

- mkdocs
    - update logger
    - exclude some particular files from logger info
- mkdocs-encryptcontent-plugin
    - turn some `log.info` into `log.debug`
- mkdocs-git-revision-date-localized-plugin
    - disable plugin when build from `serve` to speed up preview
- mkdocs-rss-plugin
    - disable plugin when build from `serve` to speed up preview