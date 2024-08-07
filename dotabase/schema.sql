CREATE TABLE heroes (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	full_name VARCHAR, 
	media_name VARCHAR, 
	localized_name VARCHAR, 
	real_name VARCHAR, 
	aliases VARCHAR, 
	roles VARCHAR, 
	role_levels VARCHAR, 
	hype VARCHAR, 
	bio VARCHAR, 
	image VARCHAR, 
	icon VARCHAR, 
	portrait VARCHAR, 
	color VARCHAR, 
	legs INTEGER, 
	team VARCHAR, 
	base_health_regen FLOAT, 
	base_mana_regen FLOAT, 
	base_movement INTEGER, 
	base_attack_speed INTEGER, 
	turn_rate FLOAT, 
	base_armor INTEGER, 
	attack_range INTEGER, 
	attack_projectile_speed INTEGER, 
	attack_damage_min INTEGER, 
	attack_damage_max INTEGER, 
	attack_rate FLOAT, 
	attack_point FLOAT, 
	attr_primary VARCHAR, 
	attr_strength_base INTEGER, 
	attr_strength_gain FLOAT, 
	attr_intelligence_base INTEGER, 
	attr_intelligence_gain FLOAT, 
	attr_agility_base INTEGER, 
	attr_agility_gain FLOAT, 
	vision_day INTEGER, 
	vision_night INTEGER, 
	magic_resistance INTEGER, 
	is_melee BOOLEAN, 
	material VARCHAR, 
	json_data VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE items (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	localized_name VARCHAR, 
	aliases VARCHAR, 
	quality VARCHAR, 
	icon VARCHAR, 
	cost INTEGER, 
	cooldown VARCHAR, 
	cast_range VARCHAR, 
	health_cost VARCHAR, 
	mana_cost VARCHAR, 
	duration VARCHAR, 
	base_level INTEGER, 
	description VARCHAR, 
	lore VARCHAR, 
	secret_shop BOOLEAN, 
	neutral_tier VARCHAR, 
	ability_special VARCHAR, 
	recipe VARCHAR, 
	shop_tags VARCHAR, 
	json_data VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE criteria (
	name VARCHAR NOT NULL, 
	pretty VARCHAR, 
	matchkey VARCHAR, 
	matchvalue VARCHAR, 
	weight FLOAT, 
	required BOOLEAN, 
	PRIMARY KEY (name)
);
CREATE TABLE emoticons (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	url VARCHAR, 
	frames INTEGER, 
	ms_per_frame INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE chatwheelmessages (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	message VARCHAR, 
	label VARCHAR, 
	sound VARCHAR, 
	image VARCHAR, 
	all_chat BOOLEAN, 
	category VARCHAR, 
	source VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE loadingscreens (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	image VARCHAR, 
	thumbnail VARCHAR, 
	creation_date DATE, 
	color VARCHAR, 
	hue INTEGER, 
	saturation INTEGER, 
	value INTEGER, 
	hero_ids VARCHAR, 
	category VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE patches (
	number VARCHAR NOT NULL, 
	timestamp DATETIME, 
	dota_url VARCHAR, 
	custom_url VARCHAR, 
	wiki_url VARCHAR, 
	PRIMARY KEY (number)
);
CREATE TABLE localestrings (
	id INTEGER NOT NULL, 
	"table" VARCHAR(255), 
	row_id INTEGER NOT NULL, 
	"column" VARCHAR, 
	lang VARCHAR, 
	value VARCHAR, 
	PRIMARY KEY (id)
);
CREATE TABLE abilities (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	hero_id INTEGER, 
	behavior VARCHAR, 
	damage_type VARCHAR, 
	spell_immunity VARCHAR, 
	target_team VARCHAR, 
	dispellable VARCHAR, 
	cast_range VARCHAR, 
	cast_point VARCHAR, 
	channel_time VARCHAR, 
	cooldown VARCHAR, 
	duration VARCHAR, 
	damage VARCHAR, 
	health_cost VARCHAR, 
	mana_cost VARCHAR, 
	charges VARCHAR, 
	ability_special VARCHAR, 
	slot INTEGER, 
	icon VARCHAR, 
	localized_name VARCHAR, 
	description VARCHAR, 
	lore VARCHAR, 
	note VARCHAR, 
	scepter_grants BOOLEAN, 
	scepter_upgrades BOOLEAN, 
	scepter_description VARCHAR, 
	shard_grants BOOLEAN, 
	shard_upgrades BOOLEAN, 
	shard_description VARCHAR, 
	json_data VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hero_id) REFERENCES heroes (id)
);
CREATE TABLE voices (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	icon VARCHAR, 
	image VARCHAR, 
	url VARCHAR, 
	media_name VARCHAR, 
	voice_actor VARCHAR, 
	hero_id INTEGER, 
	criteria VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hero_id) REFERENCES heroes (id)
);
CREATE TABLE talents (
	hero_id INTEGER, 
	ability_id INTEGER NOT NULL, 
	slot INTEGER, 
	linked_abilities VARCHAR, 
	PRIMARY KEY (hero_id, ability_id), 
	FOREIGN KEY(hero_id) REFERENCES heroes (id), 
	FOREIGN KEY(ability_id) REFERENCES abilities (id)
);
CREATE TABLE responses (
	name VARCHAR, 
	fullname VARCHAR NOT NULL, 
	mp3 VARCHAR, 
	hero_id INTEGER, 
	voice_id INTEGER, 
	text VARCHAR, 
	text_simple VARCHAR, 
	criteria VARCHAR, 
	pretty_criteria VARCHAR, 
	PRIMARY KEY (fullname), 
	FOREIGN KEY(hero_id) REFERENCES heroes (id), 
	FOREIGN KEY(voice_id) REFERENCES voices (id)
);
