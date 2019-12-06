import pytest
from linked_list import insert

def test_one():
  expected = 1
  actual = insert(1)
  assert actual == expected