# Generates json files from the database.db
# these files serve 2 purposes:
# 1. gives the viewer an idea of what is in the database
# 2. provides a way to look at what changes between each update
from dotabase import *
from collections import OrderedDict
import os
import json
import shutil

json_path = os.path.join(dotabase_dir, "../json/")

session = dotabase_session()

if os.path.exists(json_path):
	shutil.rmtree(json_path)
os.makedirs(json_path)

def write_json(filename, data):
	text = json.dumps(data, indent="\t")
	with open(filename, "w+") as f:
		f.write(text) # Do it like this so it doesnt break mid-file


# dumps an sqlalchemy table to json
def dump_table(table, query=None):
	full_data = []
	if not query:
		query = session.query(table)
	for item in query:
		data = OrderedDict()
		for col in table.__table__.columns:
			value = getattr(item, col.name)
			if col.name == "json_data":
				data[col.name] = json.loads(value, object_pairs_hook=OrderedDict)
			elif value is None or value == "":
				continue
			else:
				data[col.name] = value
		full_data.append(data)
	return full_data

def dump_heroes(filename):
	data = dump_table(Hero)
	write_json(filename, data)

def dump_abilities(filename):
	data = dump_table(Ability)
	write_json(filename, data)

def dump_items(filename):
	data = dump_table(Item)
	write_json(filename, data)

def dump_emoticons(filename):
	data = dump_table(Emoticon)
	write_json(filename, data)

def dump_chatwheel(filename):
	data = dump_table(ChatWheelMessage)
	write_json(filename, data)

def dump_criteria(filename):
	data = dump_table(Criterion)
	write_json(filename, data)

def dump_responses(directory):
	os.makedirs(directory)
	for hero in session.query(Hero):
		data = dump_table(Response, hero.responses)
		filename = os.path.join(directory, f"{hero.name}.json")
		write_json(filename, data)


dump_heroes(json_path + "heroes.json")
dump_items(json_path + "items.json")
dump_abilities(json_path + "abilities.json")
dump_emoticons(json_path + "emoticons.json")
dump_chatwheel(json_path + "chatwheel.json")
dump_criteria(json_path + "criteria.json")
dump_responses(json_path + "responses")