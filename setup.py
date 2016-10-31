# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from django_gov import __version__

github_url = 'https://github.com/ministryofjustice/django-gov'

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-gov',
    version='.'.join(str(v) for v in __version__),
    description='Base Django Application for MoJ Gov',
    long_description=readme + '\n\n' + history,
    url=github_url,
    author='Josh Rowe',
    author_email='josh.rowe@digital.justice.gov.uk',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'Django==1.10.2',
        'django-cors-headers==1.2.2',
        'django-extended-choices==1.0.7',
        'django-filter==0.15.2',
        'django-rest-swagger==2.0.7',
        'djangorestframework==3.5.0',
        'openpyxl==2.4.0',
        'psycopg2==2.6.2',
        'PyYAML==3.12',
        'django-moj-irat==4d54b86b1cb574fe787ba0fb8a992cf352f8eba6'
    ],
    dependency_links=[
        "git+ssh://git@//github.com/ministryofjustice/django-moj-irat.git@4d54b86b1cb574fe787ba0fb8a992cf352f8eba6"
    ],
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
