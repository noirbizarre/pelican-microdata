#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


def rst(filename):
    '''
    Load rst file and sanitize it for PyPI.
    Remove unsupported PyPI tags:
     - code-block directive
    '''
    content = open(filename).read()
    return re.sub(r'\.\.\s? code-block::\s*(\w|\+)+', '::', content)


long_description = '\n'.join((
    rst('README.rst'),
    rst('CHANGELOG.rst'),
    ''
))

setup(
    name='pelican-microdata',
    version=__import__('microdata').__version__,
    description=__import__('microdata').__description__,
    long_description=long_description,
    url='https://github.com/noirbizarre/pelican-microdata',
    download_url='http://pypi.python.org/pypi/pelican-microdata',
    author='Axel Haustant',
    author_email='noirbizarre+pelican@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pelican'],
    license='LGPL',
    use_2to3=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)
