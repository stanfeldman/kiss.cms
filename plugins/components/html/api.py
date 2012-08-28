from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.views.templates import Template
from kiss.models import session
from models import HtmlPage
from kiss.core.application import Application
import re
from core.extensions import ComponentInterface, ApiInterface
import pyplug
from core.models.content import Plugin, PageBlock


class HtmlPageAdminApi(pyplug.Plugin):
	implements = [ApiInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
	
	def post(self, request):
		context = {}
		page = HtmlPage(plugin=Plugin.get_by(name=u"HtmlPageComponent"), title=request.form["title"], url=request.form["url"], template="htmlpagecomponent/user/" + request.form["template"])
		session.commit()
		return Response(ComponentInterface.plugin(u"HtmlPageComponent", fullname=False, ignorecase=True).html(page))
		
	def delete(self, request):
		context = {}
		page = HtmlPage.get_by(id=request.params["page"])
		page.delete()
		session.commit()
		return Response("ok")



