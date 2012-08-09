import sys, os
sys.path.append("/home/stanislavfeldman/projects/python/kms")
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
		"templates_path": ["templates"],
		"static_path": "static"
	},
	"models": {
		"connection": "sqlite:///%s/kms_site.sqldb" % current_dir
	}
}

