# Write your test here
import pytest
from challenge01 import MyQueue

def test_push():
    Queue1 = MyQueue()
    Queue1.push(1)
    Queue1.push(2)
    Queue1.push(3)
    Queue1.push(4)
    expected = 1
    actual = Queue1.peek()
    assert actual == expected

def test_pop():
    Queue1 = MyQueue()
    Queue1.push(1)
    Queue1.push(2)
    Queue1.push(3)
    Queue1.push(4)
    expected = 1
    actual = Queue1.pop()
    assert actual == expected


def test_empty1():
    Queue1 = MyQueue()

    Queue1.push(1)
    Queue1.push(2)
    Queue1.push(3)
    Queue1.push(4)
    expected = False
    actual = Queue1.empty()
    assert actual == expected

def test_empty2():
    Queue1 = MyQueue()

    Queue1.push(1)
    Queue1.pop()
    expected = True
    actual = Queue1.empty()
    assert actual == expected