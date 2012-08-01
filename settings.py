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
from kiss.models import SqliteDatabase
from core.controllers import PageController, AdminController


options = {
	"application": {
		"address": "127.0.0.1",
		"port": 8080
	},
	"urls": {
		"": PageController,
		"admin": AdminController,
		"(?P<url>.+)": PageController
	},
	"views": {
		"templates_path": "templates",
		"templates_extensions": ["core.templates.Placeholder"]
	},
	"events": {
		ApplicationStarted: PageController.application_after_load
	},
	"models": {
		"engine": SqliteDatabase,
		"database": path.join(current_dir, "kms_site.sqldb")
	}
}

