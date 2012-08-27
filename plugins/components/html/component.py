# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import ComponentInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from kiss.core.application import Application
from jinja2 import Environment, FileSystemLoader
import os
import re
from core.extensions import ModuleInterface
from kiss.core.application import Application
from core.models.content import PageBlock


class HtmlPageComponent(Plugin):
	implements = [ComponentInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return "HTML %s" % _("page").decode('utf-8')
		
	def content(self, page):
		return TemplateResponse(page.template, {"page": page})
		
	def admin(self):
		pages = HtmlPage.query.all()
		if self.template_path:
			templates = Environment(loader=FileSystemLoader(os.path.join(self.template_path, "user"))).list_templates(extensions=["html"])
		page_htmls = []
		for page in pages:
			page_html = self.html(page)
			page_htmls.append(page_html)
		return Template.text_by_path("htmlpagecomponent/admin/main.html", {"pages": page_htmls, "templates": templates})
		
	def html(self, page):
		tmpl = Application().templates_environment.loader.get_source(Application().templates_environment, page.template)
		placeholders = re.findall(r"""{{[ ]?placeholder[ ]?\([ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?\)[ ]?}}""", unicode(tmpl))
		page.blocks = []
		for placeholder in placeholders:
			exists = False
			if PageBlock.query.filter_by(page=page, placeholder=placeholder).count() > 0:
				for block_plugin in ModuleInterface.plugins():
					title = u"unknown plugin"
					if hasattr(block_plugin, "title"):
						title = block_plugin.title()
					if hasattr(block_plugin, "admin"):
						block_plugin_admin_page = block_plugin.admin(page, placeholder)
						if block_plugin_admin_page:
							page.blocks.append((placeholder, title, block_plugin_admin_page))
							exists = True
							break
			if not exists:
				page.blocks.append((placeholder, None, None))			
		block_plugins = []
		for bp_name, bp_code in ModuleInterface.plugins_and_names(fullname=False, lowercase=True):
			block_plugins.append((bp_name, bp_code.title(), bp_code))
		return Template.text_by_path("htmlpagecomponent/admin/page.html", {"page": page, "block_plugins": block_plugins})

