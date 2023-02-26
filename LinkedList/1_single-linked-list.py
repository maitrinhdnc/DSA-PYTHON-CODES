class Node:
    def __init__(self, value):
        self.node = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertNode(self, val, pos):
        new_node = Node(val)
        temp = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            elif pos == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                index = 1
                while index < pos:
                    index += 1
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.node, end = ' ')
            temp = temp.next
        print()

    def search1stNode(self, value):
            temp = self.head
            pos_lst = []
            if self.head is None: 
                return pos_lst
            else:
                pos = 0
                while(temp):
                    if temp.node == value:
                        pos_lst.append(pos)
                    pos += 1
                    temp = temp.next
            if len(pos_lst) == 0:
                print("No node was found")
            else:
                print(f"Node was found at positon: {pos_lst}th")

    def deleteNode(self, pos):
        if self.head is None:
            return 'The SLL does not exits'
        else:
            if pos == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif pos == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    temp.next = None 
                    self.tail = temp
            else:
                index = 0
                


    def deleteEntireLinkedList(self):
        if self.head is None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None

slinkedlist = SLinkedList()

slinkedlist.insertNode(1, -1)
slinkedlist.insertNode(2, -1)
slinkedlist.insertNode(3, -1)
slinkedlist.insertNode(4, -1)
slinkedlist.insertNode(0, 0)
slinkedlist.insertNode(5, 4)

slinkedlist.printLinkedList()
# slinkedlist.deleteEntireLinkedList()
slinkedlist.search1stNode(4)
slinkedlist.deleteNode(0)
slinkedlist.printLinkedList()
slinkedlist.deleteNode(-1)
slinkedlist.printLinkedList()


