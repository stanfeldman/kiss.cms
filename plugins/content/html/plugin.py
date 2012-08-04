from pyplug import Plugin
from core.extensions import ContentPluginInterface
from models import HtmlContent

class HtmlContentPlugin(Plugin):
	name = "HTML content plugin"
	implements = [ContentPluginInterface]
	
	def __init__(self):
		print "HtmlContentPlugin loaded"
		
	def content(self, placeholder):
		result = None
		try:
			t = HtmlContent.get_by(placeholder=placeholder)
			result = t.body
		except:
			pass
		return result

