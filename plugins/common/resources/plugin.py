from pyplug import Plugin
from core.extensions import PluginInterface


class CommonResourcesPlugin(Plugin):
	implements = [PluginInterface]
	
	def __init__(self):
		print "%s loaded" % self.__class__.__name__

