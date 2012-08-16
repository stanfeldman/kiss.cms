from pyplug import Plugin
from core.extensions import PageBlockPluginInterface
from models import VideoBlock
from kiss.views.templates import Template
from admin import UpdateVideoBlockController, ShowVideoBlockController

class VideoBlockPlugin(Plugin):
	implements = [PageBlockPluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__
		
	def urls(self):
		return {
			"admin/block/video/edit": UpdateVideoBlockController
		}
		
	def content(self, page, placeholder):
		result = None
		try:
			video = VideoBlock.get_by(page=page, placeholder=placeholder)
			result = Template.text_by_path("videoblockplugin/user/%s.html" % video.source, {"video": video})
		except:
			pass
		return result
		
	def admin(self, page, placeholder):
		return ShowVideoBlockController().show(page, placeholder)


