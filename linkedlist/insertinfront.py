class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insertinfornt(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

if __name__ == "__main__":
    sll = Linkedlist()
    sll.head = Node(3)
    sll.head.next = Node(4)
    sll.printlist()
    sll.insertinfornt(2)
    sll.insertinfornt(1)
    sll.printlist()