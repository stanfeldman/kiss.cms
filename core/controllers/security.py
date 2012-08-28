from core.models.security import User


class SecurityMiddleware(object):
	def set_user(self, request):
		if "user" in request.session:
			user = User.get_by(id=request.session["user"])
			request.user = user
		else:
			request.user = None

