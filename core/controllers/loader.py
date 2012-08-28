import os
from pyplug import PluginLoader
from core.extensions import PluginInterface, ContentInterface
from kiss.models import setup_all, drop_all, create_all, session
from putils.dynamics import Importer, Introspector
from core.views.templates import placeholder
from router import PageRouter, ApiRouter
from core.models.content import Plugin, Page
from core.models.security import User, UserGroup, Permission

	
class Loader(object):
	def on_before_init_server(self, application):
		#loading plugins
		for p in application.options["plugins"]["path"]:
			PluginLoader.load(p)
		application.templates_environment.globals["placeholder"] = placeholder	
		
		#adding urls
		application.router.add_urls({"api/(?P<plugin>.+)": ApiRouter})
		application.router.add_urls({"": PageRouter})
		application.router.add_urls({"(?P<url>.+)": PageRouter})
		
		#creating db
		setup_all()
		drop_all()
		create_all()
		
		#setting some properties
		for plugin_name, plugin in PluginInterface.plugins_and_names(fullname=False):
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
			#register plugin in db
			pl_in_db = Plugin.get_or_create(name=plugin_name)
			plugin.db_instance = pl_in_db
		#calling load in all plugins
		PluginInterface.load_call_all()
		
		#adding admin page
		admin_page = Page(plugin=Plugin.get_by(name=u"AdminPageComponent"), title=u"Admin page", url=u"admin", template="adminpagecomponent/default.html")
		#adding login page
		login_page = Page(plugin=Plugin.get_by(name=u"HtmlPageComponent"), title=u"Login page", url=u"login", template="securitycomponent/user/login.html")
		
		#sample data
		from plugins.modules.html.models import HtmlBlock
		from plugins.modules.video.models import VideoBlock
		from plugins.components.html.models import HtmlPage
		from plugins.modules.menu.models import MenuBlock, MenuItem
		hello_page = HtmlPage(plugin=Plugin.get_by(name=u"HtmlPageComponent"), title=u"Aloha", url=u"", template=u"commonresourcesplugin/aloha.html")
		p = HtmlPage(plugin=Plugin.get_by(name=u"HtmlPageComponent"), title=u"test page", url=u"test", template=u"htmlpagecomponent/user/default.html")
		HtmlBlock(plugin=Plugin.get_by(name=u"HtmlBlockModule"), placeholder=u"content1", body=u"<h1>test content from db</h1>", page=p)
		#HtmlBlock(plugin=u"HtmlBlockPlugin", placeholder=u"header", body=u"<h1>header from db</h1>", page=p)
		VideoBlock(plugin=Plugin.get_by(name=u"VideoBlockModule"), page=p, placeholder=u"content2", link=u"SLBsGIP6NTg", template=u"videoblockmodule/user/youtube.html")
		#VideoBlock(plugin=u"VideoBlockPlugin", page=p, placeholder=u"footer", link=u"47502276", template=u"videoblockplugin/user/vimeo.html")
		mb = MenuBlock(plugin=Plugin.get_by(name=u"MenuBlockModule"), placeholder=u"header", title=u"Menu1", page=p, template=u"menublockmodule/user/hierarchical.html")
		mi1 = MenuItem(title=u"MenuItem 1", menu=mb, page=p)
		MenuItem(title=u"MenuItem 11", page=p, parent=mi1)
		mi12 = MenuItem(title=u"MenuItem 12", page=p, parent=mi1)
		MenuItem(title=u"MenuItem 121", page=p, parent=mi12)
		MenuItem(title=u"MenuItem 2", menu=mb, page=p)
		
		#security
		manager_group = UserGroup(name="users")
		admin_group = UserGroup(name="admins", parent=manager_group)
		permission_for_admin_page = Permission(resource=admin_page, user_group=manager_group)
		permission_for_plugin = Permission(resource=Plugin.get_by(name=u"HtmlPageAdminApi"), user_group=manager_group)
		admin_user = User(name="admin", user_group=admin_group)
		manager_user = User(name="stas", user_group=manager_group)
		simple_user = User(name="boris")
		session.commit()
		print "Application loaded(%d plugins)" % len(PluginInterface.plugins())


