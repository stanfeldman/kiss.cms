from pyplug import Plugin
from core.extensions import PagePluginInterface
from core.models import Page
from kiss.models import session
from kiss.views.templates import Template
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class AdminPagePlugin(Plugin):
	implements = [PagePluginInterface]
	
	def load(self):
		Page(plugin=self.__class__.__name__, title=u"Admin page", url=u"admin")
		session.commit()
		print "%s loaded" % self.__class__.__name__
		
	def content(self, page):
		plugins = []
		for pl_name, pl_code in PagePluginInterface.plugins().iteritems():
			if pl_name != self.__class__.__name__:
				pl_title = "Unknown plugin"
				if hasattr(pl_code, "name"):
					pl_title = pl_code.name()
				if hasattr(pl_code, "admin"):
					plugins.append((pl_name, pl_title, pl_code.admin()))
		return Template.text_by_path("adminpageplugin/admin.html", {"plugins": plugins})

