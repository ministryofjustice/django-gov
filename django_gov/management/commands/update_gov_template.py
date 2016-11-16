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
            '-d', '--directory', type=str,
            help='path to directory')

    def handle(self, *args, **options):
        tmp_dir = tempfile.gettempdir()
        directory = os.path.abspath(options.get('directory'))
        self.stdout.write(tmp_dir)
        self.stdout.write(directory)
        if not os.path.isdir(directory):
            self.stderr.write('%s is not a valid directory' % directory)
            sys.exit(1)

        response = requests.get(GITHUB_API)
        pkg_data = next(p for p in response.json()['assets'] if
                        p['name'].startswith('django'))

        tarball = os.path.join(tmp_dir, pkg_data['name'])

        urlretrieve(pkg_data['browser_download_url'], tarball)

        pkg_path = os.path.join(tmp_dir, 'django')
        shutil.rmtree(pkg_path)

        subprocess.check_call(['mkdir', 'django'], cwd=tmp_dir)

        subprocess.check_call(['tar', '-xzf', tarball, '-C', 'django'],
                              cwd=tmp_dir)

        template_path = os.path.join(pkg_path, 'govuk_template')

        subprocess.check_call(['rsync', '-r',
                               os.path.join(template_path, 'static', ''),
                               os.path.join(directory, 'static', '')])

        subprocess.check_call(['rsync', '-r',
                               os.path.join(template_path, 'templates', ''),
                               os.path.join(directory, 'templates', '')])

        shutil.rmtree(pkg_path)
