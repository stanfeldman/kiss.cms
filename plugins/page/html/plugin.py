from pyplug import Plugin
from core.extensions import PagePluginInterface
from models import HtmlPage
from kiss.views.templates import TemplateResponse

class HtmlPagePlugin(Plugin):
	name = "HTML page plugin"
	implements = [PagePluginInterface]
	
	def __init__(self):
		HtmlPage.create_table(fail_silently=True)
		print "HtmlPagePlugin loaded"
		
	def page(self, url):
		result = None
		try:
			page = HtmlPage.get(url=url)
			result = TemplateResponse(page.template)
		except:
			pass
		return result
		
	def admin(self):
		return "admin ui for HtmlPagePlugin"
