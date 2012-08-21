from kiss.views.templates import TemplateResponse
from kiss.views.core import Response
from kiss.core.events import Eventer
import datetime
from kiss.controllers.core import Controller
import os
from pyplug import PluginLoader
from core.extensions import PagePluginInterface, PageBlockPluginInterface, PluginInterface
from kiss.models import setup_all, drop_all, create_all, session
from putils.dynamics import Introspector, Importer
from templates import placeholder
from models import Page

	
class PageController(Controller):	
	def get(self, request):
		if "url" not in request.params:
			request.params["url"] = ""
		page = Page.get_by(url=request.params["url"])
		if page:
			content = PagePluginInterface.plugins[page.plugin].content(page)
			return Response(content)
		return None
		
	def on_before_init_server(self, application):
		#loading plugins
		for p in application.options["plugins"]["path"]:
			PluginLoader.load(p)
		application.templates_environment.globals["placeholder"] = placeholder	
		#adding urls
		application.router.add_urls({"": PageController})
		for i in [PagePluginInterface, PageBlockPluginInterface]:
			for urls in i.urls_get_all():
				if urls:
					application.router.add_urls(urls)
		application.router.add_urls({"(?P<url>.+)": PageController})
		#creating db
		setup_all()
		drop_all()
		create_all()
		#setting some properties
		for i in [PagePluginInterface, PageBlockPluginInterface, PluginInterface]:
			for plugin_name, plugin in i.plugins.iteritems():
				#set application ref to plugin
				plugin.application = application
				plugin_dir = os.path.dirname(Importer.object_path(plugin))
				#adding templates paths
				templates_dir = os.path.join(plugin_dir, "templates")
				if os.path.exists(templates_dir):
					application.templater.add_template_paths([templates_dir], plugin_name.lower())
					plugin.template_path = templates_dir
				#adding static paths
				static_dir = os.path.join(plugin_dir, "static")
				if os.path.exists(static_dir):
					application.add_static([static_dir], url_path="/" + plugin_name.lower())
					plugin.static_path = static_dir
				#adding translation paths
				trans_dir = os.path.join(plugin_dir, "lang")
				if os.path.exists(trans_dir):
					application.templater.add_translation_paths([trans_dir])
					plugin.translation_path = trans_dir
		#calling load in all plugins
		for i in [PagePluginInterface, PageBlockPluginInterface, PluginInterface]:
			i.load_call_all()
		#sample data
		from plugins.block.html.models import HtmlBlock
		from plugins.block.video.models import VideoBlock
		from plugins.page.html.models import HtmlPage
		from plugins.block.menu.models import MenuBlock, MenuItem
		p = HtmlPage(plugin=u"HtmlPagePlugin", title=u"test page", url=u"tp", template=u"htmlpageplugin/user/default.html")
		HtmlBlock(plugin=u"HtmlBlockPlugin", placeholder=u"content1", body=u"<h1>test content from db</h1>", page=p)
		#HtmlBlock(plugin=u"HtmlBlockPlugin", placeholder=u"header", body=u"<h1>header from db</h1>", page=p)
		VideoBlock(plugin=u"VideoBlockPlugin", page=p, placeholder=u"content2", link=u"SLBsGIP6NTg", template=u"videoblockplugin/user/youtube.html")
		#VideoBlock(plugin=u"VideoBlockPlugin", page=p, placeholder=u"footer", link=u"47502276", template=u"videoblockplugin/user/vimeo.html")
		mb = MenuBlock(plugin=u"MenuBlockPlugin", placeholder=u"header", title=u"Menu1", page=p, template=u"menublockplugin/user/hierarchical.html")
		mi1 = MenuItem(title=u"MenuItem 1", menu=mb, page=p)
		MenuItem(title=u"MenuItem 11", page=p, parent=mi1)
		mi12 = MenuItem(title=u"MenuItem 12", page=p, parent=mi1)
		MenuItem(title=u"MenuItem 121", page=p, parent=mi12)
		MenuItem(title=u"MenuItem 2", menu=mb, page=p)
		session.commit()
		print "Application loaded"


