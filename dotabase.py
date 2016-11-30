from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
import os

# The absolute path to the dotabase Python package
dotabase_dir = os.path.dirname(os.path.abspath(__file__))
# The filesystem location of the SQLite database file
dotabase_db = os.path.join(dotabase_dir, 'dotabase.db')

Base = declarative_base()

class Hero(Base):
	__tablename__ = 'heroes'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	full_name = Column(String)
	media_name = Column(String)
	localized_name = Column(String)
	real_name = Column(String)
	aliases = Column(String)
	bio = Column(String)
	image = Column(String)
	icon = Column(String)
	portrait = Column(String)

	base_health_regen = Column(Float)
	base_movement = Column(Integer)
	turn_rate = Column(Float)
	base_armor = Column(Integer)
	attack_range = Column(Integer)
	attack_projectile_speed = Column(Integer)
	attack_damage_min = Column(Integer)
	attack_damage_max = Column(Integer)
	attack_rate = Column(Float)
	attack_point = Column(Float)
	attr_primary = Column(String)
	attr_base_strength = Column(Integer)
	attr_strength_gain = Column(Float)
	attr_base_intelligence = Column(Integer)
	attr_intelligence_gain = Column(Float)
	attr_base_agility = Column(Integer)
	attr_agility_gain = Column(Float)

	responses = relationship("Response", back_populates="hero")
	abilities = relationship("Ability", back_populates="hero")

	json_data = Column(String)

	def __repr__(self):
		return "Hero: %s" % (self.localized_name)

class Ability(Base):
	__tablename__ = 'abilities'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"))
	ability_slot = Column(Integer)
	icon = Column(String)
	localized_name = Column(String)
	description = Column(String)
	lore = Column(String)

	json_data = Column(String)

	hero = relationship("Hero", back_populates="abilities")

	def __repr__(self):
		return "Ability: %s" % (self.localized_name)


class Response(Base):
	__tablename__ = 'responses'

	name = Column(String)
	fullname = Column(String, primary_key=True)
	mp3 = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"))
	text = Column(String)
	text_simple = Column(String)
	criteria = Column(String)

	hero = relationship("Hero", back_populates="responses")

	def __repr__(self):
		return "Response: %s" % (self.name)

class Criterion(Base):
	__tablename__ = 'criteria'

	name = Column(String, primary_key=True)
	matchkey = Column(String)
	matchvalue = Column(String)
	weight = Column(Float)
	required = Column(Boolean)


# returns an open dotabase session
# if recreate is true, deletes any existing database first
def dotabase_session():
	engine = create_engine('sqlite:///' + dotabase_db)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	return Session()
