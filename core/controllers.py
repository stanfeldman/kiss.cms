from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from plugins.content.html.models import HtmlContent
from plugins.page.html.models import HtmlPage
from core.extensions import PagePluginInterface

	
class CoreController(Controller):	
	def get(self, request):
		return PagePluginInterface.render(request.params["url"])
		
	#on load handler via eventer
	def application_after_load(self, application):
		project_dir = os.path.dirname(os.path.abspath(__file__))
		plugin_dir = os.path.join(project_dir, "../plugins")
		PluginLoader.load(project_dir, plugin_dir)
		p = HtmlPage.get_or_create(title="test page", url="tp", template="site_template.html")
		HtmlContent.get_or_create(placeholder="content", body="<h1>test content from db</h1>", page=p)
		HtmlContent.get_or_create(placeholder="header", body="<h1>header from db</h1>", page=p)
		print "Application loaded"

