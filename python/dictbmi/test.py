from oplossing import dict_bmi

def test1():
    x = {"Jan": {"gewicht": 79, "lengte": 1.89},"Piet": {"gewicht": 85, "lengte": 1.80},}
    expected = {"Jan": 22.1, "Piet": 26.2}
    assert dict_bmi(x) == expected


def test2():
    x = {"Jan": {"gewicht": 66, "lengte": 1.83}}
    expected = {"Jan": 19.7}
    assert dict_bmi(x) == expected


def test3():
    x = {"Jan": {"gewicht": 96, "lengte": 1.83}}
    expected = {"Jan": 28.7}
    assert dict_bmi(x) == expected


def test4():
    x = {"Jan": {"gewicht": 78, "lengte": 1.835}}
    expected = {"Jan": 23.2}
    assert dict_bmi(x) == expected

