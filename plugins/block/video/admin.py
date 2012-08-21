from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from core.models import Page, PageBlock
from kiss.core.application import Application
from kiss.views.templates import Template
from models import VideoBlock
from jinja2 import Environment, FileSystemLoader
import os


class UpdateVideoBlockController(Controller):	
	def post(self, request):
		page = Page.get_by(id=request.form["page"])
		video = VideoBlock.get_or_create(plugin=u"VideoBlockPlugin", placeholder=request.form["placeholder"], page=page)
		video.link = request.form["link"]
		video.template=request.form["template"]
		session.commit()
		return Response(ShowVideoBlockController().show(page, video.placeholder))
		
		
class ShowVideoBlockController(Controller):
	def show(self, page, placeholder):
		context = {}
		context["page"] = page.id
		context["placeholder"] = placeholder
		templates = []
		template_names = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates/user"))).list_templates(extensions=["html"])
		for tn in template_names:
			templates.append((tn, "videoblockplugin/user/"+tn))
		context["templates"] = templates
		try:
			video = PageBlock.get_by(page=page, placeholder=placeholder)
			if video and not isinstance(video, VideoBlock):
				return None
			context["link"] = video.link
			context["template"] = video.template
		except:
			pass
		return Template.text_by_path("videoblockplugin/admin/main.html", context)
