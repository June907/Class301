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
        #while the loop is not end
        while(temp):
            count+=1
            temp=temp.nextNode
        return count

    def append(self,item):
        temp=Node(item)
        if self.Node1 is None:
            self.Node1=temp
            return
        lastIndex=self.Node1
        #Find the last index
        while(lastIndex.nextNode):
            lastIndex=lastIndex.nextNode
        #After finding the last index that has an item, then change
        #that index item which is "None" to be the target item
        lastIndex.nextNode=temp

    def index(self,item):
        temp = self.Node1
        count=0
        while temp is not None:
            index=count
            count+=1
            if temp.data==item:
                return index
            temp=temp.nextNode

        return False

    def insert(self,pos,item):
        temp=self.Node1
        count=0
        while temp is not None:
            index=count
            count+=1
            if index==pos:
                temp.data=item
                return
            temp=temp.nextNode
        return False
        
        
        
        

            
    def printLL(self):
        temp=self.Node1
        while(temp):
            print (temp.data, end=" ")
            temp=temp.nextNode
            

LL = Linked_List()
LL.add(5)
LL.append(3)
LL.add(7)
LL.add(8)
LL.append(56)
print(LL.index(53))
LL.insert(2,87)
LL.printLL()








        
