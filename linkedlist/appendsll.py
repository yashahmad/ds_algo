class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        temp = self.head
        while temp:
            temp = temp.next
        new_node = Node(data)
        temp = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    sll = Linkedlist()
    sll.head = Node(1)
    sll.printlist()