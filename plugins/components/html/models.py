from core.models.content import Page
from kiss.models import Field, Unicode, using_options


class HtmlPage(Page):
	using_options(inheritance="multi")

