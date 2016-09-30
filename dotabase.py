from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
import os

# built using: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html

Base = declarative_base()

class Hero(Base):
	__tablename__ = 'heroes'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	full_name = Column(String)
	media_name = Column(String)
	localized_name = Column(String)
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

	json_data = Column(String)

	def __repr__(self):
		return "Hero: %s" % (self.localized_name)

responsegroupings_table = Table('responsegroupings', Base.metadata,
    Column('response_fullname', Integer, ForeignKey('responses.fullname')),
    Column('responserule_name', Integer, ForeignKey('responserules.name'))
)

class Response(Base):
	__tablename__ = 'responses'

	name = Column(String)
	fullname = Column(String, primary_key=True)
	mp3 = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"))
	text = Column(String)

	hero = relationship("Hero", back_populates="responses")
	groups = relationship("ResponseRule", secondary=responsegroupings_table, back_populates="responses")

	def __repr__(self):
		return "Response: %s" % (self.name)

class ResponseRule(Base):
	__tablename__ = 'responserules'

	name = Column(String, primary_key=True)

	responses = relationship("Response", secondary=responsegroupings_table, back_populates="groups")
	criteriargs = relationship("CriteriArg", order_by="CriteriArg.index")

class Criterion(Base):
	__tablename__ = 'criteria'

	name = Column(String, primary_key=True)
	matchkey = Column(String)
	matchvalue = Column(String)
	weight = Column(Float)
	required = Column(Boolean)

class CriteriArg(Base):
	__tablename__ = 'criteriargs'

	group_name = Column(String, ForeignKey("responserules.name"), primary_key=True)
	index = Column(Integer, primary_key=True)
	criterion_name = Column(String, ForeignKey("criteria.name"))


# returns an open dotabase session
# if recreate is true, deletes any existing database first
def dotabase_session(recreate=True):
	if recreate and os.path.exists("dotabase.db"):
		os.remove("dotabase.db")
	engine = create_engine('sqlite:///dotabase.db')
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	return Session()
