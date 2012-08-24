from kiss.views.core import Response
from kiss.controllers.core import Controller
from core.extensions import PagePluginInterface, ContentPluginInterface
from core.models.content import Page
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
	def get(self, request):
		controller = self.get_controller(request)
		return controller.get(request)
		
	def post(self, request):
		controller = self.get_controller(request)
		return controller.post(request)
		
	def put(self, request):
		controller = self.get_controller(request)
		return controller.put(request)
		
	def delete(self, request):
		controller = self.get_controller(request)
		return controller.delete(request)
		
	def get_controller(self, request):
		if "plugin" not in request.params or not request.params["plugin"] or "controller" not in request.params or not request.params["controller"]:
			return None
		plugin_name = request.params["plugin"]
		controller_name = request.params["controller"]
		plugin = ContentPluginInterface.plugin(plugin_name, fullname=False, ignorecase=True)
		api = plugin.api()
		if not controller_name in api:
			return None
		controller = api[controller_name]
		if inspect.isclass(controller):
			controller = controller()
		return controller
		

