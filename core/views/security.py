from core.models.security import User


class SecurityMiddleware(object):
	def set_user(self, request):
		user = User.get_by(id=1)
		request.user = user
