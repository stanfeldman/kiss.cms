from jinja2.ext import Extension
from jinja2 import nodes
from jinja2 import Markup
from core.extensions import ContentPluginInterface

class Placeholder(Extension):
	tags = set(["placeholder"])
	
	def __init__(self, environment):
		super(Placeholder, self).__init__(environment)
		self.placeholders = {}
	
	def parse(self, parser):
		stream = parser.stream
		tag_token = stream.next()
		arg_token = stream.next()
		arg = nodes.Const(arg_token.value, lineno=arg_token.lineno)
		#if not parser.filename in self.placeholders:
		#	self.placeholders[parser.filename] = set()
		#self.placeholders[parser.filename].add(arg.value)
		#print self.placeholders
		return nodes.Output([self.call_method('_render', [arg])]).set_lineno(tag_token.lineno)

	def _render(self, placeholder):
		content = ContentPluginInterface.content(placeholder)
		if content:
			return Markup(content)
		else:
			return Markup("")
