from kiss.models import Entity, Field, Unicode, Integer, OneToOne, OneToMany, ManyToOne, using_options, session
from core.models.security import SecureResource


class Plugin(SecureResource):
	using_options(inheritance="multi")
	name = Field(Unicode, primary_key=True)
	contents = OneToMany("Content")

class Content(Entity):
	using_options(inheritance="multi")
	plugin = ManyToOne("Plugin")
	template = Field(Unicode)


class Page(Content):
	using_options(inheritance="multi")
	title = Field(Unicode)
	name = Field(Unicode, unique=True)
	page_blocks = OneToMany("PageBlock")


class PageBlock(Content):
	using_options(inheritance="multi")
	placeholder = Field(Unicode)
	page = ManyToOne("Page")
	
	

