from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from models import HtmlPage
from kiss.core.application import Application
import re
from core.extensions import PageBlockPluginInterface


class AddHtmlPageController(Controller):	
	def post(self, request):
		context = {}
		context["page"] = HtmlPage(title=request.form["title"], url=request.form["url"], template=request.form["template"])
		session.commit()
		return TemplateResponse("htmlpageplugin/small_page.html", context)
		
		
class ShowHtmlPageController(Controller):
	def get(self, request):
		context = {}
		context["page"] = HtmlPage.get_by(id=request.params["page"])
		temp_env = Application().templates_environment
		tmpl = temp_env.loader.get_source(temp_env, context["page"].template)
		context["placeholders"] = re.findall(r"""{{[ ]?placeholder[ ]?\([ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?\)[ ]?}}""", unicode(tmpl))
		context["plugins"] = PageBlockPluginInterface.plugins
		return TemplateResponse("htmlpageplugin/big_page.html", context)
		

class DeleteHtmlPageController(Controller):
	def get(self, request):
		context = {}
		page = HtmlPage.get_by(id=request.params["page"])
		page.delete()
		session.commit()
		return Response("ok")

