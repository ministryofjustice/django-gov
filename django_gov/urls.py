# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url

from moj_irat.views import PingJsonView, HealthcheckView


urlpatterns = [
    url(r'^ping.json$', PingJsonView.as_view(**settings.PING_JSON_KEYS),
        name='ping_json'),
    url(r'^healthcheck.json$', HealthcheckView.as_view(),
        name='healthcheck_json'),
]
