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
		for pl in PagePluginInterface.plugins.values():
			plugins.append((pl.name(), pl.admin()))
		return TemplateResponse("adminpageplugin/admin.html", {"plugins": plugins})

