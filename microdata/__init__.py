__version__ = '0.3.dev'
__description__ = 'Microdata semantic markups support for Pelican Blog Generator'


def register():
    from microdata import plugin
    plugin.register()
