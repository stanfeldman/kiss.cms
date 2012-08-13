#this is only for dev, in production you should use this packages from pypi
import sys, os
sys.path.append("/home/stanislavfeldman/projects/python/kiss.py")
sys.path.append("/home/stanislavfeldman/projects/python/compressinja")
sys.path.append("/home/stanislavfeldman/projects/python/putils")
sys.path.append("/home/stanislavfeldman/projects/python/pyplug")
sys.path.append("/home/stanislavfeldman/projects/python/pev")
current_dir = os.path.dirname(os.path.abspath(__file__))

options = {
	"application": {
		"address": "127.0.0.1",
		"port": 8080
	},
	"views": {
		"templates_path": ["website.templates"],
		"static_path": ["website.static"]
	},
	"models": {
		"connection": "sqlite:///%s/data.sqldb" % current_dir
	}
}

