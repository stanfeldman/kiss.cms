from pyplug import Plugin
from core.extensions import PageBlockPluginInterface
from models import HtmlBlock
from kiss.views.templates import Template
from admin import UpdateHtmlBlockController, ShowHtmlBlockController

class HtmlBlockPlugin(Plugin):
	implements = [PageBlockPluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def urls(self):
		return {
			"admin/content/html": UpdateHtmlBlockController
		}
		
	def content(self, page, placeholder):
		result = None
		try:
			t = HtmlBlock.get_by(page=page, placeholder=placeholder)
			result = t.body
		except:
			pass
		return result
		
	def admin(self, page, placeholder):
		return ShowHtmlBlockController().show(page, placeholder)

