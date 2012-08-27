from pyplug import Plugin
from core.extensions import ModuleInterface
from kiss.views.templates import Template

class MenuBlockModule(Plugin):
	implements = [ModuleInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return _("menu block").decode('utf-8')
		
	def content(self, block):
		return Template.text_by_path(block.template, {"menu": block})
		
	def admin(self, page, placeholder):
		return "menu admin"


