from pyplug import Interface
from kiss.controllers.core import Controller
import pyplug
	

class PluginInterface(Interface):
	"""
	Plugin structure:
	plugin_root_dir
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


class ApiInterface(PluginInterface, Controller):
	pass
			
		
class ContentInterface(PluginInterface):
	def content(self, obj):
		pass

		
class ComponentInterface(ContentInterface):
	def admin(self):
		pass


class ModuleInterface(ContentInterface):	
	def admin(self, page, placeholder):
		pass

