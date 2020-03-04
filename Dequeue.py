class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
        self.head=None

    def addFront(self,item):
          
        if self.head is None: 
            self.head = Node(data) 
        else: 
            new_node = Node(data) 
            self.head.prev = new_node 
            new_node.next = self.head 
            new_node.prev = None
            self.head = new_node

    def addRear(self,item):
        temp=Node(item)
        if self.head is None:
            self.head=temp
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=temp
        temp.prev=last

    def removeFront(self):
        if self.head is None:
            return "The list is empty"
        temp=self.head
        self.head=self.head.next
        
        return temp.data
        
        
