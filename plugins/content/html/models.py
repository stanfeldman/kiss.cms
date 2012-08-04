from core.models import Content
from kiss.models import Field, Unicode, using_options


class HtmlContent(Content):
	using_options(inheritance="multi")
	body = Field(Unicode)
