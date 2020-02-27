class Node:
    def __init__(self,idata):
        self.data=idata
        self.nextNode = None

    def setdata(self,idata):
        self.data = idata

    def getdata(self):
        return self.data

    def setnextnode(self,inode):
        self.nextNode = inode

class Linked_List:
    def __init__(self):
        self.Node1 = None

    def add(self,item):
        newNode = Node(item)
        
        newNode.nextNode=self.Node1
        self.Node1=newNode

    def remove(self,item):
        temp = self.Node1
        if temp is not None:
            if temp.data==item:
                self.Node1=temp.next
                temp=none
                return
        while(temp is not None):
            if temp.data==item:
                prev=temp
                temp=temp.next
        if temp==None:
            return
        prev.next = temp.next
        temp= None

        
        
    def printLL(self):
        printNode=self.Node1
        while printNode is not None:
            print(printNode.data)
            printNode=printNode.nextNode

LL = Linked_List()
LL.add(3)
LL.add(4)
LL.add(5)

LL.printLL()
LL.remove(4)
LL.printLL()
        
