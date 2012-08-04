from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.models import session
from models import HtmlPage


class AdminPageController(Controller):	
	def post(self, request):
		page = HtmlPage(title=request.form["title"], url=request.form["url"], template=request.form["template"])
		session.commit()
		return TemplateResponse("page/html/templates/page.html", {"page": page})
