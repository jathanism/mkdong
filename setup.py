#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


execfile('mkdong/version.py')

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'mkdong',
]

requires = []


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='mkdong',
    version=__version__,
    description='A CLI utility to print dongs.',
    long_description=readme + '\n\n',
    author='Jathan McCollum, Clint Fralick',
    author_email='jathan@gmail.com',
    url='http://pantspooper.org',
    packages=packages,
    package_dir={'mkdong': 'mkdong'},
    include_package_data=True,
    dependency_links=[],
    install_requires=[],
    entry_points="""
        [console_scripts]
        mkdong=mkdong:main
    """,
    license=license,
    zip_safe=False,
    classifiers=(
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)
