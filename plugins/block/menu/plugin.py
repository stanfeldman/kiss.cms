from pyplug import Plugin
from core.extensions import PageBlockPluginInterface
from kiss.views.templates import Template

class MenuBlockPlugin(Plugin):
	implements = [PageBlockPluginInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def name(self):
		return _("Menu block").decode('utf-8')
		
	def content(self, block):
		return Template.text_by_path("menublockplugin/user/linear.html", {"menu": block})


