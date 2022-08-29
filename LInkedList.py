

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode 
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    
    def headInsert(self, newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp
        
    def listLength(self):
        currentNode = self.head
        length = 0 
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
        
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True: 
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
        
    def insertAt(self, newNode, position):
        if position < 0 or position >= self.listLength():
            print("Error in position")
            return
        if position == 0 :
            self.headInsert(newNode)
        currentNode = self.head
        currentPosition =0
        while True: 
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition = currentPosition + 1
            
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next= None
    
firstNode = Node(2)
linkedList= LinkedList()
linkedList.insert(firstNode)

secondNode = Node(4)
linkedList.insert(secondNode)


thirdNode = Node(5)
linkedList.headInsert(thirdNode)

forthNode = Node(8)

linkedList.insertAt(forthNode,2)

linkedList.deleteEnd()
linkedList.printList()
