from pyplug import Plugin
from core.extensions import ContentPluginInterface
from models import HtmlContent
from kiss.views.templates import Template
from admin import UpdateHtmlContentController, ShowHtmlContentController

class HtmlContentPlugin(Plugin):
	name = "HTML content plugin"
	implements = [ContentPluginInterface]
	
	def __init__(self):
		print "HtmlContentPlugin loaded"
		
	def urls(self):
		return {
			"admin/content/html": UpdateHtmlContentController
		}
		
	def content(self, placeholder):
		result = None
		try:
			t = HtmlContent.get_by(placeholder=placeholder)
			result = t.body
		except:
			pass
		return result
		
	def admin(self, page, placeholder):
		return ShowHtmlContentController().show(page, placeholder)

