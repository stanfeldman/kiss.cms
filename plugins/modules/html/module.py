from pyplug import Plugin
from core.extensions import ModuleInterface
from models import HtmlBlock
from kiss.views.templates import Template
from core.models.content import PageBlock

class HtmlBlockModule(Plugin):
	implements = [ModuleInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return _("HTML block").decode('utf-8')
		
	def content(self, block):
		return block.body
		
	def admin(self, page, placeholder):
		return self.edit(page, placeholder)
		
	def edit(self, page, placeholder):
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
		return Template.text_by_path("htmlblockmodule/admin/default.html", context)

