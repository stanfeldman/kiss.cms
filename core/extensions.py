from pyplug import Interface
	

class PluginInterface(Interface):
	"""
	Plugin structure:
	plugin_root_dir
		plugin.py(module with plugin class definition)
		static
		templates
		lang		
	"""
	def name(self):
		pass
	def urls(self):
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
