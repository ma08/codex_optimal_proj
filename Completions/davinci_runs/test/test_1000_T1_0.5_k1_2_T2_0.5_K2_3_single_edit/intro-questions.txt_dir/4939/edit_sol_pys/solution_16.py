
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode


    def printList(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def delete(self, index):
        curr_node = self.head
        if index == 0:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        count = 0
        while curr_node is not None and count != index:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None

    def length(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count

    def get(self, index):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            if count == index:
                return curr_node.data
            count += 1
            curr_node = curr_node.next
        return -1


def main():
    lines = sys.stdin.readlines()
    n, k = lines[0].split()
    n, k = int(n), int(k)
    commands = lines[1].split()

    ll = LinkedList()
    for i in range(n):
        ll.insert(i)

    curr_index = ll.length() - 1
    for i in range(k):
        command = commands[i]
        if command == "undo":
            m = int(commands[i+1])
            for j in range(m):
                ll.delete(curr_index)
            i += 1
            continue
        else:
            t = int(command)
            if t < 0:
                t = n + t
            curr_index = (curr_index - t) % ll.length()
    print(ll.get(curr_index))

if __name__ == '__main__':
    main()
