

import sys
import heapq

class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.len = r - l
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.l < other.l

    def __eq__(self, other):
        return self.l == other.l

def build(segments):
    if len(segments) == 0:
        return None

    segments.sort()

    mid = len(segments) // 2
    node = segments[mid]

    node.left = build(segments[:mid])
    node.right = build(segments[mid+1:])

    return node

def get_max_len(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.len

    left_len = right_len = 0
    if root.left is not None:
        left_len = get_max_len(root.left)

    if root.right is not None:
        right_len = get_max_len(root.right)

    return max(left_len, right_len)

def solve(segments):
    root = build(segments)
    return get_max_len(root)

def main():
    n = int(input())

    segments = []
    for i in range(n):
        l, r = map(int, input().split(' '))
        segments.append(Node(l, r))

    print(solve(segments))

if __name__ == '__main__':
    main()