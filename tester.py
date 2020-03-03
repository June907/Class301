# A linked list node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
  
# Class to create a Doubly Linked List 
class DoublyLinkedList: 
  
    # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None
  
    # Given a reference to the head of a list and an 
    # integer, inserts a new node on the front of list 
    def push(self, new_data): 
  
        # 1. Allocates node 
        # 2. Put the data in it 
        new_node = Node(new_data) 
  
        # 3. Make next of new node as head and 
        # previous as None (already None) 
        new_node.next = self.head 
  
        # 4. change prev of head node to new_node 
        if self.head is not None: 
            self.head.prev = new_node 
  
        # 5. move the head to point to the new node 
        self.head = new_node
    def printList(self, node): 
  
        print ("\nTraversal in forward direction")
        while(node is not None): 
            print (" % d" %(node.data)), 
            last = node 
            node = node.nextNode
  
        print ("\nTraversal in reverse direction")
        while(last is not None): 
            print (" % d" %(last.data)), 
            last = last.prev
D=Node(8)
print(D.prev)
