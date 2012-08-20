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
	def content(self, obj):
		pass
	def urls(self):
		pass
	def load(self):
		pass
	def unload(self):
		pass
		
		
class PagePluginInterface(PluginInterface):
	def admin(self):
		pass


class PageBlockPluginInterface(PluginInterface):	
	def admin(self, page, placeholder):
		pass

