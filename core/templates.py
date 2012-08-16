from jinja2.ext import contextfunction
from jinja2 import Markup
from core.extensions import PageBlockPluginInterface
			
@contextfunction
def placeholder(context, placeholder):
	page = context["page"]
	for content in PageBlockPluginInterface.content_get_all(page, placeholder):
		if content:
			return Markup(content)
	return Markup("")

