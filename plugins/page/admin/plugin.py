from pyplug import Plugin
from core.extensions import AdminPagePluginInterface
from kiss.views.templates import TemplateResponse

class AdminPagePlugin(Plugin):
	name = "Admin page plugin"
	implements = [AdminPagePluginInterface]
	
	def __init__(self):
		print "AdminPagePlugin loaded"
		
	def page(self):
		return TemplateResponse("admin_template.html")

