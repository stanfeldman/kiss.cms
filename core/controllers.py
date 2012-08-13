from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from plugins.content.html.models import HtmlContent
from plugins.page.html.models import HtmlPage
from core.extensions import PagePluginInterface, AdminPagePluginInterface, ContentPluginInterface
from kiss.models import setup_all, drop_all, create_all, session
from putils.dynamics import Introspector, Importer
from jinja2 import PackageLoader
from templates import placeholder

	
class PageController(Controller):	
	def get(self, request):
		return PagePluginInterface.page(request.params["url"])
		
	def on_application_started(self, application):
		#loading plugins
		for p in application.options["plugins"]["path"]:
			PluginLoader.load(p)
		application.router.add_template_paths(application.options["plugins"]["path"])
		application.options["views"]["templates_environment"].globals["placeholder"] = placeholder
		#adding urls
		application.router.add_urls({"": PageController})
		application.router.add_urls({"admin": AdminController})
		for urls in PagePluginInterface.urls_get_all():
			if urls:
				application.router.add_urls(urls)
		for urls in ContentPluginInterface.urls_get_all():
			if urls:
				application.router.add_urls(urls)
		application.router.add_urls({"(?P<url>.+)": PageController})
		#creating db
		setup_all()
		drop_all()
		create_all()
		#sample data
		p = HtmlPage(title=u"test page", url=u"tp", template=u"site_template.html")
		HtmlContent(placeholder=u"content", body=u"<h1>test content from db</h1>", page=p)
		HtmlContent(placeholder=u"header", body=u"<h1>header from db</h1>", page=p)
		session.commit()
		print "Application loaded"


class AdminController(Controller):	
	def get(self, request):
		return AdminPagePluginInterface.page()

