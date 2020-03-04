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
        if self.head is None:
            return "The list is empty"
        temp=self.head
        self.head=self.head.next
        
        return temp.data 

    def peek(self):
        if self.head is not None:
            return self.head.data
        
    def isEmpty(self):
        if self.head is None:
            return "The list is empty"
        else:
            return False
        
    def size(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count

        
    
    def printStack(self,node):
        while(node is not None):
            print(node.data, end=" ")
            last = node
            node= node.next
            

stack=stack()
stack.push(7)
stack.push(1)
stack.push(521)
stack.printStack(stack.head)
#print(stack.peek())
print(stack.isEmpty())
print(stack.size())






        
