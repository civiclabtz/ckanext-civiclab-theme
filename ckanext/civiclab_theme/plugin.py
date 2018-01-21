import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Civiclab_ThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

# IRoutes
    def before_map(self,m):
        m.connect('applications','/applications',controller='ckanext.civiclab_theme.controller:ApplicationsController',action='applications')
	m.connect('developers','/developers',controller='ckanext.civiclab_theme.controller:DevelopersController',action='developers')
	m.connect('datarequest','/datarequest',controller='ckanext.civiclab_theme.controller:DataRequestController',action='datarequest')
	m.connect('contact','/contact',controller='ckanext.civiclab_theme.controller:ContactController',action='contact')
        return m

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'civiclab_theme')
	

    

