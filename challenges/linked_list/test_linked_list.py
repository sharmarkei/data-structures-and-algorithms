import pytest
from linked_list import linked_list


def test_one():
  expected = 2
  actual = linked_list.incl('HELLO')
  assert actual == expected