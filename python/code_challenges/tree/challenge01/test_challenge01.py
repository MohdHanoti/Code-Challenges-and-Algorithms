# Write your test here
from challenge01 import buildTree

def test_one():
    lst=[]
    tree=buildTree([3,9,20,15,7],[9,3,15,20,7])
    lst.append(tree.val)
    lst.append(tree.left.val)
    lst.append(tree.right.val)
    lst.append(None)
    lst.append(None)
    lst.append(tree.right.left.val)
    lst.append(tree.right.right.val)
    actual=lst
    expected=[3,9,20,None,None,15,7]
    assert actual==expected

def test_two():
    tree=buildTree([-1],[-1])
    actual=tree.val
    expected=-1
    assert actual==expected

def test_three():
    tree=buildTree([],[1])
    actual=tree
    expected=None
    assert actual==expected

def test_four():
    lst=[]
    tree=buildTree([3,9,1,2,20,15,7],[1,9,2,3,15,20,7])
    lst.append(tree.val)
    lst.append(tree.left.val)
    lst.append(tree.right.val)
    lst.append(tree.left.left.val)
    lst.append(tree.left.right.val)
    lst.append(tree.right.left.val)
    lst.append(tree.right.right.val)
    actual=lst
    expected=[3,9,20,1,2,15,7]

    assert actual==expected 
