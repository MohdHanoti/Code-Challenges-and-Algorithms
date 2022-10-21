# Write here the code challenge solution
class Node:
    """This class creates the node """
    def __init__(self,value):
        self.value=value
        self.next= None

class linkedlist:
    """this class append and delete a node"""
    def __init__(self):
        self.head=None

    def append(self,node):
        """this is responseble to append a node"""
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = node         
    
    def printAll(self):
        """this is for printing"""
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def delete(self,node):
        """this is responseble to delete a node"""

        current=self.head
        if (current is not None):
            if (current.value == node):
                self.head = current.next
                
                return
        while(current is not None):
            if current.value == node:
                break
            prev = current
            current = current.next
        if current==None:
            print("Value not found")
            return ("Value not found") 

        prev.next = current.next
 
        current = None
    def test_fun(self):
        """this is for testing"""
        lst=[]
        if self.head is None:
            return"The linked list is empty"
        else:
            current = self.head
            while current is not None:
                lst.append(current.value)
                current = current.next
        return lst



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

linkedList1.delete("D")

linkedList1.printAll()        
