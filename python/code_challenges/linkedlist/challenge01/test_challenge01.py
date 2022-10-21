# Write your test here
import pytest 
from challenge01 import Node , linkedlist

def test_append():
    run=run_fun()
    actual=run.test_fun()
    expected=["A","B","C","D","E"]
    assert actual==expected

def test_delete1():
    run=run_fun()
    run.delete("A")

    actual=run.test_fun()
    expected=["B","C","D","E"]
    assert actual==expected

def test_delete2():
    run=run_fun()
    run.delete("C")

    actual=run.test_fun()
    expected=["A","B","D","E"]
    assert actual==expected

def test_delete3():
    run=run_fun()
    
    actual=run.delete("AC")
    expected="Value not found"
    assert actual==expected




def run_fun():
    linkedList1 = linkedlist()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    node5 = Node("E")
    linkedList1.append(node5)
    return linkedList1
    