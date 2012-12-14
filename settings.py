#this is only for dev, in production you should use this packages from pypi
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append("%s/../kiss.py" % current_dir)
sys.path.append("%s/../compressinja" % current_dir)
sys.path.append("%s/../putils" % current_dir)
sys.path.append("%s/../pyplug" % current_dir)
sys.path.append("%s/../pev" % current_dir)

#internal options in core.startup
options = {
	"application": {
		"address": "127.0.0.1",
		"port": 8080
	},
	"plugins": {
		"path": ["plugins"]
	},
	"models": {
		"connection": "sqlite:///%s/data.sqldb" % current_dir
	}
}

