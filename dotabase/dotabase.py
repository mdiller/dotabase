import os

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, Date, DateTime, Unicode
from sqlalchemy.orm import relationship, Session, declarative_base
from sqlalchemy_utils import generic_relationship

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
	roles = Column(String)
	role_levels = Column(String)
	hype = Column(String)
	bio = Column(String)
	image = Column(String)
	icon = Column(String)
	portrait = Column(String)
	color = Column(String)
	legs = Column(Integer)

	team = Column(String)
	base_health_regen = Column(Float)
	base_mana_regen = Column(Float)
	base_movement = Column(Integer)
	base_attack_speed = Column(Integer)
	turn_rate = Column(Float)
	base_armor = Column(Integer)
	attack_range = Column(Integer)
	attack_projectile_speed = Column(Integer)
	attack_damage_min = Column(Integer)
	attack_damage_max = Column(Integer)
	attack_rate = Column(Float)
	attack_point = Column(Float)
	attr_primary = Column(String)
	attr_strength_base = Column(Integer)
	attr_strength_gain = Column(Float)
	attr_intelligence_base = Column(Integer)
	attr_intelligence_gain = Column(Float)
	attr_agility_base = Column(Integer)
	attr_agility_gain = Column(Float)
	vision_day = Column(Integer)
	vision_night = Column(Integer)
	magic_resistance = Column(Integer)
	is_melee = Column(Boolean)
	material = Column(String)

	abilities = relationship("Ability", order_by="Ability.slot", back_populates="hero")
	talents = relationship("Talent", order_by="Talent.slot")
	responses = relationship("Response", back_populates="hero")
	voice = relationship("Voice", uselist=False, back_populates="hero")
	facets = relationship("Facet", back_populates="hero")
	strings = relationship(
		"LocaleString",
		primaryjoin="and_(foreign(LocaleString.table) == 'Hero', foreign(LocaleString.row_id) == Hero.id)",
		viewonly=True
	)

	json_data = Column(String)

	def __repr__(self):
		return f"Hero: {self.localized_name}"


class Ability(Base):
	__tablename__ = 'abilities'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"), nullable=True)

	behavior = Column(String)
	damage_type = Column(String)
	spell_immunity = Column(String)
	target_team = Column(String)
	dispellable = Column(String)

	cast_range = Column(String)
	cast_point = Column(String)
	channel_time = Column(String)
	cooldown = Column(String)
	duration = Column(String)
	damage = Column(String)
	health_cost = Column(String)
	mana_cost = Column(String)
	charges = Column(String)
	ability_special = Column(String)

	slot = Column(Integer)
	icon = Column(String)

	localized_name = Column(String)
	description = Column(String)
	lore = Column(String)
	note = Column(String)
	scepter_grants = Column(Boolean)
	scepter_upgrades = Column(Boolean)
	scepter_description = Column(String)
	shard_grants = Column(Boolean)
	shard_upgrades = Column(Boolean)
	shard_description = Column(String)

	innate = Column(Boolean)
	facet_id = Column(Integer, ForeignKey("facets.id"), nullable=True)

	json_data = Column(String)

	facet = relationship("Facet", back_populates="abilities")
	hero = relationship("Hero", back_populates="abilities")
	talent_links = relationship("Talent", back_populates="ability")
	facet_strings = relationship("FacetAbilityString", back_populates="ability")
	strings = relationship(
		"LocaleString",
		primaryjoin="and_(foreign(LocaleString.table) == 'Ability', foreign(LocaleString.row_id) == Ability.id)",
		viewonly=True
	)

	# _locale = None
	# def __getattr__(self, name: str):
	# 	if name.endswith("_L"):
	# 		name = name[:-2]
	# 		if hasattr(self, name):
	# 			for string in self.strings:
	# 				if string.lang == self._locale and string.column == name:
	# 					return string.value
	# 	return Base.__getattribute__(self, name)
	
	@property
	def facet_grants(self):
		return self.facet_id is not None

	@property
	def aghanim(self):
		return self.scepter_description

	@property
	def aghanim_grants(self):
		return self.scepter_grants

	@property
	def is_talent(self):
		return len(self.talent_links) > 0

	def __repr__(self):
		return f"Ability: {self.localized_name}"


