from kiss.views.core import Response
from kiss.controllers.core import Controller
from core.extensions import PagePluginInterface, ContentPluginInterface, ApiPluginInterface
from core.models.content import Page, Plugin
from core.models.security import User
import inspect

	
class PageRouter(Controller):	
	def get(self, request):
		if "name" not in request.params or not request.params["name"]:
			return None
		page = Page.get_by(name=request.params["name"])
		if not page:
			return None
		print "admin", User.get_by(id=1).has_access(page)
		print "manager", User.get_by(id=2).has_access(page)
		print "simple user", User.get_by(id=3).has_access(page)
		content = PagePluginInterface.plugin(page.plugin.name, fullname=False, ignorecase=True).content(page)
		return content
		
class ApiRouter(Controller):	
	def process(self, request):
		if "plugin" not in request.params or not request.params["plugin"]:
			return None
		plugin_name = request.params["plugin"]
		plugin = ApiPluginInterface.plugin(plugin_name, fullname=False, ignorecase=True)
		pl_db = Plugin.get_by(name=u"addhtmlpage")
		print "admin", User.get_by(id=1).has_access(pl_db)
		print "manager", User.get_by(id=2).has_access(pl_db)
		print "simple user", User.get_by(id=3).has_access(pl_db)
		action = getattr(plugin, request.method.lower())
		return action(request)

		

