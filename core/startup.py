from kiss.core.application import Application
from controllers.loader import Loader
from putils.types import Dict
from views.security import SecurityMiddleware


core_options = {
	"events": {
		"BeforeInitServer": Loader.on_before_init_server,
		"BeforeControllerAction": SecurityMiddleware.set_user
	}
}

def start(options):
	opts = Dict.merge(core_options, options)
	app = Application(options)
	app.start()

