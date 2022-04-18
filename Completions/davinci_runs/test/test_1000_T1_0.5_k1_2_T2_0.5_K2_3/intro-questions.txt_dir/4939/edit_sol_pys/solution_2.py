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
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def printList(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data)
            currNode = currNode.next

    def delete(self, index):
        currNode = self.head
        if index == 0:
            self.head = currNode.next
            currNode = None
            return

        prevNode = None
        count = 0
        while currNode is not None and count != index:
            prevNode = currNode
            currNode = currNode.next
            count += 1

        if currNode is None:
            return

        prevNode.next = currNode.next
        currNode = None

    def length(self):
        currNode = self.head
        count = 0
        while currNode is not None:
            count += 1
            currNode = currNode.next
        return count

    def get(self, index):
        currNode = self.head
        count = 0
        while currNode is not None:
            if count == index:
                return currNode.data
            count += 1
            currNode = currNode.next
        return -1


def main():
    lines = sys.stdin.readlines()
    n, k = lines[0].split(' ')
    n, k = int(n), int(k)
    commands = lines[1].split(' ')

    ll = LinkedList()
    for i in range(n):
        ll.insert(i)

    curr_index = 0
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
                t = n + t + 1
            curr_index = (curr_index + t) % ll.length()
    print(ll.get(curr_index))

if __name__ == '__main__':
    main()
