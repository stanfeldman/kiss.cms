from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from plugins.block.html.models import HtmlBlock
from plugins.page.html.models import HtmlPage
from core.extensions import PagePluginInterface, AdminPagePluginInterface, PageBlockPluginInterface
from kiss.models import setup_all, drop_all, create_all, session
from putils.dynamics import Introspector, Importer
from templates import placeholder

	
class PageController(Controller):	
	def get(self, request):
		return PagePluginInterface.page(request.params["url"])
		
	def on_before_init_server(self, application):
		#loading plugins
		for p in application.options["plugins"]["path"]:
			PluginLoader.load(p)
		application.templater.add_template_paths(application.options["plugins"]["path"])
		application.templates_environment.globals["placeholder"] = placeholder
		#adding urls
		application.router.add_urls({"": PageController})
		application.router.add_urls({"admin": AdminController})
		for i in [PagePluginInterface, AdminPagePluginInterface, PageBlockPluginInterface]:
			for urls in i.urls_get_all():
				if urls:
					application.router.add_urls(urls)
		application.router.add_urls({"(?P<url>.+)": PageController})
		#adding static paths
		for i in [PagePluginInterface, AdminPagePluginInterface, PageBlockPluginInterface]:
			for static in i.static_path_get_all():
				if static:
					application.add_static([static[1]], url_path=static[0])
		#adding translation paths
		for i in [PagePluginInterface, AdminPagePluginInterface, PageBlockPluginInterface]:
			for tr_path in i.translation_path_get_all():
				if tr_path:
					application.templater.add_translation_paths([tr_path])
		#creating db
		setup_all()
		drop_all()
		create_all()
		#sample data
		p = HtmlPage(title=u"test page", url=u"tp", template=u"site_template.html")
		HtmlBlock(placeholder=u"content", body=u"<h1>test content from db</h1>", page=p)
		HtmlBlock(placeholder=u"header", body=u"<h1>header from db</h1>", page=p)
		session.commit()
		print "Application loaded"


class AdminController(Controller):	
	def get(self, request):
		return AdminPagePluginInterface.page()

