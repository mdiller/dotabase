# Dotabase

[![PyPi](https://img.shields.io/pypi/v/dotabase.svg)](https://pypi.org/project/dotabase/)
[![Dota Version](https://img.shields.io/badge/dota-version%207.22d-e05d44.svg)](http://www.dota2.com/)

An sqlite database representing much of the data from dota2's game files, and an sqlalchemy representation to be used with it. This was built using my [dotabase-builder](https://github.com/mdiller/dotabase-builder) project.

## Description
The goal of this project is to provide an interface into dota's game files so that applications can be built around them. This repository will be kept up to date with dota so that changes to the game are available immediately. 
One main feature of this project that I couldn't find anywhere else, is a representation of dota's Hero Response system. This is the system that controls the various vocal responses that heroes have to actions that are happening in the game. 
In addition to supplying a sqlite database, this project includes a python sqlalchemy representation of the database, which provides an easy way to interface with python applications. (dotabase.py) It also happens to be a good file to look at if you want to get an idea of the structure of the database
NOTE: This project does not supply any player information or data from specific dota games. There are plenty of [already](http://dev.dota2.com/showthread.php?t=47115 "Dota 2 Match History API") [existing](https://steamcommunity.com/dev "Steam Web API") [API](http://docs.opendota.com/ "OpenDota/Yasp API")s for that.

## Installation
To start using the database, simply clone this repository and use any of the wide variety of ways to interface with the sqlite dotabase.db file.

If you want to use the dotabase package in your python applications, you can install via pip like this:
```
pip install dotabase
```

Example Usage:
```python
from dotabase import *

session = dotabase_session()

for hero in session.query(Hero):
	print(hero)
```
Note that the package was built using python 3.5 and sqlalchemy 1.1

## JSON files

In the `json` directory, I've auto-generated a bunch of json files that give you an idea of what is inside the database. These are also useful for seeing the difference between builds.

## Builder
The database is built using my custom [dotabase-builder](https://github.com/mdiller/dotabase-builder "Dotabase Builder"). Check it out for more information of how this project is being constructed.

## Extracted VPK Files
The files extracted from dota's vpk are all of the ones of the following types:
- txt
- png
- mp3 (extracted from vsnd_c files)

More file types will be added later