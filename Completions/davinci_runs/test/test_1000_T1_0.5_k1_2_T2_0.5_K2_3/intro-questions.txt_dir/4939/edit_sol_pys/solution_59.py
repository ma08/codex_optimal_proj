"""
In this problem you will be given a list of commands that can be executed on a circular list.
Each command is either an integer or an undo command. An undo command will undo the previous command
if it was an integer command.
If the command was an undo command, nothing happens.
The integer command will move the current position of the list the specified amount of positions.
The list is circular, so if the current position is 5 and the command is -2, the new position will be 3.
If the current position is 5 and the command is 3, the new position will be 1.
After the list of commands, on the last line, there will be a single integer, the index that should be printed.
The list starts at position 0.
"""

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
    n, k = map(int, lines[0].split())
    commands = lines[1].split()

    ll = LinkedList()
    for i in range(n):
        ll.insert(i)

    curr_index = 0
    for i in range(k):
        command = commands[i]
        if command == "undo":
            undo = int(commands[i+1])
            for j in range(undo):
                ll.delete(curr_index)
            i += 1
            continue
        else:
            shift = int(command)
            if shift < 0:
                shift = n + shift
            curr_index = (curr_index + shift) % ll.length()
    print(ll.get(curr_index))

if __name__ == '__main__':
    main()
