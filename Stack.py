#Lab #10
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Steve D'Amico 
# Collaboration Statement:   I worked alone.           
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
#While temp returns true until temp=None, meaning there are no nodes left
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def __len__(self):
        count = 0
        temp = self.top
        while temp: 
            count += 1
            temp = temp.next
        return count
    
    def peek(self):
        return self.top.value

    def push(self,value):
        if self.top is None:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None: 
            return "Stack is empty"
        else:
            popped = self.top.value
            self.top = self.top.next
            return popped
            

