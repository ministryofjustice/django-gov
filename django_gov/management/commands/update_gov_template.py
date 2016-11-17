# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import sys
import tempfile
from urllib.request import urlretrieve

import requests

from django.core.management import BaseCommand


GITHUB_API = 'https://api.github.com/repos/alphagov/govuk_template/releases/latest'
DIR = 'govuk_template'


class Command(BaseCommand):
    help = 'Create latest django govuk_template in to a specific directory.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-d', '--destination', type=str,
            help='path to template destination')

    def handle(self, *args, **options):
        tmp_dir = tempfile.gettempdir()
        destination = os.path.abspath(options.get('destination'))
        self.stdout.write('Temp directory: %s' % tmp_dir)
        self.stdout.write('Destination directory: %s' % destination)
        if not os.path.isdir(destination):
            self.stderr.write('%s is not a valid directory' % destination)
            sys.exit(1)

        self.stdout.write('Getting package information from : %s' % GITHUB_API)
        response = requests.get(GITHUB_API)
        pkg_data = next(p for p in response.json()['assets'] if
                        p['name'].startswith('django'))

        tarball = os.path.join(tmp_dir, pkg_data['name'])

        self.stdout.write('Getting tarball %s from : %s' %
                          (tarball, pkg_data['browser_download_url']))
        urlretrieve(pkg_data['browser_download_url'], tarball)

        pkg_path = os.path.join(tmp_dir, 'django')
        try:
            shutil.rmtree(pkg_path)
        except FileNotFoundError:
            pass

        self.stdout.write('Making directory: %s' % pkg_path)
        subprocess.check_call(['mkdir', 'django'], cwd=tmp_dir)

        self.stdout.write('Untaring tarball: %s' % tarball)
        subprocess.check_call(['tar', '-xzf', tarball, '-C', 'django'],
                              cwd=tmp_dir)

        source_path = os.path.join(pkg_path, 'govuk_template')

        for d in ['static', 'templates']:
            self.stdout.write('rsync %s to %s' %
                              (os.path.join(source_path, d, ''),
                               os.path.join(destination, d, '')))
            subprocess.check_call(['rsync', '-r',
                                   os.path.join(source_path, d, ''),
                                   os.path.join(destination, d, '')])

        shutil.rmtree(pkg_path)
