from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from core.models import Page, PageBlock
from kiss.core.application import Application
from kiss.views.templates import Template
from models import HtmlBlock


class UpdateHtmlBlockController(Controller):	
	def post(self, request):
		page = Page.get_by(id=request.form["page"])
		print request.form
		content = HtmlBlock.get_or_create(plugin=u"HtmlBlockPlugin", placeholder=request.form["placeholder"], page=page)
		content.body = request.form["body"]
		session.commit()
		return Response(ShowHtmlBlockController().show(page, content.placeholder))
		
		
class ShowHtmlBlockController(Controller):
	def show(self, page, placeholder):
		context = {}
		context["page"] = page.id
		context["placeholder"] = placeholder
		try:
			block = PageBlock.get_by(page=page, placeholder=placeholder)
			if block and not isinstance(block, HtmlBlock):
				return None
			context["body"] = block.body
		except:
			pass
		return Template.text_by_path("htmlblockplugin/admin/default.html", context)
