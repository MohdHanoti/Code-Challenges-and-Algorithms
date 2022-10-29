# Write here the code challenge solution

class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue


class Stack:
    global_size=0
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        """this function will push the value to the stack"""
        node=Node(value)

        if self.top:
            node.next=self.top
        self.top=node
        self.size+=1
        Stack.global_size+=1

    def pop(self):
        """this function will pop the last element from stack"""
        if self.top:
            temp=self.top
            self.top=self.top.next
            self.size -= 1
            Stack.global_size-=1
            return temp.value
        else :
            return "This stack is empty"    

    def peek(self):
        """this will return the last element of stack"""
        if self.top:
            
            return self.top.value
        else :
            return "This stack is empty"    

    def is_empty(self):
        """this will check if the stack is empty"""
        return self.size == 0

    def get_size(self):
        """this will get the size of the stack"""
        return self.size

class MyQueue():
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def push(self,value):
        """this will push to myQueue"""
        while self.stack2.top:
            self.stack1.push(self.stack2.pop())

        self.stack1.push(value)

        while self.stack1.top:
            self.stack2.push(self.stack1.pop())

    def pop(self):
        """this will pop the last element of myQueue"""
        return self.stack2.pop()

    def peek(self):
        """this will get the last element of myQueue"""
        return self.stack2.peek()

    def empty(self):
        """this will check if myQueue is empty"""

        return self.stack2.is_empty()                

if __name__ == "__main__":
    myQueue=MyQueue()
    myQueue.push("A")
    myQueue.push("B")
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.peek())
    print(myQueue.empty())