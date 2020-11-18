<h1 align="center">Dotabase</h1>

<p align="center">
	<a href="https://pypi.org/project/dotabase/">
		<img alt="PyPi" src="https://img.shields.io/pypi/v/dotabase.svg?style=for-the-badge&logo=pypi">
	</a>
	<a href="https://www.dota2.com/patches/">
		<img alt="Dota Version" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/mdiller/dotabase/master/DOTA_VERSION">
	</a>
</p>

An sqlite database representing much of the data from dota2's game files, and an sqlalchemy representation to be used with it. This was built using my [dotabase-builder](https://github.com/mdiller/dotabase-builder) project. Note that I've removed the database from this repository as binary files are not git-friendly, and have replaced it with an sql file dump of the database.

## Description
The goal of this project is to provide an interface into dota's game files so that applications can be built around them. This repository will be kept up to date with dota so that changes to the game are available immediately. 
One main feature of this project that I couldn't find anywhere else, is a representation of dota's Hero Response system. This is the system that controls the various vocal responses that heroes have to actions that are happening in the game. 
In addition to supplying a sqlite database, this project includes a python sqlalchemy representation of the database, which provides an easy way to interface with python applications. (dotabase.py) It also happens to be a good file to look at if you want to get an idea of the structure of the database
NOTE: This project does not supply any player information or data from specific dota games. There are plenty of [already](http://dev.dota2.com/showthread.php?t=47115 "Dota 2 Match History API") [existing](https://steamcommunity.com/dev "Steam Web API") [API](http://docs.opendota.com/ "OpenDota/Yasp API")s for that.

## Usage

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
The database is built using my custom [dotabase-builder](https://github.com/mdiller/dotabase-builder "Dotabase Builder"). Check it out for more information of how this project is being constructed. Note that the database is constructed and then dumped to an sql creation script for saving to source control. You can reconstruct it with `sqlite3 dotabase.db ".read dotabase.db.sql"`

## Extracted VPK Files
The files extracted from dota's vpk are all of the ones of the following types:
- txt
- png
- mp3 (extracted from vsnd_c files)

More file types will be added later