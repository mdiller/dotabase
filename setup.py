#!/usr/bin/env python3.6

from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
	long_description = f.read()

setup(
	name='dotabase',
	version='4.8.4',
	description='Dota 2 game data extracted as an sqlite database, with an sqlalchemy wrapper',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Malcolm Diller',
	author_email='malcolm@dillerm.io',
	url='https://github.com/mdiller/dotabase',
	keywords='dota dota2 data sqlite',
	include_package_data=True,
	packages=['dotabase'],
	install_requires=['sqlalchemy'],
	classifiers=[
		'License :: OSI Approved :: MIT License'
	],
)
