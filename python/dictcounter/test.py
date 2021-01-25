from oplossing import dict_eyecolor_counter

def test1():
    assert dict_eyecolor_counter(["bruin", "bruin"]) == {'bruin': 2, 'blauw': 0}


def test2():
    assert dict_eyecolor_counter(["bruin", "blauw"]) == {'bruin': 1, 'blauw': 1}


def test3():
    assert dict_eyecolor_counter(["bruin", "blauw", "bruin"]) == {'bruin': 2, 'blauw': 1}


def test4():
    assert dict_eyecolor_counter([]) == {'bruin': 0, 'blauw': 0}

