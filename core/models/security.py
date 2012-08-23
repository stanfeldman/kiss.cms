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
	def has_permission(self, resource, privilege_name):
		privilege = Privilege.get_by(name=privilege_name)
		permission_count = Permission.query.filter_by(privilege=privilege, resource=resource, user_group=self.user_group).count()
		return permission_count > 0
	
	
class UserGroup(Entity):
	name = Field(Unicode)
	permissions = OneToMany("Permission")
	users = OneToMany("User")


class Resource(Entity):
	using_options(inheritance="multi")
	permissions = OneToMany("Permission")
	

class Privilege(Entity):
	name = Field(Unicode, primary_key=True) #read, write, approve, etc
	permissions = OneToMany("Permission")
	
	
class Permission(Entity):
	resource = ManyToOne("Resource")
	privilege = ManyToOne("Privilege")
	user_group = ManyToOne("UserGroup")

