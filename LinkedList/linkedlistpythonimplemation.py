class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        

myLinkedList = LinkedList()
myNode = Node(10)
myNode1 = Node(20)
myNode2 = Node(30)
myNode3 = Node(40)
myNode4 = Node(50)
myLinkedList.head = myNode
myNode.next=myNode1
myNode1.next = myNode2
myNode2.next = myNode3
myNode3.next = myNode4

print("The elements in the linked list are:")

print(myLinkedList.head.data, end=" ")
print(myLinkedList.head.next.data, end=" ")
print(myLinkedList.head.next.next.data, end=" ")
print(myLinkedList.head.next.next.next.data)