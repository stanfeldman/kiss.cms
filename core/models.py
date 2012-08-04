from kiss.models import Entity, Field, Unicode, OneToMany, ManyToOne, using_options


class Page(Entity):
	using_options(inheritance="multi")
	title = Field(Unicode)
	url = Field(Unicode)
	contents = OneToMany("Content")


class Content(Entity):
	using_options(inheritance="multi")
	placeholder = Field(Unicode)
	page = ManyToOne("Page")
