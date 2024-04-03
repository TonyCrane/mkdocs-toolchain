import os
import re

import yaml
from jinja2 import Template
from rich import print

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.utils import copy_file

from typing import Any, Dict

from .utils import get_statistics, get_update_time

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(PLUGIN_DIR, "templates/toc.html")

with open(TEMPLATE_DIR, "r", encoding="utf-8") as file:
    TEMPLATE = file.read()

class TocPlugin(BasePlugin):
    config_scheme = (
        ("enabled", config_options.Type(bool, default=True)),
        ("ignore_commits", config_options.Type(list, default=[])),
    )

    enabled = True

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        if not self.enabled:
            return config
        
        if not self.config.get("enabled"):
            return config
        
        config["extra_css"] = ["css/toc_extra.css"] + config["extra_css"]
    
    def on_page_markdown(
        self, markdown: str, page: Page, config: config_options.Config, files, **kwargs
    ) -> str:
        if not self.enabled:
            return markdown
        
        if not self.config.get("enabled"):
            return markdown
        
        if "{{ BEGIN_TOC }}" not in markdown or "{{ END_TOC }}" not in markdown:
            return markdown

        toc_yml = markdown.split("{{ BEGIN_TOC }}")[1].split("{{ END_TOC }}")[0]
        toc = yaml.load(toc_yml, Loader=yaml.FullLoader)
        toc_items = self._get_toc_items(toc, os.path.dirname(page.file.abs_src_path))

        toc_html = Template(TEMPLATE).render(items=toc_items)
        markdown = re.sub(
            r"\{\{ BEGIN_TOC \}\}.*\{\{ END_TOC \}\}",
            toc_html,
            markdown,
            flags=re.IGNORECASE | re.DOTALL,
        )

        return markdown

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        if not self.enabled:
            return
        
        if not self.config.get("enabled"):
            return
        
        files = ["css/toc_extra.css"]
        for file in files:
            dest_file_path = os.path.join(config["site_dir"], file)
            src_file_path = os.path.join(PLUGIN_DIR, file)
            assert os.path.exists(src_file_path)
            copy_file(src_file_path, dest_file_path)
    
    def _get_toc_items(self, toc: dict, base: str) -> list:
        ret = []
        for i, part in enumerate(toc):
            item = dict()
            item['n'] = i
            title = list(part.keys())[0]
            if "[note]" in title:
                item['note'] = True
                title = title.replace("[note]", "")
            else:
                item['note'] = False
            item['title'] = title
            details = []
            for d in part[list(part.keys())[0]]:
                key = list(d.keys())[0]
                value = d[key]
                if key == "index":
                    item['link'] = value
                    continue
                detail = dict()
                t = key
                detail['note'] = False
                detail['lab'] = False
                if "[note]" in t:
                    detail['note'] = True
                    t = t.replace("[note]", "")
                if "[lab]" in t:
                    detail['lab'] = True
                    t = t.replace("[lab]", "")
                detail['title'] = t
                detail['link'] = value
                detail['words'], detail['codes'], detail['read_time'] = get_statistics(value, base)
                detail['update_time'] = get_update_time(value, base, self.config.get("ignore_commits", []))
                if "🔒" in t:
                    detail['lock'] = True
                details.append(detail)
            details.sort(key=lambda x: x['update_time'], reverse=True)
            item['contents'] = details
            ret.append(item)
        return ret
