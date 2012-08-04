from core.models import Content
from kiss.models import Field, Unicode


class HtmlContent(Content):
	body = Field(Unicode)
