from oplossing import BMI

def test1():
    result = BMI(67, 1.83).bmi()
    expected = 20
    assert result == expected


def test2():
    result = BMI(66, 1.83).bmi()
    expected = 19.7
    assert result == expected


def test3():
    result = BMI(96, 1.83).bmi()
    expected = 28.7
    assert result == expected


def test4():
    result = BMI(78, 1.835).bmi()
    expected = 23.2
    assert result == expected

