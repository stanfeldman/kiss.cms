from core.models import Content
from kiss.models import Entity, Field, Unicode, Integer, OneToOne, OneToMany, ManyToOne, using_options, session
		
		
# patches
Content.created = ManyToOne("User", inverse="created_contents")
Content.updated = ManyToOne("User", inverse="updated_contents")
Content.privileges = ManyToOne("Privilege")
			

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
