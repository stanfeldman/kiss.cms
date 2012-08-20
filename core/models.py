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
	created = ManyToOne("User", inverse="created_contents")
	updated = ManyToOne("User", inverse="updated_contents")
	privileges = ManyToOne("Privilege")


class Page(Content):
	using_options(inheritance="multi")
	title = Field(Unicode)
	url = Field(Unicode, unique=True)
	page_blocks = OneToMany("PageBlock")


class PageBlock(Content):
	using_options(inheritance="multi")
	placeholder = Field(Unicode)
	page = ManyToOne("Page")
	
	
class User(Entity):
	name = Field(Unicode)
	email = Field(Unicode)
	password = Field(Unicode)
	created_contents = OneToMany("Content", inverse="created")
	updated_contents = OneToMany("Content", inverse="updated")
	role = ManyToOne("UserRole")
	
	
class UserRole(Entity):
	"""
	Set of privileges
	"""
	users = OneToMany("User")
	privileges = ManyToOne("Privilege")
	
	
class PrivilegeType(object):
	Read = 0
	Write = 1


class Privilege(Entity):
	type = Field(Integer) #PrivelegeType
	role = OneToMany("UserRole")
	content = OneToMany("Content")
