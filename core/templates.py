from jinja2.ext import contextfunction
from jinja2 import Markup
from core.extensions import PageBlockPluginInterface
			
@contextfunction
def placeholder(context, placeholder):
	page = context["page"]
	content = PageBlockPluginInterface.content(page, placeholder)
	if content:
		return Markup(content)
	else:
		return Markup("")

