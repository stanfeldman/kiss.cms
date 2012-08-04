from os import path
current_dir = path.dirname(path.abspath(__file__))
import sys
sys.path.append(path.join(current_dir, "../kiss.py"))
sys.path.append(path.join(current_dir, "../compressinja/"))
sys.path.append(path.join(current_dir, "../putils/"))
sys.path.append(path.join(current_dir, "../pyplug/"))
sys.path.append(path.join(current_dir, "../pev/"))
from kiss.core.application import Application
from kiss.core.events import ApplicationStarted
from kiss.core.exceptions import InternalServerError
from core.controllers import PageController, AdminController


options = {
	"application": {
		"address": "127.0.0.1",
		"port": 8080
	},
	"views": {
		"templates_path": ["templates", "plugins"],
		"templates_extensions": ["core.templates.Placeholder"],
		"static_path": "static"
	},
	"events": {
		ApplicationStarted: PageController.on_application_started
	},
	"models": {
		"connection": "sqlite:///kms_site.sqldb"
	}
}

