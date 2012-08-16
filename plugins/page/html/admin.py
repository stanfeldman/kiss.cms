from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from models import HtmlPage
from kiss.core.application import Application
import re
from core.extensions import PageBlockPluginInterface
from core.models import PageBlock


class AddHtmlPageController(Controller):	
	def post(self, request):
		context = {}
		context["page"] = HtmlPage(title=request.form["title"], url=request.form["url"], template="htmlpageplugin/user/" + request.form["template"])
		session.commit()
		return TemplateResponse("htmlpageplugin/admin/small_page.html", context)
		
		
class ShowHtmlPageController(Controller):
	def get(self, request):
		page = HtmlPage.get_by(id=request.params["page"])
		temp_env = Application().templates_environment
		tmpl = temp_env.loader.get_source(temp_env, page.template)
		placeholders = re.findall(r"""{{[ ]?placeholder[ ]?\([ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?\)[ ]?}}""", unicode(tmpl))
		blocks = []
		for placeholder in placeholders:
			exists = False
			if PageBlock.query.filter_by(page=page, placeholder=placeholder).count() > 0:
				for block_plugin in PageBlockPluginInterface.plugins.values():
					name = "unknown plugin"
					if hasattr(block_plugin, "name"):
						name = block_plugin.name()
					if hasattr(block_plugin, "admin"):
						block_plugin_admin_page = block_plugin.admin(page, placeholder)
						if block_plugin_admin_page:
							blocks.append((placeholder, name, block_plugin_admin_page))
							exists = True
							break
			if not exists:
				blocks.append((placeholder, None))			
		block_plugins = PageBlockPluginInterface.plugins.keys()
		return TemplateResponse("htmlpageplugin/admin/big_page.html", {"page": page, "block_plugins": block_plugins, "blocks": blocks})
		

class DeleteHtmlPageController(Controller):
	def get(self, request):
		context = {}
		page = HtmlPage.get_by(id=request.params["page"])
		page.delete()
		session.commit()
		return Response("ok")

