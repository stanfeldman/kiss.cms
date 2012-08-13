from kiss.core.application import Application
from kiss.core.events import ApplicationStarted
from controllers import PageController
from putils.types import Dict


core_options = {
	"views": {
		"templates_extensions": ["core.templates.Placeholder"]
	},
	"events": {
		ApplicationStarted: PageController.on_application_started
	}
}

def start(options):
	opts = Dict.merge(core_options, options)
	app = Application(options)
	app.start()

