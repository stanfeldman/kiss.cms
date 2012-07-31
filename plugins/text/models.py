from core.models import Content
from kiss.models import TextField


class Text(Content):
	body = TextField()
