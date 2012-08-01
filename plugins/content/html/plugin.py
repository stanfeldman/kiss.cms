from pyplug import Plugin
from core.extensions import ContentPluginInterface
from models import HtmlContent

class HtmlContentPlugin(Plugin):
	name = "HTML content plugin"
	implements = [ContentPluginInterface]
	
	def __init__(self):
		HtmlContent.create_table(fail_silently=True)
		print "HtmlContentPlugin loaded"
		
	def content(self, placeholder):
		result = None
		try:
			t = HtmlContent.get(placeholder=placeholder)
			result = t.body
		except:
			pass
		return result
