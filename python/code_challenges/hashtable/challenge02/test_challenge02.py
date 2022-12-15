from challenge02 import find_first_repeated_word
import pytest

def test1_find_first_repeated_word():
    expected = "ASAC"
    actual = find_first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
    assert actual == expected

def test2_find_first_repeated_word():
    expected = "No Repetition"
    actual = find_first_repeated_word("I am learning programming at ASAC.")
    assert actual == expected

def test3_find_first_repeated_word():
    expected = "Python"
    actual = find_first_repeated_word("Python is the best language in programming. I am learning Python at ASAC")
    assert actual == expected

def test4_find_first_repeated_word():
    expected = "No Repetition"
    actual = find_first_repeated_word("My name is Mohammad")
    assert actual == expected