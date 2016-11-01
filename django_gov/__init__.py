# -*- coding: utf-8 -*-
__version__ = (0,  0, 1)


DEFAULT_SETTINGS = {
    'DEFAULT_SETTING': True,
}


try:
    from django.conf import settings
    settings.configure(default_settings=DEFAULT_SETTINGS, DEBUG=True)
except ImportError:
    pass
