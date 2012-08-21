from pyplug import Plugin
from core.extensions import PageBlockPluginInterface
from models import VideoBlock
from kiss.views.templates import Template
from admin import UpdateVideoBlockController, ShowVideoBlockController

class VideoBlockPlugin(Plugin):
	implements = [PageBlockPluginInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def name(self):
		return _("video block").decode('utf-8')
		
	def urls(self):
		return {
			"admin/block/video/edit": UpdateVideoBlockController
		}
		
	def content(self, block):
		template = "videoblockplugin/user/youtube.html"
		if hasattr(block, "template") and block.template:
			template = block.template
		return Template.text_by_path(template, {"video_block": block})
		
	def admin(self, page, placeholder):
		return ShowVideoBlockController().show(page, placeholder)


