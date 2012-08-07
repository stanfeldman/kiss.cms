from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.models import session
from models import HtmlPage
from kiss.core.application import Application
import re


class AddHtmlPageController(Controller):	
	def post(self, request):
		context = {}
		context["page"] = HtmlPage(title=request.form["title"], url=request.form["url"], template=request.form["template"])
		session.commit()
		temp_env = Application().options["views"]["templates_environment"]
		tmpl = temp_env.loader.get_source(temp_env, context["page"].template)
		context["placeholders"] = re.findall(r"""{%[ ]?placeholder[ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?%}""", unicode(tmpl))
		return TemplateResponse("page/html/templates/page.html", context)
