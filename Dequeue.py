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
            self.head = Node(item) 
        else: 
            new_node = Node(item) 
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

    def removeRear(self):
        
        while(self.head.next is not None):
            self.head=self.head.next
        temp=self.head
        self.head=None
        return temp.data

    def print(self,node):
        while(node is not None):
            print(node.data, end=" ")
            last = node
            node= node.next

de=Deque()
de.addFront(5)
de.addFront(7)
de.addFront(9)
de.print(de.head)

de.removeRear()
de.print(de.head)
        
        
