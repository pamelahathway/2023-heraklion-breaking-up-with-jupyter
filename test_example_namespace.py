from example1_namespace import increase_by_one


def test_increase_by_one():
    variable = 1
    expected = 2
    actual = increase_by_one(variable)
    assert expected == actual
