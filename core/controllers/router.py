from kiss.views.core import Response
from kiss.controllers.core import Controller
from core.extensions import PagePluginInterface
from core.models.content import Page
from core.models.security import User

	
class RouterController(Controller):	
	def get(self, request):
		if "url" not in request.params:
			request.params["url"] = ""
		page = Page.get_by(url=request.params["url"])
		if page:
			print User.get_by(id=1).has_permission(page.plugin, "read")
			content = PagePluginInterface.plugins()[page.plugin.name].content(page)
			return Response(content)
		return None

