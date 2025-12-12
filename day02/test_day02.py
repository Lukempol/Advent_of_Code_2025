import pytest
from day02pt1 import is_invalid
from day02pt2 import is_valid_v2

@pytest.mark.parametrize('id, answer', [
    (11, True),
    (1234, False),
    (1212, True),
    (1010, True),
    (1188511885, True),
    (222222, True),
    (2222222, False),
    (446446, True),
    (38593859, True),
    (123456, False),
    (1213124512, False),
    (79584683, False),
])

def test_is_invalid(id, answer):    
    assert is_invalid(id) == answer

@pytest.mark.parametrize('id, answer', [
    (11, True),
    (1234, False),
    (1212, True),
    (1010, True),
    (1188511885, True),
    (222222, True),
    (2222222, False),
    (446446, True),
    (38593859, True),
    (123456, False),
    (1213124512, False),
    (79584683, False),
])

def test_is_valid_v2(id, answer):    
    assert is_valid_v2(id) == answer