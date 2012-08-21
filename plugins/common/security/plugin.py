# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import PagePluginInterface


class SecurityPagePlugin(Plugin):
	implements = [PagePluginInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def name(self):
		return _("security page").decode('utf-8')
		
	def admin(self):
		return "hey sec"

