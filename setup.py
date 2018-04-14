#!/usr/bin/env python3.6

from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='dotabase',
	version='4.2.3',
	description='Dota 2 game data extracted as an sqlite database, with an sqlalchemy wrapper',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Malcolm Diller',
	author_email='malcolm@dillerm.io',
	url='https://github.com/mdiller/dotabase',
	license='MIT',
	keywords='dota dota2 data sqlite',
	packages=['dotabase'],
	install_requires=['sqlalchemy'],
)