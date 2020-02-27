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
        while temp is not None:
            if temp.data==item:
                break
            prev=temp
            temp=temp.nextNode
        if temp==None:
            return
        prev.nextNode = temp.nextNode
        temp= None

    def search(self,item):
        temp = self.Node1
        while temp is not None:
            if temp.data==item:
                return True
            temp=temp.nextNode
        return False

    def isEmpty(self):
        
        if self.Node1 is not None:
            return False
        else:
            return True

    def size(self):
        temp= self.Node1
        count=0
        while temp.data is not None:
                count+=1
                temp.data=temp.nextNode
                if temp.nextNode is None:
                    break
                
        print (count)
        return
                
        

            

        
        
    def printLL(self):
        printNode=self.Node1
        while printNode is not None:
            print (printNode.data)
            printNode=printNode.nextNode

LL = Linked_List()
if LL.isEmpty():
    print("True")
else:
    print("False")
LL.add(3)
LL.add(4)
LL.add(5)

LL.printLL()
if LL.search(4):
    print("True")
else:
    print("False")
if LL.isEmpty():
    print("True")
else:
    print("False")
LL.size()


LL.remove(4)
LL.printLL()
if LL.search(4):
    print("True")
else:
    print("False")





        
