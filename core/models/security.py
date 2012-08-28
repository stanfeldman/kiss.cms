from kiss.models import Entity, Field, Unicode, Boolean, Integer, OneToOne, OneToMany, ManyToOne, using_options, session
		
		
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
	def __repr__(self):
		return '<User name: %s>' % self.name
	def has_access(self, resource, permission=None):
		#you can access by default
		if Permission.query.filter_by(resource=resource).count() == 0:
			return True
		#there are some permissions, but we are not in any group
		if not self.user_group:
			return False
		return self.user_group.has_access(resource, permission)
		
	
	
class UserGroup(Entity):
	name = Field(Unicode)
	permissions = OneToMany("Permission")
	users = OneToMany("User")
	parent = ManyToOne("UserGroup")
	children = OneToMany("UserGroup")
	def has_access(self, resource, permission=None):
		permissions = Permission.query.filter_by(name=permission, resource=resource, user_group=self).all()
		if len(permissions) == 0:
			if self.parent:
				#try parents
				return self.parent.has_access(resource, permission)
			else:
				#no permissions
				return False
		else:
			for perm in permissions:
				#maybe some of them is restriction?
				if perm.is_restriction:
					return False
			else:
				#ok, we have permissions
				return True


class SecureResource(Entity):
	"""
	Secure resource, this is can be content or module
	"""
	using_options(inheritance="multi")
	permissions = OneToMany("Permission")
	
	
class Permission(Entity):
	name = Field(Unicode) #read, write, approve, etc; can be none
	resource = ManyToOne("SecureResource")
	user_group = ManyToOne("UserGroup")
	is_restriction = Field(Boolean, default=False)

