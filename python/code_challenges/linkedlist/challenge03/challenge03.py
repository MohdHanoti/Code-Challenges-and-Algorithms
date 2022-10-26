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
        
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    
    def test_fun(self):
        """this is just for testing"""
        lst=[]

        current = self.head
        while current is not None:
            lst.append(current.value)
            current = current.next
        return lst
    
    def delete_nth_from_end(self,n):
        """this function will delete the nth number from the end"""
        current=self.head
        index=0
        while current is not None:
            prev=current
            current=current.next
            index+=1
        if index==0:
            return "linked list is empty"
        elif index==1 and n==1:
             self.head=None
             return "linked list had one node and now its embty"        
        n_node=index-n
        if n_node<0:
            return f"The linked list has {index} nodes, enter a number within this range"
        current=self.head
        index=0
        prev=None
        while current:
            if current.next is None:
                prev.next=None
                break

            if index == n_node:
                current.value=current.next.value
                current.next=current.next.next
                
                break
            prev=current
            current=current.next
            
            index+=1              
        return self
    

            


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

updated=linkedList1.delete_nth_from_end(1)
print(updated)
linkedList1.printAll()



     
