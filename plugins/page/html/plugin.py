# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from admin import AddHtmlPageController, ShowHtmlPageController, DeleteHtmlPageController
from kiss.core.application import Application
from jinja2 import Environment, FileSystemLoader
import os


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
		print self.template_path
		context = {}
		context["pages"] = HtmlPage.query.all()
		if self.template_path:
			temp_env = Environment(loader=FileSystemLoader(os.path.join(self.template_path, "user")))
		context["templates"] = temp_env.list_templates(extensions=["html"])
		return Template.text_by_path("htmlpageplugin/admin/main.html", context)
