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
	def title(self):
		pass
	def load(self):
		pass
	def unload(self):
		pass
		
		
class ContentPluginInterface(PluginInterface):
	def content(self, obj):
		pass
	def urls(self):
		pass
		
		
class PagePluginInterface(ContentPluginInterface):
	def admin(self):
		pass


class PageBlockPluginInterface(ContentPluginInterface):	
	def admin(self, page, placeholder):
		pass

