from kiss.controllers.core import Controller
from kiss.views.core import Response


class AdminPageController(Controller):	
	def post(self, request):
		return Response("response: %s" % request.form["message"])
