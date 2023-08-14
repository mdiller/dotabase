#!/usr/bin/env python3.6

from os import path
from codecs import open
from setuptools import setup

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
	long_description = f.read()

with open(path.join(path.dirname(__file__), 'VERSION')) as f:
	version = f.read().strip()

setup(
	name='dotabase',
	version=version,
	description='Dota 2 game data extracted as an SQLite database, with an SQLAlchemy wrapper',
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
