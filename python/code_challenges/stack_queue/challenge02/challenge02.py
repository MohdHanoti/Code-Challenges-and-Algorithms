# Write here the code challenge solution

class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue


class Stack:
    
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
        

    def pop(self):
        """this function will pop the last element from stack"""
        if self.top:
            temp=self.top
            self.top=self.top.next
            self.size -= 1
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
    
    def valid_parentheses(self,s):
        '''this method determine if the input string is valid Parentheses'''
        parentheses={'(':')','[':']','{':'}'}
        for symbol in s:
            if symbol in parentheses.keys():
                self.push(symbol)
                

            elif symbol in parentheses.values():
                if parentheses[self.top.value] == symbol:
                    self.pop()
                else:
                    return False    
                          
        return True

stack1= Stack()
print(stack1.valid_parentheses("[({}]"))
print(stack1.valid_parentheses("()[]{}"))
print(stack1.valid_parentheses("[{(())}]"))
print(stack1.valid_parentheses("[(hello)()]"))
