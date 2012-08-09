from kms.core.models import Content
from kiss.models import Field, Unicode, using_options


class HtmlContent(Content):
	using_options(inheritance="multi")
	body = Field(Unicode)
	
	def __repr__(self):
		return '<HtmlContent "%s": %s>' % (self.placeholder, self.body)
