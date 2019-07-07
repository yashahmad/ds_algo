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

    def insert(self,val,index):
        count = 0
        

if __name__ == "__main__":
    sll = Linkedlist()
    sll.head = Node(1)
    sll.head.next = Node(2)
    sll.head.next.next = Node(4)
    sll.printlist()