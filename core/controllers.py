from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from plugins.content.html.models import HtmlContent
from plugins.page.html.models import HtmlPage
from core.extensions import PagePluginInterface, AdminPagePluginInterface
from kiss.models import Model
from putils.dynamics import Introspector

	
class PageController(Controller):	
	def get(self, request):
		return PagePluginInterface.page(request.params["url"])
		
	def on_application_started(self, application):
		project_dir = os.path.dirname(os.path.abspath(__file__))
		plugin_dir = os.path.join(project_dir, "../plugins")
		PluginLoader.load(project_dir, plugin_dir)
		application.router.add_urls({"": PageController})
		application.router.add_urls({"admin": AdminController})
		application.router.add_urls({"admin": AdminController})
		for urls in PagePluginInterface.urls_get_all():
			if urls:
				application.router.add_urls(urls)
		application.router.add_urls({"(?P<url>.+)": PageController})
		p = HtmlPage.get_or_create(title="test page", url="tp", template="site_template.html")
		HtmlContent.get_or_create(placeholder="content", body="<h1>test content from db</h1>", page=p)
		HtmlContent.get_or_create(placeholder="header", body="<h1>header from db</h1>", page=p)
		print "Application loaded"


class AdminController(Controller):	
	def get(self, request):
		return AdminPagePluginInterface.page()

