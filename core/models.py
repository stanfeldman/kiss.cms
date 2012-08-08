from kiss.models import Entity, Field, Unicode, OneToMany, ManyToOne, using_options, session

class ExtendedEntity(Entity):
	@classmethod
	def get_or_create(cls, **kwargs):
		instance = session.query(cls).filter_by(**kwargs).first()
		if instance:
			return instance
		else:
			instance = cls(**kwargs)
			return instance
Entity = ExtendedEntity #monkey patch =)


class Page(Entity):
	using_options(inheritance="multi")
	title = Field(Unicode)
	url = Field(Unicode)
	contents = OneToMany("Content")


class Content(Entity):
	using_options(inheritance="multi")
	placeholder = Field(Unicode)
	page = ManyToOne("Page")
