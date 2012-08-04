from core.models import Page
from kiss.models import Field, Unicode


class HtmlPage(Page):
	template = Field(Unicode)
