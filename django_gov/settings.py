# -*- coding: utf-8 -*-

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

API_VERSION = 'v1'

SWAGGER_SETTINGS = {
    'APIS_SORTER': 'alpha',
    'DOC_EXPANSION': 'list'
}

PING_JSON_KEYS = {
    'build_date_key': 'APP_BUILD_DATE',
    'commit_id_key': 'APP_GIT_COMMIT',
    'version_number_key': 'APPVERSION',
    'build_tag_key': 'APP_BUILD_TAG',
}

HEALTHCHECKS = [
    'moj_irat.healthchecks.database_healthcheck',
]

AUTODISCOVER_HEALTHCHECKS = True

CORS_ORIGIN_ALLOW_ALL = True

TEST_RUNNER = 'django_gov.tests.runner.GovDiscoverRunner'