class Talent(Base):
	__tablename__ = 'talents'

	hero_id = Column(Integer, ForeignKey("heroes.id"), primary_key=True, nullable=True)
	ability_id = Column(Integer, ForeignKey("abilities.id"), primary_key=True)
	slot = Column(Integer)
	linked_abilities = Column(String)

	ability = relationship("Ability", back_populates="talent_links")

	@property
	def localized_name(self):
		return self.ability.localized_name

	@property
	def level(self):
		return ((self.slot // 2) * 5) + 10

	@property
	def is_right_side(self):
		return (self.slot % 2) == 0

	def __repr__(self):
		return f"Talent: {self.localized_name}"

class Facet(Base):
	__tablename__ = 'facets'

	id = Column(Integer, primary_key=True) # auto-generated
	name = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"), nullable=True)
	icon =  Column(String)
	icon_name =  Column(String)
	color =  Column(String)
	gradient_id =  Column(Integer)
	slot = Column(Integer)

	ability_special = Column(String)
	json_data = Column(String)

	localized_name = Column(String)
	description = Column(String)


	hero = relationship("Hero", back_populates="facets")
	abilities = relationship("Ability", order_by="Ability.id", back_populates="facet")
	ability_strings = relationship("FacetAbilityString", back_populates="facet")
	strings = relationship(
		"LocaleString",
		primaryjoin="and_(foreign(LocaleString.table) == 'Facet', foreign(LocaleString.row_id) == Facet.id)",
		viewonly=True
	)

	# other stuff could include
	# "KeyValueOverrides": {
    #   "AttributeBaseStrength": "22",
    #   "AttributeStrengthGain": "4.0"
    # },
	# "AbilityIconReplacements": {
    #   "windrunner_focusfire": "windrunner_whirlwind",
    #   "windrunner_focusfire_cancel": "windrunner_whirlwind_stop"
    # }

	def __repr__(self):
		return f"Facet: {self.localized_name}"


class FacetAbilityString(Base):
	__tablename__ = 'facetabilitystrings'

	id = Column(Integer, primary_key=True) # auto-generated
	facet_id = Column(Integer, ForeignKey("facets.id"))
	ability_id = Column(Integer, ForeignKey("abilities.id"))
	description = Column(String)

	ability = relationship("Ability", back_populates="facet_strings")
	facet = relationship("Facet", back_populates="ability_strings")

	strings = relationship(
		"LocaleString",
		primaryjoin="and_(foreign(LocaleString.table) == 'Facet', foreign(LocaleString.row_id) == FacetAbilityString.id)",
		viewonly=True
	)


class Item(Base):
	__tablename__ = 'items'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	localized_name = Column(String)
	aliases = Column(String)
	quality = Column(String)
	icon = Column(String)
	cost = Column(Integer)
	cooldown = Column(String)
	cast_range = Column(String)
	health_cost = Column(String)
	mana_cost = Column(String)
	duration = Column(String)
	base_level = Column(Integer)
	description = Column(String)
	lore = Column(String)
	secret_shop = Column(Boolean)
	neutral_tier = Column(String)
	is_neutral_enhancement = Column(Boolean)
	ability_special = Column(String)
	recipe = Column(String)
	shop_tags = Column(String)

	json_data = Column(String)

	strings = relationship(
		"LocaleString",
		primaryjoin="and_(foreign(LocaleString.table) == 'Item', foreign(LocaleString.row_id) == Item.id)",
		viewonly=True
	)

	def __repr__(self):
		return f"Item: {self.localized_name}"


class Voice(Base):
	__tablename__ = 'voices'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	icon = Column(String)
	image = Column(String)
	url = Column(String)
	media_name = Column(String)
	voice_actor = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"))
	criteria = Column(String)

	hero = relationship("Hero", back_populates="voice")
	responses = relationship("Response", back_populates="voice")


class Response(Base):
	__tablename__ = 'responses'

	name = Column(String)
	fullname = Column(String, primary_key=True)
	mp3 = Column(String)
	hero_id = Column(Integer, ForeignKey("heroes.id"))
	voice_id = Column(Integer, ForeignKey("voices.id"))
	text = Column(String)
	text_simple = Column(String)
	criteria = Column(String)
	pretty_criteria = Column(String)

	hero = relationship("Hero", back_populates="responses")
	voice = relationship("Voice", back_populates="responses")

	def __repr__(self):
		return f"Response: {self.name}"


class Criterion(Base):
	__tablename__ = 'criteria'

	name = Column(String, primary_key=True)
	pretty = Column(String)
	matchkey = Column(String)
	matchvalue = Column(String)
	weight = Column(Float)
	required = Column(Boolean)


class Emoticon(Base):
	__tablename__ = 'emoticons'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	url = Column(String)
	frames = Column(Integer)
	ms_per_frame = Column(Integer)


class ChatWheelMessage(Base):
	__tablename__ = 'chatwheelmessages'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	message = Column(String)
	label = Column(String)
	sound = Column(String)
	image = Column(String)
	all_chat = Column(Boolean)
	category = Column(String)
	source = Column(String)


class LoadingScreen(Base):
	__tablename__ = 'loadingscreens'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	image = Column(String)
	thumbnail = Column(String)
	creation_date = Column(Date)

	color = Column(String)
	hue = Column(Integer)
	saturation = Column(Integer)
	value = Column(Integer)

	hero_ids = Column(String)
	category = Column(String)


class Patch(Base):
	__tablename__ = 'patches'

	number = Column(String, primary_key=True)
	timestamp = Column(DateTime)
	dota_url = Column(String)
	custom_url = Column(String)
	wiki_url = Column(String)


class LocaleString(Base):
	__tablename__ = 'localestrings'

	id = Column(Integer, primary_key=True)
	table = Column(Unicode(255))
	row_id = Column(Integer, nullable=False)
	column = Column(String)
	lang = Column(String)
	value = Column(String)

	target = generic_relationship(table, row_id)

	def __repr__(self):
		return f"String: [{self.lang}]{self.table}.{self.row_id}.{self.column}"


# returns an open dotabase session
# if recreate is true, deletes any existing database first
def dotabase_session() -> Session:
	engine = create_engine('sqlite:///' + dotabase_db)
	Base.metadata.create_all(engine)
	return Session(engine)
