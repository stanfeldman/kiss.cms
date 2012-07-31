from pyplug import Plugin
from core.interfaces import PluginInterface
from models import Text

class TextPlugin(Plugin):
	name = "Text plugin"
	version = "0.0.1"
	author = "Stanislav Feldman"
	description = "page plugin"
	implements = [PluginInterface]
	
	def __init__(self):
		Text.create_table(fail_silently=True)
		
	def render(self, placeholder):
		result = None
		try:
			t = Text.get(placeholder=placeholder)
			result = t.body
		except:
			pass
		return result
