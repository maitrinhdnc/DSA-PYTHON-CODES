class Node:
    def __init__(self, value):
        self.node = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head 
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, nodeVal):
        node = Node(nodeVal)
        node.next = node
        self.head = node
        self.tail = node 
        return "The CSLL has been created"

    def insertCSLL(self, nodeVal, pos):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(nodeVal)
            if pos == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif pos == -1:
                newNode.next = self.head 
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                temp = self.head
                while index < pos - 1:
                    temp = temp.next
                    index += 1
                newNode.next = temp.next
                temp.next = newNode

    def searchCSLL(self, nodeVal):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head 
            while tempNode:
                if tempNode.node == nodeVal:
                    return tempNode.node
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "There is not any node in this CSLL"

    def deleteCSLL(self, pos):
        if self.head is None:
            return 'The SLL does not exist'
        else:
            if pos == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail.next = self.head.next 
                    self.head = self.head.next
            elif pos == -1:
                temp = self.head 
                while temp:
                    if temp.next == self.tail:
                        break
                    temp = temp.next
                temp.next = self.head
                self.tail = temp
            else:
                index = 0
                temp = self.head 
                while index < pos - 1:
                    index += 1
                    temp = temp.next
                nextNode = temp.next
                temp.next = nextNode.next

    def deleteEntireCSLL(self):
        if self.head is None:
            return "No linked list to delete"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(2,0)
circularSLL.insertCSLL(4,0)
circularSLL.insertCSLL(4,-1)
circularSLL.insertCSLL(5,-1)
circularSLL.insertCSLL(3,0)
circularSLL.insertCSLL(5,-1)
circularSLL.insertCSLL(55,2)

print([node.node for node in circularSLL])
print(circularSLL.searchCSLL(10))
circularSLL.deleteCSLL(0)
circularSLL.deleteCSLL(-1)
circularSLL.deleteCSLL(2)
circularSLL.deleteEntireCSLL()

print([node.node for node in circularSLL])
