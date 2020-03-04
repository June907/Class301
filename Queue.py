class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Quenue:
    def __init__(self):
        self.head=None

    def enqueue(self,item):
        temp=Node(item)
        if self.head is None:
            self.head=temp
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=temp
        temp.prev=last

    def dequeue(self):
        if self.head is None:
            return "The list is empty"
        temp=self.head
        self.head=self.head.next
        
        return temp.data 

    def print(self,node):
        while(node is not None):
            print(node.data, end=" ")
            last = node
            node= node.next

q=Quenue()

q.enqueue(5)
q.enqueue(2)
q.print((q.head))
        
