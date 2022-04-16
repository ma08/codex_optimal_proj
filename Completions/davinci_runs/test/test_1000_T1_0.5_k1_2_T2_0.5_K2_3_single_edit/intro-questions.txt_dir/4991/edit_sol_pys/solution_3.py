

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert(self, new_node, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next
                counter += 1
        elif position == 1:
            new_node.next = self.head
            self.head = new_node

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def print(self):
        printval = self.head
        while printval:
            print(printval.value)
            printval = printval.next




llist = LinkedList()
llist.append(Node(1))
llist.append(Node(2))
llist.append(Node(3))
llist.append(Node(4))

llist.print()

llist.insert(Node(5), 3)

llist.print()

llist.delete(2)

llist.print()

llist.reverse()

llist.print()
