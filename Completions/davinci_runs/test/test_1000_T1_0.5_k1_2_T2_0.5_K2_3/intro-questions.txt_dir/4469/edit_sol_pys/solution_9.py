
import sys
import os
import heapq
import math

# fopen equivalent
abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")


class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_left(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_right(self, data):
        new_node = self.Node(data)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_left(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def remove_right(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

    def get_leftmost(self):
        if self.head:
            return self.head.data

    def get_rightmost(self):
        if self.tail:
            return self.tail.data

    def get_left_distance(self, data):
        distance = 0
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return distance
            distance += 1
            curr_node = curr_node.next
        return None

    def get_right_distance(self, data):
        distance = 0
        curr_node = self.tail
        while curr_node:
            if curr_node.data == data:
                return distance
            distance += 1
            curr_node = curr_node.prev
        return None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


def main():
    num_queries = int(sys.stdin.readline().strip())
    linked_list = LinkedList()
    for _ in range(num_queries):
        query = sys.stdin.readline().strip().split()
        if query[0] == "L":
            linked_list.insert_left(int(query[1]))
        elif query[0] == "R":
            linked_list.insert_right(int(query[1]))
        else:
            left_distance = linked_list.get_left_distance(int(query[1]))
            right_distance = linked_list.get_right_distance(int(query[1]))
            if left_distance is not None:
                print(left_distance)
            else:
                print(right_distance)


if __name__ == "__main__":
    main()
