from pyplug import Plugin
from core.extensions import PagePluginInterface, AdminPagePluginInterface
from kiss.views.templates import TemplateResponse
import os

class AdminPagePlugin(Plugin):
	implements = [AdminPagePluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def static_path(self):
		current_dir = os.path.dirname(os.path.abspath(__file__))
		return ("/admin_page_plugin", os.path.join(current_dir, "static"))
		
	def page(self):
		plugins = []
		for pl in PagePluginInterface.admin_get_all():
			if pl:
				plugins.append(pl)
		return TemplateResponse("page/admin/templates/admin.html", {"plugins": plugins})

