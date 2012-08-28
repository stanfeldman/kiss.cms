from kiss.views.core import Response
from kiss.controllers.core import Controller
from core.extensions import ComponentInterface, ApiInterface
from core.models.content import Page, Plugin
from core.models.security import User
import inspect

	
class PageRouter(Controller):	
	def get(self, request):
		if "url" not in request.params or not request.params["url"]:
			request.params["url"] = ""
		page = Page.get_by(url=request.params["url"])
		if not page:
			return None
		print request.user, request.user.has_access(page)
		content = ComponentInterface.plugin(page.plugin.name, fullname=False, ignorecase=True).content(page)
		return content
		
class ApiRouter(Controller):	
	def process(self, request):
		if "plugin" not in request.params or not request.params["plugin"]:
			return None
		plugin_name = request.params["plugin"]
		plugin = ApiInterface.plugin(plugin_name, fullname=False, ignorecase=True)
		print request.user, request.user.has_access(plugin.db_instance)
		action = getattr(plugin, request.method.lower())
		return action(request)

		

