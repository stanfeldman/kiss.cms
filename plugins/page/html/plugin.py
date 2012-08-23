# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from admin import AddHtmlPageController, HtmlPageController, DeleteHtmlPageController
from kiss.core.application import Application
from jinja2 import Environment, FileSystemLoader
import os
import re
from core.extensions import PageBlockPluginInterface


class HtmlPagePlugin(Plugin):
	implements = [PagePluginInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return "HTML %s" % _("page").decode('utf-8')
		
	def urls(self):
		return {
			"admin/page/html": {
				"": AddHtmlPageController,
				"(?P<page>\d+)": {
					"": HtmlPageController,
					"delete": DeleteHtmlPageController
				}
			}
		}
		
	def content(self, page):
		return Template.text_by_path(page.template, {"page": page})
		
	def admin(self):
		pages = HtmlPage.query.all()
		if self.template_path:
			templates = Environment(loader=FileSystemLoader(os.path.join(self.template_path, "user"))).list_templates(extensions=["html"])
		page_htmls = []
		for page in pages:
			page_html = HtmlPageController().html(page)
			page_htmls.append(page_html)
		return Template.text_by_path("htmlpageplugin/admin/main.html", {"pages": page_htmls, "templates": templates})
