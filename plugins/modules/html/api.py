from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from core.models.content import Page, PageBlock, Plugin
from kiss.core.application import Application
from kiss.views.templates import Template
from models import HtmlBlock
import pyplug
from core.extensions import ApiInterface


class HtmlBlockAdminApi(pyplug.Plugin):
	implements = [ApiInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def post(self, request):
		page = Page.get_by(id=request.form["page"])
		print request.form
		hbm = Plugin.get_by(name=u"HtmlBlockModule")
		content = HtmlBlock.get_or_create(plugin=hbm, placeholder=request.form["placeholder"], page=page)
		content.body = request.form["body"]
		session.commit()
		return Response(hbm.show(page, content.placeholder))

