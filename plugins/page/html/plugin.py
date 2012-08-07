from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from controllers import AddHtmlPageController
from kiss.core.application import Application


class HtmlPagePlugin(Plugin):
	name = "HTML page plugin"
	implements = [PagePluginInterface]
	
	def __init__(self):
		print "HtmlPagePlugin loaded"
		
	def urls(self):
		return {"admin/page": AddHtmlPageController}
		
	def page(self, url):
		result = None
		try:
			page = HtmlPage.get_by(url=url)
			result = TemplateResponse(page.template)
		except:
			pass
		return result
		
	def admin(self):
		context = {}
		context["pages"] = HtmlPage.query.all()
		temp_env = Application().options["views"]["templates_environment"]
		context["templates"] = temp_env.list_templates(extensions=["html"])
		return Template.text_by_path("page/html/templates/admin.html", context)
