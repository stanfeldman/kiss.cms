from kiss.models import Model, CharField, TextField, ForeignKeyField


class Page(Model):
	title = CharField()
	url = CharField()


class Content(Model):
	placeholder = CharField(unique=True)
	page = ForeignKeyField(Page)
