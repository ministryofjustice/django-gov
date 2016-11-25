=======================
Base Django App for MoJ
=======================

This can be used as a base to build MoJ Django applications. It includes some useful Django packages along with the Gov.uk template. It also includes flake8 code style test.

Includes
========

`Django <https://pypi.python.org/pypi/django>`__

`django-cors-headers <https://pypi.python.org/pypi/django-cors-headers>`__

`django-extended-choices <https://pypi.python.org/pypi/django-extended-choices>`__

`django-filter <https://pypi.python.org/pypi/django-filter>`__

`django-moj-irat <https://pypi.python.org/pypi/django-moj-irat>`__

`django-rest-swagger <https://pypi.python.org/pypi/django-rest-swagger>`__

`djangorestframework <https://pypi.python.org/pypi/django-rest-framework>`__

`flake8 <https://pypi.python.org/pypi/flake8>`__

`openpyxl <https://pypi.python.org/pypi/openpyxl>`__

`PyYAM <https://pypi.python.org/pypi/pyyaml>`__

`requests <https://pypi.python.org/pypi/requests>`__


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


You can include the default settings for all the included apps above by including the default settings in your app settings.py file

::

    from django_gov.settings import *


You can include the urls for the healthcheck endpoints

::

    url(r'^', include('django_gov.urls'))


Testing
=======

If you include the whole default settings, this will add flake8 code style tests to the directory you run your apps.

You can add a `setup.cfg` file containing your flake8 settings to the base directory of your app.

::

    [flake8]
    exclude = .git/,env/,venv/,node_modules/, manage.py
    max-complexity = 10
    max-line-length = 120


