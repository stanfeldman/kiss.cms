from pyplug import Plugin
from core.extensions import PagePluginInterface, AdminPagePluginInterface
from kiss.views.templates import TemplateResponse
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class AdminPagePlugin(Plugin):
	implements = [AdminPagePluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def page(self):
		plugins = []
		for pl_name, pl_code in PagePluginInterface.plugins.iteritems():
			plugins.append((pl_name, pl_code.name(), pl_code.admin()))
		return TemplateResponse("adminpageplugin/admin.html", {"plugins": plugins})

