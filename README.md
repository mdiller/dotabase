<h1 align="center">Dotabase</h1>

<p align="center">
	<a href="https://pypi.org/project/dotabase/">
		<img alt="PyPi" src="https://img.shields.io/pypi/v/dotabase.svg?style=for-the-badge&logo=pypi">
	</a>
	<a href="https://www.dota2.com/patches/">
		<img alt="Dota Version" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/mdiller/dotabase/master/DOTA_VERSION">
	</a>
</p>

A SQLite database representing much of the data from Dota 2 game files, and a SQLAlchemy representation to be used with it. This was built using my [dotabase-builder](https://github.com/mdiller/dotabase-builder) project. Note that I've removed the database from this repository, as binary files are not git-friendly, and have replaced it with a SQL file dump of the database.

## Description
The goal of this project is to provide an interface into Dota 2 game files so that applications can be built around them. This repository will be kept up to date with Dota so that changes to the game are immediately available. 
One main feature of this project that I couldn't find anywhere else, is a representation of Dota's Hero Response system. This is the system that controls the various vocal responses that heroes have to actions that happen in the game. 
In addition to supplying a SQLite database, this project includes a Python SQLAlchemy representation of the database, which provides an easy way to interface with Python applications. (dotabase.py) It also happens to be a good file to look at if you want to get an idea of the structure of the database
NOTE: This project does not supply any player information or data from specific Dota games. There are plenty of [already](http://dev.dota2.com/showthread.php?t=47115 "Dota 2 Match History API") [existing](https://steamcommunity.com/dev "Steam Web API") [API](http://docs.opendota.com/ "OpenDota/Yasp API")s for that.

## Usage
If you want to use the dotabase package in your Python applications, you can install via pip like this:
```
pip install dotabase
```

Example usage:
```python
from dotabase import *

session = dotabase_session()

for hero in session.query(Hero):
	print(hero)
```
If you use MyPy, you should be able to get typing hints and your editor should recognize that the "hero" variable above is an instance of the "Hero" class.

Note that the package was built using Python 3.9 and SQLAlchemy 1.4

## JSON files
In the `json` directory, I've auto-generated a bunch of JSON files that give you an idea of what is inside the database. These are also useful for seeing the difference between builds.

## Builder
The database is built using my custom [dotabase-builder](https://github.com/mdiller/dotabase-builder "Dotabase Builder"). Check it out for more information on how this project is being constructed. Note that the database is constructed and then dumped to a SQL creation script for saving to source control. You can reconstruct it with `sqlite3 dotabase.db ".read dotabase.db.sql"`

## Extracted VPK Files
The files extracted from Dota's vpk are all the ones of the following types:
- txt
- png
- mp3 (extracted from vsnd_c files)

More file types will be added later.