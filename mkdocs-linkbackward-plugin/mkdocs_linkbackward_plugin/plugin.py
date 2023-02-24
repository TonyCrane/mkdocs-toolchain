import os
import re
import logging

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files
from mkdocs.utils.meta import get_data

from typing import Any, Dict, Optional, Tuple

logger = logging.getLogger("mkdocs.mkdocs_linkbackward_plugin")

class LinkBackwardPlugin(BasePlugin):
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('wait_time', config_options.Type(int, default=5)),
        ('redirections', config_options.Type(list, default=[])),
    )

    def on_config(self, config: config_options.Config, **kwargs) -> Dict[str, Any]:
        if not self.config.get('enabled'):
            return config
        
        config['theme'].static_templates.add('redirection.html')
        
        self.redirs = []
        for each in self.config.get('redirections'):
            src, dst = each.split(' -> ')
            if not src.startswith('/'):
                src = '/' + src[1:] 
            if not dst.startswith('/'):
                dst = '/' + dst[1:]
            if src.endswith('/'):
                src += 'index.html'
            if dst.endswith('/'):
                dst += 'index.html'
            if not src.endswith('.htm') and not src.endswith('.html'):
                src += '/index.html'
            if not dst.endswith('.htm') and not dst.endswith('.html'):
                dst += '/index.html'
            self.redirs.append((src, dst))
            logger.debug(f"Redirect: `{src}` -> `{dst}`")

        return config

    def on_post_build(self, config: Dict[str, Any], **kwargs) -> None:
        site_dir = config["site_dir"]
        template_file_path = os.path.join(site_dir, 'redirection.html')
        with open(template_file_path, 'r', encoding='utf-8') as f:
            template = f.read()
        for src, dst in self.redirs:
            if os.path.exists(os.path.join(site_dir, src[1:])):
                logger.warning(f"Skip creating redirection file `{src}` because it already exists")
                continue
            if not os.path.exists(os.path.join(site_dir, dst[1:])):
                logger.warning(f"Skip creating redirection file `{src}` because the dest `{dst}` does not exist")
                continue
            logger.debug(f"Creating redirection file `{src}` -> `{dst}`")
            src_file = re.sub(
                r'\./',
                '../' * src.count('/'),
                template,
            )
            src_file = re.sub(
                r'//old//',
                src.replace('index.html', ''),
                src_file,
            )
            src_file = re.sub(
                r'//new//',
                dst.replace('index.html', ''),
                src_file,
            )
            src_file = re.sub(
                r'//wait_time//',
                str(self.config.get('wait_time')),
                src_file,
            )
            if self.config.get('wait_time') == 0:
                src_file = re.sub(
                    "<script>",
                    f"<script>window.location='{dst.replace('index.html', '')}';",
                    src_file
                )
            os.makedirs(os.path.dirname(os.path.join(site_dir, src[1:])), exist_ok=True)
            with open(os.path.join(site_dir, src[1:]), 'w', encoding='utf-8') as f:
                f.write(src_file)