from kiss.controllers.core import Controller
from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.models import session
from core.models import Page
from kiss.core.application import Application
from kiss.views.templates import Template
from models import HtmlContent


class UpdateHtmlContentController(Controller):	
	def post(self, request):
		page = Page.get_by(id=request.form["page"])
		content = HtmlContent.get_or_create(placeholder=request.form["placeholder"], page=page)
		content.body = request.form["body"]
		session.commit()
		return Response(ShowHtmlContentController().show(page, content.placeholder))
		
		
class ShowHtmlContentController(Controller):
	def show(self, page, placeholder):
		context = {}
		context["page"] = page.id
		context["placeholder"] = placeholder
		try:
			context["body"] = HtmlContent.get_by(page=page, placeholder=placeholder).body
		except:
			pass
		return Template.text_by_path("content/html/templates/admin.html", context)
