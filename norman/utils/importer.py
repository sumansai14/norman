import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['norman/settings'])[0]
    except:
        default_django_settings_module = 'norman.settings.dev'
    else:
        default_django_settings_module = 'norman.settings.local'
        file_.close()
    return default_django_settings_module
