import os

from norman.utils.importer import get_default_django_settings_module
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
os.environ.setdefault("DJANGO_CONFIGURATION", 'Settings')

from configurations.wsgi import get_wsgi_application  # NOQA

application = get_wsgi_application()