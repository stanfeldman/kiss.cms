from pyplug import Interface
	

class PluginInterface(Interface):
	def urls(self):
		pass
	def static_path(self):
		"""
		returns pair (url_path, folder_path)
		"""
		pass
		
		
class PagePluginInterface(PluginInterface):
	def page(self, url):
		pass
		
	def admin(self):
		pass


class PageBlockPluginInterface(PluginInterface):
	def content(self, page, placeholder):
		pass
		
	def admin(self, page, placeholder):
		pass
		
		
class AdminPagePluginInterface(PluginInterface):
	def page(self):
		pass
