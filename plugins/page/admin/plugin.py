from pyplug import Plugin
from core.extensions import PagePluginInterface, ContentPluginInterface, AdminPagePluginInterface
from kiss.views.templates import TemplateResponse

class AdminPagePlugin(Plugin):
	name = "Admin page plugin"
	implements = [AdminPagePluginInterface]
	
	def __init__(self):
		print "AdminPagePlugin loaded"
		
	def page(self):
		plugins = []
		for pl in PagePluginInterface.admin_get_all():
			if pl:
				plugins.append(pl)
		for pl in ContentPluginInterface.admin_get_all():
			if pl:
				plugins.append(pl)
		return TemplateResponse("page/admin/admin_template.html", {"plugins": plugins})

