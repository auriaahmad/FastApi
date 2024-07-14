# fake/explorer.py
from typing import List, Union
from model.explorer import Explorer

# fake data, replaced in Chapter 10 by a real database and SQL
_explorers = [
    Explorer(name="Claude Hande auria ahmad", country="FR", description="Scarce during full moons"),
    Explorer(name="Noah Weiser", country="DE", description="Myopic machete man"),
]

def get_all() -> List[Explorer]:
    """Return all explorers"""
    return _explorers

def get_one(name: str) -> Union[Explorer, None]:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorers list:
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer

def delete(name: str) -> bool:
    """Delete an explorer; return None if it existed"""
    return None