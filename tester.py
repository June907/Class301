LL = Linked_List()
if LL.isEmpty():
    print("True, the list is empty")
else:
    print("False, the list is not empty")
LL.add(3)
LL.add(4)
LL.add(5)

LL.printLL()
if LL.search(4):
    print("True, target is in the list")
else:
    print("False, target is not in the list")
if LL.isEmpty():
    print("True, the list is empty")
else:
    print("False, the list is not empty")
print("The length of the list is "+str(LL.size()))

LL.remove(4)
LL.printLL()
if LL.search(4):
    print("True, target is in the list")
else:
    print("False, target is not in the list")
