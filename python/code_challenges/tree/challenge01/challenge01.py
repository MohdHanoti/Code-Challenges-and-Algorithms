# Write here the code challenge solution
class TreeNode:
    '''this class will initialize the tree'''
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def buildTree( preorder, inorder):
    '''this function will build the tree'''
    if len(preorder)==0 or  len(inorder)==0:
        return None
    
    root=TreeNode(preorder[0])
    mid=inorder.index(preorder[0])
    root.left= buildTree(preorder[1:mid+1],inorder[:mid])
    root.right=buildTree(preorder[mid + 1:],inorder[mid + 1:])
    return root


