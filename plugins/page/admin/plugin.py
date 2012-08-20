from pyplug import Plugin
from core.extensions import PagePluginInterface
from core.models import Page
from kiss.models import session
from kiss.views.templates import TemplateResponse
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
		for pl_name, pl_code in PagePluginInterface.plugins.iteritems():
			if pl_name != self.__class__.__name__:
				plugins.append((pl_name, pl_code.name(), pl_code.admin()))
		return TemplateResponse("adminpageplugin/admin.html", {"plugins": plugins})

