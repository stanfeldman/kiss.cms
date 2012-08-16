from core.models import PageBlock
from kiss.models import Field, Unicode, using_options


class VideoBlock(PageBlock):
	using_options(inheritance="multi")
	link = Field(Unicode)
	source = Field(Unicode)
	
	def __repr__(self):
		return '<VideoBlock "%s": %s, %s>' % (self.placeholder, self.link, self.source)

