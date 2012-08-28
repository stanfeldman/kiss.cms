from kiss.views.core import RedirectResponse
from core.extensions import ApiInterface
import pyplug


class SecurityLoginApi(pyplug.Plugin):
	implements = [ApiInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
	
	def post(self, request):
		return RedirectResponse("/")




