from core.models import Page, PageBlock
from kiss.models import Entity, Field, Unicode, using_options, OneToMany, ManyToOne


class MenuBlock(PageBlock):
	using_options(inheritance="multi")
	title = Field(Unicode)
	menu_items = OneToMany("MenuItem")
	def __repr__(self):
		return '<MenuBlock "%s" in %s>' % (self.title, self.placeholder)
		

class MenuItem(Entity):
	title = Field(Unicode)
	menu = ManyToOne("MenuBlock")
	page = ManyToOne("Page")
	parent = ManyToOne("MenuItem", inverse="children")
	children = OneToMany("MenuItem", inverse="parent")
	def __repr__(self):
		return '<MenuItem "%s">' % self.title
