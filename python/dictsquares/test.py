from oplossing import dict_squares

def test1():
    assert dict_squares([1, 2, 3]) == {1: 1, 2: 4, 3: 9}

def test2():
    assert dict_squares([0, 4, 9]) == {0: 0, 4: 16, 9: 81}
