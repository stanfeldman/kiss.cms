from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from core.models.content import Page, PageBlock, Plugin
from kiss.core.application import Application
from kiss.views.templates import Template
from models import VideoBlock
from jinja2 import Environment, FileSystemLoader
import os
import pyplug
from core.extensions import ApiInterface


class VideoBlockAdminApi(pyplug.Plugin):
	implements = [ApiInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
			
	def post(self, request):
		page = Page.get_by(id=request.form["page"])
		vbp = Plugin.get_by(name=u"VideoBlockPlugin")
		video = VideoBlock.get_or_create(plugin=vbp, placeholder=request.form["placeholder"], page=page)
		video.link = request.form["link"]
		video.template=request.form["template"]
		session.commit()
		return Response(vbp.edit(page, video.placeholder))

