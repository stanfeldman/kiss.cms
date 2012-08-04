from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse, Template
from controllers import AdminPageController


class HtmlPagePlugin(Plugin):
	name = "HTML page plugin"
	implements = [PagePluginInterface]
	
	def __init__(self):
		print "HtmlPagePlugin loaded"
		
	def urls(self):
		return {"admin/page": AdminPageController}
		
	def page(self, url):
		result = None
		try:
			page = HtmlPage.get_by(url=url)
			result = TemplateResponse(page.template)
		except:
			pass
		return result
		
	def admin(self):
		return Template.text_by_path("page/html/admin_template.html")
