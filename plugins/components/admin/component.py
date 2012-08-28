from pyplug import Plugin
from core.extensions import ComponentInterface
from kiss.models import session
from kiss.views.templates import Template, TemplateResponse
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class AdminPageComponent(Plugin):
	implements = [ComponentInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def content(self, page):
		plugins = []
		for pl_name, pl_code in ComponentInterface.plugins_and_names(fullname=False, lowercase=True):
			if pl_name != self.__class__.__name__:
				pl_title = "Unknown plugin"
				if hasattr(pl_code, "title"):
					pl_title = pl_code.title()
				if hasattr(pl_code, "admin"):
					plugins.append((pl_name, pl_title, pl_code.admin()))
		return Template.text_by_path(page.template, {"plugins": plugins})

