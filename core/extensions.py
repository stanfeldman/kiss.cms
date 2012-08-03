from pyplug import Interface
	

class PluginInterface(Interface):
	def urls(self):
		pass
		
	def admin(self):
		pass
			

class ContentPluginInterface(PluginInterface):
	def content(self, placeholder):
		pass
		
		
class PagePluginInterface(PluginInterface):
	def page(self, url):
		pass
		
		
class AdminPagePluginInterface(PluginInterface):
	def page(self):
		pass
