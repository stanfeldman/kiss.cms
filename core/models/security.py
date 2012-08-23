from kiss.models import Entity, Field, Unicode, Integer, OneToOne, OneToMany, ManyToOne, using_options, session
		
		
# patches
#Content.created = ManyToOne("User", inverse="created_contents")
#Content.updated = ManyToOne("User", inverse="updated_contents")
			

class User(Entity):
	name = Field(Unicode)
	#email = Field(Unicode)
	#password = Field(Unicode)
	#created_contents = OneToMany("Content", inverse="created")
	#updated_contents = OneToMany("Content", inverse="updated")
	user_group = ManyToOne("UserGroup")
	def has_permission(self, permission, resource):
		permission_count = Permission.query.filter_by(name=permission, resource=resource, user_group=self.user_group).count()
		return permission_count > 0
	
	
class UserGroup(Entity):
	name = Field(Unicode)
	permissions = OneToMany("Permission")
	users = OneToMany("User")


class SecureResource(Entity):
	"""
	Secure resource, this is can be content or module
	"""
	using_options(inheritance="multi")
	permissions = OneToMany("Permission")
	
	
class Permission(Entity):
	name = Field(Unicode) #read, write, approve, etc
	resource = ManyToOne("SecureResource")
	user_group = ManyToOne("UserGroup")

