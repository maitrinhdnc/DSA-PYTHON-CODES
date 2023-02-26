class Node:
    def __init__(self, value):
        self.node = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head 
        while temp:
            yield temp
            temp = temp.next

    def createDLL(self, nodeVal):
        node = Node(nodeVal)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "the DLL is created"

doubleLL = DoubleLinkedList()
doubleLL.createDLL(3)
print([node.node for node in doubleLL])