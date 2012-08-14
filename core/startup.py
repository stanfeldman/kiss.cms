from kiss.core.application import Application
from kiss.core.events import BeforeInitServer
from controllers import PageController
from putils.types import Dict


core_options = {
	"events": {
		BeforeInitServer: PageController.on_before_init_server
	}
}

def start(options):
	opts = Dict.merge(core_options, options)
	app = Application(options)
	app.start()

