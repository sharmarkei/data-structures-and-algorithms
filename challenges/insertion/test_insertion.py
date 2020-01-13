""" 
*******************************
WORKED WITH CHARLIE ON SOLUTION
*******************************
"""

from insertion import insertion

def test_unique_values():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertion(lst)
    assert actual == expected

def test_duplicate_value():
    lst = [8,4,23,42,16,15,8,23]
    expected = [4,8,8,15,16,23,23,42]
    actual = insertion(lst)
    assert actual == expected

def test_negative_values():
    lst = [8,4,23,-42,16,-15]
    expected = [-42,-15,4,8,16,23]
    actual = insertion(lst)
    assert actual == expected
