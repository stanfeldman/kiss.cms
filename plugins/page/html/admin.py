from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.views.templates import Template
from kiss.models import session
from models import HtmlPage
from kiss.core.application import Application
import re
from core.extensions import PageBlockPluginInterface
from core.models import PageBlock


class AddHtmlPageController(Controller):	
	def post(self, request):
		context = {}
		page = HtmlPage(plugin=u"HtmlPagePlugin", title=request.form["title"], url=request.form["url"], template="htmlpageplugin/user/" + request.form["template"])
		session.commit()
		return Response(HtmlPageController().html(page))
		
		
class HtmlPageController(object):
	def html(self, page):
		tmpl = Application().templates_environment.loader.get_source(Application().templates_environment, page.template)
		placeholders = re.findall(r"""{{[ ]?placeholder[ ]?\([ ]?"(?P<placeholder>[a-zA-Z0-9]+)"[ ]?\)[ ]?}}""", unicode(tmpl))
		page.blocks = []
		for placeholder in placeholders:
			exists = False
			if PageBlock.query.filter_by(page=page, placeholder=placeholder).count() > 0:
				for block_plugin in PageBlockPluginInterface.plugins().values():
					title = u"unknown plugin"
					if hasattr(block_plugin, "title"):
						title = block_plugin.title()
					if hasattr(block_plugin, "admin"):
						block_plugin_admin_page = block_plugin.admin(page, placeholder)
						if block_plugin_admin_page:
							page.blocks.append((placeholder, title, block_plugin_admin_page))
							exists = True
							break
			if not exists:
				page.blocks.append((placeholder, None, None))			
		block_plugins = []
		for bp_name, bp_code in PageBlockPluginInterface.plugins().iteritems():
			block_plugins.append((bp_name, bp_code.title(), bp_code))
		return Template.text_by_path("htmlpageplugin/admin/page.html", {"page": page, "block_plugins": block_plugins})
		

class DeleteHtmlPageController(Controller):
	def get(self, request):
		context = {}
		page = HtmlPage.get_by(id=request.params["page"])
		page.delete()
		session.commit()
		return Response("ok")

