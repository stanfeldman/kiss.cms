from pyplug import Plugin
from core.extensions import PageBlockPluginInterface
from models import HtmlBlock
from kiss.views.templates import Template
from admin import UpdateHtmlBlockController, ShowHtmlBlockController

class HtmlBlockPlugin(Plugin):
	implements = [PageBlockPluginInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def name(self):
		return _("HTML block").decode('utf-8')
		
	def urls(self):
		return {
			"admin/content/html": UpdateHtmlBlockController
		}
		
	def content(self, block):
		return block.body
		
	def admin(self, page, placeholder):
		return ShowHtmlBlockController().show(page, placeholder)

