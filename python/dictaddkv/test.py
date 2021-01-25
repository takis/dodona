from oplossing import dict_add_kv

def test1():
    x = {"Doom": 1993}
    expected = {"Doom": 1993, "Fortnite": 2017}
    assert dict_add_kv(x) == expected


def test2():
    x = {"Doom": 1993, "Quake": 1996}
    expected = {"Doom": 1993, "Quake": 1996, "Fortnite": 2017}
    assert dict_add_kv(x) == expected


def test3():
    x = {}
    expected = {"Fortnite": 2017}
    assert dict_add_kv(x) == expected


def test4():
    x = {"Fortnite": 2017}
    expected = {"Fortnite": 2017}
    assert dict_add_kv(x) == expected
