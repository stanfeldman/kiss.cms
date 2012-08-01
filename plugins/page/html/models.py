from core.models import Page
from kiss.models import CharField


class HtmlPage(Page):
	template = CharField()
