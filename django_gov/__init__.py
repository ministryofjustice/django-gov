# -*- coding: utf-8 -*-
from django.conf import settings


__version__ = (0,  0, 1)

DEFAULT_SETTINGS = {

}

settings.configure(default_settings=DEFAULT_SETTINGS, DEBUG=True)
