class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class stack:
    def __init__(self):
        self.head=None

    def push(self, data): 
  
        if self.head is None: 
            self.head = Node(data) 
        else: 
            new_node = Node(data) 
            self.head.prev = new_node 
            new_node.next = self.head 
            new_node.prev = None
            self.head = new_node 

    def pop(self):
        if self.head is not None:
            newhead=self.head
            self.head=None
        return newhead.data
    
    def printStack(self,node):
        while(node is not None):
            print(node.data, end=" ")
            #last = node
            node= node.next
            

stack=stack()
stack.push(7)
stack.push(1)
stack.push(521)
#print(stack.pop())
stack.printStack(stack.head)


        
