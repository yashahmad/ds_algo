class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    sll = Linkedlist()
    sll.head = Node(2)
    sll.head.next = Node(3)
    sll.head.next.next = Node(4)

