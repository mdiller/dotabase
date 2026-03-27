# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

**Dotabase** is a Python package that bundles a SQLite database of Dota 2 game data along with SQLAlchemy ORM models. It's distributed via PyPI so other projects can `pip install dotabase` and query Dota 2 heroes, abilities, items, responses, etc. The database is built separately by the `dotabase-builder` project (not in this repo).

## Key Commands

**Rebuild the SQLite DB from the SQL dump:**
```sh
sqlite3 dotabase/dotabase.db ".read dotabase/dotabase.db.sql"
```

**Dump the DB to SQL (for version control):**
```sh
sqlite3 dotabase/dotabase.db ".dump" > dotabase/dotabase.db.sql
```

**Bump version (auto-increments patch if VERSION not already changed):**
```sh
bash bumpversion.sh
```

**Build and publish to PyPI:**
```sh
bash pypi.sh
```
This also SSHs to `dillerm.io` to update the production server and restarts dependent services (MangoByte, dotabase-web, vue.dotabase.dillerm.io).

**Type checking:**
```sh
mypy dotabase/
```

## Architecture

All ORM models live in `dotabase/dotabase.py`. The `dotabase/__init__.py` re-exports everything. Consumers use the package like:

```python
from dotabase import *
session = dotabase_session()
for hero in session.query(Hero):
    print(hero)
```

**Main ORM models:**
- `Hero` — stats, attributes, relationships to abilities/talents/facets/responses/voice
- `Ability` — spells with cooldowns, Aghanim scepter/shard upgrades, behavior flags
- `Facet` / `FacetAbilityString` — hero facet system (modifies ability descriptions per facet)
- `Talent` — talent tree entries linked to heroes
- `Item` — purchasable items
- `Voice` — voice actor info tied to heroes
- `Response` / `Criterion` — hero vocal response system with matching criteria and MP3 paths
- `Emoticon` / `ChatWheelMessage` — chat emoticons and chat wheel data
- `LoadingScreen` — loading screen images with HSV/RGB color analysis
- `Patch` — patch history with timestamps
- `LocaleString` — localized text for all entities (generic relationship via `table`/`row_id`)

**`json/` directory** — auto-generated JSON snapshots of all major tables, used for reference and by downstream projects. Per-hero response data lives in `json/responses/`.

## Dependent Projects

- **MangoByte** — Discord bot (`/c/dev/projects/MangoByte`)
- **vue.dotabase.dillerm.io** — Vue frontend (deployed via Docker on dillerm.io)
- **dotabase-web** / **old-dotabase-web** — older web interfaces on dillerm.io
- **dotabase-builder** — separate project that extracts data from Dota 2 VPK files and builds the DB

## Versioning

- `VERSION` — Python package version (e.g. `7.8.6`), format `<dota_major>.<dota_minor>.<package_patch>`
- `DOTA_VERSION` — shields.io badge JSON tracking the current Dota patch (e.g. `7.40c`)
