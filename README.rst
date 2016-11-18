=======================
Base Django App for MoJ
=======================

This can be used as a base to build MoJ Django applications. It includes some useful Django packages along with the Gov.uk template. It also includes flake8 code style test.

Includes
========

Django
django-cors-headers
django-extended-choices
django-filter
django-moj-irat
django-rest-swagger
djangorestframework
flake8
openpyxl
PyYAM
requests

Dependencies
============

-  `Python 3.5 <http://www.python.org/>`__ (can be installed using :code:`brew install python3`)


Installation
============

Install via pypi

::

    pip install django-gov


Features
========

govuk_template Django template and sstatic directory are included in the package, you can also download the latest govuk_template taball and extract the contentents to a directory of you choice

::

    ./manage.py update_gov_template -d /path/to/directory/to/unpack/


This will add the templates and static directories from the latest release of govuk_template to the directory passed as -d


You can include the default settings for all the included apps above by including the default settings in youe app settings.py file

::

    from django_gov.settings import *


You can include the urls for the healthcheck endpoints

::

    url(r'^', include('django_gov.urls'))


