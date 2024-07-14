from data.creature import create, get_one, get_all, modify, delete
from model.creature import Creature

sample = Creature(name="Yeti", country="CN", area="Himalayas", description="Hirsute Himalayan", aka="Abominable Snowman")

def test_create():
    create(sample)
    resp = get_one("Yeti")
    assert resp == sample

def test_get_all():
    resp = get_all()
    assert len(resp) > 0

def test_modify():
    modified = Creature(name="Yeti", country="CN", area="Himalayas", description="Hairy Himalayan", aka="Abominable Snowman")
    modify(modified)
    resp = get_one("Yeti")
    assert resp.description == "Hairy Himalayan"

def test_delete():
    delete(sample)
    resp = get_one("Yeti")
    assert resp is None