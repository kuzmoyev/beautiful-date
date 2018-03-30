#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree

from setuptools import setup, Command

here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()


NAME = 'beautiful-date'
DESCRIPTION = 'Simple and beautiful way to create date and datetime objects in Python.'
URL = 'https://github.com/kuzmoyev/beautiful-date'
DOWNLOAD_URL = 'https://github.com/kuzmoyev/beautiful-date/archive/1.0.tar.gz'
EMAIL = 'kuzmovych.goog@gmail.com'
AUTHOR = 'Yevhen Kuzmovych'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '1.0.1'

REQUIRED = [
    'python-dateutil==2.7.2',
    'six==1.11.0'
]

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    download_url=DOWNLOAD_URL,
    py_modules=['beautiful_date', 'beautiful_timedelta', 'date_range'],
    packages=['beautiful_date', 'beautiful_tests'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords=['beautiful', 'date', 'simple', 'timedelta', 'date-range'],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
