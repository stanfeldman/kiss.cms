from core.models import Content
from kiss.models import TextField


class HtmlContent(Content):
	body = TextField()
