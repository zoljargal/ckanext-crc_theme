import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

def all_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'all_fields': True, 'limit': 10})

    return groups

def latest_changed_packages():
    return toolkit.get_action('recently_changed_packages_activity_list')(data_dict={'limit': 10})

def date_string(ts):
    return ts[0:10]

class Num_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation, inherit=True)
    plugins.implements(plugins.IConfigurer, inherit=True)
    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'num_theme')

    def get_helpers(self):
        '''Register the helper function.'''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {
            'num_all_groups': all_groups,
            'num_latest_changed_packages': latest_changed_packages,
            'date_string_from_timestamp': date_string,
        }
