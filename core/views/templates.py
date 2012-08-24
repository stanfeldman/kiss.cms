from jinja2.ext import contextfunction
from jinja2 import Markup
from core.extensions import PageBlockPluginInterface
from core.models.content import PageBlock
			
@contextfunction
def placeholder(context, placeholder):
	page = context["page"]
	block = PageBlock.get_by(page=page, placeholder=placeholder)
	if block:
		cnt = PageBlockPluginInterface.plugin(block.plugin.name, fullname=False, ignorecase=True).content(block)
		return Markup(cnt)
	return Markup("")

