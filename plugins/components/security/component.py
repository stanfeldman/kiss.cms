# -*- coding: utf-8 -*-
from pyplug import Plugin
from core.extensions import ComponentInterface
from kiss.views.templates import TemplateResponse, Template


class SecurityComponent(Plugin):
	implements = [ComponentInterface]
	
	def load(self):
		print "%s loaded" % self.__class__.__name__
		
	def title(self):
		return "Security component"
		
	def content(self, page):
		return TemplateResponse(page.template)


