from core.models.content import PageBlock
from kiss.models import Field, Unicode, using_options


class HtmlBlock(PageBlock):
	using_options(inheritance="multi")
	body = Field(Unicode)
	
	def __repr__(self):
		return '<HtmlBlock "%s": %s>' % (self.placeholder, self.body)
