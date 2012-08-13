from core.models import Page
from kiss.models import Field, Unicode, using_options


class HtmlPage(Page):
	using_options(inheritance="multi")
	template = Field(Unicode)
