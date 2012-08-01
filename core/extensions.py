from pyplug import Interface
		

class ContentPluginInterface(Interface):
	def render(self, placeholder):
		pass
		
		
class PagePluginInterface(Interface):
	def render(self, url):
		pass
