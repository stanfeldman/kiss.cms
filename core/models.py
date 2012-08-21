from kiss.models import Entity, Field, Unicode, Integer, OneToOne, OneToMany, ManyToOne, using_options, session


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


class Content(Entity):
	using_options(inheritance="multi")
	plugin = Field(Unicode, nullable=False)
	template = Field(Unicode)


class Page(Content):
	using_options(inheritance="multi")
	title = Field(Unicode)
	url = Field(Unicode, unique=True)
	page_blocks = OneToMany("PageBlock")


class PageBlock(Content):
	using_options(inheritance="multi")
	placeholder = Field(Unicode)
	page = ManyToOne("Page")
	
	

