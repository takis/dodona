from oplossing import dict_increment

def test1():
    assert dict_increment({"a": 1, "c": 100}) == {'a': 2, 'c': 101}

def test2():
    assert dict_increment({'jan': 83, 'piet': 77}) == {'jan': 84, 'piet': 78}
