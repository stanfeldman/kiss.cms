from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from models import Page
from plugins.text.models import Text

	
class CoreController(Controller):	
	def get(self, request):
		try:
			page = Page.get(url=request.params["url"])
			return TemplateResponse(page.template)
		except:
			pass
		
	#on load handler via eventer
	def application_after_load(self, application):
		Page.create_table(fail_silently=True)
		project_dir = os.path.dirname(os.path.abspath(__file__))
		plugin_dir = os.path.join(project_dir, "../plugins")
		PluginLoader.load(project_dir, plugin_dir)
		p = Page.create(title="test page", url="tp", template="template1.html")
		Text.create(placeholder="content", body="<h1>test content from db</h1>", page=p)
		Text.create(placeholder="header", body="<h1>header from db</h1>", page=p)
		print "app loaded"
		
	def internal_server_error(self, request):
		return Response("<h1>error: %s</h1>" % request.description)
