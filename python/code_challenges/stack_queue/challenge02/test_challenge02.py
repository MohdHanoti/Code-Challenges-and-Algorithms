# Write your test here
import pytest

from challenge02 import stack1

def test_valid_parentheses_01():
    actual=stack1.valid_parentheses("()")
    expected=True
    assert actual== expected

def test_valid_parentheses_02():
    actual=stack1.valid_parentheses("()[]{}")
    expected=True
    assert actual== expected

def test_valid_parentheses_03():
    actual=stack1.valid_parentheses("[({}]")
    expected=False
    assert actual== expected

def test_valid_parentheses_04():
    actual=stack1.valid_parentheses("[(hello)()]")
    expected=True
    assert actual== expected

def test_valid_parentheses_05():
    actual=stack1.valid_parentheses("[{(())}]")
    expected=True
    assert actual== expected

def test_valid_parentheses_06():
    actual=stack1.valid_parentheses("[{(()}]")
    expected=False
    assert actual== expected

def test_valid_parentheses_07():
    actual=stack1.valid_parentheses("")
    expected="empty string"
    assert actual== expected
