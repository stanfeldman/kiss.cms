from kiss.models import Model, CharField, TextField, ForeignKeyField


class Page(Model):
	title = CharField()
	url = CharField()
	template = CharField()


class Content(Model):
	placeholder = CharField()
	page = ForeignKeyField(Page)
