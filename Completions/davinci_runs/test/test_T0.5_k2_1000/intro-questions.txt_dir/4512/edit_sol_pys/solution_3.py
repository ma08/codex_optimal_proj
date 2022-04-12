

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = Node()

        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def remove(self, data):
        if self.root is None:
            return
        if self.root.data == data:
            self.root = self.root.next
            self.size -= 1
            return
        curr = self.root
        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    def find(self, data):
        curr = self.root
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def print_list(self):
        curr = self.root
        while curr is not None:
            print(curr.data)
            curr = curr.next


def main():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.print_list()
    print()
    ll.remove(1)
    ll.remove(4)
    ll.remove(6)
    ll.print_list()



if __name__ == '__main__':
    main()
