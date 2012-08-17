# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from admin import AddHtmlPageController, ShowHtmlPageController, DeleteHtmlPageController
from kiss.core.application import Application
from jinja2 import Environment, FileSystemLoader
import os
import re
from core.extensions import PageBlockPluginInterface
from core.models import PageBlock


class HtmlPagePlugin(Plugin):
	implements = [PagePluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def name(self):
		return "HTML %s" % _("page").decode('utf-8')
		
	def urls(self):
		return {
			"admin/page/html": {
				"": AddHtmlPageController,
				"(?P<page>\d+)": {
					"": ShowHtmlPageController,
					"delete": DeleteHtmlPageController
				}
			}
		}
		
	def page(self, url):
		result = None
		try:
			page = HtmlPage.get_by(url=url)
			result = TemplateResponse(page.template, {"page": page})
		except:
			pass
		return result
		
	def admin(self):
		pages = HtmlPage.query.all()
		if self.template_path:
			templates = Environment(loader=FileSystemLoader(os.path.join(self.template_path, "user"))).list_templates(extensions=["html"])
		for page in pages:
			tmpl = Application().templates_environment.loader.get_source(Application().templates_environment, page.template)
			placeholders = re.findall(r"""{{[ ]?placeholder[ ]?\([ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?\)[ ]?}}""", unicode(tmpl))
			page.blocks = []
			for placeholder in placeholders:
				exists = False
				if PageBlock.query.filter_by(page=page, placeholder=placeholder).count() > 0:
					for block_plugin in PageBlockPluginInterface.plugins.values():
						name = u"unknown plugin"
						if hasattr(block_plugin, "name"):
							name = block_plugin.name()
						if hasattr(block_plugin, "admin"):
							block_plugin_admin_page = block_plugin.admin(page, placeholder)
							if block_plugin_admin_page:
								page.blocks.append((placeholder, name, block_plugin_admin_page))
								exists = True
								break
				if not exists:
					page.blocks.append((placeholder, None, None))			
			block_plugins = list(PageBlockPluginInterface.plugins.iteritems())
		return Template.text_by_path("htmlpageplugin/admin/main.html", {"pages": pages, "templates": templates, "block_plugins": block_plugins})#.decode('utf-8')
