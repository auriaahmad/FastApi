from .init import curs
from model.explorer import Explorer

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict()

def get_one(name: str) -> Explorer:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer) -> Explorer:
    qry = "INSERT INTO explorer (name, country, description) VALUES (:name, :country, :description)"
    params = model_to_dict(explorer)
    curs.execute(qry, params)
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """UPDATE explorer SET
        country=:country,
        description=:description
        WHERE name=:name"""
    params = model_to_dict(explorer)
    curs.execute(qry, params)
    return get_one(explorer.name)

def delete(explorer: Explorer) -> bool:
    qry = "DELETE FROM explorer WHERE name = :name"
    params = {"name": explorer.name}
    curs.execute(qry, params)
    return curs.rowcount > 0