from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from admin import AddHtmlPageController, ShowHtmlPageController, DeleteHtmlPageController
from kiss.core.application import Application
from jinja2 import Environment, PackageLoader, ChoiceLoader


class HtmlPagePlugin(Plugin):
	implements = [PagePluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def urls(self):
		return {
			"admin/page/html": {
				"": AddHtmlPageController,
				"(?P<page>\d+)": {
					"": ShowHtmlPageController,
					"delete": DeleteHtmlPageController
				}
			}
		}
		
	def page(self, url):
		result = None
		try:
			page = HtmlPage.get_by(url=url)
			result = TemplateResponse(page.template, {"page": page})
		except:
			pass
		return result
		
	def admin(self):
		context = {}
		context["pages"] = HtmlPage.query.all()
		#temp_env = Application().options["views"]["templates_environment"]
		tps = []
		if isinstance(Application().options["views"]["templates_path"], list):
			for tp in Application().options["views"]["templates_path"]:
				tps.append(PackageLoader(tp, ""))
		else:
			tps.append(PackageLoader(Application().options["views"]["templates_path"], ""))
		temp_env = Environment(loader=ChoiceLoader(tps))
		context["templates"] = temp_env.list_templates(extensions=["html"])
		return Template.text_by_path("page/html/templates/admin.html", context)
