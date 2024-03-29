class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    sll = Linkedlist()
    sll.head = Node(1)
    sll.head.next = Node(2)
    sll.printlist()
    sll.append(3)
    sll.append(4)
    sll.printlist()