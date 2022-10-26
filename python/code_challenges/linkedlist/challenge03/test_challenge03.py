# Write your test here
import pytest 
from challenge03 import Node , linkedlist
def run():
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
linkedList1=run()
def test_append():
    
    actual=linkedList1.test_fun()
    expected=["A","B","C","D","E"]
    assert actual==expected

def test_Delete_nth_from_end_1():
    linkedList1.delete_nth_from_end(1)
    actual=linkedList1.test_fun()
    expected=["A","B","C","D"]
    assert actual==expected

def test_Delete_nth_from_end_2():
    linkedList1.delete_nth_from_end(2)
    actual=linkedList1.test_fun()
    expected=["A","B","D"]
    assert actual==expected

def test_Delete_nth_from_end_3():
    linkedList1.delete_nth_from_end(3)
    actual=linkedList1.test_fun()
    expected=["B","D"]
    assert actual==expected

def test_Delete_nth_from_end_4():
    linkedList1.delete_nth_from_end(1)
    actual=linkedList1.test_fun()
    expected=["B"]
    assert actual==expected

def test_Delete_nth_from_end_5():
    
    actual=linkedList1.delete_nth_from_end(2)
    expected="The linked list has 1 nodes, enter a number within this range"
    assert actual==expected

def test_Delete_nth_from_end_6():
    
    actual=linkedList1.delete_nth_from_end(1)
    expected="linked list had one node and now its embty" 
    assert actual==expected

def test_Delete_nth_from_end_7():
    
    actual=linkedList1.delete_nth_from_end(2)
    expected="linked list is empty"
    assert actual==expected