

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


def main():
    llist.add(1)
    llist.add(2)
    llist.add(3)
    llist.add(4)
    llist.add(5)
    llist.printList()


if __name__ == '__main__':
    main()
