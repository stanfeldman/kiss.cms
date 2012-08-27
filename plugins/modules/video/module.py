from pyplug import Plugin
from core.extensions import ModuleInterface
from models import VideoBlock
from kiss.views.templates import Template
from jinja2 import Environment, FileSystemLoader
import os


class VideoBlockModule(Plugin):
	implements = [ModuleInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return _("video block").decode('utf-8')
		
	def content(self, block):
		template = "videoblockmodule/user/youtube.html"
		if hasattr(block, "template") and block.template:
			template = block.template
		return Template.text_by_path(template, {"video_block": block})
		
	def admin(self, page, placeholder):
		return self.edit(page, placeholder)
		
	def edit(self, page, placeholder):
		context = {}
		context["page"] = page.id
		context["placeholder"] = placeholder
		templates = []
		template_names = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates/user"))).list_templates(extensions=["html"])
		for tn in template_names:
			templates.append((tn, "videoblockmodule/user/"+tn))
		context["templates"] = templates
		try:
			video = PageBlock.get_by(page=page, placeholder=placeholder)
			if video and not isinstance(video, VideoBlock):
				return None
			context["link"] = video.link
			context["template"] = video.template
		except:
			pass
		return Template.text_by_path("videoblockmodule/admin/main.html", context)


