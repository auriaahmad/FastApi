from .init import conn, curs
from model.creature import Creature
from typing import Optional

curs.execute("""create table if not exists creature(
    name text primary key,
    description text,
    country text,
    area text,
    aka text)""")

def row_to_model(row: Optional[tuple]) -> Optional[Creature]:
    if row:
        name, description, country, area, aka = row
        return Creature(name=name, description=description, country=country, area=area, aka=aka)
    return None

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Optional[Creature]:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]

def create(creature: Creature) -> Creature:
    qry = "insert into creature values (:name, :description, :country, :area, :aka)"
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return get_one(creature.name)

def modify(creature: Creature) -> Creature:
    qry = """update creature set
        country=:country,
        description=:description,
        area=:area,
        aka=:aka
        where name=:name"""
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return get_one(creature.name)

def delete(creature: Creature) -> bool:
    qry = "delete from creature where name=:name"
    params = {"name": creature.name}
    curs.execute(qry, params)
    return curs.rowcount > 0
